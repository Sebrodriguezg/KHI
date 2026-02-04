reset
set terminal epslatex 8 standalone color colortext size 5.6, 3.6 header  "\\newcommand{\\lr}[0]{\\large}\n\\newcommand{\\nm}[0]{\\normalsize}\n\\newcommand{\\hg}[0]{\\Huge}" 
set output 'dispersion_graph.tex'
set style line 1 lc rgb '#8b1a0e' pt 6 ps 1 lt 1 lw 2 # --- red
set style line 2 lc rgb '#5e9c36' pt 6 ps 1 lt 1 lw 2 # --- green
set linestyle 3  lt 33 pt 33  ps 0.7 lc rgb "#f46d43"   lw 0.5
set linestyle 4  lt 44 pt 44  ps 0.7 lc rgb "#fdae61"   lw 0.5
set linestyle 5  lt 55 pt 55  ps 0.7 lc rgb "#fee08b"   lw 0.5
set linestyle 6  lt 66 pt 66  ps 0.7 lc rgb "#e6f598"   lw 0.5
set linestyle 7  lt 77 pt 77  ps 0.7 lc rgb "#abdda4"   lw 0.5
set linestyle 8  lt 88 pt 88  ps 0.7 lc rgb "#66c2a5"   lw 0.5
set linestyle 9  lt 99 pt 133  ps 0.7 lc rgb "#006837"   lw 0.5
set linestyle 10  lt 99 pt 100  ps 0.7 lc rgb "cyan"     lw 0.5
set linestyle 11  lt 99 pt 111  ps 0.7 lc rgb "#3288bd"  lw 0.5
set linestyle 12  lt 99 pt 122  ps 0.7 lc rgb "#5e4fa2"  lw 0.5
set linestyle 13  lt 99 pt 99   ps 0.7 lc rgb "#ff3336"  lw 0.5

set style line 020 lt 0 lc rgb "gray" lw 0.5

show style line

set grid back  ls 020

set mxtics 5
set mytics 5

set format  y '\large %g'
set format  x '\large %g'

set xlabel '\hg $l/a$' offset 0,0
set ylabel '\hg $\gamma$' offset 1,0 rotate by 0
set title '\hg tasas de crecimiento ($\gamma$) vs separacion lineas corriente ($l$)'

set key top right

plot   'growth_data.dat' u ($1):($2) title '\lr $v_{A} = 0.5$'   w lp ls 1

set output # finish the current output file
system('latex dispersion_graph.tex && dvips dispersion_graph.dvi && ps2pdf dispersion_graph.ps')