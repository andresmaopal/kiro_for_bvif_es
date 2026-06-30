
**Fecha:** 2026-06-08  
**Versión:** v2 (en pruebas beta)

---

## Contexto

Esta versión de BVIF incorpora la cuantificación de la incertidumbre mediante simulación de Monte Carlo. Se probará con Coppel (minorista mexicano, ~1,800 tiendas, ~400 casos de uso de IA) en junio de 2026 como parte del programa beta de BVIF.

La idea central: una estimación puntual única (p. ej., "\$9.36M/año") es demasiado confiada para iniciativas de IA donde los resultados son inherentemente inciertos. Al recolectar estimaciones de tres puntos y ejecutar simulaciones, producimos un rango (P10/P50/P90) que refleja mejor la realidad y es más útil para la toma de decisiones.

**Las etapas 1–4 permanecen sin cambios respecto a v1.** Las etapas 5, 6 y 7 están mejoradas.

---

## Registro de cambios

| Versión | Fecha | Resumen |
|---------|------|---------|
| **v2 (actual)** | 2026-06-08 | Agrega cuantificación de la incertidumbre. Los objetivos de mejora y la tasa de adopción se recolectan como estimaciones de tres puntos (pesimista / más probable / optimista). La Etapa 6 ejecuta una simulación de Monte Carlo (10,000 iteraciones) sobre distribuciones triangulares, produciendo un rango P10/P50/P90 en lugar de un solo número. Agrega sustracción contrafactual de la línea base, análisis de sensibilidad (r de Pearson) y guía de palancas de influencia. Los entregables ahora incluyen un script de Python ejecutable y entradas JSON editables. |
| v1 | Antes de 2026-06 | Cálculo determinista. Cada entrada era un único valor puntual, la adopción era implícitamente del 100%, no se restaba ningún contrafactual y la salida era un único número de valor de negocio sin rango ni análisis de sensibilidad. |

El cambio de v1 a v2 intercambia una pequeña cantidad de tiempo adicional de las partes interesadas (~15–30 minutos por métrica) por una salida sustancialmente más honesta: un rango que refleja la incertidumbre real, además de una guía accionable sobre en qué entradas enfocarse para mejorar el resultado.

---

## Participantes requeridos

Una sesión BVIF necesita a las personas correctas en la sala para producir un resultado creíble. Tres roles son requeridos; uno es opcional pero útil.

| Rol | Por qué se necesita |
|------|--------------------|
| **Propietario de la iniciativa** (requerido) | La persona responsable de la iniciativa. Aporta una comprensión clara de qué se está construyendo, los beneficios buscados y el alcance. Es el ancla de las etapas 1–2. |
| **Representante de la línea de negocio** (requerido) | Alguien del área de negocio que la iniciativa impactará. Ayuda a identificar y aclarar cómo la iniciativa cambia las operaciones del día a día, quién se beneficia y cómo se ve una mejora realista. Es el ancla de las etapas 3 y 5 (objetivos de mejora, tasa de adopción). |
| **Profesional de datos** (requerido) | Alguien con acceso a los datos de la organización — operaciones, finanzas o analítica. Confirma si las métricas son medibles hoy, identifica las fuentes de datos para la línea base y la tendencia histórica, y propone cómo instrumentar métricas que aún no existen. Es el ancla de la etapa 4 (factibilidad) y la etapa 5 (líneas base, impacto financiero por unidad). |
| **Experto de la industria** (opcional pero útil) | Alguien con conocimiento intersectorial o de organización — experto en la materia interno, especialista de AWS o consultor externo. Aporta benchmarks de la industria y verifica la cordura de los objetivos de mejora frente a lo que los pares han logrado. Fortalece la etapa 5. |


Todos los participantes deben estar presentes **durante toda la duración del taller**, no solo en las etapas donde su rol es el ancla principal. La discusión multifuncional es en sí misma un entregable: el propietario de la iniciativa escucha cómo la línea de negocio interpreta los beneficios, el profesional de datos aprende qué métricas realmente importan a las operaciones, y la línea de negocio ve qué es y qué no es medible hoy. Estas conversaciones sacan a la luz supuestos que ningún rol detectaría por sí solo, y construyen entendimiento compartido y alineación en toda la organización que perdura más allá del propio documento BVIF.

Si alguno de los tres roles requeridos no puede asistir, aplaza la sesión — la salida será incompleta o poco confiable.


### Nota sobre herramientas asistidas por IA

Las herramientas asistidas por IA (p. ej., Amazon Q, Claude, ChatGPT) son valiosas a lo largo del proceso BVIF, pero **complementan, no reemplazan, a los participantes anteriores**. Aplicaciones útiles incluyen:

