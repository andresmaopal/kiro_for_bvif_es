# Stage 3 / Task 2 — Metrics Feasibility Approval

## What you're approving
A feasibility label for each metric, reflecting how practical it is to measure **today**:

- **Feasibility 1** — Metric is already tracked. Ready to use out of the box.
- **Feasibility 2** — The underlying data exists, but the metric itself isn't calculated yet. Feasible with some setup.
- **Feasibility 3** — No data exists. Would require new instrumentation or infrastructure before the metric could be measured.

This assessment doesn't change any metric yet — it just tags each one so Stage 4 can decide what to do: keep as-is, activate, swap for a proxy, defer until after deployment, or eliminate. Approving means you agree the labels reflect reality in your environment (systems, tracking, data availability).

## Where to read the full artifact
`bvif-docs/01-ai-driven-corporate-lending-202606/03-metrics-identification/feasibility-table.md`

---

**Summary:**

| # | Metric | Feasibility | Notes |
|---|---|---|---|
| 1 | Campaign Conversion Rate* | F1 | Already tracked |
| 2 | New Corporate Loans Originated* | F1 | Already reported |
| 3 | Average Time-to-Decision | F1 | Tracked; ~3 weeks currently |
| 4 | Corporate Lending Revenue | F1 | Tracked via credit tables |
| 5 | Cost per Credit Decision* | F2 | Components exist, ratio not calculated |
| 6 | Analyst Productivity | F1 | Already tracked |
| 7 | Manual Processing Hours per Application | F2 | Estimated, not tracked per-application |

---

## Question 1
Do you approve the feasibility assessment?

A) Approve and continue to Stage 4 — Metrics Adjustment
B) Request changes (please describe after [Answer]: tag below)
X) Other (please describe after [Answer]: tag below)

[Answer]: A)
