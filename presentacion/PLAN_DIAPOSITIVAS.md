# Plan de diapositivas — Sustentación (30 min)

**Tratamiento numérico de la KHI bajo el marco de la RRMHD**
Bryan Martinez · Sebastián Rodriguez — Director: Sergio Miranda-Aranguren
Jurado: Juan Carlos Giraldo Acuña (perfil: formalismo tensorial/QFT + epistemología + validación física; ver `jurado.md`)

Plantilla: Beamer 16:9 de `~/Downloads/New Project(5)/main.tex` (paleta Inferno, tema Madrid, cajas EQ/RES/HYP/WRN). Se reutiliza el preámbulo íntegro.

---

## Presupuesto de tiempo (30 min)

| Bloque | Slides | Tiempo | % |
|---|---|---|---|
| 0. Portada + hoja de ruta | 2 | 1.5 min | 5% |
| 1. Motivación y fenomenología | 3 | 3 min | 10% |
| 2. Marco teórico RRMHD | 6 | 6.5 min | 22% |
| 3. Implementación numérica + setup | 6 | 7 min | 23% |
| 4. Resultados | 8 | 9 min | 30% |
| 5. Conclusiones y perspectivas | 2 | 2.5 min | 8% |
| Cierre | 1 | 0.5 min | 2% |
| **Total cuerpo** | **28 frames** | **30 min** | |
| Backup (no se presentan) | ~12 | — | |

Regla de ritmo: ~65 s/slide de contenido; las de resultados con figura grande pueden ir a 75–90 s compensando con slides visuales rápidas.

**Ajustes vs. la propuesta de Gemini** (mantengo su esqueleto, con 3 correcciones):
1. Teoría sube de 20%→22% y numérica baja de 30%→23%: el jurado es teórico-epistemológico, no de HPC; el blindaje fuerte va en covariancia + honestidad numérica, no en detalles de implementación.
2. ⚠️ Gemini pide justificar "la inversión del perfil de densidad para gatillar la inestabilidad" — **eso no describe nuestro setup**: la semilla es la perturbación senoidal en V_x (Ec. de la monografía `eq:Vx_pert`); el contraste de densidad (η_ρ=0.1) modela chorro diluido/ambiente denso, no gatilla nada. La slide del setup lo dice explícitamente.
3. ⚠️ El informe Gemini del jurado asume tesis en C++/CUDA/HLLC. Cueva es **Fortran, CPU, HLL+MP5**. Nada de CUDA en el cuerpo; en backup va la slide "¿por qué HLL y no HLLC?" que es la pregunta real que puede caer.

---

## BLOQUE 0 — Apertura (2 slides, 1.5 min)

### S1 — Portada `[plain]`
- Fondo `khi_simulation_bg.png`, logo UD, título completo, autores, director, jurado, fecha.
- Verbal (30 s): una frase-tesis: *"Cuantificamos cómo la resistividad finita y la geometría del campo magnético gobiernan la inestabilidad de Kelvin–Helmholtz relativista, con 60+ simulaciones del código Cueva."*

### S2 — Hoja de ruta
- Los 5 bloques + los **4 objetivos específicos** de la propuesta en una columna (los resultados se presentarán "por objetivo", igual que las conclusiones de la monografía).
- 🛡️ (Vector 4 — estructura argumentativa): el jurado ve desde el minuto 1 que la narrativa es objetivo→método→resultado→conclusión.

---

## BLOQUE 1 — Motivación y fenomenología (3 slides, 3 min)

### S3 — El fenómeno: KHI sin ecuaciones
- Figura: `monografia/figuras/contexto_jet` (frontera de jet AGN) + un frame de vórtice enrollado (collage ρ).
- Contenido: explicación **puramente física** en 60 s: cizalla → Bernoulli → torque sobre la interfaz → crecimiento exponencial → vórtices. Mezcla, entrainment, dicotomía FRI/FRII, aceleración de partículas.
- 🛡️ (Vector 3, pregunta pedagógica "explíquela sin fórmulas"): esta slide ES la respuesta ensayada.

