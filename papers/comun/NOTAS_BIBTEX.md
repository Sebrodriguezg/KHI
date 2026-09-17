# Bibliografía: de `biblatex/biber` (monografía) a `natbib/bibtex` (artículo)

## El problema

La monografía usa:

```latex
\usepackage[backend=biber, style=numeric-comp, sorting=anyt]{biblatex}
\addbibresource{references.bib}
...
\parencite{komissarov-2007}   \textcite{mizuno2013}
```

MNRAS y OJAp usan **BibTeX clásico + natbib**, estilo **autor–año**:

```latex
\bibliographystyle{mnras}   % o el .bst de ApJ para OJAp
\bibliography{references}
...
\citep{komissarov2007}      \citet{mizuno2013}
```

## Tabla de conversión de comandos

| biblatex (monografía) | natbib (artículo) |
|---|---|
| `\parencite{x}` | `\citep{x}` |
| `\textcite{x}` | `\citet{x}` |
| `\cite{x}` | `\citep{x}` |
| `\parencite[p.~5]{x}` | `\citep[p.~5]{x}` |
| `\parencite{a,b}` | `\citep{a,b}` |
| `\printbibliography` | `\bibliographystyle{mnras}` + `\bibliography{references}` |

Conversión masiva (revisar el resultado a mano después):

```bash
sed -i 's/\\parencite/\\citep/g; s/\\textcite/\\citet/g' main.tex
```

## Qué hacer con `references.bib`

`comun/references.bib` es **copia literal** de la monografía (83 entradas:
58 `@article`, 22 `@book`, 2 `@inproceedings`, con 2 claves en mayúsculas).
Antes de usarlo:

1. **BibTeX trata las claves como *case-insensitive***: `@ARTICLE{X}` y
   `@article{x}` chocan. Ya hubo duplicados así en este proyecto
   (`Misner1973`/`Schutz2009`, `Lee2004`). **Normalizar a minúsculas y verificar.**
2. **Campos que BibTeX ignora y biblatex no**: `date` → convertir a `year`;
   `journaltitle` → `journal`; `location` → `address`. Revisar entrada por entrada.
3. **Abreviaturas de revista**: MNRAS quiere `MNRAS`, `ApJ`, `A&A`…
   `mnras.cls` define macros (`\mnras`, `\apj`, `\aap`, …) utilizables en el campo
   `journal`. Alternativa: escribir la abreviatura literal.
4. **Regla de los 8 autores**: `mnras.bst` la aplica sola **si el campo `author`
   tiene todos los autores**. No abreviar a mano en el `.bib`.
5. **Verificar todo contra ADS**: lo más rápido es **reexportar cada entrada desde
   NASA ADS en formato BibTeX** en lugar de arreglar la vieja. ADS produce
   entradas limpias, con `doi`, `adsurl` y las abreviaturas correctas.
   👉 **Recomendación: `references.bib` del artículo se construye NUEVO desde ADS**,
   usando el de la monografía solo como lista de qué buscar.

## Comprobación rápida

```bash
cd papers/mnras && ./build.sh          # pdflatex + bibtex + 2×pdflatex
grep -i "warning--" main.blg           # entradas incompletas
grep -c "Citation.*undefined" main.log # citas rotas
```
