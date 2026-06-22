# Revisión de la monografía — tablero de avance

*Actualizado: 2026-06-22 · rama `revision-monografia`*

## 📊 Avance global: 14/122 cerradas (11%) — quedan 108

| Capítulo | Cerradas | Pendientes | Avance | Responsable |
|---|---|---|---|---|
| Preliminares | 0 | 1 | ░░░░░░░░░░ | — |
| Cap. 1 — Introducción | 0 | 4 | ░░░░░░░░░░ | Bryan |
| Cap. 2 — Teoría RRMHD | 14 | 32 | ███░░░░░░░ | Sebas+Claude |
| Cap. 3 — KHI | 0 | 10 | ░░░░░░░░░░ | Bryan |
| Cap. 4 — Métodos numéricos | 0 | 7 | ░░░░░░░░░░ | Bryan |
| Cap. 5 — Setup experimental | 0 | 9 | ░░░░░░░░░░ | Sebas+Claude |
| Cap. 6 — Resultados | 0 | 36 | ░░░░░░░░░░ | Sebas+Claude |
| Cap. 7 — Conclusiones | 0 | 6 | ░░░░░░░░░░ | al final |
| Anexos | 0 | 3 | ░░░░░░░░░░ | al final |

**Por tipo (pendientes):** 🔴 REV 5 · 🔵 SEB 73 · 🟠 CLAUDE 30 · 🟢 BRY 0

> Las notas cerradas desaparecen del documento (su `\sebnota`/`\claudenota` se elimina al resolverlas). El conteo de ``cerradas'' compara contra la línea base de anoche (commit `3656070`).


## Preliminares — pendientes

| # | Tipo | Sección | Qué dice / acción |
|---|------|---------|-------------------|
| 1 | 🔵 SEB | Resumen | no olvidar implementar la campaña de campo magnetico |

## Cap. 1 — Introducción — pendientes

| # | Tipo | Sección | Qué dice / acción |
|---|------|---------|-------------------|
| 2 | 🔵 SEB | Contexto de Plasmas Relativistas y Astrofísicos | agregar lo que haga falta de:enfatizar más en las aplicaciones en la astrofísica, por ejemplo: La inestabilidad de Kelvin–Helmholtz (KHI) aparece de manera natural en regiones donde dos flujos de plasma se desplazan con velocidades diferentes. En astrofísica, este tipo de inestabilidad es relevante en jets relativistas, vientos magnetizados, eyecciones compactas y zonas de interacción entre plasmas, donde puede favorecer la mezcla de materia, la formación de vórtices, la generación de estructuras secundarias y la reorganización del campo magnético. (esto hecho con ia, pero pueden humanizarlo o reescribirlo) |
| 3 | 🟠 CLAUDE | Contexto de Plasmas Relativistas y Astrofísicos | Se solapa con §1.3 (que ya lista jets/vientos/GRBs); mejor integrarlo allí, no aquí. Versión humanizada breve: “La KHI surge dondequiera que dos flujos de plasma se deslizan a velocidades distintas; en astrofísica, en los bordes de jets relativistas, vientos magnetizados y eyecciones compactas, donde favorece la mezcla, la formación de vórtices y la reorganización del campo magnético.” |
| 4 | 🔴 REV | Objetivos y Estructura de la Monografía | este objetivo (orientación/intensidad de B) NO se desarrolla en el cuerpo de esta versión; es la campaña pendiente (ver Conclusiones, objetivo 4). Alinear la redacción a “se sientan las bases para evaluar…” o presentarlo como trabajo futuro. |
| 5 | 🟠 CLAUDE | Objetivos y Estructura de la Monografía | Redacción propuesta: “… se sientan las bases para evaluar cómo las variaciones de dirección y magnitud del campo magnético externo modificarían la evolución de la inestabilidad; este objetivo se aborda como continuación inmediata (campaña en curso, cap.~(ref)).” |

## Cap. 2 — Teoría RRMHD — pendientes

