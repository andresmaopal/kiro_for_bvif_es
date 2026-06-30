# Cuando el usuario solicita una identificación de valor de negocio, SIEMPRE sigue este flujo de trabajo PRIMERO

## Principio de flujo de trabajo adaptativo
**El flujo de trabajo se adapta a la iniciativa, no al revés.**

El modelo de IA evalúa inteligentemente qué etapas se necesitan con base en:
1. La iniciativa de IA declarada por el usuario y su claridad
2. Los artefactos existentes y la disponibilidad de datos
3. La complejidad y el alcance de la iniciativa
4. El contexto de la industria y los requisitos de las partes interesadas

## OBLIGATORIO: Carga de los detalles de reglas
**CRÍTICO**: Al realizar cualquier fase, DEBES leer y usar el contenido relevante de los archivos de detalle de reglas en:
- `.kiro/bvif-rule-details/` (Kiro IDE)

Todas las referencias subsiguientes a archivos de detalle de reglas (p. ej., `common/process-overview.md`, `stages/stage-1-initiative-definition.md`) son relativas al directorio de detalles de reglas resuelto.

**Reglas comunes**: SIEMPRE carga las reglas comunes al inicio del flujo de trabajo:
- Carga `common/process-overview.md` para el resumen del flujo de trabajo
- Carga `common/session-continuity.md` para la guía de reanudación de sesión
- Carga `common/question-format-guide.md` para las reglas de formato de preguntas
- Referéncialas a lo largo de la ejecución del flujo de trabajo

## OBLIGATORIO: Todas las interacciones con el usuario se basan en archivos
**CRÍTICO**: Cada interacción con el usuario que requiera una respuesta — preguntas aclaratorias, aprobaciones de etapa, confirmaciones e incluso la primera pregunta durante la Configuración de la sesión — DEBE capturarse en un archivo de interacción. **Nunca hagas preguntas ni solicites aprobaciones en el chat.** El chat solo se usa para anunciar que se ha creado un archivo y para acusar recibo de la finalización.

Consulta `common/question-format-guide.md` para la estructura completa, la numeración secuencial (`01-`, `02-`, …) acotada por subcarpeta de etapa, y el flujo de trabajo para crear, leer y dar seguimiento a los archivos de interacción.

## OBLIGATORIO: No ofrezcas el modo Spec
**CRÍTICO**: El flujo de trabajo BVIF es en sí mismo un proceso estructurado de múltiples etapas con sus propias fases, aprobaciones y artefactos. NO es un Spec de Kiro y NO DEBE envolverse en uno. Cuando cualquier solicitud del usuario active este flujo de trabajo — o en cualquier punto durante una sesión BVIF activa — DEBES:

- **Nunca sugerir, proponer ni ofrecer** ejecutar este trabajo como un Spec de Kiro.
- **Nunca preguntar** si el usuario quiere "formalizar esto como un spec", "crear un spec para esto", o cualquier frase equivalente.
- **Declinar cortésmente** si el usuario pide convertir una sesión BVIF en un Spec — explica que BVIF ya proporciona su propio flujo de trabajo secuencial con compuertas de aprobación y que envolverlo en un Spec duplicaría el proceso.

La única excepción es si el usuario está trabajando explícitamente fuera de BVIF (p. ej., editando el propio código del marco o los archivos de steering como colaborador). En ese caso, el modo Spec puede ofrecerse para ese trabajo fuera de banda si genuinamente encaja, pero nunca para la sesión BVIF en sí.

## OBLIGATORIO: Mensaje de bienvenida personalizado
**CRÍTICO**: Al iniciar CUALQUIER solicitud de identificación de valor de negocio, DEBES mostrar el mensaje de bienvenida.

**Cómo mostrar el mensaje de bienvenida**:
1. Carga el mensaje de bienvenida de `common/welcome-message.md` (en el directorio de detalles de reglas resuelto)
2. Muestra el mensaje completo al usuario
3. Esto solo debe hacerse UNA VEZ al inicio de un nuevo flujo de trabajo
4. NO cargues este archivo en interacciones subsiguientes para ahorrar espacio de contexto

# Flujo de trabajo del AI Business Value Identification Framework (AI-BVIF)

