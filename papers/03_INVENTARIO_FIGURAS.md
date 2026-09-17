# Inventario de figuras: 47 en la monografía → ~12 en el artículo

> Inventario crudo generado automáticamente (label + archivos + leyenda completa):
> **`comun/inventario_figuras_auto.tsv`**. Regenerarlo con
> `papers/comun/regen_inventario.py` si la monografía cambia.

**Cuota realista**: un Paper de MNRAS de ~15 páginas admite **10–14 figuras**.
La monografía tiene **47 entornos `figure`**. Hay que cortar ~75 %.

Leyenda de veredictos:
**✅ va** · **🟡 quizá / apéndice** · **❌ fuera (didáctica o redundante)**

## Capítulos 1–4 (teoría y método): 9 figuras → **0–1**

| Label | Archivo | Veredicto | Motivo |
|---|---|---|---|
| `fig:contexto_jet` | `contexto_jet` | 🟡 | Bonita, pero la figura de contexto es lo primero que un editor recorta |
| `fig:foliacion_3p1` | `foliacion_3p1` | ❌ | Libro de texto |
| `fig:glm_limpieza` | `glm_limpieza` | ❌ | Didáctica (GLM se cita) |
| `fig:marco_comovil` | `marco_comovil_lab` | ❌ | Libro de texto |
| `fig:esquema_khi_teorico` | `KHI_una_interfaz` | ❌ | Didáctica |
| `fig:esquema_vol_fin` | `volumenes_finitos` | ❌ | Didáctica |
| `fig:celda_3d_flujos` | `celda_3d_flujos` | ❌ | Didáctica |
| `fig:riemann_hll` | `riemann_hll` | ❌ | Didáctica |
| `fig:imex_splitting` | `imex_splitting` | ❌ | Didáctica (IMEX se cita) |

## Setup: 2 figuras → **2** ✅

| Label | Archivo | Veredicto | Nota |
|---|---|---|---|
| `fig:setup_inicial` | `velocidad_inicial.pdf`, `rho_inicial.pdf` | ✅ **Fig. 1** | Reducir a 2 paneles. (Los `frame_0001_*.png` están **comentados** en el `.tex` y **no existen** en `figuras/` — no hacen falta) |
| `fig:campanas_BC_3d` | `campana_A_3d`, `campana_B_3d`, `campana_C_3d` | ✅ **Fig. 2** | Los 3 esquemas en fila. Necesaria para entender **k·B = 0** en la campaña C |

## Resultados — barrido en σ: 16 figuras → **7** (el núcleo del artículo)

| Label | Archivo | Veredicto | Nota |
|---|---|---|---|
| `fig:ultrawide_omega_tot` | `fig_ultrawide_omega_tot.pdf` | 🟡 | Redundante con `omega_zp`: **elegir una** |
| `fig:ultrawide_omega_zp` | `fig_ultrawide_omega_zp.pdf` | ✅ **Fig. 3** | Las 44 trayectorias + las 4 regiones. La figura "panorámica" |
| `fig:mapa_conductividad` | `fig_conductividad_rho_collage.pdf` | ✅ **Fig. 4** | Collage σ × t. La única figura de *imágenes* del artículo. **Necesita rótulos de columna** (lineal/pico/turbulenta) |
| `fig:lnfit` | `ln_omega_vs_t.pdf` | 🟡 | Justifica la extracción de γ. Si falta espacio → apéndice |
| `fig:ajuste_v6` | `fig1_ajuste_v6.pdf` | ✅ **Fig. 5 — LA figura del artículo** | La sigmoide γ(σ). Si solo sobreviviera una, es esta |
| `fig:3v4_v6` | `fig2_3p_vs_4p.pdf` | 🟡 | Selección de modelo (AIC). Apéndice |
| `fig:holdout_v6` | `fig10_holdout.pdf` | 🟡 | Validación. Apéndice |
| `fig:zona_transicion` | `fig_zona_transicion` | ✅ **Fig. 6** | La zona [1400, 7000]. 2.º resultado |
| `fig:regimenes` | `fig_regimenes` | 🟡 | Solapa con `zona_transicion` |
| `fig:derivadas_scrit` | `fig_derivadas_scrit` | 🟡 | Derivada logarítmica. Apéndice |
| `fig:est_v6` | `fig3_estimadores.pdf` | 🟡 | Los 4 estimadores de σ_crit → **puede reducirse a la tabla `tab:est_v6`** |
| `fig:sigma_crit_promedio` | `fig_sigma_crit_promedio` | ❌ | Se resume en un número ± error |
| `fig:omega_max_pot` | `fig_omega_max_leypotencias.pdf` | ✅ **Fig. 7** | σ^1.22 vs. piso Sweet–Parker σ^0.5. 3.er resultado |
| `fig:global_campos_transitorio` | `fig_global_campos_transitorio.pdf` | ✅ **Fig. 8** | Variables EM globales |
| `fig:global_estructuras` | `fig_global_estructuras.pdf` | ✅ **Fig. 9** | f_Vz y estructuras secundarias |