- **Etapas 2–3:** generar ideas de categorías de valor y métricas candidatas a partir de la descripción de la iniciativa.
- **Etapa 5:** redactar formulaciones neutrales de preguntas para las estimaciones de tres puntos, resumir datos de tendencia histórica, sugerir benchmarks de la industria para validar con el experto.
- **Etapa 6:** generar el script de Python de Monte Carlo y el archivo de entradas JSON a partir de los datos recolectados.
- **Etapa 7:** redactar el informe consolidado y renderizar las tablas de sensibilidad.

Los números en sí — objetivos de mejora, tasa de adopción, impacto financiero por unidad — deben provenir de los participantes humanos. Las herramientas de IA pueden ayudar a estructurar la conversación y acelerar los entregables, pero la credibilidad de BVIF descansa en el juicio de las partes interesadas.

---

## Etapa 1: Definición de la iniciativa

**Propósito:** Establecer qué es la iniciativa de IA y confirmar el alcance con la parte interesada.

- Recolectar una descripción en lenguaje sencillo de la iniciativa
- Refinar el alcance: qué se incluye, qué se excluye, quién se beneficia
- Confirmar la definición refinada con la parte interesada antes de continuar

**Salida:** Un documento de definición de la iniciativa claro y acordado.

---

## Etapa 2: Mapeo de valor de negocio

**Propósito:** Identificar qué categorías de valor podría impactar la iniciativa.

Mapea la iniciativa a una o más categorías de valor estándar (alineadas con AWS CAF):

| Categoría | Ejemplos |
|----------|----------|
| Aumentar los ingresos | Expandir mercados direccionables, nuevas fuentes de ingresos habilitadas por IA, adquisición/retención de clientes, acelerar ciclos de innovación |
| Aumentar la eficiencia operativa | Automatizar tareas repetitivas, optimizar la asignación de recursos, reducir costos mediante la optimización de procesos, mejorar la productividad |
| Reducir el riesgo del negocio | Mejorar el cumplimiento, mejorar la detección de fraude, fortalecer la continuidad del negocio, detección de anomalías |
| Mejorar el desempeño ESG (Ambiental, Social y de Gobernanza) | Optimizar el consumo de energía, sostenibilidad de la cadena de suministro, seguridad en el lugar de trabajo, monitoreo automatizado del cumplimiento |

**Salida:** Un mapeo de la iniciativa a las categorías de valor relevantes con una breve justificación.

---

## Etapa 3: Identificación de métricas

**Propósito:** Para cada categoría de valor mapeada, identificar métricas medibles específicas que demostrarían valor.

- Proponer métricas candidatas para cada categoría
- Definir cada métrica con precisión (fórmula, unidades, frecuencia de medición)
- Confirmar las métricas con la parte interesada

**Salida:** Una lista de métricas candidatas con definiciones, agrupadas por categoría de valor.

---

## Etapa 4: Ajuste de métricas

**Propósito:** Evaluar la factibilidad de medir cada métrica candidata y filtrar en consecuencia.

Asigna una calificación de factibilidad a cada métrica:

| Calificación | Significado | Acción |
|--------|---------|--------|
| F1 | Datos disponibles fácilmente | Conservar — proceder a la recolección de datos |
| F2 | Obtenible con esfuerzo razonable | Conservar — anotar el esfuerzo requerido |
| F3 | No es factible de medir | Descartar o encontrar una métrica proxy |

**Regla de decisión:** Si una métrica se califica como F3 sin un proxy viable, se excluye del cálculo.

**Salida:** Una lista refinada de métricas factibles, con los elementos F3 eliminados o reemplazados por proxies.

---

## Etapa 5: Recolección de datos (mejorada)

**Propósito:** Reunir entradas cuantitativas para cada métrica factible, incluidos rangos de incertidumbre.

### Datos existentes (igual que v1)

Para cada métrica, recolectar:

| Campo | Descripción | Cómo recolectar |
|-------|-------------|----------------|
| Línea base actual | Valor medido más reciente | Sistemas de operaciones/finanzas |
| Tendencia histórica | 8 trimestres de datos | Informes históricos, bases de datos |
| Impacto financiero por unidad | Valor en dólares por unidad de cambio de la métrica | Equipo de finanzas, contabilidad de costos |
| Benchmark de la industria | Desempeño de los mejores en su clase o de pares | Informes de la industria, asociaciones |

### Nuevos datos (mejora de v2)

