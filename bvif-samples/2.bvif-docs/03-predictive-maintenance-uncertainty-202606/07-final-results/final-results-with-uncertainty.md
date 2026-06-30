# Precision Furniture Inc. — Predictive maintenance using AI: business value summary (with uncertainty)

## Executive summary

Precision Furniture Inc. proposes implementing an AI-driven predictive maintenance program across 450 pieces of critical production equipment. This enhanced BVIF assessment quantifies the initiative's value using **Monte Carlo simulation** to provide probability-weighted ranges rather than a single point estimate.

### Estimated annual business value

| Confidence level | Value |
|-----------------|-------|
| **P10 (conservative — 90% chance of exceeding)** | **\$6.2M/year** |
| **P50 (median — most likely outcome)** | **\$7.5M/year** |
| **P90 (optimistic — 10% chance of exceeding)** | **\$8.9M/year** |

**80% confidence interval: \$6.2M – \$8.9M annually**

This estimate accounts for:
- Uncertainty in improvement targets (three-point estimates from stakeholders and benchmarks)
- Realistic adoption rates (60–90%, not the implicit 100% of a deterministic model)
- Counterfactual baseline drift (metrics would have worsened without intervention)

---

## Comparison: v1 point estimate vs. v2 uncertainty model

| Aspect | v1 (deterministic) | v2 (Monte Carlo) |
|--------|-------------------|-----------------|
| **Total value** | \$9.36M/year | P10 \$6.2M – P50 \$7.5M – P90 \$8.9M |
| **Adoption rate assumed** | 100% (implicit) | 60–90% (explicit, triangular) |
| **Counterfactual adjustment** | None (compared to current baseline) | Yes (compared to projected baseline without AI) |
| **Improvement targets** | Single estimate | Three-point: pessimistic/likely/optimistic |
| **Uncertainty visibility** | None — single number | Full range with sensitivity analysis |
| **Levers of influence** | Not assessed | Identified: which inputs are controllable and how |
| **Decision confidence** | Lower — easy to challenge | Higher — assumptions explicit and testable |

**Why is the median (\$7.5M) lower than the original (\$9.36M)?**
1. Adoption rate averages ~77% instead of the implicit 100%
2. Counterfactual adjustment: part of the "improvement" is preventing deterioration that would have happened anyway
3. Three-point estimates center slightly below the original single-point targets

---

## Per-metric breakdown

### Metric 1: Recovered production capacity

| Percentile | Annual value |
|------------|-------------|
| P10 | \$3,984,804 |
| P50 | \$5,132,292 |
| P90 | \$6,282,403 |

- **Value driver:** Reducing unplanned downtime hours recovers lost production capacity
- **Counterfactual:** Without AI, downtime would trend from 2.8% to ~3.0% (aging equipment + volume growth)
- **Improvement range:** 30–65% reduction from counterfactual (347 hours/quarter)
- **Financial basis:** \$9,971 lost contribution margin per downtime hour (86.7 units × \$250 × 46% margin)
- **Data provenance:** Baseline from scenario doc "Historical performance: Unplanned downtime rate"; financial impact from "Production output loss rate during downtime"; targets from WMIA benchmarks and peer case studies

### Metric 3: Maintenance cost reduction

| Percentile | Annual value |
|------------|-------------|
| P10 | \$1,187,668 |
| P50 | \$1,471,167 |
| P90 | \$1,832,113 |

- **Value driver:** Shifting from reactive to proactive maintenance reduces cost per unit
- **Counterfactual:** Without AI, cost trends from \$12.00 to ~\$12.50/unit (10.6% increase over prior 2 years)
- **Improvement range:** 15–30% reduction from counterfactual cost
- **Financial basis:** 720,000 units produced annually
- **Data provenance:** Baseline from scenario doc "Maintenance cost per production unit"; cost breakdown showing \$2.88M in emergency reactive costs; targets from peer case studies and Finance Director estimate

### Metric 6: Delivery penalty avoidance

