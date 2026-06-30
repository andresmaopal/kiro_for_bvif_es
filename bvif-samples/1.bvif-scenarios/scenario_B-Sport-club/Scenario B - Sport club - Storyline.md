
> ⚠️ **Aviso:** Esta es una **historia completamente ficticia** creada con fines de prueba del marco (BVIF). El club, sus personajes, las cifras financieras y los eventos descritos son totalmente inventados. Cualquier parecido con clubes, personas o resultados reales es coincidencia. Esta historia se inspiró en — y referencia al final — un caso de estudio real publicado por AWS que involucra al Clube Atlético Mineiro.

***

## El Club

En el corazón del estado brasileño de Minas Gerais, en una ciudad industrial de tamaño medio llamada **São Bernardo das Minas**, se encuentra un club de fútbol que los locales llaman **"Os Bandeirantes"** — los Pioneros.

El **Clube Esportivo Bandeirantes** fue fundado en **1923** por un grupo de trabajadores siderúrgicos. Cien años después, el club tiene **6.2 millones de aficionados registrados**, un moderno estadio de 38,000 asientos — la **Arena Ferradura** (Arena Herradura), inaugurada en 2019 — y una reciente racha de buen rendimiento que le valió títulos consecutivos del Campeonato Brasileiro Série A en 2022 y 2023. Para 2024, lo que el consejo perseguía era la sostenibilidad financiera.

***

## Cómo gana dinero un club de fútbol en Brasil

Los clubes brasileños dependen de una mezcla de ingresos más frágil y diversificada que las ligas europeas. Para Bandeirantes, el desglose de 2025 fue:

| Fuente de ingresos | Ingresos 2025 | Proporción | Nota |
|---|---|---|---|
| Derechos de TV y streaming | \$86.0M | 38% | En gran medida fijos por contrato colectivo; el descenso reduce esto en más del 60%. |
| Membresía — Sócio Torcedor | \$40.8M | 19% | 75,000 miembros activos; cuotas mensuales recurrentes de \$30–\$150. |
| Boletería de día de partido | \$36.8M | 18% | 27 partidos de local nacionales; capacidad de 38,000 asientos. |
| Comida, bebida y retail del estadio | \$24.8M | 12% | 34 puntos de A&B, 4 tiendas del club, 12 kioscos de cerveza en el estadio. |
| Mercancía y licencias | \$18.4M | 9% | Tienda propia + e-commerce + minoristas con licencia. |
| Transferencias de jugadores (irregular) | \$15.2M | — | Excluido del análisis operativo (no recurrente). |
| **Total operativo (excl. transferencias)** | **\$206.8M** | 100% | |

***

## El problema de datos y la base construida para resolverlo

A principios de 2024, el equipo de analítica del club observó que los datos de 6.2 millones de fans estaban dispersos en siete sistemas que nunca se habían comunicado entre sí — boletería, membresía de socios, punto de venta de A&B, app del club, Wi-Fi del estadio, e-commerce y redes sociales. El club podía decirte cuántos chocolates calientes se vendieron el sábado. No podía decirte quién los compró, si esa persona era miembro, o si era probable que renovara el mes siguiente.

_"Teníamos los ingredientes para un banquete,"_ observó la CFO Renata Magalhães, _"y ninguna cocina para cocinar."_

En marzo de 2024, el recién nombrado **Director Digital (CDO) Marcos Alves** — reclutado de una fintech brasileña seis meses antes — obtuvo la aprobación del consejo para un programa de 24 meses: **Projeto Bandeira**. Antes de definir el alcance de cualquier trabajo de IA, trazó una línea firme:

> _"No vamos a construir inteligencia sobre la ignorancia. La Fase 1 son los datos. Todo lo demás viene después."_

La Fase 1, completada para julio de 2024, construyó **BOLALAKE**: una plataforma de datos unificada que consolida cinco años de datos históricos de los siete sistemas, con cada interacción de fan ahora vinculada a una sola identidad. La vista de 360 grados del fan se convirtió en una base de datos.

A principios de 2026, con un año completo de BOLALAKE operativo, el liderazgo ha sacado a la luz tres iniciativas de IA en consideración. La base de datos necesaria para evaluar el valor potencial para el club de cualquiera de ellas ya está en su lugar.

***

