# Revisión de la monografía — tablero con ID fijo

*Actualizado: 2026-06-24 · rama `revision-monografia`*

## 📊 76/151 cerradas (50%) — pendientes 75

> **El # es FIJO** (no cambia aunque cerremos otras). ✅ = cerrada · ⬜ = pendiente.


## Preliminares  — 0/1 cerradas

| # | Estado | Tipo | Sección | Qué dice |
|---|---|---|---|---|
| 1 | ⬜ | SEB | Resumen | no olvidar implementar la campaña de campo magnetico |

## Cap. 1 — Introducción  — 4/4 cerradas

| # | Estado | Tipo | Sección | Qué dice |
|---|---|---|---|---|
| 2 | ✅ | SEB | Contexto de Plasmas Relativistas y Astrofísicos | agregar lo que haga falta de:enfatizar más en las aplicaciones en la astrofísica, por ejemplo: La inestabilidad de Kelvin–Helmholtz (KHI) aparece de manera natural en regiones donde dos flujos de plasma se desplazan con velocidades diferentes. En astrofísica, este tipo de inestabilidad es relevante en jets relativistas, vientos magnetizados, eyecciones compactas y zonas de interacción entre plasmas, donde puede favorecer la mezcla de materia, la formación de vórtices, la generación de estructuras secundarias y la reorganización del campo magnético. (esto hecho con ia, pero pueden humanizarlo o reescribirlo) |
| 3 | ✅ | CLAUDE | Contexto de Plasmas Relativistas y Astrofísicos | Se solapa con §1.3 (que ya lista jets/vientos/GRBs); mejor integrarlo allí, no aquí. Versión humanizada breve: “La KHI surge dondequiera que dos flujos de plasma se deslizan a velocidades distintas; en astrofísica, en los bordes de jets relativistas, vientos magnetizados y eyecciones compactas, donde favorece la mezcla, la formación de vórtices y la reorganización del campo magnético.” |
| 4 | ✅ | REV | Objetivos y Estructura de la Monografía | este objetivo (orientación/intensidad de B) NO se desarrolla en el cuerpo de esta versión; es la campaña pendiente (ver Conclusiones, objetivo 4). Alinear la redacción a “se sientan las bases para evaluar…” o presentarlo como trabajo futuro. |
| 5 | ✅ | CLAUDE | Objetivos y Estructura de la Monografía | Redacción propuesta: “… se sientan las bases para evaluar cómo las variaciones de dirección y magnitud del campo magnético externo modificarían la evolución de la inestabilidad; este objetivo se aborda como continuación inmediata (campaña en curso, cap.~(ref)).” |

## Cap. 2 — Teoría RRMHD  — 36/46 cerradas

