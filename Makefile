DOCX = $(wildcard *.docx)
HTML = $(DOCX:.docx=.html)

%.html: %.docx
	pandoc -t html5 --extract-media=. $^ -o $@

html: $(HTML)
	cp -r media docs
	./macros.py

clean:
	rm -f *.html
	rm -rf media
	rm -rf docs/*
