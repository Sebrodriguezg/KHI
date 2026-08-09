#!/usr/bin/env python3
"""fig_estructuras_secundarias_slide.pdf — lámina 27 (ronda 4).

Los DOS canales de estructura secundaria, uno al lado del otro, con la zona de
transición sombreada en ambos:
  (a) f_Vz en saturación  — canal cinético fuera del plano (anisotropía)
  (b) J_max(t<5)          — canal magnético: intensidad de las láminas

CONSISTENCIA CON LA MONOGRAFÍA (regla: nada que no esté en el documento):
  · f_Vz = (Omega_tot - Omega_z)/Omega_tot ......... setup_exp.tex:281 (Ec. eq:fvz)
    evaluado en saturación (índice del pico de Omega_zp) — igual que
    analisis_globales_obj23.py, que produce figuras/fig_global_estructuras.pdf
    (monografía Fig. global_estructuras, 05_results_discussion.tex:330-335).
    Valores citados en la monografía: máx ~0.37 en sigma~1400, ~0.08 en el ideal.
  · J_max evaluado ESTRICTAMENTE en t<5.0 ......... 05_results_discussion.tex:314,324
    (misma ventana transitoria del panel (a) de fig_global_campos_transitorio y
    de la lámina 26 del deck, gen_disipacion_ventanas_slide.py).
  · Zona de transición sigma in [1400,7000] ....... 05_results_discussion.tex:197,247
    con el borde inferior definido JUSTAMENTE como el máximo de f_Vz.
  · sigma_crit = 2815 (centro del crecimiento lineal) ... idem.
NO se grafica ningún diagnóstico ausente de la monografía (E_rec, nsheet, ...).

Correr: INFO/lab/.venv/bin/python gen_estructuras_secundarias_slide.py
"""
import os
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

LAB = os.path.expanduser("~/Documents/Grado/INFO/lab")
BASE = os.path.join(LAB, "lab_offsetC", "entornos_data_global")
OUT = os.path.expanduser(
    "~/Documents/Grado/REPO_GH/presentacion/figures/"
    "fig_estructuras_secundarias_slide.pdf")

# zona de transición y centro (monografía §5, tabla de estimadores)
ZONA = (1400.0, 7000.0)
SIGMA_CRIT = 2815.0

SIGMAS = [100,300,500,600,800,900,1000,1200,1400,1600,1800,2000,2200,2400,2600,
          2800,2950,3000,3050,3200,3400,3600,3800,4000,4500,5000,5500,6000,6200,
          6400,6500,6600,6800,7000,7400,7500,7600,8000,8500,9000,9500,10000,10250,10500]

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif", "Computer Modern Roman"],
    "mathtext.fontset": "cm",
    "font.size": 11, "axes.labelsize": 11,
    "axes.grid": True, "grid.alpha": 0.3,
    "figure.facecolor": "white", "savefig.facecolor": "white",
    "savefig.bbox": "tight", "pdf.fonttype": 42,
})


def load(sig, name):
    f = os.path.join(BASE, f"run_sigma_{sig}", "data_global", f"2d_data_{name}.dat")
    try:
        a = np.loadtxt(f)
        if a.ndim < 2 or a.shape[0] < 3:
            return None, None
        return a[:, 1], a[:, 2]
    except Exception:
        return None, None


rows = []
for s in SIGMAS:
    t, ozp = load(s, "Omega_zp_int")
    if t is None:
        continue
    ip = int(np.argmax(ozp))          # saturación = pico de la enstrofía de perturbación
    _, fv = load(s, "fraccion_aportada_Vz")
    _, jm = load(s, "Jmax")
    if fv is None or jm is None:
        continue
    rows.append(dict(
        sigma=s,
        fVz_sat=float(fv[ip]),                       # f_Vz en saturación
        Jmax_trans=float(np.nanmax(jm[t < 5.0])),    # ventana transitoria t<5
    ))

S = np.array([r["sigma"] for r in rows], float)
F = np.array([r["fVz_sat"] for r in rows])
J = np.array([r["Jmax_trans"] for r in rows])
print(f"runs con datos: {len(rows)}")

fig, ax = plt.subplots(1, 2, figsize=(11.4, 3.9))

# ---------------------------------------------------------------- (a) f_Vz
ax[0].plot(S, F, "o-", ms=4.5, lw=1.4, color="#9467bd")
ax[0].set_xscale("log")
ax[0].set_xlabel(r"$\sigma$")
ax[0].set_ylabel(r"$f_{Vz}$ en saturaci\'on" if False else r"$f_{Vz}$ en saturación")
ax[0].set_title(r"(a) Canal cinético: enstrofía fuera del plano", fontsize=10)

