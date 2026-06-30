
**AI Business Value Identification Framework — Mapeo metodológico formal**

---

## Resumen ejecutivo

BVIF no es una invención novedosa desde cero — sintetiza prácticas establecidas de valoración de proyectos, gestión de beneficios, gobierno de TI y análisis cuantitativo de riesgos en un proceso construido a medida para la estimación del valor de iniciativas de IA. Este documento mapea cada elemento de BVIF a sus ancestros metodológicos formales, analizados por separado para v1 (determinista) y v2 (con cuantificación de incertidumbre).

**Posicionamiento clave:** BVIF es un marco **centrado únicamente en el valor**. Excluye deliberadamente los costos, el ROI y el VPN (NPV). Esto lo coloca más cerca de la **Gestión de Realización de Beneficios (BRM)** y del **Total Economic Impact de Forrester (pilar de beneficios)** en su postura filosófica, tomando a la vez mecánicas del DCF (anualización), del Balanced Scorecard (categorización del valor) y — en v2 — de PERT/Monte Carlo (cuantificación de incertidumbre).

---

## Parte A: BVIF v1 (determinista) — Linaje metodológico

### A.1 Ascendencia etapa por etapa

| Etapa de BVIF v1 | Metodología más cercana | Elemento específico tomado |
|---|---|---|
| Etapa 1: Definición de la iniciativa | Gestión de Realización de Beneficios (BRM) | Identificación y alcance de beneficios |
| Etapa 2: Mapeo de valor de negocio | Balanced Scorecard (BSC) / AWS CAF | Categorización del valor desde múltiples perspectivas |
| Etapa 3: Identificación de métricas | Balanced Scorecard / marcos de KPI | Selección de indicadores adelantados/rezagados (lead/lag) |
| Etapa 4: Ajuste de métricas (F1/F2/F3) | Information Economics (Parker & Benson) | Evaluación de medibilidad / compuertas de calidad de datos |
| Etapa 5: Recolección de datos | Metodología DCF / Benchmarking | Establecimiento de línea base, economía unitaria |
| Etapa 6: Cálculo del valor de negocio | Economic Value Added (EVA) / TEI | Valor = Δ Desempeño × Economía unitaria × Tiempo |
| Etapa 7: Resultados finales | BRM / Val IT | Caso de beneficios estructurado para decisiones de inversión |

---

### A.2 Comparaciones metodológicas detalladas (v1)

#### 1. Economic Value Added (EVA) — Stern Stewart & Co.

**Qué es:** EVA mide la utilidad económica que genera una empresa por encima de su costo de capital. Fórmula: EVA = NOPAT − (Capital × WACC). Desarrollado por Stern Stewart en los años 90.

**Similitudes con BVIF v1:**
- Ambos producen un único número financiero anualizado
- Ambos usan un concepto de "brecha" (EVA: retorno en exceso sobre el costo de capital; BVIF: brecha entre el desempeño base y el objetivo)
- Ambos traducen métricas operativas a términos monetarios mediante un multiplicador de economía unitaria
- Ambos son medidas periódicas (anuales)

**Diferencias con BVIF v1:**
- EVA es una medida de desempeño **realizado** (mira hacia atrás); BVIF es una estimación **proyectada** (mira hacia adelante)
- EVA incluye el lado del costo (cargo de capital); BVIF excluye deliberadamente los costos
- EVA aplica a nivel de empresa/división; BVIF aplica a nivel de iniciativa
- EVA requiere asignación de capital; BVIF no requiere datos de costos

**Qué toma BVIF:** La estructura conceptual de "valor = mejora por encima de un punto de referencia × factor de conversión financiera". El "spread" de EVA (retorno menos costo de capital) es paralelo a la "brecha de línea base" de BVIF (objetivo menos actual).

**Referencias:** Stewart, G.B. III (1991). *The Quest for Value*. HarperBusiness. Stern, J.M., Shiely, J.S., & Ross, I. (2001). *The EVA Challenge*. Wiley.

---

#### 2. Discounted Cash Flow (DCF) / Net Present Value (NPV)

**Qué es:** El DCF estima el valor presente de flujos de caja futuros descontándolos a una tasa que refleja el valor temporal del dinero y el riesgo. NPV = Σ(CFₜ / (1+r)ᵗ) − Inversión inicial.

**Similitudes con BVIF v1:**
- Ambos anualizan los beneficios sobre un horizonte temporal
- Ambos requieren estimar impactos financieros futuros a partir de cambios operativos
- El "factor de anualización" de BVIF (×4 para trimestral, ×12 para mensual) es una versión simplificada de la proyección de series temporales del DCF

**Diferencias con BVIF v1:**
- El DCF descuenta los flujos de caja futuros por el valor temporal; BVIF no descuenta (asume estado estable)
- El DCF incluye explícitamente costos e inversión; BVIF los excluye
- El DCF produce un valor presente ajustado por riesgo; BVIF produce una estimación anual sin descontar
- El DCF requiere una tasa de descuento (WACC o tasa de corte); BVIF no requiere ninguna

