import os, numpy as np
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
LAB=os.path.expanduser("~/Documents/Grado/INFO/lab")
BASE=os.path.join(LAB,"lab_offsetC","entornos_data_global")
OUT=os.path.expanduser("~/Documents/Grado/REPO_GH/presentacion/fig_comparacion_EJ_ohm.pdf")
trap=getattr(np,"trapezoid",None) or np.trapz
T_NUM,T_FITMAX,T_CAP=2.4,3.4,15.0
plt.rcParams.update({"font.family":"serif","mathtext.fontset":"cm","axes.grid":True,
  "grid.alpha":0.3,"font.size":10.5,"savefig.bbox":"tight","pdf.fonttype":42})
SIGMAS=[100,300,500,600,800,900,1000,1200,1400,1600,1800,2000,2200,2400,2600,2800,2950,
  3000,3050,3200,3400,3600,3800,4000,4500,5000,5500,6000,6200,6400,6500,6600,6800,7000,
  7400,7500,7600,8000,8500,9000,9500,10000,10250,10500]
def load(sig,name):
    f=f"{BASE}/run_sigma_{sig}/data_global/2d_data_{name}.dat"
    try:
        a=np.loadtxt(f); return (a[:,1],a[:,2]) if a.ndim==2 and len(a)>2 else (None,None)
    except: return None,None
def ws(t,y,m): 
    return trap(y[m],t[m]) if np.count_nonzero(m)>=2 else np.nan
rows=[]
for s in SIGMAS:
    t,ozp=load(s,"Omega_zp_int")
    if t is None: continue
    tp=float(t[int(np.argmax(ozp))]); _,j2=load(s,"J2_int"); _,ej=load(s,"EdotJ_int")
    if j2 is None or ej is None: continue
    ohm=j2/float(s); comp=t[-1]>=T_CAP-0.5
    W={"num":t<T_NUM,"lin":(t>=T_NUM)&(t<=T_FITMAX),"turb":(t>tp)&(t<=T_CAP),"tot":t<=T_CAP}
    r={"sigma":s}
    for k,m in W.items():
        ok = comp or k in ("num","lin")
        r["o_"+k]=abs(ws(t,ohm,m)) if ok else np.nan
        e=ws(t,ej,m) if ok else np.nan
        r["e_"+k]=e; r["ea_"+k]=abs(e)
    rows.append(r)
S=np.array([r["sigma"] for r in rows],float)
VEN=[("num","#9e9e9e","v",r"num. $[0,2.4)$"),("lin","#2e7d32","o",r"lineal $[2.4,3.4]$"),
     ("turb","#1565c0","s",r"turb. $(t_p,15]$"),("tot","k","d",r"total $[0,15]$")]
fig,ax=plt.subplots(1,3,figsize=(16,4.3))
def plot_win(a,pre,logy):
    for k,c,mk,lab in VEN:
        V=np.array([r[pre+k] for r in rows]); m=np.isfinite(V)
        a.plot(S[m],V[m],mk+"-",ms=3.3,lw=1.25,color=c,label=lab)
    a.set_xscale("log"); a.set_xlabel(r"$\sigma$")
    if logy: a.set_yscale("log")
# (a) ηJ² — correcta
plot_win(ax[0],"o_",True); ax[0].set_ylabel(r"$\iint \eta J^2\,dA\,dt$")
ax[0].set_title("(a) $\\eta J^2$ — irreversible, positivo\n(la de la presentación · CORRECTA)",fontsize=9.5)
ax[0].legend(fontsize=7,loc="lower right",framealpha=0.9)
# (b) E·J con signo
plot_win(ax[1],"e_",False); ax[1].axhline(0,color="red",lw=1,ls="--",alpha=0.7)
ax[1].set_ylabel(r"$\iint \mathbf{E}\cdot\mathbf{J}\,dA\,dt$ (con signo)")
ax[1].set_title("(b) $\\mathbf{E}\\cdot\\mathbf{J}$ crudo, con signo\n(revela el problema: es negativo)",fontsize=9.5)
ax[1].legend(fontsize=7,loc="lower left",framealpha=0.9)
# (c) |E·J| — la de la monografía
plot_win(ax[2],"ea_",True); ax[2].set_ylabel(r"$\left|\iint \mathbf{E}\cdot\mathbf{J}\,dA\,dt\right|$")
ax[2].set_title("(c) $|\\mathbf{E}\\cdot\\mathbf{J}|$ — la de la monografía\n(engañosa: crece monótona con $\\sigma$)",fontsize=9.5)
ax[2].legend(fontsize=7,loc="lower right",framealpha=0.9)
MARK=[(0,2950,r"$\\sigma^{\\!*}\\!\\approx\\!3000$"),(2,6000,r"$\\sigma^{\\!*}\\!\\approx\\!6000$")]
for kk,sc,lab in MARK:
    ax[kk].axvline(sc,color="crimson",ls=(0,(4,2)),lw=1.5,alpha=0.9,zorder=1)
    ax[kk].annotate(lab,xy=(sc,0.42),xycoords=("data","axes fraction"),rotation=90,va="center",ha="right",fontsize=8,color="crimson",fontweight="bold")
fig.tight_layout(); fig.savefig(OUT); print("OK ->",OUT)
