#!/usr/bin/env python3
"""fig_campB_omegamax_theta versión SLIDE (P25). Picos de la enstrofía
integrada (Ω_zp^int) y puntual (Ω_zp^max) vs θ, campaña B, ambas σ.
Mismos datos (DATOS_LIMPIOS/B_orientacion_yz); títulos cortos, fuentes grandes.

Correr: INFO/lab/.venv/bin/python gen_omegamax_theta_slide.py
"""
import os, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

CLEAN = os.path.expanduser("~/Documents/Grado/INFO/lab/analisis_campanas_B_PRELIM/resultados_condensados_6000_vs_10000/ANALISIS_LIMPIO_FINAL/DATOS_LIMPIOS")
OUT = os.path.expanduser("~/Documents/Grado/REPO_GH/presentacion/figures/fig_campB_omegamax_theta_slide.pdf")

plt.rcParams.update({
    "font.family": "serif", "mathtext.fontset": "cm",
    # (ronda 3) fuentes subidas: la figura se muestra a ~media lámina y los
    # números quedaban chicos al reescalar; agrandarlas en el origen las hace
    # legibles tras el downscale del deck.
    "axes.labelsize": 28, "axes.titlesize": 26, "font.size": 20,
    "legend.fontsize": 21, "xtick.labelsize": 23, "ytick.labelsize": 23,
    "pdf.fonttype": 42,
})

ANG = {'00': 0.0, '06': 5.7, '30': 30.0, '45': 45.0, '60': 60.0, '90': 90.0}
STYLE = {'sigma6000':  dict(color='tab:red',  marker='o', label=r'$\sigma=6000$'),
         'sigma10000': dict(color='tab:blue', marker='s', label=r'$\sigma=10000$')}


def picos(sig, archivo):
    d = os.path.join(CLEAN, 'B_orientacion_yz', sig)
    ths, pks = [], []
    for ak, th in ANG.items():
        runs = [r for r in os.listdir(d) if f'th{ak}' in r]
        if not runs:
            continue
        p = os.path.join(d, runs[0], 'data_global', archivo)
        dat = np.loadtxt(p)
        ths.append(th)
        pks.append(dat[:, 2].max())
    return np.array(ths), np.array(pks)


def main():
    fig, axs = plt.subplots(1, 2, figsize=(15, 6.2))
    paneles = [
        ('2d_data_Omega_zp_int.dat', r'Integrada $\Omega_{zp}^{\rm int}$', '-'),
        ('2d_data_Omega_zp_max.dat', r'Puntual $\Omega_{zp}^{\rm max}$', '--'),
    ]
    for ax, (arch, titulo, ls) in zip(axs, paneles):
        for sig, st in STYLE.items():
            th, pk = picos(sig, arch)
            ax.plot(th, pk, ls=ls, lw=2.6, ms=11, **st)
        ax.set_xlabel(r"$\theta$ ($^\circ$)")
        ax.set_ylabel(r"$\Omega_{zp}$ (pico temporal)")
        ax.set_title(titulo, pad=10)
        ax.grid(alpha=0.35, ls='--')
        ax.legend(framealpha=0.9)
    fig.tight_layout()
    fig.savefig(OUT, dpi=160, bbox_inches='tight')
    plt.close(fig)
    print("OK ->", OUT)


if __name__ == "__main__":
    main()
