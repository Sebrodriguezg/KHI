#!/usr/bin/env python3
"""Video «sigue el guion» de la sustentación.

Réplica del pipeline del audiolibro de Electrodinámica Covariante
(edge-tts + ffmpeg, una locución por diapositiva):

  1. Extrae los parlamentos de ../guion/guion_sustentacion.tex.
  2. TTS por lámina con voz según ponente (edge-tts, + subtítulos VTT).
  3. Renderiza las páginas correspondientes de ../main.pdf.
  4. Un segmento MP4 por lámina (imagen fija + locución + pausa) y
     concatenación final con subtítulos incrustados (mov_text).

Uso:  python3 build_video.py [--solo-tts | --solo-video]
"""
import re
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
GUION_TEX = BASE.parent / "guion" / "guion_sustentacion.tex"
MAIN_PDF = BASE.parent / "main.pdf"
EDGE_TTS = Path("/home/sebastian/Downloads/Seminario_Electrodinamica_Covariante/tts_env/bin/edge-tts")

# Voz por ponente (mismas familias neuronales del audiolibro; intercambiables).
VOCES = {
    "Bryan Martinez": "es-CO-GonzaloNeural",
    "Sebastián Rodriguez": "es-MX-JorgeNeural",
}
RATE = "-5%"
PAUSA = 0.8          # silencio entre láminas [s]
FPS = 10
RES = "1920:1080"

# lámina del guion -> página de main.pdf (cuerpo 1..31; 32 = gracias, p. 36)
PAGINA = {n: n for n in range(1, 32)}
PAGINA[32] = 36

for d in ("texto", "audio", "slides", "seg"):
    (BASE / d).mkdir(exist_ok=True)


# ----------------------------------------------------------------- extracción
def detex(s: str) -> str:
    s = re.sub(r"\\emph\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\text[a-z]+\{([^}]*)\}", r"\1", s)
    s = s.replace("$", "").replace("~", " ")
    s = s.replace("---", ", ").replace("--", "-")
    s = re.sub(r"\\[a-zA-Z]+", "", s)
    s = s.replace("{", "").replace("}", "")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def extraer():
    tex = GUION_TEX.read_text(encoding="utf-8")
    pat = re.compile(
        r"\\lamina\{(\d+)\}\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}"
        r".*?\\begin\{parlamento\}\{([^}]*)\}(.*?)\\end\{parlamento\}",
        re.S)
    laminas = []
    for m in pat.finditer(tex):
        num, titulo, ponente = int(m.group(1)), m.group(2), m.group(3)
        texto = detex(m.group(7))
        assert "\\" not in texto, f"L{num}: queda LaTeX sin limpiar: {texto[:120]}"
        laminas.append((num, titulo, ponente, texto))
        (BASE / "texto" / f"{num:02d}.txt").write_text(texto + "\n", "utf-8")
    assert len(laminas) == 32, f"esperaba 32 láminas, hallé {len(laminas)}"
    return laminas


# ------------------------------------------------------------------------ tts
def tts(laminas):
    for num, _t, ponente, _x in laminas:
        mp3 = BASE / "audio" / f"{num:02d}.mp3"
        if mp3.exists() and mp3.stat().st_size > 0:
            print(f"-- {mp3.name} ya existe, se omite")
            continue
        voz = VOCES[ponente]
        print(f">> lámina {num:02d}  ({ponente} → {voz})")
        subprocess.run(
            [str(EDGE_TTS), "--voice", voz, f"--rate={RATE}",
             "-f", str(BASE / "texto" / f"{num:02d}.txt"),
             "--write-media", str(mp3),
             "--write-subtitles", str(BASE / "audio" / f"{num:02d}.vtt")],
            check=True)


# ------------------------------------------------------------------ segmentos
def dur(path: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(path)],
        capture_output=True, text=True, check=True).stdout.strip()
    return float(out)


def slides():
    for num, pag in PAGINA.items():
        png = BASE / "slides" / f"{num:02d}.png"
        if png.exists():
            continue
        subprocess.run(
            ["pdftoppm", "-png", "-r", "200", "-f", str(pag), "-l", str(pag),
             "-singlefile", str(MAIN_PDF), str(png.with_suffix(""))],
            check=True)
        print(f"slide {num:02d} <- página {pag}")


