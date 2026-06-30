# Etapa 4 — Ajuste de métricas

**Propósito**: Producir una lista finalizada de métricas que sea tanto representativa de los resultados de negocio esperados como actualmente medible.

> **Convención de rutas**: `<INITIATIVE_FOLDER>` se refiere a la carpeta por iniciativa bajo `bvif-docs/` (p. ej., `bvif-docs/01-customer-churn-predictor-202604`). Consulta `common/process-overview.md` → "Convención de rutas: carpeta por iniciativa".

## Persona del agente

Adopta la persona definida en `stages/agents/stage-4-metrics-adjustment-agent.md` (Refinador de métricas de IA de negocio). La persona se enfoca en las métricas de Factibilidad 3 — explorando alternativas proxy (2–3 sugerencias por métrica), la eliminación y si las métricas existentes ya capturan el valor previsto. También gobierna el tono, la cadencia de una pregunta a la vez y el formato de la tabla de salida (tabla original anexada con información de proxy/eliminación; las nuevas filas de proxy se completan con los mismos campos). El resto de este archivo de etapa orquesta el flujo completo de decisiones en todos los niveles de factibilidad.

## Prerrequisitos
- Etapa 3 completada y aprobada
- Tabla de factibilidad disponible

## Paso 1: Carga los artefactos previos

Lee:
- `<INITIATIVE_FOLDER>/03-metrics-identification/feasibility-table.md`
- `<INITIATIVE_FOLDER>/02-business-value-mapping/business-value-mapping.md`
- `<INITIATIVE_FOLDER>/01-initiative-definition/initiative-definition.md`

## Paso 2: Aplica las decisiones de ajuste

Para cada métrica, aplica una de las siguientes decisiones:

| Decisión | Cuándo aplicar |
|---|---|
| **Conservar tal cual** | Métricas de Factibilidad 1 — no se necesitan cambios |
| **Activar** | Métricas de Factibilidad 2 — establecer un mecanismo para extraer la métrica, preferiblemente automatizado |
| **Reemplazar con proxy** | Métricas de Factibilidad 3 — identificar una métrica proxy que capture la misma intención usando datos disponibles |
| **Diferir** | Métrica solo disponible después del despliegue — marcar para implementación post-producción |
| **Eliminar** | No representativa, redundante, o sin proxy viable |

**Flujo de decisión**:
```
Factibilidad 1 → Conservar tal cual
Factibilidad 2 → Activar (establecer mecanismo de extracción)
Factibilidad 3 → ¿Se puede encontrar un proxy?
                  ├── Sí → Reemplazar con proxy
                  ├── No, pero disponible post-despliegue → Diferir
                  └── No, y no es crítica → Eliminar
```

**⚠️ CONDICIÓN DE PARADA**: Si una métrica que es crítica para la evaluación del tomador de decisiones está calificada como Factibilidad 3 y no tiene proxy viable, **DETÉN el proceso** e informa al usuario que esta métrica debe implementarse antes de continuar.

## Paso 3: Haz preguntas aclaratorias (si es necesario)

Crea un archivo de preguntas numerado secuencialmente dentro de `<INITIATIVE_FOLDER>/04-metrics-adjustment/` (p. ej., `01-metrics-adjustment-questions.md`) si la identificación del proxy requiere el aporte del usuario sobre las fuentes de datos disponibles. Consulta `common/question-format-guide.md` para la estructura completa y las reglas de numeración.

## Paso 4: Redacta el registro de decisiones

```markdown
# Metrics Adjustment — Decision Log

| Business Value Category | Metric Name | Arithmetic Definition | Feasibility | Situation | Decision | Reasoning |
|---|---|---|---|---|---|---|
| [Category] | [Name] | [Formula] | F[1/2/3] | [Current situation] | [Decision] | [Why] |
| [Category] | [NEW PROXY] [Name] | [Formula] | F[1/2] | [Data source] | New proxy metric | [Why this proxy works] |
```

## Paso 5: Redacta la lista final de métricas

Produce una tabla limpia de todas las métricas que avanzarán a la recolección de datos:

```markdown
# Final Metrics List

| Business Value Category | Metric Name | Arithmetic Definition | Explanation |
|---|---|---|---|
| [Category] | [Name*] | [Formula] | [Why it matters] |
```

## Paso 6: Guarda los artefactos

Guarda en:
- `<INITIATIVE_FOLDER>/04-metrics-adjustment/decision-log.md`
- `<INITIATIVE_FOLDER>/04-metrics-adjustment/final-metrics-list.md`

## Paso 7: Solicita la aprobación mediante un archivo

Crea un archivo de aprobación numerado secuencialmente dentro de `<INITIATIVE_FOLDER>/04-metrics-adjustment/` (p. ej., `NN-metrics-adjustment-approval.md` donde `NN` es el siguiente prefijo no usado). Usa esta estructura:

```markdown
# Stage 4 — Metrics Adjustment Approval

## Qué estás aprobando
Las decisiones aplicadas a cada métrica de la Etapa 3 para que la lista que llevamos a la recolección de datos sea tanto **representativa** del valor esperado como **actualmente medible**. Para cada métrica, se ha aplicado una de estas decisiones:

- **Conservar tal cual** — Métrica de Factibilidad 1, no se necesitan cambios.
- **Activar** — Métrica de Factibilidad 2, configuraremos la extracción (preferiblemente automatizada).
- **Reemplazar con proxy** — Métrica de Factibilidad 3, hemos propuesto un proxy que captura la misma intención usando datos disponibles.
- **Diferir** — La métrica solo se vuelve medible post-despliegue; se marca para implementación posterior.
- **Eliminar** — La métrica es redundante, no representativa, o no tiene proxy viable.

Si alguna métrica crítica era Factibilidad 3 sin proxy viable, el proceso se detiene aquí hasta resolverlo (condición de PARADA).

Aprobar fija la lista final de métricas que usaremos para el resto del flujo de trabajo — la Etapa 5 recolecta datos para estas métricas específicas, la Etapa 6 calcula su valor de negocio y la Etapa 7 las reporta.

## Dónde leer los artefactos completos
- Registro de decisiones: `<INITIATIVE_FOLDER>/04-metrics-adjustment/decision-log.md`
- Lista final de métricas: `<INITIATIVE_FOLDER>/04-metrics-adjustment/final-metrics-list.md`

---

## Pregunta 1
¿Apruebas el registro de decisiones y la lista final de métricas?

A) Aprobar y continuar a la Etapa 5 — Recolección de datos
B) Solicitar cambios (por favor describe después de la etiqueta [Answer]: abajo)
X) Otro (por favor describe después de la etiqueta [Answer]: abajo)

[Answer]:
```

Anuncia la ruta del archivo en el chat y **NO PROCEDAS** hasta que el usuario señale que terminó y la respuesta se resuelva como Aprobar.

## Paso 8: Actualiza el estado

Después de la aprobación, actualiza `<INITIATIVE_FOLDER>/bvif-state.md`:
- Marca la Etapa 4 como `[x]`
- Establece la etapa actual como "Stage 5 — Data Collection"

Registra la aprobación en `<INITIATIVE_FOLDER>/audit.md`.