| Campo | Descripción | Cómo recolectar |
|-------|-------------|----------------|
| **Objetivo de mejora de tres puntos** | Pesimista (P10), más probable (P50), optimista (P90) | Pregunta a las partes interesadas: *"¿Cuál es tu peor resultado realista? ¿Qué esperas más? ¿Cuál es tu mejor escenario realista?"* |
| **Tasa de adopción/realización** | Estimación de tres puntos (pesimista/probable/optimista) | Pregunta: *"¿Qué porcentaje del valor teórico se realizará realmente, dada la preparación organizacional, la gestión del cambio y los desafíos de integración?"* |
| **Proyección contrafactual de la línea base** | Dónde estaría la métrica en 12 meses SIN la iniciativa | Pregunta: *"Con base en la tendencia de 8 trimestres, ¿dónde quedaría naturalmente esta métrica en 12 meses si no hicieras nada?"* Usa la tendencia histórica para extrapolar. |

### Guía para recolectar estimaciones de tres puntos

- Formula las preguntas de forma neutral — evita anclar primero en el valor "más probable"
- Pesimista (P10): "Si las cosas van mal pero no de forma catastrófica, ¿qué esperarías?"
- Optimista (P90): "Si la ejecución va bien y las condiciones son favorables, ¿qué es realista?"
- Enfatiza "realista" — no el peor/mejor caso, sino los percentiles 10 y 90 de los resultados probables
- Para la tasa de adopción: considera la preparación organizacional, las prioridades en competencia, la complejidad de integración, la disposición de los usuarios finales a cambiar sus flujos de trabajo

**Salida:** Una tabla de recolección de datos completa con rangos para cada métrica, con las fuentes documentadas.

---

## Etapa 6: Cálculo del valor de negocio (mejorada)

**Propósito:** Calcular el valor de negocio anualizado usando simulación de Monte Carlo para producir un rango.

### Enfoque: simulación de Monte Carlo

En lugar de un único cálculo determinista, ejecuta **10,000 iteraciones**:

1. Para cada iteración, **muestrea aleatoriamente** de distribuciones triangulares para:
   - Objetivo de mejora (usando pesimista/probable/optimista de la etapa 5)
   - Impacto financiero por unidad (si es incierto — de lo contrario usa un valor puntual)
   - Tasa de adopción/realización (usando pesimista/probable/optimista de la etapa 5)

2. **Resta la mejora contrafactual** — la porción de mejora que habría ocurrido orgánicamente (de la proyección contrafactual de la línea base)

3. **Calcula el valor por iteración:**
   ```
   Value = (AI-attributed improvement - Counterfactual drift) × Financial impact per unit × Adoption rate × Annualization factor
   ```

4. Después de 10,000 iteraciones, calcula:
   - **P10** (conservador): percentil 10 — "90% de probabilidad de superar esto"
   - **P50** (mediana): percentil 50 — "igualmente probable por encima o por debajo"
   - **P90** (optimista): percentil 90 — "10% de probabilidad de superar esto"

### Análisis de sensibilidad

Después de la simulación, calcula los coeficientes de correlación de Pearson (r) entre cada variable de entrada y la salida total. Esto revela qué entradas generan la mayor varianza en el resultado.

### Palancas de influencia

Para cada entrada con r > 0.4, evalúa:

| Variable de entrada | Valor r | Controlabilidad | Cómo influir |
|---------------|---------|-----------------|-----------------|
| *Ejemplo:* Reducción de inactividad | 0.748 | Parcialmente controlable | Influida por la calidad del modelo (completitud de datos, selección de algoritmo), la cobertura de sensores (inversión de capital), los protocolos de respuesta de la cuadrilla de mantenimiento (capacitación, SOPs). Mejorar mediante: mejores tuberías de datos de entrenamiento, despliegue incremental de sensores, procedimientos de respuesta estandarizados. |
| *Ejemplo:* Tasa de adopción | 0.605 | Altamente controlable | Influida por el rigor de la gestión del cambio, la calidad de la capacitación de usuarios finales, el patrocinio del liderazgo, la integración del flujo de trabajo. Mejorar mediante: mandato ejecutivo, despliegue por fases con champions, alertas automatizadas en los sistemas existentes, sesiones regulares de retroalimentación. |
| *Ejemplo:* Impacto financiero/unidad | 0.3xx | Menos controlable | Impulsado por la mezcla de producción, los precios de mercado, los términos del contrato. Monitorear pero con poca palanca para optimizar. |

Este análisis da a la parte interesada una guía accionable: *"Si quieres estrechar la incertidumbre o aumentar el resultado mediano, enfoca el esfuerzo en estas palancas específicas."*

### Entregables de la etapa 6

