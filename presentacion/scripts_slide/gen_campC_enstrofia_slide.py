#!/usr/bin/env python3
"""fig_campC_enstrofia versión SLIDE (lámina Campaña C). Ω_zp(t) por ángulo
θ del plano x-z, 2 paneles apilados (σ=6000 arriba, σ=10000 abajo).
Mismos datos que la monografía (DATOS_LIMPIOS/C_orientacion_xz).

Correr: INFO/lab/.venv/bin/python gen_campC_enstrofia_slide.py
"""
import os, glob, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

CLEAN = os.path.expanduser("~/Documents/Grado/INFO/lab/analisis_campanas_B_PRELIM/resultados_condensados_6000_vs_10000/ANALISIS_LIMPIO_FINAL/DATOS_LIMPIOS")
OUT = os.path.expanduser("~/Documents/Grado/REPO_GH/presentacion/figures/fig_campC_enstrofia_slide.pdf")

plt.rcParams.update({
    "font.family": "serif", "mathtext.fontset": "cm",
    "axes.labelsize": 21, "axes.titlesize": 21, "font.size": 16,
    "legend.fontsize": 16, "xtick.labelsize": 17, "ytick.labelsize": 17,
    "pdf.fonttype": 42,
})


def load(p):
    try:
        d = np.loadtxt(p)
        return (d[:, 1], d[:, 2]) if d.ndim == 2 and len(d) > 2 else (None, None)
    except Exception:
        return None, None


def thlbl(nm):
    ang = nm.split("_th")[-1]
    return r"$\theta=5.7^\circ$" if ang == "06" else rf"$\theta={int(ang)}^\circ$"


def main():
    # (ronda 3) paneles HORIZONTALES (σ=6000 | σ=10000) para agrandar la figura
    fig, axs = plt.subplots(1, 2, figsize=(14.0, 5.2), sharey=True)
    for ax, (sg, cfl) in zip(axs, [("sigma6000", "0.04"), ("sigma10000", "0.02")]):
        for r in sorted(glob.glob(os.path.join(CLEAN, "C_orientacion_xz", sg, "run_*"))):
            nm = os.path.basename(r).replace("run_", "")
            t, o = load(os.path.join(r, "data_global", "2d_data_Omega_zp_int.dat"))
            if t is None:
                continue
            ax.semilogy(t, o, lw=2.2, label=thlbl(nm))
        ax.set_xlabel(r"$t$")
        ax.grid(alpha=0.3)
        ax.set_title(rf"$\sigma={sg.replace('sigma','')}$ (CFL={cfl})", pad=8)
    axs[0].set_ylabel(r"$\Omega_{zp}$")
    axs[0].legend(loc="lower right", ncol=2, framealpha=0.9)
    fig.tight_layout()
    fig.savefig(OUT, dpi=160, bbox_inches='tight')
    plt.close(fig)
    print("OK ->", OUT)


if __name__ == "__main__":
    main()
