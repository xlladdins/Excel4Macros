#!/usr/bin/python3

import glob
import lxml.etree as etree
import lxml.html
#from lxml import html

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
	#print(tree)
	for x in tree.xpath('//*[count(ancestor::*) = 2]'):
		if x.tag == 'h1' and x.text:
			if len(id) > 1:
				of.write(footer())
				of.close()
				print(f'closing docs/{id}.html')
			id = x.attrib['id']
			tx = x.text
			#!!! split text on , to get all functons
			if len(id) > 1:
				of = open(f'docs/{id}.html', 'w')
				of.write(header(tx))

		if len(id) > 1:
			#print('---')
			#etree.dump(x)
			#print('---')
			#print(repr(x))
			of.write(etree.tostring(x, encoding="unicode", method="html"))
			#print(etree.tostring(x, encoding="unicode", method="html"))

	if len(id) > 1:
		of.write(footer())
		of.close()

for html in glob.glob('*.html'):
	split_html(html)
