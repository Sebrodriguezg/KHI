# Guía de estilo en inglés + glosario ES→EN del proyecto

## 1. Dialecto

**MNRAS exige inglés británico.** OJAp no impone dialecto, pero **hay que ser
consistente**. Si escribimos pensando en MNRAS primero, el texto sirve para las dos.

### Británico vs. americano — las que nos van a salir

| ✅ Británico (MNRAS) | ❌ Americano |
|---|---|
| centre, centred | center, centered |
| behaviour | behavior |
| labelled, modelling, modelled, cancelled | labeled, modeling, modeled, canceled |
| analyse, analysed, analysis | analyze, analyzed |
| normalise, normalised | normalize |
| neighbouring | neighboring |
| fibre | fiber |
| grey | gray |
| towards | toward |

### Pero estas van con **-ize** también en británico (regla de Oxford)

`recognize, minimize, emphasize, organize, ionize, polarize, parametrize,
characterize, summarize, visualize`

Regla práctica: en duda, **primera acepción del Oxford English Dictionary**.
Truco de comprobación: `\usepackage[british]{babel}` + un corrector, o buscar con
`grep -nE '(ize|yze|ization|center|behavior)'` antes de enviar — pero **ojo con
los falsos positivos de la lista -ize de arriba**.

## 2. Gramática que MNRAS vigila

- **`data` es PLURAL**: "these data **show**…", "the data **are** consistent".
  (Es el error nº 1 de los hispanohablantes en MNRAS.)
- **`none` es SINGULAR**: "none of the runs **shows**…".
- **`per cent`**: dos palabras en el texto; **`%`** solo dentro de tablas.
  → "consistent to within 8 per cent", no "8%".

## 3. Notación (MNRAS)

| Concepto | Correcto | Incorrecto |
|---|---|---|
| Unidades | `200 keV` (redonda, espacio irrompible `\,`) | `200keV`, *200 keV* en cursiva |
| Velocidad | `km s$^{-1}$` | `km/s` |
| Vectores | `$\mathbfit{B}$` / `\bm{B}` (negrita cursiva) | `$\vec{B}$` |
| Matrices | negrita sans-serif | — |
| Diferencial | `${\rm d}x$` | `$dx$` |
| Base e / unidad imaginaria | `${\rm e}$`, `${\rm i}$` | `$e$`, `$i$` |
| Trigonométricas | `$\sin$`, `$\cos$` (redonda) | `$sin$` |
| Subíndice-etiqueta | `$\sigma_{\rm crit}$`, `$\gamma_{\rm KHI}$` | `$\sigma_{crit}$` |
| Subíndice-variable | `$B_y$` (cursiva) | — |

`mnras.cls` define `\bmath`, `\mathbfit`, `\mathbfss` y los alias de revistas
(`\mnras`, `\apj`, …) — ver `mnras_guide.pdf`.

## 4. Glosario ES → EN del proyecto

**Hay que usar siempre el mismo término.** La inconsistencia terminológica es lo
que más delata una traducción.

| Español (monografía) | Inglés (artículo) |
|---|---|
| inestabilidad de Kelvin–Helmholtz | Kelvin–Helmholtz instability (KHI) |
| magnetohidrodinámica relativista resistiva | resistive relativistic magnetohydrodynamics (RRMHD) |
| tasa de crecimiento lineal | linear growth rate |
| conductividad (eléctrica) | (electrical) conductivity |
| resistividad | resistivity |
| barrido (en σ) | (conductivity) **sweep** / parameter scan |
| corrida, simulación | **run** / simulation (nunca "running") |
| zona de transición | transition **zone** (no "region", que ya se usa para el dominio) |
| conductividad crítica | critical conductivity |
| régimen resistivo / ideal | resistive / ideal **regime** |
| capa de cizalla | shear layer |
| doble capa de cizalla | double shear layer |
| enstrofía | enstrophy |
| enstrofía de perturbación | perturbation enstrophy |
| fracción fuera del plano | out-of-plane fraction |
| vorticidad | vorticity |
| lámina de corriente | current sheet |
| reconexión magnética | magnetic reconnection |
| *tearing* secundario | secondary tearing |
| congelamiento del campo | flux freezing |
| tensión magnética | magnetic tension |
| presión magnética | magnetic pressure |
| campo guía | guide field |
| número de Reynolds magnético | magnetic Reynolds number |
| factor de Lorentz (**W**, no Γ) | Lorentz factor |
| índice adiabático (**Γ**) | adiabatic index |
| ecuación de estado | equation of state (EoS) |
| volúmenes finitos | finite volume |
| reconstrucción de quinto orden | fifth-order reconstruction |
| solucionador de Riemann | Riemann solver |
| limpieza de divergencias | divergence cleaning |
| rigidez (del término resistivo) | **stiffness** |
| esquema implícito–explícito | implicit–explicit (IMEX) scheme |
| malla | grid (o mesh; elegir uno) |
| resolución de malla | grid resolution |
| condiciones iniciales | initial conditions |
| dominio computacional | computational domain |
| paso de tiempo | time step |
| ajuste (de mínimos cuadrados) | (least-squares) fit |
| modelo sigmoide con *offset* | sigmoid model with offset |
| asíntota ideal | ideal asymptote |
| bondad del ajuste | goodness of fit |
| validación cruzada | cross-validation |
| ley de potencia | power law |
| balance energético | energy balance |
| anti-fase | antiphase |
| disipación óhmica | Ohmic dissipation |
| chorro (astrofísico) | (astrophysical) **jet** |
| núcleo galáctico activo | active galactic nucleus (AGN) |

## 5. Trampas frecuentes del español académico

| ❌ No escribir | ✅ Escribir |
|---|---|
| "It is observed that the growth rate increases" | "The growth rate increases" |
| "In the present work we proceed to analyse" | "We analyse" |
| "the same one presents a behaviour of type sigmoid" | "it follows a sigmoid" |
| "allows to obtain" | "allows us to obtain" / "yields" |
| "in function of σ" | "as a function of σ" |
| "different simulations were realized" | "we ran 44 simulations" |
| "actually" (por *actualmente*) | "currently" / "at present" |
| "eventually" (por *eventualmente*) | "possibly" / "if necessary" |
| "sensible" (por *sensible*) | "sensitive" |
| "to comprise" (por *comprobar*) | "to verify" / "to check" |
| "important" (por *grande*) | "large" / "significant" |
| "respect to" | "with respect to" |
| "the figure X shows" | "Fig. X shows" (MNRAS abrevia **Fig.**; en inicio de frase, "Figure X") |

## 6. Voz y tiempo verbal

- **"We" está perfectamente aceptado** en MNRAS y es preferible a la pasiva
  constante: "We ran 44 simulations", no "44 simulations were run".
- **Pasado** para lo que hicimos: "We performed…", "The runs reached…".
- **Presente** para lo que el artículo/figura hace y para hechos generales:
  "Fig. 5 shows…", "The instability grows…", "Resistivity allows reconnection".

## 7. Antes de enviar

1. Leer el artículo **en voz alta** completo. Es el mejor detector de calcos.
2. Corrector ortográfico con diccionario **en-GB**.
3. ⚠️ **OJAp no hace copy-editing**: lo que enviemos es lo que se publica.
   Para MNRAS existe Enago (30 % dto. vía OUP); para OJAp recomiendan
   Scitext Cambridge. **Presupuestar una revisión de idioma** — es el punto donde
   un artículo bueno de no nativos se estrella.
4. Pedir al director una lectura de idioma antes del envío.
