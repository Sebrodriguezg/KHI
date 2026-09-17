# MNRAS — Instrucciones para autores (resumen operativo)

> Fuente: <https://academic.oup.com/mnras/pages/General_Instructions>
> Consultada el **2026-09-17**. Las cifras de APC y los plazos cambian cada año:
> **verificar en la web antes de enviar**.

---

## 1. Qué es y qué acepta

*Monthly Notices of the Royal Astronomical Society*. Revisión por pares,
**totalmente Open Access** (desde 2024 no hay ruta suscripción). Publica la RAS,
produce Oxford University Press. Cualquiera puede enviar: no hay restricción por
nacionalidad, afiliación ni titulación — **un trabajo de grado de la UD es
perfectamente elegible**.

### Tipos de artículo

| Tipo | Límite | Notas |
|---|---|---|
| **Paper** | Sin límite estricto de páginas; se premia la concisión | El tipo que nos corresponde |
| **Letter** | **≤ 5 páginas** | No cuentan título, autores, afiliaciones, resumen, palabras clave, *data availability*, agradecimientos ni referencias. Sí cuentan los apéndices. Publicación en ≤ 30 días. Hay que **justificar** el formato Letter al enviar |
| **Correction** | — | Para errores propios en un artículo ya publicado. Sin APC |

## 2. Costos (tarifas 2025/26 — reconfirmar)

- **Paper: £2.356** (no miembros); **−20 %** con membresía RAS.
- **Letter: £1.122** (no miembros); **−20 %** con membresía RAS.
- Vías de financiación:
  1. **Read & Publish** — si la institución tiene acuerdo con OUP, el APC se cubre.
  2. **Exención por país de ingreso bajo/medio** — *Colombia entra en la lista de
     países con descuento/waiver de OUP; hay que confirmarlo con la lista vigente.*
  3. **Waiver discrecional** caso por caso, vía formulario.
- ⚠️ **La solicitud de waiver NO se menciona en la carta de presentación**: va por
  un canal separado para no contaminar la evaluación editorial.

## 3. Envío

- Plataforma: **ScholarOne Manuscripts** — <http://mc.manuscriptcentral.com/mnras>.
  Solo electrónico. Proceso de siete pasos.
- **Se sube un PDF/PS compilado**, no el `.tex` crudo. Figuras y tablas
  **embebidas** en ese único archivo.
- Tamaños: manuscrito **≤ 10 MB**; total de archivos subidos **≤ 350 MB**.
- Si se compila con pdfTeX, incluir `\pdfminorversion=5` para evitar problemas de
  compatibilidad con ScholarOne.
- Existe **plantilla en Overleaf** con envío directo a ScholarOne.
- Fuente de la clase: CTAN, `macros/latex/contrib/mnras`
  (`mnras.cls`, `mnras.bst`, `mnras_guide.pdf`, `mnras_template.tex`).
  → **Ya están copiados en `papers/mnras/`.**

## 4. Estructura del manuscrito

- **Título**: informativo; evitar acrónimos oscuros.
- **Autores + afiliaciones completas**; autor de correspondencia con e-mail
  (como nota al pie).
- **Resumen**: **≤ 250 palabras** (Paper) / ≤ 200 (Letter). **Un solo párrafo**.
  Debe resumir objetivos, métodos y resultados nuevos.
- **Palabras clave**: **entre 1 y 6**, obligatoriamente de la lista oficial MNRAS,
  separadas por guiones largos.
- **Secciones numeradas**: 1 = Introduction … última = Conclusions. Subsecciones
  permitidas (1, 2.1, 2.1.1).
- **Data availability**: **obligatorio**, con título propio, **después** de los
  agradecimientos.
- Ecuaciones numeradas; todas las páginas numeradas; figuras y tablas citadas en
  orden numérico correcto.
- *Author contribution statement*: opcional, en prosa, dentro de Acknowledgements.
- Reconocimiento a instalaciones/telescopios/clústeres: en Acknowledgements, **no**
  en notas al pie.

## 5. Figuras

