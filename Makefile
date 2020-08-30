DOCX = $(wildcard *.docx)
MD = $(DOCX:.docx=.md)

%.md: %.docx
	pandoc -t gfm --ascii --extract-media=. $^ -o $@

all: $(MD)
	(cd docs; ../macros.awk ../Excel4Macros*.md)

clean:
	rm *.md
	rm -rf media