- Resultados de Monte Carlo (P10/P50/P90 por métrica y total)
- Tabla de análisis de sensibilidad
- Evaluación de palancas de influencia
- Script de Python ejecutable (`montecarlo_simulation.py`)
- Archivo de entradas editable (`simulation_inputs.json`) para reejecuciones del cliente

### Consolidar los valores por métrica en un total

> BVIF consolida **sumando primero el valor de cada métrica dentro de cada iteración** y luego tomando percentiles del arreglo de 10,000 totales — preservando las correlaciones de las entradas compartidas (tasa de adopción) y el beneficio de diversificación de las entradas independientes (objetivos de mejora por métrica).

Consulta el apéndice A.5 para la explicación completa.

### Verificación de doble conteo

Igual que v1 — las métricas que miden el mismo fenómeno subyacente se marcan y solo a una se le asigna valor financiero.

**Salida:** Rango de valor de negocio (P10/P50/P90), análisis de sensibilidad, palancas de influencia y código de simulación.

---

## Etapa 7: Resultados finales (mejorada)

**Propósito:** Producir un informe consolidado con rangos, análisis de sensibilidad y guía accionable.

El informe final incluye:

### Resumen ejecutivo
- Valor de negocio anualizado total como un rango: P10 / P50 / P90
- Intervalo de confianza del 80% (P10 a P90)
- Comparación con la estimación puntual de v1 (explica por qué la mediana puede diferir)

### Desglose por métrica
- Cada métrica con su propio rango P10/P50/P90
- Explicación del impulsor de valor para cada una
- Atribución de fuente

### Análisis de sensibilidad
- Qué supuestos de entrada generan la mayor varianza
- Clasificados por coeficiente de correlación (r)

### Palancas de influencia
- Para entradas con r alto: evaluación de controlabilidad y recomendaciones de mejora
- Guía accionable para la parte interesada

### Explicación del ajuste contrafactual
- Qué habría ocurrido sin la iniciativa
- Cuánto de la "mejora" es orgánico vs. atribuido a la IA
- Transparencia sobre este ajuste

### Comparación: estimación puntual de v1 vs. rango de v2
| Versión | Salida | Diferencias clave |
|---------|--------|-----------------|
| v1 | Número único (p. ej., \$9.36M) | Determinista; asume 100% de adopción; sin contrafactual |
| v2 | Rango (p. ej., P10 \$6.2M / P50 \$7.5M / P90 \$8.9M) | Modela la incertidumbre; adopción explícita; contrafactual restado |

### Secciones adicionales (igual que v1)
- Verificación de doble conteo
- Valor de negocio no financiero (cuantificado)
- Valor estratégico más allá de los números
- Riesgo de la inacción

**Salida:** Un documento integral de resultados finales con rangos y recomendaciones accionables.

---

## Principios de diseño (igual que v1, más)

- **La incertidumbre es explícita:** Las proyecciones futuras llevan rangos, no falsa precisión
- **La adopción se modela:** Se cuantifica la brecha entre "el modelo funciona" y "el valor se realiza"
- **Honestidad contrafactual:** Solo la mejora atribuida a la IA cuenta como valor
- **Accionabilidad:** Las palancas de influencia dan a las partes interesadas una guía clara sobre en qué enfocarse
- **Reproducibilidad:** Las entradas de la simulación se almacenan en un archivo JSON; cualquiera puede reejecutar con supuestos actualizados
- **Límite de alcance preservado:** BVIF v2 sigue cuantificando solo el lado del valor — sin costos, sin ROI, sin NPV

---

## Resumen de cambios respecto a v1

| Área | v1 (actual) | v2 (mejorada) |
|------|--------------|---------------|
| Objetivo de mejora | Valor único | Tres puntos (P10/P50/P90) |
| Tasa de adopción | Implícitamente 100% | Modelada explícitamente (tres puntos) |
| Contrafactual | No considerado | Proyectado y restado |
| Método de cálculo | Fórmula determinista | Monte Carlo (10,000 iteraciones) |
| Formato de salida | Estimación puntual única | Rango P10/P50/P90 |
| Sensibilidad | Ninguna | Análisis de correlación por entrada |
| Accionabilidad | Limitada | Palancas de influencia con guía |
| Entregables | Solo informe final | Informe + script de Python + entradas JSON editables |
| Preguntas de la Etapa 5 | ~6 por métrica | ~9 por métrica (3 adicionales) |
| Impacto en tiempo | Mínimo | +15–30 minutos de preguntas a las partes interesadas por métrica |

---

> **Nota:** Esta versión está en pruebas beta. La retroalimentación de los compromisos iniciales (incluido Coppel, junio de 2026) determinará si estas mejoras se vuelven parte del proceso BVIF estándar.

---

## Apéndice A: Explicaciones conceptuales

