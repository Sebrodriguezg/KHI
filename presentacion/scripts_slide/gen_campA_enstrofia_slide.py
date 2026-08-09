#!/usr/bin/env python3
"""fig_campA_enstrofia versión SLIDE (P25). Mismos datos que genesntA.py
(DATOS_LIMPIOS/A_intensidad); solo cambia presentación: sin suptitle,
fuentes grandes, anotaciones de pico legibles.

Correr: INFO/lab/.venv/bin/python gen_campA_enstrofia_slide.py
"""
import os, glob, warnings, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

CLEAN = os.path.expanduser("~/Documents/Grado/INFO/lab/analisis_campanas_B_PRELIM/resultados_condensados_6000_vs_10000/ANALISIS_LIMPIO_FINAL/DATOS_LIMPIOS")
OUT = os.path.expanduser("~/Documents/Grado/REPO_GH/presentacion/figures/fig_campA_enstrofia_slide.pdf")

warnings.filterwarnings("ignore")
plt.rcParams.update({
    "font.family": "serif", "mathtext.fontset": "cm",
    # (ronda 3) fuentes subidas: la figura se muestra a ~media lámina y los
    # números quedaban chicos al reescalar; agrandarlas en el origen las hace
    # legibles tras el downscale del deck.
    "axes.labelsize": 28, "axes.titlesize": 26, "font.size": 20,
    "legend.fontsize": 21, "xtick.labelsize": 23, "ytick.labelsize": 23,
    "pdf.fonttype": 42,
})

ALBL = {"A1_B025": r"$B_0=0.25$", "A2_B050": r"$B_0=0.5$",
        "A3_B100": r"$B_0=1.0$", "A4_B150": r"$B_0=1.5$",
        "A5_B200": r"$B_0=2.0$"}


def load(p):
    try:
        d = np.loadtxt(p)
        return (d[:, 1], d[:, 2]) if d.ndim == 2 and len(d) > 2 else (None, None)
    except Exception:
        return None, None


def main():
    fig, axs = plt.subplots(1, 2, figsize=(15, 6.8), sharey=False)
    for ax, (sg, cfl) in zip(axs, [("sigma6000", "0.04"), ("sigma10000", "0.02")]):
        runs = sorted(glob.glob(os.path.join(CLEAN, "A_intensidad", sg, "run_*")))
        for idx, r in enumerate(runs):
            nm = os.path.basename(r).replace("run_", "")
            t, o = load(os.path.join(r, "data_global", "2d_data_Omega_zp_int.dat"))
            if t is None:
                continue
            i_max = np.argmax(o)
            t_p, o_p = t[i_max], o[i_max]
            # (ronda 4) el pico va en la LEYENDA para que no se solapen las etiquetas
            lbl = rf"{ALBL.get(nm, nm)}:  $\Omega^{{\max}}\!=\!{o_p:.0f}$ en $t\!=\!{t_p:.1f}$"
            ln, = ax.semilogy(t, o, lw=2.6, label=lbl)
            ax.axvline(t_p, color=ln.get_color(), ls='--', lw=1.2, alpha=0.5)
            ax.scatter([t_p], [o_p], s=150, color=ln.get_color(), marker='*',
                       zorder=6, edgecolor='k', linewidth=0.6)
        ax.axvspan(2.4, 3.4, color="gray", alpha=0.12)
        ax.set_xlabel(r"$t$")
        ax.set_ylabel(r"$\Omega_{zp}$")
        ax.grid(alpha=0.3)
        ax.legend(loc="lower right", framealpha=0.95, fontsize=15)
        ax.set_title(rf"$\sigma={sg.replace('sigma','')}$ (CFL={cfl})", pad=10)
    fig.tight_layout()
    fig.savefig(OUT, dpi=160, bbox_inches='tight')
    plt.close(fig)
    print("OK ->", OUT)


if __name__ == "__main__":
    main()
