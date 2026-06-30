# Data collection (enhanced with uncertainty ranges)

This document collects the same data as the standard BVIF process (v1), plus three-point estimates for improvement targets, adoption rates, and counterfactual baselines. Only the three value-producing metrics are shown (metrics 2, 4, 5, 7 serve as operational validators and are excluded from financial calculation).

---

## Metric 1: Unplanned downtime rate (%)

- **Category:** Increase operational efficiency
- **Definition:** (Unplanned downtime hours / Total available hours) × 100

#### Existing datapoints (same as v1)

| Field | Value | Source |
|-------|-------|--------|
| Current baseline (Q4 2025) | 2.8% (324 hours / 11,520 total) | Scenario document: "Historical performance: Unplanned downtime rate" |
| Historical trend (8 quarters) | 2.7% → 2.5% → 2.6% → 2.8% → 3.0% → 2.9% → 2.8% → 2.8% | Scenario document: same section |
| Financial impact per hour | \$9,971 lost contribution margin (86.7 units × \$250 revenue × 46% margin) | Scenario document: "Production output loss rate during downtime" |
| Industry benchmark | <1.5% (Woodworking Machinery Industry Association) | Industry report |

#### New datapoints (v2 enhancement)

**Three-point improvement target**

*How collected:* Asked VP Operations: "What's the worst realistic outcome from predictive maintenance? What do you expect? What's the best case?" Cross-referenced with WMIA peer case studies.

| Estimate | Value | Rationale | Source |
|----------|-------|-----------|--------|
| **Pessimistic (P10)** | 30% reduction (2.8% → 1.96%) | Minimum expected from basic condition monitoring; accounts for integration challenges | Stakeholder estimate (VP Operations) |
| **Most likely (P50)** | 50% reduction (2.8% → 1.4%) | Consistent with peer case studies for similar manufacturers at 12-18 months | Industry benchmark (WMIA case studies) |
| **Optimistic (P90)** | 65% reduction (2.8% → 0.98%) | Best-case with full sensor coverage and mature ML models | Best-in-class peer data |

**Adoption/realization rate**

*How collected:* Asked Maintenance Director: "What percentage of your crews do you expect will actually follow the new predictive maintenance recommendations within the first year?" Triangulated with VP Operations and change management assessment.

| Estimate | Value | Rationale | Source |
|----------|-------|-----------|--------|
| **Pessimistic** | 60% | Some maintenance crews resist changing established schedules; partial sensor deployment | Stakeholder estimate (Maintenance Director) |
| **Most likely** | 80% | Phased rollout with training; most crews adopt within 6 months | Stakeholder estimate (VP Operations) |
| **Optimistic** | 90% | Strong executive mandate; incentive alignment; proven early wins build trust | Best-case assumption |

**Counterfactual baseline (12-month projection without AI)**

*How collected:* Extrapolated from 8-quarter trend showing consistent deterioration. Asked VP Operations: "If you did nothing, where would downtime be in 12 months?"

| Field | Value | Rationale |
|-------|-------|-----------|
| Projected baseline without initiative | 3.0% (trending up ~0.1%/year) | Historical trend shows consistent increase from 2.5% to 2.8% over 2 years as equipment ages and production volume grows 18% |

**Counterfactual adjustment:** The AI initiative's value should be measured against the counterfactual (3.0%), not the current baseline (2.8%). This means the effective improvement is from 3.0% → target, not 2.8% → target.

---

## Metric 3: Maintenance cost per unit produced

- **Category:** Increase operational efficiency
- **Definition:** Total maintenance costs (planned + unplanned) / Total units produced

#### Existing datapoints (same as v1)

| Field | Value | Source |
|-------|-------|--------|
| Current baseline (2025) | \$12.00/unit (\$8,640,000 / 720,000 units) | Scenario document: "Maintenance cost per production unit" |
| Historical trend | \$10.85 (2023) → \$11.42 (2024) → \$12.00 (2025) | Scenario document: same section |
| Cost breakdown | Preventive labor 37.5%, Emergency reactive 33.3%, Parts 22.2%, Contractors 7.0% | Scenario document: same section |
| Industry benchmark | \$9.50–\$10.50/unit | Comparable furniture manufacturers |

#### New datapoints (v2 enhancement)

**Three-point improvement target**

*How collected:* Asked Finance Director: "Given a shift to predictive maintenance, what's the minimum cost reduction you'd expect? What's realistic? What's best case?" Validated against peer case study data from similar implementations.

| Estimate | Value | Rationale | Source |
|----------|-------|-----------|--------|
| **Pessimistic (P10)** | 15% reduction (\$12.00 → \$10.20, saving \$1.80/unit) | Minimum shift from reactive to planned; some emergency costs persist | Stakeholder estimate (Finance Director) |
| **Most likely (P50)** | 20% reduction (\$12.00 → \$9.60, saving \$2.40/unit) | Consistent with peer case studies for predictive maintenance adoption | Industry benchmark (peer case studies) |
| **Optimistic (P90)** | 30% reduction (\$12.00 → \$8.40, saving \$3.60/unit) | Full elimination of emergency reactive costs; approaches benchmark | Best-in-class peer data |

