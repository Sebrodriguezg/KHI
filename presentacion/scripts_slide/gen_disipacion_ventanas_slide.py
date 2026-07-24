#!/usr/bin/env python3
"""fig_global_campos versión SLIDE con disipación por VENTANAS (ronda 2).

Observación del profesor (22-jul): la disipación resistiva acumulada debe
compararse entre ventanas dinámicas. Panel (b) rehecho con el calor de Ohm
positivo-definido ∫∫ ηJ² dA dt (η=1/σ) evaluado en 4 ventanas por simulación
(NOTA: E·J crudo cambia de signo en turbulencia —intercambio reversible— y
su |integral| sufre cancelaciones; ηJ² es la disipación irreversible):
  (1) numérica   t ∈ [0, T_FIT_MIN)      — transiente de arranque
  (2) lineal     t ∈ [T_FIT_MIN, T_FIT_MAX]  — ventana canónica de ajuste γ
  (3) turbulenta t ∈ (t_peak, fin]       — post-pico de Ω_zp (t_peak por run)
  (4) total      t ∈ [0, fin]
Paneles (a) y (c) idénticos a la variante "transitorio" usada en la lámina.

Correr: INFO/lab/.venv/bin/python gen_disipacion_ventanas_slide.py
"""
import os
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

LAB = os.path.expanduser("~/Documents/Grado/INFO/lab")
BASE = os.path.join(LAB, "lab_offsetC", "entornos_data_global")
OUT = os.path.expanduser(
    "~/Documents/Grado/REPO_GH/presentacion/figures/fig_global_campos_ventanas_slide.pdf")

T_FIT_MIN, T_FIT_MAX = 2.4, 3.4   # ventana canónica del pipeline (config_khi)
# Ventanas de la disipación (documentadas en COSAS_POR_REPASAR §4 y citadas
# en el deck/guion como 26× / 16×):
#   numérica [0, 2.4)  ·  lineal [2.4, 3.4]  ·  turbulenta (t_peak, 15]  ·  total [0,15]
# La "lineal" es EXACTAMENTE la ventana canónica de ajuste de γ; la "numérica"
# es todo lo anterior a esa ventana (transiente + arranque pre-lineal).
T_NUM = T_FIT_MIN   # 2.4

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

_trap = getattr(np, "trapezoid", None) or np.trapz


def load(sig, name):
    f = os.path.join(BASE, f"run_sigma_{sig}", "data_global", f"2d_data_{name}.dat")
    try:
        a = np.loadtxt(f)
        if a.ndim < 2 or a.shape[0] < 3:
            return None, None
        return a[:, 1], a[:, 2]
    except Exception:
        return None, None


def integral_ventana(t, ej, m):
    if np.count_nonzero(m) < 2:
        return np.nan
    return abs(_trap(ej[m], t[m]))


rows = []
for s in SIGMAS:
    t, ozp = load(s, "Omega_zp_int")
    if t is None:
        continue
    ip = int(np.argmax(ozp))
    t_peak = float(t[ip])
    _, jm = load(s, "Jmax")
    _, j2 = load(s, "J2_int")
    _, em = load(s, "emag_integral_vol")
    if j2 is None:
        continue
    ohm = j2 / float(s)          # η J² integrado en área, con η = 1/σ
    # Horizonte COMÚN t<=T_CAP: los runs tienen t_fin dispares (5.7...30);
    # sin tope común las integrales de las ventanas largas no son comparables.
    T_CAP = 15.0
    completa = t[-1] >= T_CAP - 0.5
    rec = dict(
        sigma=s,
        E_num=integral_ventana(t, ohm, t < T_NUM),
        E_lin=integral_ventana(t, ohm, (t >= T_NUM) & (t <= T_FIT_MAX)),
        E_turb=integral_ventana(t, ohm, (t > t_peak) & (t <= T_CAP))
               if completa else np.nan,
        E_tot=integral_ventana(t, ohm, t <= T_CAP) if completa else np.nan,
        t_peak=t_peak,
        Jmax_trans=float(np.nanmax(jm[t < 5.0])) if jm is not None else np.nan,
        emag_amp=float(np.nanmax(em) / em[0]) if em is not None else np.nan,
    )
    rows.append(rec)

S = np.array([r["sigma"] for r in rows], float)
print(f"runs con datos: {len(rows)}")

# valores de referencia para COSAS_POR_REPASAR (§4)
for sref in (6000, 10000):
    r = next((r for r in rows if r["sigma"] == sref), None)
    if r:
        print(f"σ={sref}: num={r['E_num']:.4g}  lin={r['E_lin']:.4g}  "
              f"turb={r['E_turb']:.4g}  tot={r['E_tot']:.4g}  "
              f"turb/lin={r['E_turb']/r['E_lin']:.1f}  t_peak={r['t_peak']:.2f}")

fig, ax = plt.subplots(1, 3, figsize=(13, 3.8))

# (a) corriente transitoria — igual a la variante de la lámina
J = np.array([r["Jmax_trans"] for r in rows])
ax[0].plot(S, J, "o-", ms=4, color="#7f8c8d")
ax[0].set_xscale("log"); ax[0].set_xlabel(r"$\sigma$"); ax[0].set_ylabel(r"$J_{\max}$")
ax[0].set_title(r"(a) Corriente transitoria $J_{\max}(t<5)$", fontsize=10)

# (b) disipación resistiva acumulada POR VENTANAS
VENTANAS = [
    ("E_num",  "#9e9e9e", "v", r"numérica $[0,\,2.4)$"),
    ("E_lin",  "#2e7d32", "o", r"lineal $[2.4,\,3.4]$"),
    ("E_turb", "#1565c0", "s", r"turbulenta $(t_{\rm peak},\,15]$"),
    ("E_tot",  "k",       "d", r"total $[0,\,15]$"),
]
for key, color, mk, lab in VENTANAS:
    V = np.array([r[key] for r in rows])
    # (ronda 3) las curvas turbulenta/total tienen NaN en los runs truncados
    # (no llegan a T_CAP); enmascararlos hace que la línea CONECTE los puntos
    # válidos en vez de dejar huecos. Los marcadores siguen mostrando dónde
    # SÍ hay dato medido; la línea sólo une esos puntos.
    m = np.isfinite(V)
    ax[1].plot(S[m], V[m], mk + "-", ms=3.5, lw=1.2, color=color, label=lab)
ax[1].set_xscale("log"); ax[1].set_yscale("log")
ax[1].set_xlabel(r"$\sigma$")
ax[1].set_ylabel(r"$\int\!\!\int \eta J^2\,dA\,dt$")
ax[1].set_title(r"(b) Disipación resistiva acumulada por ventana", fontsize=10)
ax[1].legend(fontsize=7, loc="upper left", framealpha=0.9)

# (c) amplificación de energía magnética
E = np.array([r["emag_amp"] for r in rows])
ax[2].plot(S, E, "^-", ms=4, color="#2ca02c")
ax[2].set_xscale("log"); ax[2].set_xlabel(r"$\sigma$")
ax[2].set_ylabel(r"$\max_t E_{\rm mag}/E_{\rm mag}(0)$")
ax[2].set_title(r"(c) Amplificación de energía magnética", fontsize=10)

fig.tight_layout()
fig.savefig(OUT)
plt.close(fig)
print("OK ->", OUT)