## Línea base comercial de cinco años (2021–2025)

> 📋 **Nota:** Todas las cifras están en dólares estadounidenses. El año 2025 es la línea base "as-is" — no se ha desplegado ninguna iniciativa de IA. Las tablas que siguen proporcionan los datos necesarios para cuantificar cada una de las tres iniciativas de IA descritas más adelante en este documento.

### Resumen de ingresos anuales

| Fuente de ingresos | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Derechos de TV y streaming | \$80.0M | \$82.0M | \$83.0M | \$85.0M | \$86.0M |
| Membresía — Sócio | \$22.3M | \$33.0M | \$39.9M | \$41.2M | \$40.8M |
| Boletería de día de partido | \$24.8M | \$31.4M | \$33.6M | \$33.8M | \$36.8M |
| Comida, bebida y retail del estadio | \$17.4M | \$20.8M | \$22.4M | \$23.1M | \$24.8M |
| Mercancía y licencias | \$13.8M | \$15.4M | \$17.2M | \$17.6M | \$18.4M |
| **Total operativo (excl. transferencias)** | **\$158.3M** | **\$182.6M** | **\$196.1M** | **\$200.7M** | **\$206.8M** |

Crecimiento de ingresos operativos a cinco años (2021→2025): **+30.6%**. Año más reciente (2024→2025): **+3.0%**. Los ingresos crecieron con fuerza hasta 2023 impulsados por dos títulos; el crecimiento se ha desacelerado marcadamente desde entonces, y los ingresos por membresía declinaron por primera vez en 2025.

***

## Iniciativa A — Precios dinámicos de entradas

**La observación:** El club cobra el mismo precio por cada partido, sin importar la demanda. Los precios de entrada de referencia han subido un promedio de apenas 1.8% por año desde 2021, muy por debajo de la inflación anual del 8–10%. Un derbi que se agota en horas tiene el mismo precio que un partido entre semana contra un recién ascendido que llena apenas la mitad del estadio.

**La idea:** Una herramienta de precios impulsada por IA que analiza las señales de demanda de cada partido próximo — ranking del oponente, etapa de la competición, día de la semana, asistencia histórica, engagement de los fans — y recomienda un precio óptimo para cada sección del estadio. Las decisiones de precios permanecen con el equipo comercial, informadas por el modelo.

### Desempeño anual de boletería

| Año | Partidos de local | Asistencia total | Asistencia prom. | Capacidad | Utilización | Ingresos de taquilla |
|---|---|---|---|---|---|---|
| 2021 | 25 | 593,750 | 23,750 | 38,000 | 62% | \$24.8M |
| 2022 | 28 | 766,360 | 27,370 | 38,000 | 72% | \$31.4M |
| 2023 | 27 | 779,220 | 28,860 | 38,000 | 76% | \$33.6M |
| 2024 | 26 | 740,480 | 28,480 | 38,000 | 75% | \$33.8M |
| 2025 | 27 | 779,760 | 28,880 | 38,000 | 76% | \$36.8M |

_Solo partidos nacionales (Série A + Copa do Brasil). El club también fue local en 4 partidos de la Copa Libertadores en 2025 — ver desglose abajo._

### Desempeño trimestral de boletería — 8 trimestres

| Trimestre | Partidos de local | Asistencia total | Ocupación prom. | Precio prom. de entrada | Ingresos de taquilla |
|---|---|---|---|---|---|
| Q1 2024 | 4 | 110,200 | 73% | \$46.20 | \$5.09M |
| Q2 2024 | 6 | 168,720 | 74% | \$46.20 | \$7.79M |
| Q3 2024 | 8 | 230,560 | 76% | \$46.20 | \$10.65M |
| Q4 2024 | 8 | 231,000 | 76% | \$44.80 | \$10.27M |
| Q1 2025 | 5 | 137,750 | 72% | \$46.80 | \$6.45M |
| Q2 2025 | 7 | 197,050 | 74% | \$47.20 | \$9.30M |
| Q3 2025 | 8 | 232,800 | 76% | \$47.20 | \$10.99M |
| Q4 2025 | 7 | 212,160 | 80% | \$47.60 | \$10.10M |

### Desglose de ocupación por tipo de partido 2025 (31 partidos de local, nacional + Libertadores)

