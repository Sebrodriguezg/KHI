# Declaración de uso de IA generativa — borrador

Las dos revistas lo exigen, con matices distintos.

## MNRAS

> "Use of AI tools (content generation, images, code, data processing,
> translation) must be disclosed in **cover letter** and **Methods/Acknowledgements**."

## OJAp (más estricta en lo que pide demostrar)

> Sin prohibición general, **pero**:
> 1. declararlo **en los agradecimientos**;
> 2. si se usó IA para **cualquier cálculo, análisis o visualización de datos**,
>    incluir **una descripción de los pasos dados para probar y validar** esos métodos;
> 3. **rechazo** si hay evidencia directa: **referencias alucinadas** o *prompts*
>    en el texto.

## Qué hay que determinar honestamente (antes de redactar)

- [ ] ¿Se usó asistencia de IA para **redactar o traducir** texto del artículo?
- [ ] ¿Para **escribir o depurar scripts** de análisis o de figuras?
- [ ] ¿Para **producir alguna cifra o resultado**? (Si la respuesta es sí,
      OJAp exige contar cómo se validó.)
- [ ] ¿Para revisión bibliográfica? ⚠️ **Verificar UNA POR UNA que todas las
      referencias existen** (DOI/bibcode ADS). Una referencia inventada es causal
      de rechazo en OJAp.

## Plantilla (ajustar a lo que realmente ocurrió)

> **Acknowledgements** (fragmento)
>
> Generative AI tools (Claude, Anthropic) were used to assist with LaTeX
> formatting, code refactoring of the analysis and plotting scripts, and language
> editing of the manuscript. All physical results, numerical simulations and their
> interpretation are the authors' own. Analysis scripts produced with AI assistance
> were verified against independent manual calculations on a subset of the runs,
> and every figure was checked against the raw simulation output. All references
> were verified against NASA ADS.

⚠️ **La última frase solo se escribe si es verdad.** Es exactamente lo que OJAp
pide demostrar, y es una afirmación verificable.
