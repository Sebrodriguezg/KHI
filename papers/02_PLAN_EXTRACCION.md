# Plan de extracción: monografía (167 pp, español) → artículo (~15 pp, inglés)

> Documento de trabajo. **No copia texto**: dice *de dónde sale cada cosa* y
> *qué hay que hacerle*. Todas las rutas son relativas a `monografia/`.

## 0. El cambio de género que hay que tener en la cabeza

La monografía es un documento **pedagógico y exhaustivo**: deriva la RRMHD desde
el cuadripotencial, explica qué es un volumen finito, incluye un apéndice de
técnicas estadísticas. Un artículo de MNRAS/OJAp es lo contrario: **asume al
lector experto y solo cuenta lo nuevo**.

Regla de tijera: **si está en Komissarov (2007), Mizuno et al. (2013) o en
cualquier libro de texto, se cita — no se reproduce.**

Proporción objetivo (Paper I, ~15 páginas MNRAS a dos columnas):

| Sección del artículo | Páginas | Origen en la monografía | Compresión |
|---|---|---|---|
| 1 Introduction | 1,5 | cap. 1 completo + §3.4 | 22 pp → 1,5 |
| 2 Numerical method & setup | 2,5 | cap. 4 (muy podado) + cap. *setup_exp* | 58 pp → 2,5 |
| 3 Results | 6 | cap. 5 §§ barrido | 92 pp → 6 |
| 4 Comparison with linear theory | 2 | cap. 5 §teoria_v6 + apéndice A | — |
| 5 Magnetic field campaign | 1,5 | cap. 5 §campana_magnetica | 25 pp → 1,5 |
| 6 Discussion & conclusions | 1,5 | cap. 6 | 7 pp → 1,5 |
| Appendix A (estadística) | 1 | cap. 7 §técnicas estadísticas | solo lo no estándar |

---

## 1. Introduction  ← `sections/01_introduction.tex`

**Qué se conserva (≈5 párrafos):**

1. Contexto: KHI en chorros relativistas / AGN. Sale de §"Relevancia de la RRMHD
   en Chorros Astrofísicos y AGN" (líneas 6–18). **Recortar a 4–5 frases**
   con las citas fuertes.
2. Por qué resistiva y no ideal: §"Transición de RMHD a RRMHD" (l. 29–35).
   Este es **el gancho del artículo**: la RMHD ideal impone congelamiento y
   prohíbe la reconexión; la resistividad finita la permite y cambia la KHI.
3. Qué se sabe ya: aquí falta trabajo — **hay que ampliar la revisión de
   literatura**. La monografía cita poco trabajo previo de KHI-RRMHD. Ver §7 abajo.
4. Qué hace este trabajo: reformular los 4 objetivos (l. 36+) **como preguntas de
   investigación**, no como objetivos de propuesta de grado.
   ⚠️ *"Objetivo específico 1"* es lenguaje de trabajo de grado — **eliminarlo por
   completo** del artículo.
5. Estructura del artículo (1 frase por sección).

**Qué se elimina:** todo el tono de "el trabajo en cuestión consta de un recorrido
conceptual…"; la descripción de la estructura de la monografía.

**Figura candidata:** `figuras/contexto_jet.pdf` (`fig:contexto_jet`) — opcional,
solo si el espacio lo permite. En MNRAS una figura de contexto rara vez sobrevive.

---

## 2. Numerical method and setup

### 2.1 Equations ← `sections/02_rrmhd_theory.tex` (**el capítulo que más se poda**)

De 80 kB de capítulo teórico, al artículo pasan **entre media y una columna**:

- **Se conserva**: el sistema RRMHD en **forma conservativa 3+1** — el bloque de
  §"Resumen del Sistema RRMHD en Forma Conservativa" (l. 413+, ecuación
  `eq:def_conservativas`) y la **ley de Ohm relativista** (l. 373+). Esto es
  literalmente "las ecuaciones que integramos", y va tal cual, citando
  **Komissarov (2007)**.
