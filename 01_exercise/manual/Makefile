pdf:
	pdflatex -shell-escape intro_sql.tex

spelling:
	hunspell -l -t -i utf-8 intro_sql.tex

clean:
	rm -f *.aux
	rm -f *.log
	rm -f *.out
	rm -f *.toc
	rm -rf _minted-*/
	rm -f tmp.markdown
	rm -f tmp.tex
