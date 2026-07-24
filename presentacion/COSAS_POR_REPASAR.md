# Cosas por repasar — conceptos que el jurado/profesor preguntó (o puede preguntar) y hay que tener claros

Formato por concepto: respuesta corta (la que se dice en la sustentación, ~30–60 s) y detalle (para estudiar).
Origen: ensayo del 22-jul-2026 — el profesor preguntó y no supimos responder en el momento.

---

## 1. FR I y FR II (preguntado el 22-jul — no lo supimos decir)

**Respuesta corta (60 s):**
FR I y FR II son las dos clases **morfológicas de radiofuentes** (radiogalaxias) definidas por
Fanaroff & Riley en 1974, según dónde brilla más la fuente en radio:

- **FR I — "edge-darkened"**: el brillo se concentra **cerca del núcleo** y decae hacia afuera.
  Sus chorros se **frenan y decoliman** a kiloparsecs del centro, formando plumas turbulentas.
  Son las radiofuentes de **menor potencia**. Ejemplos: **M87** (Virgo A), **Centaurus A**.
- **FR II — "edge-brightened"**: el brillo se concentra en los **extremos**, en lóbulos con
  *hotspots* compactos donde el chorro termina contra el medio. Los chorros permanecen
  **colimados y relativistas** hasta el final. Son las de **mayor potencia**. Ejemplo canónico:
  **Cygnus A**.

**Conexión con nuestra tesis:** la transición FR I/FR II se asocia al **frenado del chorro por
arrastre de medio externo** (*entrainment*), y el mecanismo físico que media esa mezcla en la
frontera del chorro es precisamente la **KHI en la capa de cizalla** (cita del deck:
osmanov-2008). Es decir: los FR I son los chorros donde la KHI "ganó" — se desaceleraron y
se volvieron turbulentos; los FR II mantienen la colimación.

**Detalle para estudiar:**
- Criterio original: cociente R = (distancia entre los dos puntos más brillantes) / (tamaño total).
  R < 0.5 → FR I; R > 0.5 → FR II.
- La división en potencia radio está en L_178MHz ≈ 2×10²⁵ W Hz⁻¹ sr⁻¹ (FR II por encima).
- La dicotomía también correlaciona con el entorno (los FR I viven en entornos más densos,
  cúmulos) y posiblemente con la potencia del motor central y la carga másica del chorro.
- Referencia: Fanaroff, B.L. & Riley, J.M. (1974), MNRAS 167, 31P.

---

## 2. S21 — Qué se compara en la gráfica del sigmoide (comentario del profe a la explicación)

**Frase para la expo (decirla ANTES de leer los números):**
"En esta gráfica comparamos **lo medido contra el modelo**: cada punto es la tasa de
crecimiento γ_KHI medida en **una** simulación —la pendiente de ln Ω en su ventana lineal—
graficada contra su conductividad σ; la curva es el **modelo sigmoide de 4 parámetros
ajustado** a los 35 puntos con σ≥1600. Los 9 puntos resistivos no entraron al ajuste:
son la validación *hold-out*."

**Clave:** no son dos teorías ni dos simulaciones — es dato medido vs. modelo ajustado.
La lámina no cambia; cambia cómo se abre la explicación.

---

## 3. S25 — El piso de la ley de potencia es de UNA lámina de corriente (decir los autores)

**Frase para la expo:**
"El valor de comparación Ω^max ∝ σ^{1/2} es el piso teórico de **una única lámina de
corriente Sweet–Parker** — el modelo clásico de reconexión de **Sweet (1958) y
Parker (1957)**, cuyo escalamiento del espesor δ ∝ S^{−1/2} es robusto frente a
correcciones relativistas según **Lyubarsky (2005)**. Nuestro exponente medido es
α = 1.22: excede ese piso en un factor ~2.4. Nuestra hipótesis —declarada como
hipótesis— es que la lámina primaria se **fragmenta** por el modo *tearing*
(**Furth, Killeen & Rosenbluth 1963**), multiplicando la superficie disipativa."

**Clave:** los nombres se dicen EN VOZ ALTA (Sweet, Parker, Lyubarsky, Furth). El dato
de literatura no es de un barrido como el nuestro: es el escalamiento analítico de una
sola lámina; nuestro sistema desarrolla muchas.

---

## 4. Disipación resistiva acumulada por ventanas (S26/lámina 23, panel b) — ✅ REHECHA

**Qué es la gráfica (nueva versión, 23-jul):** el calor de Ohm acumulado
∫∫ ηJ² dA dt (η = 1/σ, positivo-definido) contra σ, evaluado en 4 ventanas:
numérica [0, 2.4) · lineal [2.4, 3.4] · turbulenta (t_peak, 15] · total [0, 15].
OJO: se usa ηJ² y NO E·J crudo — E·J cambia de signo en turbulencia (intercambio
reversible con el campo) y su integral sufre cancelaciones; ηJ² es la disipación
irreversible. Horizonte común t≤15; los runs truncados aparecen como huecos.

