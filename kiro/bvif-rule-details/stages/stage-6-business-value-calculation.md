# Etapa 6 — Cálculo del valor de negocio

**Propósito**: Consolidar la información recolectada en las etapas previas para calcular los beneficios estimados de la iniciativa.

> **Convención de rutas**: `<INITIATIVE_FOLDER>` se refiere a la carpeta por iniciativa bajo `bvif-docs/` (p. ej., `bvif-docs/01-customer-churn-predictor-202604`). Consulta `common/process-overview.md` → "Convención de rutas: carpeta por iniciativa".

## Persona del agente

Adopta la persona definida en `stages/agents/stage-6-business-value-calculation-agent.md` (Analizador de Valor de Métricas de IA). Ese archivo es la fuente de verdad para el esquema de la tabla de salida (9 atributos: número secuencial, categoría, nombre de la métrica, definición, explicación, desempeño histórico, % de mejora esperada, montos en moneda — mejora/anualizado/una sola vez, y la explicación de la inferencia), la cadencia de aclaración de una pregunta a la vez, el tono y el requisito de detallar los cálculos financieros para la revisión de calidad por humanos. No repitas esas especificaciones aquí.

## Prerrequisitos
- Etapa 5 completada y aprobada
- Documento de recolección de datos disponible con líneas base, tendencias, benchmarks y objetivos

## Paso 1: Carga los artefactos previos

Lee:
- `<INITIATIVE_FOLDER>/05-data-collection/data-collection.md`
- `<INITIATIVE_FOLDER>/04-metrics-adjustment/final-metrics-list.md`
- `<INITIATIVE_FOLDER>/02-business-value-mapping/business-value-mapping.md`
- `<INITIATIVE_FOLDER>/01-initiative-definition/initiative-definition.md`

## Paso 2: Clasifica cada métrica

Para cada métrica, determina:

| Tipo | Descripción |
|---|---|
| **Financiero** | Beneficios que pueden expresarse como un valor monetario anualizado |
| **No financiero** | Mejoras cuantificables que no se traducen directamente a dinero |

## Paso 3: Calcula el valor de negocio por métrica

Aplica el esquema de salida de 9 atributos de la persona del agente a cada métrica de la lista final. Además de las filas por métrica, agrega las siguientes notas donde aplique:

- Si el valor financiero de una métrica ya está capturado en otra métrica (ver Paso 4), márcalo en consecuencia y referencia la métrica que lo lleva.
- Muestra toda la aritmética de cada valor financiero para que los humanos puedan validar el cálculo.

## Paso 4: Verifica el doble conteo

**CRÍTICO**: Múltiples métricas pueden capturar el mismo impacto subyacente desde diferentes perspectivas.

- Identifica las métricas que miden el mismo evento o resultado
- Indica claramente qué métrica lleva el valor financiero
- Marca las otras métricas relacionadas como "Captured in Metric [N]" para evitar el doble conteo
- Al sumar los totales, usa solo la métrica que mejor representa el impacto financiero

## Paso 5: Maneja la comparabilidad de categorías

- **Aumentar la eficiencia operativa**: Produce reducciones de costos que afectan la línea inferior
- **Aumentar los ingresos**: Refleja valor de línea superior — requiere un ajuste de margen de contribución antes de compararlo con los ahorros operativos
- **NO mezcles cifras** de diferentes categorías sin ajuste
- Usa el criterio: algunas métricas de la categoría de ingresos pueden producir beneficios de línea inferior (p. ej., penalizaciones evitadas)

## Paso 6: Produce la tabla resumen

```markdown
# Stage 6 Summary Table

| # | Metric | Expected Improvement | Expected Improvement ($) | Annualized Figure ($) |
|---|---|---|---|---|
| 1 | [Name] | [Description] | $[amount]/[period] | $[amount]/year |
| 2 | [Name] | [Description] | Captured in Metric [N] | See Metric [N] |
| ... | ... | ... | ... | ... |
```

## Paso 7: Guarda el artefacto

Guarda en `<INITIATIVE_FOLDER>/06-business-value-calculation/business-value-calculation.md`.

## Paso 8: Solicita la aprobación mediante un archivo

Crea un archivo de aprobación numerado secuencialmente dentro de `<INITIATIVE_FOLDER>/06-business-value-calculation/` (p. ej., `NN-business-value-calculation-approval.md` donde `NN` es el siguiente prefijo no usado). Usa esta estructura:

```markdown
# Stage 6 — Business Value Calculation Approval

## Qué estás aprobando
Las cifras de valor de negocio por métrica y el resumen que alimenta el informe final. Cada métrica se ha clasificado como:

- **Financiera** — beneficios expresables como un valor monetario anualizado (la cifra principal de dólares/año).
- **No financiera** — mejoras cuantificables que no se traducen directamente a dinero (p. ej., mejora del puntaje de satisfacción del cliente, reducción de la tasa de defectos).

Se han aplicado dos verificaciones transversales, y debes prestarles especial atención:

- **Verificación de doble conteo** — Múltiples métricas pueden capturar fácilmente el mismo impacto subyacente desde distintos ángulos. Donde existe superposición, una métrica lleva el valor financiero y las otras se marcan como "Captured in Metric [N]" para que no se sumen dos veces.
- **Comparabilidad de categorías** — Los ahorros de Eficiencia Operativa impactan la línea inferior directamente, pero las cifras de Aumentar los Ingresos son de línea superior y necesitan un ajuste de margen de contribución antes de sumarse a los ahorros. Cualquier ajuste entre categorías se señala.

Se muestra toda la aritmética de cada valor financiero para que puedas verificar el cálculo. Aprobar fija las cifras que pasan directamente al informe ejecutivo de la Etapa 7.

**Notas clave para esta ejecución**:
- Verificación de doble conteo: [lista cualquier métrica donde se identificó superposición]
- Comparabilidad de categorías: [anota cualquier ajuste entre categorías realizado]

## Dónde leer el artefacto completo
`<INITIATIVE_FOLDER>/06-business-value-calculation/business-value-calculation.md`

---

## Pregunta 1
¿Apruebas el cálculo del valor de negocio?

A) Aprobar y continuar a la Etapa 7 — Documentación de resultados finales
B) Solicitar cambios (por favor describe después de la etiqueta [Answer]: abajo)
X) Otro (por favor describe después de la etiqueta [Answer]: abajo)

[Answer]:
```

Anuncia la ruta del archivo en el chat y **NO PROCEDAS** hasta que el usuario señale que terminó y la respuesta se resuelva como Aprobar.

Si se necesitan preguntas aclaratorias antes de producir el cálculo, crea un archivo de preguntas numerado secuencialmente en la misma carpeta (p. ej., `01-business-value-calculation-questions.md`) siguiendo `common/question-format-guide.md`.

## Paso 9: Actualiza el estado

Después de la aprobación, actualiza `<INITIATIVE_FOLDER>/bvif-state.md`:
- Marca la Etapa 6 como `[x]`
- Establece la etapa actual como "Stage 7 — Final Results Documentation"

Registra la aprobación en `<INITIATIVE_FOLDER>/audit.md`.