| Tipo de partido | # Partidos | Ocupación prom. | Ingresos prom. / partido | Asientos vacíos (prom.) |
|---|---|---|---|---|
| Derbi local (vs. EC Fundição) | 2 | 99% | \$1.78M | 380 |
| Oponente Top-4 — fin de semana | 5 | 94% | \$1.68M | 2,280 |
| Oponente Top-4 — entre semana | 3 | 82% | \$1.46M | 6,840 |
| Media tabla — fin de semana | 6 | 80% | \$1.42M | 7,600 |
| Media tabla — entre semana | 6 | 63% | \$1.14M | 14,060 |
| Recién ascendido / Mitad inferior | 5 | 56% | \$1.00M | 16,720 |
| **Promedio nacional** | **27** | **~76%** | **~\$1.36M** | **~9,200** |
| Copa Libertadores de local | 4 | 88% | \$1.66M | 4,560 |
| **Todos los partidos (incl. Libertadores)** | **31** | **~78%** | **~\$1.40M** | **~8,600** |

En 2025, los 11 partidos nacionales de menor demanda dejaron **168,000 asientos sin vender**. Los 7 partidos nacionales de mayor demanda se agotaron al mismo precio plano, dejando ingresos del lado de la demanda sin capturar.

### Engagement de Wi-Fi del estadio y en la app por tipo de partido en 2025

| Tipo de partido | Sesiones de Wi-Fi prom. / partido | Tiempo de Wi-Fi prom. / fan | Sesiones de app durante el partido |
|---|---|---|---|
| Derbi local | 24,800 | 58 min | 18,200 |
| Oponente Top-4 — fin de semana | 22,400 | 51 min | 15,600 |
| Oponente Top-4 — entre semana | 18,600 | 49 min | 13,100 |
| Media tabla — fin de semana | 17,900 | 46 min | 11,400 |
| Media tabla — entre semana | 13,200 | 44 min | 8,200 |
| Recién ascendido / Mitad inferior | 11,800 | 42 min | 7,100 |
| Copa Libertadores de local | 21,500 | 53 min | 14,400 |
| **Promedio 2025** | **~17,800** | **~47 min** | **~12,000** |

_Los datos de Wi-Fi los proporciona un contratista externo de servicios del recinto bajo un contrato operativo separado; los informes semanales agregados son la única salida disponible._

### Referencia financiera y de benchmark

- **Precio promedio de entrada (2025, mezclado):** \$47.20 por asiento vendido (solo ingresos de taquilla).
- **Ingreso promedio por fan asistente (entrada + complementario en taquilla):** ~\$73.10. _El gasto complementario en taquilla cubre comida, bebida y mercancía comprada por los fans dentro de la Arena Ferradura el día del partido — promediando \$25.90 por asistente en 2025._
- **Contexto de la industria:** La utilización de estadios de la Premier League está por encima del 95%, con precios basados en demanda integrados en la mayoría de los partidos de primera división. La Liga promedia 68% con precios variables crecientes en partidos estelares. Los San Francisco Giants — el primer equipo deportivo importante en adoptar precios dinámicos completos en 2009 — vieron crecer significativamente sus ingresos de taquilla en el primer año. Las franquicias de la NFL que usan precios dinámicos promedian una utilización general del 88–92%. Los clubes brasileños que han piloteado precios variables para partidos de Libertadores y de copa han reportado aumentos de ingresos de un dígito a dos dígitos bajos en esas categorías específicas.
- **Tipo de beneficio esperado:** aumento de ingresos de taquilla, proveniente de dos efectos — optimización de precios en partidos de alta demanda (capturando la disposición a pagar que el precio plano de \$47.20 actualmente deja sobre la mesa) y estímulo de la demanda en partidos de baja demanda (llenando algunos de los 168,000 asientos vacíos observados en 2025).

***

## Iniciativa B — Predicción de abandono de membresías

**La observación:** Casi la mitad de todos los socios no renuevan cada año (tasa de renovación del 54% en 2025). 36,000 miembros salieron en 2025 — 19,800 cancelaciones voluntarias y 16,200 bajas por falla de pago — frente a apenas 32,800 nuevas adquisiciones. El club no tiene ninguna señal anticipada de quién está a punto de irse: cada esfuerzo de retención se lanza después de que la decisión (o el pago fallido) ya ocurrió.

