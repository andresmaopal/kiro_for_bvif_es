"""
BVIF Monte Carlo simulation — Predictive maintenance (Precision Furniture Inc.)

Enhanced business value calculation with uncertainty quantification.
Reads inputs from simulation_inputs.json for easy re-execution with updated assumptions.

Usage:
    python montecarlo_simulation.py

Requirements:
    numpy (pip install numpy)

Inputs:
    simulation_inputs.json (same directory) — edit this file to update assumptions
"""

import json
import os
import numpy as np


# ─────────────────────────────────────────────────────────────────────────────
# Load inputs from JSON
# ─────────────────────────────────────────────────────────────────────────────

script_dir = os.path.dirname(os.path.abspath(__file__))
inputs_path = os.path.join(script_dir, "simulation_inputs.json")

with open(inputs_path, "r") as f:
    config = json.load(f)

ITERATIONS = config["simulation_config"]["iterations"]
SEED = config["simulation_config"]["random_seed"]
np.random.seed(SEED)

# Adoption rate (shared)
adoption_cfg = config["adoption_rate"]
ADOPTION_LOW = adoption_cfg["pessimistic"]
ADOPTION_MODE = adoption_cfg["most_likely"]
ADOPTION_HIGH = adoption_cfg["optimistic"]

# Metrics
metrics_cfg = config["metrics"]
m1_cfg = next(m for m in metrics_cfg if m["id"] == "M1")
m3_cfg = next(m for m in metrics_cfg if m["id"] == "M3")
m6_cfg = next(m for m in metrics_cfg if m["id"] == "M6")


# ─────────────────────────────────────────────────────────────────────────────
# Monte Carlo simulation
# ─────────────────────────────────────────────────────────────────────────────

def triangular_sample(low, mode, high, n=ITERATIONS):
    """Sample from triangular distribution."""
    return np.random.triangular(low, mode, high, n)


# Sample adoption rate (shared across metrics)
adoption = triangular_sample(ADOPTION_LOW, ADOPTION_MODE, ADOPTION_HIGH)

# --- Metric 1: Recovered production capacity ---
m1_reduction = triangular_sample(
    m1_cfg["improvement_target"]["pessimistic"],
    m1_cfg["improvement_target"]["most_likely"],
    m1_cfg["improvement_target"]["optimistic"]
)
m1_hours_recovered = m1_cfg["counterfactual_hours_per_quarter"] * m1_reduction
m1_quarterly_value = m1_hours_recovered * m1_cfg["financial_impact_per_hour"]
m1_annual_value = m1_quarterly_value * m1_cfg["annualization_factor"] * adoption

# --- Metric 3: Maintenance cost reduction ---
m3_reduction = triangular_sample(
    m3_cfg["improvement_target"]["pessimistic"],
    m3_cfg["improvement_target"]["most_likely"],
    m3_cfg["improvement_target"]["optimistic"]
)
m3_savings_per_unit = m3_cfg["counterfactual_cost_per_unit"] * m3_reduction
m3_annual_value = m3_savings_per_unit * m3_cfg["annual_units"] * adoption

# --- Metric 6: Delivery penalty avoidance ---
m6_improvement = triangular_sample(
    m6_cfg["improvement_target"]["pessimistic"],
    m6_cfg["improvement_target"]["most_likely"],
    m6_cfg["improvement_target"]["optimistic"]
)
m6_late_orders_avoided = m6_improvement * m6_cfg["orders_per_quarter"]
m6_quarterly_value = m6_late_orders_avoided * m6_cfg["penalty_per_late_order"]
m6_annual_value = m6_quarterly_value * m6_cfg["annualization_factor"] * adoption

# Total
total_annual_value = m1_annual_value + m3_annual_value + m6_annual_value


# ─────────────────────────────────────────────────────────────────────────────
# Results
# ─────────────────────────────────────────────────────────────────────────────

def percentiles(arr):
    """Return P10, P50, P90."""
    return np.percentile(arr, 10), np.percentile(arr, 50), np.percentile(arr, 90)


print("=" * 72)
print("BVIF MONTE CARLO SIMULATION — Predictive Maintenance")
print("=" * 72)
print(f"Initiative: {config['metadata']['initiative']}")
print(f"Iterations: {ITERATIONS:,}")
print(f"Inputs: {inputs_path}")
print()

print("─" * 72)
print("PER-METRIC RESULTS (annualized)")
print("─" * 72)

metric_results = [
    ("Metric 1: Recovered production capacity", m1_annual_value),
    ("Metric 3: Maintenance cost reduction", m3_annual_value),
    ("Metric 6: Delivery penalty avoidance", m6_annual_value),
]

for name, values in metric_results:
    p10, p50, p90 = percentiles(values)
    print(f"\n  {name}")
    print(f"    P10 (conservative):  ${p10:,.0f}")
    print(f"    P50 (median):        ${p50:,.0f}")
    print(f"    P90 (optimistic):    ${p90:,.0f}")

print()
print("─" * 72)
print("TOTAL ANNUAL BUSINESS VALUE")
print("─" * 72)