| # | Estado | Tipo | Sección | Qué dice |
|---|---|---|---|---|
| 6 | ✅ | SEB | (intro) | cambiar “mencionado” por “explicado en detalle” o ampliar la explicación allí. |
| 7 | ✅ | SEB | (intro) | ¿el observador euleriano va con el fluido? Aclarar la relación entre el observador euleriano (normal a las hipersuperficies) y el comóvil; en el espacio plano coinciden solo si el fluido está en reposo respecto a la malla. |
| 8 | ✅ | SEB | Electrodinámica Covariante y el Tensor de Campo Electromagnético | añadir nota al pie que defina “covarianza” (invariancia de forma de las ecuaciones bajo el grupo de Poincaré). |
| 9 | ✅ | SEB | Electrodinámica Covariante y el Tensor de Campo Electromagnético | reescribir esta frase en términos más algebro-geométricamente correctos. |
| 10 | ✅ | SEB | Electrodinámica Covariante y el Tensor de Campo Electromagnético | completar: ...y de las propiedades geométricas de los mismos (diferenciación exterior). |
| 11 | ✅ | SEB | El Cuadripotencial y la Definición del Tensor de Faraday | arreglar/mejorar este footnote (el del espacio cotangente). |
| 12 | ✅ | SEB | El Cuadripotencial y la Definición del Tensor de Faraday | revisar este apartado (redundancia de gauge) — pendiente de revisión de Sebas. |
| 13 | ✅ | SEB | El Cuadripotencial y la Definición del Tensor de Faraday | añadir un apéndice dedicado a la derivada exterior (definición, propiedades, $d^2=0$, relación con grad/rot/div). |
| 14 | ✅ | SEB | El Cuadripotencial y la Definición del Tensor de Faraday | llevar esta derivación (regla de Leibniz / desarrollo de $F=dA$) al anexo. |
| 15 | ✅ | SEB | El Cuadripotencial y la Definición del Tensor de Faraday | ¿esto es así tal cual? verificar la igualdad $d(dx^)=d^2x^=0$. |
| 16 | ✅ | CLAUDE | El Cuadripotencial y la Definición del Tensor de Faraday | Sí, correcto: $dx^=d(x^)$ es exacta y $d(dx^)=d^2x^=0$ por nilpotencia ($d^2=0$). La escritura $d^2x^$ es legítima (no es una 2.ª derivada del cálculo, sino $d$ aplicado dos veces). |
| 17 | ✅ | SEB | Descomposición Relativa a un Observador | relacionar esta normalización del observador comóvil con el observador euleriano de la malla. |
| 18 | ✅ | SEB | Descomposición Relativa a un Observador | notación: valorar usar el símbolo de Hodge $$ para el dual a lo largo del documento. |
| 19 | ✅ | SEB | Descomposición Relativa a un Observador | ¿“covariantemente” es el término correcto aquí? revisar. |
| 20 | ⬜ | SEB | Descomposición Relativa a un Observador | revisar la estructura y jerarquía del documento: capítulos, secciones, subsecciones, subsubsecciones y niveles siguientes (consistencia y profundidad). |
| 21 | ✅ | SEB | El par inhomogéneo y el acoplamiento con la fuente | verificar si esto es resultado de un lagrangiano; incluir el resultado y el procedimiento, o llevarlo a un anexo. |
| 22 | ✅ | SEB | Derivación a partir de las Densidades Lagrangianas | ¿por qué $S_ em$ no incluye la fuente material ($J_ A^$)? explicarlo; y en un anexo mostrar dónde aparece la energía del campo electromagnético. |
| 23 | ✅ | CLAUDE | Derivación a partir de las Densidades Lagrangianas | Respuesta: aquí es la acción del campo libre porque $T^_ em$ se obtiene variando la métrica (Hilbert) y $J_ A^$ no depende de $g_$, luego no contribuye a $T^_ em$. El acoplamiento $J_ A^$ sí aparece después en la acción aumentada (Sección~(ref)). |
| 24 | ⬜ | SEB | Derivación a partir de las Densidades Lagrangianas | (general) revisar el uso de los términos “tensor” y “forma” a lo largo del capítulo, según el tratamiento de Vargas. |
| 25 | ⬜ | SEB | Derivación a partir de las Densidades Lagrangianas | añadir en el anexo la derivación paso a paso de $T^_ em$ (derivada funcional de Hilbert). |
| 26 | ✅ | SEB | Derivación a partir de las Densidades Lagrangianas | verificar si la acción del fluido perfecto $S_ fluid= p-g\,d^4x$ es efectivamente válida en RRMHD (¿se modifica por la parte resistiva?). |
| 27 | ✅ | CLAUDE | Derivación a partir de las Densidades Lagrangianas | Sí es válida: en RRMHD el fluido sigue siendo perfecto; la disipación vive en el sector electromagnético (ley de Ohm con $$ finita), no en $T^_ fluid$. Por eso $S_ fluid= p-g\,d^4x$ (acción de Taub) no cambia. |
| 28 | ✅ | CLAUDE | Derivación a partir de las Densidades Lagrangianas | Símbolo ambiguo: aquí $$ es densidad de energía (incluye masa en reposo, $ h=+p$), pero en §(ref) se usa $h=1++p/$ con $$ = energía interna específica. Unificar: $$ para densidad y $$ (o $e$) para la específica, como en el Anexo ($h=1+-1p/$). |
| 29 | ⬜ | SEB | Dinámica Acoplada y el Sistema Completo de RRMHD | hacer explícita la derivación con $T^_ tot$ y separarla; añadir un anexo completo con el paso de (2.30) a (2.31). |
| 30 | ✅ | SEB | Dinámica Acoplada y el Sistema Completo de RRMHD | se nombra “RRMHD” pero aún no se ha introducido la resistividad/ley de Ohm (§(ref)); reordenar o aclarar para no adelantar el término. |
| 31 | ✅ | SEB | Dinámica Acoplada y el Sistema Completo de RRMHD | revisar este sistema de ecuaciones (2.32)--(2.35) y las relaciones entre ellas. |
| 32 | ✅ | SEB | El Sistema Aumentado de Maxwell | añadir una nota al pie explicando el acrónimo/método GLM (Generalized Lagrange Multipliers). |
| 33 | ✅ | CLAUDE | El Sistema Aumentado de Maxwell | Footnote propuesta: “GLM (Generalized Lagrange Multipliers): técnica de Dedner_etal:2002 que acopla las restricciones de divergencia ($\!\! B=0$ y la ley de Gauss) a campos escalares auxiliares, convirtiéndolas en ecuaciones de transporte amortiguadas que propagan y disipan el error en vez de acumularlo.” |
| 34 | ✅ | SEB | Extensión Lagrangiana y el Campo Auxiliar Eléctrico $$ | explicar la diferencia y la justificación de esta acción extendida frente a la acción $S_ em$ original. |
| 35 | ✅ | SEB | Extensión Lagrangiana y el Campo Auxiliar Eléctrico $$ | explicar la función e implicación física del campo $$, y explicar el tercer término de la acción ($12_^$). |
| 36 | ✅ | SEB | Extensión Lagrangiana y el Campo Auxiliar Eléctrico $$ | ¿esta es la ecuación del telégrafo? aclarar: aquí es de onda pura; la forma telegráfica aparece luego con el amortiguamiento $$. |
| 37 | ⬜ | CLAUDE | Extensión Lagrangiana y el Campo Auxiliar Eléctrico $$ | Confirmado: aquí es onda pura. Pero hay un salto de coherencia: la acción y las Ecs.~(ref)--(ref) dan un sistema de segundo orden (telégrafo), mientras que el sistema 3+1 que integra el código, Ecs.~(ref)--(ref), es de primer orden (forma de Dedner). No se muestra la reducción de uno a otro; conviene aclararlo o presentar directamente la forma de Dedner. |
| 38 | ✅ | SEB | Simetría Dual y el Campo Auxiliar Magnético $$ | añadir nota al pie aclarando que la formulación con potencial dual violaría esta invariancia/simetría de Hodge. |
| 39 | ✅ | SEB | Simetría Dual y el Campo Auxiliar Magnético $$ | ¿hay forma de introducir estos términos de amortiguamiento de manera formal (derivada) y no ad-hoc? |
| 40 | ✅ | SEB | La Ecuación del Telégrafo: Origen Covariante y Causalidad Disipativa | revisar y añadir cita(s) de respaldo. |
| 41 | ⬜ | SEB | Descomposición 3+1 del Sistema Aumentado | añadir un anexo con los procedimientos/derivaciones de las ecuaciones (2.40)--(2.48). |
| 42 | ✅ | CLAUDE | Descomposición 3+1 del Sistema Aumentado | Inconsistencia de notación con el Anexo (Ec.~(ref)): aquí $$ limpia la ley de Gauss eléctrica y $$ la magnética; en el anexo se usan $$ (eléctrica) y $$ (magnética), con las letras intercambiadas. Unificar en todo el documento. |
| 43 | ✅ | SEB | Descomposición de la Cuadricorriente y la Ley de Ohm Relativista | citar y revisar toda esta sección. |
| 44 | ⬜ | SEB | Descomposición Ortogonal del Cuadrivector Corriente | añadir una figura que distinga $_e$ (propia, marco comóvil) de $_q$ (laboratorio), y en general el marco comóvil vs.\ el de laboratorio. |
| 45 | ✅ | CLAUDE | Resumen del Sistema RRMHD en Forma Conservativa | Verificado contra el código Cueva (06\_conserved\_var.f95): convención TOTAL correcta; $$ lleva $ h^2$ (con masa en reposo, sin restar $D$). Consistente con el Anexo. Da por resuelta la antigua nota roja de variables conservadas. |
| 46 | ✅ | CLAUDE | Resumen del Sistema RRMHD en Forma Conservativa | En contexto relativista “invarianza de Galileo” es impreciso (el término de Powell se asocia a la invariancia galileana en MHD clásica). Aquí conviene hablar de consistencia Lorentz/entropía, o atribuirlo con cuidado a su origen clásico. |
| 47 | ⬜ | SEB | Análisis de la KHI en el Límite Lineal | Expandir la explicaćion , implicaćion y justificaíon de lo que se dice ahí, es mas como justificar la aparicion de este tema en el marco teorico, entra un poco ortodoxo y seco |
| 48 | ⬜ | CLAUDE | Análisis de la KHI en el Límite Lineal | Marco sugerido: enlazar con el cap.~3 (cierre §3.5): el $[ M]=0$ existe formalmente, pero en RRMHD no se reduce a una relación de dispersión algebraica cerrada (Ohm resistiva = parabólica). Decir que aquí se plantea el problema y que su forma cerrada solo existe en los límites ideal/RMHD (cap.~3) lo haría menos seco y más justificado. |
| 49 | ✅ | CLAUDE | Inercia Térmica Relativista y Anisotropía Magnética | Estilo: cuando los autores son el sujeto (“… demostraron”), va textcite (ya corregido aquí). Revisar otros “ parencite\…\ + verbo” en el capítulo. |
| 50 | ✅ | CLAUDE | Inercia Térmica Relativista y Anisotropía Magnética | Esta es la definición correcta y estándar ($w= h^2$). El cap.~3 (§3.4.1) escribe $w= h^2+B^2$: unificar a esta (quitar el $+B^2$ del cap.~3), como pide la nota roja de ese capítulo. |
| 51 | ⬜ | SEB | Enstrofía de Perturbación y Extracción de $$ | En general, revisar todas las citas bien plantedas y utilizadas, y añadir en el marco teorico todas las herramientas estadisticas utilizadad, o discutir si deben de ser anexos , ya que son erramientas validas pero poco convencionales |