**La idea:** Un modelo de IA que monitorea el comportamiento de los miembros de forma continua — frecuencia de asistencia, engagement en la app, historial de pagos, tendencias de engagement — e identifica a los miembros en riesgo de cancelar antes de que lo hagan, permitiendo un alcance de retención dirigido.

### Flujo anual de membresías

| Año | Miembros (1 ene) | Nuevos miembros | Cancelaciones voluntarias | Bajas (falla de pago) | Miembros (31 dic) | Tasa de renovación | Ingresos por membresía |
|---|---|---|---|---|---|---|---|
| 2021 | 32,600 | 23,400 | 6,800 | 4,600 | 44,600 | 65% | \$22.3M |
| 2022 | 44,600 | 38,000 | 10,300 | 7,500 | 64,800 | 60% | \$33.0M |
| 2023 | 64,800 | 39,000 | 15,800 | 12,000 | 76,000 | 57% | \$39.9M |
| 2024 | 76,000 | 34,900 | 18,300 | 14,400 | 78,200 | 57% | \$41.2M |
| 2025 | 78,200 | 32,800 | 19,800 | 16,200 | 75,000 | 54% | \$40.8M |

_Tasa de renovación = % de miembros activos el 1 de enero que siguen activos el 31 de diciembre. Antes de BOLALAKE, el sistema de membresía registraba las cancelaciones voluntarias y las bajas por falla de pago juntas como "finalizadas"; la división mostrada arriba se reconstruyó a partir del retrospectivo de BOLALAKE de 2024._

Las tasas de renovación han ido a la baja de forma constante — del 65% en 2021, pasando por el 60% en 2022 y hacia el rango de 54–57% desde 2023 en adelante. Las bajas (salidas por falla de pago) son una característica estructural del modelo de suscripción mensual brasileño, representando el 40–45% del total de salidas durante todo el periodo; esto refleja el churn por límite de tarjeta de pago más que un rechazo activo del miembro. La tendencia descendente de renovación quedó enmascarada durante años por una adquisición agresiva: durante el periodo de títulos 2022–2023, el club incorporó 38–39 mil nuevos miembros por año. Para 2025, incluso con 32,800 nuevas altas, la adquisición ya no podía seguir el ritmo de las 36,000 salidas totales — produciendo el primer declive neto del club de 3,200 miembros.

### Desempeño trimestral de membresías — 8 trimestres

| Trimestre | Miembros (inicio) | Nuevos | Voluntarias | Bajas | Miembros (fin) | Tasa de renovación trimestral | Ingresos trimestrales |
|---|---|---|---|---|---|---|---|
| Q1 2024 | 76,000 | 7,700 | 4,100 | 3,300 | 76,300 | 90.3% | \$9.85M |
| Q2 2024 | 76,300 | 8,900 | 4,500 | 3,500 | 77,200 | 89.5% | \$10.10M |
| Q3 2024 | 77,200 | 9,300 | 4,700 | 3,700 | 78,100 | 89.1% | \$10.30M |
| Q4 2024 | 78,100 | 9,000 | 5,000 | 3,900 | 78,200 | 88.6% | \$10.95M |
| Q1 2025 | 78,200 | 7,700 | 4,600 | 3,800 | 77,500 | 89.3% | \$10.40M |
| Q2 2025 | 77,500 | 8,400 | 4,900 | 4,000 | 77,000 | 88.5% | \$10.20M |
| Q3 2025 | 77,000 | 8,500 | 5,000 | 4,100 | 76,400 | 88.2% | \$10.05M |
| Q4 2025 | 76,400 | 8,200 | 5,300 | 4,300 | 75,000 | 87.4% | \$10.15M |

### Economía de la membresía (2025)

| Métrica | Valor |
|---|---|
| Ingreso anual promedio por socio | \$541 |
| Margen bruto promedio por miembro (después de costos de servicio) | \$470 |
| Costo estimado de adquirir un nuevo miembro (mezclado) | \$47 |
| Cancelaciones voluntarias en 2025 | 19,800 |
| Bajas por falla de pago en 2025 | 16,200 |
| Total de miembros que salieron en 2025 | 36,000 |
| Nuevos miembros adquiridos en 2025 | 32,800 |
| Cambio neto de membresía | −3,200 |
| Costo de reemplazar a los miembros salientes mediante nueva adquisición (2025) | \$1.69M |

