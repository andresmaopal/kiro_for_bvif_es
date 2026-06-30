# BVIF process v1

**Date:** 2026-06-08  
**Version:** v1 (current)

---

## Overview

BVIF is a 7-stage process that transforms a plain-language AI initiative description into a quantified, auditable annualized business value estimate. Each stage builds on the previous one, with stakeholder approval checkpoints between stages. The process is guided by AI (Kiro IDE) and produces a complete audit trail.

**Typical duration:** 2–4 weeks per initiative.

---

## Stage 1: Initiative definition

**Purpose:** Establish what the AI initiative is and confirm scope with the stakeholder.

- Collect a plain-language description of the initiative
- Refine scope: what's included, what's excluded, who benefits
- Confirm the refined definition with the stakeholder before proceeding

**Output:** A clear, agreed-upon initiative definition document.

---

## Stage 2: Business value mapping

**Purpose:** Identify which value categories the initiative could impact.

Map the initiative to one or more standard value categories (aligned with AWS CAF):

| Category | Examples |
|----------|----------|
| Grow Revenue | Expanding addressable markets, new AI-enabled revenue streams, customer acquisition/retention, accelerating innovation cycles |
| Increase Operational Efficiency | Automating repetitive tasks, optimizing resource allocation, reducing costs through process optimization, improving productivity |
| Reduce Business Risk | Enhancing compliance, improving fraud detection, strengthening business continuity, anomaly detection |
| Improve ESG Performance | Optimizing energy consumption, supply chain sustainability, workplace safety, automated compliance monitoring |

**Output:** A mapping of the initiative to relevant value categories with brief rationale.

---

## Stage 3: Metrics identification

**Purpose:** For each mapped value category, identify specific measurable metrics that would demonstrate value.

- Propose candidate metrics for each category
- Define each metric precisely (formula, units, measurement frequency)
- Confirm metrics with the stakeholder

**Output:** A list of candidate metrics with definitions, grouped by value category.

---

## Stage 4: Metrics adjustment

**Purpose:** Assess the feasibility of measuring each candidate metric and filter accordingly.

Assign a feasibility rating to each metric:

| Rating | Meaning | Action |
|--------|---------|--------|
| F1 | Data readily available | Keep — proceed to data collection |
| F2 | Obtainable with reasonable effort | Keep — note the effort required |
| F3 | Not feasible to measure | Drop or find a proxy metric |

**Decision rule:** If a metric is rated F3 with no viable proxy, it is excluded from the calculation. This prevents computing value against metrics nobody can actually track.

**Output:** A refined list of feasible metrics, with F3 items removed or replaced by proxies.

---

## Stage 5: Data collection

**Purpose:** Gather the quantitative inputs needed to calculate business value for each feasible metric.

For each metric, collect:

| Field | Description |
|-------|-------------|
| Current baseline | Most recent measured value (e.g., "2.8% unplanned downtime") |
| Historical trend | 8 quarters of data to establish trajectory |
| Financial impact per unit | Dollar value per unit of metric change (e.g., "\$9,971 per hour of downtime") |
| Industry benchmark | Best-in-class or peer performance for context |
| Improvement target | Expected improvement with the AI initiative (single value) |
| Target rationale | Why this target is realistic (peer studies, pilot data, expert judgment) |

**Output:** A completed data collection table for each metric, with sources documented.

---

## Stage 6: Business value calculation

**Purpose:** Calculate the annualized business value for each metric and produce a total.

### Key terms

- **Annualized value:** The estimated yearly benefit if the initiative performs as expected at steady state. This assumes the improvement is sustained for a full year at the target level.
- **Baseline gap:** The difference between current performance and the improvement target (e.g., reducing downtime from 2.8% to 1.4% = 1.4 percentage points of improvement, or 162 hours per quarter).
- **Improvement target:** The expected performance after AI implementation (collected in stage 5).
- **Financial impact per unit:** The dollar value associated with each unit of metric change (e.g., \$9,971 contribution margin lost per hour of downtime).
- **Annualization factor:** The multiplier to convert the measurement period to a yearly figure (×4 for quarterly data, ×12 for monthly data, ×1 for annual data).

### Formula

```
Annualized value = Baseline gap × Financial impact per unit × Annualization factor
```

### Additional checks

- **Double-counting verification:** Ensure metrics measuring the same underlying phenomenon are not both assigned financial value. Mark overlapping metrics as "Captured in Metric N" and assign value to only one.
- **Source fidelity:** Each number in the calculation must trace back to a documented source (scenario document section, stakeholder statement, industry report).

### Important limitation

This is a **point estimate** — it produces a single number (e.g., "\$9.36M/year"). It does not account for:
- Uncertainty in the improvement target
- Adoption or realization rates (implicitly assumes 100%)
- Counterfactual baseline drift (what would happen without the initiative)

**Output:** A value calculation table showing per-metric annualized value, double-counting checks, and a total.

---

## Stage 7: Final results

**Purpose:** Produce a consolidated, auditable report with the total business value estimate.

The final report includes:

- Executive summary with total annualized business value
- Per-metric breakdown table (metric, category, annualized value, calculation explanation)
- Double-counting verification statement
- Non-financial (quantified) business value (operational improvements not monetized)
- Strategic value beyond the numbers (competitive positioning, risk of inaction)
- Data provenance for every figure

**Output:** A complete final results document suitable for stakeholder review and investment decisions.

---

## Design principles

- **Approval gates:** The agent never advances without explicit stakeholder approval
- **Audit trail:** Every interaction is captured in sequentially numbered files
- **Feasibility discipline:** F3 metrics are excluded — no value computed against unmeasurable metrics
- **Double-counting discipline:** Overlapping metrics are flagged and deduplicated
- **Scope boundary:** BVIF quantifies the value side only — it does not estimate costs, calculate ROI, or produce NPV

---

> **Note:** See `bvif_process_v2_with_uncertainty.md` for the enhanced version incorporating Monte Carlo simulation and uncertainty quantification.
