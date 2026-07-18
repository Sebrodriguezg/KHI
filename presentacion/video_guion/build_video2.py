#!/usr/bin/env python3
"""Video completo: guion (parte 1) + anexos del guion (parte 2) +
banco de preguntas (parte 3), con TTS multivoz y subtítulos.

Visual: parte 1 usa la lámina correspondiente; los anexos, la lámina que
cada respuesta referencia; el banco, la lámina/respaldo indicada en la
etiqueta de la pregunta o una tarjeta generada cuando no la hay.
"""
import re
import subprocess
import sys
import time
from pathlib import Path

BASE = Path(__file__).resolve().parent
PRES = BASE.parent
GUION = PRES / "guion" / "guion_sustentacion.tex"
BANCO = PRES / "banco_preguntas"
MAIN_PDF = PRES / "main.pdf"
EDGE = Path("/home/sebastian/Downloads/Seminario_Electrodinamica_Covariante/tts_env/bin/edge-tts")

VOZ_BRYAN = "es-CO-GonzaloNeural"
VOZ_SEBAS = "es-MX-JorgeNeural"
VOZ_JURADO = "es-CO-SalomeNeural"
RATE = "-5%"
FPS = 10
RES = "1920:1080"

# El interludio (p. 3 del PDF) corre +1 las páginas desde la lámina 3;
# la numeración de láminas del pie NO cambia (frame counter compensado).
PAG_GUION = {n: (n if n <= 2 else n + 1) for n in range(1, 32)}
PAG_GUION[32] = 37
PAG_ANEXO_A = [4, 9, 27, 8, 11, 45]      # A.1..A.6 del guion

for d in ("slides2", "audio2", "cards", "seg2"):
    (BASE / d).mkdir(exist_ok=True)


# ------------------------------------------------------------ util LaTeX
def read_group(s, i):
    """s[i] == '{' -> (contenido, indice tras '}')"""
    depth, j = 1, i + 1
    while depth:
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
        j += 1
    return s[i + 1:j - 1], j


MATH_SUB = [
    (r"\\hat\\omega", "omega sombrero"), (r"\\hat\s*\\omega", "omega sombrero"),
    (r"\\sigma", "sigma"), (r"\\gamma", "gamma"), (r"\\eta", "eta"),
    (r"\\rho", "rho"), (r"\\tau", "tau"), (r"\\Omega", "Omega"),
    (r"\\omega", "omega"), (r"\\beta", "beta"), (r"\\delta", "delta"),
    (r"\\theta", "theta"), (r"\\Gamma", "Gamma"), (r"\\mu", "mu"),
    (r"\\nu", "nu"), (r"\\lambda", "lambda"), (r"\\kappa", "kappa"),
    (r"\\Phi", "Fi"), (r"\\Psi", "Psi"), (r"\\alpha", "alfa"),
    (r"\\xi", "xi"), (r"\\pi", "pi"),
    (r"\\pm", " más menos "), (r"\\mp", " menos más "),
    (r"\\to", " tiende a "), (r"\\infty", " infinito"),
    (r"\\ge", " mayor o igual que "), (r"\\le", " menor o igual que "),
    (r"\\gg", " mucho mayor que "), (r"\\ll", " mucho menor que "),
    (r"\\approx", " aproximadamente "), (r"\\simeq", " aproximadamente "),
    (r"\\sim", " del orden de "), (r"\\propto", " proporcional a "),
    (r"\\times", " por "), (r"\\cdot", " punto "), (r"\\in", " en "),
    (r"\\perp", " perpendicular"), (r"\\parallel", " paralelo"),
    (r"\\nabla", " nabla "), (r"\\partial", " derivada parcial "),
    (r"\\sqrt\s*2", " raíz de dos"), (r"\\sqrt", " raíz de "),
    (r"\\int", " integral de "), (r"\\max", " máximo"), (r"\\min", " mínimo"),
    (r"\\tanh", " tangente hiperbólica "), (r"\\langle", ""), (r"\\rangle", ""),
    (r"\\star", " estrella "), (r"\\circ", " grados"), (r"\\,", ""),
    (r"\\;", " "), (r"\\!", ""), (r"\\ ", " "), (r"\\%", " por ciento"),
]


