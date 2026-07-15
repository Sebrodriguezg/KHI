# Auditoría de figuras — presentación de sustentación

*Revisión página por página del `main.pdf` (46 pp) a 130 dpi — 2026-07-14.*
Criterios: (a) ¿texto y números legibles proyectados?, (b) ¿la imagen cabe completa?

## Resumen

| Categoría | Páginas | Acción |
|---|---|---|
| 🔴 REHACER (versión slide) | P19, P25(×2), P26, P16(×2), P18 | necesitan regenerarse con fuentes grandes |
| 🟡 Recorte/ajuste opcional | P21, P42, P46, P5 | mejorarían, no bloquean |
| 🟢 Reacomodadas (ya corregido en main.tex) | P16, P26, P41 | cortes eliminados el 14-jul |
| ✅ OK sin cambios | resto (35 páginas) | — |

---

## 🔴 REHACER — versión slide con fuentes grandes (pendiente de los scripts)

Las figuras de la monografía se diseñaron para página completa a 11 pt; al reducirlas a media lámina los textos internos caen por debajo del tamaño legible. **Regla para las versiones slide**: fuentes de ejes/leyendas ≥14–16 pt en el canvas original, sin título interno (el frametitle ya lo dice), leyendas dentro del panel, y solo los paneles que la lámina necesita.

1. **P19 (S19 — extracción de γ): `ln_omega_vs_t.pdf`**
   - Problema: leyenda ilegible, título interno diminuto, colorbar con 44 etiquetas microscópicas, ejes ilegibles.
   - Versión slide: sin título interno; colorbar continua (σ) en vez de 44 items; fuentes grandes; mantener ventana sombreada [2.4,3.4] y el código de estilo por régimen.

2. **P25 (S25 — campaña magnética I): `fig_campA_enstrofia.pdf` y `fig_campB_omegamax_theta.pdf`**
   - Problema: títulos largos diminutos, leyendas (B₀=…, σ=…) y ejes muy pequeños en ambas.
   - Versión slide: fuentes ×1.6–2, títulos internos fuera (o a una sola línea corta), leyendas grandes.

3. **P26 (S26 — balance energético): `fig_campB_ekin_emag_scatter.pdf`**
   - Problema original: 6 paneles verticales (684×837 pt) — se cortaban θ=60° y 90°. Interim aplicado: height=0.72\textheight (cabe entera pero paneles pequeños).
   - Versión slide: **1 fila × 3 paneles (θ=0°, 45°, 90°)** con fuentes grandes — es la progresión que cuenta la historia; los 6 paneles completos quedan en la monografía.

4. **P16 (S16 — setup): `velocidad_inicial.pdf` y `rho_inicial.pdf`**
   - Problema original: apiladas a ancho completo se cortaba ρ. Interim: height=0.33\textheight cada una (caben, pero ticks/títulos internos pequeños).
   - Versión slide: un solo PDF con 2 paneles apilados (o lado a lado), sin títulos internos, fuentes grandes, colorbar compartida si aplica.

5. **P18 (S18 — visión global): `fig_conductividad_rho_collage.pdf`**
   - Problema: ticks y rótulos de ejes microscópicos; rótulos de fila (σ=…) y columna (t=…) apenas legibles; título interno redundante.
   - Versión slide: sin título interno, SIN ticks/números de ejes (es cualitativa), rótulos de fila/columna grandes (≥16 pt), colorbar con 3–4 ticks grandes.

## 🟡 Mejoras opcionales (no bloquean)

6. **P21 (S21): `fig_zona_transicion.pdf`** — anotaciones de los estimadores (M4=2815, M2=3400, bordes) diminutas. Los valores están duplicados en la caja de texto de la lámina → tolerable. Si se regenera: agrandar solo las anotaciones y los rótulos RESISTIVO/TRANSICIÓN/IDEAL.
7. **P42 (B10): `fig_ultrawide_omega_zp.pdf`** — misma familia que P19 (ilegible), pero es respaldo cualitativo. Rehacer solo si se rehace la de P19 con el mismo script.
8. **P46 (B14): collages B y C** — ticks microscópicos; respaldo cualitativo, tolerable. Se beneficiaría de la misma versión sin-ejes del punto 5.
9. **P5 (S5): `campana_A/B/C_3d.pdf`** — etiquetas `x=±0.5` y ejes pequeños; legibles a duras penas. Opcional: regenerar con fuentes mayores (son TikZ/matplotlib de la monografía, `figuras/tikz_src`?).

## 🟢 Reacomodos ya aplicados en `main.tex` (14-jul)

- **P16**: las dos figuras del setup pasaron de `width=\linewidth` a `height=0.33\textheight` → ya no se corta ρ.
- **P26**: scatter 6-paneles pasó a `height=0.72\textheight` → caben los 6 paneles (interim hasta versión slide).
- **P41 (B9)**: `fig_derivadas_scrit.pdf` pasó a `height=0.74\textheight` → el panel M3 ya no se corta.

## ✅ Verificadas OK (legibles y completas)

- **TikZ propios** (nítidos a cualquier escala): P3 contexto_jet, P8 glm_limpieza, P10 mapa de límites, P12 celda_3d, P13 riemann_hll, P14 imex_splitting, P37 marco_comovil.
- **Matplotlib legibles**: P20 fig1_ajuste (leyenda pequeña pero legible), P22 fig6_escalera, P23 ley de potencias, P24 global_campos (títulos de panel pequeños pero legibles), P40 (B8) 3p-vs-4p + holdout, P38 (B6) michalke + dual, P41 (B9) regimenes, P45 (B13) estructuras + campC scatter (respaldo).
- **Texto puro** (siempre nítido): P1, P2, P4, P6, P7, P9, P11, P15, P17, P27–P36, P39, P43, P44.

## Pendiente

- [ ] Ubicar scripts generadores (el usuario indicará el directorio) y regenerar las 7 figuras de la categoría 🔴 en versión slide.
- [ ] Sustituir en `figures/` y recompilar; re-auditar P16, P18, P19, P25, P26.
