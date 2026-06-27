#!/usr/bin/env python3
import os, glob, warnings, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

CLEAN = os.path.expanduser("~/Documents/Grado/INFO/lab/analisis_campanas_B_PRELIM/resultados_condensados_6000_vs_10000/ANALISIS_LIMPIO_FINAL/DATOS_LIMPIOS")
FIG = os.path.expanduser("~/Documents/Grado/REPO_GH/monografia/figuras")

warnings.filterwarnings("ignore")
plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "cm"})

def load(p):
    try:
        d = np.loadtxt(p)
        return (d[:, 1], d[:, 2]) if d.ndim == 2 and len(d) > 2 else (None, None)
    except: return None, None

def albl_fn(nm):
    ALBL = {"A1_B025": r"$B_0=0.25$", "A2_B050": r"$B_0=0.5$", "A3_B100": r"$B_0=1.0$", "A4_B150": r"$B_0=1.5$", "A5_B200": r"$B_0=2.0$"}
    return ALBL.get(nm, nm)

def combo(fam, fname, titulo, lblfn, con_picos=False):
    # Aumentamos figsize para mayor espacio
    fig, axs = plt.subplots(1, 2, figsize=(15, 6.5), sharey=False)
    configs = [("sigma6000", "0.04"), ("sigma10000", "0.02")]
    
    for ax, (sg, cfl) in zip(axs, configs):
        ruta_base = os.path.join(CLEAN, fam, sg)
        runs = sorted(glob.glob(os.path.join(ruta_base, "run_*")))
        
        for idx, r in enumerate(runs):
            nm = os.path.basename(r).replace("run_", "")
            t, o = load(os.path.join(r, "data_global", "2d_data_Omega_zp_int.dat"))
            if t is None: continue
            
            ln, = ax.semilogy(t, o, lw=1.8, label=f"{lblfn(nm)} (t={t[-1]:.0f})")
            
            if con_picos:
                idx_max = np.argmax(o)
                t_p, o_p = t[idx_max], o[idx_max]
                ax.axvline(t_p, color=ln.get_color(), ls='--', lw=0.9, alpha=0.5)
                ax.scatter([t_p], [o_p], s=40, color=ln.get_color(), marker='*', zorder=6)
                
                # REPELENTE: Si es índice par, ponemos el texto arriba, si es impar, abajo
                va = 'bottom' if idx % 2 == 0 else 'top'
                offset = 1.2 if idx % 2 == 0 else 0.85
                ax.text(t_p, o_p * offset, f"({t_p:.1f}, {o_p:.0f})", 
                        color=ln.get_color(), fontsize=8.5, ha='center', va=va,
                        bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='none', alpha=0.7))
        
        ax.axvspan(2.4, 3.4, color="gray", alpha=0.1)
        ax.set_xlabel(r"$t$", fontsize=12)
        ax.set_ylabel(r"$\Omega_{zp}$", fontsize=12)
        ax.tick_params(labelsize=10)
        ax.grid(alpha=0.3)
        ax.legend(fontsize=9, loc="best")
        ax.set_title(rf"$\sigma={sg.replace('sigma','')}$ (CFL={cfl})", fontsize=13)
    
    fig.suptitle(titulo, fontsize=15, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(FIG, f"{fname}.{ext}"), dpi=160)
    plt.close(fig); print("OK:", fname)

if __name__ == "__main__":
    combo("A_intensidad", "fig_campA_enstrofia", 
          r"Campaña A — enstrofía $\Omega_{zp}(t)$ vs intensidad $B_0$", albl_fn, con_picos=True)