## Cap. 3 — KHI  — 10/10 cerradas

| # | Estado | Tipo | Sección | Qué dice |
|---|---|---|---|---|
| 52 | ✅ | SEB | Planteamiento Hidrodinámico | añadir una figura de la condición inicial / inestabilidad donde se distinga cada lámina de cizalla. |
| 53 | ✅ | SEB | Extensión Magnetohidrodinámica Ideal (MHD) | revisar consistencia con el montaje: aquí $B_0$ va alineado al flujo (caso clásico ilustrativo); en la simulación el campo es guía ($B_z$ dominante, componente paralela débil). |
| 54 | ✅ | CLAUDE | Extensión Magnetohidrodinámica Ideal (MHD) | Observación correcta. Basta una frase: “este caso alineado es ilustrativo; el montaje numérico usa campo guía con $B_z$ dominante (cap.~5), de modo que $ k B0$ (presión, no tensión)”. |
| 55 | ✅ | REV | Correcciones Relativistas y Factor de Inercia | inconsistencia con el cap.~2, donde la inercia efectiva transversal se define como $w= h^2$ (sin el término magnético $B^2$). Unificar la definición entre capítulos. |
| 56 | ✅ | SEB | Correcciones Relativistas y Factor de Inercia | revisar la definición de $w$ contra la bibliografía (Bodo, Osmanov) y unificarla con el cap.~2. |
| 57 | ✅ | CLAUDE | Correcciones Relativistas y Factor de Inercia | Corrección recomendada: $w= h^2+B^2 w= h^2$ (como en cap.~2, ya verificado). El $+B^2$ no es inercia térmica transversal; la tensión magnética entra aparte por $( k B_0)^2$. Esto resuelve la nota roja. (Mismo $$ ambiguo que en cap.~2: $h=1++p/$ usa $$ específica.) |
| 58 | ✅ | SEB | El Rol de la Resistividad y la Relajación Topológica | ¿se puede deducir una relación de dispersión como en MHD/clásica? — ver abajo: en RRMHD NO es posible de forma algebraica cerrada. |
| 59 | ✅ | CLAUDE | El Rol de la Resistividad y la Relajación Topológica | Esta pregunta ya queda respondida por el cierre de §3.5 (párrafo nuevo sobre por qué en RRMHD no hay dispersión algebraica cerrada). Sugerencia: dejar esta nota como puntero a ese párrafo o borrarla para no duplicar. |
| 60 | ✅ | SEB | Motivación Numérica y Relevancia Computacional | explicar a fondo (o en footnote) el esquema IMEX: advección explícita del fluido $+$ tratamiento implícito de las fuentes disipativas rígidas. |
| 61 | ✅ | CLAUDE | Motivación Numérica y Relevancia Computacional | Footnote IMEX propuesta: “IMEX-RK (Implicit--Explicit Runge--Kutta): integra de forma explícita los flujos advectivos no rígidos e implícita las fuentes resistivas rígidas ($$), evitando el paso de tiempo $ t^-1$ que impondría un esquema totalmente explícito a alta conductividad.” Coherente con la implementación del Cueva (Pareschi--Russo + Aloy--Cordero). |

