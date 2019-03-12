CC := pdflatex

all: report

report:
	${CC} report.tex

clean:
	find . -regextype posix-awk -regex "(.*.pdf|.*.aux|.*.bib|.*.log)" -type f -delete