## Resultados — teoría lineal: 5 figuras → **2**

| Label | Archivo | Veredicto | Nota |
|---|---|---|---|
| `fig:michalke_v6` | `fig4_michalke.pdf` | 🟡 | Techo inviscido |
| `fig:dual_v6` | `fig7_dual.pdf` | ❌ | Se resuelve en una frase |
| `fig:compresible_v6` | `fig9_compresible.pdf` | ✅ **Fig. 10** | Lees–Lin: 0,095 vs. 0,103 |
| `fig:escalera_v6` | `fig6_escalera.pdf` | 🟡 | "Escalera" de correcciones — didáctica pero muy efectiva |
| `fig:marcos_v6` | `fig8_marcos.pdf` | ✅ **Fig. 11** | Contraste MHD / RMHD / RRMHD. Muy vendible |

## Campaña magnética: 15 figuras → **2–3** (el recorte más brutal)

| Label | Archivo | Veredicto | Nota |
|---|---|---|---|
| `fig:mapa_campA` | `fig_campA_rho_collage.pdf` | ❌ | Collage; a suplementario |
| `fig:campA_enstrofia` | `fig_campA_enstrofia` | ✅ **Fig. 12** | Supresión por B₀ |
| `fig:campB_enstrofia` | `fig_campB_enstrofia` | 🟡 | Solapa con `omegamax_theta` |
| `fig:mapa_campB` | `fig_campB_rho_collage.pdf` | ❌ | Collage; a suplementario |
| `fig:campB_omegamax_theta` | `fig_campB_omegamax_theta` | ✅ **Fig. 13** | Ω^max(θ): la figura de orientación |
| `fig:campB_conversion` | `fig_campB_conversion` | ❌ | — |
| `fig:campB_emag` | `fig_campB_emag` | ❌ | — |
| `fig:campB_ekin_emag` | `fig_campB_ekin_emag` | 🟡 | Anti-fase en el tiempo |
| `fig:campB_ekin_emag_scatter` | `fig_campB_ekin_emag_scatter` | ✅ **Fig. 14** | Espacio de fases: σ=6000 vs 10⁴. **Más contundente que la serie temporal** |
| `fig:campC_enstrofia` | `fig_campC_enstrofia` | 🟡 | Campaña C (k·B = 0) |
| `fig:mapa_campC` | `fig_campC_rho_collage.pdf` | ❌ | Collage; a suplementario |
| `fig:campC_ekin_emag_scatter` | `fig_campC_ekin_emag_scatter` | 🟡 | — |
| `fig:campB_energia_todos` | `fig_campB_energia_todos` | ❌ | — |
| `fig:campB_cierre` | `fig_campB_cierre` | ❌ | — |
| `fig:campB_disipacion_resumen` | `fig_campB_disipacion_resumen` | ❌ | — |
| `fig:campC_energia_todos` | `fig_campC_energia_todos` | ❌ | — |
| `fig:campC_disipacion_resumen` | `fig_campC_disipacion_resumen` | ❌ | — |

---

## Trabajo técnico sobre las figuras (aplica a TODAS las que pasen)

1. **Traducir al inglés**: ejes, leyendas, anotaciones, títulos internos.
   ⚠️ Esto obliga a **regenerar desde los scripts**, no a editar el PDF. Los
   generadores están en `presentacion/scripts_slide/` y en
   `INFO/lab/lab_offsetC/` (ver memoria del proyecto). **Localizar el script de
   cada figura que pase el corte es tarea previa a escribir.**
2. **Ancho de columna MNRAS**: `mnras.cls` es de **2 columnas**.
   - Columna simple: **84 mm (3,3 in)** → `width=\columnwidth`
   - Doble columna: **170 mm (6,7 in)** → entorno `figure*`, `width=\textwidth`
   - Regenerar con `figsize` correcto y **fuentes ≥ 8 pt al tamaño final**
     (una figura de 6,7 in reducida a 3,3 in deja las etiquetas ilegibles).
3. **Vectorial (PDF)**: ya lo son casi todas. Los collages de densidad son raster
   → verificar **≥ 300 ppi** al tamaño final.
4. **Sin rojo–verde** (requisito de accesibilidad MNRAS). Revisar la paleta
   negro→púrpura→naranja del barrido: es segura. Revisar las de campaña.
5. **Unidades en todos los ejes.**
6. **Alt text** para cada figura (`Alt text: ...` bajo la leyenda). Requisito MNRAS.
7. **Grosor de línea ≥ 0,3 pt.**
8. Nombres de archivo simples: `fig1.pdf`, `fig2.pdf`, … al empaquetar el envío.
9. **Quitar el `\figtag` F1–F41** — ese contador es del deck de sustentación, no va
   al artículo.
