#!/usr/bin/env bash
# Compila el esqueleto MNRAS: pdflatex + bibtex + pdflatex x2 (natbib, no biber).
set -e
cd "$(dirname "$0")"
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main || echo ">> bibtex se quejo (normal mientras no haya citas reales)"
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
echo
echo ">> main.pdf listo. Avisos que conviene mirar:"
grep -c "Citation.*undefined"  main.log || true
grep -n  "Overfull \\\\hbox"   main.log | head -5 || true
