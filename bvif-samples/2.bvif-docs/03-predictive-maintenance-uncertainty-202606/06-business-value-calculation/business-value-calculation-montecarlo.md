# Business value calculation (Monte Carlo)

## Methodology

Instead of a single deterministic calculation, this enhanced version uses **Monte Carlo simulation** to quantify uncertainty in the business value estimate.

**How it works:**
1. Each uncertain input (improvement target, adoption rate) is modeled as a **triangular distribution** with three points: pessimistic, most likely, optimistic
2. A **counterfactual baseline** (where the metric would land without the initiative) is subtracted from the improvement — so only AI-attributed value is counted
3. The simulation runs **10,000 iterations**, sampling randomly from all distributions simultaneously
4. The result is a **probability distribution** of outcomes, reported as P10 (conservative), P50 (median), P90 (optimistic)

**Key formula per iteration:**

```
Annual value = (Counterfactual baseline - Target) × Financial impact per unit × Units × Adoption rate × Annualization factor
```

Where `Target` and `Adoption rate` are each sampled from their respective triangular distributions.

---

## Per-metric formulas and ranges

### Metric 1: Recovered production capacity

```
Hours recovered/quarter = Counterfactual hours (347) × Reduction % [triangular: 30%, 50%, 65%]
Quarterly value = Hours recovered × \$9,971/hour
Annual value = Quarterly value × 4 × Adoption rate [triangular: 60%, 80%, 90%]
```

| Percentile | Annual value |
|------------|-------------|
| P10 (conservative) | \$3,984,804 |
| P50 (median) | \$5,132,292 |
| P90 (optimistic) | \$6,282,403 |

**Input sources:** Counterfactual hours from 8-quarter trend extrapolation. Reduction targets from WMIA benchmarks and peer case studies. Financial impact from scenario document "Production output loss rate during downtime." Adoption rate from VP Operations and Maintenance Director estimates.

---

### Metric 3: Maintenance cost reduction

```
Savings/unit = Counterfactual cost (\$12.50) × Reduction % [triangular: 15%, 20%, 30%]
Annual value = Savings/unit × 720,000 units/year × Adoption rate [triangular: 60%, 80%, 90%]
```

| Percentile | Annual value |
|------------|-------------|
| P10 (conservative) | \$1,187,668 |
| P50 (median) | \$1,471,167 |
| P90 (optimistic) | \$1,832,113 |

**Input sources:** Counterfactual cost from 2-year trend (\$10.85 → \$11.42 → \$12.00, projected to \$12.50). Reduction targets from peer case studies and Finance Director estimate. Production volume from scenario document.

---

### Metric 6: Delivery penalty avoidance

```
Late orders avoided/quarter = OTD improvement [triangular: 3pp, 5pp, 7pp] × 2,340 orders/quarter
Quarterly value = Late orders avoided × \$2,500/order
Annual value = Quarterly value × 4 × Adoption rate [triangular: 60%, 80%, 90%]
```

| Percentile | Annual value |
|------------|-------------|
| P10 (conservative) | \$681,024 |
| P50 (median) | \$892,997 |
| P90 (optimistic) | \$1,116,326 |

**Input sources:** Counterfactual OTD from 8-quarter trend (declining ~1pp/year). Improvement targets from CRO estimate and Metric 1 root-cause relationship (68%). Penalty amount from scenario document contractual terms.

---

## Combined results

| Percentile | Total annual business value |
|------------|---------------------------|
| **P10 (conservative)** | **\$6,220,856** |
| **P50 (median)** | **\$7,508,611** |
| **P90 (optimistic)** | **\$8,855,357** |

Mean: \$7,521,458 | Standard deviation: \$1,002,861

**80% confidence interval:** \$6.2M – \$8.9M annually

---

## Sensitivity analysis

Which inputs drive the most variance in total value?

| Input variable | Correlation with total | Impact |
|---------------|----------------------|--------|
| M1 downtime reduction % | +0.748 | **HIGH** |
| Adoption rate | +0.605 | **HIGH** |
| M3 cost reduction % | +0.185 | MEDIUM |
| M6 OTD improvement (pp) | +0.128 | LOW |

**Interpretation:** The downtime reduction target (Metric 1) and the adoption rate are by far the largest drivers of uncertainty. Reducing uncertainty in these two inputs — through pilot data, phased rollouts, or tighter benchmarking — would narrow the total value range most effectively.

---

## Levers of influence

Not all uncertain inputs are equally controllable. This section assesses which high-impact variables the organization can actively influence, and how.

### M1 downtime reduction (r=+0.748) — Partially controllable

**Influenced by:** Model quality (data completeness, algorithm selection), sensor coverage (capital investment), and maintenance crew response protocols (training, SOPs).

**Actions to narrow this uncertainty:**
- Better training data pipelines — more complete failure history improves model accuracy
- Incremental sensor deployment on highest-failure equipment (CNC routers, pneumatic presses)
- Standardized response procedures for predictive alerts
- Run a 3-month pilot on one production line to validate reduction assumptions before full commitment

### Adoption rate (r=+0.605) — Highly controllable

**Influenced by:** Change management rigor, end-user training quality, leadership sponsorship, and workflow integration.

**Actions to increase adoption:**
- Executive mandate from plant manager (clear expectation that crews follow predictive alerts)
- Phased rollout with local champions per shift
- Automated alerts integrated into existing CMMS (not a separate system)
- Regular feedback sessions with maintenance crews to surface friction points
- Incentive alignment (crew KPIs tied to predictive compliance rate)

### M3 cost reduction (r=+0.185) — Moderately controllable

**Influenced by:** Parts procurement strategy, contractor dependency, preventive schedule optimization.

**Actions:** Negotiate volume parts contracts, reduce external contractor reliance through skill-building, optimize PM intervals based on condition data rather than fixed schedules.

### M6 OTD improvement (r=+0.128) — Less controllable

**Influenced by:** Production scheduling decisions, customer order mix, and non-maintenance causes of late delivery (32% of cases).

**Guidance:** Monitor but don't over-optimize for this input. OTD improvement is a downstream consequence of Metric 1 improvement — focus effort upstream on downtime reduction and adoption.

---

## Double-counting verification

Same as original analysis — no overlap between the three value-producing metrics:
- Metric 1 (recovered capacity) captures lost contribution margin from downtime
- Metric 3 (maintenance cost) captures direct cost reduction in maintenance operations
- Metric 6 (penalty avoidance) captures contractual penalty savings from improved delivery

These represent distinct value streams. All three are additive.

---

## Deliverables

| File | Purpose |
|------|---------|
| `montecarlo_simulation.py` | Runnable Python script — executes the simulation |
| `simulation_inputs.json` | Editable input variables — change assumptions and re-run without modifying code |

**To re-run with updated assumptions:**
1. Edit `simulation_inputs.json` (change improvement targets, adoption rates, or counterfactual projections)
2. Run: `python montecarlo_simulation.py`
3. Review updated P10/P50/P90 results