- **Se conserva en una frase**: el sistema aumentado GLM con los campos auxiliares
  Ψ y Φ y sus constantes de amortiguamiento κ_E, κ_B. Citar Dedner et al. (2002)
  y Komissarov (2007).
- **Se elimina sin piedad**: la derivación del tensor de Faraday desde el
  cuadripotencial (l. 16–103); las densidades lagrangianas (l. 156–191); la
  ecuación del telégrafo (l. 291–309); la descomposición ortogonal de la
  cuadricorriente (l. 328–357). Todo eso es libro de texto.
  → *Si un árbitro lo pide, va a un apéndice; no al cuerpo.*
- **Figuras que NO pasan**: `foliacion_3p1`, `marco_comovil_lab`, `glm_limpieza`.
  Son didácticas.

### 2.2 The code ← `sections/04_numerical_methods.tex`

**Un solo párrafo denso**, con esta forma:

> "We use *Cueva* (Miranda-Aranguren 2018), a finite-volume RRMHD code that solves
> the Komissarov (2007) formulation with fifth-order MP5 reconstruction (Suresh &
> Huynh 1997), an HLL Riemann solver, GLM divergence cleaning, and IMEX-RK time
> integration to handle the stiff resistive term (Palenzuela et al. 2009)."

Y luego **solo lo que no es estándar**: la condición subcaracterística (l. 75–81)
y la inversión algebraica local del término de conducción (l. 148–168), porque son
lo que hace viable el σ alto. Una o dos ecuaciones como mucho.

- **Se elimina**: qué es un volumen finito, qué es un limitador de pendiente, qué
  es HLL, la estructura espectral del jacobiano 14×14.
- **Figuras que NO pasan**: `volumenes_finitos`, `celda_3d_flujos`, `riemann_hll`,
  `imex_splitting`. Todas didácticas.
- ⚠️ **Citar bien a *Cueva***: es el código del director. Confirmar con él la
  referencia exacta y si hay DOI/ASCL. Si no lo hay, **este es el momento de
  registrarlo** (ver `comun/DATA_AVAILABILITY.md`).

### 2.3 Initial conditions ← `sections/setup_exp.tex` §"Condiciones Iniciales" (l. 24–115)

**Pasa casi completo, pero comprimido a ecuaciones + una tabla.**

- Perfil de doble capa de cizalla tipo **Mizuno et al. (2013), test 35A**:
  v_sh = 0,5c, a_kh = 0,05, perturbación, B = (0, √0,02, √2,0), Γ = 4/3.
- Dominio y malla: 2D, **512×256**, sistema de unidades (l. 116–164).
- **`tab:setup_summary` (setup_exp.tex:139) → Tabla 1 del artículo.** Es la mejor
  candidata del documento: ya está condensada y es exactamente lo que un árbitro
  busca. Solo hay que traducirla y quitarle las líneas verticales (MNRAS no las
  admite).
- **Figura `fig:setup_inicial`** (`velocidad_inicial.pdf` + `rho_inicial.pdf` +
  frames): **sí pasa**, reducida a **un panel de 2 subfiguras** (v_y inicial y ρ
  inicial). Es la figura que evita 200 palabras de descripción.

### 2.4 The two campaigns ← `setup_exp.tex` l. 165–271

- **Campaña 1**: barrido de 44 simulaciones, σ ∈ [100, 10500]. Un párrafo + la
  **tabla canónica** (`tab:canonica_sigma`, 05_results:68).
  ⚠️ **44 filas es demasiado para el cuerpo en MNRAS**: la norma es dar **5–10
  filas de muestra** y la tabla completa como material suplementario / VizieR.
  Decisión sugerida: en el cuerpo, **una frase** con el rango y el paso; la tabla
  completa (con γ_KHI, R², Ω_zp^max, t_peak por simulación) como **Tabla A1
  suplementaria en formato legible por máquina**. Eso además fortalece el
  *data availability*.
  ⚠️ **σ = 10500 fue el límite numérico del código.** En el artículo hay que
  **decirlo explícitamente** (o truncar el barrido a 10⁴ y justificarlo), porque un
  árbitro va a preguntar por qué se corta ahí.
