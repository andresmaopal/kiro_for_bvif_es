# Etapa 7 — Documentación de resultados finales

**Propósito**: Producir un documento consolidado que resuma el valor de negocio de la iniciativa, listo para la toma de decisiones ejecutiva.

> **Convención de rutas**: `<INITIATIVE_FOLDER>` se refiere a la carpeta por iniciativa bajo `bvif-docs/` (p. ej., `bvif-docs/01-customer-churn-predictor-202604`). Consulta `common/process-overview.md` → "Convención de rutas: carpeta por iniciativa".

## Prerrequisitos
- Etapa 6 completada y aprobada
- Documento de cálculo del valor de negocio disponible

## Paso 1: Carga todos los artefactos previos

Lee:
- `<INITIATIVE_FOLDER>/00-session-setup/session-context.md`
- `<INITIATIVE_FOLDER>/01-initiative-definition/initiative-definition.md`
- `<INITIATIVE_FOLDER>/02-business-value-mapping/business-value-mapping.md`
- `<INITIATIVE_FOLDER>/04-metrics-adjustment/final-metrics-list.md`
- `<INITIATIVE_FOLDER>/06-business-value-calculation/business-value-calculation.md`

## Paso 2: Produce el documento de resultados finales

Estructura el documento de la siguiente manera:

```markdown
# [Customer Name] — [Initiative Name]: Resumen de Valor de Negocio

## Resumen ejecutivo
[Visión general de 2-3 párrafos de la iniciativa, el enfoque de evaluación y la cifra financiera principal]

## Valor de negocio anual total cuantificado

| Impulsor de valor de negocio | Valor anualizado |
|---|---|
| [Driver 1] | $[amount]/año |
| [Driver 2] | $[amount]/año |
| ... | ... |
| **Total** | **~$[total]/año** |

## Tabla consolidada de métricas

Esta es la fuente única de verdad para el equipo que **implementará, rastreará y reportará** esta iniciativa. Cada métrica por la que se juzgará la iniciativa aparece exactamente una vez. Las métricas marcadas por doble conteo (cuyo valor financiero se captura en otro lugar) permanecen en la tabla — aún se rastrean para la visibilidad operativa — pero llevan "Captured in Metric [N]" en las columnas financieras para que el total no se sobre-cuente.

| # | Nombre de la métrica | Categoría | Definición (aritmética) | Tipo (Financiero / No financiero) | Línea base (Q[X] [Año]) | Objetivo | Mejora esperada (%) | Mejora esperada ($) | Valor anualizado ($) | Explicación del cálculo | Cadencia de medición | Fuente de datos / Propietario | Procedencia de datos | Notas |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Metric name] | [Category] | [Formula] | [Financiero/No financiero] | [value] | [value] | [X%] | $[amount]/[period] | $[amount]/año | [Explicación de una o dos oraciones: qué línea base, qué objetivo, qué supuesto, mostrando la aritmética — p. ej., "Línea base 8,000 tickets/mes × 15% de reducción × $12 costo/ticket × 12 meses = $172,800/año"] | [Mensual / Trimestral / …] | [Sistema o equipo dueño de los datos] | [respuesta en línea / uploads/<file> / estimación] | [Salvedades, notas de doble conteo como "Captured in Metric [N]", medición diferida, etc.] |
| 2 | … | … | … | … | … | … | … | … | … | … | … | … | … | … |

**Cómo leer esta tabla**:
- **Tipo** — los valores `Financiero` se suman al Valor de Negocio Anual Total de arriba; los valores `No financiero` se reportan por su cuenta y no se suman al total financiero.
- **Explicación del cálculo** — muestra el camino aritmético desde la línea base y el objetivo hasta la cifra anualizada en dólares. Un revisor debería poder reproducir el número a partir de esta columna sin abrir el documento de trabajo de la Etapa 6.
- **Cadencia de medición** — con qué frecuencia el equipo de implementación debe recolectar y reportar esta métrica después del lanzamiento. Usa la granularidad de la tendencia histórica de la Etapa 5 como valor predeterminado (normalmente Mensual o Trimestral).
- **Fuente de datos / Propietario** — el sistema, dashboard o equipo que proporcionará las mediciones continuas. Si no se estableció durante la sesión, márcalo como `TBD` y señálalo en la columna de Notas.
- **Procedencia de datos** — de dónde vinieron los números de línea base, objetivo e impacto financiero por unidad durante la Etapa 5 (respuesta en línea, un nombre de archivo subido específico, o una estimación). Permite a futuros revisores juzgar qué tan blanda es cada entrada.
- **Notas** — banderas de doble conteo, aplazamientos de la Etapa 4, salvedades de factibilidad de la Etapa 3, advertencias de baja Fidelidad de la Fuente y cualquier otra cosa que un futuro rastreador necesite saber.

**Reglas para producir la tabla**:
- Una fila por métrica de `<INITIATIVE_FOLDER>/04-metrics-adjustment/final-metrics-list.md`. No descartes métricas, incluso si son no financieras o están marcadas como capturadas en otro lugar.
- Preserva la numeración de métricas de la lista final para que las filas sean estables entre revisiones.
- Para las métricas cuyo valor financiero lo lleva otra métrica, pon `Captured in Metric [N]` en `Mejora esperada ($)` y `Valor anualizado ($)` y explica por qué en `Notas` — esto mantiene la vista operativa completa mientras protege el total financiero del doble conteo.
- Para métricas diferidas o solo post-despliegue, pon `Deferred — see Notes` en las columnas financieras y explica cuándo comienza la medición.
- Extrae la `Explicación del cálculo` directamente del análisis por métrica de la Etapa 6 (no recalcules); esta columna es lo que hace que el documento final sea autocontenido para futuras auditorías.

## Aspectos destacados del valor de negocio no financiero cuantificado

Una narrativa corta que destaca las métricas no financieras de mayor impacto de la tabla consolidada anterior. Explica **por qué** importa cada métrica destacada más allá de su mejora numérica.

| Métrica | Mejora esperada | Por qué importa |
|---|---|---|
| [Metric name] | [p. ej., +8 puntos de NPS] | [1–2 oraciones] |
| ... | ... | ... |

> No reafirmes cada métrica no financiera aquí — la tabla consolidada es la lista exhaustiva. Esta sección es solo para el enmarcado ejecutivo de los 2–4 principales beneficios no financieros.

## Valor estratégico más allá de los números
[Documenta los beneficios estratégicos que son difíciles de monetizar por completo:
- Posicionamiento competitivo
- Protección de la relación con el cliente
- Transformación de la fuerza laboral
- Longevidad de los activos
- Base de datos para futura IA
- etc.]

## Riesgo de la inacción
[Documenta qué sucede si la iniciativa NO se persigue:
- Análisis de continuación de tendencias
- Riesgo de erosión competitiva
- Trayectoria de costos
- Impacto en el cliente]

## Apéndice A: Resumen de la definición de la iniciativa
[Una versión condensada de `<INITIATIVE_FOLDER>/01-initiative-definition/initiative-definition.md` — suficiente para que un lector de solo el documento final pueda entender la iniciativa sin abrir ningún otro artefacto.]

## Apéndice B: Metodología
[Breve descripción del proceso AI-BVIF seguido: tres fases, siete etapas, cómo se seleccionaron y refinaron las métricas, cómo se recolectaron los datos (en línea vs. carga de documentos) y cómo se validaron los cálculos. Indica claramente que **AI-BVIF cuantifica solo el lado del valor**. El costo de implementación, el costo operativo, el riesgo y el momento aún deben evaluarse por separado antes de que esto se convierta en un caso de negocio completo. AI-BVIF produce una estimación fundamentada y auditable que apoya la toma de decisiones informada, no un sustituto de ese análisis más amplio.]
```

**Lineamientos**:
- Escribe para una audiencia ejecutiva — clara, concisa, basada en evidencia
- Encabeza con la cifra financiera total
- La **Tabla consolidada de métricas** es el corazón del entregable. Debe ser completa, autocontenida y lo suficientemente estable para que un equipo que reciba este documento pueda comenzar la implementación y el rastreo sin necesidad de abrir ningún otro artefacto en `<INITIATIVE_FOLDER>/`.
- Separa los beneficios financieros de los no financieros en la tabla consolidada mediante la columna `Tipo`; no mantengas dos listas de métricas paralelas.
- Incluye el valor estratégico que no se puede monetizar solo como narrativa (no como filas en la tabla consolidada — solo las métricas cuantificadas pertenecen ahí).
- Incluye el riesgo de la inacción para enmarcar la decisión
- **AI-BVIF cuantifica solo el lado del valor** — el costo de implementación, el costo operativo, el riesgo y el momento deben evaluarse por separado antes de que esto se convierta en un caso de negocio completo. Indícalo claramente en el Apéndice B.
- Los documentos de trabajo intermedios (archivos de preguntas, archivos de aprobación, archivos de respuestas extraídas) NO son requeridos en la salida final — permanecen en las subcarpetas de etapa como el registro de auditoría.