### Señales de comportamiento disponibles en BOLALAKE (por miembro, mensual)

| Señal | Cobertura | Uso en el modelo de abandono |
|---|---|---|
| Asistencia a partidos (torniquete) | 100% de los miembros | Indicador principal de engagement |
| Sesiones de app y pantallas vistas | 84% de los miembros (los que usan la app) | Engagement secundario; la pendiente de la tendencia > el nivel absoluto (un miembro cuyo uso está cayendo está en mayor riesgo que uno con un uso bajo pero estable) |
| Transacciones de A&B y mercancía vinculadas al ID del fan | 71% de los miembros | Trayectoria de gasto |
| Historial de pagos (rechazos, pagos tardíos) | 100% de los miembros | Fuerte indicador adelantado de abandono |
| Bajas de nivel (tier) | 100% de los miembros | Fuerte indicador adelantado de abandono |

### Mezcla de canales de adquisición de miembros en 2025

| Canal de adquisición | Nuevos miembros 2025 | Proporción | CAC prom. |
|---|---|---|---|
| Kiosco del estadio en día de partido | 10,200 | 31% | \$22 |
| Sitio web del club | 8,200 | 25% | \$38 |
| App móvil | 6,200 | 19% | \$31 |
| Banco socio (tarjeta co-branded) | 4,600 | 14% | \$74 |
| Referido de un miembro existente | 2,300 | 7% | \$18 |
| Campañas salientes | 1,300 | 4% | \$96 |
| **Total / mezclado** | **32,800** | **100%** | **\$47** |

_La mezcla de canales se ha mantenido ampliamente estable desde 2022. La adquisición por kiosco del estadio se dispara durante los derbis y los partidos que deciden títulos._

### Referencia financiera y de benchmark

- **Valor anual de un miembro retenido:** \$541 en ingresos (\$470 de margen bruto).
- **Contexto de la industria:** Los abonados de temporada de la NFL renuevan al 85–90% anual. Las franquicias de la NBA están en el rango del 80–85%. Los clubes de la MLS promedian 70–76%. La English Premiership Rugby — estructuralmente el comparable más cercano, con una economía de fans similar al modelo de sócio torcedor — reporta 62–74%. Los clubes brasileños de Série A comparables se ubican entre el 54% y el 66% según el desempeño deportivo, lo que coloca el 54% actual de Bandeirantes en la parte baja de su grupo de pares. Las organizaciones de deportes, streaming y telco que han desplegado programas de predicción de abandono impulsados por IA normalmente reportan mejoras de renovación medidas en puntos porcentuales de dos dígitos bajos dentro del primer año, concentradas en miembros que muestran desvinculación temprana.
- **Tipo de beneficio esperado:** aumento de la tasa de renovación, impulsado por un alcance de retención personalizado a los miembros marcados como en riesgo 30–60 días antes de los eventos típicos de cancelación. Cada punto porcentual de mejora de renovación preservado en la base de 75,000 miembros se traduce directamente en ingresos de membresía retenidos a \$541 por miembro, más el costo de readquisición evitado de \$47 por reemplazo.

***

## Iniciativa C — Personalización en el estadio

**La observación:** Cada fan que entra a la Arena Ferradura recibe la misma experiencia genérica — las mismas ofertas (o ninguna), las mismas concesiones indiferenciadas, sin reconocimiento de su historial. Un miembro que ha asistido a 60 partidos y siempre ordena la misma comida es tratado igual que alguien que asiste por primera vez.

**La idea:** Un motor de personalización con IA que usa el perfil BOLALAKE de cada fan para entregar ofertas y contenido individualmente relevantes a través de la app del club antes y durante cada partido — reflejando el historial de compras, la frecuencia de asistencia, el estado de membresía y las preferencias dentro del estadio.

### Gasto anual de día de partido por fan

