# MNRAS vs. OJAp — comparativa y estrategia de publicación

## 1. Tabla comparativa

| | **MNRAS** | **OJAp** |
|---|---|---|
| Modelo | Revista clásica, Open Access | **Overlay de arXiv** |
| **Costo para nosotros** | **£2.356** (Paper) / £1.122 (Letter); −20 % socios RAS; posible waiver por país | **£0. Cero. Nada.** |
| Plataforma | ScholarOne | Scholastica (envío "muy corto") |
| Formato de envío | **PDF compilado** con figuras embebidas (≤10 MB) | arXiv primero, luego el enlace |
| Clase LaTeX | `mnras.cls` (2 columnas, CTAN) | `openjournal.cls` (basada en `emulateapj`, estilo ApJ) |
| Bibliografía | **Harvard autor–año**, `mnras.bst` + `natbib` | Estilo ApJ (`aasjournal.bst` / `apj.bst`), autor–año |
| Resumen | **≤ 250 palabras**, un párrafo | Sin límite duro publicado (usar ≤250 igual) |
| Palabras clave | **1–6, de la lista oficial MNRAS** | Categorías arXiv (astro-ph.HE, .IM) |
| Idioma | **Inglés británico obligatorio** | Inglés (sin dialecto impuesto) |
| Copy-editing | Sí (pruebas de Aptara) | **No hay.** El texto sale como lo mandemos |
| Data availability | **Sección obligatoria** | Recomendado (Chen et al. 2022) |
| Declaración de IA | Cover letter + Methods/Acknowledgements | **Agradecimientos + validación de métodos** |
| Licencia | CC-BY | CC-BY, autores retienen copyright |
| Revisión | Simple ciego, 2+ árbitros | Editor gestor → editor → 1+ árbitros |
| Tiempos | Producción ≤30 días tras aceptación | DOI y arXiv tras aceptación |
| Prestigio / indexación | Muy alto; ADS, WoS, Scopus | Creciente; ADS, DOAJ, CrossRef. Respetada en la comunidad |
| Premio estudiantil | **Sí** (autor estudiante) | No |

## 2. El punto que decide

**No se puede enviar a las dos a la vez.** Ambas lo prohíben explícitamente
(MNRAS: rechazo inmediato por envío múltiple; OJAp: "No paper should be submitted
… that is already published elsewhere or is being considered for publication by
another journal"). La estrategia es **secuencial**.

## 3. Recomendación

**Ruta sugerida: un solo artículo, enviado primero a MNRAS; si lo rechazan, a OJAp.**

Razones:

1. El contenido da para un **Paper MNRAS completo** (barrido de 44 simulaciones +
   modelo sigmoide + validación estadística + contraste con teoría lineal +
   campaña magnética). No es material de *Letter*.
2. MNRAS tiene más peso para hojas de vida de pregrado, y el **premio estudiantil**
   aplica a este caso.
3. El **riesgo real es el APC de £2.356**. Antes de comprometerse hay que resolver:
   - ¿La Universidad Distrital tiene acuerdo *Read & Publish* con OUP? (probable
     que **no**).
   - ¿Colombia califica para waiver de país de ingreso bajo/medio en OUP? Hay que
     **verificar la lista vigente** — si califica, el APC puede quedar en cero y
     MNRAS es una decisión fácil.
   - Si no hay waiver y no hay quién pague, **OJAp es la respuesta correcta**, no
     un premio de consolación: es gratis, indexada en ADS, con DOI CrossRef, y el
     artículo queda en arXiv para siempre.
4. **arXiv no es excluyente**: MNRAS permite el preprint. Se puede (y conviene)
   subir a arXiv al momento de enviar a MNRAS. Si luego hay que virar a OJAp, el
   preprint ya está y el envío es cuestión de minutos.

> ⚠️ **Decisión pendiente del equipo (Bryan, Sebastián y el director):** MNRAS con
> waiver, o directo a OJAp. Contestar esto **antes** de escribir una sola sección,
> porque cambia clase LaTeX, estilo de citas y dialecto del inglés.
> Mientras tanto, la escritura arranca en la **carpeta `mnras/`** porque es la más
> restrictiva: bajar de MNRAS a OJAp es fácil (relajar), subir es caro (rehacer).

## 4. Alternativa: dos artículos

Si el volumen resulta excesivo para un solo *paper*, la partición natural es:

- **Paper I — "The resistive-to-ideal transition of the relativistic KHI"**
  (objetivos 1–3): barrido en σ, sigmoide con offset, zona de transición,
  σ^1.22, contraste con Lees–Lin. **Este es el artículo fuerte.**
- **Paper II — "Magnetic field strength and orientation …"** (objetivo 4):
  campañas A/B/C, balance energético, anti-fase E_kin↔E_mag.

Recomendación: **empezar por el Paper I solo**. Es autocontenido, tiene el
resultado más citable, y evita que la campaña magnética (menos madura: sin fase
lineal limpia, análisis por balance energético) arrastre al conjunto en el
arbitraje. La campaña magnética puede ir como **sección corta + apéndice** del
mismo artículo si el árbitro no objeta, o como Paper II después.

## 5. Un tercer destino a tener presente

Si las dos anteriores fallan o el equipo quiere algo intermedio:
**A&A** (APC similar a MNRAS), **ApJ/ApJS** (APC alto), **Physics of Plasmas**
(encaja por la parte RRMHD/numérica), o **RAS Techniques and Instruments (RASTI)**
si el énfasis se moviera al esquema numérico. No se desarrollan aquí.
