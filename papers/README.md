# `papers/` — terreno preparado para publicar

Rama **`papers`**. Aquí vive todo lo necesario para convertir la monografía
(`monografia/`, 167 pp, español) en uno o dos artículos para
**MNRAS** y/o **The Open Journal of Astrophysics**.

**Estado: andamiaje listo. No hay texto del artículo escrito todavía — esa es la
siguiente tarea, y es de ustedes.**

---

## Por dónde empezar (15 minutos de lectura, en este orden)

| # | Archivo | Qué responde |
|---|---|---|
| 0 | `manuales/MNRAS_instrucciones.md` | Qué exige MNRAS (resumen operativo de la web oficial) |
| 0 | `manuales/OJAP_instrucciones.md` | Qué exige OJAp |
| 1 | **`01_COMPARATIVA_Y_ESTRATEGIA.md`** | **A cuál enviamos, y por qué. Tiene una decisión pendiente que bloquea todo lo demás** |
| 2 | **`02_PLAN_EXTRACCION.md`** | **El documento central: qué sale de qué capítulo, qué se recorta, qué hay que escribir de cero** |
| 3 | `03_INVENTARIO_FIGURAS.md` | Cuáles de las 47 figuras sobreviven (~12) y qué hay que hacerles |
| 4 | `04_ESTILO_INGLES.md` | Inglés británico, notación MNRAS y glosario ES→EN del proyecto |
| 5 | `05_CHECKLIST_ENVIO.md` | Checklist punto por punto antes de darle a "enviar" |

## Estructura

```
papers/
├── README.md                          este archivo
├── 01_COMPARATIVA_Y_ESTRATEGIA.md     MNRAS vs. OJAp + recomendación
├── 02_PLAN_EXTRACCION.md              monografía → artículo, sección por sección
├── 03_INVENTARIO_FIGURAS.md           47 figuras → ~12, con veredicto
├── 04_ESTILO_INGLES.md                estilo, notación y glosario ES→EN
├── 05_CHECKLIST_ENVIO.md              checklist de envío
│
├── manuales/
│   ├── MNRAS_instrucciones.md         resumen operativo (consultado 2026-09-17)
│   ├── OJAP_instrucciones.md          resumen operativo (consultado 2026-09-17)
│   └── ojap_for_authors_2026-09-17.txt  transcripción literal de la web de OJAp
│
├── mnras/                             ESQUELETO LISTO Y COMPILANDO
│   ├── main.tex                       estructura completa con \todo{} y punteros
│   ├── build.sh                       pdflatex + bibtex + pdflatex ×2
│   ├── mnras.cls, mnras.bst           oficiales, de CTAN
│   ├── mnras_guide.pdf                manual de la clase (MNRAS)
│   ├── mnras_template.tex             plantilla oficial intacta, de referencia
│   ├── README_CTAN.txt                readme del paquete CTAN
│   ├── references.bib                 copia de la monografía (ver NOTAS_BIBTEX)
│   └── figures/                       figuras ya traducidas y redimensionadas
│
├── ojap/                              ESQUELETO LISTO Y COMPILANDO
│   ├── main.tex
│   ├── build.sh
│   ├── openjournal.cls                oficial, descargada de la revista
│   ├── references.bib
│   └── figures/
│
└── comun/
    ├── DATA_AVAILABILITY.md           borrador + decisiones pendientes
    ├── DECLARACION_IA.md              borrador (obligatorio en ambas revistas)
    ├── COVER_LETTER_MNRAS.md          borrador de carta de presentación
    ├── NOTAS_BIBTEX.md                biblatex/biber → natbib/bibtex
    ├── references.bib                 copia maestra
    ├── inventario_figuras_auto.tsv    las 47 figuras con leyenda completa
    └── regen_inventario.py            regenera el TSV desde monografia/sections/
```

## Compilar

```bash
cd papers/mnras && ./build.sh    # -> main.pdf (MNRAS, 2 columnas, Times)
cd papers/ojap  && ./build.sh    # -> main.pdf (OJAp, estilo ApJ)
```

Ambos esqueletos **compilan hoy, sin errores**. Los `\todo{...}` salen impresos en
negrita dentro del PDF: es intencional, para que se vea de un vistazo qué falta.
Las figuras se resuelven vía `\graphicspath` contra `../../monografia/figuras/`,
así que se pueden probar sin copiar nada.

## Las tres decisiones que bloquean la escritura

1. **¿MNRAS o OJAp?** Depende sobre todo del APC: **£2.356 vs. £0**.
   Hay que averiguar si la UD tiene acuerdo con OUP y si Colombia califica para
   waiver. → `01_COMPARATIVA_Y_ESTRATEGIA.md`
2. **¿Un artículo o dos?** La recomendación es **uno** (barrido en σ), con la
   campaña magnética como sección corta. → `01_COMPARATIVA_Y_ESTRATEGIA.md` §4
3. **Autoría**: orden, autor de correspondencia, ORCID, y el permiso del director
   sobre cómo citar y/o liberar el código *Cueva*. → `05_CHECKLIST_ENVIO.md` §A

## Lo que no es extracción, sino trabajo nuevo

Está detallado en `02_PLAN_EXTRACCION.md` §7, pero conviene tenerlo presente
desde el primer día porque es lo que más tiempo va a costar:

- **Revisión bibliográfica actual** (la monografía cita poco trabajo previo de
  KHI-RRMHD; un artículo necesita 50–80 referencias vigentes).
- **Validación contra un resultado publicado** (¿reproduce *Cueva* el test 35A de
  Mizuno en el límite ideal?). Un árbitro lo va a pedir.
- **Convergencia de malla**: todo el barrido es 512×256.
- **Traducir y regenerar las figuras** desde sus scripts (no editando los PDF).
- **Alt text** de cada figura (requisito MNRAS).
- Decidir si entran los **diagnósticos de lámina de corriente** (`E_rec`,
  `nsheet`, η|J_z|), que hoy no están en la monografía y que reforzarían la
  afirmación de reconexión.

---

*Las instrucciones de ambas revistas se consultaron el **2026-09-17**. Las tarifas,
los plazos y la lista de palabras clave cambian: **reverificar en la web antes de
enviar**.*