---

# 🔵 FASE DE DESCUBRIMIENTO

**Propósito**: Entender al cliente, la iniciativa de IA y mapearla a categorías de valor de negocio

**Enfoque**: Determinar QUÉ es la iniciativa y POR QUÉ importa

**Etapas en la FASE DE DESCUBRIMIENTO**:
- Configuración de la sesión (SIEMPRE)
- Etapa 1 — Refinar la definición de la iniciativa (SIEMPRE)
- Etapa 2 — Mapeo de valor de negocio (SIEMPRE)

---

## Configuración de la sesión (EJECUTAR SIEMPRE)

> A partir de esta etapa, cada referencia a `audit.md`, `bvif-state.md`, o cualquier subcarpeta de etapa (`00-session-setup/` hasta `07-final-results/`) se refiere al archivo o carpeta **dentro de la carpeta de la iniciativa activa** bajo `bvif-docs/`, nunca en la raíz de `bvif-docs/`. Consulta "Creación de la carpeta de la iniciativa (OBLIGATORIO)" más abajo para saber cómo se elige esa carpeta.

1. **OBLIGATORIO**: Registra la solicitud inicial del usuario. Como la carpeta de la iniciativa aún no existe, almacena esta entrada en búfer y escríbela en `audit.md` tan pronto como se cree la carpeta de la iniciativa (Paso 7 del procedimiento de Creación de la carpeta de la iniciativa).
2. Carga todos los pasos de `stages/session-setup.md`
3. Ejecuta la configuración de la sesión:
   - Verifica si hay carpetas de iniciativa existentes bajo `bvif-docs/` (reanuda si el usuario está continuando una iniciativa existente)
   - Identifica el nombre del cliente, la industria y el contexto
   - Confirma la iniciativa de IA a evaluar
   - **OBLIGATORIO**: Crea una carpeta dedicada para la iniciativa (ver "Creación de la carpeta de la iniciativa" más abajo)
   - Establece la estructura del espacio de trabajo dentro de la carpeta de la iniciativa
4. **OBLIGATORIO**: Registra los hallazgos en audit.md (dentro de la nueva carpeta de la iniciativa)
5. Presenta el mensaje de finalización al usuario, incluyendo la ruta completa de la carpeta de la iniciativa recién creada
6. Procede automáticamente a la Etapa 1

### Creación de la carpeta de la iniciativa (OBLIGATORIO)

Cada nueva iniciativa de IA DEBE tener su propia carpeta dedicada bajo `bvif-docs/`. Todos los artefactos intermedios y finales de esa iniciativa — incluidos `bvif-state.md`, `audit.md` y cada subcarpeta de etapa (`00-session-setup/` hasta `07-final-results/`) — DEBEN vivir dentro de esa carpeta de la iniciativa.

**Pasos**:

1. **Pregunta al usuario por el nombre de la iniciativa** si no se proporcionó ya en la solicitud inicial. Esta pregunta DEBE colocarse en un archivo de interacción, no hacerse en el chat. Como la carpeta de la iniciativa aún no existe, crea el archivo en la carpeta de preparación previa a la iniciativa:

   ```
   bvif-docs/_pending-session/01-session-setup-questions.md
   ```

   Usa la estructura definida en `common/question-format-guide.md`. La pregunta debe cubrir el nombre de la iniciativa y cualquier otro campo faltante de la Configuración de la sesión (nombre del cliente, industria, patrocinador, etc.) como bloques `## Pregunta N` separados. Anuncia la ruta del archivo en el chat y espera a que el usuario lo complete antes de proceder.

2. **Genera un slug corto y sin espacios** a partir del nombre de la iniciativa:
   - Pon todo en minúsculas
   - Reemplaza espacios y puntuación con guiones (`-`)
   - Elimina palabras de relleno (`el`, `la`, `los`, `de`, `para`, `y`; o sus equivalentes en inglés `the`, `a`, `an`, `of`, `for`, `and`) cuando sea necesario para mantener el slug corto
   - Mantén el slug en aproximadamente 3–5 palabras, máximo 40 caracteres
   - Elimina cualquier carácter que no sea `a-z`, `0-9` o `-`
   - Colapsa guiones consecutivos y recorta los guiones iniciales/finales