**Qué toma BVIF:** La mecánica de convertir ganancias operativas periódicas en una cifra financiera a lo largo del tiempo. La fórmula de BVIF es esencialmente un DCF de un solo periodo, con tasa de descuento cero, aplicado únicamente al flujo de beneficios.

**Referencias:** Brealey, R., Myers, S., & Allen, F. (2020). *Principles of Corporate Finance* (13ª ed.). McGraw-Hill. Damodaran, A. (2012). *Investment Valuation* (3ª ed.). Wiley.

---

#### 3. Benefits Realization Management (BRM) — PMI / APMG

**Qué es:** BRM es un enfoque estructurado para identificar, planificar, medir y dar seguimiento a los beneficios de proyectos y programas. El *Benefits Realization Management Framework* de PMI (2019) define un ciclo de vida: Identificar → Ejecutar y Medir → Sostener.

**Similitudes con BVIF v1:**
- **El marco filosóficamente más alineado.** Ambos se centran exclusivamente en el lado del valor/beneficios
- Ambos usan participación de las partes interesadas y compuertas de aprobación a lo largo del proceso
- Ambos requieren la identificación explícita de beneficios antes de la cuantificación
- Ambos enfatizan la medibilidad (el F1/F2/F3 de BVIF ≈ la "evaluación de medibilidad de beneficios" de BRM)
- Ambos producen un "registro de beneficios" o artefacto equivalente

**Diferencias con BVIF v1:**
- BRM cubre el ciclo de vida completo, incluido el seguimiento de la realización post-implementación; BVIF es solo estimación pre-implementación
- BRM es agnóstico de metodología en la cuantificación (no prescribe una fórmula); BVIF proporciona una fórmula de cálculo específica
- BRM aborda la gestión del cambio y la preparación organizacional; BVIF (v1) no

**Qué toma BVIF:** La filosofía general — identificación, validación y cuantificación estructuradas de beneficios con aprobación de las partes interesadas en cada etapa. El proceso de 7 etapas de BVIF ES un flujo de trabajo de identificación y estimación de beneficios.

**Referencias:** PMI (2019). *Benefits Realization Management: A Practice Guide*. Project Management Institute. Bradley, G. (2010). *Benefit Realisation Management* (2ª ed.). Gower.

---

#### 4. Balanced Scorecard (BSC) — Kaplan & Norton

**Qué es:** El BSC organiza el desempeño organizacional en cuatro perspectivas: Financiera, Cliente, Procesos Internos y Aprendizaje y Crecimiento. Vincula objetivos estratégicos entre perspectivas mediante mapas estratégicos.

**Similitudes con BVIF v1:**
- Las cuatro categorías de valor de BVIF (Ingresos, Eficiencia, Riesgo, ESG) son paralelas a las cuatro perspectivas del BSC
- Ambos usan una taxonomía estructurada para asegurar que el valor no se mida en una sola dimensión
- Ambos conectan métricas operativas con resultados estratégicos/financieros
- Ambos requieren seleccionar KPIs específicos por categoría

**Diferencias con BVIF v1:**
- El BSC es un sistema de gestión estratégica (continuo); BVIF es un proceso de estimación de una sola vez
- El BSC no prescribe cálculos de valor monetario; BVIF sí
- El BSC cubre toda la empresa; BVIF se acota a iniciativas individuales
- Las perspectivas del BSC son más generales; las categorías de BVIF son específicas de IA/digital (alineadas con AWS CAF)

**Qué toma BVIF:** El mapeo de valor multicategoría (Etapa 2). La insistencia de BVIF en mapear las iniciativas a múltiples categorías de valor asegura una visión holística, en paralelo directo con el enfoque multiperspectiva del BSC.

**Referencias:** Kaplan, R.S. & Norton, D.P. (1996). *The Balanced Scorecard*. Harvard Business School Press. Kaplan, R.S. & Norton, D.P. (2004). *Strategy Maps*. Harvard Business School Press.

---

#### 5. Forrester Total Economic Impact™ (TEI)

**Qué es:** TEI es el marco propietario de Forrester para evaluar inversiones tecnológicas en cuatro dimensiones: Beneficios, Costos, Flexibilidad y Riesgo. Usa modelado de organización compuesta y ajusta los beneficios por riesgo.

**Similitudes con BVIF v1:**
- Ambos cuantifican en términos monetarios los beneficios de iniciativas tecnológicas
- Ambos usan un proceso estructurado con compuertas por etapa
- Ambos producen cálculos de impacto financiero por métrica
- Ambos abordan preocupaciones de doble conteo
- El pilar de "Beneficios" de TEI es estructuralmente muy cercano a BVIF v1

**Diferencias con BVIF v1:**
- TEI incluye Costos, Flexibilidad (valor de opción) y Riesgo; BVIF v1 cubre solo Beneficios
- TEI aplica factores de ajuste por riesgo a los beneficios; BVIF v1 no
- TEI usa una "organización compuesta" (representante sintetizado); BVIF usa los datos reales del cliente
- TEI suele ser comisionado por proveedores; BVIF está orientado al cliente

**Qué toma BVIF:** La estructura de cálculo de beneficios por métrica (identificar métrica → establecer línea base → estimar mejora → monetizar). La metodología de beneficios de TEI es el análogo de marco único más cercano al enfoque de cálculo de BVIF v1.