| # | Tipo | Sección | Qué dice / acción |
|---|------|---------|-------------------|
| 6 | 🔵 SEB | (intro del capítulo) | ¿el observador euleriano va con el fluido? Aclarar la relación entre el observador euleriano (normal a las hipersuperficies) y el comóvil; en el espacio plano coinciden solo si el fluido está en reposo respecto a la malla. |
| 7 | 🔵 SEB | Electrodinámica Covariante y el Tensor de Campo Electromagnético | reescribir esta frase en términos más algebro-geométricamente correctos. |
| 8 | 🔵 SEB | El Cuadripotencial y la Definición del Tensor de Faraday | arreglar/mejorar este footnote (el del espacio cotangente). |
| 9 | 🔵 SEB | El Cuadripotencial y la Definición del Tensor de Faraday | revisar este apartado (redundancia de gauge) — pendiente de revisión de Sebas. |
| 10 | 🔵 SEB | El Cuadripotencial y la Definición del Tensor de Faraday | añadir un apéndice dedicado a la derivada exterior (definición, propiedades, $d^2=0$, relación con grad/rot/div). |
| 11 | 🔵 SEB | El Cuadripotencial y la Definición del Tensor de Faraday | llevar esta derivación (regla de Leibniz / desarrollo de $F=dA$) al anexo. |
| 12 | 🔵 SEB | Descomposición Relativa a un Observador | relacionar esta normalización del observador comóvil con el observador euleriano de la malla. |
| 13 | 🔵 SEB | Descomposición Relativa a un Observador | notación: valorar usar el símbolo de Hodge $$ para el dual a lo largo del documento. |
| 14 | 🔵 SEB | Descomposición Relativa a un Observador | ¿“covariantemente” es el término correcto aquí? revisar. |
| 15 | 🔵 SEB | Descomposición Relativa a un Observador | revisar la estructura y jerarquía del documento: capítulos, secciones, subsecciones, subsubsecciones y niveles siguientes (consistencia y profundidad). |
| 16 | 🔵 SEB | El par inhomogéneo y el acoplamiento con la fuente | verificar si esto es resultado de un lagrangiano; incluir el resultado y el procedimiento, o llevarlo a un anexo. |
| 17 | 🔵 SEB | Derivación a partir de las Densidades Lagrangianas | (general) revisar el uso de los términos “tensor” y “forma” a lo largo del capítulo, según el tratamiento de Vargas. |
| 18 | 🔵 SEB | Derivación a partir de las Densidades Lagrangianas | añadir en el anexo la derivación paso a paso de $T^_ em$ (derivada funcional de Hilbert). |
| 19 | 🟠 CLAUDE | Derivación a partir de las Densidades Lagrangianas | Símbolo ambiguo: aquí $$ es densidad de energía (incluye masa en reposo, $ h=+p$), pero en §(ref) se usa $h=1++p/$ con $$ = energía interna específica. Unificar: $$ para densidad y $$ (o $e$) para la específica, como en el Anexo ($h=1+-1p/$). |
| 20 | 🔵 SEB | Dinámica Acoplada y el Sistema Completo de RRMHD | hacer explícita la derivación con $T^_ tot$ y separarla; añadir un anexo completo con el paso de (2.30) a (2.31). |
| 21 | 🔵 SEB | Dinámica Acoplada y el Sistema Completo de RRMHD | revisar este sistema de ecuaciones (2.32)--(2.35) y las relaciones entre ellas. |
| 22 | 🔵 SEB | Extensión Lagrangiana y el Campo Auxiliar Eléctrico $$ | explicar la diferencia y la justificación de esta acción extendida frente a la acción $S_ em$ original. |
| 23 | 🔵 SEB | Extensión Lagrangiana y el Campo Auxiliar Eléctrico $$ | explicar la función e implicación física del campo $$, y explicar el tercer término de la acción ($12_^$). |
| 24 | 🟠 CLAUDE | Extensión Lagrangiana y el Campo Auxiliar Eléctrico $$ | Confirmado: aquí es onda pura. Pero hay un salto de coherencia: la acción y las Ecs.~(ref)--(ref) dan un sistema de segundo orden (telégrafo), mientras que el sistema 3+1 que integra el código, Ecs.~(ref)--(ref), es de primer orden (forma de Dedner). No se muestra la reducción de uno a otro; conviene aclararlo o presentar directamente la forma de Dedner. |
| 25 | 🔵 SEB | Simetría Dual y el Campo Auxiliar Magnético $$ | ¿hay forma de introducir estos términos de amortiguamiento de manera formal (derivada) y no ad-hoc? |
| 26 | 🔵 SEB | La Ecuación del Telégrafo: Origen Covariante y Causalidad Disipativa | revisar y añadir cita(s) de respaldo. |
| 27 | 🔵 SEB | Descomposición 3+1 del Sistema Aumentado | añadir un anexo con los procedimientos/derivaciones de las ecuaciones (2.40)--(2.48). |
| 28 | 🟠 CLAUDE | Descomposición 3+1 del Sistema Aumentado | Inconsistencia de notación con el Anexo (Ec.~(ref)): aquí $$ limpia la ley de Gauss eléctrica y $$ la magnética; en el anexo se usan $$ (eléctrica) y $$ (magnética), con las letras intercambiadas. Unificar en todo el documento. |
| 29 | 🔵 SEB | Descomposición de la Cuadricorriente y la Ley de Ohm Relativista | citar y revisar toda esta sección. |
| 30 | 🔵 SEB | Descomposición Ortogonal del Cuadrivector Corriente | añadir una figura que distinga $_e$ (propia, marco comóvil) de $_q$ (laboratorio), y en general el marco comóvil vs.\ el de laboratorio. |
| 31 | 🟠 CLAUDE | Resumen del Sistema RRMHD en Forma Conservativa | Verificado contra el código Cueva (06\_conserved\_var.f95): convención TOTAL correcta; $$ lleva $ h^2$ (con masa en reposo, sin restar $D$). Consistente con el Anexo. Da por resuelta la antigua nota roja de variables conservadas. |
| 32 | 🟠 CLAUDE | Resumen del Sistema RRMHD en Forma Conservativa | En contexto relativista “invarianza de Galileo” es impreciso (el término de Powell se asocia a la invariancia galileana en MHD clásica). Aquí conviene hablar de consistencia Lorentz/entropía, o atribuirlo con cuidado a su origen clásico. |
| 33 | 🔵 SEB | Análisis de la KHI en el Límite Lineal | Expandir la explicaćion , implicaćion y justificaíon de lo que se dice ahí, es mas como justificar la aparicion de este tema en el marco teorico, entra un poco ortodoxo y seco |
| 34 | 🟠 CLAUDE | Análisis de la KHI en el Límite Lineal | Marco sugerido: enlazar con el cap.~3 (cierre §3.5): el $[ M]=0$ existe formalmente, pero en RRMHD no se reduce a una relación de dispersión algebraica cerrada (Ohm resistiva = parabólica). Decir que aquí se plantea el problema y que su forma cerrada solo existe en los límites ideal/RMHD (cap.~3) lo haría menos seco y más justificado. |
| 35 | 🟠 CLAUDE | Inercia Térmica Relativista y Anisotropía Magnética | Estilo: cuando los autores son el sujeto (“… demostraron”), va textcite (ya corregido aquí). Revisar otros “ parencite\…\ + verbo” en el capítulo. |
| 36 | 🟠 CLAUDE | Inercia Térmica Relativista y Anisotropía Magnética | Esta es la definición correcta y estándar ($w= h^2$). El cap.~3 (§3.4.1) escribe $w= h^2+B^2$: unificar a esta (quitar el $+B^2$ del cap.~3), como pide la nota roja de ese capítulo. |
| 37 | 🔵 SEB | Enstrofía de Perturbación y Extracción de $$ | En general, revisar todas las citas bien plantedas y utilizadas, y añadir en el marco teorico todas las herramientas estadisticas utilizadad, o discutir si deben de ser anexos , ya que son erramientas validas pero poco convencionales |