3. **Determina el número de secuencia consecutivo**:
   - Escanea las carpetas existentes directamente bajo `bvif-docs/` (excluyendo archivos como `bvif-state.md` y `audit.md` si existen en ese nivel por ejecuciones heredadas)
   - Encuentra el prefijo de dos dígitos más alto existente (p. ej., `01`, `02`, `03`)
   - Usa el siguiente número, con relleno de ceros a dos dígitos (p. ej., `04`)
   - Si aún no existen carpetas de iniciativa, empieza en `01`

4. **Determina el sufijo de fecha**:
   - Usa el año y mes actuales en formato `yyyymm` (p. ej., `202604` para abril de 2026)

5. **Compón el nombre final de la carpeta** usando este patrón exacto:
   ```
   <NN>-<initiative-slug>-<yyyymm>
   ```
   Ejemplos:
   - `01-customer-churn-predictor-202604`
   - `02-contact-center-ai-assistant-202604`
   - `03-invoice-auto-classification-202605`

6. **Confirma el nombre de la carpeta con el usuario** antes de crearla. Esta confirmación DEBE ser también una interacción basada en archivo — crea el siguiente archivo de aprobación numerado secuencialmente en la carpeta de preparación:

   ```
   bvif-docs/_pending-session/02-session-setup-approval.md
   ```

   Muestra la ruta propuesta (p. ej., `bvif-docs/01-customer-churn-predictor-202604/`) en el párrafo de contexto, con opciones de aprobar / solicitar-un-slug-diferente / otro. Espera la aprobación explícita. Si el usuario solicita un slug diferente, regenéralo y crea el siguiente archivo de aprobación numerado secuencialmente (p. ej., `03-session-setup-approval.md`).

7. **Crea la carpeta y su andamiaje** una vez aprobado:
   - Crea `bvif-docs/<NN>-<initiative-slug>-<yyyymm>/`
   - Crea las siete subcarpetas de etapa (`00-session-setup/` hasta `07-final-results/`)
   - Crea `bvif-state.md` y `audit.md` vacíos dentro de la carpeta de la iniciativa
   - **Mueve** cada archivo de interacción de `bvif-docs/_pending-session/` a `<INITIATIVE_FOLDER>/00-session-setup/`, preservando los nombres de archivo y los números de secuencia, luego limpia la carpeta de preparación.

8. **De este punto en adelante, todas las referencias a archivos en el flujo de trabajo** (p. ej., `bvif-state.md`, `audit.md`, `00-session-setup/`, `01-initiative-definition/`, etc.) DEBEN interpretarse como relativas a la carpeta de la iniciativa, NO directamente a `bvif-docs/`.

## Etapa 1 — Refinar la definición de la iniciativa (EJECUTAR SIEMPRE)

1. **OBLIGATORIO**: Registra cualquier entrada del usuario durante esta etapa en audit.md
2. Carga todos los pasos de `stages/stage-1-initiative-definition.md`
3. Ejecuta la definición de la iniciativa:
   - Analiza la idea cruda de la iniciativa de IA
   - Aclara qué hace la iniciativa
   - Identifica los beneficios y las principales partes interesadas
   - Identifica al propietario del presupuesto
   - Produce una descripción clara y en lenguaje sencillo
4. **Espera la aprobación explícita vía archivo**: Crea un archivo de aprobación numerado secuencialmente en `<INITIATIVE_FOLDER>/01-initiative-definition/` (p. ej., `NN-initiative-definition-approval.md`) que contenga la definición refinada de la iniciativa más opciones de aprobar / solicitar-cambios según `common/question-format-guide.md`. Anuncia el archivo en el chat y NO PROCEDAS hasta que el usuario confirme.
5. **OBLIGATORIO**: Registra la respuesta del usuario en audit.md con la entrada cruda completa

## Etapa 2 — Mapeo de valor de negocio (EJECUTAR SIEMPRE)

1. **OBLIGATORIO**: Registra cualquier entrada del usuario durante esta etapa en audit.md
2. Carga todos los pasos de `stages/stage-2-business-value-mapping.md`
3. Ejecuta el mapeo de valor de negocio:
   - Mapea la iniciativa a las categorías de valor de negocio de CAF v3
   - Identifica las categorías primaria y secundaria
   - Justifica la selección de categorías
   - Mantén las categorías al mínimo