| Percentile | Annual value |
|------------|-------------|
| P10 | \$681,024 |
| P50 | \$892,997 |
| P90 | \$1,116,326 |

- **Value driver:** Improved equipment uptime enables reliable production schedules and on-time delivery
- **Counterfactual:** Without AI, OTD declines from 90.0% to ~89.0% (2.4pp decline over prior 2 years)
- **Improvement range:** 3–7 percentage points improvement from counterfactual
- **Financial basis:** \$2,500 contractual penalty per late order × 2,340 orders/quarter
- **Data provenance:** Baseline from scenario doc "On-time delivery (OTD) rate"; root cause (68% from downtime); penalty from contractual terms; targets from CRO estimate and Metric 1 causal relationship

---

## Sensitivity analysis

| Input variable | Correlation with total value | Impact level |
|---------------|------------------------------|-------------|
| M1 downtime reduction % | +0.748 | **HIGH** |
| Adoption rate | +0.605 | **HIGH** |
| M3 cost reduction % | +0.185 | MEDIUM |
| M6 OTD improvement (pp) | +0.128 | LOW |

---

## Levers of influence

Which high-impact inputs can the organization actively influence?

| Input | r value | Controllability | Key actions |
|-------|---------|-----------------|-------------|
| **M1 downtime reduction** | +0.748 | Partially controllable | Better training data pipelines, incremental sensor deployment, standardized response procedures, 3-month pilot to validate |
| **Adoption rate** | +0.605 | Highly controllable | Executive mandate, phased rollout with champions, CMMS-integrated alerts, crew feedback sessions, incentive alignment |
| **M3 cost reduction** | +0.185 | Moderately controllable | Volume parts contracts, reduce contractor reliance, condition-based PM intervals |
| **M6 OTD improvement** | +0.128 | Less controllable | Downstream effect of M1; monitor but focus effort upstream |

**Key insight:** The two largest drivers of uncertainty (downtime reduction and adoption rate) are both within the organization's ability to influence. This means the value range can be narrowed through deliberate action — the estimate is not purely subject to external factors.

---

## Non-financial value (unchanged from original)

| Metric | Current | Target | Improvement |
|--------|---------|--------|-------------|
| MTBF | 4,114 hours | 5,554 hours | 35% improvement in equipment reliability |
| Unplanned work order rate | 15.0% | 8.0% | 47% reduction in reactive events |
| Planned/unplanned ratio | 5.67:1 | 11.5:1 | Fundamental shift to proactive maintenance |
| Production capacity utilization | 84.4% | 92.2% | 7.8pp increase |

---

## Strategic value (unchanged from original)

- **Customer relationship protection:** \$2.5M in contract value at risk due to delivery concerns
- **Competitive positioning:** Competitors offering 16–17 day lead times vs. Precision Furniture's 21-day promise
- **Operational resilience:** Current maintenance model unsustainable as equipment ages and volume grows
- **Data foundation:** Sensor infrastructure enables future AI use cases (quality prediction, energy optimization)

---

## Methodology note

This assessment uses an enhanced version of the AI Business Value Identification Framework (AI-BVIF) that incorporates:

1. **Three-point estimates** for all uncertain inputs (pessimistic/most likely/optimistic)
2. **Monte Carlo simulation** (10,000 iterations with triangular distributions) replacing deterministic calculation
3. **Adoption/realization rate** as an explicit multiplier (not assumed to be 100%)
4. **Counterfactual baseline projection** to ensure only AI-attributed value is counted
5. **Levers of influence analysis** identifying which inputs are controllable and how

**Reproducibility:** The simulation is delivered as a runnable Python script (`montecarlo_simulation.py`) reading from an editable JSON configuration (`simulation_inputs.json`). The customer can re-run the simulation at any time with updated assumptions — no code changes required.

**Limitations:** This remains a lightweight validation — a grounded estimate to inform prioritization, not a full financial model. It does not address implementation costs, timeline, or organizational readiness. It is a structured first step toward a complete business case.

---

*Generated: 2026-06-08 | Framework: AI-BVIF v2 (enhanced with uncertainty quantification)*