| Año | Asistencia prom. | A&B / Fan | Mercancía / Fan | Gasto total / Fan | Ingresos totales de gasto de día de partido | Inflación acumulada (vs 2021) |
|---|---|---|---|---|---|---|
| 2021 | 23,750 | \$17.60 | \$5.60 | \$23.20 | \$13.77M | — |
| 2022 | 27,370 | \$18.10 | \$5.90 | \$24.00 | \$18.39M | ~9% |
| 2023 | 28,860 | \$18.80 | \$6.20 | \$25.00 | \$21.05M | ~19% |
| 2024 | 28,480 | \$19.10 | \$6.30 | \$25.40 | \$19.55M | ~29% |
| 2025 | 28,880 | \$19.40 | \$6.50 | \$25.90 | \$20.20M | ~40% |

_Gasto de día de partido = A&B + mercancía comprada por los fans asistentes el día del partido. Excluye el costo de la entrada y el e-commerce durante todo el año._

Crecimiento nominal 2021→2025: +11.6%. Inflación acumulada: ~40%. **El gasto real por fan ha disminuido aproximadamente 20%** a pesar de una base de asistencia creciente.

### Gasto trimestral de día de partido por fan — 8 trimestres

| Trimestre | Asistencia prom. | Gasto / Fan | Gasto total de día de partido |
|---|---|---|---|
| Q1 2024 | 27,550 | \$24.80 | \$2.73M |
| Q2 2024 | 28,120 | \$25.10 | \$4.24M |
| Q3 2024 | 28,820 | \$25.40 | \$5.86M |
| Q4 2024 | 28,875 | \$25.80 | \$5.96M |
| Q1 2025 | 27,550 | \$25.30 | \$3.49M |
| Q2 2025 | 28,150 | \$25.70 | \$5.06M |
| Q3 2025 | 29,100 | \$26.00 | \$6.05M |
| Q4 2025 | 30,310 | \$26.40 | \$5.60M |

### Segmentación de gasto por perfil de fan en 2025

| Perfil de fan | % de asistencia | Gasto prom. de día de partido | Indexado vs. prom. |
|---|---|---|---|
| Socio — alta asistencia (10+ partidos/año) | 18% | \$38.40 | 148 |
| Socio — asistencia moderada (4–9) | 24% | \$27.20 | 105 |
| Socio — baja asistencia (1–3) | 21% | \$19.80 | 76 |
| No miembro — entrada de compra única | 31% | \$16.40 | 63 |
| Invitado corporativo / de hospitalidad | 6% | \$63.00 | 243 |
| **Promedio mezclado** | **100%** | **\$25.90** | **100** |

### Hallazgos de comunicación dirigida (análisis BOLALAKE 2025)

- Los fans que recibieron cualquier comunicación digital dirigida en las 48 horas previas al partido gastaron **\$4.40 más** en promedio que quienes no la recibieron.
- Solo el **34%** de los usuarios de la app tenían habilitadas las notificaciones push.
- De esos, solo el **11%** recibió comunicaciones relevantes para su perfil.
- Alcance de la app: **2.1 millones de usuarios activos mensuales de la app**; el 61% de los fans asistentes tienen la app instalada.

### Inventario de comida de día de partido en 2025

| Tipo de partido | Inventario preparado / partido | Inventario vendido / partido | Tasa de desperdicio | Costo de desperdicio / partido |
|---|---|---|---|---|
| Derbi local | \$310,000 | \$291,400 | 6% | \$18,600 |
| Oponente Top-4 — fin de semana | \$295,000 | \$260,200 | 12% | \$34,800 |
| Media tabla — fin de semana | \$278,000 | \$231,000 | 17% | \$47,000 |
| Media tabla — entre semana | \$245,000 | \$176,400 | 28% | \$68,600 |
| Recién ascendido / Mitad inferior | \$220,000 | \$158,400 | 28% | \$61,600 |
| **Promedio 2025 en 31 partidos** | **~\$268,000** | **~\$210,000** | **19%** | **~\$58,000** |

_El inventario de A&B se adquiere en un ciclo semanal fijo y se ajusta manualmente por el equipo de operaciones según los benchmarks del año anterior. Operaciones del estadio ha señalado esto como un área prioritaria para 2026._

### Referencia financiera y de benchmark

