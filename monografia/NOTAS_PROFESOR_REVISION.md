# Notas del director (Prof. Sergio Miranda) — commit `e45cf38`

**Commit:** `e45cf38` "0ultima revisión escrito cap 4, 5, 6, 7 y 8" — Sergio Miranda `<sermiranda@gmail.com>`, 2026-06-28.
**Rama:** `revision-monografia`. **Convención del profesor:** notas en macro `\prof{...}` (rojo, `[REV: ...]`); texto que sugiere eliminar/reemplazar con `\sout{...}` (tachado, paquete `ulem`).

Numeración de capítulos del profesor (según su mensaje de commit): **cap 4** = Código Cueva (`04_numerical_methods`), **cap 5** = Set-up (`setup_exp`), **cap 6** = Resultados (`05_results_discussion`), **cap 7** = Conclusiones (`06_conclusions`), **cap 8 / apéndice** = Agradecimientos-cómputo (`agradecimientos_cluster`).

**Total: 38 notas `\prof` + varios `\sout` sin nota.** Capítulos 1–3 (Introducción, RRMHD, KHI) NO recibieron cambios.

### Avance (actualizado 29-jun)

**Resueltas: 5** — `6.3`, `6.4`, `6.6`, `6.22`, `6.23`. · **Reubicada (pendiente): 1** — `6.5`. · **Pendientes: 32**.

Lo hecho hasta ahora (todo en `05_results_discussion.tex`, sin commit todavía):
- **3 fallas de compilación corregidas:** (a) borrado el *fence* de Markdown (marca de código `latex`) que quedó pegado y ensuciaba la lista de validación; (b) de-duplicado el caption de la fig. de marcos; (c) el "2815" ya no se desborda/tacha.
- **Caption de la fig. de ajuste (6.3/6.4):** reemplazado por la redacción del director (sin "v6", sin "asíntota disipativa"). Esto además **arregló el desborde de la figura en la página** (ahora las figs. de ajuste y 3v4 caben limpias juntas).
- **Caption de la fig. de marcos (6.22/6.23):** adoptada la redacción del director; eliminado el caption viejo y el término ambiguo "polarización magnética".
- **6.5** movida del `\caption` a un comentario `%` (para no desbordar), pero **falta aplicarla** (usar "3 y 4 parámetros", no "3p/4p").

> Las celdas marcadas **— HECHA** abajo ya están aplicadas en el `.tex`. Todo es reversible (git).

---

## CAP 4 — Código *Cueva* (`04_numerical_methods.tex`) — 9 notas

| # | Texto literal de la nota | A qué se refiere / qué pide |
|---|---|---|
| 4.1 | "Ojo el jacobiano debe ser una matriz de $14\times 14$ revisen bien esto" | Sobre `$\mathbf{A}_{13\times13}=\partial\mathbf F/\partial\mathbf U$`. El director afirma que el jacobiano del sistema RRMHD conservativo debería ser **14×14**, no 13×13. Conecta con la nota 4.6: falta la variable de carga $q$, lo que cambia el número de variables conservadas/primitivas. Hay que recontar las variables del sistema y corregir la dimensión (y el número de autovalores). |
| 4.2 | "referencias a esta afirmación" | Sobre la frase "Esta acumulación del espectro limita la aplicabilidad de los solucionadores de Riemann exactos, induciendo singularidades algebraicas…". Pide **citar la fuente** que respalda esa afirmación (no puede ir sin referencia). |
| 4.3 | "este termino suena poco natural, cambienlo por de interfaz" | Tacha "interfasiales" (`\sout{interfasiales}`) en "estados interfasiales $(\mathbf U_L,\mathbf U_R)$". Cambiar **"interfasiales" → "de interfaz"**. |
| 4.4 | "Recuperación de variables primitivas mediante el método de Ferrari--Cardano" | Reemplaza el **título de sección** `\sout{Recuperación de Variables Primitivas: la Cuártica del Factor de Lorentz}`. El profesor prefiere nombrar el método (Ferrari–Cardano) en vez de "la Cuártica del Factor de Lorentz". |
| 4.5 | "acá les hace falta la carga, por ello la dimensión del jacobiano no es la correcta" | Sobre el vector de primitivas, al que añade $q$: `$\mathbf P=(\rho,v^j,p,B^j,E^j,q)^T$`. **Falta la densidad de carga $q$** entre las primitivas; ésta es la causa de fondo de la nota 4.1 (dimensión del jacobiano). |
| 4.6 | "ojo no llamen al codigo EL CUEVA, solamente cueva" | Tacha el artículo: `\sout{el}` antes de `\textit{Cueva}` (y `\sout{EL CUEVA}` dentro de la nota). Convención de nombre: decir **"Cueva"**, no "el Cueva". (Revisar todo el documento por consistencia.) |
| 4.7 | "Tschirnhaus" | Corrige la ortografía: `\sout{Tchirnhaus}` → **"Tschirnhaus"** (transformación de Tschirnhaus). |
| 4.8 | "lleva la ecuación a una cuártica sin término cúbico, también conocida como cuártica reducida" | Reemplaza `\sout{la lleva a la forma deprimida}`. Reescritura del paso algebraico de la cuártica. |
| 4.9 | "el término deprimida corresponde al inglés ``depressed'', suprimida, … reducida" | Complemento de 4.8: **"forma deprimida" es un anglicismo** (de *depressed quartic*); usar "cuártica reducida/suprimida". |

