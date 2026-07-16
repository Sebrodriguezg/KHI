#!/usr/bin/env python3
"""ln_omega_vs_t versión SLIDE (P19 del deck de sustentación).

Reusa el pipeline lab_offsetC (config_khi) con los MISMOS datos y ajustes;
solo cambia la presentación: sin título interno, colorbar continua de σ,
fuentes ≥14-16 pt, leyenda compacta.

Correr desde INFO/lab/lab_offsetC:
    cd ~/Documents/Grado/INFO/lab/lab_offsetC
    ../.venv/bin/python ~/Documents/Grado/REPO_GH/presentacion/scripts_slide/gen_ln_omega_slide.py
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
    T_FIT_MIN, T_FIT_MAX, T_PLOT_MIN, T_PLOT_MAX,
    T_PICO_MIN, T_PICO_MAX, SIGMA_MIN_PICOS,
    BASE_DIR, ARCHIVO_DIAGNOSTICO, T_FILTRO,
    cargar_simulaciones_validas, asignar_indices_canonicos,
    construir_cmap_canonico, ajustar_gamma_corregida,
    detectar_picos_omega_max, finalizar_regimenes,
)

OUT = Path.home() / "Documents/Grado/REPO_GH/presentacion/figures/ln_omega_vs_t_slide.pdf"

plt.rcParams.update({
    "text.usetex": False, "mathtext.fontset": "cm",
    "font.family": "serif",
    "font.serif": ["DejaVu Serif", "Computer Modern Roman"],
    "axes.labelsize": 19, "font.size": 15,
    "legend.fontsize": 14.5, "xtick.labelsize": 16, "ytick.labelsize": 16,
    "pdf.fonttype": 42,
})

_REG_COLOR = {'R': '#d62728', 'T': '#ff7f0e', 'I': '#2ca02c'}
_REG_LS    = {'R': ':',       'T': '--',      'I': '-'}
_REG_LABEL = {'R': 'Resistivo',
              'T': 'Transición',
              'I': 'Ideal'}


def main():
    sims = cargar_simulaciones_validas(
        BASE_DIR, ARCHIVO_DIAGNOSTICO, T_FILTRO, cargar_curva=True)
    sigmas_global = [s['sigma'] for s in sims]
    idx_canon = asignar_indices_canonicos(sigmas_global)
    n_total = len(sims)

    resultados = []
    for sim in sims:
        aj = ajustar_gamma_corregida(sim['t'], sim['omega_zp'])
        if np.isnan(aj['gamma_khi']):
            continue
        resultados.append({
            'indice_canonico': idx_canon[sim['sigma']],
            'sigma': sim['sigma'], 't': sim['t'],
            'omega_zp': sim['omega_zp'], **aj,
        })

    # Picos → borde ideal → regímenes definitivos (idéntico al pipeline)
    sp, om = [], []
    for sim in sims:
        if sim['sigma'] < SIGMA_MIN_PICOS:
            continue
        m = (sim['t'] >= T_PICO_MIN) & (sim['t'] <= T_PICO_MAX)
        if m.sum() == 0:
            continue
        sp.append(sim['sigma'])
        om.append(sim['omega_zp'][m].max())
    pk = detectar_picos_omega_max(np.array(sp), np.array(om))
    finalizar_regimenes(resultados, pk['pico2'])

    cmap, norm = construir_cmap_canonico(n_total)

    fig = plt.figure(figsize=(12.6, 7.0))
    gs = gridspec.GridSpec(1, 2, width_ratios=[46, 1], wspace=0.03)
    ax, cax = fig.add_subplot(gs[0]), fig.add_subplot(gs[1])

    ax.axvspan(T_FIT_MIN, T_FIT_MAX, alpha=0.15, color='gold', zorder=0,
               label=rf'Ventana $[{T_FIT_MIN},\,{T_FIT_MAX}]$')

    seen = set()
    for r in resultados:
        color = cmap(norm(r['indice_canonico'] - 1))
        reg = r.get('regimen', 'I')
        sig = r.get('gamma_significativa', True)
        m = ((r['t'] >= T_PLOT_MIN) & (r['t'] <= T_PLOT_MAX)
             & (r['omega_zp'] > 1e-15))
        ax.plot(r['t'][m], np.log(r['omega_zp'][m]),
                color=color, lw=1.3, alpha=0.55 if sig else 0.22)
        ta = r.get('t_start', T_FIT_MIN)
        tb = r.get('t_end', T_FIT_MAX)
        t_fit = np.linspace(ta, tb, 60)
        lbl = _REG_LABEL[reg] if reg not in seen else None
        ax.plot(t_fit, r['intercept'] + r['slope'] * t_fit,
                color=_REG_COLOR[reg], lw=3.0, alpha=0.92,
                ls=_REG_LS[reg], solid_capstyle='round', label=lbl, zorder=4)
        seen.add(reg)

    ax.set_xlim(T_PLOT_MIN, T_PLOT_MAX)
    ax.set_xlabel(r"$t$")
    ax.set_ylabel(r"$\ln\,\Omega_{zp}(t)$")
    ax.legend(loc='upper left', framealpha=0.92)
    ax.grid(True, ls="--", alpha=0.4)

    # Colorbar continua etiquetada con σ (no 44 ítems)
    sigma_por_idx = {idx_canon[s]: s for s in sigmas_global}
    sm = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
    cb = fig.colorbar(sm, cax=cax)
    n_ticks = 6
    tick_idx = np.unique(np.linspace(1, n_total, n_ticks).round().astype(int))
    cb.set_ticks(tick_idx - 1)
    cb.set_ticklabels([f"{sigma_por_idx[i]:.0f}" for i in tick_idx])
    cb.ax.tick_params(labelsize=15)
    cax.set_ylabel(r"$\sigma$", fontsize=19, rotation=0, labelpad=18)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT, format='pdf', bbox_inches='tight')
    plt.close(fig)
    print(f"OK -> {OUT}")


if __name__ == "__main__":
    main()
