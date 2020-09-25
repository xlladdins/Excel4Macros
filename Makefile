DOCX = $(wildcard *.docx)
HTML = $(DOCX:.docx=.html)

%.html: %.docx
	pandoc -t html5 --ascii --extract-media=. $^ -o $@

html: $(HTML)

clean:
	rm *.md
	rm *.html
	rm -rf media
