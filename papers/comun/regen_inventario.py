#!/usr/bin/env python3
"""Regenera comun/inventario_figuras_auto.tsv a partir de monografia/sections/*.tex.

Uso:  python3 papers/comun/regen_inventario.py     (desde la raiz del repo)
Salida: papers/comun/inventario_figuras_auto.tsv  (archivo_tex, label, imagenes, caption)

Detecta tambien las imagenes referenciadas que no existen en disco (p. ej. lineas
comentadas), y las lista al final por consola.
"""
import glob
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SECCIONES = os.path.join(RAIZ, 'monografia', 'sections', '*.tex')
SALIDA = os.path.join(RAIZ, 'papers', 'comun', 'inventario_figuras_auto.tsv')
EXTS = ('.pdf', '.png', '.eps', '.jpg')


def caption_de(bloque):
    """Extrae el argumento de \\caption{} respetando llaves anidadas."""
    m = re.search(r'\\caption\{', bloque)
    if not m:
        return ''
    i, prof, j = m.end(), 1, m.end()
    while j < len(bloque) and prof:
        if bloque[j] == '{':
            prof += 1
        elif bloque[j] == '}':
            prof -= 1
        j += 1
    return re.sub(r'\s+', ' ', bloque[i:j - 1])


def main():
    filas, faltantes = [], []
    for ruta in sorted(glob.glob(SECCIONES)):
        texto = open(ruta, encoding='utf-8', errors='replace').read()
        for m in re.finditer(r'\\begin\{figure\*?\}(.*?)\\end\{figure\*?\}', texto, re.S):
            bloque = m.group(1)
            imgs = re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', bloque)
            lab = re.search(r'\\label\{([^}]+)\}', bloque)
            filas.append((os.path.basename(ruta), lab.group(1) if lab else '-',
                          '; '.join(imgs), caption_de(bloque)))
            for img in imgs:
                p = os.path.join(RAIZ, 'monografia', img)
                if not (os.path.exists(p) or any(os.path.exists(p + e) for e in EXTS)):
                    faltantes.append(img)

    with open(SALIDA, 'w', encoding='utf-8') as o:
        o.write('archivo_tex\tlabel\timagenes\tcaption\n')
        for fila in filas:
            o.write('\t'.join(fila) + '\n')

    print(f'{len(filas)} entornos figure -> {SALIDA}')
    if faltantes:
        print('Imagenes referenciadas que no existen en disco '
              '(normalmente lineas comentadas):')
        for img in sorted(set(faltantes)):
            print('  -', img)


if __name__ == '__main__':
    main()