- Formato preferido: **EPS** (con preview PC). Alternativas: **PDF**, **TIFF**.
- Resolución (al tamaño final):
  - fotografías / medios tonos: **300 ppi**
  - figuras mixtas línea+tono: **800 ppi**
  - Ejemplo a una columna (≈ 80 mm = 3,15 in): ≥ 945 px (foto) / ≥ 2500 px (mixta).
  - **Vectorial (PDF/EPS) evita todo esto** — es nuestro caso: casi todas las
    figuras de la monografía ya son PDF vectorial de matplotlib/TikZ.
- Grosor mínimo de línea: **0,3 pt** al tamaño final. Fuente recomendada: **8 pt**.
- Ejes rotulados **con unidades**; paneles etiquetados (a), (b), …; marco en los
  cuatro lados con marcas fiduciales en todos los bordes.
- **Accesibilidad daltónica**: evitar combinaciones rojo–verde.
- **Alt text obligatorio** para cada figura: se pone bajo la leyenda como
  `Alt text: ...` (no sale en el PDF tipográfico, solo en lectores).
- Una figura por archivo, nombres descriptivos (`fig6.eps`).
- Vídeos/animaciones: `.mp4`. Modelos 3D: formatos Sketchfab, ≤ 50 MB,
  2048×1024 px, con imagen fija representativa.

## 6. Tablas

- Solo **líneas horizontales** (arriba, abajo y bajo los encabezados de columna).
  **Nunca líneas verticales.**
- Sin color ni sombreado de celdas (no se soporta en la versión web): usar negrita
  o símbolos en superíndice.
- Tablas largas: **5–10 filas de muestra** en el texto y la tabla completa como
  material suplementario online. Se anima a depositarla en **VizieR (CDS)**.
  → *Aplica directo a nuestra Tabla canónica del barrido (44 filas).*

## 7. Referencias — Harvard (autor–año)

Citación en texto:

- Un autor: `J. Brown 1999`
- Dos: `J. Brown & P. Jones 1991`
- Tres, primera vez: `J. Brown, P. Jones & A. Smith 1994`; luego `J. Brown et al. 1994`
- Varias: `(A. Smith et al. 1990; J. Brown et al. 1995)` — por fecha, con punto y coma.

Lista de referencias:

- Orden **alfabético**. Sin negrita ni cursiva. **Sin coma tras el apellido**.
  **Sin `&`** entre los dos últimos autores.
- **≤ 8 autores: se listan todos**; **> 8: primer autor + et al.**
- Ejemplos canónicos:
  - Artículo: `Eke V., Cole S., Frenk C.S., 1996, MNRAS, 282, 263`
  - Libro: `Peebles P. J. E., 1980, The Large-Scale Structure of the Universe. Princeton Univ. Press, Princeton, NJ`
  - Actas: `Smith A., 2000, in Minh Y.C., van Dishoeck E.F., eds, Proc. IAU Symp. 197, ... Astron. Soc. Pac., San Francisco, p. 210`
  - Preprint: `Smith P. et al., 2013, preprint (arXiv:0123.45678)`
  - Software: `Brown J., 2015, Astrophysics Source Code Library, record ascl:1234.567`
- Nombres de revista abreviados (MNRAS, ApJ, A&A, PASP, AJ, ApJS, PASJ, …).
- 👉 **`mnras.bst` con `natbib` hace todo esto solo.** Ver `papers/comun/NOTAS_BIBTEX.md`.

## 8. Unidades y notación (lo que nos afecta)

- Unidades en **redonda**, con espacio irrompible: `200 keV`, no `200keV`.
- **Exponente negativo, no barra**: `km s^-1`, nunca `km/s`.
- `per cent` en el texto (con espacio, dos palabras); `%` solo en tablas.
- Escalares en *cursiva*; **vectores en negrita cursiva sin flechas**
  (`\mathbf{B}` / `\bm{B}`, no `\vec B`); matrices en negrita sans-serif.
- Producto punto: `\bmath{\cdot}` en negrita; producto cruz: `×` en negrita.
- **Redonda** (no cursiva) para: diferenciales `d`, la unidad imaginaria `i`, la
  base `e`, y las funciones trigonométricas.
- Sub/superíndices: cursiva si son variables físicas, redonda si son etiquetas
  (→ `\sigma_{\rm crit}`, `\gamma_{\rm KHI}`, `\Omega_{zp}` con `zp` redonda).
