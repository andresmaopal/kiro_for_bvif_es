# Configuración de la sesión

**Propósito**: Inicializar la sesión AI-BVIF, identificar el cliente y la iniciativa, crear una carpeta dedicada por iniciativa y establecer el espacio de trabajo dentro de ella.

> **Convención de rutas**: `<INITIATIVE_FOLDER>` se refiere a la carpeta por iniciativa bajo `bvif-docs/` (p. ej., `bvif-docs/01-customer-churn-predictor-202604`). Consulta `common/process-overview.md` → "Convención de rutas: carpeta por iniciativa".

## Paso 1: Verifica si hay un proyecto existente

Escanea `bvif-docs/` en busca de subcarpetas que coincidan con el patrón `<NN>-<slug>-<yyyymm>/`:

- **Si existen una o más y el usuario está reanudando una de ellas**: Identifica la carpeta de la iniciativa activa (pregunta al usuario si es ambiguo), luego sigue `common/session-continuity.md` y reanuda desde `<INITIATIVE_FOLDER>/bvif-state.md`.
- **Si el usuario está iniciando una nueva iniciativa (o no existen carpetas)**: Continúa con la configuración de un nuevo proyecto a continuación.

## Paso 2: Reúne el contexto del cliente

Recolecta la siguiente información del usuario:

- **Nombre del cliente**: Organización que se evalúa
- **Industria**: Sector/vertical
- **Contexto breve**: Qué hace el cliente, su posición en el mercado, antecedentes relevantes
- **Iniciativa de IA**: La idea cruda o propuesta a evaluar
- **Nombre de la iniciativa**: Un nombre corto y legible para esta iniciativa (usado para nombrar la carpeta)
- **Patrocinador de la iniciativa**: Quién la propuso (p. ej., COO, CTO, VP de Ingeniería)

Si el usuario ya proporcionó esta información en su solicitud inicial, extráela directamente. Pregunta solo por lo que falte.

**Todas las preguntas DEBEN hacerse mediante un archivo de interacción — nunca en el chat.** Consulta `common/question-format-guide.md` para la estructura completa, la numeración secuencial y las reglas del flujo de trabajo.

Como la carpeta de la iniciativa aún no existe en este punto, crea el primer archivo de interacción en la carpeta de preparación previa a la iniciativa:

```
bvif-docs/_pending-session/01-session-setup-questions.md
```

Incluye un bloque `## Pregunta N` por cada pieza de información faltante de las anteriores, cada uno con opciones significativas más `X) Otro`. Anuncia el archivo en el chat, espera a que el usuario responda, luego lee las respuestas.

Una vez creada la carpeta de la iniciativa en el Paso 4, **mueve** `bvif-docs/_pending-session/01-session-setup-questions.md` a `<INITIATIVE_FOLDER>/00-session-setup/` (manteniendo el mismo nombre de archivo) para que el historial secuencial se preserve dentro de la carpeta de la iniciativa. Cualquier pregunta adicional de Configuración de la sesión usa el siguiente número de secuencia dentro de `<INITIATIVE_FOLDER>/00-session-setup/`.

## Paso 3: Construye el nombre de la carpeta de la iniciativa

Genera el nombre de la carpeta a partir del nombre de la iniciativa proporcionado por el usuario:

1. **Convierte el nombre de la iniciativa en slug**:
   - Pon todo en minúsculas
   - Reemplaza espacios y puntuación con guiones (`-`)
   - Elimina palabras de relleno (`el`, `la`, `los`, `de`, `para`, `y`; o sus equivalentes en inglés `the`, `a`, `an`, `of`, `for`, `and`) cuando sea necesario para mantenerlo corto
   - Mantén el slug en aproximadamente 3–5 palabras, máximo 40 caracteres
   - Elimina cualquier carácter que no sea `a-z`, `0-9` o `-`
   - Colapsa guiones consecutivos y recorta los guiones iniciales/finales

2. **Determina el número de secuencia consecutivo**:
   - Lista las carpetas de iniciativa existentes directamente bajo `bvif-docs/` (las que coinciden con `<NN>-<slug>-<yyyymm>/`)
   - Encuentra el prefijo de dos dígitos más alto existente
   - Usa el siguiente número, con relleno de ceros a dos dígitos (p. ej., `04`)
   - Si aún no existen carpetas de iniciativa, empieza en `01`

3. **Determina el sufijo de fecha**: año y mes actuales en formato `yyyymm` (p. ej., `202604`).

4. **Compón el nombre de la carpeta**:
   ```
   <NN>-<initiative-slug>-<yyyymm>
   ```
   Ejemplos:
   - `01-customer-churn-predictor-202604`
   - `02-contact-center-ai-assistant-202604`
   - `03-invoice-auto-classification-202605`