### S4 — Por qué resistiva: los límites del congelamiento
- Idea central: RMHD ideal (σ→∞) congela topología (teorema de Alfvén) → prohíbe reconexión; cuando ocurre en códigos ideales es **resistividad numérica** (error de truncamiento, incontrolado). RRMHD la vuelve física, predictiva y controlada (η=1/σ).
- Mini-esquema: current sheet + reconexión. Mencionar llamaradas AGN/GRB/magnetares.
- 🛡️ Anticipa la pregunta "¿su disipación es física o numérica?" — se planta la respuesta desde la motivación.

### S5 — Objetivos y diseño del experimento
- Los 4 objetivos: (1) γ_KHI(σ), (2) estructuras secundarias, (3) variables globales EM, (4) intensidad/orientación de B.
- Diagrama: dos campañas — barrido σ (44 sims, obj. 1–3) y campaña magnética A/B/C a σ={6000, 10000} (obj. 4).

---

## BLOQUE 2 — Marco teórico RRMHD (6 slides, 6.5 min)

> Registro doble: ecuación impecable en pantalla + traducción física verbal en una frase por término. Declarar **signatura (−,+,+,+) y unidades Heaviside–Lorentz (c=μ₀=ε₀=1) UNA VEZ aquí** y no volver a tocarlas (gotcha clásico de jurado formado en QFT).

### S6 — Estructura covariante del sistema
- Caja EQ con las 4 leyes: ∂_μ(ρu^μ)=0, ∂_μT^{μν}=0, ∂_μF^{μν}=J^ν, ∂_μ(⋆F)^{μν}=0.
- T^{μν} = T^{μν}_fluid + T^{μν}_em explícito (fluido perfecto + Faraday–Maxwell), origen variacional (Hilbert) mencionado en una línea, derivación completa → backup.
- Punto fino verbal: F=dA ⟹ dF=0 **identidad geométrica** (Bianchi), no ecuación dinámica; las inhomogéneas sí son dinámica.
- 🛡️ (Vector 1, "la prueba del físico"): es la slide que el informe pide "innegociable".

### S7 — Ley de Ohm relativista: el cierre resistivo
- Cadena: J^μ = ρ_e u^μ + σF^{μν}u_ν (covariante, comóvil) → proyección 3+1 → **J = ρ_q v + σW[E + v×B − (E·v)v]**.
- Los dos límites en caja: σ→∞ ⟹ E+v×B=0 (ideal, congelamiento); 0<σ<∞ ⟹ E comóvil sobrevive ⟹ calentamiento Joule + reconexión.
- Honestidad explícita: σ **escalar**, isótropa, sin Hall (plasma colisional macroscópico) — límite de validez declarado aquí, no escondido.
- 🛡️ (Vector epistemológico sobre origen de η): "η es un coeficiente de transporte fenomenológico que emerge de las integrales de colisión del nivel cinético (Vlasov–Boltzmann); el cierre escalar exige ν_col ≫ ω_ciclotrón" — tener esta frase ensayada.

### S8 — El problema de ∇·B y el sistema GLM aumentado
- Planteo: en el continuo dF=0 garantiza ∇·B=0 (d²=0); **la malla discreta rompe la nilpotencia (d²≠0)** → monopolos espurios que se acumulan.
- Solución GLM: dos escalares Φ, Ψ vía acción extendida (multiplicadores de Lagrange generalizados) → el error obedece la **ecuación del telégrafo**: propaga a c_h y decae ∝e^{−κt/2}. Causalidad intacta.
- Figura: `figuras/glm_limpieza` (acumulación vs. propagación+amortiguamiento).
- 🛡️ (Vector 1, pregunta predicha textualmente: "¿cómo garantiza ∇·B sin destruir la causalidad?"): respuesta completa en pantalla. Monitoreo numérico del error → backup.