- Unidades solares con subíndice ⊙ en redonda.
- Ángulos: `arcsec` / `arcmin` para tamaños; primas para coordenadas.

## 9. Data availability (obligatorio)

- Va **tras Acknowledgements**, bajo el encabezado `Data availability`.
- Debe decir **dónde están los datos y cómo se accede**: enlace al repositorio,
  identificador único, o referencia a los datos originales / de terceros.
- MNRAS suscribe los **principios FORCE11** de citación de datos y software:
  el software y los datos con DOI se **citan en la lista de referencias**.
- → Borrador listo en `papers/comun/DATA_AVAILABILITY.md`.

## 10. Idioma

- **Inglés británico obligatorio**: *centre*, *behaviour*, *labelled*, *modelled*,
  *analyse* (no *analyze*), *normalise*… pero *recognize, minimize, emphasize,
  organize, ionize, polarize, parametrize* van con **-ize**.
  Regla práctica: en duda, primera acepción del *Oxford English Dictionary*.
- **`data` es plural**: "these data show…". **`none` es singular**.
- OUP tiene convenio con **Enago** (30 % de descuento) para edición de idioma; no
  es obligatorio pero se recomienda a no nativos.
- → Detalle y glosario ES→EN en `papers/04_ESTILO_INGLES.md`.

## 11. Preprints / arXiv

- Se **permite** el preprint (Author's Original Version) antes y durante el envío;
  no impide la publicación.
- Se puede declarar el arXiv ID al enviar por ScholarOne: al aceptar, el registro
  de arXiv se actualiza con el DOI.
- Tras publicar, hay que actualizar el preprint con el DOI (política de
  auto-archivo).

## 12. Ética e IA

- Declaración obligatoria de originalidad: inédito y no en evaluación en otra parte.
- Todo se pasa por **iThenticate**; el plagio — **incluido el autoplagio** — es
  causal de rechazo.
  ⚠️ **Punto crítico para nosotros**: la monografía es un documento de grado. No es
  una publicación con ISSN/DOI, así que reutilizar su contenido **no** es
  autoplagio; aun así conviene **mencionarlo en la carta de presentación** ("this
  work is based on the undergraduate thesis of B.M.A. & S.R.G., Universidad
  Distrital Francisco José de Caldas, 2026") y, si la UD la publica en su
  repositorio, **citarla** en las referencias.
- **Uso de IA generativa**: debe declararse en la **carta de presentación** y en
  Methods/Acknowledgements (aplica a generación de texto, imágenes, código,
  procesamiento de datos y traducción).
- Autoría: solo quien haya contribuido sustancialmente a concepción/diseño,
  adquisición/análisis/interpretación de datos, o ejecución.

## 13. Carta de presentación (*cover letter*)

Solo la ve la oficina editorial, **no** los árbitros.

- **No** resumir los resultados (para eso está el abstract).
- Sí: requisitos especiales de manejo, razones para excluir/pedir árbitros,
  artículos compañeros o series, lista del material suplementario, conflictos de
  interés, declaración de uso de IA.
- **No** mencionar waivers de APC.
- → Borrador en `papers/comun/COVER_LETTER_MNRAS.md`.

## 14. Revisión y plazos

- Revisión **simple ciego** (los árbitros conocen a los autores). Normalmente 2+
  árbitros. El rechazo lo confirma un segundo editor.
- Plazos de revisión (Papers): **mayor 6 meses / moderada 3 meses / menor 45 días**.
  (Letters: moderada 2 meses / menor 1 mes.)
- Apelaciones: **hasta 1 mes** tras el rechazo, por el autor de correspondencia,
  con respuesta punto por punto. Solo si el manuscrito llegó a un Scientific Editor.
- Producción: OUP publica online **dentro de los 30 días** de recibir el artículo
  en producción. Pruebas en PDF vía Aptara; **no** se aceptan correcciones como
  ficheros `.tex` nuevos (sí fragmentos cortos). "Note added in proof": 2–3 frases.

## 15. Premio estudiantil

Si el autor de correspondencia o el primer autor es **estudiante**, marcar "yes" en
ScholarOne e incluir una breve declaración de contribución estudiantil. Los
ganadores se anuncian en el RAS National Astronomy Meeting.
→ **Nos aplica**: Bryan y Sebastián son estudiantes de pregrado.
