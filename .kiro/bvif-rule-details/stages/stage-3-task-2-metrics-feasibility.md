# Etapa 3 — Tarea 2: Evaluar la factibilidad de las métricas

**Propósito**: Evaluar si cada métrica es actualmente medible asignando una etiqueta de factibilidad.

> **Convención de rutas**: `<INITIATIVE_FOLDER>` se refiere a la carpeta por iniciativa bajo `bvif-docs/` (p. ej., `bvif-docs/01-customer-churn-predictor-202604`). Consulta `common/process-overview.md` → "Convención de rutas: carpeta por iniciativa".

## Persona del agente

Adopta la persona definida en `stages/agents/stage-3-task-2-metrics-feasibility-agent.md` (Evaluador de métricas de IA de negocio). Ese archivo gobierna el enfoque de clasificación (tres categorías de factibilidad), el requisito de explicación por métrica, la cadencia de una pregunta a la vez, el tono y el formato de salida (tabla anexada con factibilidad y explicación) — no repitas su contenido aquí.

## Prerrequisitos
- Etapa 3 Tarea 1 completada y aprobada
- Tabla de métricas disponible

## Paso 1: Carga los artefactos previos

Lee:
- `<INITIATIVE_FOLDER>/03-metrics-identification/metrics-table.md`
- `<INITIATIVE_FOLDER>/01-initiative-definition/initiative-definition.md`

## Paso 2: Guía la evaluación de factibilidad

Para cada métrica, asigna una de las siguientes etiquetas de factibilidad:

| Etiqueta | Definición |
|---|---|
| **Factibilidad 1** | La métrica ya se rastrea. Lista para usar. |
| **Factibilidad 2** | Los datos existen, pero la métrica aún no se calcula. Factible con algo de configuración. |
| **Factibilidad 3** | No existen datos. Requiere nueva infraestructura. |

**Lineamientos**:
- Usa un archivo de preguntas numerado secuencialmente dentro de `<INITIATIVE_FOLDER>/03-metrics-identification/` (p. ej., `NN-metrics-feasibility-questions.md` donde `NN` es el siguiente prefijo no usado — el contador de secuencia se comparte con los archivos de la Tarea 1) para impulsar la conversación de factibilidad con el usuario
- Las preguntas deben indagar: "¿Esta métrica se rastrea actualmente?", "¿Existen los datos subyacentes?", "¿Qué sistemas tienen estos datos?"
- Agrega comentarios opcionales para cada métrica explicando la justificación de la factibilidad
- Consulta `common/question-format-guide.md` para la estructura completa y las reglas de numeración

## Paso 3: Redacta la tabla de factibilidad

Extiende la tabla de métricas con columnas de factibilidad:

```markdown
# Metrics Feasibility Assessment

| Business Value Category | Metric Name | Arithmetic Definition | Explanation | Feasibility | Comments |
|---|---|---|---|---|---|
| [Category] | [Name*] | [Formula] | [Why] | Feasibility [1/2/3] | [Optional notes] |
| ... | ... | ... | ... | ... | ... |
```

## Paso 4: Guarda el artefacto

Guarda en `<INITIATIVE_FOLDER>/03-metrics-identification/feasibility-table.md`.

## Paso 5: Solicita la aprobación mediante un archivo

Crea un archivo de aprobación numerado secuencialmente dentro de `<INITIATIVE_FOLDER>/03-metrics-identification/` (p. ej., `NN-metrics-feasibility-approval.md` donde `NN` es el siguiente prefijo no usado). Usa esta estructura:

```markdown
# Stage 3 / Task 2 — Metrics Feasibility Approval

## Qué estás aprobando
Una etiqueta de factibilidad para cada métrica, que refleja qué tan práctico es medirla **hoy**:

- **Factibilidad 1** — La métrica ya se rastrea. Lista para usar de inmediato.
- **Factibilidad 2** — Los datos subyacentes existen, pero la métrica en sí aún no se calcula. Factible con algo de configuración.
- **Factibilidad 3** — No existen datos. Requeriría nueva instrumentación o infraestructura antes de poder medir la métrica.

Esta evaluación aún no cambia ninguna métrica — solo etiqueta cada una para que la Etapa 4 pueda decidir qué hacer: conservar tal cual, activar, cambiar por un proxy, diferir hasta después del despliegue, o eliminar. Aprobar significa que estás de acuerdo en que las etiquetas reflejan la realidad en tu entorno (sistemas, rastreo, disponibilidad de datos).

## Dónde leer el artefacto completo
`<INITIATIVE_FOLDER>/03-metrics-identification/feasibility-table.md`

---

## Pregunta 1
¿Apruebas la evaluación de factibilidad?

A) Aprobar y continuar a la Etapa 4 — Ajuste de métricas
B) Solicitar cambios (por favor describe después de la etiqueta [Answer]: abajo)
X) Otro (por favor describe después de la etiqueta [Answer]: abajo)

[Answer]:
```

Anuncia la ruta del archivo en el chat y **NO PROCEDAS** hasta que el usuario señale que terminó y la respuesta se resuelva como Aprobar.

## Paso 6: Actualiza el estado

Después de la aprobación, actualiza `<INITIATIVE_FOLDER>/bvif-state.md`:
- Marca la Etapa 3 Tarea 2 como `[x]`
- Marca la Etapa 3 en general como `[x]`
- Establece la etapa actual como "Stage 4 — Metrics Adjustment"

Registra la aprobación en `<INITIATIVE_FOLDER>/audit.md`.
