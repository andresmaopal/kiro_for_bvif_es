# Resumen del proceso AI-BVIF

**Propósito**: Referencia técnica para que el modelo de IA entienda la estructura completa del flujo de trabajo de AI-BVIF.

## El ciclo de vida de tres fases:
- **FASE DE DESCUBRIMIENTO**: Entender la iniciativa y mapearla a categorías de valor de negocio
- **FASE DE MÉTRICAS**: Identificar, evaluar factibilidad y refinar métricas
- **FASE DE CUANTIFICACIÓN**: Recolectar datos, calcular el valor de negocio, producir el informe final

## El flujo de trabajo secuencial:
Configuración de la sesión → Etapa 1 (Definición de la iniciativa) → Etapa 2 (Mapeo de valor de negocio) → Etapa 3 (Identificación y factibilidad de métricas) → Etapa 4 (Ajuste de métricas) → Etapa 5 (Recolección de datos) → Etapa 6 (Cálculo del valor de negocio) → Etapa 7 (Resultados finales)

## Categorías de valor de negocio (CAF v3):

| Categoría | Descripción |
|---|---|
| Aumentar los ingresos | Aumentos en el consumo del cliente, expansión de los mercados direccionables (crecimiento de la línea superior) |
| Aumentar la eficiencia operativa | Reducción de gastos existentes (ahorro de costos) o prevención de costos futuros (evitación de costos) |
| Reducir el riesgo del negocio | Inversiones en cumplimiento regulatorio, seguridad, etc. Normalmente sin beneficio financiero directo |
| Mejorar el ESG | Objetivos Ambientales, Sociales o de Gobernanza. Sin beneficio financiero directo, pero con valor estratégico |

## Etiquetas de factibilidad:

| Etiqueta | Definición |
|---|---|
| Factibilidad 1 | La métrica ya se rastrea. Lista para usar. |
| Factibilidad 2 | Los datos existen, pero la métrica aún no se calcula. Factible con algo de configuración. |
| Factibilidad 3 | No existen datos. Requiere nueva infraestructura. |

## Decisiones de métricas de la Etapa 4:

| Decisión | Cuándo aplicar |
|---|---|
| Conservar tal cual | Métricas de Factibilidad 1 — no se necesitan cambios |
| Activar | Métricas de Factibilidad 2 — establecer mecanismo de extracción |
| Reemplazar con proxy | Métricas de Factibilidad 3 — encontrar un proxy usando datos disponibles |
| Diferir | Métrica solo disponible post-despliegue — marcar para más tarde |
| Eliminar | No representativa, redundante o sin proxy viable |

## Tipos de beneficio de la Etapa 6:

| Tipo | Descripción |
|---|---|
| Financiero | Beneficios expresados como valor monetario anualizado |
| No financiero | Mejoras cuantificables no directamente traducibles a dinero |

## Niveles de Fidelidad de la Fuente de la Etapa 5:

> **Fuente única de verdad**. Estas definiciones aplican siempre que el agente extrae datos de documentos proporcionados por humanos en la ruta de carga de la Etapa 5. Tanto las reglas de extracción del agente como el archivo de respuestas extraídas orientado al humano referencian esta sección — actualiza las definiciones aquí y en ningún otro lugar para evitar la deriva.

**Por qué "Fidelidad de la Fuente" y no "Confianza"**: "Fidelidad de la Fuente" se acota estrechamente a qué tan fielmente el valor extraído reproduce lo que dice el documento fuente. **No** es una predicción sobre si la iniciativa logrará el valor de negocio calculado — ese es un concepto distinto (ver "Reservas de terminología" más abajo). Mantener los nombres distintos evita que los revisores confundan "extraje fielmente este número del documento fuente" con "creo que alcanzaremos este número".

| Nivel | Definición | Ejemplo |
|---|---|---|
| **Alta** | El valor aparece textualmente en la fuente, en un contexto inequívoco. No se necesitó interpretación, conversión de unidades, agregación ni inferencia. | El documento contiene "Tasa de abandono Q2 2025: 4.2%" y la métrica que se extrae es la tasa de abandono del Q2 2025. |
| **Media** | El valor está claramente respaldado por la fuente pero requirió una interpretación ligera: agregación simple (p. ej., sumar valores mensuales para producir un trimestre), conversión de unidades, mapeo de sinónimos (el documento dice "tasa de deserción", la métrica es "tasa de abandono"), o seleccionar el más reciente de varios valores listados. Un revisor podría reproducir la derivación en unos segundos. | El documento lista el abandono mensual de abr/may/jun 2025 — la cifra del Q2 2025 se promedió. |
| **Baja** | El valor se infirió, estimó o ensambló a partir de múltiples lugares. Proyecciones para periodos faltantes, benchmarks derivados de oraciones narrativas ("los pares rondan el 5%"), o resolución de números conflictivos. Un revisor necesita verificar el razonamiento, no solo la fuente. | El Q1 2024 faltaba — se proyectó a partir de Q2–Q4 2024 y el cierre de año 2023. |