5. **Confirma el nombre de la carpeta con el usuario** antes de crearla. Esta confirmación es en sí misma una interacción basada en archivo — crea el siguiente archivo de aprobación numerado secuencialmente (aún en `bvif-docs/_pending-session/`, ya que la carpeta de la iniciativa todavía no existe):

   ```
   bvif-docs/_pending-session/02-session-setup-approval.md
   ```

   Usa esta estructura:

   ```markdown
   # Session Setup — Initiative Folder Approval

   ## Qué estás aprobando
   El nombre de la carpeta que usaremos para todo lo relacionado con esta iniciativa de IA. El nombre sigue el patrón `<NN>-<initiative-slug>-<yyyymm>`:

   - `<NN>` — número consecutivo de dos dígitos para que las iniciativas se ordenen según el orden en que se iniciaron.
   - `<initiative-slug>` — una versión corta, en minúsculas y separada por guiones del nombre de la iniciativa, fácil de leer y navegar en un árbol de archivos.
   - `<yyyymm>` — el año y mes en que se inició la iniciativa, para que puedas encontrar trabajo antiguo por fecha.

   Una vez que apruebes, esta carpeta contendrá todos los artefactos de esta iniciativa: salidas intermedias de etapa, archivos de interacción, el registro de auditoría y el informe final de valor de negocio. Es puramente organizacional — nada de la iniciativa en sí cambia con base en este nombre. Si el slug no se lee bien para tu equipo, pide uno diferente.

   **Ruta propuesta**: `bvif-docs/<NN>-<initiative-slug>-<yyyymm>/` (p. ej., `bvif-docs/01-customer-churn-predictor-202604/`)

   ---

   ## Pregunta 1
   ¿Apruebas el nombre de carpeta propuesto?

   A) Aprobar el nombre de carpeta propuesto y continuar
   B) Solicitar un slug diferente (por favor describe después de la etiqueta [Answer]: abajo)
   X) Otro (por favor describe después de la etiqueta [Answer]: abajo)

   [Answer]:
   ```

   Espera a que el usuario responda. Si solicita un slug diferente, regenéralo y crea el siguiente archivo de aprobación numerado secuencialmente (p. ej., `03-session-setup-approval.md`) hasta que el usuario apruebe.

De aquí en adelante en el flujo de trabajo, `<INITIATIVE_FOLDER>` se refiere a esta carpeta.

## Paso 4: Crea la estructura de directorios

Una vez que el usuario apruebe el nombre de la carpeta, crea `<INITIATIVE_FOLDER>/` con las siguientes subcarpetas:

```
<INITIATIVE_FOLDER>/
├── 00-session-setup/
├── 01-initiative-definition/
├── 02-business-value-mapping/
├── 03-metrics-identification/
├── 04-metrics-adjustment/
├── 05-data-collection/
├── 06-business-value-calculation/
├── 07-final-results/
```

Todas las subcarpetas de etapa, `bvif-state.md` y `audit.md` DEBEN crearse dentro de `<INITIATIVE_FOLDER>`. Nunca las coloques en la raíz de `bvif-docs/`.

**Inmediatamente después de crear la estructura de directorios**, mueve cada archivo de interacción de `bvif-docs/_pending-session/` a `<INITIATIVE_FOLDER>/00-session-setup/`, preservando los nombres de archivo y los números de secuencia. Luego elimina (o deja vacía) `bvif-docs/_pending-session/`.

## Paso 5: Crea el documento de contexto de la sesión

Crea `<INITIATIVE_FOLDER>/00-session-setup/session-context.md`:

```markdown
# AI-BVIF Session Context

## Customer Information
- **Customer Name**: [name]
- **Industry**: [industry]
- **Context**: [brief description]

## AI Initiative
- **Initiative Name**: [initiative name]
- **Initiative Folder**: <INITIATIVE_FOLDER>
- **Initiative Summary**: [raw initiative description]
- **Sponsor/Budget Owner**: [role]

## Session Information
- **Start Date**: [ISO timestamp]
- **Team Members**: [if provided]
```

## Paso 6: Crea el archivo de estado inicial

Crea `<INITIATIVE_FOLDER>/bvif-state.md`:

```markdown
# AI-BVIF State Tracking

## Project Information
- **Customer**: [customer name]
- **Industry**: [industry]
- **Initiative Name**: [initiative name]
- **Initiative Folder**: <INITIATIVE_FOLDER>
- **Initiative Summary**: [brief summary]
- **Start Date**: [ISO timestamp]
- **Current Stage**: Session Setup

## Stage Progress
- [x] Session Setup
- [ ] Stage 1 — Refine the Initiative Definition
- [ ] Stage 2 — Business Value Mapping
- [ ] Stage 3 — Metrics Identification & Feasibility
  - [ ] Task 1: Identify Metrics
  - [ ] Task 2: Assess Metrics Feasibility
- [ ] Stage 4 — Metrics Adjustment
- [ ] Stage 5 — Data Collection
- [ ] Stage 6 — Business Value Calculation
- [ ] Stage 7 — Final Results Documentation
```

> **Nota:** Los rótulos de etapa del archivo de estado (`Stage 1 — …`, `Session Setup`, etc.) se mantienen en inglés a propósito, ya que la página del taller en el navegador los lee para detectar el progreso. El agente puede conversar en español, pero conserva estos rótulos tal cual en `bvif-state.md`.

## Paso 7: Crea el registro de auditoría

Crea `<INITIATIVE_FOLDER>/audit.md`:

```markdown
# AI-BVIF Audit Log

**Initiative Folder**: <INITIATIVE_FOLDER>

---

## Session Setup
**Timestamp**: [ISO timestamp]
**User Input**: "[Complete raw user input]"
**AI Response**: "Session initialized for [customer]. Initiative folder <INITIATIVE_FOLDER> created."
**Context**: Session Setup — New project initialized

---
```

## Paso 8: Presenta el mensaje de finalización

```markdown
# ✅ Configuración de la sesión completa

- **Cliente**: [customer name]
- **Industria**: [industry]
- **Nombre de la iniciativa**: [initiative name]
- **Carpeta de la iniciativa**: <INITIATIVE_FOLDER>
- **Espacio de trabajo**: todas las subcarpetas de etapa, `bvif-state.md` y `audit.md` creadas dentro de la carpeta de la iniciativa

**Siguiente paso**: Procediendo a la **Etapa 1 — Refinar la definición de la iniciativa**...
```

Procede automáticamente a la Etapa 1.
