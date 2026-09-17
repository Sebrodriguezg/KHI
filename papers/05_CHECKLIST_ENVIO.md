# Checklist de envío

## A. Antes de escribir (decisiones bloqueantes)

- [ ] **Revista elegida** (MNRAS / OJAp) → `01_COMPARATIVA_Y_ESTRATEGIA.md`
- [ ] **¿Hay waiver / Read&Publish para el APC de MNRAS?** Verificado con OUP y con
      la biblioteca de la UD
- [ ] **Uno o dos artículos** y alcance cerrado
- [ ] **Lista de autores y orden** acordada por escrito (Bryan, Sebastián,
      Sergio Miranda-Aranguren). ¿Alguien más del grupo CoCoA?
      ⚠️ Ver también la postulación a Distinción Meritoria: coautoría y conflictos
- [ ] **Autor de correspondencia** designado (con e-mail institucional estable)
- [ ] **ORCID** de cada autor creado y a la mano
- [ ] **Permiso del director** para publicar resultados del código *Cueva*, y forma
      correcta de citarlo
- [ ] **Convergencia de malla**: ¿se corre 1024×512 antes de enviar? (ver
      `02_PLAN_EXTRACCION.md` §7.5)

## B. Contenido del manuscrito

- [ ] Título informativo, sin acrónimos oscuros
- [ ] Abstract **≤ 250 palabras**, **un solo párrafo**, con objetivos + métodos +
      resultados nuevos y las cifras clave (1,03 ± 0,05; 8 %; [1400, 7000]; σ^1,22)
- [ ] **1–6 palabras clave de la lista oficial MNRAS**. Candidatas:
      `instabilities`, `magnetic reconnection`, `MHD`, `plasmas`,
      `relativistic processes`, `methods: numerical`
      (verificar contra el PDF oficial de keywords antes de enviar)
- [ ] Secciones numeradas: **1 Introduction … última Conclusions**
- [ ] Todas las figuras y tablas **citadas en el texto**, en orden
- [ ] Ecuaciones numeradas
- [ ] **Data availability** tras Acknowledgements → `comun/DATA_AVAILABILITY.md`
- [ ] **Declaración de uso de IA** → `comun/DECLARACION_IA.md`
- [ ] Acknowledgements: financiación, clúster/recursos de cómputo, software
      (numpy, scipy, matplotlib…), personas
- [ ] **Software citado en las referencias** con versión y DOI/ASCL (FORCE11)
- [ ] Mención de la tesis de origen (si el repositorio de la UD la publica, **citarla**)

## C. Formato (MNRAS)

- [ ] Compila con `mnras.cls` (`\documentclass[fleqn,usenatbib]{mnras}`)
- [ ] `\pdfminorversion=5` en el preámbulo
- [ ] Bibliografía con `mnras.bst` + `natbib` (Harvard autor–año)
- [ ] ≤ 8 autores por referencia → todos; > 8 → primer autor + et al.
- [ ] Tablas **sin líneas verticales**, solo horizontales (`booktabs`)
- [ ] Tabla larga (44 filas) → 5–10 filas de muestra + completa en suplementario
- [ ] Figuras: vectorial PDF/EPS, ≥300 ppi el raster, líneas ≥0,3 pt, fuentes ≥8 pt
      al tamaño final, ejes con unidades, sin rojo–verde
- [ ] **Alt text** bajo cada leyenda
- [ ] Unidades en redonda con `\,`; `km\,s$^{-1}$`; `per cent` en texto
- [ ] Vectores en negrita cursiva; `d`, `e`, `i` y trigonométricas en redonda
- [ ] Inglés **británico** consistente (`04_ESTILO_INGLES.md`)
- [ ] Páginas numeradas; PDF final **≤ 10 MB**

## D. Formato (OJAp)

- [ ] Compila con `openjournal.cls`
- [ ] Artículo **subido a arXiv con licencia CC-BY**
- [ ] Categoría primaria `astro-ph.HE`; cross-list `astro-ph.IM`
      (y opcionalmente `physics.plasm-ph`)
- [ ] arXiv ID a la mano para el formulario de Scholastica
- [ ] **Declaración de IA en los agradecimientos** (+ validación de métodos si se
      usó IA para cálculo/análisis/visualización)
- [ ] Texto revisado a conciencia: **no hay copy-editing**
- [ ] El envío lo hace **alguien de la lista de autores**

## E. Paquete de envío (MNRAS / ScholarOne)

- [ ] PDF único con figuras y tablas **embebidas**
- [ ] **Cover letter** → `comun/COVER_LETTER_MNRAS.md`
      (sin resumir resultados, **sin mencionar el waiver**)
- [ ] Material suplementario (tabla canónica completa en `.txt` legible por
      máquina; collages de densidad; vídeos `.mp4` si aplica)
- [ ] arXiv ID declarado, si ya está subido
- [ ] Marcar **"yes" en premio estudiantil** + declaración de contribución
      estudiantil (Bryan y Sebastián son estudiantes de pregrado)
- [ ] Fuentes de financiación declaradas en el formulario
- [ ] Conflictos de interés declarados
- [ ] Sugerir / excluir árbitros si aplica (con justificación en la carta)

## F. Después del envío

- [ ] Subir/actualizar el preprint en arXiv
- [ ] Guardar el ID del manuscrito
- [ ] Al aceptar: actualizar arXiv con el DOI; depositar en el repositorio
      institucional de la UD; actualizar el CV y la postulación a Distinción
      Meritoria
