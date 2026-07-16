#!/usr/bin/env python3
"""setup_inicial_slide (P16): un solo PDF con 2 paneles apilados —
líneas de corriente sobre |V| (arriba) y ρ con contornos (abajo) —
de la CONDICIÓN INICIAL REAL (t=0) del run base, volcada por el clúster
(bundle_prompt_figs → INFO/lab/bundle_cluster_figs/run_base_init/).
Verificada contra el setup de la monografía: ρ centro=0.10, fuera=1.00,
v_y ∈ [-0.5, 0.5]. Estilo dark nativo de AVP.py; sin títulos internos.

Correr: INFO/lab/.venv/bin/python gen_setup_inicial_slide.py
"""
from pathlib import Path
import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt

DATA = Path.home() / "Documents/Grado/INFO/lab/bundle_cluster_figs/run_base_init"
OUT = Path.home() / "Documents/Grado/REPO_GH/presentacion/figures/setup_inicial_slide.pdf"

plt.style.use('dark_background')
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif", "Computer Modern Roman"],
    "mathtext.fontset": "cm",
    "axes.labelsize": 20, "font.size": 15,
    "xtick.labelsize": 16, "ytick.labelsize": 16,
    "figure.facecolor": "black", "axes.facecolor": "black",
    "savefig.facecolor": "black", "text.color": "white",
    "axes.edgecolor": "white", "xtick.color": "white",
    "ytick.color": "white", "pdf.fonttype": 42,
})

MAPA = 'inferno'
CONTORNOS = 18


def cargar(nombre):
    data = np.loadtxt(DATA / f"init_{nombre}.dat", usecols=(0, 1, 2))
    x_unq, y_unq = np.unique(data[:, 0]), np.unique(data[:, 1])
    xi = {v: i for i, v in enumerate(x_unq)}
    yi = {v: i for i, v in enumerate(y_unq)}
    Z = np.full((len(y_unq), len(x_unq)), np.nan)
    for xv, yv, zv in data:
        Z[yi[yv], xi[xv]] = zv
    X, Y = np.meshgrid(x_unq, y_unq)
    return X, Y, Z


def main():
    X, Y, vx = cargar("vx")
    _, _, vy = cargar("vy")
    _, _, rho = cargar("rho")

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9.0, 8.6), sharex=True)

    # ── panel 1: |V| + líneas de corriente ──────────────────────────
    mag = np.sqrt(vx ** 2 + vy ** 2)
    im1 = ax1.imshow(mag, extent=[-1, 1, 0, 1],
                     origin='lower', cmap=MAPA, aspect='auto',
                     interpolation='bilinear')
    lw = np.clip(1.8 * (mag / mag.max()), 0.3, 2.5)
    ax1.streamplot(X, Y, vx, vy, color='white', density=1.4,
                   linewidth=lw, arrowsize=0.9)
    ax1.set_xlim(-1, 1); ax1.set_ylim(0, 1)
    ax1.set_ylabel(r"$y$")
    cb1 = plt.colorbar(im1, ax=ax1, fraction=0.03, pad=0.02)
    cb1.set_label(r"$|\mathbf{V}|$", fontsize=19)
    cb1.outline.set_visible(False)
    cb1.set_ticks(np.round(np.linspace(mag.min(), mag.max(), 4), 2))
    cb1.ax.tick_params(labelsize=15)

    # ── panel 2: ρ + contornos ──────────────────────────────────────
    im2 = ax2.imshow(rho, extent=[-1, 1, 0, 1],
                     origin='lower', cmap=MAPA, aspect='auto',
                     interpolation='bilinear')
    niveles = np.linspace(rho.min(), rho.max(), CONTORNOS)
    ax2.contour(X, Y, rho, levels=niveles, colors='white',
                linewidths=0.3, alpha=0.25)
    ax2.set_xlim(-1, 1); ax2.set_ylim(0, 1)
    ax2.set_xlabel(r"$x$"); ax2.set_ylabel(r"$y$")
    cb2 = plt.colorbar(im2, ax=ax2, fraction=0.03, pad=0.02)
    cb2.set_label(r"$\rho$", fontsize=19)
    cb2.outline.set_visible(False)
    cb2.set_ticks([0.1, 0.4, 0.7, 1.0])
    cb2.ax.tick_params(labelsize=15)

    fig.tight_layout()
    fig.savefig(OUT, bbox_inches='tight', dpi=240)
    plt.close(fig)
    print("OK ->", OUT)


if __name__ == "__main__":
    main()