> Cambio sin nota: "introduce al sistema hiperbólico **en** un régimen" (corrección de preposición, edición directa).

---

## CAP 5 — Set-up Experimental (`setup_exp.tex`) — 3 notas

| # | Texto literal de la nota | A qué se refiere / qué pide |
|---|---|---|
| 5.1 | "se menciona multiples veces a **cueva** pero no se dice cual es el significado de este acronimo: podrian en el lugar correcto colocar ---> El código \textsc{CUEVA} (*Computing Unit for Environments in Astrophysics*) es una herramienta computacional desarrollada para el estudio numérico de plasmas astrofísicos relativistas.`\parencite{miranda-aranguren-2014}`" | **Definir el acrónimo CUEVA** la primera vez que aparece. El profesor da la frase exacta a insertar y la cita (`miranda-aranguren-2014`). Decidir el "lugar correcto" (probablemente la primera mención en cap 4 o aquí). |
| 5.2 | "La componente $B_z$, dominante en la configuración inicial, corresponde a un campo guía fuera del plano que incrementa la presión magnética total y la magnetización del sistema. Aunque no produce una fuerza inicial, su presencia condiciona la evolución no lineal al modificar el acoplamiento entre el campo magnético, la vorticidad y la compresibilidad del flujo." | **Reescritura propuesta** del texto sobre $B_z$. Tacha `\sout{la componente $B_z$ dominante introduce una presión magnética fuera del plano significativa que regula la termodinámica del flujo.}` y lo sustituye por su versión (más precisa: campo guía, magnetización, sin fuerza inicial). |
| 5.3 | "estan utilizando $\Gamma$ para el indice adiabático y el factor de Lorentz, en el area de la RMHD se acostumbra utilizar $W$ como factor de Lorentz, para evitar esta confusión, a esto se le llama la formulación de Valencia" | **Conflicto de notación:** $\Gamma$ se usa a la vez para índice adiabático ($\Gamma=4/3$) y para el factor de Lorentz. Sugiere usar **$W$ para el factor de Lorentz** (formulación de Valencia). Implica revisar toda la monografía donde aparezca $\Gamma$ como Lorentz. |

---

## CAP 6 — Resultados y análisis de la KHI (`05_results_discussion.tex`) — 23 notas

