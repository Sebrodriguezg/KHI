#!/usr/bin/env python3
import os, glob, sys, warnings, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Directorios según tu configuración
CLEAN = os.path.expanduser("/home/sebastian/Documents/Grado/INFO/lab/analisis_campanas_B_PRELIM/resultados_condensados_6000_vs_10000/ANALISIS_LIMPIO_FINAL/DATOS_LIMPIOS")
FIG = os.path.expanduser("/home/sebastian/Documents/Grado/REPO_GH/monografia/figuras")

warnings.filterwarnings("ignore")
plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "cm"})

def load(p):
    try:
        d = np.loadtxt(p)
        return (d[:,1], d[:,2]) if d.ndim == 2 and len(d) > 2 else (None, None)
    except: return None, None

def thlbl(nm): 
    # Extrae el ángulo y corrige 06 -> 5.7
    ang = nm.split("_th")[-1]
    if ang == "06": return r"$\theta=5.7^\circ$"
    return r"$\theta=" + ang + r"^\circ$"

def combo(fam, fname, titulo, lblfn):
    fig, axs = plt.subplots(1, 2, figsize=(13, 5.2), sharey=False)
    for ax, (sg, cfl) in zip(axs, [("sigma6000", "0.04"), ("sigma10000", "0.02")]):
        for r in sorted(glob.glob(os.path.join(CLEAN, fam, sg, "run_*"))):
            nm = os.path.basename(r).replace("run_", "")
            t, o = load(os.path.join(r, "data_global", "2d_data_Omega_zp_int.dat"))
            if t is None: continue
            
            # --- CORRECCIÓN AQUÍ: Eliminados los '$' extra del f-string ---
            ln, = ax.semilogy(t, o, lw=1.6, label=f"{lblfn(nm)} (t={t[-1]:.0f})")
            ax.scatter([t[-1]], [o[-1]], s=18, color=ln.get_color(), zorder=5)
        
        ax.axvspan(2.4, 3.4, color="gray", alpha=0.15, label="ventana γ")
        ax.set_xlabel(r"$t$")
        ax.set_ylabel(r"$\Omega_{zp}$")
        ax.grid(alpha=0.3)
        ax.legend(fontsize=8)
        # --- CORRECCIÓN AQUÍ: Usar raw string para evitar error con \s en \sigma ---
        ax.set_title(rf"$\sigma={sg.replace('sigma','')}$ (CFL={cfl})", fontsize=12)
    
    fig.suptitle(titulo, fontsize=13, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(FIG, f"{fname}.{ext}"), dpi=140)
    plt.close(fig)
    print("OK:", fname)

if __name__ == "__main__":
    # Generación específica para Campaña B
    combo("B_orientacion_yz", "fig_campB_enstrofia", 
          r"Campaña B (plano $y$–$z$) — enstrofía $\Omega_{zp}(t)$ vs orientación $\theta$", thlbl)