**Valores a memorizar (del pipeline, 23-jul):**

| σ | numérica | lineal | turbulenta | total | turb/lineal |
|---|---|---|---|---|---|
| 6000 | 0.033 | 0.062 | 1.60 | 1.90 | **26×** |
| 10⁴ | 0.023 | 0.059 | 0.94 | 1.21 | **16×** |

**Física que hay que saber decir:**
- **La ventana turbulenta domina el presupuesto disipativo** (16–26× la lineal):
  casi todo el calor de Ohm se genera DESPUÉS del pico, en la maraña de láminas
  de corriente de la fase turbulenta. La fase lineal casi no disipa.
- El total crece fuerte del régimen resistivo hacia la transición y alcanza su
  **máximo cerca de la zona de transición** (σ ~ 2000–3000); en el ideal se
  mantiene alto (≈1–2). No colapsa a cero aunque η = 1/σ → 0 porque las láminas
  se intensifican: J² crece más rápido de lo que η cae.
- La ventana numérica DECRECE con σ: es difusión del transiente inicial, y a σ
  baja (η grande) ese transiente disipa más.

---

## 5. Unidades de la conductividad y la resistividad (y del tiempo)

**Regla de oro en la expo:** nunca decir "segundos". El tiempo va en **unidades de
tiempo del código** (tiempos de cruce de luz de la caja, L/c con c=1).

**Respuesta corta si preguntan por las unidades de σ:**
"Trabajamos en unidades de código con c=1: las longitudes se miden en unidades de la
caja L y los tiempos en unidades de L/c. En ese sistema la conductividad σ tiene
unidades de **inverso de tiempo**: su recíproco, 1/σ, es directamente el **tiempo de
relajación resistiva** en unidades de cruce. Por eso σ=100 significa que el campo
eléctrico relaja hacia el valor ideal en τ ≈ 0.01 tiempos de cruce, y σ=10⁴ en 10⁻⁴.
La resistividad es η = 1/σ (difusividad magnética en esas mismas unidades). En SI la
conductividad se mediría en **siemens por metro** (S/m, siemens = 1/ohm), pero el
número del código NO está en S/m: es adimensionalizado."

**Chequeo de consistencia útil:** el número de Reynolds magnético Rm = σ·L·V es
adimensional; con σ=10⁴, L~1, V~1 ⇒ Rm~10⁴ ≫ 1 (régimen cuasi-ideal), y con σ=100,
Rm~10² (la difusión compite). Esa es la manera limpia de traducir σ a física.

---

## 6. Momentos de Vlasov (preguntado el 22-jul) — respaldo B9

**Respuesta corta (60 s):**
"La ecuación de Vlasov gobierna la función de distribución f(x, p, t) en el espacio de
fase — cuántas partículas hay en cada posición con cada momento. Sus **momentos** son
las integrales de f sobre el momento, ponderadas por potencias crecientes de p:

- **Momento 0** (∫f d³p): densidad numérica → ecuación de continuidad.
- **Momento 1** (∫p f d³p): flujo medio → ecuación de momento (Euler).
- **Momento 2** (∫pp f d³p): presión/energía → ecuación de energía.

Cada momento arrastra al siguiente (jerarquía infinita); se **cierra** truncando con
una ecuación de estado. Ese es el puente riguroso del plasma cinético al fluido:
nuestras ecuaciones RRMHD son los primeros momentos de Vlasov + las ecuaciones de
Maxwell + el cierre resistivo de Ohm."

**Repregunta probable — ¿cuándo vale el cierre fluido?** Cuando hay equilibrio local:
colisiones (o giro-radios) rápidos y pequeños frente a las escalas de interés del
sistema. Para escalas de jet ≫ escalas cinéticas, el fluido es la descripción correcta.

**Puntero:** lámina de respaldo B9 ("Del Espacio de Fase al Fluido").

---

## 7. Enstrofía: qué es y en qué unidades (S11)

**La frase de una línea (para abrir S11):**
"La enstrofía es la **variable global de la vorticidad**: el cuadrado de la vorticidad
de perturbación integrado sobre **toda la malla** — un solo número por instante que
mide cuánta rotación ha generado la inestabilidad."