4. **Espera la aprobación explícita vía archivo**: Crea un archivo de aprobación numerado secuencialmente en `<INITIATIVE_FOLDER>/02-business-value-mapping/` (p. ej., `NN-business-value-mapping-approval.md`) que contenga el mapeo de categorías más opciones de aprobar / solicitar-cambios según `common/question-format-guide.md`. Anuncia el archivo en el chat y NO PROCEDAS hasta que el usuario confirme.
5. **OBLIGATORIO**: Registra la respuesta del usuario en audit.md con la entrada cruda completa

---

# 🟢 FASE DE MÉTRICAS

**Propósito**: Identificar, evaluar la factibilidad y refinar las métricas que demuestran el valor de negocio

**Enfoque**: Determinar CÓMO medir el éxito

**Etapas en la FASE DE MÉTRICAS**:
- Etapa 3 — Identificación y factibilidad de métricas (SIEMPRE)
  - Tarea 1: Identificar métricas
  - Tarea 2: Evaluar la factibilidad de las métricas
- Etapa 4 — Ajuste de métricas (SIEMPRE)

---

## Etapa 3 — Identificación y factibilidad de métricas (EJECUTAR SIEMPRE)

### Tarea 1 — Identificar métricas

1. **OBLIGATORIO**: Registra cualquier entrada del usuario durante esta etapa en audit.md
2. Carga todos los pasos de `stages/stage-3-task-1-metrics-identification.md`
3. Ejecuta la identificación de métricas:
   - Para cada categoría de valor de negocio, identifica las métricas relevantes
   - Proporciona el nombre de la métrica, la definición aritmética y la explicación
   - Marca las métricas más relevantes con un asterisco (*)
   - Asegura al menos 1 métrica por categoría, no más de 10
   - Cada métrica debe ser un número absoluto, porcentaje o moneda
4. **Espera la aprobación explícita vía archivo**: Crea un archivo de aprobación numerado secuencialmente en `<INITIATIVE_FOLDER>/03-metrics-identification/` (p. ej., `NN-metrics-identification-approval.md`) que contenga la tabla de métricas más opciones de aprobar / solicitar-cambios según `common/question-format-guide.md`. Anuncia el archivo en el chat y NO PROCEDAS hasta que el usuario confirme.
5. **OBLIGATORIO**: Registra la respuesta del usuario en audit.md con la entrada cruda completa

### Tarea 2 — Evaluar la factibilidad de las métricas

1. **OBLIGATORIO**: Registra cualquier entrada del usuario durante esta etapa en audit.md
2. Carga todos los pasos de `stages/stage-3-task-2-metrics-feasibility.md`
3. Ejecuta la evaluación de factibilidad:
   - Asigna una etiqueta de factibilidad a cada métrica (F1, F2, F3)
   - Agrega comentarios opcionales por métrica
   - Guía al usuario a través de las preguntas de factibilidad
4. **Espera la aprobación explícita vía archivo**: Crea un archivo de aprobación numerado secuencialmente en `<INITIATIVE_FOLDER>/03-metrics-identification/` (p. ej., `NN-metrics-feasibility-approval.md`) que contenga la tabla de factibilidad más opciones de aprobar / solicitar-cambios según `common/question-format-guide.md`. Anuncia el archivo en el chat y NO PROCEDAS hasta que el usuario confirme.
5. **OBLIGATORIO**: Registra la respuesta del usuario en audit.md con la entrada cruda completa

## Etapa 4 — Ajuste de métricas (EJECUTAR SIEMPRE)

1. **OBLIGATORIO**: Registra cualquier entrada del usuario durante esta etapa en audit.md
2. Carga todos los pasos de `stages/stage-4-metrics-adjustment.md`
3. Ejecuta el ajuste de métricas:
   - Aplica las decisiones: Conservar tal cual, Activar, Reemplazar con proxy, Diferir, Eliminar
   - Produce el registro de decisiones con razonamiento
   - Produce la lista finalizada de métricas
   - Marca las métricas F3 críticas sin proxy (condición de PARADA)
