# Guía de formato de preguntas

> **Convención de rutas**: `<INITIATIVE_FOLDER>` se refiere a la carpeta por iniciativa bajo `bvif-docs/` (p. ej., `bvif-docs/01-customer-churn-predictor-202604`). Consulta `common/process-overview.md` → "Convención de rutas: carpeta por iniciativa".

## OBLIGATORIO: Todas las interacciones deben usar archivos

### Regla: Nunca hagas preguntas ni solicites aprobaciones en el chat
**CRÍTICO**: NUNCA debes hacer preguntas ni solicitar aprobaciones directamente en el chat. CADA interacción con el usuario que requiera una respuesta — preguntas aclaratorias, aprobaciones de etapa, confirmaciones e incluso la primera pregunta (el nombre de la iniciativa) — DEBE colocarse en un archivo de interacción dedicado.

El chat se reserva solo para tres cosas:
1. Anunciar que se ha creado un archivo de interacción, dónde se ubica y cómo responderlo.
2. Acusar recibo de la respuesta del usuario y resumir qué sucederá a continuación.
3. Mostrar contenido no interactivo (mensaje de bienvenida, resúmenes de finalización de etapa, actualizaciones de estado).

**Sin excepciones**. Esto incluye la Configuración de la sesión: el nombre de la iniciativa se captura mediante un archivo en una ubicación de preparación previa a la iniciativa (ver "Carpeta de preparación previa a la iniciativa" más abajo) porque la carpeta de la iniciativa aún no existe.

### Dos tipos de archivos de interacción

Cada archivo de interacción usa la misma estructura descrita más abajo. La única diferencia es la intención:

| Tipo | Propósito | Sufijo del nombre de archivo |
|---|---|---|
| **Archivo de preguntas** | Reunir información o aclarar ambigüedad del usuario | `-questions.md` |
| **Archivo de aprobación** | Solicitar la aprobación explícita del usuario para avanzar más allá de una compuerta de etapa | `-approval.md` |

### Convención de numeración secuencial

Cada archivo de interacción dentro de una subcarpeta `<INITIATIVE_FOLDER>/XX-stage/` DEBE llevar como prefijo un número de secuencia de dos dígitos que refleje el orden en que se creó **dentro de esa subcarpeta de etapa**.

- El primer archivo de interacción en una etapa es `01-`, el segundo es `02-`, y así sucesivamente.
- La numeración está acotada por subcarpeta de etapa; no continúa entre etapas.
- La numeración es continua entre archivos de preguntas Y archivos de aprobación — el que se cree a continuación obtiene el siguiente número.
- Nunca reutilices un número, incluso si un archivo de interacción previo es reemplazado por un archivo de aclaración.

**Formato**:

```
<INITIATIVE_FOLDER>/<XX-stage>/<NN>-<descriptive-name>-<questions|approval>.md
```

**Ejemplos**:

```
<INITIATIVE_FOLDER>/01-initiative-definition/01-initiative-definition-questions.md
<INITIATIVE_FOLDER>/01-initiative-definition/02-initiative-definition-approval.md
<INITIATIVE_FOLDER>/03-metrics-identification/01-metrics-identification-questions.md
<INITIATIVE_FOLDER>/03-metrics-identification/02-metrics-identification-approval.md
<INITIATIVE_FOLDER>/03-metrics-identification/03-metrics-feasibility-questions.md
<INITIATIVE_FOLDER>/03-metrics-identification/04-metrics-feasibility-approval.md
```

Esto hace que el orden cronológico de cada pregunta hecha y cada aprobación solicitada sea inmediatamente visible para el revisor humano.

### Carpeta de preparación previa a la iniciativa

Como la carpeta de la iniciativa no existe al inicio de la Configuración de la sesión, el primer archivo de interacción — que captura el nombre de la iniciativa y el contexto de sesión relacionado — vive en una carpeta de preparación previa a la iniciativa:

```
bvif-docs/_pending-session/01-session-setup-questions.md
```

Una vez creada la carpeta de la iniciativa (ver `stages/session-setup.md`), el archivo de preparación DEBE moverse a `<INITIATIVE_FOLDER>/00-session-setup/` con el mismo nombre de archivo. Mantén `bvif-docs/_pending-session/` vacía (o elimínala) después del movimiento. Cualquier pregunta adicional de Configuración de la sesión se crea directamente dentro de `<INITIATIVE_FOLDER>/00-session-setup/` usando el siguiente número de secuencia.

### Estructura del archivo de interacción

Cada archivo de interacción sigue la misma disposición:

```markdown
# <Stage Name> — <Questions | Approval>

## Qué estás <aprobando | decidiendo>
<Una explicación breve y en lenguaje sencillo — unas pocas oraciones, sin jerga — que le diga al lector:
 1. Qué se está pidiendo o qué decisión se está capturando.
 2. Qué papel juega esta interacción en el flujo de trabajo general (por qué importa, qué le sigue).
 3. Cualquier término o concepto clave que el lector necesite conocer para responder bien.
Si el contexto relevante vive fuera del flujo de trabajo (una especificación externa, un marco o un whitepaper), incluye un enlace directo para que el lector pueda profundizar. Mantén esta sección concisa — lo suficiente para decidir, no una re-enseñanza.>

## Dónde leer el artefacto completo
`<ruta al artefacto del que trata esta interacción, si lo hay>`

---

## Pregunta 1
[Texto de la pregunta claro y específico]

A) [Primera opción significativa]
B) [Segunda opción significativa]
[...opciones adicionales según sea necesario...]
X) Otro (por favor describe después de la etiqueta [Answer]: abajo)

[Answer]:

---

## Pregunta 2
[Siguiente pregunta, mismo formato]

A) ...
B) ...
X) Otro (por favor describe después de la etiqueta [Answer]: abajo)

[Answer]:
```