**Referencias:** Forrester Research. (2023). *The Total Economic Impact™ Methodology*. Forrester. Schadler, T. & Fenwick, N. (2014). *The Mobile Mind Shift*. Groundswell Press (discute la aplicación de TEI).

---

#### 6. Val IT / COBIT — ISACA

**Qué es:** Val IT es un marco de gobierno de TI (ahora integrado en COBIT 2019) para gestionar inversiones de negocio habilitadas por TI. Define tres dominios: Gobierno del Valor, Gestión del Portafolio y Gestión de la Inversión.

**Similitudes con BVIF v1:**
- Ambos buscan establecer el valor de negocio de iniciativas de TI/tecnología
- Ambos requieren el desarrollo de un caso de negocio con propuestas de valor claras
- Ambos usan procesos de aprobación estructurados (Val IT: "revisiones Stage-Gate"; BVIF: "puntos de aprobación")
- El concepto de Val IT de "costos y beneficios del ciclo de vida completo" se alinea con la identificación estructurada de beneficios de BVIF

**Diferencias con BVIF v1:**
- Val IT es un marco de gobierno empresarial (políticas, procesos, estructuras); BVIF es una herramienta de estimación
- Val IT cubre la priorización a nivel de portafolio; BVIF trabaja a nivel de iniciativa individual
- Val IT incluye gestión de costos y ROI; BVIF no
- Val IT es pesado en proceso e intensivo en documentación; BVIF es comparativamente ligero

**Qué toma BVIF:** La filosofía de gobierno de validación de valor con compuertas por etapa y rendición de cuentas de las partes interesadas. El "el agente nunca avanza sin aprobación explícita" de BVIF refleja la disciplina de stage-gate de Val IT.

**Referencias:** ISACA (2008). *Val IT Framework 2.0*. ISACA (2019). *COBIT 2019 Framework: Governance and Management Objectives*.

---

#### 7. Information Economics — Parker, Benson & Trainor

**Qué es:** Una metodología para valorar inversiones de TI que va más allá del análisis financiero tradicional al incorporar "value linking" (efectos financieros indirectos), "value acceleration" (valor temporal de beneficios más tempranos) y puntuación de alineación estratégica.

**Similitudes con BVIF v1:**
- Ambos reconocen que el valor tecnológico no siempre es directamente medible en términos financieros tradicionales
- Ambos usan puntuación/evaluación estructurada de dimensiones de valor
- El concepto de "value linking" de Information Economics (conectar la mejora operativa con el impacto financiero mediante pasos intermedios) es paralelo a la cadena de "impacto financiero por unidad" de BVIF
- Ambos abordan el problema de los beneficios intangibles o difíciles de medir (la exclusión F3 de BVIF)

**Diferencias con BVIF v1:**
- Information Economics usa puntuación ponderada para la alineación estratégica; BVIF usa cuantificación monetaria pura
- Information Economics aborda el riesgo organizacional y el ajuste estratégico; BVIF se centra en el valor operativo
- Information Economics fue diseñado para la priorización de proyectos de TI; BVIF es para la estimación de valor de iniciativas individuales

**Qué toma BVIF:** El concepto de evaluación de factibilidad (las calificaciones F1/F2/F3 de BVIF hacen eco del reconocimiento de Information Economics de que no todas las dimensiones de valor son igualmente medibles) y la lógica de "value linking" de conectar métricas operativas con dólares mediante factores de conversión intermedios.

**Referencias:** Parker, M.M., Benson, R.J., & Trainor, H.E. (1988). *Information Economics: Linking Business Performance to Information Technology*. Prentice Hall.

---

#### 8. Applied Information Economics (AIE) — Douglas Hubbard

**Qué es:** AIE es una metodología de análisis de decisiones que aplica evaluación de probabilidad calibrada, análisis del valor de la información y simulación de Monte Carlo a decisiones de TI y de negocio. Enfatiza que "si importa, se puede medir".

**Similitudes con BVIF v1:**
- Ambos insisten en cuantificar el valor en lugar de dejarlo cualitativo
- Ambos usan descomposición estructurada (dividir el valor complejo en componentes medibles)
- La filosofía de AIE de que todo valor es medible (con los métodos adecuados) se alinea con el enfoque de calificaciones de factibilidad de BVIF — aunque BVIF es más pragmático (F3 = simplemente excluirlo)

**Diferencias con BVIF v1:**
- AIE usa juicio experto calibrado con elicitación formal de probabilidades; BVIF v1 usa estimaciones puntuales simples
- AIE incluye análisis del "valor de la información" (decidir qué medir a continuación); BVIF no
- AIE aplica simulación de Monte Carlo por defecto; BVIF v1 no (v2 lo agrega)
- AIE es pesado en metodología y requiere facilitadores capacitados; BVIF es guiado por IA y más ligero

**Qué toma BVIF (más aplicable a v2):** La filosofía de descomposición. La influencia de AIE aparece con más fuerza en v2, pero la descomposición estructurada de métricas de v1 refleja el principio de AIE de dividir el valor aparentemente intangible en subcomponentes medibles.

