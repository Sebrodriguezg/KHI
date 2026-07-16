#!/usr/bin/env python3
"""fig_campB_ekin_emag_scatter versión SLIDE (P26): 1 fila × 3 paneles
(θ = 0°, 45°, 90°) — la progresión que cuenta la historia; los 6 paneles
completos quedan en la monografía.

Mismos datos (DATOS_LIMPIOS/B_orientacion_yz): parte oscilatoria de
E_kin y E_mag (residuo tras restar la tendencia lenta savgol). NO se
imprime r por panel para no duplicar cifras de la monografía (el rango
r ≈ −0.6 a −0.9 se cita en la lámina); la figura muestra la anti-
correlación cualitativa.

Correr: INFO/lab/.venv/bin/python gen_ekin_emag_scatter_slide.py
"""
import os, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

CLEAN = os.path.expanduser("~/Documents/Grado/INFO/lab/analisis_campanas_B_PRELIM/resultados_condensados_6000_vs_10000/ANALISIS_LIMPIO_FINAL/DATOS_LIMPIOS")
OUT = os.path.expanduser("~/Documents/Grado/REPO_GH/presentacion/figures/fig_campB_ekin_emag_scatter_slide.pdf")

plt.rcParams.update({
    "font.family": "serif", "mathtext.fontset": "cm",
    "axes.labelsize": 15, "axes.titlesize": 16, "font.size": 12,
    "legend.fontsize": 12, "xtick.labelsize": 11, "ytick.labelsize": 11,
    "pdf.fonttype": 42,
})

ANGS = [('00', r'$\theta=0^\circ$'), ('45', r'$\theta=45^\circ$'),
        ('90', r'$\theta=90^\circ$')]
STYLE = {'sigma6000':  dict(color='tab:red',  label=r'$\sigma=6000$'),
         'sigma10000': dict(color='tab:blue', label=r'$\sigma=10000$')}


T_MIN = 1.0   # descarta el transitorio inicial (igual que la figura original)


def cargar(sig, ak):
    d = os.path.join(CLEAN, 'B_orientacion_yz', sig)
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
    fig, axs = plt.subplots(1, 3, figsize=(11.0, 3.9))
    for ax, (ak, tlab) in zip(axs, ANGS):
        for sig, st in STYLE.items():
            K, E = cargar(sig, ak)
            ax.scatter(osc(K), osc(E), s=26, alpha=0.65,
                       edgecolors='none', **st)
        ax.axhline(0, color='k', ls=':', lw=1.0)
        ax.axvline(0, color='k', ls=':', lw=1.0)
        ax.set_title(tlab, pad=10)
        ax.set_xlabel(r"$E'_{\rm kin}$ (osc.)")
        ax.ticklabel_format(style='sci', scilimits=(-2, 2))
        ax.xaxis.get_offset_text().set_fontsize(12)
        ax.yaxis.get_offset_text().set_fontsize(12)
    axs[0].set_ylabel(r"$E'_{\rm mag}$ (osc.)")
    axs[0].legend(loc='upper right', framealpha=0.9)
    fig.tight_layout()
    fig.savefig(OUT, dpi=160, bbox_inches='tight')
    plt.close(fig)
    print("OK ->", OUT)


if __name__ == "__main__":
    main()
