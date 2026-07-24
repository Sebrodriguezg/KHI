#!/usr/bin/env python3
"""Snapshot único de ρ(x,y) para la lámina S3 (overlay paso 2, ronda 2):
σ=1000 (s3) en t=8 — plena fase de enrollamiento, el vórtice KH clásico
(a σ=10⁴ en t=8 ya hay fragmentación y es menos didáctico).
Estilo blanco/inferno de la monografía, sin ticks.

Correr: INFO/lab/.venv/bin/python gen_khi_snapshot_slide.py
"""
import os
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

DATA = os.path.expanduser("~/Documents/Grado/INFO/lab/bundle_cluster_figs/conductividad")
OUT = os.path.expanduser(
    "~/Documents/Grado/REPO_GH/presentacion/figures/khi_rho_snapshot_slide.pdf")

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif", "Computer Modern Roman"],
    "mathtext.fontset": "cm",
    "figure.facecolor": "white", "axes.facecolor": "white",
    "savefig.facecolor": "white", "pdf.fonttype": 42,
})


def grid(path):
    d = np.loadtxt(path, usecols=(0, 1, 2))
    xu, yu = np.unique(d[:, 0]), np.unique(d[:, 1])
    xi = {v: i for i, v in enumerate(xu)}
    yi = {v: i for i, v in enumerate(yu)}
    Z = np.full((len(yu), len(xu)), np.nan)
    for xv, yv, zv in d:
        Z[yi[yv], xi[xv]] = zv
    X, Y = np.meshgrid(xu, yu)
    return X, Y, Z


def main():
    frame = 8
    for nm in (f"2d_data_rho_{frame:04d}.dat", f"2d_data_rhoo_{frame:04d}.dat"):
        p = os.path.join(DATA, "s3", nm)
        if os.path.exists(p):
            X, Y, Z = grid(p)
            break
    else:
        raise FileNotFoundError("frame 8 de s4")

    fig, ax = plt.subplots(figsize=(4.6, 4.6))
    ax.imshow(Z, extent=[X.min(), X.max(), Y.min(), Y.max()],
              origin="lower", cmap="inferno", aspect="auto",
              interpolation="bilinear")
    ax.contour(X, Y, Z, levels=16, colors="k", linewidths=0.3, alpha=0.28)
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_linewidth(0.8)
    fig.tight_layout(pad=0.1)
    fig.savefig(OUT, bbox_inches="tight", dpi=240)
    plt.close(fig)
    print("OK ->", OUT)


if __name__ == "__main__":
    main()