### S9 — Sistema conservativo final: 14 variables
- U = (D, S^j, τ, B^j, E^j, ρ_q, Ψ, Φ)ᵀ con las definiciones **totales** (S^j y τ incluyen Poynting y ½(E²+B²)) — consecuencia directa de ∂_μT^{μν}_total=0: la fuerza de Lorentz NO es término fuente, está en la divergencia del flujo.
- Fuente S(U): solo −J^j (Ohm), sumideros telegráficos y términos de Godunov–Powell (rigor termodinámico frente a monopolos transitorios).
- 🛡️ Jacobiano 14×14, 8 autovalores degenerados a ±c → mencionar en una frase, espectro completo en backup (fue nota del director; el jurado QFT puede contar variables).

### S10 — Mapa de límites (slide-puente)
- Diagrama de flechas: **RRMHD → (σ→∞) RMHD ideal → (v≪c) MHD clásica → (B→0) Navier–Stokes/Euler → Maxwell en vacío (σ→0)**.
- Al lado, la misma escalera para la KHI: clásica (incondicionalmente inestable, ec. cuadrática) → MHD (tensión estabiliza si (k·B)² suficiente) → RMHD (inercia ρhW², criterio 0<M_re<√2 de Königl/Bodo) → RRMHD (**no existe relación de dispersión algebraica cerrada**: el término η∇²B es parabólico y suaviza la discontinuidad ⟹ la tasa se caracteriza numéricamente).
- 🛡️ (Vector 2 completo, neutralizado preventivamente — el informe Claude la recomienda textualmente). Además, esta slide **justifica epistemológicamente la tesis**: como no hay fórmula cerrada, medir γ(σ) numéricamente es el único camino.

