#!/usr/bin/python3

import glob
import lxml.etree as etree
import lxml.html
import re

# macro name to id map
macro_id = dict()

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

def split_html(html):
	'''create files based on <h1> sections'''
	id = ''
	tree = lxml.html.parse(html)
	for x in tree.xpath('//*[count(ancestor::*) = 2]'):
		if x.tag == 'h1' and x.text:
			if len(id) > 1:
				of.write(footer())
				of.close()
			id = x.attrib['id']
			tx = x.text

			#!!! split text on , to get all functons
			for m in tx.split(", "):
				macro_id[m] = id

			if len(id) > 1:
				of = open(f'docs/{id}.html', 'w')
				of.write(header(tx))

		if len(id) > 1:
			line = etree.tostring(x, encoding="unicode", method="html")
			if x.tag == 'h1':
				line = line.replace(x.text, x.text + " macro")
			of.write(line)

	if len(id) > 1:
		of.write(footer())
		of.close()

for html in glob.glob('*.html'):
	split_html(html)

# Insert references
for html in glob.glob('docs/*.html'):
	print(html)
