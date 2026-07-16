#!/usr/bin/env python3
"""fig_zona_transicion versión SLIDE (lámina de la zona de transición).
Mismos datos y ajuste que la figura de la monografía (pipeline lab_offsetC:
γ_KHI(σ) + sigmoide con offset), SIN las anotaciones descriptivas largas —
los valores están en el recuadro lateral de la lámina. Se conservan las
bandas R/T/I, las líneas de los 4 estimadores (valores publicados) y la
asíntota C+γ₀, con rótulos cortos grandes.

Correr desde INFO/lab/lab_offsetC:
    cd ~/Documents/Grado/INFO/lab/lab_offsetC
    ../.venv/bin/python ~/Documents/Grado/REPO_GH/presentacion/scripts_slide/gen_zona_transicion_slide.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd()))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from config_khi import (
    BASE_DIR, ARCHIVO_DIAGNOSTICO, T_FILTRO,
    cargar_simulaciones_validas, ajustar_gamma_corregida,
)
from khi_modelos import ajustar_todos_los_modelos, modelo_sigmoide_offset

OUT = Path.home() / "Documents/Grado/REPO_GH/presentacion/figures/fig_zona_transicion_slide.pdf"

plt.rcParams.update({
    "text.usetex": False, "mathtext.fontset": "cm",
    "font.family": "serif",
    "font.serif": ["DejaVu Serif", "Computer Modern Roman"],
    "axes.labelsize": 19, "font.size": 15,
    "legend.fontsize": 14, "xtick.labelsize": 16, "ytick.labelsize": 16,
    "pdf.fonttype": 42,
})

# Valores publicados (monografía / lámina): bordes y estimadores
BORDE_R, BORDE_I = 1400.0, 7000.0
ESTIMADORES = [  # (valor, etiqueta, color)
    (2815, r"M4$\,{=}\,$2815", "purple"),
    (3400, r"M2$\,{=}\,$3400", "green"),
    (6000, r"M3$\,{=}\,$6000", "teal"),
    (6800, r"M1$\,{=}\,$6800", "crimson"),
]


def main():
    sims = cargar_simulaciones_validas(
        BASE_DIR, ARCHIVO_DIAGNOSTICO, T_FILTRO, cargar_curva=True)
    sg, gg, sig = [], [], []
    for sim in sims:
        aj = ajustar_gamma_corregida(sim['t'], sim['omega_zp'])
        if np.isnan(aj['gamma_khi']):
            continue
        sg.append(sim['sigma']); gg.append(aj['gamma_khi'])
        sig.append(aj.get('gamma_significativa', True))
    sg, gg, sig = np.array(sg), np.array(gg), np.array(sig)

    # El ajuste usa solo las sims con γ significativa (idéntico al pipeline);
    # los puntos se muestran todos (los resistivos son el plateau γ≈0).
    res = ajustar_todos_los_modelos(sg[sig], gg[sig])
    p = res['v5']['sigmoide']
    ss = np.geomspace(sg.min() * 0.9, sg.max() * 1.1, 400)
    curva = modelo_sigmoide_offset(ss, p['gamma0'], p['sigma0'], p['k'], p['C'])
    asintota = p['C'] + p['gamma0']

    fig, ax = plt.subplots(figsize=(12.6, 6.6))
    x0, x1 = sg.min() * 0.9, sg.max() * 1.1

    # Bandas de régimen con rótulos grandes
    ax.axvspan(x0, BORDE_R, color='red', alpha=0.06)
    ax.axvspan(BORDE_R, BORDE_I, color='orange', alpha=0.10)
    ax.axvspan(BORDE_I, x1, color='green', alpha=0.07)
    for xc, lab, c in [(np.sqrt(x0 * BORDE_R), "RESISTIVO", 'firebrick'),
                       (np.sqrt(BORDE_R * BORDE_I), "ZONA DE TRANSICIÓN", 'darkorange'),
                       (np.sqrt(BORDE_I * x1), "IDEAL", 'green')]:
        ax.text(xc, 1.30, lab, ha='center', va='center', fontsize=16,
                fontweight='bold', color=c)

    # Bordes de la zona
    ax.axvline(BORDE_R, color='firebrick', ls=':', lw=2.0)
    ax.axvline(BORDE_I, color='green', ls=':', lw=2.0)

    # Estimadores (etiquetas cortas, alternando altura)
    for n, (v, lab, c) in enumerate(ESTIMADORES):
        ax.axvline(v, color=c, lw=2.2, alpha=0.85)
        y = -0.32 if n % 2 == 0 else -0.47
        ax.text(v, y, lab, ha='center', va='top', fontsize=14.5,
                color=c, fontweight='bold')

    # Datos y ajuste
    ax.plot(sg, gg, 'o', color='gray', ms=6, alpha=0.8,
            label=r"$\gamma_{\rm KHI}(\sigma)$")
    ax.plot(ss, curva, color='blue', lw=2.8, label="sigmoide con offset")
    ax.axhline(asintota, color='blue', ls='--', lw=1.6, alpha=0.8)
    ax.text(x1 * 0.97, asintota + 0.03, r"$C+\gamma_0$", ha='right',
            fontsize=16, color='blue')

    ax.set_xscale('log')
    ax.set_xlim(x0, x1)
    ax.set_ylim(-0.62, 1.42)
    ax.set_xlabel(r"Conductividad $\sigma$")
    ax.set_ylabel(r"$\gamma_{\rm KHI}$")
    ax.legend(loc='center left', framealpha=0.92)
    ax.grid(alpha=0.25, which='both')

    fig.tight_layout()
    fig.savefig(OUT, bbox_inches='tight')
    plt.close(fig)
    print("OK ->", OUT)


if __name__ == "__main__":
    main()
