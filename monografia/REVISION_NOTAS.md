# Revisión de la monografía — notas pendientes de cambio

*Generado: 2026-06-21 · rama `revision-monografia`*

**Total: 88 notas** — 🔴 REV (revisor, rojo): 5 · 🔵 SEB (Sebastián, azul): 83 · 🟢 BRY (Bryan, verde): 0

> Cada nota aparece en el PDF como `[REV: …]` en su color. Esta tabla las condensa para revisión de Director y compañero.


## Preliminares

| # | Tipo | Sección | Qué dice / acción |
|---|------|---------|-------------------|
| 1 | 🔵 SEB | Resumen | no olvidar implementar la campaña de campo magnetico |

## Cap. 1 — Introducción

| # | Tipo | Sección | Qué dice / acción |
|---|------|---------|-------------------|
| 2 | 🔵 SEB | Contexto de Plasmas Relativistas y Astrofísicos | agregar lo que haga falta de:enfatizar más en las aplicaciones en la astrofísica, por ejemplo: La inestabilidad de Kelvin–Helmholtz (KHI) aparece de manera natural en regiones donde dos flujos de plasma se desplazan con velocidades diferentes. En astrofísica, este tipo de inestabilidad es relevante en jets relativistas, vientos magnetizados, eyecciones compactas y zonas de interacción entre plasmas, donde puede favorecer la mezcla de materia, la formación de vórtices, la generación de estructuras secundarias y la reorganización del campo magnético. (esto hecho con ia, pero pueden humanizarlo o reescribirlo) |
| 3 | 🔴 REV | Objetivos y Estructura de la Monografía | este objetivo (orientación/intensidad de B) NO se desarrolla en el cuerpo de esta versión; es la campaña pendiente (ver Conclusiones, objetivo 4). Alinear la redacción a “se sientan las bases para evaluar…” o presentarlo como trabajo futuro. |

## Cap. 2 — Teoría RRMHD