## Cap. 4 — Métodos numéricos  — 7/7 cerradas

| # | Estado | Tipo | Sección | Qué dice |
|---|---|---|---|---|
| 62 | ✅ | SEB | (intro) | añadir figuras para visualizar los volúmenes finitos, los flujos interfasiales y la discretización. |
| 63 | ✅ | CLAUDE | (intro) | No bloquea la entrega: una sola figura esquemática (celda $i$, interfaces $i1/2$, stencil de 5 puntos de MP5) basta. Si falta tiempo, puede omitirse sin perder rigor. |
| 64 | ✅ | SEB | Acoplamiento Numérico con el Sistema Aumentado GLM | el GLM ya se trató en el cap.~2; condensar esta introducción para no ser repetitivo ni redundante. |
| 65 | ✅ | CLAUDE | Acoplamiento Numérico con el Sistema Aumentado GLM | De acuerdo: reducir a 1--2 frases con ref a §(ref). Aquí basta decir “se implementa la limpieza GLM ya derivada (§ref), con velocidad de limpieza $c_h=1$”. |
| 66 | ✅ | SEB | Estructura Espectral de los Potenciales Auxiliares | ¿dónde se muestra esta diagonalización? ¿es pertinente incluirla explícitamente? |
| 67 | ✅ | CLAUDE | Estructura Espectral de los Potenciales Auxiliares | No es esencial en el cuerpo: basta afirmar que las submatrices $22$ tienen autovalores $ c_h$ (de ahí la propagación causal). Si se quiere el detalle, llevarlo al anexo. Conecta con la nota de cap.~2 sobre derivar el 2$$2 desde el sistema 3+1. |
| 68 | ✅ | CLAUDE | Recuperación de Variables Primitivas: la Cuártica del Factor de Lorentz | Verificado contra el código (12\_varprimitive.f95, subrutina varprimitivecardano): cuártica en $$ + Tchirnhaus + refinamiento Newton, correcto. Cita: el esquema de recuperación es del Cueva; citar miranda-aranguren-2018 aquí (mizuno-2013 es el paper de EoS, no de recuperación de primitivas). |

## Cap. 5 — Setup experimental  — 3/12 cerradas