### S11 — Observable: vorticidad y enstrofía de perturbación
- ω'_z = ω_z − ⟨ω_z(t=0)⟩_y ; Ω'_zp = ∫(ω'_z)²dA ; en fase lineal ln Ω'_zp = a + **2**γ_KHI·t (el factor 2 explicado: la enstrofía es cuadrática en la amplitud).
- Figura pequeña: esquema de sustracción del fondo de cizalla (`enstrophy_schematic.png` de la plantilla o regenerar).
- Diagnósticos complementarios listados: Ω_tot, f_Vz, J_max, ∫E·J dA, E_mag.
- 🛡️ Define el estimador ANTES de mostrar resultados: nada de números sin origen (alergia declarada del jurado a "dejar términos a adivinar").

---

## BLOQUE 3 — Implementación numérica y setup (6 slides, 7 min)

### S12 — Volúmenes finitos: por qué FVM y no otra cosa
- Forma integral ⟹ conservación exacta por construcción (el flujo que sale de una celda entra a la vecina); en flujos relativistas emergen **choques** que vuelven singular la forma diferencial ⟹ la formulación integral es matemáticamente obligatoria (condiciones de Rankine–Hugoniot respetadas por el flujo numérico).
- Figura: `figuras/volumenes_finitos.pdf` o `figuras/celda_3d_flujos`.
- 🛡️ (Choque de paradigmas FEM vs FVM del informe Gemini): frase preparada — "FEM (formulación débil) es óptimo para dominios complejos con soluciones suaves; para leyes de conservación hiperbólicas con discontinuidades, la captura de choques exige la forma integral conservativa".

### S13 — Reconstrucción MP5 + solucionador HLL: control de la difusión numérica
- Teorema de Godunov → limitadores; TVD 2.º orden recorta extremos y mata la enstrofía; **MP5** (Suresh–Huynh): 5.º orden + mediana proyectiva, retención casi espectral de vorticidad.
- HLL: robusto, libre de jacobianos, positivo; su difusión sobre la onda de contacto la **compensa la agudeza de los estados MP5** (hallazgo del propio Miranda-Aranguren+2018). Criterio de diseño: **disipación numérica < disipación física η** en todo el barrido.
- 🛡️ (Vector 2 Gemini, "¿su vórtice es física o viscosidad artificial?"): respuesta en dos niveles — aquí el argumento de diseño; la **evidencia empírica** llega en S24 (plateau de J_max). Pregunta "¿por qué no HLLC si el paper del código es HLLC?" → backup B7.

### S14 — Rigidez e IMEX-RK
- El problema: τ_relax ~ 1/σ ≪ Δt_CFL; explícito puro ⟹ Δt ∝ Δx²/σ (parálisis).
- La solución: partición IMEX-RK (SSP, Pareschi–Russo): flujos hiperbólicos explícitos (MP5+HLL), fuente rígida −σE **implícita**; la inversión es **algebraica local 3×3 con solución analítica** (cero acoplamiento intercelular, sin Newton global).
- Caja RES: **preservación asintótica** — al dividir por ασW y tomar σ→∞ la actualización implícita converge exactamente a E = −v×B (Ohm ideal). El esquema respeta el límite físico por construcción.
- Figura: `figuras/imex_splitting`.
- 🛡️ (Vector 3 Gemini sobre coste de inversión implícita): la inversión no es matricial iterativa, es analítica → el "sobrecosto" es despreciable frente al salto de Δt.

### S15 — Recuperación de primitivas: cuártica de Ferrari–Cardano
- U(P) no tiene inversa cerrada (W acopla cinemática y termodinámica). Cueva lo reduce a **una cuártica en W** resuelta analíticamente (Tschirnhaus → cuártica reducida → Ferrari–Cardano) + refinamiento Newton; guardias físicas: v²<1, p>0.
- 🛡️ (pregunta predicha sobre "robustez de la recuperación frente a presiones negativas/superlumínicas"): la respuesta exacta está en pantalla. Además desactiva la crítica "caja negra": sabemos qué polinomio resuelve el código y por qué.

### S16 — Setup: doble capa de cizalla tipo Mizuno (Test 35A)
- Figura: `figuras/velocidad_inicial.pdf` + `figuras/rho_inicial.pdf`.
- Perfiles V_y(x) (tanh dobles en x=±0.5, v_sh=0.5c), **semilla: perturbación senoidal V_x** confinada gaussiana (modo fundamental k=2π/L_y) — ⚠️ corregir aquí el guion de Gemini: la densidad no gatilla nada; η_ρ=0.1 modela chorro diluido en ambiente denso.
- B=(0, √0.02, √2.0): campo **guía** B_z dominante (presión, no tensión: k·B∝B_y débil) — decisión topológica que PERMITE que la KHI se desarrolle y aísla el efecto resistivo.
- BCs: periódicas en y (compatibles con el modo), abiertas en x. Malla 512×256 (≈13 celdas por capa). Γ=4/3. CFL=0.1 (0.04/0.02 campaña B).
- Equivalencia astrofísica (una línea): L₀=10¹⁶ cm ⟹ τ_c≈3.8 días; t=5 ≈ 19 días de un jet de AGN; vórtice maduro ≈ 170 UA.

### S17 — Las dos campañas y su matriz de parámetros
- Campaña 1: σ ∈ {100…10500}, 44 valores, todo lo demás fijo → aísla η=1/σ.
- Campaña 2 (B fija σ): A (intensidad B₀=1,1.5,2 — los casos débiles 0.25/0.5 fallaron numéricamente y se excluyen, transparencia), B (rotación y–z: tensión ∝B_y), C (rotación x–z: k·B=0, sin tensión), a σ=6000 (CFL 0.04) y σ=10000 (CFL 0.02).
- 🛡️ Honestidad de datos excluidos declarada en pantalla (θ=15° divergió; B₀ débiles crashearon): madurez científica > cherry-picking.

---

## BLOQUE 4 — Resultados (8 slides, 9 min)

### S18 — Visión global del barrido: fenomenología
- Figura: `figuras/fig_conductividad_rho_collage.pdf` (ρ(x,y): 3 σ × 3 tiempos).
- Las tres fases (lineal → enrollamiento → saturación) y el contraste morfológico resistivo vs cuasi-ideal (reconexión fragmenta vs campo congelado + turbulencia fina).
- Verbal: cada régimen en una frase física.

### S19 — Extracción de γ_KHI
- Figura: `figuras/ln_omega_vs_t.pdf` (44 curvas, ventana [2.4, 3.4] sombreada).
- Pendiente = 2γ_KHI; criterio de calidad R² clasifica regímenes; el análisis cuantitativo usa las 35 sims con σ≥1600 (en el resistivo extremo NO hay fase lineal limpia — no es "ajuste pobre", es que la difusión domina desde t=0).
- 🛡️ (Vector 3: "¿cómo sabe que la solución es física?"): criterios de selección de datos explícitos y conservadores.

### S20 — Modelo sigmoide con offset: la transición resistivo→ideal
- Figura: `figuras/fig1_ajuste_v6.pdf`. Ecuación en caja: γ(σ) = C + γ₀/(1+e^{−k(σ−σ₀)}).
- Resultado: asíntota ideal **C+γ₀ = 1.03±0.05**; σ₀=2815±123.
- Validación en 3 líneas (sin ahogarse): ΔAIC=−126 anidado (mismo dataset, 1 parámetro extra), hold-out sobre los 9 puntos resistivos no usados (RMSE 0.039→0.025, −36%), residuos autocorrelacionados ⟹ el error formal subestima (por eso los múltiples estimadores de la siguiente slide). Detalle estadístico → backup.
- 🛡️ Se presenta C como parámetro del modelo con soporte predictivo fuera de muestra, NO como "tasa negativa física" (objeción anticipada por el director y NLM).

### S21 — σ_crit no es un número: es una zona de transición
- Figura: `figuras/fig_zona_transicion` (cascada de activación).
- Cada observable se idealiza a una σ distinta (σ₀=2815 lineal, 3400 amplitud, 6000 t_peak, 6800 aceleración) ⟹ **zona [1400, 7000]**, centro ≈2815; en Lundquist S~10³.
- Mensaje epistemológico explícito: la dispersión inter-método (±1944) es física multi-escala, no ruido; reportar la banda es lo riguroso.
- 🛡️ (Vector 4 + epistemología): esta slide muestra conciencia del significado de la incertidumbre — es de las que más conectan con el perfil del jurado.

### S22 — Contraste con la teoría lineal (resultado central)
- Figura: `figuras/fig6_escalera.pdf` (Michalke 0.190 → Lees–Lin compresible-magnetosónica 0.095 → medido 0.103) + opcional `fig9_compresible.pdf` pequeña.
- La cadena: techo hidrodinámico inviscido (validado contra Michalke 1964); geometría fija la velocidad de restitución (k⊥B ⟹ v_f⊥=0.691, Chow 2023: "presión pero no tensión"); predicción ω̂=0.095; medido ω̂=0.103 ⟹ **acuerdo al 8% sin parámetros de ajuste**. Control negativo: con c_s sola colapsaría a 0.016 — es la presión de B_z la que sostiene la inestabilidad.
- M_re = 0.60 < √2 (Königl/Bodo/Chow): holgadamente inestable, la extrapolación no roza el umbral.
- 🛡️ Frase de honestidad ensayada: "es una consistencia cuantitativa fuerte, no una validación cerrada: la asíntota es extrapolación (el dato máximo alcanza el 85%) y la predicción usa la sustitución escalar c_s→v_f⊥, no la dispersión RMHD de grado 8".

### S23 — No linealidad: ley de potencia de la enstrofía máxima
- Figura: `figuras/fig_omega_max_leypotencias.pdf`. Ω^max_zp ∝ σ^1.22 (R²=0.997) vs piso Sweet–Parker σ^0.5 (lámina única; escalamiento robusto a correcciones relativistas por Lyubarsky 2005).
- Presentar tearing como **hipótesis fenomenológica** (caja HYP): el exceso ×2.4 sugiere fragmentación de la lámina (plasmoides) que multiplica la superficie disipativa; la demostración exige resolver la jerarquía de sub-láminas (trabajo futuro, mignone2024).
- 🛡️ Grado de certeza calibrado en pantalla: "firma fenomenológica", no constante derivada.

### S24 — Variables globales: la firma de la resistividad… y el blindaje numérico
- Figura: `figuras/fig_global_campos_transitorio.pdf` (J_max, ∫E·J, amplificación E_mag) + `fig_global_estructuras.pdf` (f_Vz).
- Física: disipación acumulada crece 0.03→0.44 con σ; amplificación de E_mag propia decae 15%→0 (congelamiento); f_Vz máxima (0.37) justo en σ≈1400 — las estructuras secundarias viven en la transición.
- **Punto crítico**: la estabilización del plateau de J_max marca dónde la difusividad física supera el error de truncamiento de la malla ⟹ **evidencia empírica de que los resultados en σ∈[1400,7000] no están contaminados por disipación artificial**. + argumento de buen planteamiento (Lecoanet 2016: la KHI 2D ideal no converge; la η explícita es lo que da significado convergente a γ(σ)).
- 🛡️ ESTA es la respuesta empírica al vector "disipación numérica vs física". Ensayarla como tal.

### S25 — Campaña magnética I: intensidad y orientación (obj. 4)
- Figuras: `figuras/fig_campA_enstrofia` (o tabla A) + `figuras/fig_campB_rho_collage.pdf`.
- A (intensidad): γ cae 0.81→0.38 y Ω^max 87→25 al subir B₀ — pero el agente es **presión/magnetización** (β∝B₀⁻²), NO tensión: el flujo sigue super-Alfvénico paralelo (M_A,∥=9.4→6.4).
- B (orientación y–z): la tensión la ejerce solo B_y∥k; paradoja θ=0° (guía pura ⟹ sin estiramiento en el plano ⟹ sin dinamo/reconexión ⟹ enstrofía baja) resuelta con el argumento de Mizuno (B_y como semilla de amplificación). Observable global vs local (Ω^int vs Ω^max) desambigua la "paradoja" de θ=90°.

### S26 — Campaña magnética II: balance energético y canales de disipación
- Figuras: `figuras/fig_campB_ekin_emag` (anti-fase) o `fig_campB_conversion` (espacio de fases de tasas) + `fig_campB_disipacion_resumen`.
- Anti-fase E_kin↔E_mag ciclo a ciclo (r≈−0.6 a −0.98): canal de conversión directo y reversible. La resistividad decide el **destino** de la energía: a σ=10000 intercambio cuasi-reversible; a σ=6000 la disipación óhmica desvía energía a calor (a θ=90° hasta un orden de magnitud más). Conservación de E_tot a ≲10⁻³ (validación interna del esquema).
- Mensaje del objetivo 4: cuando la geometría enmascara la fase lineal, el observable correcto no es γ sino el balance energético.

---

## BLOQUE 5 — Cierre (3 slides, 3 min)

### S27 — Conclusiones (por objetivo, espejo de la monografía)
1. γ_KHI(σ): sigmoide con offset; asíntota ideal 1.03±0.05, consistente al 8% con teoría lineal RMHD compresible; transición como zona [1400,7000].
2. Estructuras secundarias: Ω∝σ^1.22 > piso Sweet–Parker (hipótesis tearing); f_Vz máxima en la transición.
3. Variables globales: la conductividad controla láminas de corriente, disipación acumulada y amplificación magnética.
4. Campo magnético: supresión por presión/magnetización (A); tensión solo vía B_y∥k (B); sin tensión, reconexión y disipación directa (C); anti-fase cinético↔magnética como canal universal.
- SIN "[objetivo cumplido]" — lección del director: eso lo decide el evaluador.

### S28 — Limitaciones y trabajo futuro (honestidad epistemológica)
- Dos columnas. Limitaciones: 2D (sin cascada 3D), EoS politrópica Γ=4/3, **σ escalar (sin Hall/anisotropía; el continuo unifluido es un truncamiento de la jerarquía de momentos de Vlasov — válido mientras la escala disipativa relevante sea la capa resistiva δ~S^{−1/2}, no el giroradio)**, resolución roza las láminas a alta σ, asíntota ideal extrapolada (dato máximo = 85%).
- Futuro: plateau directo a Rm*≳500, dispersión RMHD grado 8 completa, 3D/GRMHD, esquemas de 4.º orden (mignone2024), frontera tensión-vs-presión con más ángulos.
- 🛡️ (Cobertura filosófica del informe): reconocer el límite colisional/cinético del modelo ANTES de que lo pregunten. Es la slide de "madurez intelectual" que ambos informes recomiendan cerrar.

### S29 — Gracias `[plain]`
- Imagen fuerte (vórtice), datos de contacto, "Preguntas".

---

## BACKUP (después de `\appendix`, ~12 frames — no cuentan para los 30 min)

| # | Título | Contenido | Vector que cubre |
|---|---|---|---|
| B1 | Derivación F=dA y Bianchi | Paso a paso d²=0, matrices F_{μν} explícitas | V1 tensorial |
| B2 | T^{μν} por derivada funcional de Hilbert | S_em y S_fluid (Taub), por qué J·A no contribuye | V1 |
| B3 | Telégrafo desde la acción GLM | 2.º orden vs forma Dedner 1.er orden; equivalencia y por qué se integra en 1.er orden (Riemann + Godunov–Powell + SHTC) | V1 |
| B4 | Espectro del jacobiano 14×14 | 8 a ±c (EM+GLM), magnetosónicas, entropía/cizalla, carga; condición subcaracterística de Liu; CFL | V1/V3 |
| B5 | Ley de Ohm 3+1 completa | Álgebra de la proyección, ρ_e vs ρ_q (figura marco comóvil) | V1 |
| B6 | Validación del solver lineal | Michalke (ω̂=0.1897 reproducido), umbral de Landau √2 (vortex sheet), doble capa desacoplada (e^{−kD}≈0.2%) | V3 convergencia |
| B7 | **¿Por qué HLL+MP5 y no HLLC?** | El paper del código ES HLLC; para el barrido usamos HLL+MP5: la agudeza de estados de 5.º orden compensa la difusión de contacto, con simplicidad/positividad/costo; disipación numérica < física verificada (S24) | V2/V3 — pregunta muy probable |
| B8 | Estadística completa | AIC/BIC definiciones, test de rachas (p-valor), hold-out RMSE, degeneración corr(γ₀,C)=−0.997 y por qué C+γ₀ es el observable robusto (varía 3.9%) | V3 |
| B9 | Tabla canónica 44 σ + matriz σ×CFL | Incluye criterios de exclusión (R², SNR, picos) | transparencia |
| B10 | De Vlasov al fluido | Jerarquía de momentos, equilibrio termodinámico local, dónde colapsa el continuo; conexión Liouville | V4 epistemológico (Liouville es tema reciente del jurado) |
| B11 | Recursos computacionales | ~30 000 horas-núcleo, servidor, Fortran/estructura de Cueva, flujo de análisis Python | "caja negra" |
| B12 | Figuras extra campañas B/C | fig_campC_*, energía por ángulo, colecciones de mapas ρ | repreguntas obj. 4 |

---

## Notas de producción

- **Compilación**: igual que la plantilla (`pdflatex → bibtex → pdflatex ×2`); mantener `\parencite→\citep`.
- **Figuras**: TODAS ya existen en `monografia/figuras/` (PDF vectorial). Copiarlas a `presentacion/figures/`. Solo habría que producir: (a) esquema de flechas del mapa de límites (TikZ, S10), (b) diagrama de campañas (S5/S17 — puede reusarse `figuras/campana_A_3d` etc.).
- **Paleta**: la Inferno de la plantilla YA es la paleta de las gráficas del barrido (negro→púrpura→naranja) — coherencia visual automática.
- **Notación en slides = notación de la monografía**: W Lorentz, Γ adiabático, ω̂ tasa normalizada, σ SOLO conductividad. Cueva sin artículo ("Cueva", no "el Cueva"). Sin jerga interna (nada de "v5/v6", "35A" solo como "setup tipo Mizuno").
- **Ensayos**: cronometrar bloques con checkpoints — min 4:30 fin motivación, min 11 fin teoría, min 18 fin numérica, min 27 fin resultados.
- **Respuestas de 60 s a ensayar** (del perfil del jurado): (1) KHI sin ecuaciones; (2) ∇·B/Bianchi/GLM/causalidad; (3) disipación numérica vs física (plateau J_max + Lecoanet + diseño MP5); (4) origen cinético de η y límites del continuo; (5) límite no relativista del sistema; (6) por qué HLL y no HLLC.
