#!/usr/bin/env python3
"""Diagnósticos de lámina de corriente que calcula Cueva — MATERIAL DE ANEXO.

  fig_diag_laminas_barrido_anexo.pdf   (B20)  — barrido en sigma
  fig_diag_laminas_series_anexo.pdf    (B21)  — series temporales

AVISO IMPORTANTE (regla de consistencia deck<->monografía):
  NINGUNO de estos diagnósticos aparece en la monografía. El código los
  escribe en data_global/2d_data_Erec_AB.dat, pero no se usaron para sustentar
  ninguna afirmación del documento. Van SOLO al respaldo, rotulados como tal.

DEFINICIONES (22_writer.f95, 2.º pase, líneas ~1292-1330; constantes en
parameters.f95:311-316):
  Bup_rms  = rms de Bperp=sqrt(Bx^2+By^2) en el "upstream" |x| >= 0.75
             (dominio Lx=2 -> x en [-1,1]; lejos de ambas capas de cizalla)
  máscara de lámina, celda a celda:
             Bperp <= epsB_sheet * Bup_rms       con epsB_sheet = 0.10
       Y     J^2   >= epsJ_sheet * J2max_all     con epsJ_sheet = 0.20
  nsheet   = NÚMERO DE CELDAS que cumplen la máscara  (NO número de láminas)
  Erec     = max_{celdas de lámina} |Ez|        (proxy de reconexión, "B")
  Eeta     = eta * max_{celdas de lámina} |Jz|  (proxy resistivo, "A")
             eta_loc = 1/sigma_0, recompilado por corrida -> es el eta real
             (verificado: col4/col5 = 1/sigma exacto en cada run)

COLUMNAS de 2d_data_Erec_AB.dat (write(239,*) en 22_writer.f95:1430):
  0=h  1=t  2=Ezmax_sheet  3=eta*Jzmax_sheet  4=Jzmax_sheet
  5=Ezmax_sheet (DUPLICADA de la 2, quirk del writer)  6=Bup_rms  7=nsheet

Correr: INFO/lab/.venv/bin/python gen_diag_laminas_anexo.py
"""
import os
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

LAB = os.path.expanduser("~/Documents/Grado/INFO/lab")
BASE = os.path.join(LAB, "lab_offsetC", "entornos_data_global")
FIG = os.path.expanduser("~/Documents/Grado/REPO_GH/presentacion/figures")

NCELL = (512 - 1) * (256 - 1)     # celdas barridas por el detector = 130305
ZONA = (1400.0, 7000.0)
SIGMA_CRIT = 2815.0
T_CAP = 15.0
REPRES = [(1000, "#1f77b4", "resistivo"),
          (3000, "#d62728", "transición"),
          (10000, "#2ca02c", "ideal")]

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


def col(sig, name):
    f = os.path.join(BASE, f"run_sigma_{sig}", "data_global", f"2d_data_{name}.dat")
    try:
        a = np.loadtxt(f)
        return a if (a.ndim == 2 and a.shape[0] >= 3) else None
    except Exception:
        return None


rows, series = [], {}
for s in SIGMAS:
    O = col(s, "Omega_zp_int")
    R = col(s, "Erec_AB")
    if O is None or R is None:
        continue
    t_o, ozp = O[:, 1], O[:, 2]
    t_peak = float(t_o[np.argmax(ozp)])

    t = R[:, 1]
    erec = R[:, 2]                  # max |Ez| en la lámina
    eeta = R[:, 3]                  # eta * max |Jz| en la lámina
    ns = R[:, 7] / NCELL * 100.0    # % del dominio marcado como lámina

    # ventana turbulenta: del pico de enstrofía al horizonte común
    m_turb = (t >= t_peak) & (t <= T_CAP)
    ip = int(np.argmin(np.abs(t - t_peak)))
    rows.append(dict(
        sigma=s, t_peak=t_peak,
        erec_max=float(np.nanmax(erec)),
        erec_turb=float(np.nanmedian(erec[m_turb])) if m_turb.sum() > 2 else np.nan,
        eeta_turb=float(np.nanmedian(eeta[m_turb])) if m_turb.sum() > 2 else np.nan,
        ns_turb=float(np.nanmedian(ns[m_turb])) if m_turb.sum() > 2 else np.nan,
        ns_max=float(np.nanmax(ns)),
        ns_pk=float(ns[ip]),
    ))
    if s in [r[0] for r in REPRES]:
        series[s] = (t, ns, erec, t_peak)