## Cap. 3 — KHI — pendientes

| # | Tipo | Sección | Qué dice / acción |
|---|------|---------|-------------------|
| 38 | 🔵 SEB | Planteamiento Hidrodinámico | añadir una figura de la condición inicial / inestabilidad donde se distinga cada lámina de cizalla. |
| 39 | 🔵 SEB | Extensión Magnetohidrodinámica Ideal (MHD) | revisar consistencia con el montaje: aquí $B_0$ va alineado al flujo (caso clásico ilustrativo); en la simulación el campo es guía ($B_z$ dominante, componente paralela débil). |
| 40 | 🟠 CLAUDE | Extensión Magnetohidrodinámica Ideal (MHD) | Observación correcta. Basta una frase: “este caso alineado es ilustrativo; el montaje numérico usa campo guía con $B_z$ dominante (cap.~5), de modo que $ k B0$ (presión, no tensión)”. |
| 41 | 🔴 REV | Correcciones Relativistas y Factor de Inercia | inconsistencia con el cap.~2, donde la inercia efectiva transversal se define como $w= h^2$ (sin el término magnético $B^2$). Unificar la definición entre capítulos. |
| 42 | 🔵 SEB | Correcciones Relativistas y Factor de Inercia | revisar la definición de $w$ contra la bibliografía (Bodo, Osmanov) y unificarla con el cap.~2. |
| 43 | 🟠 CLAUDE | Correcciones Relativistas y Factor de Inercia | Corrección recomendada: $w= h^2+B^2 w= h^2$ (como en cap.~2, ya verificado). El $+B^2$ no es inercia térmica transversal; la tensión magnética entra aparte por $( k B_0)^2$. Esto resuelve la nota roja. (Mismo $$ ambiguo que en cap.~2: $h=1++p/$ usa $$ específica.) |
| 44 | 🔵 SEB | El Rol de la Resistividad y la Relajación Topológica | ¿se puede deducir una relación de dispersión como en MHD/clásica? — ver abajo: en RRMHD NO es posible de forma algebraica cerrada. |
| 45 | 🟠 CLAUDE | El Rol de la Resistividad y la Relajación Topológica | Esta pregunta ya queda respondida por el cierre de §3.5 (párrafo nuevo sobre por qué en RRMHD no hay dispersión algebraica cerrada). Sugerencia: dejar esta nota como puntero a ese párrafo o borrarla para no duplicar. |
| 46 | 🔵 SEB | Motivación Numérica y Relevancia Computacional | explicar a fondo (o en footnote) el esquema IMEX: advección explícita del fluido $+$ tratamiento implícito de las fuentes disipativas rígidas. |
| 47 | 🟠 CLAUDE | Motivación Numérica y Relevancia Computacional | Footnote IMEX propuesta: “IMEX-RK (Implicit--Explicit Runge--Kutta): integra de forma explícita los flujos advectivos no rígidos e implícita las fuentes resistivas rígidas ($$), evitando el paso de tiempo $ t^-1$ que impondría un esquema totalmente explícito a alta conductividad.” Coherente con la implementación del Cueva (Pareschi--Russo + Aloy--Cordero). |