Este apéndice proporciona explicaciones intuitivas de los conceptos estadísticos usados en las etapas 5, 6 y 7. Está destinado a partes interesadas o practicantes que quieran entender el *porqué* detrás de las matemáticas sin necesitar formación en estadística.

### A.1 Qué significa "muestrear aleatoriamente de una distribución triangular"

Una **distribución triangular** es una forma de probabilidad simple definida por tres números de las estimaciones de la etapa 5:

- **min** = pesimista (P10)
- **mode** = más probable
- **max** = optimista (P90)

Al graficarse, parece un triángulo — el pico se sitúa sobre el valor "más probable", y las pendientes caen hacia el min y el max. Los valores cercanos al pico se extraen con más frecuencia; los cercanos a los bordes, con menos frecuencia.

**"Muestrear aleatoriamente"** significa: en cada iteración, la simulación lanza un dado bajo ese triángulo y elige un número, ponderado por la forma — de modo que el "más probable" sale con más frecuencia, pero los extremos sí aparecen a veces.

#### Ejemplo concreto: reducción de inactividad

Supón que la etapa 5 recolectó:
- Pesimista: **5%** de reducción
- Más probable: **15%** de reducción
- Optimista: **25%** de reducción

La distribución triangular se ve así (pico en 15%):

```
        /\
       /  \
      /    \
     /      \
    /        \
   /          \
  5%   15%   25%
```

Ahora ejecuta 10,000 iteraciones. Algunas extracciones de muestra podrían verse así:

| Iteración | Extracción aleatoria |
|---|---|
| 1 | 14.2% |
| 2 | 17.8% |
| 3 | 11.5% |
| 4 | 22.1% |
| 5 | 8.3% |
| ... | ... |
| 10,000 | 16.0% |

La mayoría de las extracciones se agrupan cerca del 15%, menos cerca del 5% o 25% — exactamente lo que implica la forma del triángulo.

En Python (NumPy), una extracción es literalmente:
```python
np.random.triangular(left=0.05, mode=0.15, right=0.25)
```

Esa única línea es lo que la etapa 6 llama "muestrear aleatoriamente de una distribución triangular".

---

### A.2 Por qué triangular en lugar de normal (u otras distribuciones)

La elección está impulsada por **lo que puedes pedirle realísticamente a una parte interesada**, no por elegancia matemática.

#### Triangular: coincide con cómo estiman los humanos

La etapa 5 recolecta estimaciones de tres puntos: pesimista / más probable / optimista. Una distribución triangular mapea **directamente** sobre esos tres números — sin matemáticas extra, sin supuestos ocultos. El experto dice "5% / 15% / 25%" y tienes una distribución completa.

#### Normal: requiere cosas que los expertos no pueden darte

Una distribución normal necesita una **media (μ)** y una **desviación estándar (σ)**. Las partes interesadas no piensan en desviaciones estándar — pregúntale a un gerente de planta "¿cuál es la σ de tu estimación de reducción de inactividad?" y obtendrás una mirada en blanco. De todos modos tendrías que *retro-calcular* σ a partir del P10/P90, agregando una capa de falsa precisión.

También tiene propiedades que a menudo no encajan con las estimaciones de BVIF:

| Propiedad | Normal | Triangular | Por qué importa para BVIF |
|---|---|---|---|
| **Simétrica** | Sí (forzada) | No (puede ser asimétrica) | Las estimaciones reales suelen ser asimétricas — p. ej., "probable 15%, pero podría llegar plausiblemente a 25%, y solo realísticamente caer a 10%" |
| **Acotada** | No (colas infinitas) | Sí (min/max estrictos) | La tasa de adopción no puede superar el 100% ni bajar de 0% — la normal muestrearía valores imposibles |
| **Comportamiento de las colas** | Probabilidad diminuta pero no nula de valores atípicos extremos | Probabilidad cero más allá del min/max | La parte interesada dijo "el peor caso es 5%" — lo dice en serio, no "5% con 0.3% de probabilidad de -10%" |

#### El compromiso

La triangular es **tosca pero honesta**. Dice: "Tengo tres datos de una estimación humana y no fingiré que tengo más información que esa". Una distribución normal *parecería* más sofisticada pero introduciría supuestos (simetría, colas infinitas, una σ específica) que los datos subyacentes de la entrevista en realidad no respaldan.

Para BVIF, donde las entradas son juicios subjetivos de las partes interesadas en lugar de datos históricos medidos, la triangular es la elección más veraz.

#### Cuándo cambiarías a otra distribución