S = np.array([r["sigma"] for r in rows], float)
g = lambda k: np.array([r[k] for r in rows])
print(f"runs: {len(rows)}   (nsheet normalizado a {NCELL} celdas)")

# ============================================================ FIG 1 · barrido
# Los ceros NO son "valor cero": son "el detector no encontró ninguna celda de
# lámina". Se enmascaran y se marca la banda donde eso ocurre de forma sostenida.
def masked(k):
    v = g(k).copy()
    v[v <= 0] = np.nan
    return v


NOD = 1400.0    # por debajo, la mediana turbulenta de nsheet es 0 en casi todos

fig, ax = plt.subplots(1, 3, figsize=(13.2, 3.7))

E = g("erec_max")
ax[0].plot(S, E, "o-", ms=4, lw=1.3, color="#c2185b", label="máx en la corrida")
ax[0].plot(S, masked("erec_turb"), "s--", ms=3.2, lw=1.1, color="#7b1fa2",
           label="mediana turbulenta")
ax[0].set_ylabel(r"$E_{\rm rec}=\max_{\rm lámina}|E_z|$")
ax[0].set_title("(a) Campo eléctrico en la lámina", fontsize=10)
ax[0].legend(fontsize=7.5, loc="lower right", framealpha=0.9)
ax[0].plot(S[np.argmax(E)], E.max(), "o", ms=11, mfc="none", mec="crimson", mew=2, zorder=5)
ax[0].annotate(rf"máx en $\sigma\approx{S[np.argmax(E)]:.0f}$",
               xy=(S[np.argmax(E)], E.max()), xytext=(150, E.max()*0.995),
               fontsize=8.5, color="crimson", fontweight="bold", va="center",
               arrowprops=dict(arrowstyle="->", color="crimson", lw=1.1))

N = masked("ns_turb")
ax[1].plot(S, N, "o-", ms=4, lw=1.3, color="#e65100")
ax[1].set_ylabel("área de lámina  [% del dominio]")
ax[1].set_title("(b) Extensión de lámina (fase turbulenta)", fontsize=10)
ax[1].plot(S[np.nanargmax(N)], np.nanmax(N), "o", ms=11, mfc="none", mec="crimson",
           mew=2, zorder=5)
ax[1].annotate(f"máx $\\approx${np.nanmax(N):.2f}% del dominio\n"
               f"en $\\sigma\\approx${S[np.nanargmax(N)]:.0f}  "
               f"({np.nanmax(N)/100*NCELL:.0f} celdas)",
               xy=(S[np.nanargmax(N)], np.nanmax(N)), xytext=(1.08e2, np.nanmax(N)*0.80),
               fontsize=8.5, color="crimson", fontweight="bold", va="center",
               arrowprops=dict(arrowstyle="->", color="crimson", lw=1.1))

EJ = masked("eeta_turb")
ax[2].plot(S, EJ, "^-", ms=4, lw=1.3, color="#00695c")
ax[2].set_yscale("log")
ax[2].set_ylabel(r"$\eta\,\max_{\rm lámina}|J_z|$")
ax[2].set_title(r"(c) Campo resistivo $\eta J$ en la lámina", fontsize=10)
ax[2].text(0.035, 0.95,
           "crece con $\\sigma$: $|J_z|$ en la lámina sube\n"
           "más rápido de lo que cae $\\eta=1/\\sigma$",
           transform=ax[2].transAxes, fontsize=8, color="#00695c",
           va="top", ha="left")

