#!/usr/bin/env python3
"""fig_ultrawide_omega_zp versión SLIDE (lámina "El Barrido Completo").
Ω_zp(t) de las 44 simulaciones, color = índice canónico (colorbar continua
de σ), sin título ni anotaciones por curva — versión compacta y legible de
la ULTRAWIDE de 53×22 in (enstrofia_ultrawide.py, pipeline lab_offsetC).

Correr desde INFO/lab/lab_offsetC:
    cd ~/Documents/Grado/INFO/lab/lab_offsetC
    ../.venv/bin/python ~/Documents/Grado/REPO_GH/presentacion/scripts_slide/gen_ultrawide_slide.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd()))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.gridspec as gridspec

from config_khi import (
    BASE_DIR, ARCHIVO_DIAGNOSTICO, T_FILTRO,
    cargar_simulaciones_validas, asignar_indices_canonicos,
    construir_cmap_canonico,
)

OUT = Path.home() / "Documents/Grado/REPO_GH/presentacion/figures/fig_ultrawide_omega_zp_slide.pdf"

plt.rcParams.update({
    "text.usetex": False, "mathtext.fontset": "cm",
    "font.family": "serif",
    "font.serif": ["DejaVu Serif", "Computer Modern Roman"],
    "axes.labelsize": 19, "font.size": 15,
    "xtick.labelsize": 16, "ytick.labelsize": 16,
    "pdf.fonttype": 42,
})


def main():
    sims = cargar_simulaciones_validas(
        BASE_DIR, ARCHIVO_DIAGNOSTICO, T_FILTRO, cargar_curva=True)
    sigmas = [s['sigma'] for s in sims]
    idx = asignar_indices_canonicos(sigmas)
    n = len(sims)
    cmap, norm = construir_cmap_canonico(n)

    fig = plt.figure(figsize=(12.6, 6.6))
    gs = gridspec.GridSpec(1, 2, width_ratios=[46, 1], wspace=0.03)
    ax, cax = fig.add_subplot(gs[0]), fig.add_subplot(gs[1])

    for sim in sims:
        m = sim['omega_zp'] > 1e-15
        ax.semilogy(sim['t'][m], sim['omega_zp'][m],
                    color=cmap(norm(idx[sim['sigma']] - 1)),
                    lw=1.5, alpha=0.85)

    ax.set_xlabel(r"$t$")
    ax.set_ylabel(r"$\Omega_{zp}(t)$")
    ax.set_xlim(-0.6, 15)
    ax.grid(True, ls="--", alpha=0.35)

    sigma_por_idx = {idx[s]: s for s in sigmas}
    sm = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
    cb = fig.colorbar(sm, cax=cax)
    ticks = np.unique(np.linspace(1, n, 6).round().astype(int))
    cb.set_ticks(ticks - 1)
    cb.set_ticklabels([f"{sigma_por_idx[i]:.0f}" for i in ticks])
    cb.ax.tick_params(labelsize=15)
    cax.set_ylabel(r"$\sigma$", fontsize=19, rotation=0, labelpad=18)

    fig.tight_layout()
    fig.savefig(OUT, bbox_inches='tight')
    plt.close(fig)
    print("OK ->", OUT)


if __name__ == "__main__":
    main()