## Cap. 4 — Métodos numéricos — pendientes

| # | Tipo | Sección | Qué dice / acción |
|---|------|---------|-------------------|
| 48 | 🔵 SEB | (intro del capítulo) | añadir figuras para visualizar los volúmenes finitos, los flujos interfasiales y la discretización. |
| 49 | 🟠 CLAUDE | (intro del capítulo) | No bloquea la entrega: una sola figura esquemática (celda $i$, interfaces $i1/2$, stencil de 5 puntos de MP5) basta. Si falta tiempo, puede omitirse sin perder rigor. |
| 50 | 🔵 SEB | Acoplamiento Numérico con el Sistema Aumentado GLM | el GLM ya se trató en el cap.~2; condensar esta introducción para no ser repetitivo ni redundante. |
| 51 | 🟠 CLAUDE | Acoplamiento Numérico con el Sistema Aumentado GLM | De acuerdo: reducir a 1--2 frases con ref a §(ref). Aquí basta decir “se implementa la limpieza GLM ya derivada (§ref), con velocidad de limpieza $c_h=1$”. |
| 52 | 🔵 SEB | Estructura Espectral de los Potenciales Auxiliares | ¿dónde se muestra esta diagonalización? ¿es pertinente incluirla explícitamente? |
| 53 | 🟠 CLAUDE | Estructura Espectral de los Potenciales Auxiliares | No es esencial en el cuerpo: basta afirmar que las submatrices $22$ tienen autovalores $ c_h$ (de ahí la propagación causal). Si se quiere el detalle, llevarlo al anexo. Conecta con la nota de cap.~2 sobre derivar el 2$$2 desde el sistema 3+1. |
| 54 | 🟠 CLAUDE | Recuperación de Variables Primitivas: la Cuártica del Factor de Lorentz | Verificado contra el código (12\_varprimitive.f95, subrutina varprimitivecardano): cuártica en $$ + Tchirnhaus + refinamiento Newton, correcto. Cita: el esquema de recuperación es del Cueva; citar miranda-aranguren-2018 aquí (mizuno-2013 es el paper de EoS, no de recuperación de primitivas). |