| # | Estado | Tipo | Sección | Qué dice |
|---|---|---|---|---|
| 69 | ⬜ | SEB | Condiciones Iniciales del Problema | inconexo, necesita continuidad. |
| 70 | ✅ | SEB | Condiciones Iniciales del Problema | Aclarar que esta configuración del campo $B$ es solo para el objetivo~2 (campaña magnética); en esa comparación estas componentes serán nuestras variables. |
| 71 | ⬜ | SEB | Dominio Computacional, Discretización y Sistema de Unidades | Mirar bien en el código las condiciones de frontera. |
| 72 | ⬜ | CLAUDE | Dominio Computacional, Discretización y Sistema de Unidades | Según el propio §(ref) y el código: periódicas en $y$ y abiertas (derivada normal nula / flujo libre) en $x$. Confirmar el flag exacto en parameters.f95; la descripción del texto es consistente. |
| 73 | ⬜ | SEB | Sistema de unidades y equivalencia temporal. | Dar un ejemplo concreto con escalas astrofísicas, deduciendo las dimensiones e incluso mostrando el radio de un vórtice generado en los hd plots. |
| 74 | ✅ | SEB | Exploración del Espacio de Parámetros: Resistividad | Falta poner el espacio de parámetros dictado por la campaña de campo magnético, en $=6000$ y $=10000$. |
| 75 | ✅ | CLAUDE | Exploración del Espacio de Parámetros: Resistividad | Pendiente de los datos de la campaña (martes). Marcador: al llegar, tabular los $$ usados (6000, 10000), las orientaciones/intensidades de $ B$ y el CFL de cada corrida. |
| 76 | ⬜ | SEB | Variables de Control y Diagnóstico | Mirar cuáles de estos diagnósticos sí se usan y cuáles no; además, seguro se usan otros, como campos y energías. |
| 77 | ⬜ | CLAUDE | Variables de Control y Diagnóstico | Del código: se usan $_z$, $_ tot$, $f_Vz$ y $'_zp$ (estos en cap.~6) y además $J_$, $ E\!\! J$ y $E_ mag$ (§(ref)). Conviene listar también estos últimos aquí para que la sección de diagnósticos quede completa. |
| 123 | ⬜ | SEB | Conductividades y paso temporal. | revisar la matriz final $$CFL realmente usada: los datos de llegada incluyen también $=4500,5500,6500,7000$ y versiones CFL $0.10/0.04/0.02$; definir cuáles entran en la monografía. |
| 124 | ⬜ | SEB | Conductividades y paso temporal. | la comparación entre $$ queda entonces a CFL mixto; decidir si se homogeniza para el análisis final. |
| 125 | ⬜ | SEB | Conductividades y paso temporal. | el análisis cuantitativo (\,$$ vs $B$, $^$ vs $$, conversión magnética--cinética\,) se desarrolla en el Capítulo~(ref); resultados preliminares, pendientes de revisión a fondo (no fiarse aún del informe de llegada). |

## Cap. 6 — Resultados  — 16/62 cerradas

