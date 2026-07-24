#!/usr/bin/env python3
"""Figura didáctica para S11 "El Observable" (ronda 2, opción c):
Ω_zp(t) del run ideal σ=10⁴ en escala log con la ventana canónica de ajuste
[2.4, 3.4] sombreada y la recta ajustada (pendiente 2γ_KHI) marcada.
Conecta la definición de la enstrofía con CÓMO se mide γ.

Correr desde INFO/lab/lab_offsetC:
    cd ~/Documents/Grado/INFO/lab/lab_offsetC
    ../.venv/bin/python ~/Documents/Grado/REPO_GH/presentacion/scripts_slide/gen_enstrofia_observable_slide.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd()))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from config_khi import (
    BASE_DIR, ARCHIVO_DIAGNOSTICO, T_FILTRO, T_FIT_MIN, T_FIT_MAX,
    cargar_simulaciones_validas,
)

SIGMA_REF = 10000
OUT = Path.home() / "Documents/Grado/REPO_GH/presentacion/figures/fig_enstrofia_observable_slide.pdf"

plt.rcParams.update({
    "text.usetex": False, "mathtext.fontset": "cm",
    "font.family": "serif",
    "font.serif": ["DejaVu Serif", "Computer Modern Roman"],
    "axes.labelsize": 12, "font.size": 10,
    "xtick.labelsize": 10, "ytick.labelsize": 10,
    "figure.facecolor": "white", "savefig.facecolor": "white",
    "pdf.fonttype": 42,
})


def main():
    sims = cargar_simulaciones_validas(
        BASE_DIR, ARCHIVO_DIAGNOSTICO, T_FILTRO, cargar_curva=True)
    ref = next(s for s in sims if s['sigma'] == SIGMA_REF)
    t, o = ref['t'], ref['omega_zp']
    m = o > 1e-15

    # ajuste en la ventana canónica: ln Ω = a + 2γ t
    mw = m & (t >= T_FIT_MIN) & (t <= T_FIT_MAX)
    p = np.polyfit(t[mw], np.log(o[mw]), 1)
    gamma = 0.5 * p[0]
    print(f"σ={SIGMA_REF}: pendiente={p[0]:.3f}  ->  γ_KHI={gamma:.3f}")

    fig, ax = plt.subplots(figsize=(8.2, 2.2))
    ax.semilogy(t[m], o[m], color="#1565c0", lw=2.0,
                label=fr"$\Omega_{{zp}}(t)$,  $\sigma=10^4$")
    ax.axvspan(T_FIT_MIN, T_FIT_MAX, color="#2e7d32", alpha=0.15)

    tt = np.linspace(T_FIT_MIN - 0.9, T_FIT_MAX + 0.9, 50)
    ax.semilogy(tt, np.exp(np.polyval(p, tt)), "--", color="#c62828", lw=1.6,
                label=fr"pendiente $=2\gamma_{{\rm KHI}}$"
                      fr"  ($\gamma={gamma:.2f}$)")

    ax.text(0.5 * (T_FIT_MIN + T_FIT_MAX), 200, "ventana\ncanónica",
            fontsize=8.5, color="#2e7d32", ha="center", va="top",
            fontweight="bold")

    ax.set_xlim(0, 15)
    ax.set_ylim(1, 400)
    ax.set_xlabel(r"$t$  (unidades de código)")
    ax.set_ylabel(r"$\Omega_{zp}(t)$")
    ax.grid(True, ls="--", alpha=0.35)
    ax.legend(fontsize=8.5, loc="lower right", framealpha=0.9)

    fig.tight_layout()
    fig.savefig(OUT, bbox_inches="tight")
    plt.close(fig)
    print("OK ->", OUT)


if __name__ == "__main__":
    main()