- **Campaña 2**: `tab:campana_A`, `tab:campana_B`, `tab:campana_C`
  (setup_exp.tex:209/231/255) → **fundir las tres en una sola tabla** de 3 bloques.
- **Figura `fig:campanas_BC_3d`** (`campana_A/B/C_3d`): **sí pasa**. Los esquemas
  3D de la geometría de cada campaña son necesarios para entender por qué C tiene
  **k·B = 0**.

---

## 3. Results ← `sections/05_results_discussion.tex` (**el corazón del artículo**)

Este capítulo es el que **menos** hay que recortar: es el resultado nuevo.

| Subsección monografía | Label | → Artículo | Figuras que arrastra |
|---|---|---|---|
| Trayectorias temporales del barrido | `sec:vision_global` | §3.1 | `fig:ultrawide_omega_tot`, `fig:ultrawide_omega_zp`, `fig:mapa_conductividad` |
| Extracción de γ y calidad del ajuste | `sec:lnfit` | §3.2 | `fig:lnfit` |
| Tabla canónica | `tab:canonica_sigma` | → suplementario | — |
| **Modelo sigmoide con offset** | `sec:sigmoide_v6` | **§3.3 — resultado central** | `fig:ajuste_v6`, `tab:par_v6` |
| Validación estadística | `sec:validacion_v6` | §3.4 (comprimir) | `fig:3v4_v6`, `fig:holdout_v6` |
| **Zona de transición y σ_crit** | `sec:scrit_v6` | **§3.5 — 2.º resultado** | `fig:zona_transicion`, `fig:regimenes`, `fig:derivadas_scrit`, `fig:est_v6`, `tab:est_v6` |
| **Leyes de potencia Ω^max ∝ σ^1.22** | `sec:leyes_potencia` | **§3.6 — 3.er resultado** | `fig:omega_max_pot`, `tab:leyes_potencia` |
| Variables globales / corrientes | `sec:globales` | §3.7 | `fig:global_campos_transitorio`, `fig:global_estructuras` |

**Los tres resultados que el artículo tiene que vender (van en el abstract):**

1. **γ(σ) = C + γ₀/(1+e^{−k(σ−σ₀)})**, con asíntota ideal
   **C + γ₀ = 1,03 ± 0,05** (ω̂ = 0,103), consistente al **8 %** con la teoría
   lineal RMHD compresible.
2. La transición resistivo→ideal **no es un umbral sino una zona**,
   **σ ∈ [1400, 7000]** con centro **σ_crit ≈ 2815**: cada observable se idealiza
   a una σ distinta.
3. **Ω_zp^max ∝ σ^1,22**, exponente que **excede el piso de Sweet–Parker (σ^1/2)**
   → firma de reconexión resistiva, con hipótesis de *tearing* secundario.

**Advertencias que deben sobrevivir al recorte (honestidad metodológica):**

- `C + γ₀` es una **extrapolación**: el dato de mayor σ llega solo al **85 %** del
  plateau. Confirmarlo exige Rm* ≳ 500. **Esto va en el texto, no escondido.**
- El *tearing* secundario es **hipótesis**: no se mapearon directamente las láminas
  de corriente. (Los diagnósticos de lámina que Cueva sí calcula —`E_rec`,
  `nsheet`, η|J_z|— **no están en la monografía**; están en el respaldo B20/B21 del
  deck. **Decisión pendiente: ¿entran al artículo?** Ver §6 abajo.)
- El anti-correlación de canales (f_Vz vs J_max, Spearman −0,83) está en el deck
  (lámina 28) pero **no en la monografía**: si entra al artículo, hay que
  documentar el análisis desde cero.

---

## 4. Comparison with linear theory ← `sec:teoria_v6` + `07_appendices.tex` §1

Esta es la sección que **da credibilidad** al número 1,03.

- Techo hidrodinámico inviscido (ecuación de Rayleigh) → **1 párrafo + 1 ecuación**.
- El carácter dual del montaje no altera el techo → **1 frase**.
- **Predicción RMHD compresible (Lees–Lin)** con la sustitución c_s → v_f⊥ de
  Chow et al. (2023) → **el núcleo**: ω̂ = 0,095 frente a nuestro 0,103.