**Adoption/realization rate**

*How collected:* Same methodology as Metric 1 — maintenance cost savings depend on the same adoption of predictive signals.

| Estimate | Value | Rationale | Source |
|----------|-------|-----------|--------|
| **Pessimistic** | 60% | Partial implementation; some equipment not suitable for sensors | Stakeholder estimate (Maintenance Director) |
| **Most likely** | 80% | Full sensor deployment on critical equipment (80% of maintenance cost) | Stakeholder estimate (VP Operations) |
| **Optimistic** | 90% | Complete coverage including secondary equipment | Best-case assumption |

**Counterfactual baseline (12-month projection without AI)**

*How collected:* Extrapolated from 2-year cost trend (10.6% increase). Asked Finance Director: "What would maintenance cost per unit be next year if you continued the current approach?"

| Field | Value | Rationale |
|-------|-------|-----------|
| Projected baseline without initiative | \$12.50/unit (trending up ~\$0.50/year) | 10.6% increase over 2 years driven by aging equipment and growing emergency repair costs |

**Counterfactual adjustment:** Effective improvement measured from \$12.50 → target, not \$12.00 → target.

---

## Metric 6: On-time delivery rate (%)

- **Category:** Grow revenue (penalty avoidance)
- **Definition:** (Orders delivered on-time / Total orders) × 100

#### Existing datapoints (same as v1)

| Field | Value | Source |
|-------|-------|--------|
| Current baseline (Q4 2025) | 90.0% (2,106 on-time / 2,340 total) | Scenario document: "On-time delivery (OTD) rate" |
| Historical trend (8 quarters) | 92.4% → 91.8% → 91.2% → 90.6% → 89.8% → 90.2% → 90.0% → 90.0% | Scenario document: same section |
| Root cause | 68% of late deliveries attributable to unplanned production downtime | Scenario document: root cause analysis |
| Contractual penalty | \$2,500 per late order | Scenario document: same section |
| Total orders per quarter | 2,340 | Scenario document: same section |

#### New datapoints (v2 enhancement)

**Three-point improvement target**

*How collected:* Asked CRO: "If we reduce unplanned downtime significantly, how much do you expect on-time delivery to improve — worst case, expected case, best case?" Validated against the causal relationship (68% of late deliveries from downtime).

| Estimate | Value | Rationale | Source |
|----------|-------|-----------|--------|
| **Pessimistic (P10)** | 3 percentage point improvement (90% → 93%) | Only partial downtime reduction flows through to delivery; other causes remain | Stakeholder estimate (CRO) |
| **Most likely (P50)** | 5 percentage point improvement (90% → 95%) | Consistent with 50% downtime reduction × 68% root cause attribution | Calculated from Metric 1 relationship |
| **Optimistic (P90)** | 7 percentage point improvement (90% → 97%) | Full downtime reduction plus scheduling improvements from better predictability | Best-case assumption |

**Adoption/realization rate**

*How collected:* Asked Supply Chain Director: "If maintenance improves uptime, how quickly can your scheduling team translate that into better delivery performance?"

| Estimate | Value | Rationale | Source |
|----------|-------|-----------|--------|
| **Pessimistic** | 60% | Delivery improvement depends on production scheduling also adapting | Stakeholder estimate (Supply Chain Director) |
| **Most likely** | 80% | Scheduling team committed to leveraging uptime improvements | Stakeholder estimate (VP Operations) |
| **Optimistic** | 90% | Full integration of predictive maintenance signals into production scheduling | Best-case assumption |

**Counterfactual baseline (12-month projection without AI)**

*How collected:* Extrapolated from 8-quarter trend showing consistent decline. Asked CRO: "If downtime continues to worsen, where does OTD end up in 12 months?"

| Field | Value | Rationale |
|-------|-------|-----------|
| Projected baseline without initiative | 89.0% (trending down ~1 percentage point/year) | 2.4 percentage point decline from 92.4% to 90.0% over 2 years; equipment aging continues |

**Counterfactual adjustment:** Effective improvement measured from 89.0% → target, not 90.0% → target.

---

## Summary of inputs for Monte Carlo simulation

| Input | Metric 1 (Downtime) | Metric 3 (Maint. cost) | Metric 6 (OTD) |
|-------|---------------------|------------------------|-----------------|
| Counterfactual baseline | 3.0% | \$12.50/unit | 89.0% |
| Target (pessimistic) | 1.96% | \$10.20/unit | 93.0% |
| Target (most likely) | 1.40% | \$9.60/unit | 95.0% |
| Target (optimistic) | 0.98% | \$8.40/unit | 97.0% |
| Financial impact/unit | \$9,971/hr downtime | 720,000 units/year | \$2,500/late order, 2,340 orders/qtr |
| Adoption rate (P/ML/O) | 60% / 80% / 90% | 60% / 80% / 90% | 60% / 80% / 90% |

All inputs are stored in `06-business-value-calculation/simulation_inputs.json` for easy re-execution with updated assumptions.