## Cap. 5 — Setup experimental — pendientes

| # | Tipo | Sección | Qué dice / acción |
|---|------|---------|-------------------|
| 55 | 🔵 SEB | Condiciones Iniciales del Problema | inconexo, necesita continuidad. |
| 56 | 🔵 SEB | Condiciones Iniciales del Problema | Aclarar que esta configuración del campo $B$ es solo para el objetivo~2 (campaña magnética); en esa comparación estas componentes serán nuestras variables. |
| 57 | 🔵 SEB | Dominio Computacional, Discretización y Sistema de Unidades | Mirar bien en el código las condiciones de frontera. |
| 58 | 🟠 CLAUDE | Dominio Computacional, Discretización y Sistema de Unidades | Según el propio §(ref) y el código: periódicas en $y$ y abiertas (derivada normal nula / flujo libre) en $x$. Confirmar el flag exacto en parameters.f95; la descripción del texto es consistente. |
| 59 | 🔵 SEB | Sistema de unidades y equivalencia temporal. | Dar un ejemplo concreto con escalas astrofísicas, deduciendo las dimensiones e incluso mostrando el radio de un vórtice generado en los hd plots. |
| 60 | 🔵 SEB | Exploración del Espacio de Parámetros: Resistividad | Falta poner el espacio de parámetros dictado por la campaña de campo magnético, en $=6000$ y $=10000$. |
| 61 | 🟠 CLAUDE | Exploración del Espacio de Parámetros: Resistividad | Pendiente de los datos de la campaña (martes). Marcador: al llegar, tabular los $$ usados (6000, 10000), las orientaciones/intensidades de $ B$ y el CFL de cada corrida. |
| 62 | 🔵 SEB | Variables de Control y Diagnóstico | Mirar cuáles de estos diagnósticos sí se usan y cuáles no; además, seguro se usan otros, como campos y energías. |
| 63 | 🟠 CLAUDE | Variables de Control y Diagnóstico | Del código: se usan $_z$, $_ tot$, $f_Vz$ y $'_zp$ (estos en cap.~6) y además $J_$, $ E\!\! J$ y $E_ mag$ (§(ref)). Conviene listar también estos últimos aquí para que la sección de diagnósticos quede completa. |

## Cap. 6 — Resultados — pendientes