- **Normal/lognormal:** cuando tienes datos históricos reales (p. ej., reducciones de inactividad de 200 proyectos pasados) y puedes ajustar μ y σ a partir de mediciones reales.
- **Beta o PERT:** cuando quieres la entrada de tres puntos de la triangular pero con colas más suaves (PERT es esencialmente "triangular suavizada", aún parametrizada por min/probable/max).
- **Uniforme:** cuando genuinamente no tienes idea de dónde dentro de un rango se encuentra el valor verdadero — solo un min y un max, sin "más probable".

#### Qué usa Monte Carlo

Monte Carlo es un **método**, no una distribución — es agnóstico de la distribución. La receta es siempre la misma:

1. Para cada entrada incierta, elige *alguna* distribución de probabilidad (triangular, normal, lognormal, beta, uniforme, empírica, lo que se ajuste a tus datos).
2. Cada iteración: extrae una muestra aleatoria de la distribución de cada entrada.
3. Inserta las muestras en tu fórmula → obtén un valor de salida.
4. Repite 10,000 veces → ahora tienes una distribución de salidas de la cual leer percentiles.

BVIF resulta usar **triangular** por las razones de entrada de las partes interesadas anteriores. Si tuvieras datos históricos medidos, usarías normal o lognormal en el mismo bucle de Monte Carlo y el resto de la etapa 6 funcionaría de forma idéntica. En `numpy`, solo cambia la línea del muestreador:

```python
# Triangular (predeterminado de BVIF)
np.random.triangular(left=0.05, mode=0.15, right=0.25)

# Normal (si tuvieras media y desviación históricas)
np.random.normal(loc=0.15, scale=0.04)

# Lognormal (p. ej., para impactos de costo/ingresos que no pueden ser negativos)
np.random.lognormal(mean=np.log(0.15), sigma=0.3)
```

Mismo Monte Carlo, distinta lente sobre la incertidumbre.

---

### A.3 Qué significa el coeficiente de correlación de Pearson (r)

**r te dice qué tan fuertemente se mueven juntas dos cosas.** Es un número entre **-1 y +1**.

| Valor r | Qué significa |
|---|---|
| **+1.0** | Relación positiva perfecta — cuando X sube, Y siempre sube proporcionalmente |
| **+0.7** | Positiva fuerte — que X suba normalmente significa que Y sube |
| **+0.3** | Positiva débil — leve tendencia a moverse juntas |
| **0** | Sin relación lineal — conocer X no te dice nada sobre Y |
| **-0.3** | Negativa débil — leve tendencia a moverse en sentido opuesto |
| **-0.7** | Negativa fuerte — que X suba normalmente significa que Y baja |
| **-1.0** | Relación negativa perfecta |

#### Analogía cotidiana

- **Estatura vs. talla de zapato:** r ≈ +0.7 → las personas más altas tienden a tener pies más grandes, pero no siempre.
- **Horas de estudio vs. calificación de examen:** r ≈ +0.6 → más estudio normalmente ayuda, pero otros factores importan.
- **Temperatura exterior vs. uso de calefacción:** r ≈ -0.8 → días más calurosos, menos calefacción.
- **Talla de zapato vs. coeficiente intelectual:** r ≈ 0 → sin relación.

#### Qué significa en la etapa 6 de BVIF

Después de 10,000 iteraciones de Monte Carlo, tienes 10,000 filas como esta:

| Iteración | Reducción de inactividad (entrada) | Tasa de adopción (entrada) | Financiero/unidad (entrada) | **Valor total (salida)** |
|---|---|---|---|---|
| 1 | 14.2% | 72% | \$48K | \$3.1M |
| 2 | 17.8% | 65% | \$52K | \$3.8M |
| 3 | 11.5% | 80% | \$45K | \$2.9M |
| ... | ... | ... | ... | ... |

Luego se calcula r entre **cada columna de entrada** y la **columna de salida**:

| Entrada | r | Interpretación |
|---|---|---|
| Reducción de inactividad | **0.748** | Impulsor fuerte — cuando esta entrada es alta en una iteración, el valor total suele ser alto también |
| Tasa de adopción | **0.605** | Impulsor fuerte — impacto significativo en la salida |
| Financiero/unidad | **0.32** | Moderado — importa pero menos |
| Costo de sensores | **0.05** | Insignificante — apenas afecta el resultado |

#### Por qué esto importa: muestra dónde enfocarse

El umbral en la etapa 6 es **r > 0.4** = "esta entrada impulsa materialmente el resultado".

- **r alto + controlable** (p. ej., tasa de adopción, r=0.605) → **invierte esfuerzo aquí**: mejor capacitación, gestión del cambio y patrocinio ejecutivo moverán la aguja.
- **r alto + no controlable** (p. ej., precios de mercado, r=0.7) → **monitorea, pero no desperdicies esfuerzo** intentando optimizar.
- **r bajo** (p. ej., costo de sensores, r=0.05) → ignóralo para la optimización; no es lo que impulsa la varianza en el resultado.