**Referencias:** Hubbard, D.W. (2014). *How to Measure Anything* (3ª ed.). Wiley. Hubbard, D.W. (2010). *The Failure of Risk Management*. Wiley.

---

### A.3 Resumen: posicionamiento de BVIF v1

BVIF v1 se entiende mejor como un **proceso de Gestión de Realización de Beneficios** (en filosofía) que usa **cálculos de beneficios por métrica al estilo TEI** (en mecánica), organizado por una **taxonomía de valor similar al Balanced Scorecard**, con **compuertas de gobierno al estilo Val IT** y una **anualización DCF** simplificada, despojada de descuento y de análisis del lado de los costos.

**Lo que v1 NO es:**
- No es una evaluación de inversión completa (sin costos → sin ROI/NPV)
- No es una herramienta de portafolio estratégico (alcance de iniciativa individual)
- No es una medición de valor realizado (solo prospectiva)
- No está ajustado por riesgo (estimación puntual única, sin probabilidad)

---

## Parte B: BVIF v2 (con incertidumbre) — Linaje metodológico adicional

v2 conserva todo el linaje de v1 (arriba) y agrega cuantificación de incertidumbre. Esta sección cubre solo los **nuevos elementos** introducidos en v2.

### B.1 Nuevos elementos y su ascendencia

| Nuevo elemento de BVIF v2 | Metodología más cercana | Técnica específica tomada |
|---|---|---|
| Estimaciones de tres puntos (P10/P50/P90) | PERT / Estimación de tres puntos | Distribución triangular a partir de pesimista/probable/optimista |
| Simulación de Monte Carlo (10K iteraciones) | Análisis Cuantitativo de Riesgos (QRA) / @RISK | Simulación estocástica con distribuciones muestreadas |
| Análisis de sensibilidad (r de Pearson) | Diagramas de tornado / QRA | Ranking de importancia de entradas basado en correlación |
| Proyección contrafactual de la línea base | Evaluación de Impacto / Evaluación de Programas | Lógica de diferencias en diferencias |
| Modelado de tasa de adopción/realización | Modelos de Adopción Tecnológica / BRM | Factor de realización explícito |
| Palancas de influencia (controlabilidad) | Applied Information Economics (AIE) | Valor del control / optimización de decisiones |
| Intervalos de confianza (rango P10–P90) | Estimación Probabilística de Costos (AACE) | Reporte estándar de percentiles |

---

### B.2 Comparaciones metodológicas detalladas (mejoras de v2)

#### 1. PERT — Estimación de tres puntos

**Qué es:** Program Evaluation and Review Technique (1958, Marina de EE. UU./Booz Allen). Usa tres estimaciones (optimista, más probable, pesimista) para modelar la incertidumbre en duraciones o costos de actividades. Fórmula PERT: Esperado = (O + 4M + P) / 6. La práctica moderna suele usar distribuciones triangulares o beta-PERT.

**Similitudes con BVIF v2:**
- Ambos recolectan exactamente tres puntos: pesimista, más probable, optimista
- Ambos los usan para definir una distribución de probabilidad (BVIF usa triangular)
- Ambos plantean la pregunta de forma idéntica a las partes interesadas ("¿Cuál es tu peor caso realista? ¿El más esperado? ¿El mejor realista?")
- Ambos están diseñados para la elicitación de juicio experto cuando los datos históricos son limitados

**Diferencias con BVIF v2:**
- El PERT clásico usa una distribución beta y una fórmula de promedio ponderado; BVIF v2 usa distribuciones triangulares alimentadas a Monte Carlo
- El PERT fue diseñado para la estimación de cronogramas; BVIF lo aplica a la estimación de beneficios
- El PERT suele producir un único valor esperado + varianza; BVIF produce distribuciones completas de percentiles
- El PERT no incorpora tasas de adopción ni contrafactuales

**Qué toma BVIF:** El protocolo de elicitación de tres puntos directamente. Las preguntas de BVIF a las partes interesadas ("¿Cuál es tu peor resultado realista? ¿Qué esperas más? ¿Cuál es tu mejor escenario realista?") son elicitación PERT de manual.

**Referencias:** Malcolm, D.G., Roseboom, J.H., Clark, C.E., & Fazar, W. (1959). "Application of a Technique for Research and Development Program Evaluation." *Operations Research*, 7(5), 646-669. PMI (2021). *PMBOK Guide* (7ª ed.), §6.4.

---

#### 2. Simulación de Monte Carlo en finanzas de proyectos / análisis de riesgos

**Qué es:** Una técnica computacional que ejecuta miles de iteraciones muestreando de distribuciones de entrada para producir una distribución de probabilidad de resultados. Práctica estándar en el análisis de riesgos de proyectos desde los años 80 (popularizada por herramientas como @RISK, Crystal Ball).

**Similitudes con BVIF v2:**
- Ambos ejecutan 10,000+ iteraciones muestreando de distribuciones definidas
- Ambos producen rangos de salida P10/P50/P90
- Ambos usan distribuciones triangulares para entradas de juicio experto
- Ambos combinan múltiples entradas inciertas de forma multiplicativa
- Ambos realizan análisis de sensibilidad después de la simulación