def speak_math(m):
    s = m
    s = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"\1 sobre \2", s)
    s = re.sub(r"\\(?:mathbf|mathrm|rm|bm|boldsymbol|text|mathcal)\s*", "", s)
    s = re.sub(r"\^\{\\max\}", " máximo ", s)
    for pat, rep in MATH_SUB:
        s = re.sub(pat, rep, s)
    s = s.replace("+", " más ")
    s = s.replace("^2", " al cuadrado").replace("^4", " a la cuarta")
    s = re.sub(r"\^\{?-1/2\}?", " a la menos un medio", s)
    s = re.sub(r"\^\{?1/2\}?", " a la un medio", s)
    s = re.sub(r"\^\{([^{}]*)\}", r" a la \1 ", s)
    s = re.sub(r"\^(\S)", r" a la \1 ", s)
    s = re.sub(r"_\{([^{}]*)\}", r" sub \1 ", s)
    s = re.sub(r"_(\S)", r" sub \1 ", s)
    s = s.replace("=", " igual a ").replace("<", " menor que ")
    s = s.replace(">", " mayor que ")
    s = s.replace("|", " ").replace("(", " ").replace(")", " ")
    s = s.replace("{", " ").replace("}", " ").replace("[", " ").replace("]", " ")
    s = re.sub(r"\\[a-zA-Z]+", " ", s)
    s = s.replace("/", " sobre ")
    return re.sub(r"\s+", " ", s).strip()


def speak(texto):
    """LaTeX (prosa + $math$) -> español hablado."""
    s = texto
    for _ in range(3):
        s = re.sub(r"\\(?:emph|textbf|textit|texttt|text)\{([^{}]*)\}",
                   r"\1", s)
    s = re.sub(r"\$([^$]*)\$", lambda m: " " + speak_math(m.group(1)) + " ", s)
    s = s.replace("~", " ").replace("\\&", " y ").replace("\\%", " por ciento")
    s = s.replace("---", ", ").replace("--", "-")
    s = s.replace("\\'a", "á").replace("\\'e", "é").replace("\\'i", "í")
    s = s.replace("\\'o", "ó").replace("\\'u", "ú").replace("\\~n", "ñ")
    s = s.replace("``", "«").replace("''", "»")
    s = re.sub(r"\\[a-zA-Z]+\*?", " ", s)
    s = s.replace("{", "").replace("}", "")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n", "\n\n", s)
    return s.strip()


# ------------------------------------------------------------ fuentes
def parse_guion_parte1():
    tex = GUION.read_text("utf-8")
    pat = re.compile(
        r"\\lamina\{(\d+)\}\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}"
        r".*?\\begin\{parlamento\}\{([^}]*)\}(.*?)\\end\{parlamento\}", re.S)
    out = []
    for m in pat.finditer(tex):
        out.append((int(m.group(1)), m.group(3), m.group(7)))
    assert len(out) == 32
    return out


def parse_anexo_a():
    tex = GUION.read_text("utf-8")
    a = tex.split("Anexo A --- Respuestas ensayadas")[1]
    a = a.split("\\section{Anexo B")[0]
    bloques = re.split(r"\\subsection\{", a)[1:]
    out = []
    for b in bloques:
        tit, j = read_group("{" + b, 0)
        cuerpo = b[j - 1:]
        cuerpo = re.sub(r"\\emph\{\(.*?\)\}", "", cuerpo, flags=re.S)
        out.append((tit, cuerpo.strip()))
    assert len(out) == 6, len(out)
    return out


ANEXO_B_TEXTO = (
    "Cierre de los anexos: el mapa del material de respaldo. "
    "El respaldo B1 desarrolla el tensor de Faraday desde el cuadripotencial; "
    "B2, el tensor de energía momento por la vía de Hilbert; "
    "B3, el sistema GLM desde la acción extendida y su relación con la forma "
    "de Dedner; B4, el espectro característico del jacobiano de catorce por "
    "catorce y la estabilidad temporal; B5, el álgebra completa de la "
    "proyección tres más uno de la ley de Ohm; B6, la validación del "
    "solucionador de la teoría lineal contra Michalke; B7, la comparación "
    "entre HLL con MP5 y HLLC; B8, la estadística del ajuste sigmoide; "
    "B9, el fundamento cinético del continuo, de Vlasov al fluido; "
    "B10, los recursos computacionales; B11, las estructuras secundarias y "
    "la campaña C; B12, los mapas de densidad de las campañas magnéticas; "
    "y B13, el tablero dinámico de la campaña B. "
    "La lámina de referencias contiene las cuarenta y cuatro fuentes de la "
    "monografía.")