#### La intuición en una frase

> r responde: *"Si pudiera estrechar mi estimación de esta única entrada, ¿cuánto se estrecharía mi estimación de valor de negocio total?"*

Un r alto significa que esa entrada está haciendo el trabajo pesado en tu incertidumbre — así que reducir su incertidumbre (o mejorar su valor real) te da el mayor beneficio.

#### Advertencia importante

**Correlación no es causalidad.** r=0.7 entre dos cosas no prueba que una cause la otra — ambas podrían depender de un tercer factor. Pero en Monte Carlo específicamente, dado que *tú* definiste la fórmula que vincula las entradas con la salida, un r alto sí significa genuinamente "esta entrada impulsa matemáticamente la salida" — esa interpretación es segura aquí.

---

### A.4 Por qué r cambia entre BVIFs aunque la fórmula sea la misma

La **fórmula** es la misma entre BVIFs, pero **r no depende solo de la fórmula**. Depende de **qué tan amplio es el rango de cada entrada** comparado con los demás.

#### La idea clave

> **r mide cuál *incertidumbre* de entrada está impulsando la incertidumbre de la salida.**

Incluso con una fórmula idéntica, si un proyecto tiene un rango amplio en la tasa de adopción y un rango estrecho en el impacto financiero, la adopción dominará r. En otro proyecto donde los rangos están invertidos, el impacto financiero dominará.

#### Ejemplo concreto con la misma fórmula

Fórmula (fija para ambos proyectos):
```
Value = Improvement × Financial_per_unit × Adoption × Annualization
```

##### Proyecto A: mantenimiento predictivo en una refinería

| Entrada | Rango (P10 / probable / P90) | ¿Qué tan amplio? |
|---|---|---|
| Reducción de inactividad | 5% / 15% / 25% | **Amplio** (dispersión de 5x) |
| Financiero/unidad | \$48K / \$50K / \$52K | Estrecho (costo bien conocido) |
| Tasa de adopción | 60% / 70% / 80% | Estrecho (despliegues pasados similares) |

Ejecuta Monte Carlo → resultado probable:

| Entrada | r |
|---|---|
| Reducción de inactividad | **0.85** ← domina |
| Financiero/unidad | 0.15 |
| Tasa de adopción | 0.30 |

**Por qué:** la reducción de inactividad es la única entrada con gran incertidumbre, así que impulsa casi toda la variación en la salida.

##### Proyecto B: misma fórmula, distinto proyecto (p. ej., despliegue de asistente de IA)

| Entrada | Rango (P10 / probable / P90) | ¿Qué tan amplio? |
|---|---|---|
| Ganancia de productividad | 12% / 15% / 18% | Estrecho (medido en piloto) |
| Financiero/unidad | \$30K / \$50K / \$80K | Amplio (varía por rol) |
| Tasa de adopción | 20% / 50% / 80% | **Muy amplio** (gestión del cambio incierta) |

Ejecuta Monte Carlo → resultado probable:

| Entrada | r |
|---|---|
| Ganancia de productividad | 0.20 |
| Financiero/unidad | 0.45 |
| Tasa de adopción | **0.80** ← domina |

**Misma fórmula. Valores de r completamente diferentes.**

#### La intuición

Piensa en la fórmula como una **máquina** con perillas. La fórmula no cambia. Pero:

- Si solo se gira con fuerza **una perilla** y las demás apenas se mueven → esa perilla tiene r ≈ 1.
- Si **todas las perillas** se giran con igual fuerza → r se reparte entre ellas.

r esencialmente pregunta: *"De todo el ruido que entra a esta máquina, ¿qué entrada contribuyó más?"* Esa respuesta cambia cada vez, porque los niveles de ruido (los rangos de entrada) cambian con cada BVIF.

#### Aún más sutil: el mismo proyecto, solo **estrechar una estimación** invierte r

Imagina que en el Proyecto A anterior, el equipo hace más entrevistas y estrecha la estimación de reducción de inactividad a **13% / 15% / 17%** (mucho más estrecha). Reejecuta Monte Carlo y verías:

| Entrada | r antes | r después de estrechar |
|---|---|---|
| Reducción de inactividad | 0.85 | **0.30** ← ahora importa menos |
| Tasa de adopción | 0.30 | **0.65** ← ahora el mayor impulsor |

La fórmula no cambió. El proyecto no cambió. **Solo recolectar mejores datos sobre una entrada desplazó cuál entrada es ahora "la palanca en la que enfocarse".**