4. **Espera la aprobación explícita vía archivo**: Crea un archivo de aprobación numerado secuencialmente en `<INITIATIVE_FOLDER>/04-metrics-adjustment/` (p. ej., `NN-metrics-adjustment-approval.md`) que contenga el registro de decisiones y las métricas finales más opciones de aprobar / solicitar-cambios según `common/question-format-guide.md`. Anuncia el archivo en el chat y NO PROCEDAS hasta que el usuario confirme.
5. **OBLIGATORIO**: Registra la respuesta del usuario en audit.md con la entrada cruda completa

---

# 🟡 FASE DE CUANTIFICACIÓN

**Propósito**: Recolectar datos, calcular el valor de negocio y producir el documento de resultados finales

**Enfoque**: Determinar CUÁNTO valor entrega la iniciativa

**Etapas en la FASE DE CUANTIFICACIÓN**:
- Etapa 5 — Recolección de datos (SIEMPRE)
- Etapa 6 — Cálculo del valor de negocio (SIEMPRE)
- Etapa 7 — Documentación de resultados finales (SIEMPRE)

---

## Etapa 5 — Recolección de datos (EJECUTAR SIEMPRE)

1. **OBLIGATORIO**: Registra cualquier entrada del usuario durante esta etapa en audit.md
2. Carga todos los pasos de `stages/stage-5-data-collection.md`
3. Ejecuta la recolección de datos:
   - **Pregunta al usuario cómo quiere proporcionar los datos** vía `01-data-collection-questions.md` — respuestas en línea, carga de documentos, o una mezcla
   - **Si es en línea**: crea archivos de preguntas de seguimiento con preguntas de datos por métrica y espera las respuestas
   - **Si son cargas**: crea `<INITIATIVE_FOLDER>/05-data-collection/uploads/` con un README corto que explique qué colocar (solo texto plano o markdown, sin binarios, sin secretos); espera a que el usuario confirme que las cargas están completas; luego lee los archivos, extrae los datos con atribución de fuente y una etiqueta de **Fidelidad de la Fuente** (ver `common/process-overview.md` → "Niveles de Fidelidad de la Fuente de la Etapa 5"), y crea un archivo de respuestas extraídas para que el usuario valide cada valor
   - Haz preguntas de seguimiento dirigidas (en archivos numerados secuencialmente) para cualquier dato no encontrado en las cargas o aún poco claro
   - Una vez reunidos todos los datos: establece la línea base actual, ~8 trimestres de tendencia histórica, el impacto financiero por unidad, el benchmark de la industria y el objetivo de mejora para cada métrica
   - Registra la **procedencia de los datos** (respuesta en línea, nombre de archivo subido, o estimación) en cada valor del artefacto final
4. **Espera la aprobación explícita vía archivo**: Crea un archivo de aprobación numerado secuencialmente en `<INITIATIVE_FOLDER>/05-data-collection/` (p. ej., `NN-data-collection-approval.md`) que contenga los resultados de la recolección de datos más opciones de aprobar / solicitar-cambios según `common/question-format-guide.md`. Anuncia el archivo en el chat y NO PROCEDAS hasta que el usuario confirme.
5. **OBLIGATORIO**: Registra la respuesta del usuario en audit.md con la entrada cruda completa. Si se subieron documentos, registra también la lista de archivos leídos y de qué archivo vino cada dato.

## Etapa 6 — Cálculo del valor de negocio (EJECUTAR SIEMPRE)

1. **OBLIGATORIO**: Registra cualquier entrada del usuario durante esta etapa en audit.md
2. Carga todos los pasos de `stages/stage-6-business-value-calculation.md`
3. Ejecuta el cálculo del valor de negocio:
   - Clasifica cada métrica como financiera o no financiera
   - Calcula el valor monetario anualizado para las métricas financieras
   - Documenta la mejora esperada para las métricas no financieras
   - Verifica el doble conteo entre métricas
   - Produce la tabla resumen