def parse_banco():
    """[(categoria, [(tag, pregunta, respuesta), ...]), ...]"""
    cats = []
    for f in ("parte_a.tex", "parte_b.tex", "parte_c.tex"):
        s = (BANCO / f).read_text("utf-8")
        i = 0
        while True:
            msec = re.compile(r"\\section\{").search(s, i)
            mq = re.compile(r"\\Q\{").search(s, i)
            if msec and (not mq or msec.start() < mq.start()):
                nom, i = read_group(s, msec.end() - 1)
                cats.append((nom, []))
                continue
            if not mq:
                break
            tag, j = read_group(s, mq.end() - 1)
            preg, j = read_group(s, s.index("{", j))
            ma = re.compile(r"\\A\{").search(s, j)
            resp, i = read_group(s, ma.end() - 1)
            cats[-1][1].append((tag, preg, resp))
    return cats


def pagina_de_tag(tag):
    m = re.search(r"l[áa]minas?\s+(\d+)", tag)
    if m:
        n = int(m.group(1))
        return n if n <= 2 else n + 1
    m = re.search(r"respaldo B(\d+)", tag)
    if m:
        return 38 + int(m.group(1))
    return None


# ------------------------------------------------------------ tarjetas
def gen_cards(cats, preguntas_sueltas):
    """Tarjetas beamer: divisores + categorías + preguntas sin lámina."""
    frames = []

    def card(kind, big, small=""):
        frames.append((kind, big, small))

    card("div", "Anexos del Guion",
         "Respuestas ensayadas de sesenta segundos (A.1--A.6) y mapa del "
         "material de respaldo")
    card("div", "Banco de Preguntas",
         f"{len(cats)} categorías · "
         f"{sum(len(qs) for _, qs in cats)} preguntas con respuesta")
    for k, (nom, qs) in enumerate(cats, 1):
        card("cat", f"Categoría {k}", f"{nom} · {len(qs)} preguntas")
    for num, tag, preg in preguntas_sueltas:
        card("q", f"Pregunta {num}", preg + f"\\\\[0.4cm]{{\\small\\color{{gris}}{tag}}}")

    tex = [r"""\documentclass[aspectratio=169,11pt]{beamer}
\usepackage[utf8]{inputenc}\usepackage[T1]{fontenc}
\usepackage[spanish,es-tabla]{babel}\usepackage{lmodern}
\usepackage{tikz}
\definecolor{primary}{HTML}{1B0C41}\definecolor{accent}{HTML}{E65D2F}
\definecolor{gold}{HTML}{F5B841}\definecolor{soft}{HTML}{F7F1E1}
\definecolor{gris}{HTML}{888888}
\setbeamertemplate{navigation symbols}{}
\begin{document}"""]
    for kind, big, small in frames:
        if kind in ("div", "cat"):
            tex.append(
                "\\begin{frame}[plain]\\begin{tikzpicture}[remember picture,overlay]"
                "\\fill[primary] (current page.south west) rectangle (current page.north east);"
                "\\fill[accent] ([yshift=-0.44\\paperheight]current page.north west)"
                " rectangle ([yshift=-0.47\\paperheight]current page.north east);"
                "\\end{tikzpicture}\\begin{center}\\vspace{1.2cm}"
                f"{{\\color{{soft}}\\LARGE\\bfseries {big}}}\\\\[0.9cm]"
                f"{{\\color{{gold}}\\normalsize {small}}}"
                "\\end{center}\\end{frame}")
        else:
            tex.append(
                "\\begin{frame}[plain]\\vspace{0.4cm}\\begin{center}"
                f"{{\\color{{accent}}\\Large\\bfseries {big}}}\\\\[0.12cm]"
                "{\\color{primary}\\rule{0.55\\textwidth}{1.2pt}}\\\\[0.6cm]"
                "\\begin{minipage}{0.86\\textwidth}\\centering\\large "
                + small +
                "\\end{minipage}\\end{center}\\end{frame}")
    tex.append("\\end{document}")

    (BASE / "cards" / "cards.tex").write_text("\n".join(tex), "utf-8")
    for _ in range(2):   # doble pasada: overlays tikz (remember picture)
        subprocess.run(["pdflatex", "-interaction=nonstopmode", "cards.tex"],
                       cwd=BASE / "cards", stdout=subprocess.DEVNULL,
                       check=True)
    subprocess.run(["pdftoppm", "-png", "-r", "200", "cards.pdf", "card"],
                   cwd=BASE / "cards", check=True)
    pngs = sorted((BASE / "cards").glob("card-*.png"))
    assert len(pngs) == len(frames), (len(pngs), len(frames))
    return pngs


