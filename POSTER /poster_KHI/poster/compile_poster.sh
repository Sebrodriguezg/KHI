#!/usr/bin/env bash
set -eu # strict config (non-zero returns and unset vars halt script)

# Define functions

line(){
    echo "==============================================================================="
       }

compile_texdoc(){
    tex_filename="$1"
    line
    echo " Compiling ${tex_filename}.tex"
    line
    pdflatex ${tex_filename}.tex
    pdflatex ${tex_filename}.tex
    pdflatex ${tex_filename}.tex
    line
}

# Here start sh bash

line
echo "- Compiling"
compile_texdoc "poster_portrait" 

line
echo "- Cleaning"
find . -name "*.aux" -delete
find . -name "*.out" -delete
find . -name "*.log" -delete
find . -name "*.toc" -delete
find . -name "*.nav" -delete
find . -name "*.snm" -delete
find . -name "*.bbl" -delete
find . -name "*.blg" -delete
find . -name "*.spl" -delete

line
echo "- Success, have a good day¡"
line