- **Gasto promedio de día de partido por fan (2025):** \$25.90.
- **Asistencia total anual de día de partido (2025, nacional + Libertadores):** ~914,000 fans en 31 partidos de local.
- **Contexto de la industria:** Los recintos de la NFL generan \$65–\$82 por fan en gasto de día de partido. Los clubes de la MLS — el comparable demográfico más cercano — promedian \$42–\$55. Los estadios de la Premier League rondan los \$48–\$66. Los clubes brasileños de Série A sin programas de personalización promedian \$19–\$27 por fan, lo que coloca los \$25.90 de Bandeirantes hacia el extremo superior de su grupo de pares actual pero muy por debajo de los benchmarks internacionales. Los recintos que han desplegado personalización impulsada por IA y ofertas dirigidas dentro del estadio normalmente reportan aumentos de gasto por fan en el rango de un porcentaje de adolescentes altos a veintes altos, con las mayores ganancias realizadas en los primeros 12 meses de despliegue.
- **Tipo de beneficio esperado:** aumento del gasto de día de partido por fan, aplicado a los ~914,000 asistentes anuales de día de partido. La segmentación de 2025 ya muestra lo que es alcanzable dentro de la base de fans existente: los socios de alta asistencia gastan \$38.40 vs. un promedio mezclado de \$25.90 — cerrar incluso parte de esa brecha entre fans mediante una mejor segmentación representa la palanca de valor central. La reducción del desperdicio de comida (actualmente el 19% del inventario preparado) es un beneficio secundario si la demanda puede predecirse partido por partido.

***

## Constantes de referencia para los cálculos (línea base 2025)

| Constante | Valor | Fuente |
|---|---|---|
| Ingresos operativos totales (excl. transferencias) | \$206.8M | Resumen de ingresos anuales |
| Socios activos (31 dic 2025) | 75,000 | Flujo anual de membresías |
| Ingreso anual por miembro | \$541 | Economía de la membresía |
| Costo de adquirir un miembro | \$47 | Economía de la membresía |
| Partidos de local nacionales | 27 | Desempeño anual de boletería |
| Partidos de local totales (incl. Libertadores) | 31 | Desglose por tipo de partido 2025 |
| Capacidad del estadio 2025 | 38,000 asientos | Arena Ferradura |
| Precio prom. de entrada (2025, mezclado) | \$47.20 | Boletería trimestral |
| Asistencia prom. de día de partido (2025, todos los partidos) | ~29,500 | Desglose por tipo de partido 2025 |
| Total de asistentes de día de partido (2025) | ~914,000 | Suma de los 31 partidos |
| Gasto prom. de día de partido por fan | \$25.90 | Gasto anual de día de partido |
| Ingresos anuales de taquilla (nacional) | \$36.8M | Resumen de ingresos anuales |
| Ingresos anuales de A&B + mercancía de día de partido | ~\$23.7M (≈ \$20.2M de día de partido + ~\$3.5M de halo) | Gasto anual de día de partido |
| Crecimiento de ingresos 2024→2025 | +3.0% | Resumen de ingresos anuales |

***

## 📎 Referencia: La historia real que inspiró esta

> Este escenario ficticio se inspiró en un **caso de estudio real publicado** por Amazon Web Services Brasil, que presenta al **Clube Atlético Mineiro** ("O Galo"), un importante club de fútbol brasileño fundado en 1908 y con sede en Belo Horizonte, Minas Gerais.
>
> El caso real, publicado en mayo de 2026 y escrito por Leandro Evangelista (CIO, Atlético Mineiro), Vinicius Teodoro (CTO, Guidance) y Thamires Cunha (AWS), describe cómo el club construyó una plataforma unificada de datos e IA y desplegó modelos de machine learning que abarcan precios dinámicos de entradas, prevención de abandono de miembros e hiperpersonalización dentro del estadio.
>
> Todos los nombres, cifras, detalles del club y eventos narrativos de la historia de **Bandeirantes** anterior son **totalmente ficticios** y se crearon únicamente con el propósito de probar el marco BVIF. Los desafíos, la estructura de ingresos y los resultados del club ficticio están vagamente inspirados en — pero no representan con exactitud — el caso real de Atlético Mineiro.
>
> Caso original: _"Clube Atlético Mineiro: Como o Galo usou IA/ML para transformar dados em mais de R\$ 15 milhões com a AWS"_ — AWS Blog Brasil, mayo de 2026.

***

_Versión del documento: v2 | Actualizado: mayo de 2026 | Propósito: Pruebas del marco BVIF — Escenario B_