| # | Estado | Tipo | Sección | Qué dice |
|---|---|---|---|---|
| 78 | ⬜ | SEB | (intro) | Añadir toda la parte de la campaña de variación magnética: los $$ utilizados y los valores de CFL empleados en cada caso, y por qué. |
| 79 | ⬜ | SEB | Resultados del ajuste | Expandir esto, ya que puede ser muy perjudicial. |
| 80 | ⬜ | SEB | Validación estadística del modelo | Aclarar esto; suena muy a IA. |
| 81 | ⬜ | SEB | Conductividad crítica $$ y sus tres fuentes de incertidumbre | Mostrar explícitamente todas las gráficas que sostienen este resultado; sí o sí deben salir. |
| 82 | ⬜ | SEB | Conductividad crítica $$ y sus tres fuentes de incertidumbre | Se dejó a un lado todos los datos, análisis y construcción de la zona de transición. |
| 83 | ⬜ | SEB | Leyes de potencia para $()$ | confuso; suena a IA. |
| 84 | ⬜ | SEB | Leyes de potencia para $()$ | afirmación de cita: ¿es de la fuente o es interna? Revisar. |
| 85 | ⬜ | SEB | Leyes de potencia para $()$ | ¿en qué se basa esta justificación? |
| 86 | ⬜ | SEB | Leyes de potencia para $()$ | tasa de reconexión: ¿lo justifico? ¿se puede graficar y sustentar? |
| 87 | ✅ | SEB | Leyes de potencia para $()$ | ¿qué es Res-RMHD? |
| 88 | ✅ | CLAUDE | Leyes de potencia para $()$ | Res-RMHD = Resistive Relativistic MHD (el marco de todo el trabajo); aquí alude a esquemas numéricos de alto orden para Res-RMHD (mignone2024). Conviene definir la sigla en su primer uso o usar “RRMHD” para no introducir una variante. |
| 89 | ⬜ | SEB | Leyes de potencia para $()$ | revisar la validez y el argumento. |
| 90 | ⬜ | SEB | Corrientes, disipación y energía magnética | Revisar esto: ¿qué? Rompe toda la fiabilidad; además, estos resultados justifican la zona de transición. |
| 91 | ⬜ | SEB | Estructuras secundarias y anisotropía fuera del plano | Esto es increíble; revisar conexión y correlación. |
| 92 | ✅ | SEB | Contraste con la teoría lineal | ¿De dónde sale este valor? ¿Dónde está revisado? |
| 93 | ✅ | CLAUDE | Contraste con la teoría lineal | $=(C+_0)\,a_kh/v_sh=1.030.05/0.5=0.103$. La cadena completa (Michalke $$ Lees--Lin $$ medido) está recomputada y verificada en el Anexo~(ref); conviene citar ese anexo aquí. |
| 94 | ⬜ | SEB | Techo hidrodinámico inviscido (ecuación de Rayleigh) | revisar la validez de las fuentes. |
| 95 | ⬜ | SEB | El carácter dual del montaje no altera el techo | En la figura, no uses la expresión “tus datos”. |
| 96 | ⬜ | SEB | Predicción RMHD compresible (Lees--Lin) | ¿cuál es mi dato en la figura? |
| 97 | ✅ | SEB | Velocidades características y números de Mach | buscar dónde poner el footnote de la velocidad de Alfvén. |
| 98 | ✅ | CLAUDE | Velocidades características y números de Mach | Ubicación natural: primera aparición de $V_A$ en la tabla de Mach (§6.7.4). Footnote: “$V_A=B^2/( h+B^2)$ (con $c=1$): velocidad de Alfvén relativista.” Ya hay un footnote de $V_A$ en el cap.~1; podría bastar un ref a él. |
| 99 | ⬜ | SEB | Velocidades características y números de Mach | expandir mejor la justificación. |
| 100 | ⬜ | SEB | Contraste con los marcos MHD, RMHD y RRMHD | arreglar esto. |
| 101 | ⬜ | SEB | Contraste con los marcos MHD, RMHD y RRMHD | ¿estamos seguros? |
| 102 | ⬜ | SEB | Buen planteamiento y papel de la resistividad | Poner y organizar todo para la variación del campo magnético. |
| 103 | ✅ | REV | Buen planteamiento y papel de la resistividad | TONO (revisor): “prueba decisiva” suena tajante y no sabemos si lo será; considerar “una prueba más exhaustiva”. |
| 104 | ✅ | REV | Limitaciones del análisis y perspectivas | TONO (revisor): esta sección suena a IA y da por seguro que las pruebas futuras “arreglarían” las discrepancias; en realidad no se sabe. Reescribir en condicional/posibilidades (“podría”, “permitiría”) en vez de certezas, y revisar el uso de “prueba decisiva”/“máxima prioridad”. |
| 105 | ⬜ | SEB | Limitaciones del análisis y perspectivas | límite numérico. |
| 106 | ✅ | SEB | Limitaciones del análisis y perspectivas | ¿ya existe? |
| 107 | ✅ | CLAUDE | Limitaciones del análisis y perspectivas | Sí existe: chow2023 da el análisis lineal RMHD magnetizado (el polinomio de alto grado); ya está citado y subido al NotebookLM. La sustitución $c_s v_f$ es la aproximación que aquí se usa en vez de resolver ese polinomio completo. |
| 108 | ⬜ | SEB | Limitaciones del análisis y perspectivas | esto lo estamos haciendo nosotros (campaña en curso). |
| 109 | ⬜ | SEB | Limitaciones del análisis y perspectivas | ¿estamos más arriba del radio de sincrotrón, no? |
| 110 | ⬜ | CLAUDE | Limitaciones del análisis y perspectivas | El Cueva es un código de fluido (RRMHD), sin escala cinética/giroradio: no hay “radio de sincrotrón” resuelto. La escala micro relevante es la capa resistiva $ S^-1/2$. Si la duda es por Hall/anisotropía, eso sí queda fuera del modelo escalar de $$ (ya anotado en limitaciones). |
| 111 | ⬜ | SEB | Limitaciones del análisis y perspectivas | No existe inestabilidad, o al menos no se generan tasas de crecimiento. Esto está mal. |
| 112 | ⬜ | CLAUDE | Limitaciones del análisis y perspectivas | De acuerdo: a $500$ el problema no es “ajuste pobre” sino que la disipación domina desde $t=0$ y no hay fase lineal limpia $$ no se puede extraer una $$ fiable. Reformular así (no “$R^2<0.7$” a secas). |
| 113 | ⬜ | SEB | Limitaciones del análisis y perspectivas | variación y orientación, inminentes. |
| 126 | ⬜ | BRY | Variación de Intensidad y Orientación del Campo Magnético | Sección redactada por Bryan (campaña magnética, objetivo 4); pendiente cablear figuras/tablas de ANALISIS\_LIMPIO\_FINAL/figuras. |
| 127 | ⬜ | CLAUDE | Variación de Intensidad y Orientación del Campo Magnético | Notación: usar $$ como en el resto del documento, no $_i$. |
| 128 | ⬜ | CLAUDE | Variación de Intensidad y Orientación del Campo Magnético | Definir/referenciar aquí presión magnética ($P_ mag=B^2/2$) y tensión magnética ($( k B)^2$), clave de todo el capítulo. La tensión la ejerce la componente paralela a $ k$ (aquí $B_y$; el flujo y $ k$ van en $ y$). |
| 129 | ⬜ | CLAUDE | Impacto de la intensidad del campo magnético en el desarrollo de la inestabilidad | OJO física: en la Campaña A la orientación es Mizuno ($B_y=B_00.02$ pequeña; $B_z=B_02$ domina). La tensión $( k B)^2 B_y^2$ es débil ($M_A,=9.4$, super-Alfvénico, §(ref)). ¿La supresión al subir $B_0$ es por tensión o más bien por presión/magnetización ($$)? El texto lo atribuye todo a la tensión; verificar. |
| 130 | ⬜ | CLAUDE | Impacto de la intensidad del campo magnético en el desarrollo de la inestabilidad | ¿Se estabiliza el modo lineal ($$) o solo se atenúa/retrasa el pico no lineal? Respaldarlo midiendo $$ (pendiente en la ventana) por $B_0$. |
| 131 | ⬜ | CLAUDE | Impacto de la intensidad del campo magnético en el desarrollo de la inestabilidad | La tabla solo incluye $B_01.0$ (casos A3, A4, A5): las configuraciones de campo débil $B_0=0.25$ y $0.5$ (alta $$) crashearon en $t1$ antes de desarrollar la inestabilidad, por lo que se excluyeron de los datos limpios. |
| 132 | ⬜ | CLAUDE | Impacto de la intensidad del campo magnético en el desarrollo de la inestabilidad | Los colores NO coinciden: las figuras regeneradas usan el ciclo por defecto (A3$=$azul, A4$=$naranja, A5$=$verde), no “verde/rojo/morado”. Unificar: re-generar con ese esquema o quitar las menciones de color del texto. Igual con la “curva roja $=30°$” más abajo. |
| 133 | ⬜ | CLAUDE | Impacto de la intensidad del campo magnético en el desarrollo de la inestabilidad | Verificar los tiempos de pico ($t5$ para $B_0=1$; $t7$ para $B_0=2$) midiendo $t_ peak$ real. |
| 134 | ⬜ | CLAUDE | Impacto de la intensidad del campo magnético en el desarrollo de la inestabilidad | Notación: $_Zp_zp$ (minúscula; macro Ozp) aquí y en toda la sección. Los valores $85$ vs $45$ concuerdan con §(ref). |
| 135 | ⬜ | CLAUDE | Variación en el plano $y-z$ | ¿Por qué solo $=5.7°$ y no $=0°$? A $=0$ (guía pura, $ k B=0$, sin tensión) cabría esperar la KHI más limpia; sin embargo $^(=0)$ es BAJO ($14$, Fig. del director). Aclarar la contraintuición. |
| 136 | ⬜ | CLAUDE | Variación en el plano $y-z$ | Precisar: la presión de $B_z$ entra vía la velocidad magnetosónica/compresibilidad, no en $w= h^2$ (que NO lleva $B^2$, ver cap.~2/3). |
| 137 | ⬜ | CLAUDE | Variación en el plano $y-z$ | Falta $=90°$ aquí: es la de máxima tensión ($ k B$ máximo) y debería ser la más suprimida; incluir su comportamiento. |
| 138 | ⬜ | CLAUDE | Variación en el plano $y-z$ | Esta figura concreta la duda de las notas previas: el mínimo de $^$ NO está en $=90^$ (máxima tensión, $ k B$ máximo) sino en ángulos intermedios, y $=90^$ da el valor MÁS ALTO. Hay que explicar físicamente esta no-monotonía antes de afirmar que “la tensión suprime”. |
| 139 | ✅ | CLAUDE | Variación en el plano $y-z$ | Orden: la Fig.~(ref) aparece en el .tex antes que la (ref), pero el texto cita primero la de $E_ mag$. Reordenar. Además “Las Figuras” (plural) con una sola referencia. |
| 140 | ✅ | CLAUDE | Variación en el plano $y-z$ | Referencia incorrecta: $^$ vs $E_ mag$ muestra co-amplificación (corr.\ positiva), NO el intercambio mediado por disipación. El intercambio real es la Fig.~(ref) (tasas). Reasignar. |
| 141 | ✅ | CLAUDE | Variación en el plano $y-z$ | Referencia suelta (sin frase). Integrarla en el párrafo de las derivadas, abajo. |
| 142 | ⬜ | CLAUDE | Variación en el plano $y-z$ | Verificar que el colormap de la Fig.~(ref) coincida con la descripción (azul oscuro $$ morado/fucsia $$ amarillo según $t$); mi script usa el colormap por defecto. |
| 143 | ✅ | SEB | Variación en el plano $y-z$ | Insertar todas las variables exigidas por el director para esta campaña |
| 144 | ✅ | CLAUDE | Variación en el plano $y-z$ | Coloqué la correlación cruzada $$--$ B^2$ vs $$ (fuerza de acople y retardo $$ del pico). Si el director pide MÁS variables (p.ej. $E\!\!J$, $J_z$, $E_ mag$), hay figuras listas en figuras/director/ para añadir aquí. |
| 145 | ⬜ | CLAUDE | Variación en el plano $x-z$ (Campaña C) | Jerarquía inconsistente: “intensidad” es subsection y las orientaciones subsubsection* (sin numerar); y la de $y$-$z$ no dice “(Campaña B)”. Unificar niveles y etiquetas. |
| 146 | ⬜ | CLAUDE | Variación en el plano $x-z$ (Campaña C) | INCONSISTENCIA con el cap.~5: allí (siguiendo al profe) la Campaña C es “componente paralela al flujo que estabiliza por tensión”; AQUÍ (correcto) es “sin tensión”. La tensión la da $B_y$ ($ k$, flujo en $ y$); en C $B_y=0$ y $B_x$ es normal a la interfaz ($ k$) $$ NO hay tensión. CORREGIR el cap.~5 (“paralela al flujo” es engañoso). |
| 147 | ⬜ | CLAUDE | Variación en el plano $x-z$ (Campaña C) | En C, $\| B\|$ (y la presión) es constante en $$; la variación con $$ no puede venir de la presión. Aclarar qué cambia con $$ en C (dirección de $B_x$ respecto a la interfaz / reconexión). |
| 148 | ⬜ | CLAUDE | Balance energético y procesos disipativos | Sección redactada por Claude desde los datos limpios (scripts analisis\_energia\_disipacion.py). REVISAR redacción y física. Decisión de fondo aquí: en las campañas de orientación (B y C) la mayoría de las curvas no desarrollan una fase de crecimiento exponencial limpia (solo $=5.7^$ y, a $=10000$, $=30,45^$), por lo que NO se reporta $$ para B/C salvo como dato puntual; el análisis se centra en el intercambio energético y la disipación. Las figuras y los valores numéricos están verificados; el relato físico es mi interpretación y debe contrastarse. |
| 149 | ⬜ | CLAUDE | Balance energético y procesos disipativos | Caveat numérico para verificar: $E_int$ se estima como $ p$ (proxy del calor); a $=90^$, $=6000$ la óhmica acumulada llega a igualar/superar $ E_int$ (ver Fig.~(ref)), lo que indica que parte del calor óhmico se compensa con pérdidas advectivas o que el proxy subestima; conviene afinar la definición de $E_int$ antes de hacer afirmaciones cuantitativas finas sobre fracciones. |
| 150 | ✅ | CLAUDE | Variación en el plano $y-z$ | Corrección metodológica (REVISAR): un análisis previo comparaba el único máximo global de $_zp$ con el único mínimo global de $E_ mag$; para señales oscilatorias eso es engañoso (el mínimo global suele caer en el transitorio y da desfases espurios de varios $t$, incluso de signo opuesto). Aquí se identifican todos los extremos locales por cruce-cero de la derivada (filtrados por prominencia) y se mide el desfase ciclo a ciclo. Esto reemplaza la figura y la conclusión anteriores sobre “orden temporal”. |
| 151 | ⬜ | CLAUDE | Variación en el plano $y-z$ | REVISAR redacción/física. Cambio de enfoque respecto a versiones previas: el análisis de máximos y mínimos se hace ahora entre $E_ kin$ y $E_ mag$ (canal de intercambio directo), no entre $_zp$ y $E_ mag$. Motivo verificado en los datos: la enstrofía co-amplifica con la inestabilidad (correlación de valores positiva, efecto de envolvente), de modo que la anti-fase real del intercambio solo se ve limpia en el par cinético--magnético. La anti-correlación de tasas (Fig.~(ref)) es la versión diferencial de este mismo hecho. |

