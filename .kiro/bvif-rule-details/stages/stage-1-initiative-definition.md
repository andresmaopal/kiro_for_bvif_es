# Etapa 1 — Refinar la definición de la iniciativa

**Propósito**: Producir un enunciado claro y conciso que describa la iniciativa de IA. La descripción debe explicar qué hace la iniciativa, sus beneficios y sus principales partes interesadas — incluido quién tiene el presupuesto.

> **Convención de rutas**: `<INITIATIVE_FOLDER>` se refiere a la carpeta por iniciativa bajo `bvif-docs/` (p. ej., `bvif-docs/01-customer-churn-predictor-202604`). Consulta `common/process-overview.md` → "Convención de rutas: carpeta por iniciativa".

## Persona del agente

Adopta la persona definida en `stages/agents/stage-1-initiative-definition-agent.md` (Asesor de Iniciativas de IA de Negocio). Ese archivo es la fuente de verdad para el rol, el marco de preguntas, los lineamientos de comportamiento, el tono y la estructura de respuesta usados durante esta etapa — no repitas su contenido aquí.

## Prerrequisitos
- Configuración de la sesión completada
- Contexto del cliente e idea cruda de la iniciativa disponibles

## Paso 1: Analiza la iniciativa cruda

Lee el contexto de la sesión de `<INITIATIVE_FOLDER>/00-session-setup/session-context.md`. Analiza la idea cruda de la iniciativa e identifica:
- Qué hace la iniciativa (la capacidad de IA/ML)
- Qué problema resuelve
- Quién se beneficia de ella
- Quién tiene el presupuesto

## Paso 2: Haz preguntas aclaratorias (si es necesario)

Si la descripción de la iniciativa es vaga o le faltan elementos clave, crea un archivo de preguntas numerado secuencialmente dentro de `<INITIATIVE_FOLDER>/01-initiative-definition/` (p. ej., `01-initiative-definition-questions.md`). Sigue el marco de preguntas de la persona del agente — haz una pregunta por bloque `## Pregunta N` y enfócate en los resultados de negocio, no en los detalles técnicos. Consulta `common/question-format-guide.md` para la estructura completa y las reglas de numeración.

Áreas clave a aclarar:
- El proceso de negocio que se está mejorando
- El estado actual (cómo funcionan las cosas hoy sin IA)
- El estado futuro deseado (cómo funcionarán las cosas con IA)
- Las partes interesadas clave y la propiedad del presupuesto

## Paso 3: Redacta la definición refinada de la iniciativa

Escribe la definición de la iniciativa en lenguaje sencillo que un no experto de la industria pueda entender. Estructura:

1. **Quiénes somos**: Breve descripción de la empresa y su posición en el mercado
2. **Qué proponemos**: La iniciativa de IA y su capacidad central
3. **Estado actual**: Cómo funcionan las cosas hoy (el problema)
4. **Estado futuro**: Cómo funcionarán las cosas con IA (la solución)
5. **Áreas de impacto de negocio**: 2-3 áreas clave de beneficio esperado
6. **Propiedad del presupuesto**: Quién tiene el presupuesto y por qué esto se alinea con su mandato

**Lineamientos**:
- Lenguaje sencillo — sin jerga
- Sin datos ni explicaciones extensas en esta etapa
- Enfócate en la claridad de la comprensión
- Mantenlo conciso pero completo

## Paso 4: Guarda el artefacto

Guarda la definición refinada en `<INITIATIVE_FOLDER>/01-initiative-definition/initiative-definition.md`.

## Paso 5: Solicita la aprobación mediante un archivo

Crea un archivo de aprobación numerado secuencialmente dentro de `<INITIATIVE_FOLDER>/01-initiative-definition/` (p. ej., `NN-initiative-definition-approval.md` donde `NN` es el siguiente prefijo no usado en esa carpeta). Usa esta estructura:

```markdown
# Stage 1 — Initiative Definition Approval

## Qué estás aprobando
Una descripción en lenguaje sencillo de la iniciativa de IA: qué hace, quién se beneficia, cómo funcionan las cosas hoy vs. después de la iniciativa, y quién es dueño del presupuesto. Esta definición se convierte en la base sobre la que se construye cada etapa posterior — las métricas, la factibilidad y la cifra final de valor de negocio todas hacen referencia a ella. Aprobar significa que estás de acuerdo en que la descripción captura con exactitud la iniciativa que quieres evaluar.

## Dónde leer el artefacto completo
`<INITIATIVE_FOLDER>/01-initiative-definition/initiative-definition.md`

---

## Pregunta 1
¿Apruebas la definición refinada de la iniciativa?

A) Aprobar y continuar a la Etapa 2 — Mapeo de valor de negocio
B) Solicitar cambios (por favor describe después de la etiqueta [Answer]: abajo)
X) Otro (por favor describe después de la etiqueta [Answer]: abajo)

[Answer]:
```

Anuncia la ruta del archivo en el chat y **NO PROCEDAS** hasta que el usuario señale que terminó y la respuesta se resuelva como Aprobar.

## Paso 6: Actualiza el estado

Después de la aprobación, actualiza `<INITIATIVE_FOLDER>/bvif-state.md`:
- Marca la Etapa 1 como `[x]`
- Establece la etapa actual como "Stage 2 — Business Value Mapping"

Registra la aprobación en `<INITIATIVE_FOLDER>/audit.md`.