ipk = int(np.argmax(F))
ax[0].plot(S[ipk], F[ipk], "o", ms=10, mfc="none", mec="crimson", mew=2, zorder=5)
# el máximo de f_Vz ES la definición del borde inferior de la zona (monografía §5)
ax[0].annotate(rf"máx $={F[ipk]:.3f}$ en $\sigma\approx{S[ipk]:.0f}$" "\n"
               r"$=$ borde inferior de la zona",
               xy=(S[ipk], F[ipk]), xytext=(150, 0.315),
               fontsize=8.5, color="crimson", fontweight="bold",
               va="center", ha="left",
               arrowprops=dict(arrowstyle="->", color="crimson", lw=1.2))
ax[0].annotate(rf"ideal: $\approx{F[-1]:.2f}$",
               xy=(S[-1], F[-1]), xytext=(S[-1]*0.60, F[-1] + 0.060),
               fontsize=8.5, color="#5b3a8e", ha="center", fontweight="bold",
               arrowprops=dict(arrowstyle="->", color="#5b3a8e", lw=1.1))

# ---------------------------------------------------------------- (b) J_max
ax[1].plot(S, J, "o-", ms=4.5, lw=1.4, color="#d62728")
ax[1].set_xscale("log")
ax[1].set_xlabel(r"$\sigma$")
ax[1].set_ylabel(r"$J_{\max}$   $(t<5)$")
ax[1].set_title(r"(b) Canal magnético: intensidad de las láminas", fontsize=10)

# meseta (blindaje numérico, ya argumentado en la lámina 26) y despegue
mpl_ = (S >= 900) & (S <= 5500)
ax[1].annotate("meseta: la difusividad física\nsupera el truncamiento de malla",
               xy=(1800, float(np.nanmean(J[mpl_]))),
               xytext=(115, 186),
               fontsize=8, color="#7f4b3a", ha="left",
               arrowprops=dict(arrowstyle="->", color="#7f4b3a", lw=1.0))
ax[1].annotate(rf"despegue $\sigma\gtrsim6000$" "\n" rf"(${J[0]:.0f}\rightarrow{J[-1]:.0f}$)",
               xy=(8500, float(J[S == 8500][0])), xytext=(1750, 202),
               fontsize=8.5, color="#a01c1c", fontweight="bold", ha="left",
               va="center",
               arrowprops=dict(arrowstyle="->", color="#a01c1c", lw=1.1))

# ------------------------------------------------- zona de transición en AMBOS
for k in (0, 1):
    ax[k].axvspan(*ZONA, color="#ff9f43", alpha=0.16, zorder=0, lw=0)
    ax[k].axvline(SIGMA_CRIT, color="crimson", ls=(0, (4, 2)), lw=1.4, alpha=0.85,
                  zorder=1)
    ax[k].set_xlim(90, 12000)

# colocación por panel: se esquiva la curva en cada caso. La etiqueta de la zona
# va SOLO en (b): en (a) el espacio de arriba lo ocupa el marcador del máximo.
for k, y_crit in ((0, 0.17), (1, 0.24)):
    ax[k].annotate(r"$\sigma_{\rm crit}\!\approx\!2815$",
                   xy=(SIGMA_CRIT * 0.93, y_crit), xycoords=("data", "axes fraction"),
                   rotation=90, va="center", ha="right", fontsize=8.2,
                   color="crimson", fontweight="bold")
ax[1].annotate("zona de transición  [1400, 7000]",
               xy=(np.sqrt(ZONA[0] * ZONA[1]), 0.030),
               xycoords=("data", "axes fraction"),
               ha="center", va="bottom", fontsize=8.2, color="#b06a1a",
               fontweight="bold")

fig.tight_layout()
fig.savefig(OUT)
plt.close(fig)

print(f"f_Vz : máx {F.max():.3f} en sigma={S[np.argmax(F)]:.0f}  ->  {F[-1]:.3f} (ideal)")
print(f"J_max: {J.min():.1f} (sigma={S[np.argmin(J)]:.0f})  ->  {J.max():.1f} "
      f"(sigma={S[np.argmax(J)]:.0f})")
rho = np.corrcoef(np.argsort(np.argsort(F)), np.argsort(np.argsort(J)))[0, 1]
print(f"Spearman(f_Vz, J_max) = {rho:+.3f}  (anti-correlación: canales que se turnan)")
print("OK ->", OUT)