- Velocidades características y números de Mach (`tab:mach_v6`) → tabla pequeña o
  frase: **M_re = 0,60 < √2** ⇒ holgadamente inestable.
- Contraste MHD / RMHD / RRMHD (`sec:marcos_v6`, `fig:marcos_v6`) → figura fuerte,
  **conservarla**.
- Figuras: `fig:michalke_v6`, `fig:dual_v6`, `fig:compresible_v6`,
  `fig:escalera_v6`, `fig:marcos_v6` → **seleccionar 2, no las 5**.
- El desarrollo paso a paso del apéndice A de la monografía → **Apéndice A del
  artículo, muy recortado**, o suprimido citando Lees & Lin y Chow et al.

---

## 5. Magnetic field campaign ← `sec:campana_magnetica` (l. 430–674)

Es 25 pp de monografía que deben caber en **1,5 columnas**. Se conserva:

- **Campaña A (intensidad)**: γ_KHI cae de **0,81 a 0,38** y la enstrofía pico de
  **≈87 a ≈25** (σ = 10⁴) al aumentar B₀. Clave: el agente es la **presión
  magnética / magnetización (β ∝ B₀⁻²)**, **no** la tensión — el flujo sigue
  **super-Alfvénico a lo largo de k (M_A,∥ = 9,4)**.
  Figuras: `fig:campA_enstrofia` + `tab:campA_enstrofia`.
- **Campañas B y C (orientación)**: solo **B_y** (∥ a k) ejerce tensión
  restauradora, y solo a ángulos grandes; **B_x** cumple **k·B = 0** y **no**
  ejerce tensión → actúa por presión y reconexión.
  Figuras: `fig:campB_omegamax_theta` (la más informativa), `fig:campC_enstrofia`.
- **Balance energético** (`sec:balance_energetico`): **anti-fase E_kin ↔ E_mag**;
  en σ = 10⁴ el intercambio es cuasi-reversible, en σ = 6000 la disipación óhmica
  desvía energía a interna. Figura: `fig:campB_ekin_emag_scatter` **o**
  `fig:campB_ekin_emag`, no ambas.
- Se eliminan o se van a apéndice: los collages de densidad
  (`fig:mapa_campA/B/C`), `fig:campB_conversion`, `fig:campB_emag`,
  `fig:campB_energia_todos`, `fig:campB_cierre`, `fig:campB_disipacion_resumen`,
  `fig:campC_energia_todos`, `fig:campC_disipacion_resumen`. **Son 9 figuras para
  1,5 columnas: imposible.**
- Mencionar que **B₀ ≤ 0,5 no completa la evolución numérica** (es un límite del
  experimento, y hay que decirlo).

---

## 6. Discussion and conclusions ← `sections/06_conclusions.tex`

El capítulo 6 **ya está escrito en el registro correcto** (denso, con cifras). Es
el que menos trabajo cuesta: básicamente **traducir y reordenar**, quitando la
estructura "(1) objetivo… (2) objetivo…" y convirtiéndola en prosa temática.

- Las **limitaciones** (2D; EoS politrópica Γ=4/3; σ escalar sin Hall ni
  anisotropía; resolución de las hojas resistivas cerca del límite de malla;
  asíntota extrapolada al 85 %) **van íntegras**. En un artículo esto suma, no resta.
- El **trabajo futuro** se comprime a 2–3 frases.

---

## 7. Lo que HAY QUE AÑADIR (no está en la monografía)

Esto es trabajo nuevo, no extracción. **Es la parte que más tiempo va a tomar.**

