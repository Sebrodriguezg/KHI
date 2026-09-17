# Data availability statement — borrador

**Obligatorio en MNRAS** (sección propia, tras Acknowledgements).
**Recomendado en OJAp** (siguiendo Chen et al. 2022, ApJS 260, 5).

## Decisiones pendientes

- [ ] ¿Se publican los datos del barrido? Mínimo recomendable: la **tabla canónica
      completa** (44 filas: σ_j, γ_KHI, σ_γ, R², Ω_zp^max, t_peak, marca de pico)
      en un `.csv`/`.txt` legible por máquina.
- [ ] ¿Dónde? **Zenodo** es la opción estándar (da DOI, gratis, sin límite
      práctico para tablas y scripts). Alternativa para la tabla: **VizieR (CDS)**,
      que MNRAS recomienda explícitamente.
- [ ] ¿Se publican los **scripts de análisis** (pipeline de σ, ajuste sigmoide,
      estimadores de σ_crit)? **Recomendado**: es lo que hace el resultado
      reproducible y no compromete el código del director.
- [ ] ¿Qué pasa con ***Cueva***? Es código del director, **no es nuestro para
      liberar**. Decisión suya. Opciones: (a) disponible bajo petición razonable;
      (b) registro en **ASCL** (`ascl.net`) sin liberar el código; (c) liberación
      con licencia. **Hay que preguntárselo explícitamente.**
- [ ] ¿Los volcados completos (`print_backup_*`, 140 MB cada uno) se comparten?
      Probablemente no: demasiado pesados y solo existe una corrida local completa
      (y esa es del caso 35B, densidad invertida). **Se ofrecen bajo petición.**

## Plantilla A — datos derivados en Zenodo, código bajo petición

> **Data availability**
>
> The derived data underlying this article — the growth rates, fit parameters and
> global diagnostics for all 44 conductivity runs, together with the analysis
> scripts used to produce the figures — are available in Zenodo, at
> https://doi.org/10.5281/zenodo.XXXXXXX. The raw simulation output (several
> terabytes) is not publicly archived owing to its volume, but will be shared on
> reasonable request to the corresponding author. The RRMHD code *Cueva* is not
> publicly available; enquiries should be addressed to S.M.-A.

## Plantilla B — mínima (si no se archiva nada)

> **Data availability**
>
> The data underlying this article will be shared on reasonable request to the
> corresponding author.

⚠️ **La plantilla B es legal pero débil.** Un árbitro puede objetarla, y desperdicia
la oportunidad de que el barrido se cite por sí mismo. **Recomendación: plantilla A.**

## Citación de software (FORCE11 — MNRAS lo pide)

Entradas `.bib` a añadir y citar en el texto, con **versión**:

- `numpy` — Harris et al. (2020), Nature 585, 357
- `scipy` — Virtanen et al. (2020), Nat. Methods 17, 261
- `matplotlib` — Hunter (2007), CSE 9, 90
- `astropy`, si se usa
- *Cueva* — Miranda-Aranguren (2018) + registro ASCL si se crea
