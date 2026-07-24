#!/usr/bin/env python3
"""fig_campC_ekin_emag_scatter versión SLIDE (lámina Campaña C): 2 paneles
apilados (θ=60°, 90°), donde la anti-correlación es más fuerte (r≈-0.98 en
la monografía). Parte oscilatoria igual que la versión B slide (savgol,
t≥1); sin r por panel (la lámina cita el valor de la monografía).

Correr: INFO/lab/.venv/bin/python gen_campC_scatter_slide.py
"""
import os, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

CLEAN = os.path.expanduser("~/Documents/Grado/INFO/lab/analisis_campanas_B_PRELIM/resultados_condensados_6000_vs_10000/ANALISIS_LIMPIO_FINAL/DATOS_LIMPIOS")
OUT = os.path.expanduser("~/Documents/Grado/REPO_GH/presentacion/figures/fig_campC_ekin_emag_scatter_slide.pdf")

plt.rcParams.update({
    "font.family": "serif", "mathtext.fontset": "cm",
    "axes.labelsize": 19, "axes.titlesize": 21, "font.size": 15,
    "legend.fontsize": 15, "xtick.labelsize": 14, "ytick.labelsize": 14,
    "pdf.fonttype": 42,
})

ANGS = [('60', r'$\theta=60^\circ$'), ('90', r'$\theta=90^\circ$')]
STYLE = {'sigma6000':  dict(color='tab:red',  label=r'$\sigma=6000$'),
         'sigma10000': dict(color='tab:blue', label=r'$\sigma=10000$')}
T_MIN = 1.0


def cargar(sig, ak):
    d = os.path.join(CLEAN, 'C_orientacion_xz', sig)
    run = [r for r in os.listdir(d) if f'th{ak}' in r][0]
    g = os.path.join(d, run, 'data_global')
    dk = np.loadtxt(os.path.join(g, '2d_data_ekin_r_integral_vol.dat'))
    de = np.loadtxt(os.path.join(g, '2d_data_emag_integral_vol.dat'))
    m = dk[:, 1] >= T_MIN
    return dk[m, 2], de[m, 2]


def osc(y, win=21, order=3):
    w = min(win, (len(y) // 2) * 2 - 1)
    if w % 2 == 0:
        w += 1
    return y - savgol_filter(y, w, order)


def main():
    # (ronda 3) paneles HORIZONTALES (θ=60° | θ=90°) para agrandar la figura
    fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.8), sharey=True)
    for ax, (ak, tlab) in zip(axs, ANGS):
        for sig, st in STYLE.items():
            K, E = cargar(sig, ak)
            ax.scatter(osc(K), osc(E), s=22, alpha=0.65, edgecolors='none', **st)
        ax.axhline(0, color='k', ls=':', lw=1.0)
        ax.axvline(0, color='k', ls=':', lw=1.0)
        ax.set_title(tlab, pad=8)
        ax.set_xlabel(r"$E'_{\rm kin}$ (osc.)")
        ax.ticklabel_format(style='sci', scilimits=(-2, 2))
        ax.xaxis.get_offset_text().set_fontsize(11)
        ax.yaxis.get_offset_text().set_fontsize(11)
    axs[0].set_ylabel(r"$E'_{\rm mag}$ (osc.)")
    axs[0].legend(loc='upper right', framealpha=0.9)
    fig.tight_layout()
    fig.savefig(OUT, dpi=160, bbox_inches='tight')
    plt.close(fig)
    print("OK ->", OUT)


if __name__ == "__main__":
    main()