| # | Tipo | Sección | Qué dice / acción |
|---|------|---------|-------------------|
| 64 | 🔵 SEB | (intro del capítulo) | Añadir toda la parte de la campaña de variación magnética: los $$ utilizados y los valores de CFL empleados en cada caso, y por qué. |
| 65 | 🔵 SEB | Resultados del ajuste | Expandir esto, ya que puede ser muy perjudicial. |
| 66 | 🔵 SEB | Validación estadística del modelo | Aclarar esto; suena muy a IA. |
| 67 | 🔵 SEB | Conductividad crítica $$ y sus tres fuentes de incertidumbre | Mostrar explícitamente todas las gráficas que sostienen este resultado; sí o sí deben salir. |
| 68 | 🔵 SEB | Conductividad crítica $$ y sus tres fuentes de incertidumbre | Se dejó a un lado todos los datos, análisis y construcción de la zona de transición. |
| 69 | 🔵 SEB | Leyes de potencia para $()$ | confuso; suena a IA. |
| 70 | 🔵 SEB | Leyes de potencia para $()$ | afirmación de cita: ¿es de la fuente o es interna? Revisar. |
| 71 | 🔵 SEB | Leyes de potencia para $()$ | ¿en qué se basa esta justificación? |
| 72 | 🔵 SEB | Leyes de potencia para $()$ | tasa de reconexión: ¿lo justifico? ¿se puede graficar y sustentar? |
| 73 | 🔵 SEB | Leyes de potencia para $()$ | ¿qué es Res-RMHD? |
| 74 | 🟠 CLAUDE | Leyes de potencia para $()$ | Res-RMHD = Resistive Relativistic MHD (el marco de todo el trabajo); aquí alude a esquemas numéricos de alto orden para Res-RMHD (mignone2024). Conviene definir la sigla en su primer uso o usar “RRMHD” para no introducir una variante. |
| 75 | 🔵 SEB | Leyes de potencia para $()$ | revisar la validez y el argumento. |
| 76 | 🔵 SEB | Corrientes, disipación y energía magnética | Revisar esto: ¿qué? Rompe toda la fiabilidad; además, estos resultados justifican la zona de transición. |
| 77 | 🔵 SEB | Estructuras secundarias y anisotropía fuera del plano | Esto es increíble; revisar conexión y correlación. |
| 78 | 🔵 SEB | Contraste con la teoría lineal | ¿De dónde sale este valor? ¿Dónde está revisado? |
| 79 | 🟠 CLAUDE | Contraste con la teoría lineal | $=(C+_0)\,a_kh/v_sh=1.030.05/0.5=0.103$. La cadena completa (Michalke $$ Lees--Lin $$ medido) está recomputada y verificada en el Anexo~(ref); conviene citar ese anexo aquí. |
| 80 | 🔵 SEB | Techo hidrodinámico inviscido (ecuación de Rayleigh) | revisar la validez de las fuentes. |
| 81 | 🔵 SEB | El carácter dual del montaje no altera el techo | En la figura, no uses la expresión “tus datos”. |
| 82 | 🔵 SEB | Predicción RMHD compresible (Lees--Lin) | ¿cuál es mi dato en la figura? |
| 83 | 🔵 SEB | Velocidades características y números de Mach | buscar dónde poner el footnote de la velocidad de Alfvén. |
| 84 | 🟠 CLAUDE | Velocidades características y números de Mach | Ubicación natural: primera aparición de $V_A$ en la tabla de Mach (§6.7.4). Footnote: “$V_A=B^2/( h+B^2)$ (con $c=1$): velocidad de Alfvén relativista.” Ya hay un footnote de $V_A$ en el cap.~1; podría bastar un ref a él. |
| 85 | 🔵 SEB | Velocidades características y números de Mach | expandir mejor la justificación. |
| 86 | 🔵 SEB | Contraste con los marcos MHD, RMHD y RRMHD | arreglar esto. |
| 87 | 🔵 SEB | Contraste con los marcos MHD, RMHD y RRMHD | ¿estamos seguros? |
| 88 | 🔵 SEB | Buen planteamiento y papel de la resistividad | Poner y organizar todo para la variación del campo magnético. |
| 89 | 🔴 REV | Buen planteamiento y papel de la resistividad | TONO (revisor): “prueba decisiva” suena tajante y no sabemos si lo será; considerar “una prueba más exhaustiva”. |
| 90 | 🔴 REV | Limitaciones del análisis y perspectivas | TONO (revisor): esta sección suena a IA y da por seguro que las pruebas futuras “arreglarían” las discrepancias; en realidad no se sabe. Reescribir en condicional/posibilidades (“podría”, “permitiría”) en vez de certezas, y revisar el uso de “prueba decisiva”/“máxima prioridad”. |
| 91 | 🔵 SEB | Limitaciones del análisis y perspectivas | límite numérico. |
| 92 | 🔵 SEB | Limitaciones del análisis y perspectivas | ¿ya existe? |
| 93 | 🟠 CLAUDE | Limitaciones del análisis y perspectivas | Sí existe: chow2023 da el análisis lineal RMHD magnetizado (el polinomio de alto grado); ya está citado y subido al NotebookLM. La sustitución $c_s v_f$ es la aproximación que aquí se usa en vez de resolver ese polinomio completo. |
| 94 | 🔵 SEB | Limitaciones del análisis y perspectivas | esto lo estamos haciendo nosotros (campaña en curso). |
| 95 | 🔵 SEB | Limitaciones del análisis y perspectivas | ¿estamos más arriba del radio de sincrotrón, no? |
| 96 | 🟠 CLAUDE | Limitaciones del análisis y perspectivas | El Cueva es un código de fluido (RRMHD), sin escala cinética/giroradio: no hay “radio de sincrotrón” resuelto. La escala micro relevante es la capa resistiva $ S^-1/2$. Si la duda es por Hall/anisotropía, eso sí queda fuera del modelo escalar de $$ (ya anotado en limitaciones). |
| 97 | 🔵 SEB | Limitaciones del análisis y perspectivas | No existe inestabilidad, o al menos no se generan tasas de crecimiento. Esto está mal. |
| 98 | 🟠 CLAUDE | Limitaciones del análisis y perspectivas | De acuerdo: a $500$ el problema no es “ajuste pobre” sino que la disipación domina desde $t=0$ y no hay fase lineal limpia $$ no se puede extraer una $$ fiable. Reformular así (no “$R^2<0.7$” a secas). |
| 99 | 🔵 SEB | Limitaciones del análisis y perspectivas | variación y orientación, inminentes. |