| # | Tipo | Sección | Qué dice / acción |
|---|------|---------|-------------------|
| 4 | 🔵 SEB | (intro del capítulo) | cambiar “mencionado” por “explicado en detalle” o ampliar la explicación allí. |
| 5 | 🔵 SEB | (intro del capítulo) | ¿el observador euleriano va con el fluido? Aclarar la relación entre el observador euleriano (normal a las hipersuperficies) y el comóvil; en el espacio plano coinciden solo si el fluido está en reposo respecto a la malla. |
| 6 | 🔵 SEB | Electrodinámica Covariante y el Tensor de Campo Electromagnético | añadir nota al pie que defina “covarianza” (invariancia de forma de las ecuaciones bajo el grupo de Poincaré). |
| 7 | 🔵 SEB | Electrodinámica Covariante y el Tensor de Campo Electromagnético | reescribir esta frase en términos más algebro-geométricamente correctos. |
| 8 | 🔵 SEB | Electrodinámica Covariante y el Tensor de Campo Electromagnético | completar: ...y de las propiedades geométricas de los mismos (diferenciación exterior). |
| 9 | 🔵 SEB | El Cuadripotencial y la Definición del Tensor de Faraday | arreglar/mejorar este footnote (el del espacio cotangente). |
| 10 | 🔵 SEB | El Cuadripotencial y la Definición del Tensor de Faraday | revisar este apartado (redundancia de gauge) — pendiente de revisión de Sebas. |
| 11 | 🔵 SEB | El Cuadripotencial y la Definición del Tensor de Faraday | añadir un apéndice dedicado a la derivada exterior (definición, propiedades, $d^2=0$, relación con grad/rot/div). |
| 12 | 🔵 SEB | El Cuadripotencial y la Definición del Tensor de Faraday | llevar esta derivación (regla de Leibniz / desarrollo de $F=dA$) al anexo. |
| 13 | 🔵 SEB | El Cuadripotencial y la Definición del Tensor de Faraday | ¿esto es así tal cual? verificar la igualdad $d(dx^)=d^2x^=0$. |
| 14 | 🔵 SEB | Descomposición Relativa a un Observador | relacionar esta normalización del observador comóvil con el observador euleriano de la malla. |
| 15 | 🔵 SEB | Descomposición Relativa a un Observador | notación: valorar usar el símbolo de Hodge $$ para el dual a lo largo del documento. |
| 16 | 🔵 SEB | Descomposición Relativa a un Observador | ¿“covariantemente” es el término correcto aquí? revisar. |
| 17 | 🔵 SEB | Descomposición Relativa a un Observador | revisar la estructura y jerarquía del documento: capítulos, secciones, subsecciones, subsubsecciones y niveles siguientes (consistencia y profundidad). |
| 18 | 🔵 SEB | El par inhomogéneo y el acoplamiento con la fuente | verificar si esto es resultado de un lagrangiano; incluir el resultado y el procedimiento, o llevarlo a un anexo. |
| 19 | 🔵 SEB | Derivación a partir de las Densidades Lagrangianas | ¿por qué $S_ em$ no incluye la fuente material ($J_ A^$)? explicarlo; y en un anexo mostrar dónde aparece la energía del campo electromagnético. |
| 20 | 🔵 SEB | Derivación a partir de las Densidades Lagrangianas | (general) revisar el uso de los términos “tensor” y “forma” a lo largo del capítulo, según el tratamiento de Vargas. |
| 21 | 🔵 SEB | Derivación a partir de las Densidades Lagrangianas | añadir en el anexo la derivación paso a paso de $T^_ em$ (derivada funcional de Hilbert). |
| 22 | 🔵 SEB | Derivación a partir de las Densidades Lagrangianas | verificar si la acción del fluido perfecto $S_ fluid= p-g\,d^4x$ es efectivamente válida en RRMHD (¿se modifica por la parte resistiva?). |
| 23 | 🔵 SEB | Dinámica Acoplada y el Sistema Completo de RRMHD | hacer explícita la derivación con $T^_ tot$ y separarla; añadir un anexo completo con el paso de (2.30) a (2.31). |
| 24 | 🔵 SEB | Dinámica Acoplada y el Sistema Completo de RRMHD | se nombra “RRMHD” pero aún no se ha introducido la resistividad/ley de Ohm (§(ref)); reordenar o aclarar para no adelantar el término. |
| 25 | 🔵 SEB | Dinámica Acoplada y el Sistema Completo de RRMHD | revisar este sistema de ecuaciones (2.32)--(2.35) y las relaciones entre ellas. |
| 26 | 🔵 SEB | El Sistema Aumentado de Maxwell | añadir una nota al pie explicando el acrónimo/método GLM (Generalized Lagrange Multipliers). |
| 27 | 🔵 SEB | Extensión Lagrangiana y el Campo Auxiliar Eléctrico $$ | explicar la diferencia y la justificación de esta acción extendida frente a la acción $S_ em$ original. |
| 28 | 🔵 SEB | Extensión Lagrangiana y el Campo Auxiliar Eléctrico $$ | explicar la función e implicación física del campo $$, y explicar el tercer término de la acción ($12_^$). |
| 29 | 🔵 SEB | Extensión Lagrangiana y el Campo Auxiliar Eléctrico $$ | ¿esta es la ecuación del telégrafo? aclarar: aquí es de onda pura; la forma telegráfica aparece luego con el amortiguamiento $$. |
| 30 | 🔵 SEB | Simetría Dual y el Campo Auxiliar Magnético $$ | añadir nota al pie aclarando que la formulación con potencial dual violaría esta invariancia/simetría de Hodge. |
| 31 | 🔵 SEB | Simetría Dual y el Campo Auxiliar Magnético $$ | ¿hay forma de introducir estos términos de amortiguamiento de manera formal (derivada) y no ad-hoc? |
| 32 | 🔵 SEB | La Ecuación del Telégrafo: Origen Covariante y Causalidad Disipativa | revisar y añadir cita(s) de respaldo. |
| 33 | 🔵 SEB | Descomposición 3+1 del Sistema Aumentado | añadir un anexo con los procedimientos/derivaciones de las ecuaciones (2.40)--(2.48). |
| 34 | 🔵 SEB | Descomposición de la Cuadricorriente y la Ley de Ohm Relativista | citar y revisar toda esta sección. |
| 35 | 🔵 SEB | Descomposición Ortogonal del Cuadrivector Corriente | añadir una figura que distinga $_e$ (propia, marco comóvil) de $_q$ (laboratorio), y en general el marco comóvil vs.\ el de laboratorio. |
| 36 | 🔵 SEB | Análisis de la KHI en el Límite Lineal | Expandir la explicaćion , implicaćion y justificaíon de lo que se dice ahí, es mas como justificar la aparicion de este tema en el marco teorico, entra un poco ortodoxo y seco |
| 37 | 🔵 SEB | Enstrofía de Perturbación y Extracción de $$ | En general, revisar todas las citas bien plantedas y utilizadas, y añadir en el marco teorico todas las herramientas estadisticas utilizadad, o discutir si deben de ser anexos , ya que son erramientas validas pero poco convencionales |

## Cap. 3 — KHI