| # | Texto literal de la nota | A qué se refiere / qué pide |
|---|---|---|
| 6.1 | "no se entiende cuales son los modelos AIC y BIC" | Caption de Tabla `par_v6`. Pide **explicar qué son AIC y BIC** (criterios de información de Akaike/Bayesiano) — no se definen en el capítulo. |
| 6.2 | "mejorar la presentación de estos datos no se dice que es 4p y 3p (obviamente 3 puntos y 4 puntos, pero lo dejan a inferir al lector mala practica), que es comparación anidada?, el lector no se entera que es lo que proponen con estos dos valores que presentan" | Fila `$\Delta$AIC (4p vs 3p)` de la tabla. **"4p"/"3p" sin definir** (en realidad son modelos de 4 y 3 *parámetros*, no puntos) y "comparación anidada" sin explicar. Mejorar presentación y aclarar qué se concluye. |
| **6.3 — HECHA** | "Yo evitaría llamar a $C\simeq -0.45$ "asíntota disipativa" como un dato físico fuerte, porque una tasa de crecimiento negativa puede sonar problemática si el lector espera crecimiento KHI." | Caption de Fig. `ajuste_v6`. Además el profesor **reescribe el caption completo** (versión sin "v6", describiendo regímenes y asíntotas). Advierte sobre presentar $C<0$ como asíntota física. |
| **6.4 — HECHA** | "que es v6, versión 6? si es así es un dato irrelevante para el lector" | Dentro del caption tachado. **Quitar "v6"** de los textos visibles: es nomenclatura interna de versiones, irrelevante para el lector. (Aplica a muchos `_v6` en labels/captions.) |
| **6.5 — REUBIC.** | "así debería ir la grafica anterior en cambio de 3p y 4p, sean consistententes con su formulación y llamado a conceptos" | Caption de Fig. `3v4_v6` ("modelos de 3 y 4 parámetros"). Usar **esta forma** (parámetros) en vez de "3p/4p" de la figura anterior — **consistencia** de nomenclatura entre figuras. |
| **6.6 — HECHA** | "en mi compilación este numero aparece tachado" | Sobre "$\approx 2815$" en el caption de Fig. `3v4_v6` (L148). **Problema de compilación**: el número sale tachado en el PDF del profesor. *(Verificado: en L148 NO hay `\sout` local sobre el número → la causa es externa: probablemente `ulem` interpretando el doble guion `--` / el `\to` o algún `\sout` mal cerrado de un caption previo que se propaga. Requiere compilar para reproducir y aislar.)* |
| 6.7 | "ok aquí justifican y aclaran el valor negativo de $C$" (+ reescritura del párrafo de degeneración $\gamma_0$/$C$) | Párrafo del resultado $C+\gamma_0=1.03$. El profesor **reescribe** la explicación de la anticorrelación $\mathrm{corr}(\gamma_0,C)=-0.997$ (`\sout{Solo la suma...}` → versión propia) y al final **aprueba** ("ok… justifican el valor negativo de C"). Nota mixta: reescritura + visto bueno. |
| 6.8 | "nuevamente no dicen en este capitulo que es AIC anidado ????" | Bullet "Justificación del offset (AIC anidado…)". Reitera 6.1/6.2: **AIC y "anidado" no se han definido** en el capítulo. |
| 6.9 | "podrian decirle al lector que es p???" | Sobre "test de rachas con $p<0.05$". **Definir el $p$-valor** (o el test) para el lector. |
| 6.10 | (Bloque largo) "**Validación fuera de muestra (*hold-out*):** … $\mathrm{RMSE}_{\rm HO}=\sqrt{\frac1{N_{HO}}\sum…}$ … reduce el error de $0.039$ a $0.025$ … mejora ~36% … el offset $C$ no es artefacto…" | **Reescritura completa** del bullet de validación cruzada. Tacha la versión vieja (`\sout{Validación cruzada…}`) y propone una con **la fórmula del RMSE escrita explícitamente** y redacción más formal. *(Ojo: el bloque viene precedido de un ```` ```latex ```` suelto que hay que borrar — artefacto de pegado.)* |
| 6.11 | "En lugar de un umbral abrupto, la idealización procede como una cascada de activación de mecanismos a lo largo de un rango logarítmico amplio en $\sigma$" | Reescritura: cambia "**casi una década**" por "**rango logarítmico amplio**" (`\sout{…casi una década…}`). Matiz: el rango `[1400,7000]` no es exactamente una década. |
| 6.12 | "esto suena a IA" | Caption de tabla `est_v6`: tacha "honesta" en "incertidumbre `\sout{honesta}`". El término **"incertidumbre honesta" suena a redacción de IA**; cambiarlo. |
| 6.13 | "IA" | Misma corrección que 6.12 en la fila `multicolumn` de la tabla ("Incertidumbre `\sout{honesta}` (dispersión inter-método)"). Reemplazar "honesta". |
| 6.14 | "$\Rmst$ es un numero de Reynolds magnético, lo han definido antes, por favor hacer llamdo a esa definición o definirlo en este momento" | Sobre "$S\simeq21\,\Rmst$". **Referenciar o definir $\mathrm{Rm}^*$** (número de Reynolds magnético) en su primer uso aquí. |
| 6.15 | (Bloque largo) "Una demostración concluyente … requieren … esquemas RRMHD de alta resolución, que combinen reconstrucciones espaciales de alto orden, solucionadores de Riemann poco difusivos e integradores temporales … IMEX … reducir la disipación numérica y distinguirla de la física `\parencite{mignone2024}` …" | **Reescritura completa** del párrafo de trabajo futuro sobre el exponente $\alpha\approx1.22$ y *tearing*. Versión más detallada y técnica (menciona explícitamente IMEX, reconstrucción de alto orden). Tacha la anterior. |
| 6.16 | "esta ecuación debería estar numerada y referenciada en los llamados que se hacen con anterioridad en el texto" | Sobre $f_{Vz}=(\Otot-\Omega_z)/\Otot$. **Numerar la ecuación** y referenciarla donde se menciona antes en el texto. |
| 6.17 | "sean rigurosos y no dejen terminos a adivinar $c_s$ que es? obviamente la velocidad del sonido, pero si introducen un simbolo nuevo deben especificarlo" | Sobre la ecuación de Lees–Lin. **Definir $c_s$** en su aparición en el cap. 6. *(Verificado: $c_s$ sí se define en el cap.1, `01_introduction` L25 —"velocidad del sonido térmica del gas"—, pero NO se recuerda aquí. Además coexisten **tres grafías** del mismo símbolo: $c_s$ en el texto, $C_s$ en la tabla L389, y $\mathcal{C}_s$ en el apéndice. Hay que unificar.)* Conecta con 6.20. |
| 6.18 | "los puntos estrella de incompresible y de michaelke no aparecen en la gráfica" | Caption de Fig. `compresible_v6`. **La figura no muestra** los puntos-estrella (validación incompresible y Michalke) que el caption menciona. Corregir figura o caption. |
| 6.19 | "ya lo definieron con anterioridad???" | Caption de tabla `mach_v6`, sobre "$M_{re}$… Mach relativista efectivo de Königl". *(Verificado: la **definición formal con fórmula** ($M_{re}=\frac{v_{sh}}{v_{f\perp}}\sqrt{(1-v_{f\perp}^2)/(1-v_{sh}^2)}$) está en el **apéndice** `07_appendices` L71, no en el cuerpo antes de la tabla; en el cuerpo solo aparece la cota $0<M_{re}<\sqrt2$ en L368.)* Acción: **añadir referencia cruzada al apéndice** (o definirlo en el cuerpo) en su primer uso. |
| 6.20 | "$C_s$ es tambien la velocidad del sonido?, sean consistentes con su notación" | Tabla de velocidades: aparece "$C_s=0.516$" (mayúscula) vs "$c_s$" (minúscula, texto) vs "$\mathcal{C}_s$" (apéndice). **Inconsistencia de notación: tres grafías para la velocidad del sonido** — unificar a una sola. (Mismo problema que 6.17.) |
| 6.21 | "el uso de $\sigma_{KHI}$ puede ser contrproducente pues utilizamos $\sigma$ continuamente para conductividad, aunque en el campo de la KHI se utilice para enstrofía o tasa de crecimiento es mejor mantener nuestra simbología, pues estamos en un area donde $\sigma$ tiene un significado especial" | Sobre $\sigma_{KHI}$ y $\sigma_Z$ (tasas). **Colisión de símbolos:** $\sigma$ ya es la conductividad en todo el capítulo; usar $\sigma_{KHI}/\sigma_Z$ para tasas confunde. Cambiar a la simbología propia ($\hat\omega$, etc.). |
| **6.22 — HECHA** | (Bloque largo) "Comparación de la tasa de crecimiento normalizada del modo primario $\hat\omega=\gamma_{KHI}a/v_{sh}$ … La línea roja indica el valor medido $\hat\omega=0.103$ … rangos RMHD diamagnética y paramagnética … reportados por Pimentel y Lora-Clavijo `\textcite{pimentel-2019}`" | **Reescritura del caption** de Fig. `marcos_v6`. **(!)** *Verificado (L411–423): el profesor NO tachó el caption viejo (dijo "no puedo tachar en los caption"), así que ahora el caption tiene **AMBOS textos juntos** (el nuevo en rojo + el viejo en negro). En el PDF saldría duplicado → hay que **reemplazar**, no solo añadir.* |
| **6.23 — HECHA** | "No se entiende que querian decir con polarización magnetica, el lector puede preguntarse: "¿polarización de qué?, ¿del campo?, ¿de la radiación?, ¿del plasma?" …. no puedo tachar en los caption así que cambienlo por lo que les marco en rojo" | Mismo caption (Fig. `marcos_v6`). **"polarización magnética" es ambiguo** (en el caption viejo: "Las filas de polarización magnética corresponden a Pimentel-2019"). Su reescritura (6.22) ya lo resuelve nombrando "RMHD diamagnética/paramagnética". Al reemplazar el caption viejo por el nuevo, esta nota queda absorbida. |

> Cambios sin nota (ediciones directas): "reconexión magnética `\sout{interfasial}`" (quitar "interfasial"); "el `\sout{proxy}` `\prof{estimador indirecto}` $E_{int}$" y "el `\sout{proxy}` `\prof{estimador}`" (cambiar **"proxy" → "estimador"**); fusión de la línea suelta "(Fig. campC_enstrofia)" con su párrafo.

---

## CAP 7 — Conclusiones (`06_conclusions.tex`) — 1 nota + 4 tachados

| # | Texto literal de la nota | A qué se refiere / qué pide |
|---|---|---|
| 7.1 | "esto le corresponde al evaluador decidir si se cumplio o no con el objetivo" | Tacha las **cuatro** declaraciones `\sout{\emph{[Objetivo cumplido.]}}` (objetivos 1, 2, 3 y 4). Postura del director: **no autoadjudicarse el cumplimiento** de los objetivos; lo decide el jurado/evaluador. Quitar las cuatro. |
| 7.2 | "de integración temporal" | Bullet de trabajo futuro: "Esquemas `\prof{de integración temporal}` de orden aún mayor". **Precisar** que son esquemas *de integración temporal* (no de reconstrucción espacial), p. ej. cuarto orden, `mignone2024`. |

---

## APÉNDICE / CAP 8 — Agradecimientos y cómputo (`agradecimientos_cluster.tex`) — 1 nota

| # | Texto literal de la nota | A qué se refiere / qué pide |
|---|---|---|
| 8.1 | "deberian separar esto en dos capitulos por un lado los recursos computacionales y por otro los agradecimientos, donde obviamente deberían agradecer al profesor por facilitarles el codigo **cueva** y su invaluable orientación ;), agradecer a sus familiares y compañeros y tambien a quien les ha dado acceso al servidor (universidad o investigador), tambien una agradecimientoa la UD por la formación que les ha brindado …. etc" | **Reestructurar:** separar en dos partes —(a) recursos computacionales y (b) agradecimientos—. Y **ampliar los agradecimientos**: al director (por el código Cueva y la orientación), familiares, compañeros, quien dio acceso al servidor, y a la Universidad Distrital. |

---

## Resumen por tipo de nota

- **Falta definir símbolo/concepto:** 4.1·4.5 (carga $q$/jacobiano), 5.1 (CUEVA), 5.3 ($W$ Lorentz), 6.1·6.8 (AIC/BIC/anidado), 6.9 ($p$), 6.14 ($\mathrm{Rm}^*$), 6.17·6.20 ($c_s$/$C_s$), 6.19 ($M_{re}$).
- **Consistencia de notación/nombres:** 4.6 ("Cueva" sin "el"), 5.3 ($\Gamma$ vs $W$), 6.4 ("v6"), 6.5 (3p/4p), 6.20 ($C_s$), 6.21 ($\sigma_{KHI}$).
- **Falta referencia:** 4.2.
- **Redacción/estilo (anglicismos, "suena a IA"):** 4.3 (interfasiales), 4.8·4.9 (deprimida), 6.11 (década), 6.12·6.13 (honesta), 6.23 (polarización), "proxy"→"estimador".
- **Figuras/captions:** 6.3, 6.5, 6.6 (tachado en PDF), 6.18 (faltan puntos), 6.22·6.23 (reescritura), 6.16 (numerar ecuación).
- **Reescrituras completas propuestas:** 4.4 (título), 5.2 ($B_z$), 6.7, 6.10 (hold-out+RMSE), 6.15 (trabajo futuro), 6.22 (caption marcos).
- **Contenido/física a revisar:** 4.1 (jacobiano 14×14), 6.3 ($C<0$).
- **Postura editorial:** 7.1 (quitar "[Objetivo cumplido]" ×4).
- **Estructura:** 8.1 (separar capítulo + ampliar agradecimientos).
- **Artefacto a limpiar:** ```` ```latex ```` suelto antes de la nota 6.10.

---

## Verificación contra el texto fuente (relectura, 29-jun)

Se releyó el `.tex` actual (HEAD `e45cf38`) en cada zona con nota. Resultado:

1. **Conteo confirmado:** 38 notas `\prof` (cap4=9, setup=3, cap6/resultados=23, cap7=2, agradec.=1) + `\sout` adicionales sin nota. Capítulos 1–3 intactos.
2. **Tres problemas que rompen/ensucian la compilación** (no son "opinión" del profesor, son fallas materiales):
   - **L161** (`05_results_discussion`): hay un ```` ```latex ```` (fence de Markdown) pegado dentro del `.tex`. LaTeX lo imprimiría como texto o fallaría. **Borrar.**
   - **L411–423** (caption fig. `marcos_v6`): el caption nuevo del profesor (rojo) quedó **junto** al caption viejo (negro), porque él no pudo tachar dentro del `\caption`. Saldría **duplicado**. **Reemplazar el viejo por el nuevo.**
   - **L148** (caption fig. `3v4_v6`): el profesor ve "$\approx2815$" tachado en su PDF. No hay `\sout` local → propagación de `ulem` desde otro punto. **Reproducir compilando.**
3. **Notas que eran preguntas — ya respondidas con el fuente:**
   - **6.19** ($M_{re}$ "¿ya definido?"): sí, pero la fórmula está en el **apéndice** `07_appendices` L71; en el cuerpo solo está la cota. Falta el cross-ref.
   - **6.17 / 6.20** ($c_s$ / $C_s$): $c_s$ se define en cap.1 L25, pero el símbolo aparece con **tres grafías** ($c_s$, $C_s$, $\mathcal{C}_s$). Unificar.
4. **Notas "de fondo" (física) confirmadas:** 4.1+4.5 (jacobiano 14×14 por falta de la carga $q$ en las primitivas) y 5.3 ($\Gamma$ usado a la vez para índice adiabático y Lorentz → usar $W$) son las que más se propagan por el documento.
5. **El profesor a veces aprueba:** la nota 6.7 termina en "ok aquí justifican y aclaran el valor negativo de $C$" — es un **visto bueno** a la frase final del párrafo (no una corrección).

---

## Verificación DIRIGIDA de los puntos de fondo (29-jun)

### Punto 1 — Jacobiano 14×14 (notas 4.1 + 4.5): **el profesor tiene razón. CONFIRMADO.**

El cap. 2 (`02_rrmhd_theory`) respalda los 14 grados de libertad del sistema aumentado Maxwell-GLM resistivo:
- **Dos** escalares de limpieza GLM: $\Phi$ (eléctrico, ley de Gauss, §"Campo Auxiliar Eléctrico $\Phi$" L243) y $\Psi$ (magnético, $\nabla\!\cdot\!\mathbf B$, §"Campo Auxiliar Magnético $\Psi$" L267).
- La **densidad de carga** $\rho_q$ es variable del sistema: $J^\mu=(\rho_q,\mathbf J)$ (L125) con conservación $\partial_\nu J^\nu=0$ (L136).

Conteo de variables conservadas: $D$(1) $+\,S^i$(3) $+\,\tau$(1) $+\,B^i$(3) $+\,E^i$(3) $+\,\Phi$(1) $+\,\Psi$(1) $+\,\rho_q$(1) $=\mathbf{14}$.
El cap. 4 actualmente dice **13×13** y omite $\rho_q$. **Es un error real**, no cosmético, y se propaga a 3 sitios del cap. 4:
1. L65: "$\mathbf A_{13\times13}$" → 14×14.  2. L65: "comprende **13** autovalores" → recontar.  3. L159: vector de primitivas (el profesor ya le añadió $q$). *Acción: verificar contra la formulación/código y corregir los tres de forma consistente.*

### Punto 2 — Notación $\Gamma$ Lorentz vs índice adiabático (nota 5.3): **colisión real. CONFIRMADO.**

$\Gamma$ aparece **~38 veces** y se usa con los **dos** significados:
- **Factor de Lorentz:** cap. 4 L159/L161 ("factor de Lorentz inercial $\Gamma=(1-\mathbf v^2)^{-1/2}$"), cap. 2 L409/L494 ("factores de Lorentz $\Gamma\gg1$").
- **Índice adiabático:** `setup_exp` ($\Gamma=4/3$), cap. 4 ($\Gamma_{\rm ad}$, gas politrópico), apéndice ($h=1+\Gamma/(\Gamma-1)\,p/\rho$).

Adoptar $W$ para Lorentz (formulación de Valencia) es un **cambio transversal**: toca sobre todo el cap. 2 y la sección de recuperación de primitivas del cap. 4 (la "cuártica en el factor de Lorentz" pasaría a estar en $W$). *Cuidado: NO cambiar los $\Gamma$ que son índice adiabático.* No es un cambio de 3 líneas.

### Punto 3 — "Faltan definiciones" (6.1, 6.8, 6.9, 6.14, 6.17, 6.19): **casi todas YA existen — falta el cross-ref.**

El profesor leyó el cuerpo del cap. 6 sin el apéndice/glosario delante. Casi todo está definido; la acción correcta es **añadir `\ref`/`\cref`**, no redactar definiciones nuevas:

| Nota | Término | ¿Definido? ¿Dónde? | Acción |
|---|---|---|---|
| 6.1 | AIC | Sí — apéndice §`ap:est:aic` (L210-213) + fórmula L129 | cross-ref |
| 6.1 | BIC | Sí — apéndice L219 ("criterio bayesiano de Schwarz, $\mathrm{AIC}$ con penalización $\kappa\ln N$") | cross-ref |
| 6.8 | comparación "anidada" | Sí — apéndice L219 ("anidada justa, mismo conjunto $\sigma\ge1600$") | cross-ref |
| 6.9 | $p$ / test de rachas | Sí — apéndice §`ap:est:rachas` (L222-225), define el estadístico y el $p$ | cross-ref |
| 6.14 | $\mathrm{Rm}^*$ | Sí — **glosario** `00_preliminares` L24 ($\vsh\,\akh\,\sigma$) | cross-ref |
| 6.19 | $M_{re}$ (Königl) | Sí — apéndice `07_appendices` L71 (fórmula completa) | cross-ref |
| 6.17/6.20 | $c_s$ | Sí — cap. 1 L25; pero **3 grafías** ($c_s$, $C_s$, $\mathcal C_s$) | unificar símbolo + cross-ref |

→ **6 de las 23 notas del cap. 6 se resuelven con referencias cruzadas** (trabajo mecánico, bajo riesgo), no con redacción nueva.

### Punto 4 — Cambios sin `\prof` (ediciones directas): confirmados y menores.
Cap. 4: "introduce al sistema **en** un régimen" (preposición). Cap. 6: "reconexión `\sout{interfasial}`"; **"proxy" → "estimador"** (×2, L623); fusión de la línea suelta "(Fig. campC)". Ninguno cambia el contenido.

### Conclusión de la verificación dirigida
- **2 notas de fondo reales que sí dan trabajo:** jacobiano 14×14 (cap. 4, verificar y propagar) y $\Gamma\to W$ (cap. 2 + cap. 4, transversal).
- **6 notas que parecían "redactar definición" → en realidad son cross-refs** (rápidas).
- **3 fallas de compilación** que hay que tocar igual (```` ```latex ````, caption duplicado, número tachado).
- El resto ($\approx$27): estilo, captions y consistencia, ya claras.
