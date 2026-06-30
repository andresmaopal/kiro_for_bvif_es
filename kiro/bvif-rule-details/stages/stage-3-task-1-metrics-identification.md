# Etapa 3 — Tarea 1: Identificar métricas

**Propósito**: Identificar las métricas más apropiadas para confirmar que la iniciativa de IA ha logrado con éxito sus objetivos de negocio.

> **Convención de rutas**: `<INITIATIVE_FOLDER>` se refiere a la carpeta por iniciativa bajo `bvif-docs/` (p. ej., `bvif-docs/01-customer-churn-predictor-202604`). Consulta `common/process-overview.md` → "Convención de rutas: carpeta por iniciativa".

## Persona del agente

Adopta la persona definida en `stages/agents/stage-3-task-1-metrics-identification-agent.md` (Asesor de Métricas de Valor de la Iniciativa de IA). Ese archivo es la fuente de verdad para el rol, los campos requeridos por métrica, el mínimo/máximo por categoría, la regla de resaltado con asterisco, el aplazamiento de la factibilidad a la siguiente tarea y el tono — no repitas su contenido aquí.

## Prerrequisitos
- Etapa 2 completada y aprobada
- Definición de la iniciativa y categorías de valor de negocio disponibles

## Paso 1: Carga los artefactos previos

Lee:
- `<INITIATIVE_FOLDER>/01-initiative-definition/initiative-definition.md`
- `<INITIATIVE_FOLDER>/02-business-value-mapping/business-value-mapping.md`

## Paso 2: Identifica métricas por categoría

Sigue la persona del agente para los campos de las métricas, los conteos por categoría, el resaltado con asterisco y las reglas de unidades. Este archivo de etapa solo agrega guía de orquestación:

- Piensa en métricas que sean:
  - Directamente impactadas por la iniciativa de IA
  - Medibles y cuantificables
  - Significativas para el propietario del presupuesto / tomador de decisiones
  - Representativas del resultado de negocio esperado

## Paso 3: Haz preguntas aclaratorias (si es necesario)

Si el dominio del usuario requiere conocimiento específico de métricas, crea un archivo de preguntas numerado secuencialmente dentro de `<INITIATIVE_FOLDER>/03-metrics-identification/` (p. ej., `01-metrics-identification-questions.md`). Consulta `common/question-format-guide.md` para la estructura completa y las reglas de numeración. Ten en cuenta que la Tarea 1 y la Tarea 2 de la Etapa 3 comparten la misma subcarpeta `03-metrics-identification/`, por lo que el contador de secuencia continúa entre ambas tareas.

## Paso 4: Redacta la tabla de métricas

Da formato como una tabla markdown:

```markdown
# Metrics Identification

| Business Value Category | Metric Name | Arithmetic Definition | Explanation |
|---|---|---|---|
| [Category] | [Name*] | [Formula] | [Why it matters] |
| ... | ... | ... | ... |
```

## Paso 5: Guarda el artefacto

Guarda en `<INITIATIVE_FOLDER>/03-metrics-identification/metrics-table.md`.

## Paso 6: Solicita la aprobación mediante un archivo

Crea un archivo de aprobación numerado secuencialmente dentro de `<INITIATIVE_FOLDER>/03-metrics-identification/` (p. ej., `NN-metrics-identification-approval.md` donde `NN` es el siguiente prefijo no usado en esa carpeta — recuerda que el contador se comparte con la Tarea 2). Usa esta estructura:

```markdown
# Stage 3 / Task 1 — Metrics Identification Approval

## Qué estás aprobando
La lista de métricas que proponemos usar para demostrar que la iniciativa entregó valor. Para cada categoría de valor de negocio de la Etapa 2, hemos identificado métricas que están directamente influidas por la iniciativa, son significativas para el propietario del presupuesto y se pueden expresar como un número absoluto, un porcentaje o un monto en moneda. Las métricas marcadas con un asterisco (*) son las que consideramos más representativas.

En este punto solo estamos decidiendo **qué medir**, no si cada métrica es fácil de medir hoy — la factibilidad viene a continuación en la Tarea 2, y los ajustes (proxies, activación, aplazamiento) vienen en la Etapa 4. Aprobar significa que estás de acuerdo en que estas métricas son las correctas para contar la historia del valor de la iniciativa.

## Dónde leer el artefacto completo
`<INITIATIVE_FOLDER>/03-metrics-identification/metrics-table.md`

---

## Pregunta 1
¿Apruebas la tabla de métricas?

A) Aprobar y continuar a la Tarea 2 — Evaluar la factibilidad de las métricas
B) Solicitar cambios (por favor describe después de la etiqueta [Answer]: abajo)
X) Otro (por favor describe después de la etiqueta [Answer]: abajo)

[Answer]:
```

Anuncia la ruta del archivo en el chat y **NO PROCEDAS** hasta que el usuario señale que terminó y la respuesta se resuelva como Aprobar.

## Paso 7: Actualiza el estado

Después de la aprobación, actualiza `<INITIATIVE_FOLDER>/bvif-state.md`:
- Marca la Etapa 3 Tarea 1 como `[x]`
- Establece la etapa actual como "Stage 3 — Task 2: Assess Metrics Feasibility"

Registra la aprobación en `<INITIATIVE_FOLDER>/audit.md`.