**Diferencias con BVIF v2:**
- El Monte Carlo tradicional de proyectos modela costos, cronograma Y beneficios; BVIF modela solo beneficios
- El Monte Carlo de proyectos suele usar entradas correlacionadas; BVIF v2 parece tratar las entradas como independientes
- Las aplicaciones tradicionales incluyen tasas de descuento y NPV en la simulación; BVIF no
- El Monte Carlo de proyectos suele usar más tipos de distribución (lognormal, uniforme, discreta); BVIF usa solo triangular

**Qué toma BVIF:** Todo el enfoque del motor de simulación — muestreo de distribución triangular, convención de 10,000 iteraciones, reporte de percentiles (P10/P50/P90) y análisis de sensibilidad post-simulación mediante correlación de Pearson. Esto es análisis cuantitativo de riesgos de manual.

**Referencias:** Vose, D. (2008). *Risk Analysis: A Quantitative Guide* (3ª ed.). Wiley. Palisade. (2020). *@RISK User Guide*. AACE International (2019). *Recommended Practice 41R-08: Risk Analysis and Contingency Determination*.

---

#### 3. Análisis de sensibilidad — Diagramas de tornado / Análisis de correlación

**Qué es:** Análisis post-simulación que identifica qué variables de entrada contribuyen más a la varianza de la salida. Dos enfoques principales: (a) variación de una a la vez (OAT) que produce gráficos de tornado, (b) basado en correlación (r de Pearson/Spearman entre entradas muestreadas y salida).

**Similitudes con BVIF v2:**
- Ambos usan coeficientes de correlación de Pearson entre entradas y salida
- Ambos clasifican las entradas por magnitud del valor r
- Ambos identifican qué variables "importan más" para el resultado
- Ambos establecen un umbral de significancia (BVIF usa r > 0.4 como umbral para "palancas")

**Diferencias con BVIF v2:**
- El análisis de sensibilidad tradicional se detiene en la identificación; BVIF v2 lo extiende a "evaluación de controlabilidad" y "cómo influir" — esto es más accionable
- La práctica estándar suele usar correlación de rangos de Spearman (mejor para relaciones no lineales); BVIF especifica Pearson
- El concepto de "palancas de influencia" de BVIF (controlabilidad × sensibilidad) va más allá del análisis de sensibilidad estándar hacia el terreno del soporte de decisiones

**Qué toma BVIF:** El enfoque de correlación de Pearson para el ranking de sensibilidad post-simulación. La innovación es la extensión de BVIF hacia recomendaciones de acción ponderadas por controlabilidad.

**Referencias:** Saltelli, A., et al. (2008). *Global Sensitivity Analysis: The Primer*. Wiley. Vose, D. (2008), Capítulo 12: "Sensitivity Analysis."

---

#### 4. Análisis contrafactual / Evaluación de impacto

**Qué es:** En la evaluación de programas (Banco Mundial, economía del desarrollo), el análisis contrafactual estima qué habría ocurrido en ausencia de una intervención. Los métodos incluyen diferencias en diferencias, regresión discontinua y emparejamiento por puntaje de propensión.

**Similitudes con BVIF v2:**
- Ambos restan "lo que habría pasado de todos modos" de la mejora observada/proyectada
- Ambos requieren proyectar explícitamente la trayectoria sin intervención
- Ambos usan datos de tendencia histórica como base para la estimación contrafactual
- Ambos abordan la atribución: separar la mejora causada por la iniciativa de la mejora orgánica

**Diferencias con BVIF v2:**
- La evaluación de impacto formal usa métodos estadísticos rigurosos (diseños cuasi-experimentales); BVIF usa simple extrapolación de tendencias
- La evaluación de impacto suele ocurrir post-intervención; BVIF la aplica pre-intervención (proyectando el contrafactual hacia adelante)
- Los métodos formales consideran factores de confusión, sesgo de selección, etc.; BVIF se apoya en el juicio de las partes interesadas sobre la trayectoria

**Qué toma BVIF:** El principio filosófico de que la atribución de valor requiere un contrafactual — solo puedes atribuirte el crédito por la mejora *más allá* de lo que habría ocurrido orgánicamente. Esta es quizás la adición intelectualmente más significativa de v2, arraigando a BVIF en la lógica de inferencia causal.

**Referencias:** Gertler, P.J., et al. (2016). *Impact Evaluation in Practice* (2ª ed.). World Bank. Angrist, J.D. & Pischke, J. (2009). *Mostly Harmless Econometrics*. Princeton University Press.

---

#### 5. Análisis de opciones reales (ROA)

**Qué es:** Aplica la teoría de opciones financieras a decisiones estratégicas/de proyectos bajo incertidumbre. Reconoce que la flexibilidad de la gerencia (para diferir, expandir, abandonar o cambiar) tiene un valor cuantificable. Usa modelos de Black-Scholes o de retícula binomial.

**Similitudes con BVIF v2:**
- Ambos reconocen que la incertidumbre no solo crea riesgo — crea valor de información
- El concepto de "palancas de influencia" de BVIF v2 (qué puedes controlar para desplazar la distribución) hace eco del principio de ROA de que la gestión activa bajo incertidumbre es valiosa
- Ambos están motivados por la insuficiencia de las estimaciones deterministas puntuales para inversiones inciertas

