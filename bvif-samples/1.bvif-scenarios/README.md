# BVIF — Escenarios resueltos

Cada subcarpeta bajo `bvif-scenarios/` es un ejemplo completo, de principio a fin, de una ejecución BVIF: un cliente ficticio, un documento de guion y un conjunto completo de artefactos de una sesión terminada. Usa cualquiera de ellos para familiarizarte con el marco antes de ejecutar uno propio. Pueden agregarse escenarios adicionales en el futuro.

| Carpeta | Cliente (ficticio) | Iniciativa de IA | Artefactos de la ejecución de referencia |
|---|---|---|---|
| `scenario_A-Manufacturing-company/` | Precision Furniture Inc. — fabricante de muebles de EE. UU. con tres plantas automatizadas | Mantenimiento predictivo usando IA | `bvif-samples/2.bvif-docs/01-predictive-maintenance-ai-202604/` |
| `scenario_B-Sport-club/` | Clube Esportivo Bandeirantes — club de fútbol brasileño de Série A con 75 mil socios | Predicción de abandono de membresías | `bvif-samples/2.bvif-docs/02-membership-churn-prediction-202605/` |

Si llegaste a esta carpeta desde el README principal del repo, el Apéndice C de ese documento tiene el ejercicio de aprendizaje recomendado. Este archivo es una orientación ligera para quien llegue aquí directamente.

## Cómo se comparan los escenarios

Ambos escenarios producen una ejecución BVIF completa. Difieren en forma, complejidad y en lo que te permiten practicar:

| Dimensión | Escenario A — Precision Furniture | Escenario B — Bandeirantes |
|---|---|---|
| **Industria y geografía** | Industrial / manufactura, con sede en EE. UU. | Deportes y entretenimiento, Brasil |
| **Número de iniciativas** | Una sola iniciativa de IA (Mantenimiento predictivo) | Tres iniciativas de IA sobre la mesa (Precios dinámicos de entradas, Predicción de abandono de membresías, Personalización en el estadio) — elige una, o ejecuta varias y compáralas para simular un ejercicio de priorización |
| **Complejidad de la iniciativa** | Mayor — más métricas que interactúan y decisiones de factibilidad más matizadas | Menor — menos métricas por iniciativa y conceptos más directos |
| **Principal impulsor de valor** | Evitación de costos (inactividad, desperdicio, sobrecarga de mantenimiento) | Aumento de ingresos (renovaciones, boletería, gasto en día de partido) |
| **Narrativa de disponibilidad de datos** | Telemetría operativa a nivel de planta — OEE, MTBF, tasa de desperdicio, historial de órdenes de trabajo | Plataforma unificada de fans (BOLALAKE) que consolida boletería, membresía de socios, A&B, app del club, Wi-Fi del estadio, e-commerce, redes sociales — una configuración típica de customer-360 |
| **Formatos de guion provistos** | `.pdf`, `.docx`, `.md`, `.txt` | Solo `.md` — afecta lo que puedes colocar en `uploads/` de la Etapa 5 |
| **Objetivo de aprendizaje que mejor encaja** | "¿Cómo maneja BVIF una sola iniciativa, técnicamente rica, de principio a fin?" | "¿Cómo ayuda BVIF a un equipo de liderazgo a comparar y priorizar múltiples iniciativas de IA?" |

## Qué hay en cada carpeta de escenario

```
scenario_<X>-<short-name>/
└── Scenario <X> - <name> - Storyline.<pdf|docx|md|txt>   # El guion (uno o más formatos)
```

La ejecución de referencia de cada escenario — cada archivo de preguntas, cada archivo de aprobación, el archivo de respuestas extraídas de la Etapa 5, el cálculo del valor de negocio con la aritmética y la tabla final consolidada de métricas — vive en la carpeta correspondiente `bvif-samples/2.bvif-docs/<NN>-<slug>-<yyyymm>/` listada en la tabla anterior.

Algunas cosas que saber sobre los archivos de guion:

- Cuando un escenario provee múltiples formatos (`.pdf`, `.docx`, `.md`, `.txt`), son idénticos en contenido — elige el que sea más fácil de leer o de alimentar a un asistente de IA. El Escenario A se entrega en los cuatro formatos; el Escenario B actualmente se entrega solo en `.md`.
- Para la ruta de carga de la Etapa 5, usa `.md` o `.txt` (BVIF te pide explícitamente mantener binarios como `.pdf` y `.docx` fuera de `uploads/`).
- La versión `.md` se renderiza bien en la vista previa integrada de Kiro y es la más legible cuando quieres revisar el guion dentro del IDE.

La carpeta `bvif-samples/0.workshop/` contiene una presentación HTML autocontenida (`index.html`) que introduce BVIF a través de uno de estos escenarios. Si quieres una experiencia guiada paso a paso — o si estás ejecutando un taller BVIF para un equipo — ábrela en cualquier navegador. Recorre los personajes, muestra el valor de negocio calculado, explica el proceso de 7 etapas y proporciona instrucciones prácticas para una sesión práctica, incluido el trabajo previo, consejos para ejecutar la sesión en Kiro y una agenda sugerida. Las notas del presentador están integradas en cada diapositiva (presiona `N` para alternarlas). Consulta `bvif-samples/0.workshop/README.md` para los atajos de teclado y el esquema completo de diapositivas.