## Cap. 7 — Conclusiones  — 0/6 cerradas

| # | Estado | Tipo | Sección | Qué dice |
|---|---|---|---|---|
| 114 | ⬜ | SEB | (intro) | + variación de campo magnético. |
| 115 | ⬜ | CLAUDE | (intro) | Sí: al llegar los datos, añadir un párrafo/objetivo con la conclusión de la campaña de B (intensidad/orientación). Hasta entonces el objetivo 4 se lee como “en curso”. |
| 116 | ⬜ | SEB | (1) Efecto de la resistividad sobre la tasa de crecimiento lineal. | Ver cómo la correlación energética en $=6000$ y $=10000$, en compañía del campo magnético, habla del papel de la resistividad. |
| 117 | ⬜ | SEB | (3) Efecto sobre las variables globales. | Se puede agregar un análisis igual al del campo magnético para ver la correlación de las variables energéticas y cómo esta cambia con $$. |
| 118 | ⬜ | SEB | Trabajo Futuro | no es válido: ya no es “trabajo futuro”, la campaña está en curso. |
| 119 | ⬜ | CLAUDE | Trabajo Futuro | Correcto: mover “Campaña de campo magnético” de Trabajo Futuro a Resultados/Conclusiones una vez integrada (martes). Si para la entrega aún no está, dejarla como “en curso”, no como futuro. |

## Anexos  — 0/3 cerradas

| # | Estado | Tipo | Sección | Qué dice |
|---|---|---|---|---|
| 120 | ⬜ | SEB | Justificación de $C+_0$: derivación paso a paso | Revisar y contrastar con la bibliografía, o directamente solo poner los resultados. |
| 121 | ⬜ | CLAUDE | Justificación de $C+_0$: derivación paso a paso | El anexo ya recomputa todo de forma independiente y coincide con el cuerpo; las fuentes (Michalke, Landau, Bodo, Chow) están verificadas. Decisión: dejarlo como auditoría (valor añadido) o condensarlo a la tabla-síntesis. La nota roja del “Veredicto” (duplicado con §6.7) apunta a recortar esa subsección, no la auditoría numérica. |
| 122 | ⬜ | REV | Veredicto: validez teórica del montaje | REVISAR (revisor): esta subsección repite la discusión de robustez/consistencia ya hecha (con más detalle) en el cap.\ de Resultados (§(ref)). Considerar recortarla a una síntesis breve específica del apéndice o eliminarla para no duplicar. |