## Paso 3: Guarda el artefacto

Guarda en `<INITIATIVE_FOLDER>/07-final-results/final-results.md`.

## Paso 4: Solicita la aprobación mediante un archivo

Crea un archivo de aprobación numerado secuencialmente dentro de `<INITIATIVE_FOLDER>/07-final-results/` (p. ej., `NN-final-results-approval.md` donde `NN` es el siguiente prefijo no usado). Usa esta estructura:

```markdown
# Stage 7 — Final Results Approval

## Qué estás aprobando
El entregable listo para ejecutivos de todo el proceso AI-BVIF. Este documento consolida todo lo que hemos trabajado y está destinado al propietario del presupuesto, los tomadores de decisiones y el equipo que implementará y rastreará la iniciativa. Incluye:

- **Resumen ejecutivo** y el valor de negocio anualizado total principal.
- Tabla de **valor de negocio anual total cuantificado**, agregada a partir de las métricas financieras de la Etapa 6.
- **Tabla consolidada de métricas** — la fuente única de verdad para el equipo de implementación y rastreo. Cada métrica aparece exactamente una vez con su definición, línea base, objetivo, explicación del cálculo, cadencia de medición y fuente de datos. Las métricas cuyo valor financiero se captura en otro lugar siguen listadas (para el rastreo operativo) pero marcadas para prevenir el doble conteo.
- **Aspectos destacados del valor de negocio no financiero** — un breve enmarcado ejecutivo de las métricas no financieras de mayor impacto. La lista no financiera completa vive en la tabla consolidada.
- **Valor estratégico más allá de los números** — posicionamiento competitivo, impacto en el cliente, transformación de la fuerza laboral y otros beneficios difíciles de monetizar pero reales.
- **Riesgo de la inacción** — qué sucede si la iniciativa no se persigue (continuación de tendencias, erosión competitiva, trayectoria de costos).
- **Apéndices** que cubren una definición condensada de la iniciativa y la metodología AI-BVIF seguida.

AI-BVIF cuantifica solo el lado del valor. El costo de implementación, el costo operativo, el riesgo y el momento aún deben evaluarse por separado antes de que esto se convierta en un caso de negocio completo. Aprobar significa que estás de acuerdo en que el documento (incluida la tabla consolidada de métricas) está listo para presentarse ante el tomador de decisiones y en manos del equipo de implementación, entendiendo que la evaluación del valor está completa pero el caso de negocio completo no.

## Dónde leer el artefacto completo
`<INITIATIVE_FOLDER>/07-final-results/final-results.md`

---

## Pregunta 1
¿Apruebas el documento de resultados finales?

A) Aprobar — proceso AI-BVIF completo
B) Solicitar cambios (por favor describe después de la etiqueta [Answer]: abajo)
X) Otro (por favor describe después de la etiqueta [Answer]: abajo)

[Answer]:
```

Anuncia la ruta del archivo en el chat y **NO PROCEDAS** hasta que el usuario señale que terminó y la respuesta se resuelva como Aprobar.

## Paso 5: Actualiza el estado y cierra

Después de la aprobación, actualiza `<INITIATIVE_FOLDER>/bvif-state.md`:
- Marca la Etapa 7 como `[x]`
- Establece la etapa actual como "COMPLETE"
- Agrega la marca de tiempo de finalización

Registra la aprobación en `<INITIATIVE_FOLDER>/audit.md`.

Presenta el mensaje final:

```markdown
# ✅ Proceso AI-BVIF completo

La identificación de valor de negocio para la **[Initiative Name]** de **[Customer Name]** está completa.

**Valor de negocio anual total cuantificado**: ~$[total]/año

Todos los artefactos están almacenados en `<INITIATIVE_FOLDER>/` con carpetas prefijadas por secuencia.
El documento de resultados finales está en `<INITIATIVE_FOLDER>/07-final-results/final-results.md`.
```
