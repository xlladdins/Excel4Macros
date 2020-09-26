DOCX = $(wildcard *.docx)
HTML = $(DOCX:.docx=.html)

%.html: %.docx
	pandoc -t html5 --standalone --extract-media=docs --metadata title="none" $^ -o $@

html: $(HTML)

clean:
	rm -f *.html
	rm -rf media
	rm -rf docs/*
