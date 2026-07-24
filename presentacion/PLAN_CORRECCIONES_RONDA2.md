# Plan de correcciones — Ronda 2 (observaciones del profesor, 22-jul-2026)

> **ESTADO 23-jul: TODO IMPLEMENTADO Y COMPILADO (main.pdf, 52 pp).**
> Deck: interludio eliminado; S3 con overlay 2 pasos (contexto → esquema+simulación
> σ=1000+nubes CC BY); mapa MHD movido a lámina 5 con frase de resistividad; nota de
> unidades en "Diseño"; ecuación IMEX arriba de "Forma Conservativa"; S11 con franja
> Ω_zp(t)+ventana canónica; S12–S15 fusionadas en "Método Numérico" (F6+F8, CFL,
> originales → respaldo B14–B17); matriz con etiquetas transición/cuasi-ideal;
> ultrawide con 4 regiones (fronteras: ventana canónica [2.4,3.4] + t_peak=5.4 del
> run σ=10⁴); collage con encabezados de fase; S25 con autores explícitos; S26 con
> disipación ηJ² por 4 ventanas (fig nueva fig_global_campos_ventanas_slide).
> Scripts nuevos/modificados en scripts_slide/. F5 (GLM) corregida.
> PENDIENTE de Sebastián: revisar el PDF; preguntar a Bryan la observación perdida.
> NO tocados (por decisión): guion, banco, video, anexo de figuras (la numeración F
> cambió: F7=imex en lámina 12, etc. — el anexo quedó desfasado si se retoma).

**Contexto:** sustentación = **30 min exactos de exposición + 15 min de preguntas**.
El guion actual está presupuestado en 44:30 → hay que recortar ~15 min.
**Próximo ensayo: sábado 26-jul, 18:00.**

**Regla de trabajo:** discutir observación por observación con Sebastián; implementar TODO al final, cuando la lista esté cerrada.

---

## ✅ Acordado (pendiente de implementar)

### 1. Fusión del método numérico: S12+S13+S14+S15 → UNA lámina
- Nueva lámina única "Método numérico": FV + MP5/HLL + IMEX + Ferrari–Cardano.
- Conserva **F6** (`celda_3d_flujos.pdf`) y **F8** (`imex_splitting_slide.pdf`). Se suelta F7 (`riemann_hll.pdf`).
- Conservar la caja "disipación numérica < disipación física" (blindaje ante jurado).
- Las 4 láminas originales completas pasan al respaldo.
- Ahorro estimado: ~5–6 min.

### 2. S9 (Forma Fuertemente Conservativa) recibe la ecuación de la partición IMEX
- Arriba, al centro: ∂ₜ**U** = −∂ᵢ**F**ⁱ(**U**) [no rígido] + **S**_rig(**U**) [rígido], con underbraces.
- Tipografiada en LaTeX (no la figura); F8 sigue viviendo en la lámina fusionada.
- Se mantiene el desglose conservadas/fuentes ya existente (encaja con la observación
  del profe: "ecuación de conservación con fuentes, explicar cuáles son").
- Narrativa: "la fuente −J es rígida → por eso se integra implícita (IMEX)".

