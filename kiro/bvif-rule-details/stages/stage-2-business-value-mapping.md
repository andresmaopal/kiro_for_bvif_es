# Etapa 2 — Mapeo de valor de negocio

**Propósito**: Identificar la categoría principal de valor de negocio (y opcionalmente una secundaria) que representa el beneficio de mayor impacto de la iniciativa. Usa las mismas cuatro categorías definidas en CAF v3.

> **Convención de rutas**: `<INITIATIVE_FOLDER>` se refiere a la carpeta por iniciativa bajo `bvif-docs/` (p. ej., `bvif-docs/01-customer-churn-predictor-202604`). Consulta `common/process-overview.md` → "Convención de rutas: carpeta por iniciativa".

## Persona del agente

Adopta la persona definida en `stages/agents/stage-2-business-value-mapping-agent.md`. Ese archivo es la fuente de verdad para el rol, las reglas de priorización, el tono y cómo llevar al usuario a un acuerdo sobre las categorías seleccionadas — no repitas su contenido aquí.

## Prerrequisitos
- Etapa 1 completada y aprobada
- Definición refinada de la iniciativa disponible

## Paso 1: Carga los artefactos previos

Lee `<INITIATIVE_FOLDER>/01-initiative-definition/initiative-definition.md`.

## Paso 2: Analiza frente a las categorías de CAF v3

Mapea la iniciativa a una o más de estas categorías:

| Categoría | Descripción |
|---|---|
| **Aumentar los ingresos** | Aumentos en el consumo del cliente, expansión de los mercados direccionables (crecimiento de la línea superior) |
| **Aumentar la eficiencia operativa** | Reducción de gastos existentes (ahorro de costos) o prevención de costos futuros (evitación de costos) |
| **Reducir el riesgo del negocio** | Inversiones en cumplimiento regulatorio, seguridad, etc. Normalmente sin beneficio financiero directo |
| **Mejorar el ESG** | Objetivos Ambientales, Sociales o de Gobernanza. Sin beneficio financiero directo, pero con valor estratégico |

**Lineamientos**:
- Elige como máximo dos categorías (una primaria, opcionalmente una secundaria)
- Justifica cada selección con una breve explicación ligada a la iniciativa

Consulta la persona del agente para las reglas completas de priorización (impacto directo, categorías mínimas, acuerdo del usuario).

## Paso 3: Haz preguntas aclaratorias (si es necesario)

Si el mapeo es ambiguo, crea un archivo de preguntas numerado secuencialmente dentro de `<INITIATIVE_FOLDER>/02-business-value-mapping/` (p. ej., `01-business-value-mapping-questions.md`). Consulta `common/question-format-guide.md` para la estructura completa y las reglas de numeración.

## Paso 4: Redacta el mapeo de valor de negocio

Estructura la salida como:

```markdown
# Business Value Mapping

## Primary Category: [Category Name]
[Explicación de por qué esta es la categoría primaria, ligada a la definición de la iniciativa]

## Secondary Category: [Category Name] (if applicable)
[Explicación de por qué esta es una categoría secundaria]
```

## Paso 5: Guarda el artefacto

Guarda en `<INITIATIVE_FOLDER>/02-business-value-mapping/business-value-mapping.md`.

## Paso 6: Solicita la aprobación mediante un archivo

Crea un archivo de aprobación numerado secuencialmente dentro de `<INITIATIVE_FOLDER>/02-business-value-mapping/` (p. ej., `NN-business-value-mapping-approval.md` donde `NN` es el siguiente prefijo no usado). Usa esta estructura:

```markdown
# Stage 2 — Business Value Mapping Approval

## Qué estás aprobando
Cuáles de las cuatro categorías de valor de negocio del AWS Cloud Adoption Framework (CAF v3) describen mejor cómo esta iniciativa entrega valor. Elegir la categoría correcta (o dos) da forma a las métricas que elegiremos en la Etapa 3 y a cómo expresaremos el impacto financiero en la Etapa 6. Las distintas categorías se comparan de forma diferente — por ejemplo, el crecimiento de ingresos necesita un ajuste de margen antes de poder compararse con los ahorros operativos.

### Las cuatro categorías de valor de negocio de CAF v3
- **Aumentar los ingresos** — crecimiento de la línea superior. Aumentos en el consumo del cliente, nuevos clientes o expansión a nuevos mercados direccionables. El impacto en ingresos requiere un ajuste de margen de contribución antes de ser comparable con los ahorros de costos.
- **Aumentar la eficiencia operativa** — ahorros de línea inferior. Ya sea reducción de costos (bajar gastos existentes) o evitación de costos (prevenir costos futuros). Directamente comparable con otras cifras de ahorro de costos.
- **Reducir el riesgo del negocio** — inversiones en cumplimiento regulatorio, seguridad, resiliencia y áreas similares. Normalmente sin beneficio financiero directo, pero previene pérdidas materiales (multas, interrupciones, pérdida de datos).
- **Mejorar el ESG** — objetivos Ambientales, Sociales o de Gobernanza. Sin beneficio financiero directo, pero entrega valor estratégico y reputacional alineado con compromisos de sostenibilidad y responsabilidad.

¿Quieres las definiciones y ejemplos completos? Consulta la página principal del AWS Cloud Adoption Framework, que siempre apunta a la versión actual del whitepaper: https://aws.amazon.com/cloud-adoption-framework/

## Dónde leer el artefacto completo
`<INITIATIVE_FOLDER>/02-business-value-mapping/business-value-mapping.md`

---

## Pregunta 1
¿Apruebas el mapeo de valor de negocio?

A) Aprobar y continuar a la Etapa 3 — Identificación y factibilidad de métricas
B) Solicitar cambios (por favor describe después de la etiqueta [Answer]: abajo)
X) Otro (por favor describe después de la etiqueta [Answer]: abajo)

[Answer]:
```

Anuncia la ruta del archivo en el chat y **NO PROCEDAS** hasta que el usuario señale que terminó y la respuesta se resuelva como Aprobar.

## Paso 7: Actualiza el estado

Después de la aprobación, actualiza `<INITIATIVE_FOLDER>/bvif-state.md`:
- Marca la Etapa 2 como `[x]`
- Establece la etapa actual como "Stage 3 — Metrics Identification & Feasibility"

Registra la aprobación en `<INITIATIVE_FOLDER>/audit.md`.