## Cap. 7 — Conclusiones — pendientes

| # | Tipo | Sección | Qué dice / acción |
|---|------|---------|-------------------|
| 100 | 🔵 SEB | (párrafo inicial) | + variación de campo magnético. |
| 101 | 🟠 CLAUDE | (párrafo inicial) | Sí: al llegar los datos, añadir un párrafo/objetivo con la conclusión de la campaña de B (intensidad/orientación). Hasta entonces el objetivo 4 se lee como “en curso”. |
| 102 | 🔵 SEB | (1) Efecto de la resistividad sobre la tasa de crecimiento lineal. | Ver cómo la correlación energética en $=6000$ y $=10000$, en compañía del campo magnético, habla del papel de la resistividad. |
| 103 | 🔵 SEB | (3) Efecto sobre las variables globales. | Se puede agregar un análisis igual al del campo magnético para ver la correlación de las variables energéticas y cómo esta cambia con $$. |
| 104 | 🔵 SEB | Trabajo Futuro | no es válido: ya no es “trabajo futuro”, la campaña está en curso. |
| 105 | 🟠 CLAUDE | Trabajo Futuro | Correcto: mover “Campaña de campo magnético” de Trabajo Futuro a Resultados/Conclusiones una vez integrada (martes). Si para la entrega aún no está, dejarla como “en curso”, no como futuro. |

## Anexos — pendientes

| # | Tipo | Sección | Qué dice / acción |
|---|------|---------|-------------------|
| 106 | 🔵 SEB | Justificación de $C+_0$: derivación paso a paso | Revisar y contrastar con la bibliografía, o directamente solo poner los resultados. |
| 107 | 🟠 CLAUDE | Justificación de $C+_0$: derivación paso a paso | El anexo ya recomputa todo de forma independiente y coincide con el cuerpo; las fuentes (Michalke, Landau, Bodo, Chow) están verificadas. Decisión: dejarlo como auditoría (valor añadido) o condensarlo a la tabla-síntesis. La nota roja del “Veredicto” (duplicado con §6.7) apunta a recortar esa subsección, no la auditoría numérica. |
| 108 | 🔴 REV | Veredicto: validez teórica del montaje | REVISAR (revisor): esta subsección repite la discusión de robustez/consistencia ya hecha (con más detalle) en el cap.\ de Resultados (§(ref)). Considerar recortarla a una síntesis breve específica del apéndice o eliminarla para no duplicar. |
