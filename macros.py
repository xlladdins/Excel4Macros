#!/usr/bin/python3

import glob
import lxml.etree as etree
import lxml.html
import re
from subprocess import call

# id to text map
id_text = dict()

def header(title):
	return f'''<html>
<head>
<title>{title}</title>
<link rel="stylesheet" href="../macros.css">
</head>
<body>
'''

def footer():
	return f'''
</body>
</html>
'''

# list of lines in file
def lines_file(file):
	with open(file) as f:
		return f.readlines()

# split lines based on h1
def split_lines(lines):
	h1 = dict()
	id = None
	pat = re.compile(r'<h1\s+id="(?P<id>\S+)">(?P<text>.+)</h1>')
	for line in lines:
		m = re.match(pat, line)
		if m and not re.match(r'.*syntax.*', m.group('id')):
			id = m.group('id')
			text = m.group('text')
			if len(id) > 1:
				h1[id] = []
				id_text[id] = text
		if id and len(id) > 1:
			h1[id].append(line)

	return h1

# map h1 id to lines and populate id_text
pages = dict()
for html in glob.glob('*.html'):
	pages.update(split_lines(lines_file(html)))

# map macro names to id
macro_id = dict()
for id, text in id_text.items():
	for m in text.split(", "):
		macro_id[m] = id

#print(macro_id)

# create html files for each id
for id, lines in pages.items():
	with open(f'docs/{id}.html', 'w') as of:
		related = False
		of.write(header(id))
		lines[0] = re.sub(r'</h1>', " macro</h1>", lines[0])
		for line in lines:
			if re.match(r'.*Related Functions.*', line):
				related = True
			# add links for macros
			if related:
				m = re.match(r'^<p>([A-Z\.]{2,})(\s+)(.*)$', line)
				if m:
					macro = m[1]
					if macro == "GETBAR": # fix up!!!
						macro = "GET.BAR"
					line = f'<p><a href="{macro_id[macro]}.html">{m[1]}</a>{m[2]}{m[3]}'
			if not re.match(r'^<p>Return to', line):
				of.write(line)
		of.write(footer())

# index
with open('docs/index.html', 'w') as index:
	# first letter, list of macros
	macros = dict()
	for m in macro_id:
		macros[m[0]] = []
	for m in macro_id:
		macros[m[0]].append(m)

	index.write(header("Excel4Macros"))

	index.write("<h1>Excel4Macros</h1>\n")
	nav = [f'<a href="#{k}">{k}</a>' for k in macros.keys()]
	index.write("<p>" + ' | '.join(nav) + "</p>\n")
	for k, v in macros.items():
		vs =  [f'<a href="{macro_id[i]}.html">{i}</a>' for i in v]
		index.write(f'<p id="{k}">' + "  ".join(vs) + "</p>\n")
	
	index.write(footer())