### 3. A3 — S8 (GLM): SIN cambio de lámina
- La observación era sobre la explicación oral (reducir tiempo al hablar), no sobre el contenido.
- Guion: comprimir el relato de S8 a mensaje único ("dos campos auxiliares que
  transportan y amortiguan los errores de divergencia; álgebra en respaldo B3").

## ✅ Ya aplicado

- **F5 (`glm_limpieza.pdf`), panel (b):** flechas y etiquetas c_h subidas de y=0.5 a y=1.05
  para no superponerse a las crestas de los pulsos. Fuente TikZ editada
  (`monografia/figuras/tikz_src/glm_limpieza.tex`), recompilada y copiada a
  `monografia/figuras/` y `presentacion/figures/`. Falta solo recompilar el deck (al final).

### 4. Mover S10 (Mapa de límites MHD) casi a la introducción — ACORDADO
- Insertarla entre S4 ("Por qué resistiva") y S5 ("Diseño del experimento").
- Narrativa: fenómeno → por qué resistiva → mapa HD/MHD/RMHD/RRMHD → diseño.
- Reparto de ponentes: lo deciden Bryan y Sebastián después (NO tocar el reparto en el guion;
  solo ajustar tiempos/checkpoints y dejar los bloques como estén).
- AÑADIDO (del punto 17): en la lámina movida, incluir UNA frase sobre qué hace la
  resistividad — "σ finita rompe el congelamiento en las capas finas: permite reconexión
  y difusión del campo; σ→∞ recupera el congelamiento ideal" — como puente entre las
  versiones de MHD del mapa.

---

## 📋 Por discutir (orden tentativo)

~~5. S3: FR I / FR II~~ — RECLASIFICADO: no es cambio de lámina, es concepto que los ponentes
   deben dominar (el profe preguntó y no se supo responder). Documentado en
   `COSAS_POR_REPASAR.md` §1. Sin cambio en el deck.
~~6. S3: imagen en dos pasos~~ — ACORDADO (pendiente de implementar):
   - Overlay `\only<1>/<2>` en la columna derecha de S3, mismo esqueleto, cambian imagen+caption.
   - Paso 1 = contexto astronómico (`contexto_jet.pdf`, lo actual).
   - Paso 2 = "esto es la KHI": COMPUESTO nuevo = esquema TikZ de cizalla (arriba, pequeño)
     + fotograma de densidad de NUESTRAS simulaciones con vórtices enrollados (principal)
     + foto pequeña de nubes Kelvin–Helmholtz (NASA, dominio público) como gancho cotidiano.
     Detalles (σ y t del fotograma, foto elegida, layout) a discreción al implementar.
   - ELIMINAR el interludio [plain] (su contenido queda absorbido por S3 paso 2);
     desaparece el `\addtocounter{framenumber}{-1}` y el corrimiento de páginas físicas.
   - Guion "para primíparos" (~30 s) en el paso 2.
~~7. S18 (ultrawide enstrofía)~~ — ACORDADO (pendiente de implementar):
   - Regenerar `fig_ultrawide_omega_zp_slide.pdf` (pipeline `INFO/lab/lab_offsetC`) con
     4 bandas verticales sombreadas + etiquetas: numérica / lineal / explosiva /
     relajación-turbulencia.
   - Fronteras definidas sobre el caso ideal de referencia (σ=10⁴); caption:
     "fronteras ilustrativas, definidas sobre el régimen ideal".
   - ⚠️ SER RIGUROSO en determinar las fronteras: derivarlas de los DATOS del run de
     referencia (fin del transiente = inicio de la recta en ln Ω con R² alto de la
     ventana de ajuste del pipeline; fin de lineal = salida de la recta; explosiva
     = hasta t_peak; relajación = post-pico), no ponerlas a ojo. Documentar los t
     de corte usados en el caption o en el guion.
   - Guion: mencionar de viva voz que a σ baja las fronteras se desplazan.
~~8. S19 (visión global)~~ — ACORDADO (pendiente de implementar):
   - Regenerar `fig_conductividad_rho_collage_slide.pdf` (script en `scripts_slide/`) con
     encabezados de columna: "Fase lineal (t=3)" · "Pico (t≈8)" · "Turbulenta (t=14)"
     (en unidades de tiempo de código).
   - Añadir a `COSAS_POR_REPASAR.md`: por qué persisten las estructuras a σ baja
     (difusión óhmica = filtro pasa-bajas → suprime inestabilidades secundarias y
     reconexión rápida → sin cascada; la estructura grande solo decae difusivamente).
   - Guion S19: frase fija con esa explicación.
~~9. S21 (sigmoide)~~ — RECLASIFICADO: comentario sobre la exposición oral, la lámina QUEDA
   como está. Al explicarla, dejar claro qué se compara: cada punto = γ_KHI medida en una
   simulación (pendiente de ln Ω en su ventana lineal); curva = sigmoide ajustada (35 pts,
   σ≥1600); los 9 resistivos son hold-out. Dato medido vs modelo ajustado. → añadido a
   `COSAS_POR_REPASAR.md`.
~~10. S25 (ley de potencia)~~ — RECLASIFICADO: repaso + verificación menor.
    - La lámina YA declara el piso σ^{1/2} como lámina única Sweet–Parker con citas
      (parker1957, lyubarsky2005, furth1963). Entrada añadida a `COSAS_POR_REPASAR.md` §3
      con la frase para la expo (nombres de autores en voz alta).
    - Al implementar: verificar que las citas de S25 rendericen autor-año visible;
      si salen numéricas, escribir los nombres explícitos en el texto de la caja.
~~11. Disipación resistiva acumulada~~ — ACORDADO (pendiente de implementar):
    - La gráfica es el panel (b) de F19 en S26 (fig_global_campos_transitorio):
      |∫∫ E·J dA dt| vs σ, hoy integrada 0→t_peak.
    - REHACER el análisis con la integral en CUATRO ventanas, como pidió el profe:
      (1) ANTES (transiente numérico), (2) fase LINEAL, (3) zona TURBULENTA (post-pico),
      (4) TODA la serie. Cuatro curvas vs σ para comparar los valores entre sí.
    - Fronteras de ventana consistentes con las del punto #7 (rigurosas, del pipeline).
    - Datos: series temporales de ∫E·J dA de las 44 sims (pipeline lab_offsetC);
      si solo existe el acumulado a t_peak, recomputar de las series crudas.
    - DESPUÉS de rehechas: completar la entrada §4 de `COSAS_POR_REPASAR.md` con los
      valores reales (cocientes entre ventanas) para poder explicarla bien.
    - Física a dominar: la disipación crece con σ aunque η=1/σ cae, porque las láminas
      de corriente se intensifican más rápido (ηJ² sube).
~~12. Unidades~~ — RECLASIFICADO parcial:
    - "No decir segundos" = comentario sobre la exposición oral (sin cambio de deck;
      nota en repaso).
    - SÍ es cambio de deck: aclarar en qué unidades están σ y η EN NUESTRAS UNIDADES.
      Añadir nota breve en S5 (primera aparición numérica de σ): unidades de código,
      c=1, t en L/c; σ en (L/c)⁻¹ ⇒ 1/σ = tiempo resistivo en tiempos de cruce;
      η = 1/σ. Entrada completa en `COSAS_POR_REPASAR.md` §5.
~~13. Momentos de Vlasov~~ — RECLASIFICADO: solo repaso (`COSAS_POR_REPASAR.md` §6);
    B9 queda intacta como respaldo.
~~14–15. Enstrofía (unidades + definición)~~ — RECLASIFICADO: repaso (§7; el pipeline
    INTEGRA sobre el área, no promedia) + UN cambio de deck acordado:
    - S11 recibe una figura didáctica HECHA POR NOSOTROS que acompañe la definición.
    - Propuestas a evaluar al implementar (presentar mockups a Sebastián):
      (a) mapa de ω_z' en 3 instantes + curva Ω(t) con esos instantes marcados;
      (b) esquema TikZ "campo 2D → ∫ω² dA → escalar → punto de la serie Ω(t)";
      (c) RECOMENDADA: snapshot de ω_z' (σ=10⁴, fase de enrollamiento) a la izquierda
          + ln Ω(t) a la derecha con la ventana canónica [2.4,3.4] y la pendiente
          2γ_KHI marcada — conecta el observable con cómo se mide γ.
    - Datos propios (DATOS_LIMPIOS / bundle del clúster).
~~16. Factor CFL~~ — ACORDADO: repaso (§8) + cambio de deck:
    - En la lámina FUSIONADA de método numérico (ex S12–S15), añadir nota breve:
      qué es el CFL (Δt = CFL·Δx/λ_max) y qué significa subirlo/bajarlo
      (subir = paso más grande, más barato, menos margen de estabilidad;
      bajar = paso más corto, más caro, más margen — por eso campaña B usa
      0.04/0.02 frente al 0.10 del barrido).
~~17. Congelamiento de líneas~~ — ACORDADO: repaso (§9) + una frase sobre qué hace la
    resistividad en la lámina del mapa MHD desplazada a la intro (ver punto 4).
~~18. σ=10500 y 6000/10000~~ — ACORDADO: repaso (§10, CORREGIDO: 10500 fue el LÍMITE
    NUMÉRICO del código con CFL=0.10 — consistente con el "límite práctico" de la
    lámina Ferrari–Cardano; además a esa σ la sigmoide ya está al 85% del plateau).
    + OPCIONAL de deck, solo si hay espacio: en S17 (matriz) etiquetar el régimen de
    cada σ de la campaña B: 6000 → "transición", 10000 → "cuasi-ideal".
~~19. Menciones sueltas a "Cueva"~~ — ACORDADO: SE DEJAN las tres (portada, S2, B10).
    El profe objetó el tiempo del método numérico, no el nombre de la herramienta.
~~20. Guion/banco/video~~ — DESCARTADO por decisión de Sebastián (22-jul): esta ronda
    NO se tocan guion, banco de preguntas ni video. Solo las diapositivas.
21. Recompilar deck + re-auditar a 130 dpi. → EN CURSO con la implementación.

## ⚠️ Pendientes externos

- Falta 1 observación final del profesor (Sebastián perdió el internet): preguntar a Bryan o al profesor.
- Para el artículo: usar σ máx = 10000 (no 10500).