1. **Revisión de literatura de verdad.** Un artículo de MNRAS necesita situarse
   frente al trabajo previo en KHI relativista y resistiva. Mínimos a buscar y
   leer: Mizuno et al. (2013) —nuestro test de partida—, Zhang, MacFadyen &
   Wang (2009), Bodo et al. (2004), Perucho et al. (jets), Beckwith & Stone,
   Ripperda et al. (reconexión resistiva relativista), Mignone et al. (2024),
   Del Zanna et al. (ECHO), Bucciantini & Del Zanna, Palenzuela et al. (2009).
   👉 **Búsqueda sistemática en ADS pendiente.** La monografía tiene 83 entradas
   `.bib`; un paper de este tipo suele traer 50–80 **actuales**.
2. **Comparación cuantitativa con al menos un resultado publicado.** Hoy solo hay
   contraste con teoría lineal. Un árbitro va a pedir: "¿reproduce su código el
   test 35A de Mizuno en el límite ideal?" — **la respuesta debe estar en el
   artículo** (idealmente una figura de validación).
3. **Data availability statement** (obligatorio en MNRAS). → `comun/DATA_AVAILABILITY.md`.
4. **Declaración de uso de IA.** → `comun/DECLARACION_IA.md`.
5. **Convergencia de malla.** Todo el barrido es 512×256. Que las hojas resistivas
   "se acercan al límite de la malla" está reconocido como limitación, pero
   **un árbitro de MNRAS casi con seguridad pedirá al menos una corrida a
   1024×512** para el σ más alto. **Anticiparlo.**
6. **Alt text** de cada figura (requisito MNRAS).
7. **Decisión sobre los diagnósticos de lámina** (`E_rec`, área de lámina,
   η|J_z|; fuente `data_global/2d_data_Erec_AB.dat`, detector en `22_writer.f95`,
   umbrales en `parameters.f95:311-316`). **No están en la monografía** pero
   **refuerzan directamente** la afirmación de reconexión que hoy queda como
   hipótesis. Hallazgos ya verificados: E_rec máximo en σ≈1600; área máxima
   0,115 % del dominio (150 celdas) en σ≈3200; Spearman +0,66 con f_Vz.
   Limitación conocida: `nsheet` cuenta **celdas, no láminas** → no zanja el
   *tearing* por sí solo. **Recomendación: incluirlos**, con las limitaciones
   declaradas — es material nuevo y es exactamente lo que el árbitro va a pedir.

---

## 8. Lo que NO debe pasar al artículo (lista negra)

- Toda la derivación pedagógica del cap. 2 (tensor de Faraday, lagrangianos,
  telégrafo, descomposición de la cuadricorriente).
- Todo el cap. 4 salvo un párrafo y dos ecuaciones.
- El glosario de símbolos y acrónimos (`00_preliminares.tex`).
- El apéndice de técnicas estadísticas (R², AIC, jackknife, hold-out, test de
  rachas): **son estándar**. Se citan en una frase de Methods: "model selection by
  AIC, uncertainties by jackknife, validated by hold-out". Solo si el árbitro
  pregunta se amplía.
- El capítulo de recursos computacionales (`agradecimientos_cluster.tex`) → **se
  convierte en 2 frases de Acknowledgements**.
- Las notas de revisión `\prof{}`, `\sebnota{}`, `\brynota{}`.
- El lenguaje de trabajo de grado: "objetivo específico", "la presente
  monografía", "el trabajo en cuestión", "se abordará".

---

## 9. Orden de trabajo sugerido

1. **Decidir revista** (ver `01_COMPARATIVA_Y_ESTRATEGIA.md`) — bloquea todo lo demás.
2. **Decidir 1 artículo vs. 2** y cerrar el alcance.
3. Escribir **Results** primero (§3). Es lo nuevo, lo que ya está maduro, y fija
   el resto del artículo.
4. Luego **Setup** (§2.3–2.4) y **Comparison with linear theory** (§4): apoyan a Results.
5. Luego **Conclusions** (§6) — casi traducción directa.
6. **Introduction al final**, cuando ya se sabe qué se está introduciendo, y
   después de la búsqueda bibliográfica del §7.1.
7. Abstract **de último**, ≤250 palabras.
8. Pasada de figuras (ver `03_INVENTARIO_FIGURAS.md`), pasada de inglés
   (`04_ESTILO_INGLES.md`), checklist (`05_CHECKLIST_ENVIO.md`).
