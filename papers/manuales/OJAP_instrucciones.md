# The Open Journal of Astrophysics (OJAp) — Instrucciones para autores (resumen operativo)

> Fuente: <https://astro.theoj.org/for-authors>. Consultada el **2026-09-17**.
> Transcripción literal en `manuales/ojap_for_authors_2026-09-17.txt`.

---

## 1. Qué es

Revista **overlay de arXiv**, publicada por *Maynooth Academic Publishing*
(editor gestor: Peter Coles, Maynooth). Tiene consejo editorial y arbitraje
convencionales, pero **el artículo vive en arXiv**: la revista publica una
"capa" con resumen, metadatos de autor, DOI y enlace a la entrada de arXiv.

> **GRATIS EN TODO SENTIDO**: "Papers can be submitted for publication free of
> charge, are refereed free of charge and are published (online only) free of
> charge." Sin APC, sin cuota de envío, sin suscripción. Miembro de la
> *Free Journal Network*.

## 2. ¿Es apto nuestro artículo?

Criterio único: **si — y solo si — sirve para la sección `astro-ph` de arXiv,
sirve para OJAp**. Las seis áreas:

| Categoría | Contenido |
|---|---|
| `astro-ph.GA` | Galaxias, ISM, **núcleos galácticos activos, agujeros negros supermasivos, cuásares** |
| `astro-ph.CO` | Cosmología y astrofísica no galáctica |
| `astro-ph.EP` | Sistemas planetarios |
| **`astro-ph.HE`** | **Fenómenos de alta energía: … estrellas de neutrones, púlsares, agujeros negros, *jets*, microcuásares** |
| **`astro-ph.IM`** | **Instrumentación y métodos: métodos de análisis de datos, métodos estadísticos, software** |
| `astro-ph.SR` | Astrofísica solar y estelar |

→ **Nuestro encaje**: primaria `astro-ph.HE` (KHI en chorros relativistas /
plasmas de alta energía), secundarias `astro-ph.IM` (esquema numérico RRMHD,
IMEX, estadística del ajuste) y opcionalmente `physics.plasm-ph` como
*cross-list*.

Otros requisitos: **artículos en inglés**; se aceptan **artículos de revisión**
si el consejo los considera aportes útiles.

## 3. Proceso de envío (la ruta preferida)

1. **Publicar primero en arXiv**, eligiendo licencia **CC-BY** al subir.
   (Si ya está con una licencia más restrictiva no es grave: se puede dar una
   licencia distinta a la versión publicada.)
2. Ir a <https://astro.theoj.org> → botón **"Submit a manuscript"** (plataforma
   **Scholastica**) y seguir el proceso, que es **muy corto**.
3. Si el proceso falla, se puede escribir a un editor y él mete el artículo.

Notas:

- La revista **acepta** envíos directos a la plataforma sin arXiv previo, pero
  **desaconseja** esa vía: la versión final **debe** estar en arXiv de todos modos.
- **Nadie que no esté en la lista de autores puede enviar el artículo.**

## 4. Formato / LaTeX

- Clase oficial: **`openjournal.cls`**, descargable de
  <http://www.thphys.nuim.ie/staff/pcoles/openjournal.cls>
  → **ya copiada en `papers/ojap/openjournal.cls`** (versión 6-sep-2015).
- Está **basada en `emulateapj`** (estilo ApJ/ApJL). Opciones: `[twocolumn]`,
  `[onecolumn]` (por defecto), `[apj]`, `[apjl]` (por defecto), `[tighten]`,
  `[numberedappendix]`, `[appendixfloats]`, `[twocolappendix]`, `[revtex4]`,
  `[astrosymb]`.
- **El envío inicial puede ir en cualquier formato que acepte arXiv**, pero
  prefieren la versión final en esta clase — y el proceso se simplifica si se usa
  desde el principio.
- Los **fuentes de todos los artículos publicados están en arXiv**: se puede tomar
  cualquiera como plantilla.
- **No hay corrección de estilo (copy-editing)**. Por eso exigen una revisión
  cuidadosa antes de enviar la versión final, y rechazan artículos mal escritos.
  Recomiendan (con coste, pero barato) **Scitext Cambridge** <http://www.scitext.com/>.

## 5. Proceso editorial y de publicación

1. Criba inicial del **Managing Editor** → asignación a un editor → uno o más árbitros.
2. Evaluación **exclusivamente** por: **calidad científica, originalidad,
   relevancia y comprensibilidad**.
3. Tras aceptar: se añaden metadatos (ID de artículo, fecha de aceptación, etc.),
   la versión aceptada se sube a **arXiv**, y se asigna y registra un **DOI en
   CrossRef**.
4. El artículo aparece en la revista como *overlay*: resumen + metadatos + DOI +
   enlace a arXiv.

Confidencialidad: como el artículo ya está en arXiv, no es secreto; pero **el
hecho de que se haya enviado a OJAp no se divulga** fuera del proceso.

## 6. Licencia y derechos

- **CC-BY**, libre lectura a perpetuidad.
- **Los autores conservan copyright y derechos de publicación sin restricción**;
  pueden depositar en repositorios institucionales (→ el repositorio de la UD).
- Compromiso de preservación vía Maynooth Academic Publishing; adhesión a los
  principios de *Fair Open Access*.

## 7. IA generativa (política explícita — leer con cuidado)

> No hay prohibición general, **pero**:
> - Si se usan LLM u otra IA generativa, **hay que declararlo en la sección de
>   agradecimientos** del artículo.
> - Si la IA se usa para **cualquier cálculo, análisis o visualización de datos**,
>   hay que **incluir una descripción de los pasos dados para probar y validar**
>   esos métodos.
> - **Se rechazan** los artículos con evidencia directa de IA: referencias
>   alucinadas o *prompts* dentro del texto.

→ Ver la redacción propuesta en `papers/comun/DECLARACION_IA.md`.

## 8. Responsabilidades del autor

- Solo obra propia y original; citar claramente todo resultado ajeno.
- Copiar o parafrasear partes sustanciales sin atribución es inaceptable.
  **arXiv hace una criba de plagio y OJAp mira con lupa lo que dispare ese filtro.**
- **Nada que esté publicado o en evaluación en otra revista.**
  ⚠️ Es decir: **MNRAS y OJAp son excluyentes en el tiempo** — hay que elegir uno,
  esperar el veredicto, y solo entonces ir al otro.
- Autoría = contribución sustancial; a quien contribuyó así hay que **ofrecerle** la autoría.
- Si se descubre un error importante, avisar a la revista de inmediato.
- Política completa de ética: <https://astro.theoj.org/pages/390-ethics>

## 9. Datos

Recomiendan seguir **"Best Practices for Data Publication in the Astronomical
Literature"** (Chen et al. 2022, ApJS 260, 5) —
<https://scixplorer.org/abs/2022ApJS..260....5C/abstract> — para preparar y
publicar los datos de forma reutilizable y reproducible.
No hay una sección "Data availability" obligatoria como en MNRAS, pero **la
incluiremos igual** (es buena práctica y hace el texto portable entre las dos).
