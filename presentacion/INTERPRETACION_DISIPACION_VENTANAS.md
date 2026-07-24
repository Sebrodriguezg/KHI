# Interpretación de la disipación resistiva por ventanas (panel b) — vs. comentario del profesor

> Figura: `figures/fig_global_campos_ventanas_slide.pdf`, panel **(b)**.
> Lámina del deck: "Variables Globales: la Firma Electromagnética de σ" (Objetivo 3).
> Script generador: `scripts_slide/gen_disipacion_ventanas_slide.py`.
> Docs relacionados: `PLAN_CORRECCIONES_RONDA2.md` §11 · `COSAS_POR_REPASAR.md` §4.

---

## 1. El comentario del profesor (ensayo 22-jul-2026)

Origen textual en los `.md` del repo:

- **`PLAN_CORRECCIONES_RONDA2.md`, punto 11** ("Disipación resistiva acumulada"):
  > "REHACER el análisis con la integral en CUATRO ventanas: (1) ANTES (transiente
  > numérico), (2) fase LINEAL, (3) zona TURBULENTA (post-pico), (4) TODA la serie.
  > Cuatro curvas vs σ para comparar los valores entre sí."

- **`COSAS_POR_REPASAR.md` §4**: registra la física a defender y los valores medidos.

En una frase: **el profe no quería un solo número de disipación, sino la disipación
descompuesta por fase dinámica**, para poder comparar cuánto calor de Ohm se genera en
cada régimen y contra qué crece con σ.

---

## 2. Qué muestra el panel (b) — la respuesta a ese comentario

Calor de Ohm acumulado **∫∫ ηJ² dA dt** (η = 1/σ) evaluado por simulación en 4 ventanas,
graficado contra σ:

| Ventana | Intervalo temporal | Qué captura |
|---|---|---|
| numérica | `[0, 2.4)` | transiente de arranque + rampa pre-lineal — **sin física de ajuste** |
| lineal | `[2.4, 3.4]` | ventana canónica de ajuste de γ (la misma del pipeline) |
| turbulenta | `(t_peak, 15]` | maraña de láminas de corriente post-pico |
| total | `[0, 15]` | balance completo (horizonte común t ≤ 15) |

**Valores de referencia (campaña magnética, del pipeline):**

| σ | numérica | lineal | turbulenta | total | turb/lineal |
|---|---|---|---|---|---|
| 6000 | 0.033 | 0.062 | 1.60 | 1.90 | **26×** |
| 10⁴ | 0.023 | 0.059 | 0.94 | 1.21 | **16×** |

**Lectura física (lo que se dice en voz alta):**

1. **La ventana turbulenta domina el presupuesto disipativo** (16–26× la lineal): casi
   todo el calor de Ohm se genera DESPUÉS del pico, en la turbulencia de pequeña escala.
   La fase lineal casi no disipa — coherente con que ahí el modo apenas crece.
2. **El total crece del régimen resistivo hacia la transición** y alcanza su máximo cerca
   de σ ~ 2000–3000; en el ideal se mantiene alto (≈1–2). No colapsa a cero aunque
   η = 1/σ → 0, **porque las láminas de corriente se intensifican más rápido de lo que η
   cae** (J² sube más rápido de lo que 1/σ baja).
3. **La ventana numérica DECRECE con σ**: es difusión del transiente inicial; a σ baja
   (η grande) ese arranque disipa más. Es la única ventana sin contenido físico → sirve
   de control: su magnitud es siempre pequeña frente a la turbulenta.

---

## 3. El punto donde NOS APARTAMOS del comentario literal (y por qué)

El profe habló de la disipación como **E·J**. **Nosotros graficamos ηJ², no E·J crudo.**
Es una decisión deliberada, no un descuido:

- **E·J cambia de signo en la fase turbulenta**: hay intercambio *reversible* de energía
  entre campo y fluido (dínamo ↔ rebote de la tensión). Su integral sufre cancelaciones
  y **no representa el calor efectivamente disipado**.
- **ηJ² es positivo-definido**: es la disipación *irreversible* (calentamiento óhmico
  real). Es exactamente la cantidad que responde a la pregunta del profe —"cuánto calor
  se genera por ventana"— sin el artefacto de signo.

En la sustentación conviene **anticipar la pregunta**: "graficamos ηJ² y no E·J porque
E·J cambia de signo en turbulencia (intercambio reversible) y su integral se cancela;
ηJ² es la disipación irreversible, que es lo que el balance térmico pide."

---

## 4. Nota sobre las líneas conectadas (cambio de ronda 3)

Las curvas **turbulenta** y **total** quedaban con huecos: los runs truncados (que no
alcanzan t = 15) daban `NaN` en esas dos ventanas. En la ronda 3 se enmascaran los `NaN`
para que la línea **conecte los puntos válidos** (`gen_disipacion_ventanas_slide.py`).

⚠️ **Matiz honesto que hay que tener presente:** la línea ahora *interpola visualmente*
sobre los σ cuyos runs se truncaron; los **marcadores** siguen indicando dónde hay dato
medido real. Si el profe pregunta por los huecos, la respuesta es: "las ventanas
turbulenta y total exigen llegar al horizonte común t = 15; algunos runs resistivos se
detuvieron antes, así que esos σ no tienen valor en esas dos ventanas — la línea une los
que sí; los marcadores marcan el dato real." (Las ventanas numérica y lineal no tienen
huecos: se evalúan sobre [0, 3.4], que todos los runs alcanzan.)

---

## 5. Checklist para la defensa de esta lámina

- [ ] Abrir con la descomposición por ventana (no con el número total).
- [ ] Decir el cociente turb/lineal (26× / 16×) — es el titular.
- [ ] Explicar por qué el total NO colapsa hacia el ideal (J² vs 1/σ).
- [ ] Tener lista la justificación ηJ² vs E·J (signo / reversibilidad).
- [ ] Tener lista la explicación de los huecos → líneas (runs truncados a t=15).