4. **Espera la aprobación explícita vía archivo**: Crea un archivo de aprobación numerado secuencialmente en `<INITIATIVE_FOLDER>/06-business-value-calculation/` (p. ej., `NN-business-value-calculation-approval.md`) que contenga los resultados del cálculo más opciones de aprobar / solicitar-cambios según `common/question-format-guide.md`. Anuncia el archivo en el chat y NO PROCEDAS hasta que el usuario confirme.
5. **OBLIGATORIO**: Registra la respuesta del usuario en audit.md con la entrada cruda completa

## Etapa 7 — Documentación de resultados finales (EJECUTAR SIEMPRE)

1. **OBLIGATORIO**: Registra cualquier entrada del usuario durante esta etapa en audit.md
2. Carga todos los pasos de `stages/stage-7-final-results.md`
3. Ejecuta la documentación final:
   - Produce el resumen consolidado de valor de negocio
   - Incluye la tabla de valor de negocio anual total cuantificado
   - **Produce una tabla consolidada de métricas** que liste cada métrica exactamente una vez con su definición, línea base, objetivo, mejora esperada (% y $), valor anualizado, explicación del cálculo, cadencia de medición, fuente de datos/propietario, procedencia de datos y notas. Esta tabla es el artefacto de traspaso para el equipo que implementará y rastreará la iniciativa. Las métricas con valor financiero capturado en otro lugar permanecen en la tabla (para el rastreo operativo) pero se marcan como "Captured in Metric [N]" para proteger el total financiero del doble conteo.
   - Incluye una sección corta de aspectos no financieros destacados para el enmarcado ejecutivo (la lista no financiera exhaustiva vive en la tabla consolidada)
   - Documenta el valor estratégico más allá de los números
   - Documenta el riesgo de la inacción
   - Incluye apéndices: definición condensada de la iniciativa y metodología AI-BVIF
4. **Espera la aprobación explícita vía archivo**: Crea un archivo de aprobación numerado secuencialmente en `<INITIATIVE_FOLDER>/07-final-results/` (p. ej., `NN-final-results-approval.md`) que contenga el documento final más opciones de aprobar / solicitar-cambios según `common/question-format-guide.md`. Anuncia el archivo en el chat y NO PROCEDAS hasta que el usuario confirme.
5. **OBLIGATORIO**: Registra la respuesta del usuario en audit.md con la entrada cruda completa

---

## Principios clave

- **Ejecución secuencial**: Las etapas se ejecutan en orden (1 a 7), cada una construyendo sobre las salidas previas
- **Progreso transparente**: Siempre muestra la etapa actual y qué sigue
- **Control del usuario**: El usuario aprueba cada etapa antes de continuar
- **Seguimiento del progreso**: Actualiza `<INITIATIVE_FOLDER>/bvif-state.md` después de completar cada etapa
- **Registro de auditoría completo**: Registra TODAS las entradas del usuario y las respuestas de la IA en `<INITIATIVE_FOLDER>/audit.md` con marcas de tiempo
- **Documenta todo**: Almacena los artefactos intermedios y finales con prefijos de secuencia
- **Sin doble conteo**: Siempre verifica la superposición de métricas antes de sumar valores financieros
- **Lenguaje sencillo**: Escribe para no expertos de la industria cuando sea posible

## OBLIGATORIO: Cumplimiento de las casillas

### REGLAS OBLIGATORIAS PARA LA EJECUCIÓN DE ETAPAS
1. **NUNCA completes ningún trabajo sin actualizar las casillas de etapa en `<INITIATIVE_FOLDER>/bvif-state.md`**
2. **INMEDIATAMENTE después de completar CUALQUIER etapa, marca esa etapa con [x]**
3. **Esto debe suceder en la MISMA interacción donde se completa el trabajo**

## Requisitos de registro de prompts
- **OBLIGATORIO**: Registra CADA entrada del usuario con marca de tiempo en `<INITIATIVE_FOLDER>/audit.md`
- **OBLIGATORIO**: Captura la ENTRADA CRUDA COMPLETA del usuario exactamente como se proporcionó (nunca resumas)
- **CRÍTICO**: SIEMPRE anexa a `<INITIATIVE_FOLDER>/audit.md`, NUNCA sobrescribas su contenido
- Usa el formato ISO 8601 para las marcas de tiempo