**Diferencias con BVIF v2:**
- ROA valora explícitamente la opción de diferir/abandonar/expandir; BVIF no fija precio a la opcionalidad
- ROA usa matemáticas de fijación de precios de opciones; BVIF usa simulación de Monte Carlo
- ROA trata fundamentalmente sobre la flexibilidad de decisión; BVIF trata sobre la estimación de valor
- ROA requiere estimación de volatilidad; BVIF requiere juicio experto de tres puntos
- BVIF no modela puntos de decisión secuenciales

**Qué toma BVIF:** Principalmente la motivación filosófica — las estimaciones deterministas son insuficientes para inversiones inciertas. La influencia intelectual de ROA es indirecta: BVIF v2 reconoce la incertidumbre pero se detiene antes de fijar el precio de las opciones que la incertidumbre crea.

**Referencias:** Copeland, T. & Antikarov, V. (2003). *Real Options: A Practitioner's Guide*. Texere. Trigeorgis, L. (1996). *Real Options: Managerial Flexibility and Strategy in Resource Allocation*. MIT Press.

---

#### 6. Applied Information Economics (AIE) — Hubbard

**Qué es:** (Descrito arriba.) AIE combina evaluación de probabilidad calibrada, simulación de Monte Carlo y análisis del valor de la información para la toma de decisiones bajo incertidumbre.

**Similitudes con BVIF v2 (alineación más fuerte que con v1):**
- Ambos usan la simulación de Monte Carlo como motor central de cuantificación
- Ambos descomponen el valor complejo en subcomponentes medibles con rangos de incertidumbre
- Ambos producen distribuciones de probabilidad en lugar de estimaciones puntuales
- Las "estimaciones expertas calibradas" de AIE son paralelas a la elicitación de tres puntos de las partes interesadas de BVIF
- Ambos identifican qué incertidumbres importan más (AIE: valor de la información; BVIF: análisis de sensibilidad)

**Diferencias con BVIF v2:**
- AIE usa entrenamiento formal de calibración para reducir el exceso de confianza del experto; BVIF se apoya en formular bien las preguntas
- AIE incluye el "Valor Esperado de la Información Perfecta (EVPI)" para determinar si vale la pena recopilar más datos; BVIF no
- AIE usa tipos de distribución más amplios (normal, lognormal, etc.); BVIF usa triangular
- AIE es una metodología general de decisiones; BVIF está construido a medida para el valor de iniciativas de IA

**Qué toma BVIF:** BVIF v2 es posiblemente el más cercano a AIE en espíritu — una implementación práctica de los principios de AIE (descomponer → estimar con incertidumbre → simular → identificar lo que importa) adaptada para la estimación del valor de iniciativas de IA, sin todo el aparato de calibración de AIE.

**Referencias:** Hubbard, D.W. (2014). *How to Measure Anything* (3ª ed.). Wiley.

---

#### 7. Tasa de adopción/realización — Adopción tecnológica y BRM

**Qué es:** El modelado de adopción tecnológica (Difusión de Innovaciones de Rogers, modelo de difusión de Bass) describe cómo se difunden las innovaciones en las organizaciones. BRM incluye explícitamente "tasas de realización" como la fracción de los beneficios teóricos que realmente se captura.

**Similitudes con BVIF v2:**
- La tasa de adopción de BVIF es paralela directa al "factor de realización de beneficios" de BRM
- Ambos reconocen que el valor teórico nunca se realiza al 100% en la práctica
- Ambos tratan la adopción como una variable separada del desempeño técnico
- La estimación de tres puntos de BVIF para la tasa de adopción captura la incertidumbre del cambio organizacional

**Diferencias con BVIF v2:**
- Los modelos formales de adopción (Bass, curva en S) modelan la adopción a lo largo del tiempo; BVIF usa un porcentaje estático
- BRM suele dar seguimiento a la realización post-implementación; BVIF la estima pre-implementación
- BVIF no modela la forma de la curva de adopción (periodo de arranque)

**Qué toma BVIF:** La separación explícita entre "mejora de la capacidad técnica" y "realización organizacional de esa mejora". Esta es quizás la adición práctica más importante de BVIF v2 — reconocer que un sistema de IA con desempeño perfecto aún requiere adopción para crear valor.

**Referencias:** Rogers, E.M. (2003). *Diffusion of Innovations* (5ª ed.). Free Press. Bass, F.M. (1969). "A New Product Growth Model for Consumer Durables." *Management Science*, 15(5).

---

#### 8. Estimación probabilística de costos de AACE (Estimaciones por clase)

**Qué es:** La Association for the Advancement of Cost Engineering (AACE) define cinco clases de estimaciones de costos (Clase 5 a Clase 1), cada una con rangos de exactitud esperados. Las estimaciones por clase usan rangos P10/P50/P90 (o P80) como salida estándar, generados mediante simulación de Monte Carlo.

**Similitudes con BVIF v2:**
- Ambos usan P10/P50/P90 como formato de salida estándar
- Ambos usan simulación de Monte Carlo para generar esos percentiles
- Ambos reconocen que la calidad de la estimación depende de la madurez de los datos de entrada
- Las calificaciones de factibilidad de BVIF (F1/F2/F3) son conceptualmente paralelas al sistema de clases de estimación de AACE (mejores datos → rangos más estrechos)

