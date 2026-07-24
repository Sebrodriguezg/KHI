#!/usr/bin/env python3
"""fig_conductividad_rho_collage versión SLIDE (P18): collage 3×3 de ρ(x,y),
filas = σ (100 resistiva / 1000 / 10⁴ ideal), columnas = t (3, 8, 14) —
MISMOS runs, frames y estilo blanco/inferno que la figura de la monografía
(render_collages_2D.py del clúster; datos en
INFO/lab/bundle_cluster_figs/conductividad/{s2,s3,s4}).

Cambios versión slide (auditoría, lámina cualitativa): SIN título interno,
SIN ticks ni números de eje; rótulos de fila/columna grandes; colorbar fina
con 4 ticks grandes.

Correr: INFO/lab/.venv/bin/python gen_conductividad_collage_slide.py
"""
import os
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

DATA = os.path.expanduser("~/Documents/Grado/INFO/lab/bundle_cluster_figs/conductividad")
OUT = os.path.expanduser("~/Documents/Grado/REPO_GH/presentacion/figures/fig_conductividad_rho_collage_slide.pdf")

CMAP, CONT = "inferno", 16
FILAS = [(r"$\sigma=100$" + "\n(resistiva)", "s2"),
         (r"$\sigma=1000$", "s3"),
         (r"$\sigma=10^4$" + "\n(ideal)", "s4")]
TIEMPOS = [3, 8, 14]
# Ronda 2 (obs. del profesor): encabezado de columna = fase dinámica
# (t en unidades de código; fases definidas sobre el régimen ideal)
FASES = ["Fase lineal", "Pico", "Turbulenta"]

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


def load_rho(s, frame):
    for nm in (f"2d_data_rho_{frame:04d}.dat", f"2d_data_rhoo_{frame:04d}.dat"):
        p = os.path.join(DATA, s, nm)
        if os.path.exists(p):
            return grid(p)
    raise FileNotFoundError(f"{s} frame {frame}")


def main():
    datos, vmin, vmax = {}, np.inf, -np.inf
    for i, (_, s) in enumerate(FILAS):
        for j, t in enumerate(TIEMPOS):
            r = load_rho(s, t)
            datos[(i, j)] = r
            vmin = min(vmin, np.nanmin(r[2]))
            vmax = max(vmax, np.nanmax(r[2]))

    fig, axs = plt.subplots(3, 3, figsize=(13.2, 8.6))
    im = None
    for i, (lab, _) in enumerate(FILAS):
        for j, t in enumerate(TIEMPOS):
            ax = axs[i][j]
            X, Y, Z = datos[(i, j)]
            im = ax.imshow(Z, extent=[X.min(), X.max(), Y.min(), Y.max()],
                           origin="lower", cmap=CMAP, aspect="auto",
                           interpolation="bilinear", vmin=vmin, vmax=vmax)
            ax.contour(X, Y, Z, levels=np.linspace(vmin, vmax, CONT),
                       colors="k", linewidths=0.3, alpha=0.28)
            ax.set_xticks([]); ax.set_yticks([])
            if i == 0:
                ax.set_title(f"{FASES[j]}\n$t={t}$", fontsize=21, pad=10)
            if j == 0:
                ax.set_ylabel(lab, fontsize=21, labelpad=12)

    fig.tight_layout(rect=[0, 0, 0.92, 1])
    cax = fig.add_axes([0.935, 0.10, 0.018, 0.80])
    cb = fig.colorbar(im, cax=cax)
    cb.set_label(r"$\rho$", fontsize=24, rotation=0, labelpad=14)
    cb.set_ticks(np.round(np.linspace(vmin, vmax, 4), 1))
    cb.ax.tick_params(labelsize=18)
    fig.savefig(OUT, bbox_inches="tight", dpi=240)
    plt.close(fig)
    print("OK ->", OUT)


if __name__ == "__main__":
    main()
