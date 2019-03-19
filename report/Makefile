NAME := report
CC := pdflatex
REF := bibtex

all: report

report:
	${CC} ${NAME}
	${REF} ${NAME}
	${CC} ${NAME}
	${CC} ${NAME}

clean:
	find . -regextype posix-awk -regex "(.*.pdf|.*.aux|.*.bbl|.*.blg|.*.log)" -type f -delete