| # | Tipo | Sección | Qué dice / acción |
|---|------|---------|-------------------|
| 38 | 🔵 SEB | Planteamiento Hidrodinámico | añadir una figura de la condición inicial / inestabilidad donde se distinga cada lámina de cizalla. |
| 39 | 🔵 SEB | Extensión Magnetohidrodinámica Ideal (MHD) | revisar consistencia con el montaje: aquí $B_0$ va alineado al flujo (caso clásico ilustrativo); en la simulación el campo es guía ($B_z$ dominante, componente paralela débil). |
| 40 | 🔴 REV | Correcciones Relativistas y Factor de Inercia | inconsistencia con el cap.~2, donde la inercia efectiva transversal se define como $w= h^2$ (sin el término magnético $B^2$). Unificar la definición entre capítulos. |
| 41 | 🔵 SEB | Correcciones Relativistas y Factor de Inercia | revisar la definición de $w$ contra la bibliografía (Bodo, Osmanov) y unificarla con el cap.~2. |
| 42 | 🔵 SEB | El Rol de la Resistividad y la Relajación Topológica | ¿se puede deducir una relación de dispersión como en MHD/clásica? — ver abajo: en RRMHD NO es posible de forma algebraica cerrada. |
| 43 | 🔵 SEB | Motivación Numérica y Relevancia Computacional | explicar a fondo (o en footnote) el esquema IMEX: advección explícita del fluido $+$ tratamiento implícito de las fuentes disipativas rígidas. |

## Cap. 4 — Métodos numéricos

| # | Tipo | Sección | Qué dice / acción |
|---|------|---------|-------------------|
| 44 | 🔵 SEB | (intro del capítulo) | añadir figuras para visualizar los volúmenes finitos, los flujos interfasiales y la discretización. |
| 45 | 🔵 SEB | Acoplamiento Numérico con el Sistema Aumentado GLM | el GLM ya se trató en el cap.~2; condensar esta introducción para no ser repetitivo ni redundante. |
| 46 | 🔵 SEB | Estructura Espectral de los Potenciales Auxiliares | ¿dónde se muestra esta diagonalización? ¿es pertinente incluirla explícitamente? |

## Cap. 5 — Setup experimental

| # | Tipo | Sección | Qué dice / acción |
|---|------|---------|-------------------|
| 47 | 🔵 SEB | Condiciones Iniciales del Problema | inconexo, necesita continuidad. |
| 48 | 🔵 SEB | Condiciones Iniciales del Problema | Aclarar que esta configuración del campo $B$ es solo para el objetivo~2 (campaña magnética); en esa comparación estas componentes serán nuestras variables. |
| 49 | 🔵 SEB | Dominio Computacional, Discretización y Sistema de Unidades | Mirar bien en el código las condiciones de frontera. |
| 50 | 🔵 SEB | Sistema de unidades y equivalencia temporal. | Dar un ejemplo concreto con escalas astrofísicas, deduciendo las dimensiones e incluso mostrando el radio de un vórtice generado en los hd plots. |
| 51 | 🔵 SEB | Exploración del Espacio de Parámetros: Resistividad | Falta poner el espacio de parámetros dictado por la campaña de campo magnético, en $=6000$ y $=10000$. |
| 52 | 🔵 SEB | Variables de Control y Diagnóstico | Mirar cuáles de estos diagnósticos sí se usan y cuáles no; además, seguro se usan otros, como campos y energías. |

## Cap. 6 — Resultados