# ------------------------------------------------------------ pipeline
def dur(p):
    return float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(p)], capture_output=True, text=True,
        check=True).stdout.strip())


def render_paginas():
    for p in range(1, 52):
        png = BASE / "slides2" / f"page_{p:02d}.png"
        if not png.exists():
            subprocess.run(
                ["pdftoppm", "-png", "-r", "200", "-f", str(p), "-l", str(p),
                 "-singlefile", str(MAIN_PDF), str(png.with_suffix(""))],
                check=True)
    print("páginas del deck renderizadas")


def tts(txt_path, mp3, vtt, voz, reintentos=3):
    for k in range(reintentos):
        try:
            subprocess.run(
                [str(EDGE), "--voice", voz, f"--rate={RATE}",
                 "-f", str(txt_path), "--write-media", str(mp3),
                 "--write-subtitles", str(vtt)], check=True,
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if mp3.exists() and mp3.stat().st_size > 0:
                return
        except subprocess.CalledProcessError:
            pass
        time.sleep(4 * (k + 1))
    raise RuntimeError(f"TTS falló: {mp3.name}")


def main():
    render_paginas()
    parte1 = parse_guion_parte1()
    anexo_a = parse_anexo_a()
    cats = parse_banco()

    # ---------- programa: (id, png, texto_hablado, voz, pausa)
    programa = []
    for num, ponente, texto in parte1:
        voz = VOZ_BRYAN if "Bryan" in ponente else VOZ_SEBAS
        png = BASE / "slides2" / f"page_{PAG_GUION[num]:02d}.png"
        programa.append((f"g{num:02d}", png, speak(texto), voz, 0.8))

    # tarjetas
    sueltas, qn = [], 0
    for nom, qs in cats:
        for tag, preg, _r in qs:
            qn += 1
            if pagina_de_tag(tag) is None:
                sueltas.append((qn, tag, preg))
    cards = gen_cards(cats, sueltas)
    idx_div_anexos, idx_div_banco = 0, 1
    idx_cat = {k: 2 + k for k in range(len(cats))}
    idx_q = {num: 2 + len(cats) + i for i, (num, _t, _p) in enumerate(sueltas)}

    programa.append(("div_anexos", cards[idx_div_anexos],
                     "Anexos del guion: las seis respuestas ensayadas de "
                     "sesenta segundos para el turno de preguntas, y el mapa "
                     "del material de respaldo.", VOZ_JURADO, 0.8))
    for k, (tit, cuerpo) in enumerate(anexo_a, 1):
        png = BASE / "slides2" / f"page_{PAG_ANEXO_A[k-1]:02d}.png"
        texto = f"Respuesta ensayada {k}. {speak(tit)}. {speak(cuerpo)}"
        voz = VOZ_BRYAN if k % 2 else VOZ_SEBAS
        programa.append((f"anexoA{k}", png, texto, voz, 0.8))
    programa.append(("anexoB", BASE / "slides2" / "page_38.png",
                     ANEXO_B_TEXTO, VOZ_BRYAN, 1.0))

    programa.append(("div_banco", cards[idx_div_banco],
                     f"Banco de preguntas para la sustentación: "
                     f"{len(cats)} categorías y {qn} preguntas con su "
                     "respuesta. Las preguntas las formula una voz; las "
                     "respuestas alternan entre los dos ponentes.",
                     VOZ_JURADO, 1.0))
    qn = 0
    for c, (nom, qs) in enumerate(cats):
        programa.append((f"cat{c+1:02d}", cards[idx_cat[c]],
                         f"Categoría {c+1}: {speak(nom)}. "
                         f"{len(qs)} preguntas.", VOZ_JURADO, 0.8))
        for tag, preg, resp in qs:
            qn += 1
            pag = pagina_de_tag(tag)
            png = (BASE / "slides2" / f"page_{pag:02d}.png") if pag \
                else cards[idx_q[qn]]
            programa.append((f"q{qn:03d}", png,
                             f"Pregunta {qn}. {speak(preg)}",
                             VOZ_JURADO, 0.3))
            voz = VOZ_BRYAN if qn % 2 else VOZ_SEBAS
            programa.append((f"a{qn:03d}", png, speak(resp), voz, 1.0))

    # ---------- TTS
    for i, (iid, _png, texto, voz, _p) in enumerate(programa):
        mp3 = BASE / "audio2" / f"{iid}.mp3"
        if iid.startswith("g"):           # parte 1: reutiliza el audio previo
            viejo = BASE / "audio" / f"{iid[1:]}.mp3"
            if viejo.exists() and not mp3.exists():
                mp3.symlink_to(viejo)
                vtt_v = BASE / "audio" / f"{iid[1:]}.vtt"
                if vtt_v.exists():
                    (BASE / "audio2" / f"{iid}.vtt").symlink_to(vtt_v)
                continue
        if mp3.exists() and mp3.stat().st_size > 0:
            continue
        txt = BASE / "audio2" / f"{iid}.txt"
        txt.write_text(texto + "\n", "utf-8")
        print(f">> TTS {i+1}/{len(programa)}  {iid}")
        tts(txt, mp3, BASE / "audio2" / f"{iid}.vtt", voz)

    # ---------- segmentos
    lista = BASE / "seg2" / "lista.txt"
    tiempos, t = [], 0.0
    with lista.open("w") as fh:
        for iid, png, _x, _v, pausa in programa:
            mp3 = BASE / "audio2" / f"{iid}.mp3"
            seg = BASE / "seg2" / f"{iid}.mp4"
            if not seg.exists():
                total = dur(mp3) + pausa
                subprocess.run(
                    ["ffmpeg", "-v", "error", "-y",
                     "-loop", "1", "-i", str(png), "-i", str(mp3),
                     "-t", f"{total:.3f}",
                     "-vf", f"scale={RES}:force_original_aspect_ratio=decrease,"
                            f"pad={RES}:(ow-iw)/2:(oh-ih)/2:color=white,"
                            "format=yuv420p",
                     "-r", str(FPS), "-c:v", "libx264", "-tune", "stillimage",
                     "-preset", "veryfast", "-crf", "22",
                     "-af", "apad", "-shortest",
                     "-c:a", "aac", "-b:a", "128k", "-ar", "44100", "-ac", "2",
                     str(seg)], check=True)
            fh.write(f"file '{seg}'\n")
            tiempos.append((iid, t))
            t += dur(seg)

    # ---------- subtítulos
    TS = re.compile(r"(\d+):(\d+):(\d+)[.,](\d+)")

    def srt_ts(x):
        h, m2 = int(x // 3600), int(x % 3600 // 60)
        return f"{h:02d}:{m2:02d}:{x % 60:06.3f}".replace(".", ",")

    idx, bloques = 1, []
    for iid, ini in tiempos:
        vtt = BASE / "audio2" / f"{iid}.vtt"
        if not vtt.exists():
            continue
        cue_t, cue_x = None, []
        for line in vtt.read_text("utf-8").splitlines() + [""]:
            if "-->" in line:
                a, b = [x.strip() for x in line.split("-->")]
                ma_, mb_ = TS.match(a), TS.match(b)
                if ma_ and mb_:
                    cue_t = tuple(int(m[1]) * 3600 + int(m[2]) * 60 +
                                  int(m[3]) + int(m[4]) / 1000
                                  for m in (ma_, mb_))
                    cue_x = []
            elif line.strip() and cue_t:
                cue_x.append(line.strip())
            elif not line.strip() and cue_t and cue_x:
                bloques.append(f"{idx}\n{srt_ts(ini + cue_t[0])} --> "
                               f"{srt_ts(ini + cue_t[1])}\n"
                               + " ".join(cue_x) + "\n")
                idx += 1
                cue_t = None
    (BASE / "subs2.srt").write_text("\n".join(bloques), "utf-8")

    # ---------- concatenación
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y",
         "-f", "concat", "-safe", "0", "-i", str(lista),
         "-i", str(BASE / "subs2.srt"),
         "-c:v", "copy", "-c:a", "copy",
         "-c:s", "mov_text", "-metadata:s:s:0", "language=spa",
         "-movflags", "+faststart",
         str(BASE / "guion_sustentacion_video.mp4")], check=True)

    with (BASE / "linea_de_tiempo.txt").open("w") as fh:
        for iid, ini in tiempos:
            fh.write(f"{int(ini//3600)}:{int(ini%3600//60):02d}:"
                     f"{int(ini%60):02d}  {iid}\n")
    total = t / 60
    print(f"\nListo: guion_sustentacion_video.mp4  ({total:.1f} min, "
          f"{len(programa)} segmentos)")


if __name__ == "__main__":
    main()
