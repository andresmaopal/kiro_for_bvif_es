# 03 — Predictive maintenance (with uncertainty quantification)

**Created:** June 2026  
**Last updated:** 2026-06-08  
**Based on:** `01-predictive-maintenance-ai-202604` (original point-estimate run)

---

## Purpose

This folder demonstrates the **enhanced BVIF process (v2) with Monte Carlo simulation and uncertainty quantification**. It re-runs stages 5, 6, and 7 of the Precision Furniture predictive maintenance scenario using the proposed methodology improvements.

## Relationship to the original scenario

Stages 00–04 are **not duplicated** here because they are identical to the original run:

| Stage | Location | Notes |
|-------|----------|-------|
| 00 – Session setup | See `01-predictive-maintenance-ai-202604/00-session-setup/` | Same initiative |
| 01 – Initiative definition | See `01-predictive-maintenance-ai-202604/01-initiative-definition/` | Same scope |
| 02 – Business value mapping | See `01-predictive-maintenance-ai-202604/02-business-value-mapping/` | Same value categories |
| 03 – Metrics identification | See `01-predictive-maintenance-ai-202604/03-metrics-identification/` | Same 7 metrics |
| 04 – Metrics adjustment | See `01-predictive-maintenance-ai-202604/04-metrics-adjustment/` | Same feasibility ratings |
| **05 – Data collection** | **This folder** | Enhanced: three-point ranges, adoption rate, counterfactual |
| **06 – Business value calculation** | **This folder** | Enhanced: Monte Carlo + levers of influence + Python script + JSON inputs |
| **07 – Final results** | **This folder** | Enhanced: P10/P50/P90 ranges, sensitivity, controllability |

## Files in this folder

| Path | Description |
|------|-------------|
| `bvif-state.md` | Stage completion tracker |
| `05-data-collection/data-collection-with-ranges.md` | Enhanced data collection — clearly separates v1 datapoints from v2 enhancements |
| `06-business-value-calculation/business-value-calculation-montecarlo.md` | Calculation methodology, per-metric formulas, sensitivity, levers of influence |
| `06-business-value-calculation/montecarlo_simulation.py` | Runnable Python script (reads from JSON) |
| `06-business-value-calculation/simulation_inputs.json` | Editable input variables — customer can modify and re-run |
| `07-final-results/final-results-with-uncertainty.md` | Executive summary with ranges, v1/v2 comparison, levers of influence |

## What changed from v1 (stages 5–7)

### Stage 5 — Data collection with ranges
- Same baseline data as v1 (current value, 8-quarter trend, financial impact, benchmark)
- **NEW:** Three-point improvement targets (pessimistic / most likely / optimistic)
- **NEW:** Adoption/realization rate (60% / 80% / 90%)
- **NEW:** Counterfactual baseline projection (where metric would be without AI)
- **NEW:** Clear separation of "Existing datapoints (same as v1)" vs. "New datapoints (v2 enhancement)"
- **NEW:** Directions on how each new datapoint was elicited from stakeholders

### Stage 6 — Monte Carlo business value calculation
- Runs **10,000 iterations** sampling from triangular distributions
- Subtracts counterfactual improvement before attributing value to AI
- Applies adoption rate as a multiplier
- Outputs **P10 / P50 / P90** instead of a single number
- **NEW:** Sensitivity analysis with correlation coefficients
- **NEW:** Levers of influence — which inputs are controllable and specific actions to narrow uncertainty
- **NEW:** `simulation_inputs.json` for customer re-execution without code changes
- Delivers runnable Python script

### Stage 7 — Final results with uncertainty
- Reports ranges instead of point estimate
- **NEW:** v1 vs. v2 comparison table
- **NEW:** Levers of influence section with controllability assessment
- **NEW:** Note on `simulation_inputs.json` for future re-runs
- Median is lower than v1 because it accounts for adoption < 100% and counterfactual drift

## Key finding

| Version | Output |
|---------|--------|
| v1 (point estimate) | \$9.36M/year |
| v2 (with uncertainty) | P10: \$6.2M · P50: \$7.5M · P90: \$8.9M |

The median drops ~20% because the enhanced model honestly accounts for:
1. Adoption won't be 100% from day one
2. Some improvement would have happened organically (counterfactual)

**Top sensitivity drivers:**
- M1 downtime reduction (r=0.748) — partially controllable via pilot data, sensor coverage
- Adoption rate (r=0.605) — highly controllable via change management, executive mandate

## How to re-run the simulation

```bash
cd 06-business-value-calculation/
# Edit simulation_inputs.json to update assumptions
python montecarlo_simulation.py
```

No code changes required — all parameters are externalized to JSON.

## Related documentation

- Process methodology v1: `docs/bvif_process/bvif_process_v1.md`
- Process methodology v2: `docs/bvif_process/bvif_process_v2_with_uncertainty.md`
- Consolidated feedback: `bvif-samples/0.workshop/feedback/CONSOLIDATED-FEEDBACK.md`
