# Revisión nocturna automática (Claude) — resumen

*Rama `revision-monografia`. Trabajo hecho mientras Sebas dormía, sin autorización por paso.*

## Qué hice
Revisé **todo el documento** con el mismo detalle con que Sebas leyó sus notas. Añadí un comando nuevo **`\claudenota{}` en naranja** (`[CLAUDE: …]`), distinto del azul de Sebas (`\sebnota`), para:
1. **Responder/afinar** las notas de Sebas donde tengo cómo (código `Cueva`, literatura, matemática).
2. **Añadir hallazgos nuevos** (inconsistencias de notación, citas, consistencia con el código).

**34 `\claudenota`** insertadas. El documento compila limpio (**110 pp**, 0 referencias/citas indefinidas). Nada destructivo: todo en naranja y reversible (cada capítulo en su commit).

## Hallazgos más importantes (nuevos)
- **Cap. 2 — símbolo `ε` ambiguo:** se usa como densidad de energía (`ρh=ε+p`) y como energía interna específica (`h=1+ε+p/ρ`). Unificar.
- **Cap. 2 vs Anexo — notación GLM intercambiada:** cap.2 usa `Φ`(eléctrica)/`Ψ`(magnética); el anexo usa `ψ`/`φ` con las letras cambiadas. Unificar.
- **Cap. 2 — GLM 2.º vs 1.er orden:** la acción/telégrafo da un sistema de 2.º orden, pero el sistema 3+1 implementado (Dedner) es de 1.er orden; no se muestra la reducción. Aclarar.
- **Cap. 2 — "invarianza de Galileo"** es impreciso en contexto relativista (término de Powell = MHD clásica).
- **Cap. 3 — `w=ρhΓ²+B²`** debe ser `w=ρhΓ²` (unificar con cap.2; resuelve la nota roja). El `+B²` no es inercia térmica.
- **Cap. 4 — recuperación de primitivas:** verificada contra el código (`varprimitivecardano`); la cita correcta es **Miranda**, no `mizuno-2013` (que es el paper de EoS).
- **Cap. 6 — `Res-RMHD`** = RRMHD (evitar introducir una sigla nueva); **`ω̃=0.103`** = `(C+γ₀)·a_kh/v_sh` (derivación dada); **`R²<0.7`** reformular ("no hay fase lineal", no "ajuste pobre"); **dispersión de grado 8 ya existe** en `chow2023`; en un código de fluido **no hay "radio de sincrotrón"**.

## Respuestas dadas a dudas de Sebas (selección)
- `d(dx^ν)=d²x^ν=0` → **sí, correcto** (nilpotencia).
- `S_em` sin fuente `J·A` → **correcto** (T_em sale de variar la métrica; la fuente no depende de g).
- `S_fluid=∫p√−g` válida en RRMHD → **sí** (el fluido sigue perfecto; la disipación está en Ohm).
- footnote IMEX, footnote GLM, footnote Alfvén → **propuestas redactadas** en sus notas.
- BCs del setup → **periódicas en y, abiertas en x** (confirmar flag en `parameters.f95`).

## Por capítulo
Cap.1: 2 · Cap.2: 12 · Cap.3: 4 · Cap.4: 4 · Cap.5: 3 · Cap.6: 6 · Cap.7: 2 · Anexos: 1.

## Estado de la tabla de revisión
`REVISION_NOTAS.md` / `REVISION_NOTAS.pdf` regenerados: **122 notas** (🔴 REV 5 · 🔵 SEB 83 · 🟠 CLAUDE 34 · 🟢 BRY 0).

## Cómo limpiar al final (T16)
Las `\claudenota` (y `\sebnota`, `\revnota`) se quitan de un golpe redefiniéndolas vacías en el preámbulo:
```latex
\renewcommand{\claudenota}[1]{}
```

## Lo que NO toqué (a propósito)
- El contenido de tus `\sebnota` (las dejé intactas; solo añadí naranjas al lado).
- Las ~8 notas de **campaña magnética** (cap.5/6/7): dependen de los datos del martes.
- No reescribí prosa del cuerpo: todo va como anotación para que tú decidas.