**Definición exacta del pipeline:** Ω_zp(t) = ∫(ω_z')² dA, con ω_z' = ω_z − ⟨ω_z(t=0)⟩_y
(se resta la cizalla base para quedarse solo con la perturbación). Es INTEGRAL, no
promedio: no es "vorticidad/área", es vorticidad² × área.

**Unidades:** [ω] = 1/T ⇒ [Ω] = L²/T² en físico; adimensional en unidades de código.

**Por qué es EL observable de la KHI:**
- La KHI enrolla vórtices: la vorticidad es su firma natural.
- Restar la cizalla base aísla la perturbación (sin contaminación del flujo medio).
- Es cuadrática en la amplitud del modo ⇒ ln Ω(t) = a + 2γ_KHI·t en fase lineal:
  la pendiente da directamente la tasa de crecimiento (ventana canónica t∈[2.4, 3.4]).

---

## 8. Factor CFL (Courant–Friedrichs–Lewy)

**Respuesta corta:**
"Es la condición de estabilidad de los esquemas explícitos: Δt = CFL · Δx/λ_max, con
λ_max la velocidad característica más rápida del sistema (aquí ~c, por el sector
electromagnético). Físicamente: en un paso de tiempo, la información numérica no puede
cruzar más de una fracción (el factor CFL < 1) de una celda — si la señal real viaja
más lejos de lo que el esquema 'mira' por paso, el método se vuelve inestable y explota."

**Qué significa subir/bajar el CFL:**
- **Subirlo** → pasos de tiempo más grandes → simulación más BARATA (menos pasos),
  pero más cerca del límite de estabilidad y con más error temporal.
- **Bajarlo** → pasos más cortos → más CARO (más pasos para el mismo tiempo físico),
  pero más margen de estabilidad frente a rigidez y no linealidades violentas.
- No mejora la resolución espacial (esa es Δx); solo controla el paso temporal.

**Nuestros valores:** CFL = 0.10 en el barrido de 44 simulaciones; en la campaña
magnética B se bajó a 0.04 (σ=6000) y 0.02 (σ=10⁴) porque las corrientes intensas de
las configuraciones magnéticas endurecen el sistema (rigidez resistiva + gradientes
fuertes) y exigen paso más corto para sostener la estabilidad algorítmica.

---

## 9. Congelamiento de las líneas de campo: cuándo sucede y cuándo se rompe (S4)

**Qué es:** teorema de Alfvén (1942): si vale la ley de Ohm ideal, E = −v×B, el flujo
magnético a través de cualquier superficie **que se mueve con el fluido** se conserva.
Consecuencia visual: las líneas de campo quedan "congeladas" al plasma — plasma y campo
se mueven juntos y la topología magnética no puede cambiar.

**Cuándo sucede:** siempre que la conductividad sea efectivamente infinita a la escala
que miras: R_m = σLV ≫ 1. Como R_m depende de la escala L, el congelamiento es una
**propiedad por escala**: el mismo plasma puede estar congelado a escalas grandes y
descongelado en sus capas finas.

**Cuándo se rompe:** donde los gradientes se agudizan — láminas de corriente de espesor
δ pequeño — hasta que R_m(δ) ~ 1: ahí la difusión resistiva compite, las líneas se
"sueltan" y pueden **reconectar** (cambio de topología; energía magnética → calor+flujo).

**El puente con la tesis (frase para S4):** "la KHI enrolla las líneas congeladas y
estira los gradientes hasta fabricar las láminas delgadas donde el congelamiento se
rompe — por eso la pregunta de a qué σ el sistema se comporta como ideal no es trivial,
y por eso necesitamos RRMHD y no MHD ideal."

---

## 10. Por qué σ=10500 (campaña 1) y por qué 6000/10000 (campaña 2)

**¿Por qué el barrido termina en 10500?**
"σ=10500 fue nuestro **límite numérico**: hasta donde el código integró establemente
el barrido con CFL=0.10. A σ más alta, las láminas de corriente se vuelven tan agudas
que la recuperación de primitivas y la rigidez resistiva comprometen la estabilidad
(es exactamente el límite práctico que describe la lámina de Ferrari–Cardano). Y
resultó suficiente: a σ=10500 la sigmoide ya alcanzó el 85% de su plateau y por encima
de σ≈7000 ningún observable cambia — el extremo del barrido ya es un proxy válido del
régimen ideal."
- **Para el artículo:** truncar a σ=10000 (redondo, consistente con la campaña B);
  no cambia ninguna conclusión.

**¿Por qué 6000 y 10000 en la campaña magnética?**
Representantes de los dos regímenes que el barrido identificó:
- **σ=6000 → zona de TRANSICIÓN** (coincide con el estimador M3: inflexión de
  t_peak = 6000±1147): resistividad dinámicamente relevante.
- **σ=10000 → régimen CUASI-IDEAL** (por encima del borde ideal σ≈7000).
- Lógica del experimento: evaluar cada configuración magnética "con y sin"
  resistividad relevante, aislando el papel termodinámico de σ en el balance
  energético. (CFL 0.04 vs 0.02: ver §8.)