**Diferencias con BVIF v2:**
- AACE se centra en la estimación de costos; BVIF se centra en la estimación de beneficios
- AACE tiene definiciones formales de clase con rangos de exactitud; BVIF no tiene una taxonomía formal de clases de estimación
- AACE incluye la determinación de contingencia; BVIF no

**Qué toma BVIF:** La convención de reporte P10/P50/P90 y la expectativa de que las estimaciones probabilísticas son el estándar profesional para pronósticos de grado de decisión.

**Referencias:** AACE International (2019). *Recommended Practice 18R-97: Cost Estimate Classification System*. AACE International (2019). *RP 41R-08: Risk Analysis and Contingency Determination*.

---

### B.3 Resumen: posicionamiento de BVIF v2

BVIF v2 superpone **elicitación de tres puntos PERT**, **simulación de Monte Carlo** (QRA estándar), **análisis de sensibilidad basado en correlación** y **lógica de atribución contrafactual** sobre la base BRM/TEI de v1.

El análogo de marco único más cercano es **Applied Information Economics (AIE)** — ambos comparten la filosofía de "descomponer → estimar con rangos → simular → identificar lo que importa". BVIF v2 puede entenderse como una **implementación específica de dominio, guiada por IA, de los principios de AIE** enfocada exclusivamente en el lado del valor de las iniciativas de IA.

**Lo que v2 agrega más allá de la práctica estándar:**
- **Palancas de influencia** (controlabilidad × sensibilidad) — extiende el análisis de sensibilidad tradicional hacia el terreno prescriptivo
- **Elicitación guiada por IA** — usa el IDE Kiro para facilitar lo que tradicionalmente requiere facilitadores capacitados
- **Sustracción contrafactual** — lleva la lógica de inferencia causal a la estimación del valor de TI (poco común en la práctica de la industria)

---

## Parte C: Tabla comparativa consolidada

| Dimensión | BVIF v1 | BVIF v2 | EVA | DCF/NPV | BRM | TEI | PERT | Monte Carlo (QRA) | AIE | BSC | Opciones reales |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Alcance** | Solo beneficios | Solo beneficios | P&L completo | Inversión completa | Beneficios + costos | Beneficios + costos + flexibilidad + riesgo | Cronograma/costo | Cualquier cantidad incierta | Decisión completa | KPIs estratégicos | Flexibilidad de inversión |
| **Salida** | Un número en $ | Rango P10/P50/P90 | Un número en $ | Un número en $ | Registro de beneficios | Valor en dólares | Duración/costo esperado | Distribución de probabilidad | Distribución de probabilidad | Scorecard | Valor de opción |
| **Incertidumbre** | Ninguna | Monte Carlo | Ninguna | Análisis de escenarios | Cualitativa | Ajustada por riesgo | Beta/triangular | Probabilística completa | Probabilística completa | Ninguna | Basada en volatilidad |
| **Horizonte temporal** | Anualizado (estado estable) | Anualizado (estado estable) | Anual | Multianual descontado | Ciclo de vida del proyecto | 3 años | Duración del proyecto | Ciclo de vida del proyecto | Horizonte de decisión | Continuo | Vida de la opción |
| **Lado del costo** | ❌ Excluido | ❌ Excluido | ✅ Cargo de capital | ✅ Inversión completa | ✅ Opcional | ✅ Incluido | N/A | ✅ Normalmente | ✅ Incluido | ❌ Indirecto | ✅ Precio de ejercicio |
| **Compuertas de partes interesadas** | ✅ Cada etapa | ✅ Cada etapa | ❌ | ❌ | ✅ Hitos clave | ❌ | ❌ | ❌ | ✅ | ✅ Revisiones | ❌ |
| **Contrafactual** | ❌ | ✅ Explícito | ❌ | ❌ (implícito en el descuento) | ❌ | ❌ | ❌ | ❌ | ✅ Posible | ❌ | ❌ |
| **Tasa de adopción** | ❌ (asume 100%) | ✅ Tres puntos | N/A | Implícita en el FC | ✅ Factor de realización | ✅ Ajuste por riesgo | N/A | A veces | Posible | N/A | N/A |
| **Análisis de sensibilidad** | ❌ | ✅ r de Pearson | ❌ | ✅ Escenario | ❌ | ❌ | ❌ | ✅ Estándar | ✅ EVPI | ❌ | ✅ Griegas |
| **Accionabilidad** | Informe | Informe + palancas | Métrica | Go/no-go | Plan de acción | Caso de negocio | Cronograma | Respuesta al riesgo | Optimización de decisiones | Ejecución de estrategia | Decisión de momento |

---

## Parte D: Genealogía intelectual de BVIF (resumen visual)