**Regla general**: si la extracción tomó más de un paso de razonamiento, no es Alta. En caso de duda entre dos niveles, elige el más bajo.

**Enmarcado orientado al humano**: Los valores de baja fidelidad merecen la mirada más cercana — son los que más probablemente necesiten corrección durante la validación.

## Reservas de terminología:

El marco evita deliberadamente la palabra escueta "**confianza**" para evitar que dos ideas conceptualmente diferentes choquen:

| Término | Alcance | Definido en | Estado |
|---|---|---|---|
| **Fidelidad de la Fuente** | Qué tan fielmente un valor extraído de la Etapa 5 reproduce lo que dice el documento fuente. Se aplica por dato durante la ruta de carga de documentos. | "Niveles de Fidelidad de la Fuente de la Etapa 5" arriba | Definido y en uso |
| **Confianza en la Realización del Valor** | Qué tan probable es que el valor de negocio calculado en la Etapa 6 se logre realmente. Aplicaría por métrica o para la iniciativa en su conjunto. | Aún no definido | **Reservado** — no uses "Confianza" para nada en la Etapa 5 |

**Reglas para futuros autores**:
- NO uses la palabra escueta "Confianza" para describir la calidad de extracción de la Etapa 5. Usa "Fidelidad de la Fuente" o "Fidelidad" en su lugar.
- Si un cambio futuro introduce un concepto de probabilidad de realización en la Etapa 6 o la Etapa 7, nómbralo **Confianza en la Realización del Valor** (no solo "Confianza") y defínelo en este archivo junto a la Fidelidad de la Fuente — nunca reutilices los niveles de la Etapa 5 para ello, ya que las dos miden cosas diferentes en escalas diferentes.

## Reglas críticas:
- **Sin doble conteo**: Múltiples métricas pueden capturar el mismo impacto subyacente — siempre verifica la superposición
- **Comparabilidad de categorías**: "Eficiencia operativa" = ahorros de línea inferior; "Aumentar los ingresos" = valor de línea superior que requiere un ajuste de margen de contribución antes de comparar
- **Condición de PARADA**: Si una métrica crítica de Factibilidad 3 no tiene proxy viable, detén el proceso hasta resolverlo
- **AI-BVIF cuantifica solo el lado del valor** — el costo de implementación, el costo operativo, el riesgo y el momento deben evaluarse por separado antes de que esto se convierta en un caso de negocio completo. AI-BVIF alinea las iniciativas de IA con el valor de negocio para una toma de decisiones informada, pero no es la decisión completa.

## Convención de nombres de artefactos:
Todos los archivos de salida usan un prefijo de secuencia que coincide con el número de etapa:
- `00-` para la configuración de la sesión
- `01-` para la Etapa 1
- `02-` para la Etapa 2
- ... hasta `07-` para la Etapa 7

## Convención de rutas: carpeta por iniciativa

Cada iniciativa de IA vive en su propia carpeta bajo `bvif-docs/`, nombrada:

```
bvif-docs/<NN>-<initiative-slug>-<yyyymm>/
```

donde `<NN>` es un número consecutivo con relleno de ceros que empieza en `01` y `<yyyymm>` es el año y mes en que se inició la iniciativa.

En este y en todos los demás archivos de detalle de reglas, el marcador `<INITIATIVE_FOLDER>` se refiere a esa carpeta específica de la iniciativa (por ejemplo `bvif-docs/01-customer-churn-predictor-202604`). Todos los artefactos — `bvif-state.md`, `audit.md` y cada subcarpeta de etapa de `00-` a `07-` — DEBEN vivir dentro de `<INITIATIVE_FOLDER>`, nunca en la raíz de `bvif-docs/`.

Consulta `core-workflow.md` → "Creación de la carpeta de la iniciativa (OBLIGATORIO)" para saber cómo se genera el nombre de la carpeta y se confirma con el usuario.
