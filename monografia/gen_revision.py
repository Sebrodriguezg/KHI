import re, datetime, subprocess, sys
order=[("sections/00_preliminares.tex","Preliminares","Resumen"),
("sections/01_introduction.tex","Cap. 1 — Introducción","(intro)"),
("sections/02_rrmhd_theory.tex","Cap. 2 — Teoría RRMHD","(intro)"),
("sections/03_KHI.tex","Cap. 3 — KHI","(intro)"),
("sections/04_numerical_methods.tex","Cap. 4 — Métodos numéricos","(intro)"),
("sections/setup_exp.tex","Cap. 5 — Setup experimental","(intro)"),
("sections/05_results_discussion.tex","Cap. 6 — Resultados","(intro)"),
("sections/06_conclusions.tex","Cap. 7 — Conclusiones","(intro)"),
("sections/07_appendices.tex","Anexos","(intro)")]
BASE="3656070"
def grab(t,s):
    d=1;i=s
    while i<len(t) and d>0: d+=(t[i]=='{')-(t[i]=='}'); i+=1
    return t[s:i-1]
def disp(s):
    s=re.sub(r'\\(emph|textit|textbf|texttt|text|mathbf|textsf)\{([^{}]*)\}',r'\2',s)
    s=s.replace('``','“').replace("''","”").replace('---','—').replace('\\dots','…')
    s=re.sub(r'\\(ref|eqref)\{[^}]*\}','(ref)',s); s=re.sub(r'\\S','§',s)
    s=re.sub(r'\\[a-zA-Z]+','',s); s=s.replace('{','').replace('}','')
    return re.sub(r'\s+',' ',s).strip()
def tcl(s): return re.sub(r'\\(emph|textit|textbf)\{([^{}]*)\}',r'\2',s).strip()
def notes(text,deflt):
    secs=[(m.start(),grab(text,m.end())) for m in re.finditer(r'\\(section|subsection|subsubsection|paragraph)\*?(?:\[[^\]]*\])?\{',text)]
    out=[]
    for m in re.finditer(r'\\(revnota|sebnota|brynota|claudenota|notebooknota)\{',text):
        body=grab(text,m.end()); cur=deflt
        for pos,t in secs:
            if pos<m.start(): cur=t
            else: break
        out.append((m.group(1),cur,body))
    return out
mtag={'revnota':'REV','sebnota':'SEB','brynota':'BRY','claudenota':'CLAUDE','notebooknota':'NLM'}
mcol={'REV':'red','SEB':'blue','BRY':'green!60!black','CLAUDE':'orange!80!black','NLM':'violet!70!black'}
# baseline (raw bodies) per chapter, assign global ID
baseline=[]; gid=0
for path,chap,deflt in order:
    bt=subprocess.run(["git","show",f"{BASE}:monografia/{path}"],capture_output=True,text=True).stdout
    for typ,sec,body in notes(bt,deflt):
        gid+=1; baseline.append([gid,chap,typ,sec,body])
# current raw bodies set
curbodies=[]; curnotes=[]
for path,chap,deflt in order:
    cur=open(path,encoding='utf-8').read()
    for typ,sec,body in notes(cur,deflt):
        curbodies.append(body.strip()); curnotes.append((chap,typ,sec,body))
curset=set(curbodies)
for r in baseline: r.append(r[4].strip() in curset)  # r[5]=pending(True)/closed(False)
# notas NUEVAS (post-baseline): ledger persistente -> ID fijo y ✅ al resolverse
import json,os
LEDGER="revision_ledger.json"
ledger=json.load(open(LEDGER,encoding='utf-8')) if os.path.exists(LEDGER) else {}
baseset=set(r[4].strip() for r in baseline)
maxid=max([gid]+[v["id"] for v in ledger.values()]) if ledger else gid
curpost={}  # body -> (chap,typ,sec,body)
for chap,typ,sec,body in curnotes:
    k=body.strip()
    if k in baseset: continue
    curpost[k]=(chap,typ,sec,body)
    if k in ledger: ledger[k].update(chap=chap,typ=typ,sec=sec,body=body)
    else: maxid+=1; ledger[k]={"id":maxid,"chap":chap,"typ":typ,"sec":sec,"body":body}
for k,v in ledger.items():  # incluye resueltas (no presentes en curpost) -> ✅
    baseline.append([v["id"],v["chap"],v["typ"],v["sec"],v["body"],k in curpost])
json.dump(ledger,open(LEDGER,"w",encoding='utf-8'),ensure_ascii=False,indent=1)
# ordenar por (capítulo según 'order', luego ID) para agrupar bien
chord={chap:i for i,(_,chap,_) in enumerate(order)}
baseline.sort(key=lambda r:(chord.get(r[1],99),r[0]))
rev=[r for r in baseline if r[2]!='notebooknota']
total=len(rev); closed=sum(1 for r in rev if not r[5]); pend=total-closed
nlm=sum(1 for r in baseline if r[2]=='notebooknota')
# ---- MD ----
o=["# Revisión de la monografía — tablero con ID fijo\n",
   f"*Actualizado: {datetime.date.today().isoformat()} · rama `revision-monografia`*\n",
   f"## 📊 {closed}/{total} cerradas ({100*closed//total}%) — pendientes {pend} · {nlm} notebooknotas (NLM, aparte)\n",
   "> **El # es FIJO** (no cambia aunque cerremos otras). ✅ = cerrada · ⬜ = pendiente.\n"]
