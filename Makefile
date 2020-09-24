DOCX = $(wildcard *.docx)
MKDN = $(DOCX:.docx=.md)
HTML = $(DOCX:.docx=.html)

%.md: %.docx
	pandoc -t gfm --ascii --extract-media=. $^ -o $@

%.html: %.docx
	pandoc -t html5 --ascii --extract-media=. $^ -o $@

mkdn: $(MKDN)
	(cd docs; ../macros.awk ../Excel4Macros*.md)

html: $(HTML)

clean:
	rm *.md
	rm *.html
	rm -rf media