| # | Tipo | Sección | Qué dice / acción |
|---|------|---------|-------------------|
| 53 | 🔵 SEB | (intro del capítulo) | Añadir toda la parte de la campaña de variación magnética: los $$ utilizados y los valores de CFL empleados en cada caso, y por qué. |
| 54 | 🔵 SEB | Resultados del ajuste | Expandir esto, ya que puede ser muy perjudicial. |
| 55 | 🔵 SEB | Validación estadística del modelo | Aclarar esto; suena muy a IA. |
| 56 | 🔵 SEB | Conductividad crítica $$ y sus tres fuentes de incertidumbre | Mostrar explícitamente todas las gráficas que sostienen este resultado; sí o sí deben salir. |
| 57 | 🔵 SEB | Conductividad crítica $$ y sus tres fuentes de incertidumbre | Se dejó a un lado todos los datos, análisis y construcción de la zona de transición. |
| 58 | 🔵 SEB | Leyes de potencia para $()$ | confuso; suena a IA. |
| 59 | 🔵 SEB | Leyes de potencia para $()$ | afirmación de cita: ¿es de la fuente o es interna? Revisar. |
| 60 | 🔵 SEB | Leyes de potencia para $()$ | ¿en qué se basa esta justificación? |
| 61 | 🔵 SEB | Leyes de potencia para $()$ | tasa de reconexión: ¿lo justifico? ¿se puede graficar y sustentar? |
| 62 | 🔵 SEB | Leyes de potencia para $()$ | ¿qué es Res-RMHD? |
| 63 | 🔵 SEB | Leyes de potencia para $()$ | revisar la validez y el argumento. |
| 64 | 🔵 SEB | Corrientes, disipación y energía magnética | Revisar esto: ¿qué? Rompe toda la fiabilidad; además, estos resultados justifican la zona de transición. |
| 65 | 🔵 SEB | Estructuras secundarias y anisotropía fuera del plano | Esto es increíble; revisar conexión y correlación. |
| 66 | 🔵 SEB | Contraste con la teoría lineal | ¿De dónde sale este valor? ¿Dónde está revisado? |
| 67 | 🔵 SEB | Techo hidrodinámico inviscido (ecuación de Rayleigh) | revisar la validez de las fuentes. |
| 68 | 🔵 SEB | El carácter dual del montaje no altera el techo | En la figura, no uses la expresión “tus datos”. |
| 69 | 🔵 SEB | Predicción RMHD compresible (Lees--Lin) | ¿cuál es mi dato en la figura? |
| 70 | 🔵 SEB | Velocidades características y números de Mach | buscar dónde poner el footnote de la velocidad de Alfvén. |
| 71 | 🔵 SEB | Velocidades características y números de Mach | expandir mejor la justificación. |
| 72 | 🔵 SEB | Contraste con los marcos MHD, RMHD y RRMHD | arreglar esto. |
| 73 | 🔵 SEB | Contraste con los marcos MHD, RMHD y RRMHD | ¿estamos seguros? |
| 74 | 🔵 SEB | Buen planteamiento y papel de la resistividad | Poner y organizar todo para la variación del campo magnético. |
| 75 | 🔴 REV | Buen planteamiento y papel de la resistividad | TONO (revisor): “prueba decisiva” suena tajante y no sabemos si lo será; considerar “una prueba más exhaustiva”. |
| 76 | 🔴 REV | Limitaciones del análisis y perspectivas | TONO (revisor): esta sección suena a IA y da por seguro que las pruebas futuras “arreglarían” las discrepancias; en realidad no se sabe. Reescribir en condicional/posibilidades (“podría”, “permitiría”) en vez de certezas, y revisar el uso de “prueba decisiva”/“máxima prioridad”. |
| 77 | 🔵 SEB | Limitaciones del análisis y perspectivas | límite numérico. |
| 78 | 🔵 SEB | Limitaciones del análisis y perspectivas | ¿ya existe? |
| 79 | 🔵 SEB | Limitaciones del análisis y perspectivas | esto lo estamos haciendo nosotros (campaña en curso). |
| 80 | 🔵 SEB | Limitaciones del análisis y perspectivas | ¿estamos más arriba del radio de sincrotrón, no? |
| 81 | 🔵 SEB | Limitaciones del análisis y perspectivas | No existe inestabilidad, o al menos no se generan tasas de crecimiento. Esto está mal. |
| 82 | 🔵 SEB | Limitaciones del análisis y perspectivas | variación y orientación, inminentes. |

## Cap. 7 — Conclusiones

| # | Tipo | Sección | Qué dice / acción |
|---|------|---------|-------------------|
| 83 | 🔵 SEB | (párrafo inicial) | + variación de campo magnético. |
| 84 | 🔵 SEB | (1) Efecto de la resistividad sobre la tasa de crecimiento lineal. | Ver cómo la correlación energética en $=6000$ y $=10000$, en compañía del campo magnético, habla del papel de la resistividad. |
| 85 | 🔵 SEB | (3) Efecto sobre las variables globales. | Se puede agregar un análisis igual al del campo magnético para ver la correlación de las variables energéticas y cómo esta cambia con $$. |
| 86 | 🔵 SEB | Trabajo Futuro | no es válido: ya no es “trabajo futuro”, la campaña está en curso. |

## Anexos

| # | Tipo | Sección | Qué dice / acción |
|---|------|---------|-------------------|
| 87 | 🔵 SEB | Justificación de $C+_0$: derivación paso a paso | Revisar y contrastar con la bibliografía, o directamente solo poner los resultados. |
| 88 | 🔴 REV | Veredicto: validez teórica del montaje | REVISAR (revisor): esta subsección repite la discusión de robustez/consistencia ya hecha (con más detalle) en el cap.\ de Resultados (§(ref)). Considerar recortarla a una síntesis breve específica del apéndice o eliminarla para no duplicar. |