**Reglas para cada archivo de interacción**:
- La sección `## Qué estás <aprobando | decidiendo>` es OBLIGATORIA. Su función es permitir que el humano tome una decisión informada sin tener que reconstruir el contexto de memoria. Para archivos de aprobación es "Qué estás aprobando"; para archivos de preguntas es "Qué estás decidiendo" o "Qué necesitamos de ti".
- La sección `## Dónde leer el artefacto completo` es OBLIGATORIA cuando la interacción se refiere a un artefacto que el usuario debe revisar (p. ej., una definición, tabla o cálculo producido en esa etapa). Omítela solo cuando la interacción no tenga un artefacto separado (p. ej., una decisión de reanudar o revisar).
- Enlaza a fuentes externas autorizadas siempre que existan y ayuden al lector (marcos, estándares, whitepapers). Prefiere URLs directas sobre indicaciones vagas como "la documentación de AWS".

**Reglas para cada bloque de pregunta**:
- "Otro" es OBLIGATORIO como la ÚLTIMA opción (siempre etiquetada `X)`).
- Incluye solo opciones significativas — no rellenes para llenar espacios.
- Usa tantas o tan pocas opciones como tenga sentido (mínimo 2 + Otro).
- Una pregunta por bloque `## Pregunta N`. Se permiten múltiples bloques por archivo.

**Los archivos de aprobación** usan la misma estructura pero normalmente contienen una sola pregunta con dos opciones estándar más "Otro":

```markdown
A) Aprobar y continuar a <siguiente etapa o siguiente tarea>
B) Solicitar cambios (por favor describe después de la etiqueta [Answer]: abajo)
X) Otro (por favor describe después de la etiqueta [Answer]: abajo)

[Answer]:
```

### Formato de respuesta del usuario

Los usuarios responden completando la opción de letra después de `[Answer]:`:

```markdown
[Answer]: C
```

Para respuestas de "Otro", los usuarios escriben la letra `X` seguida de texto libre en la misma línea o en la siguiente:

```markdown
[Answer]: X — ya rastreamos esta métrica trimestralmente vía el CRM
```

### Lectura de las respuestas del usuario

Después de que el usuario señale que terminó (en el chat, p. ej., "listo" o "respondido"):
1. Lee el archivo de interacción.
2. Extrae el valor después de cada etiqueta `[Answer]:`.
3. Valida que cada pregunta tenga una respuesta no vacía.
4. Procede con el análisis con base en las respuestas.

### Flujo de trabajo para cada interacción

1. **Crear**: Genera el archivo de interacción en la subcarpeta `<INITIATIVE_FOLDER>/XX-stage/` correcta, usando el siguiente número de secuencia disponible.
2. **Informar en el chat**: Dile al usuario (a) la ruta del archivo, (b) qué tipo de interacción es (preguntas vs aprobación) y (c) cómo responder. Ejemplo:
   > "He creado `<INITIATIVE_FOLDER>/01-initiative-definition/01-initiative-definition-questions.md` con 3 preguntas aclaratorias. Por favor completa la línea `[Answer]:` debajo de cada pregunta y avísame cuando termines."
3. **Esperar**: No procedas hasta que el usuario confirme que terminó.
4. **Leer**: Analiza las respuestas y valida la completitud.
5. **Aclarar**: Si se encuentran contradicciones o respuestas faltantes, crea un NUEVO archivo de interacción (con el siguiente número de secuencia) en lugar de editar el existente.
6. **Proceder**: Avanza solo cuando todas las respuestas sean consistentes y completas.

### Manejo de errores

#### Respuestas faltantes
Crea un nuevo archivo de interacción (con el siguiente número de secuencia) que contenga solo las preguntas sin responder, y dile al usuario en el chat:
> "Noté que la Pregunta [X] en `<file>` no está respondida. He creado `<new file>` con la(s) pregunta(s) restante(s). Por favor complétalo y avísame cuando termines."

#### Respuestas inválidas
Crea un nuevo archivo de interacción (con el siguiente número de secuencia) reformulando la pregunta con opciones o guía más claras, y dile al usuario en el chat:
> "La Pregunta [X] tiene una respuesta inválida. He creado `<new file>` reformulando la pregunta con opciones más claras. Por favor complétalo y avísame cuando termines."

### Buenas prácticas

- Sé específico y claro en el texto de la pregunta.
- Cubre los escenarios más comunes en las opciones.
- Haz las opciones mutuamente excluyentes.
- Siempre incluye "Otro" como la última opción.
- Mantén cada bloque `## Pregunta N` enfocado en un solo tema.
- Nunca modifiques un archivo de interacción existente después de que el usuario lo haya respondido — crea un nuevo archivo numerado secuencialmente para los seguimientos.