def segmentos(laminas):
    tiempos = []          # (num, inicio, dur_audio)
    t = 0.0
    lista = BASE / "seg" / "lista.txt"
    with lista.open("w") as fh:
        for num, _t_, _p, _x in laminas:
            mp3 = BASE / "audio" / f"{num:02d}.mp3"
            d = dur(mp3)
            total = d + PAUSA
            seg = BASE / "seg" / f"{num:02d}.mp4"
            if not seg.exists():
                print(f"segmento {num:02d}  ({total:6.1f}s)")
                subprocess.run(
                    ["ffmpeg", "-v", "error", "-y",
                     "-loop", "1", "-i", str(BASE / "slides" / f"{num:02d}.png"),
                     "-i", str(mp3),
                     "-t", f"{total:.3f}",
                     "-vf", f"scale={RES}:force_original_aspect_ratio=decrease,"
                            f"pad={RES}:(ow-iw)/2:(oh-ih)/2:color=white,"
                            "format=yuv420p",
                     "-r", str(FPS),
                     "-c:v", "libx264", "-tune", "stillimage",
                     "-preset", "veryfast", "-crf", "22",
                     "-af", "apad", "-shortest",
                     "-c:a", "aac", "-b:a", "128k", "-ar", "44100", "-ac", "2",
                     str(seg)], check=True)
            fh.write(f"file '{seg}'\n")
            tiempos.append((num, t, d))
            t += dur(seg)   # duración real del segmento codificado
    return tiempos


# ----------------------------------------------------------------- subtítulos
TS = re.compile(r"(\d+):(\d+):(\d+)[.,](\d+)")


def _seg2srt_ts(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int(seconds % 3600 // 60)
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")


def subtitulos(tiempos):
    idx, bloques = 1, []
    for num, inicio, _d in tiempos:
        vtt = BASE / "audio" / f"{num:02d}.vtt"
        if not vtt.exists():
            continue
        cue_t, cue_x = None, []
        for line in vtt.read_text("utf-8").splitlines() + [""]:
            if "-->" in line:
                a, b = [x.strip() for x in line.split("-->")]
                cue_t = tuple(
                    int(m[1]) * 3600 + int(m[2]) * 60 + int(m[3]) + int(m[4]) / 1000
                    for m in (TS.match(a), TS.match(b)))
                cue_x = []
            elif line.strip() and cue_t:
                cue_x.append(line.strip())
            elif not line.strip() and cue_t and cue_x:
                bloques.append(
                    f"{idx}\n{_seg2srt_ts(inicio + cue_t[0])} --> "
                    f"{_seg2srt_ts(inicio + cue_t[1])}\n" + " ".join(cue_x) + "\n")
                idx += 1
                cue_t = None
    (BASE / "subs.srt").write_text("\n".join(bloques), "utf-8")


# ---------------------------------------------------------------------- final
def concatenar():
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y",
         "-f", "concat", "-safe", "0", "-i", str(BASE / "seg" / "lista.txt"),
         "-i", str(BASE / "subs.srt"),
         "-c:v", "copy", "-c:a", "copy",
         "-c:s", "mov_text", "-metadata:s:s:0", "language=spa",
         "-movflags", "+faststart",
         str(BASE / "guion_sustentacion_video.mp4")], check=True)


def main():
    laminas = extraer()
    if "--solo-video" not in sys.argv:
        tts(laminas)
    if "--solo-tts" in sys.argv:
        return
    slides()
    tiempos = segmentos(laminas)
    subtitulos(tiempos)
    concatenar()
    total = sum(dur(BASE / "seg" / f"{n:02d}.mp4") for n, _, _ in tiempos)
    print(f"\nListo: guion_sustentacion_video.mp4  ({total/60:.1f} min)")
    with (BASE / "linea_de_tiempo.txt").open("w") as fh:
        for num, inicio, _d in tiempos:
            fh.write(f"{int(inicio//60):02d}:{int(inicio%60):02d}  lámina {num:02d}\n")


if __name__ == "__main__":
    main()
