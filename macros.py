#!/usr/bin/python3

import glob
import lxml.etree as etree
import lxml.html
import re
from subprocess import call


def header(title):
	return f'''<html>
<head>
<title>{title}</title>
<link rel="stylesheet" type="text/css" href="css/macros.css"/>
</head>
<body>
'''

def footer():
	return f'''
</body>
</html>
'''

# id to text map
id_text = dict()
# id to description map
id_desc = dict()

# list of lines in file
def lines_file(file):
	with open(file) as f:
		return f.readlines()

# split lines based on h1
def split_lines(lines):
	h1 = dict()
	id = None
	desc = False
	pat = re.compile(r'<h1\s+id="(?P<id>\S+)">(?P<text>.+)</h1>')
	for line in lines:
		m = re.match(pat, line)
		if m and not re.match(r'.*syntax.*', m.group('id')):
			desc = True
			id = m.group('id')
			text = m.group('text')
			if len(id) > 1:
				h1[id] = [line]
				id_text[id] = text
		elif id and len(id) > 1:
			if desc:
				m = re.match(r'<p>([^\.]*)\.', line)
				if m:
					id_desc[id] = m.group(1)
				desc = False
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
			if re.match(r'^<p>Return to', line):
				of.write('<p>Return to <a href="index.html">index</a></p>\n')
			else:
				of.write(line)
		of.write(footer())

# index
with open('docs/index.html', 'w') as index:
	index.write(header("Excel4Macros"))

	index.write("<h1>EXCEL4MACROS</h1>\n")
	# first letter, list of macros
	macros = dict()
	for m in macro_id:
		macros[m[0]] = []

	nav = [f'<a href="#{k}">{k}</a>' for k in macros.keys()]
	index.write("<nav><p>" + ' | '.join(nav) + "</p></nav>\n")
	index.write('<table id="macros">\n<tr><th>Macro</th><th>Description</th></tr>\n')
	A = "A"
	for k in id_desc:
		text = id_text[k]
		if A == text[0]:
			id = f' id="{A}"'
		else:
			id = ""
			A = text[0]
		index.write(f'<tr{id}><td><a href="{k}.html">{text}</a></td><td>{id_desc[k]}</td</tr>\n')
	index.write("</table>\n")
	
	index.write(footer())