```
                    ┌─────────────────────┐
                    │  Benefits Realization │
                    │  Management (BRM)    │  ← Filosofía: identificación estructurada de beneficios
                    └──────────┬──────────┘       con gobierno de partes interesadas
                               │
         ┌─────────────────────┼─────────────────────┐
         │                     │                     │
         ▼                     ▼                     ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ Balanced        │  │ Forrester TEI   │  │ Val IT / COBIT  │
│ Scorecard       │  │ (Cálc. benef.)  │  │ (Stage gates)   │
│ (Categorías)    │  │                 │  │                 │
└────────┬────────┘  └────────┬────────┘  └────────┬────────┘
         │                     │                     │
         └─────────────────────┼─────────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     BVIF v1         │
                    │  (Determinista)     │
                    └──────────┬──────────┘
                               │
         ┌─────────────────────┼─────────────────────┐
         │                     │                     │
         ▼                     ▼                     ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ PERT            │  │ Monte Carlo /   │  │ Análisis        │
│ (Est. 3 puntos) │  │ QRA / AIE       │  │ contrafactual   │
│                 │  │ (Simulación)    │  │ (Atribución)    │
└────────┬────────┘  └────────┬────────┘  └────────┬────────┘
         │                     │                     │
         └─────────────────────┼─────────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     BVIF v2         │
                    │ (Con incertidumbre) │
                    └─────────────────────┘
```

---

## Parte E: Qué hace distintivo a BVIF

A pesar de basarse en metodologías establecidas, BVIF tiene características distintivas que no se encuentran en ningún ancestro individual:

1. **Pureza centrada en el valor** — Ningún otro marco excluye los costos de forma tan deliberada. Esto es por diseño: BVIF se posiciona como el *primer paso* del análisis de inversión (validar la hipótesis de valor) antes de comprometerse con el desarrollo completo del caso de negocio.

2. **Facilitación guiada por IA** — Las metodologías tradicionales requieren consultores o facilitadores capacitados. BVIF usa el IDE Kiro como facilitador, haciendo la metodología accesible sin experiencia especializada.

3. **Filtrado por factibilidad (F1/F2/F3)** — Aunque BRM e Information Economics discuten la medibilidad, el sistema de tres niveles de BVIF con una regla de exclusión estricta (F3 = descartar) es más prescriptivo que la mayoría de los marcos.

4. **Verificación de doble conteo** — La deduplicación explícita de métricas superpuestas es poco común en las metodologías formales (la mayoría asume que el analista lo manejará; BVIF lo convierte en un paso formal del proceso).

5. **Contrafactual + Adopción + Sensibilidad como paquete integrado** (v2) — Ninguna metodología individual combina las tres de la forma en que lo hace BVIF v2. El contrafactual proviene de la evaluación de impacto, la adopción de BRM/teoría de difusión, la sensibilidad de QRA — pero integrar las tres en un Monte Carlo centrado solo en beneficios es novedoso.

6. **Palancas de influencia** (v2) — Pasar de "esto es lo que impulsa la varianza" (sensibilidad estándar) a "esto es lo que puedes controlar y cómo mejorarlo" es una extensión prescriptiva que no se encuentra en la práctica estándar de QRA.

---

## Referencias (consolidadas)

- AACE International (2019). *RP 18R-97: Cost Estimate Classification System*.
- AACE International (2019). *RP 41R-08: Risk Analysis and Contingency Determination*.
- Angrist, J.D. & Pischke, J. (2009). *Mostly Harmless Econometrics*. Princeton.
- Bass, F.M. (1969). "A New Product Growth Model for Consumer Durables." *Management Science*, 15(5).
- Bradley, G. (2010). *Benefit Realisation Management* (2nd ed.). Gower.
- Brealey, R., Myers, S., & Allen, F. (2020). *Principles of Corporate Finance* (13th ed.). McGraw-Hill.
- Copeland, T. & Antikarov, V. (2003). *Real Options: A Practitioner's Guide*. Texere.
- Damodaran, A. (2012). *Investment Valuation* (3rd ed.). Wiley.
- Forrester Research (2023). *The Total Economic Impact™ Methodology*.
- Gertler, P.J., et al. (2016). *Impact Evaluation in Practice* (2nd ed.). World Bank.
- Hubbard, D.W. (2014). *How to Measure Anything* (3rd ed.). Wiley.
- ISACA (2008). *Val IT Framework 2.0*.
- ISACA (2019). *COBIT 2019 Framework*.
- Kaplan, R.S. & Norton, D.P. (1996). *The Balanced Scorecard*. Harvard Business School Press.
- Malcolm, D.G., et al. (1959). "Application of a Technique for R&D Program Evaluation." *Operations Research*, 7(5).
- Parker, M.M., Benson, R.J., & Trainor, H.E. (1988). *Information Economics*. Prentice Hall.
- PMI (2019). *Benefits Realization Management: A Practice Guide*.
- PMI (2021). *PMBOK Guide* (7th ed.).
- Rogers, E.M. (2003). *Diffusion of Innovations* (5th ed.). Free Press.
- Saltelli, A., et al. (2008). *Global Sensitivity Analysis: The Primer*. Wiley.
- Stewart, G.B. III (1991). *The Quest for Value*. HarperBusiness.
- Trigeorgis, L. (1996). *Real Options*. MIT Press.
- Vose, D. (2008). *Risk Analysis: A Quantitative Guide* (3rd ed.). Wiley.