for k in range(3):
    ax[k].set_xscale("log"); ax[k].set_xlabel(r"$\sigma$"); ax[k].set_xlim(90, 12000)
    ax[k].axvspan(*ZONA, color="#ff9f43", alpha=0.16, zorder=0, lw=0)
    ax[k].axvline(SIGMA_CRIT, color="crimson", ls=(0, (4, 2)), lw=1.3, alpha=0.8, zorder=1)
    # banda de NO DETECCIÓN sostenida (limitación del diagnóstico, no física)
    ax[k].axvspan(90, NOD, color="#607d8b", alpha=0.17, zorder=0, lw=0, hatch="///")
ax[1].annotate("zona de transición", xy=(np.sqrt(ZONA[0]*ZONA[1]), 0.035),
               xycoords=("data", "axes fraction"), ha="center", va="bottom",
               fontsize=8, color="#b06a1a", fontweight="bold")
ax[0].annotate("sin lámina\nsostenida", xy=(340, 0.62), xycoords=("data", "axes fraction"),
               ha="center", va="center", fontsize=8, color="#37474f", fontweight="bold")

fig.tight_layout()
o1 = os.path.join(FIG, "fig_diag_laminas_barrido_anexo.pdf")
fig.savefig(o1); plt.close(fig)

# ==================================================== FIG 2 · series temporales
fig, ax = plt.subplots(1, 2, figsize=(11.6, 3.7))
for s, c, lab in REPRES:
    if s not in series:
        continue
    t, ns, erec, tp = series[s]
    m = t <= T_CAP
    ax[0].plot(t[m], ns[m], "-", lw=1.2, color=c, label=rf"$\sigma={s}$ ({lab})")
    ax[1].plot(t[m], erec[m], "-", lw=1.2, color=c, label=rf"$\sigma={s}$ ({lab})")
    for k in (0, 1):
        ax[k].axvline(tp, color=c, ls=":", lw=1.1, alpha=0.75)

ax[0].set_ylabel("área de lámina  [% del dominio]")
ax[0].set_title(r"(a) $n_{\rm sheet}(t)$ --- punteadas: $t_{\rm peak}$ de cada corrida",
                fontsize=10)
ax[1].set_ylabel(r"$E_{\rm rec}(t)=\max_{\rm lámina}|E_z|$")
ax[1].set_title(r"(b) Campo de reconexión en la lámina", fontsize=10)
for k in (0, 1):
    ax[k].set_xlabel(r"$t$"); ax[k].set_xlim(0, T_CAP)
    ax[k].legend(fontsize=7.5, framealpha=0.9)
for k in (0, 1):
    ax[k].axvspan(0, 1.9, color="#607d8b", alpha=0.15, zorder=0, lw=0)
    ax[k].text(1.9 / T_CAP * 0.5, 0.42, "sin\nlámina", transform=ax[k].transAxes,
               fontsize=7.5, color="#37474f", ha="center", va="center",
               zorder=3, rotation=90)

fig.tight_layout()
o2 = os.path.join(FIG, "fig_diag_laminas_series_anexo.pdf")
fig.savefig(o2); plt.close(fig)

# ------------------------------------------------------------------ resumen
print(f"E_rec  : máx {E.max():.4g} en sigma={S[np.argmax(E)]:.0f}")
print(f"area   : máx {np.nanmax(N):.3f}% en sigma={S[np.nanargmax(N)]:.0f} "
      f"(= {np.nanmax(N)/100*NCELL:.0f} celdas)")
print(f"eta*Jz : {g('eeta_turb')[0]:.4g} (sigma=100) -> {g('eeta_turb')[-1]:.4g} (sigma=10500)")
fv = []
for s in SIGMAS:
    O = col(s, "Omega_zp_int"); F = col(s, "fraccion_aportada_Vz")
    if O is None or F is None: continue
    fv.append(float(F[int(np.argmax(O[:, 2])), 2]))
fv = np.array(fv)
for k, lab in (("erec_max", "E_rec máx"), ("ns_turb", "área lámina")):
    v = g(k); m = np.isfinite(v) & np.isfinite(fv)
    rk = lambda a: np.argsort(np.argsort(a))
    print(f"Spearman(f_Vz, {lab:12s}) = "
          f"{np.corrcoef(rk(fv[m]), rk(v[m]))[0,1]:+.3f}")
print("OK ->", o1, "\nOK ->", o2)