### Formato del registro de auditoría:
```markdown
## [Stage Name]
**Timestamp**: [ISO timestamp]
**User Input**: "[Complete raw user input]"
**AI Response**: "[AI's response or action taken]"
**Context**: [Stage, action, or decision made]

---
```

## Estructura de directorios

Cada iniciativa de IA vive en su propia carpeta dedicada bajo `bvif-docs/`. El nombre de la carpeta sigue el patrón `<NN>-<initiative-slug>-<yyyymm>` donde `<NN>` es un número consecutivo con relleno de ceros que empieza en `01` y `<yyyymm>` es el año y mes en que se inició la iniciativa.

```text
<WORKSPACE-ROOT>/
├── bvif-docs/                                              # 📄 TODA LA DOCUMENTACIÓN BVIF
│   ├── _pending-session/                                   # 🕒 Preparación (solo existe antes de crear una carpeta de iniciativa)
│   │   └── 01-session-setup-questions.md                   # Primer archivo de interacción; se mueve a la carpeta de la iniciativa una vez creada
│   ├── 01-customer-churn-predictor-202604/                 # Iniciativa #1 (ejemplo)
│   │   ├── 00-session-setup/                               # Contexto de la sesión + archivos de interacción de configuración
│   │   │   ├── 01-session-setup-questions.md               # Movido aquí desde _pending-session/
│   │   │   ├── 02-session-setup-approval.md                # Numerado secuencialmente (preguntas + aprobaciones intercaladas)
│   │   │   └── session-context.md
│   │   ├── 01-initiative-definition/                       # Salidas de la Etapa 1 + archivos de interacción
│   │   │   ├── 01-initiative-definition-questions.md       # (solo si se necesitaron preguntas aclaratorias)
│   │   │   ├── 02-initiative-definition-approval.md
│   │   │   └── initiative-definition.md
│   │   ├── 02-business-value-mapping/                      # Salidas de la Etapa 2
│   │   ├── 03-metrics-identification/                      # Salidas de la Etapa 3 Tareas 1 y 2 (secuencia compartida)
│   │   ├── 04-metrics-adjustment/                          # Salidas de la Etapa 4
│   │   ├── 05-data-collection/                             # Salidas de la Etapa 5
│   │   │   └── uploads/                                    # Opcional — documentos fuente provistos por el humano (si el usuario eligió la ruta de carga)
│   │   ├── 06-business-value-calculation/                  # Salidas de la Etapa 6
│   │   ├── 07-final-results/                               # Documento final de la Etapa 7
│   │   ├── bvif-state.md                                   # Seguimiento de progreso (esta iniciativa)
│   │   └── audit.md                                        # Registro de auditoría completo (esta iniciativa)
│   └── 02-contact-center-ai-assistant-202604/              # Iniciativa #2 (ejemplo)
│       ├── 00-session-setup/
│       ├── 01-initiative-definition/
│       ├── ...
│       ├── bvif-state.md
│       └── audit.md
```

**Reglas**:
- `bvif-state.md` y `audit.md` están acotados a una sola iniciativa y DEBEN vivir dentro de la carpeta de esa iniciativa. Nunca los escribas en la raíz de `bvif-docs/`.
- Todas las salidas intermedias de etapa (00–07) DEBEN vivir dentro de la carpeta de la iniciativa a la que pertenecen.
- **Los archivos de interacción** (preguntas + aprobaciones) dentro de cada subcarpeta `XX-stage/` usan un prefijo `NN-` de dos dígitos que se incrementa en el orden en que el agente los creó dentro de esa etapa. Las preguntas y las aprobaciones comparten la misma secuencia — el que se cree a continuación obtiene el siguiente número. Consulta `common/question-format-guide.md` para las reglas completas de nombres.
- `bvif-docs/_pending-session/` es el hogar temporal del primer archivo de interacción (antes de que exista la carpeta de la iniciativa). Su contenido DEBE moverse a `<INITIATIVE_FOLDER>/00-session-setup/` tan pronto como se cree la carpeta de la iniciativa; la carpeta de preparación se vacía o se elimina entonces.
- Al reanudar el trabajo, primero identifica qué carpeta de iniciativa está activa, luego lee el `bvif-state.md` de esa carpeta para determinar la etapa actual.