## Dos cosas que saber antes de usar una muestra

### 1. No ejecutes tu sesión BVIF dentro de esta carpeta

Tu propia sesión debe ejecutarse desde la raíz del espacio de trabajo — la carpeta que contiene `.kiro/` y `bvif-samples/` como hermanos — no desde dentro de `bvif-samples/`. Las secciones [Preparación](../../README.md#preparación) y [Ejecutar una sesión BVIF](../../README.md#ejecutar-una-sesión-bvif) del README principal del repo explican cómo abrir la carpeta correcta en Kiro.

Esto importa porque BVIF escribe cada artefacto en una carpeta `bvif-docs/` en la **raíz del espacio de trabajo**. Cuando abres la carpeta raíz (la que tiene `.kiro/` dentro), Kiro escribirá los artefactos de tu sesión en una nueva carpeta `bvif-docs/` que queda junto a `bvif-samples/` — nunca dentro de ella. De esa forma los artefactos de referencia en `bvif-samples/2.bvif-docs/` permanecen intactos y puedes comparar (diff) tu ejecución con ellos limpiamente. Si por accidente inicias una sesión desde dentro de `bvif-samples/`, Kiro la trataría como la raíz del espacio de trabajo y escribiría en `bvif-samples/2.bvif-docs/`, mezclando tus artefactos con los de referencia. Evita eso.

### 2. Espera divergencia, no identidad

Tu ejecución **no** producirá los mismos artefactos que ninguna ejecución de referencia — y eso es lo esperado. BVIF tiene decisiones de criterio en cada etapa, por lo que distintas salidas legítimas son posibles desde el mismo punto de partida. La divergencia puede provenir de:

- **Las distintas respuestas que des** a los archivos de preguntas — por ejemplo, elegir una categoría primaria de valor de negocio distinta en la Etapa 2, o seleccionar un conjunto distinto de métricas en la Etapa 3.
- **El distinto direccionamiento humano** durante la sesión — las preguntas aclaratorias que haces, los seguimientos que cuestionas, qué etiquetas de factibilidad aceptas o desafías, y cómo formulas los objetivos de mejora en la Etapa 5.
- **La naturaleza no determinista de la IA generativa** — incluso con las mismas entradas y los mismos prompts, el agente puede redactar las cosas de forma distinta, sugerir métricas proxy ligeramente diferentes, o redactar el informe final de forma distinta de una ejecución a otra.

El objetivo es ver **cómo encajan las piezas** — definición → categorías → métricas → factibilidad → ajuste → datos → cálculo → documento final consolidado — no reproducir los mismos números.

## Enlaces rápidos a las ejecuciones de referencia

Cuando quieras calibrar tu propia ejecución en progreso frente a una salida razonablemente "buena", estos son los archivos más útiles para echar un vistazo. Las rutas son relativas a `bvif-samples/`. Elige la ejecución de referencia que coincida con el escenario en el que estás trabajando.

| Artefacto de etapa | Escenario A — Mantenimiento predictivo | Escenario B — Abandono de membresías |
|---|---|---|
| Definición de la iniciativa | `2.bvif-docs/01-predictive-maintenance-ai-202604/01-initiative-definition/initiative-definition.md` | `2.bvif-docs/02-membership-churn-prediction-202605/01-initiative-definition/initiative-definition.md` |
| Mapeo de valor de negocio | `2.bvif-docs/01-predictive-maintenance-ai-202604/02-business-value-mapping/business-value-mapping.md` | `2.bvif-docs/02-membership-churn-prediction-202605/02-business-value-mapping/business-value-mapping.md` |
| Lista final de métricas (post-ajuste) | `2.bvif-docs/01-predictive-maintenance-ai-202604/04-metrics-adjustment/final-metrics-list.md` | `2.bvif-docs/02-membership-churn-prediction-202605/04-metrics-adjustment/final-metrics-list.md` |
| Cálculo del valor de negocio de la Etapa 6 con aritmética | `2.bvif-docs/01-predictive-maintenance-ai-202604/06-business-value-calculation/business-value-calculation.md` | `2.bvif-docs/02-membership-churn-prediction-202605/06-business-value-calculation/business-value-calculation.md` |
| Entregable ejecutivo final | `2.bvif-docs/01-predictive-maintenance-ai-202604/07-final-results/final-results.md` | `2.bvif-docs/02-membership-churn-prediction-202605/07-final-results/final-results.md` |
| Registro de auditoría completo | `2.bvif-docs/01-predictive-maintenance-ai-202604/audit.md` | `2.bvif-docs/02-membership-churn-prediction-202605/audit.md` |
