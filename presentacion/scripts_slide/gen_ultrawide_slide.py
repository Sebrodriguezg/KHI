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
    BASE_DIR, ARCHIVO_DIAGNOSTICO, T_FILTRO, T_FIT_MIN, T_FIT_MAX,
    cargar_simulaciones_validas, asignar_indices_canonicos,
    construir_cmap_canonico,
)

# Ronda 2 (obs. del profesor): 4 regiones dinámicas sobre el eje temporal.
# Fronteras RIGUROSAS: la ventana lineal es la canónica del pipeline
# [T_FIT_MIN, T_FIT_MAX] = [2.4, 3.4] (la misma de todos los ajustes de γ);
# el fin de la fase explosiva es el t_peak MEDIDO del run ideal de referencia
# σ=10000 (argmax de su Ω_zp). Fronteras ilustrativas para σ bajas.
SIGMA_REF = 10000

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

    # ---- 4 regiones dinámicas (fronteras del pipeline + run de referencia) ----
    ref = next(s for s in sims if s['sigma'] == SIGMA_REF)
    t_peak = float(ref['t'][int(np.argmax(ref['omega_zp']))])
    # Fin del transiente numérico: primer máximo local de Ω_zp del run de
    # referencia (el ajuste inicial de la CI termina ahí, t ~ 0.5).
    o_ref, t_ref = ref['omega_zp'], ref['t']
    i_num = next(i for i in range(1, len(o_ref) - 1)
                 if o_ref[i] >= o_ref[i + 1] and t_ref[i] < 1.5)
    t_num = float(t_ref[i_num])
    print(f"t_num = {t_num:.2f};  t_peak(sigma={SIGMA_REF}) = {t_peak:.2f};  "
          f"ventana de ajuste = [{T_FIT_MIN}, {T_FIT_MAX}]")
    T_END = 15.0
    regiones = [
        (0.0,        t_num,     "#9e9e9e", "num."),
        (t_num,      T_FIT_MAX, "#2e7d32", "lineal"),
        (T_FIT_MAX,  t_peak,    "#e65100", "explosiva"),
        (t_peak,     T_END,     "#1565c0", "relajación / turbulencia"),
    ]
    # (ronda 3) la zona "numérica" es sólo el crecimiento rápido inicial
    # (transiente de arranque, SIN física); se resalta con trama y más
    # opacidad para distinguirla claramente del resto.
    for k, (t0, t1, color, _) in enumerate(regiones):
        if k == 0:
            ax.axvspan(t0, t1, facecolor=color, alpha=0.30,
                       hatch="////", edgecolor="#546e7a", linewidth=0.0,
                       zorder=0)
        else:
            ax.axvspan(t0, t1, color=color, alpha=0.10, zorder=0)
    for t0, t1, color, nombre in regiones:
        ax.axvline(t1, color="k", lw=0.8, ls=":", alpha=0.5)
        ax.text(0.5 * (t0 + t1), 0.985, nombre, color=color,
                fontsize=13, fontweight="bold", ha="center", va="top",
                transform=mpl.transforms.blended_transform_factory(
                    ax.transData, ax.transAxes))
    # ventana canónica de ajuste, marcada dentro de la región lineal
    ax.axvspan(T_FIT_MIN, T_FIT_MAX, color="#2e7d32", alpha=0.10, zorder=0)

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
