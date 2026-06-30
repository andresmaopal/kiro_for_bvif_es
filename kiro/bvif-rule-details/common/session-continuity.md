# Continuidad de sesión

> **Convención de rutas**: `<INITIATIVE_FOLDER>` se refiere a la carpeta por iniciativa bajo `bvif-docs/` (p. ej., `bvif-docs/01-customer-churn-predictor-202604`). Consulta `common/process-overview.md` → "Convención de rutas: carpeta por iniciativa".

## Flujo de "Bienvenido de nuevo"
Cuando un usuario regresa a continuar el trabajo en un proyecto AI-BVIF existente, sigue este flujo de dos pasos. **La decisión real de reanudar DEBE capturarse en un archivo, nunca en el chat** (consulta `common/question-format-guide.md`).

### Paso 1 — Anuncio en el chat (no interactivo)
Publica un mensaje de estado en el chat resumiendo lo que se encontró. Esto es solo informativo; NO contiene ninguna etiqueta `[Answer]:`:

```markdown
**¡Bienvenido de nuevo! Encontré un proyecto AI-BVIF existente.**

Según `<INITIATIVE_FOLDER>/bvif-state.md`:
- **Cliente**: [customer-name]
- **Iniciativa**: [initiative summary]
- **Carpeta de la iniciativa**: [<INITIATIVE_FOLDER>]
- **Fase actual**: [DISCOVERY / METRICS / QUANTIFICATION]
- **Última etapa completada**: [Stage X — Name]
- **Siguiente etapa**: [Stage Y — Name]

He creado un archivo de interacción para capturar cómo quieres proceder — consulta la ruta abajo.
```

### Paso 2 — Decisión de reanudación en un archivo

Crea un archivo de interacción numerado secuencialmente dentro de `<INITIATIVE_FOLDER>/00-session-setup/` (usando el siguiente prefijo no usado, p. ej., `03-session-resume-questions.md`). Usa esta estructura:

```markdown
# Reanudación de sesión — Siguiente paso

## Qué estás decidiendo
Dónde retomar tu iniciativa AI-BVIF existente. Ya leí tu `bvif-state.md` y los artefactos de las etapas completadas, así que sé exactamente dónde te quedaste. Tienes dos opciones realistas:

- **Continuar** — avanzar a la siguiente etapa ([Next stage description]). Retomaré el flujo de trabajo desde ahí.
- **Revisar una etapa anterior** — releer los artefactos de una etapa previa (y opcionalmente reabrirla para cambios) antes de avanzar. Útil si algo anterior necesita corregirse antes de comprometerte con el siguiente paso.

Este archivo es solo para decidir la siguiente acción — no estás aprobando ningún contenido aquí. Responde abajo y actuaré en consecuencia.

---

## Pregunta 1
¿Qué te gustaría hacer?

A) Continuar donde te quedaste ([Next stage description])
B) Revisar una etapa anterior (por favor especifica cuál después de la etiqueta [Answer]: abajo)
X) Otro (por favor descríbelo después de la etiqueta [Answer]: abajo)

[Answer]:
```

Anuncia la ruta del archivo en el chat y espera a que el usuario responda antes de continuar.

## OBLIGATORIO: Instrucciones de continuidad de sesión
1. **Identifica primero la carpeta de la iniciativa activa**:
   - Escanea `bvif-docs/` en busca de subcarpetas que coincidan con el patrón `<NN>-<slug>-<yyyymm>/` (ignora la carpeta de preparación `_pending-session/`)
   - Si existe más de una, crea un archivo de preguntas numerado secuencialmente en `bvif-docs/_pending-session/` (p. ej., `01-session-resume-selection-questions.md`) preguntando al usuario qué iniciativa reanudar, con cada iniciativa listada como una opción con letra
   - Si solo existe una, úsala
   - Si no existe ninguna, trata esto como un proyecto nuevo y comienza desde la Configuración de la sesión
2. **Siempre lee primero `<INITIATIVE_FOLDER>/bvif-state.md`** al detectar un proyecto existente
3. **Analiza el estado actual** del archivo de estado para poblar el anuncio en el chat y el archivo de interacción de reanudación
4. **Carga los artefactos de las etapas previas** — Antes de reanudar, lee todos los artefactos relevantes de las etapas completadas:
   - **Configuración de la sesión**: Lee el contexto del cliente, el resumen de la iniciativa
   - **Etapa 1**: Lee `<INITIATIVE_FOLDER>/01-initiative-definition/initiative-definition.md`
   - **Etapa 2**: Lee `<INITIATIVE_FOLDER>/02-business-value-mapping/business-value-mapping.md`
   - **Etapa 3**: Lee `<INITIATIVE_FOLDER>/03-metrics-identification/metrics-table.md`, `feasibility-table.md`
   - **Etapa 4**: Lee `<INITIATIVE_FOLDER>/04-metrics-adjustment/decision-log.md`, `final-metrics-list.md`
   - **Etapa 5**: Lee `<INITIATIVE_FOLDER>/05-data-collection/data-collection.md`. Si una sesión de la Etapa 5 está a medias (sin archivo de aprobación respondido aún), lista también el contenido de `<INITIATIVE_FOLDER>/05-data-collection/uploads/` (si existe) para saber si el usuario estaba en la ruta de respuestas en línea o en la ruta de carga de documentos, y lee cualquier archivo subido antes de continuar.
   - **Etapa 6**: Lee `<INITIATIVE_FOLDER>/06-business-value-calculation/business-value-calculation.md`
   - **Etapa 7**: Lee `<INITIATIVE_FOLDER>/07-final-results/final-results.md`
5. **Muestra los siguientes pasos específicos** en el archivo de interacción de reanudación en lugar de descripciones genéricas
6. **Registra la interacción de reanudación** (tanto el anuncio como la ruta del archivo) en `<INITIATIVE_FOLDER>/audit.md` con marca de tiempo

## Manejo de errores
Si faltan artefactos o están corruptos durante la reanudación de la sesión:
1. Informa al usuario en el chat qué artefactos faltan
2. Crea un archivo de preguntas numerado secuencialmente dentro de la subcarpeta de la etapa afectada preguntando si re-ejecutar la etapa o abortar
3. No avances más allá de una etapa con artefactos prerrequisito faltantes