last=None
for gid,chap,typ,sec,body,pending in baseline:
    if chap!=last:
        cc=sum(1 for r in baseline if r[1]==chap and r[2]!='notebooknota' and not r[5]); ct=sum(1 for r in baseline if r[1]==chap and r[2]!='notebooknota')
        o+=[f"\n## {chap}  — {cc}/{ct} cerradas\n","| # | Estado | Tipo | Sección | Qué dice |","|---|---|---|---|---|"]; last=chap
    st="🟣" if typ=='notebooknota' else ("⬜" if pending else "✅")
    o.append(f"| {gid} | {st} | {mtag[typ]} | {disp(sec)} | {disp(body).replace('|',chr(92)+'|')} |")
open("REVISION_NOTAS.md","w",encoding='utf-8').write("\n".join(o)+"\n")
# ---- PDF ----
hdr=r"""\documentclass[9pt]{extarticle}
\usepackage[T1]{fontenc}\usepackage[utf8]{inputenc}\usepackage{lmodern}
\usepackage[spanish]{babel}\usepackage{amsmath,amssymb,mathtools,bm}
\usepackage[table]{xcolor}\usepackage{longtable}\usepackage{array}
\usepackage[landscape,margin=1.1cm]{geometry}\usepackage{fancyhdr}
\providecommand{\gKHI}{\gamma_{\mathrm{KHI}}}\providecommand{\scrit}{\sigma_{\mathrm{crit}}}
\providecommand{\Rmst}{\mathrm{Rm}^{*}}\providecommand{\Ozp}{\Omega_{zp}}
\providecommand{\Omaxzp}{\Omega_{zp}^{\max}}\providecommand{\Otot}{\Omega_{\mathrm{tot}}}
\providecommand{\akh}{a_{kh}}\providecommand{\vsh}{v_{\mathrm{sh}}}\providecommand{\what}{\hat{\omega}}
\providecommand{\textcite}[1]{\textit{[cit]}}\providecommand{\parencite}[1]{\textit{[cit]}}\providecommand{\Rmst}{\mathrm{Rm}^{*}}
\renewcommand{\arraystretch}{1.2}\pagestyle{fancy}\fancyhf{}\rhead{\thepage}\lhead{Revisión KHI--RRMHD (ID fijo)}
\begin{document}\begin{center}{\Large\bfseries Revisión de la monografía — tablero con ID fijo}\\[2pt]"""
hdr+= f"DATE · \\textbf{{{closed}/{total} cerradas ({100*closed//total}\\%)}} · pendientes {pend}. \\textcolor{{gray}}{{Gris/✓ = cerrada.}} El \\# es fijo.\\end{{center}}\n\\vspace{{3pt}}\n"
hdr=hdr.replace("DATE",datetime.date.today().isoformat())
L=[hdr,r"\begin{longtable}{|p{0.5cm}|p{0.7cm}|p{1.2cm}|p{3.6cm}|p{17.0cm}|}",
   r"\hline \textbf{\#} & \textbf{Est.} & \textbf{Tipo} & \textbf{Sección} & \textbf{Qué dice / acción}\\ \hline\endhead"]
last=None
for gid,chap,typ,sec,body,pending in baseline:
    if chap!=last:
        cc=sum(1 for r in baseline if r[1]==chap and r[2]!='notebooknota' and not r[5]); ct=sum(1 for r in baseline if r[1]==chap and r[2]!='notebooknota')
        nn=sum(1 for r in baseline if r[1]==chap and r[2]=='notebooknota'); extra=(r" \ — %d NLM"%nn) if nn else ""
        L.append(r"\rowcolor{gray!22}\multicolumn{5}{|l|}{\textbf{%s} \ — %d/%d cerradas%s}\\ \hline"%(chap,cc,ct,extra)); last=chap
    if typ=='notebooknota':
        L.append(r"\rowcolor{violet!8}%d & \textcolor{violet!70!black}{$\bullet$} & \textcolor{%s}{\scriptsize\textbf{%s}} & {\scriptsize %s} & {\scriptsize %s}\\ \hline"%(gid,mcol['NLM'],'NLM',tcl(sec),body))
    elif pending:
        L.append(r"%d & $\square$ & \textcolor{%s}{\scriptsize\textbf{%s}} & {\scriptsize %s} & {\scriptsize %s}\\ \hline"%(gid,mcol[mtag[typ]],mtag[typ],tcl(sec),body))
    else:
        L.append(r"\rowcolor{black!8}%d & \textcolor{green!50!black}{$\checkmark$} & \textcolor{gray}{\scriptsize %s} & \textcolor{gray}{\scriptsize %s} & \textcolor{gray}{\scriptsize %s}\\ \hline"%(gid,mtag[typ],tcl(sec),body))
L+=[r"\end{longtable}",r"\end{document}"]
open("/tmp/revn.tex","w",encoding='utf-8').write("\n".join(L))
print(f"{closed}/{total} cerradas, {pend} pendientes")