p10_total, p50_total, p90_total = percentiles(total_annual_value)
print(f"\n  P10 (conservative):  ${p10_total:,.0f}")
print(f"  P50 (median):        ${p50_total:,.0f}")
print(f"  P90 (optimistic):    ${p90_total:,.0f}")
print(f"\n  Mean:                ${np.mean(total_annual_value):,.0f}")
print(f"  Std deviation:       ${np.std(total_annual_value):,.0f}")
print(f"\n  80% confidence interval: ${p10_total:,.0f} – ${p90_total:,.0f}")

print()
print("─" * 72)
print("COMPARISON WITH ORIGINAL POINT ESTIMATE (v1)")
print("─" * 72)
original_point_estimate = 9_359_688
print(f"\n  Original v1 (deterministic):  ${original_point_estimate:,.0f}")
print(f"  Enhanced v2 P50 (median):     ${p50_total:,.0f}")
print(f"  Difference:                   ${p50_total - original_point_estimate:+,.0f}")
print(f"\n  The median is lower because the enhanced version accounts for:")
print(f"    1. Adoption rate < 100% (avg ~77%)")
print(f"    2. Counterfactual baseline drift (metrics would worsen without AI)")
print(f"    3. Three-point estimates center slightly below original targets")


# ─────────────────────────────────────────────────────────────────────────────
# Sensitivity analysis
# ─────────────────────────────────────────────────────────────────────────────

print()
print("─" * 72)
print("SENSITIVITY ANALYSIS")
print("─" * 72)
print("\n  Which inputs drive the most variance in total value?\n")

inputs_dict = {
    "M1 downtime reduction %": m1_reduction,
    "Adoption rate": adoption,
    "M3 cost reduction %": m3_reduction,
    "M6 OTD improvement (pp)": m6_improvement,
}

correlations = {}
for name, values in inputs_dict.items():
    corr = np.corrcoef(values, total_annual_value)[0, 1]
    correlations[name] = corr

sorted_inputs = sorted(correlations.items(), key=lambda x: abs(x[1]), reverse=True)

print(f"  {'Input variable':<30} {'Correlation':>12} {'Impact':>8}")
print(f"  {'─' * 30} {'─' * 12} {'─' * 8}")
for name, corr in sorted_inputs:
    impact = "HIGH" if abs(corr) > 0.5 else "MEDIUM" if abs(corr) > 0.3 else "LOW"
    print(f"  {name:<30} {corr:>+12.3f} {impact:>8}")


# ─────────────────────────────────────────────────────────────────────────────
# Levers of influence
# ─────────────────────────────────────────────────────────────────────────────

print()
print("─" * 72)
print("LEVERS OF INFLUENCE")
print("─" * 72)
print("""
  Which inputs can the organization actually influence?

  ┌─────────────────────────────────────────────────────────────────────┐
  │ M1 downtime reduction (r=+{:.3f})                                  │
  │ Controllability: PARTIALLY CONTROLLABLE                             │
  │                                                                     │
  │ Influenced by: model quality (data completeness, algorithm          │
  │ selection), sensor coverage (capital investment), maintenance crew   │
  │ response protocols (training, SOPs).                                │
  │                                                                     │
  │ Actions to narrow uncertainty:                                      │
  │   • Better training data pipelines (more complete failure history)  │
  │   • Incremental sensor deployment on highest-failure equipment      │
  │   • Standardized response procedures for predictive alerts          │
  │   • 3-month pilot on one line to validate reduction assumptions     │
  └─────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────┐
  │ Adoption rate (r=+{:.3f})                                          │
  │ Controllability: HIGHLY CONTROLLABLE                                │
  │                                                                     │
  │ Influenced by: change management rigor, end-user training quality,  │
  │ leadership sponsorship, and workflow integration.                    │
  │                                                                     │
  │ Actions to increase adoption:                                       │
  │   • Executive mandate from plant manager                            │
  │   • Phased rollout with local champions per shift                   │
  │   • Automated alerts integrated into existing CMMS                  │
  │   • Regular feedback sessions with maintenance crews                │
  │   • Incentive alignment (crew KPIs tied to predictive compliance)   │
  └─────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────┐
  │ M3 cost reduction (r=+{:.3f})                                      │
  │ Controllability: MODERATELY CONTROLLABLE                            │
  │                                                                     │
  │ Influenced by: parts procurement strategy, contractor dependency,   │
  │ preventive schedule optimization.                                   │
  │                                                                     │
  │ Actions: Negotiate parts contracts, reduce contractor reliance,     │
  │ optimize PM intervals based on condition data.                      │
  └─────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────┐
  │ M6 OTD improvement (r=+{:.3f})                                     │
  │ Controllability: LESS CONTROLLABLE (downstream effect)              │
  │                                                                     │
  │ Influenced by: production scheduling decisions, customer order mix, │
  │ and other non-maintenance causes of late delivery (32% of cases).   │
  │                                                                     │
  │ Actions: Monitor but don't over-optimize — this is a secondary      │
  │ benefit that follows from Metric 1 improvement.                     │
  └─────────────────────────────────────────────────────────────────────┘
""".format(
    correlations.get("M1 downtime reduction %", 0),
    correlations.get("Adoption rate", 0),
    correlations.get("M3 cost reduction %", 0),
    correlations.get("M6 OTD improvement (pp)", 0)
))

print("─" * 72)
print("END OF SIMULATION")
print("─" * 72)
print(f"\n  To re-run with different assumptions, edit simulation_inputs.json")
print(f"  and run: python montecarlo_simulation.py")
