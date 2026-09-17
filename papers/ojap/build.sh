#!/usr/bin/env bash
# Compila el esqueleto OJAp (openjournal.cls -> revtex4-1 -> natbib/bibtex).
set -e
cd "$(dirname "$0")"
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main || echo ">> bibtex se quejo (normal mientras no haya citas reales)"
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
echo
echo ">> main.pdf listo."