Esto es exactamente por qué el paso de palancas de influencia se rehace después del análisis de sensibilidad — y por qué es útil *reejecutar* la simulación a medida que las estimaciones mejoran con el tiempo.

#### Resumen en una línea

> La fórmula le dice a Monte Carlo *cómo* se combinan las entradas. r te dice *cuál incertidumbre de entrada* está dominando actualmente la incertidumbre de la salida — y eso depende de los **rangos** que te dio la parte interesada, que difieren para cada proyecto.

---

### A.5 Cómo BVIF consolida los valores por métrica en el valor de negocio total

#### La idea clave: NO suma los P50

Un enfoque ingenuo sería:
```
Total P50 = M1.P50 + M3.P50 + M6.P50    ❌ INCORRECTO
```

Eso **sobreestimaría la incertidumbre** en las colas (P10 y P90) porque asume que el peor caso de cada métrica ocurre simultáneamente. En realidad, cuando vuelves a tirar las entradas aleatoriamente, algunas métricas quedan altas mientras otras quedan bajas — se cancelan parcialmente.

#### Lo que en realidad hace: sumar por iteración, luego tomar percentiles

En el script de simulación:

```python
total_annual_value = m1_annual_value + m3_annual_value + m6_annual_value
```

Cada uno de esos es un **arreglo de 10,000 valores**, no un solo número. La suma es elemento por elemento:

| Iteración | Valor M1 | Valor M3 | Valor M6 | **Total (suma)** |
|---|---|---|---|---|
| 1 | \$3.2M | \$1.8M | \$0.9M | **\$5.9M** |
| 2 | \$4.1M | \$2.2M | \$1.1M | **\$7.4M** |
| 3 | \$2.8M | \$1.5M | \$0.7M | **\$5.0M** |
| ... | ... | ... | ... | ... |
| 10,000 | \$3.7M | \$2.0M | \$1.0M | **\$6.7M** |

Ahora tienes **10,000 números de valor total**. Luego los percentiles se calculan **sobre el arreglo de totales**:

```python
p10_total, p50_total, p90_total = percentiles(total_annual_value)
```

Así que el P10/P50/P90 consolidado proviene de la *distribución de totales sumados*, no de sumar percentiles.

#### Por qué esta es la forma correcta (ejemplo concreto)

Supón que la simulación produce:

| Métrica | P10 | P50 | P90 |
|---|---|---|---|
| M1 (inactividad) | \$2.5M | \$3.5M | \$4.6M |
| M3 (costo de mant.) | \$1.2M | \$1.9M | \$2.6M |
| M6 (entrega) | \$0.5M | \$0.9M | \$1.4M |

| Enfoque | Total P10 | Total P50 | Total P90 |
|---|---|---|---|
| ❌ Ingenuo (sumar percentiles) | \$4.2M | \$6.3M | \$8.6M |
| ✅ BVIF (suma por iteración) | ~\$5.0M | \$6.3M | ~\$7.8M |

Las medianas coinciden (P50 de una suma ≈ suma de P50), pero el **rango se estrecha** con el método correcto. Eso se debe a que:

- **La tasa de adopción es compartida** entre las tres métricas (se muestrea una vez, se usa en todas). Cuando la adopción es alta en la iteración N, es alta para *todas* las métricas; cuando es baja, baja para todas. Esto crea una **correlación positiva** que la suma por iteración captura.
- **Los objetivos de mejora son independientes** entre métricas (M1, M3, M6 obtienen cada uno sus propias extracciones). Un M1 alto no implica un M3 alto — así que se cancelan parcialmente, **estrechando el rango total**.

#### Diagrama de resumen

```
La simulación de la Etapa 6 produce 4 arreglos de 10,000 valores cada uno:
  m1_annual_value  → [v1, v2, ..., v10000]
  m3_annual_value  → [v1, v2, ..., v10000]
  m6_annual_value  → [v1, v2, ..., v10000]

Paso 1: Suma elemento por elemento entre métricas
  total_annual_value[i] = m1[i] + m3[i] + m6[i]    para i = 1..10,000

Paso 2: Toma percentiles del arreglo de totales
  P10_total = percentil 10 de total_annual_value
  P50_total = percentil 50 de total_annual_value
  P90_total = percentil 90 de total_annual_value
```

#### Resumen en una línea

> BVIF consolida **sumando primero el valor de cada métrica dentro de cada iteración** y luego tomando percentiles del arreglo de 10,000 totales — preservando las correlaciones de las entradas compartidas (tasa de adopción) y el beneficio de diversificación de las entradas independientes (objetivos de mejora por métrica).
