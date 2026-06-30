# Metrics Adjustment — Decision Log

| # | Business Value Category | Metric Name | Arithmetic Definition | Feasibility | Situation | Decision | Reasoning |
|---|---|---|---|---|---|---|---|
| 1 | Grow Revenue | Campaign Conversion Rate* | (Corporate prospects → loan clients ÷ Total prospects contacted) × 100 | F1 | Already tracked and reported regularly | Keep as-is | Metric is production-ready. No changes needed. |
| 2 | Grow Revenue | New Corporate Loans Originated* | Count of new corporate loan contracts per quarter | F1 | Already reported on a regular basis | Keep as-is | Metric is production-ready. No changes needed. |
| 3 | Grow Revenue | Average Time-to-Decision | Average business days from application to credit decision | F1 | Tracked end-to-end; currently ~3 weeks (15 business days) | Keep as-is | Metric is production-ready. No changes needed. |
| 4 | Grow Revenue | Corporate Lending Revenue (Interest Income) | Total interest income from corporate portfolio per quarter (USD) | F1 | Tracked via credit tables by term, risk profile, and amount | Keep as-is | Metric is production-ready. No changes needed. |
| 5 | Increase Operational Efficiency | Cost per Credit Decision* | Total origination cost ÷ Number of corporate credit decisions per quarter | F2 | Team costs and decision counts known separately, ratio not calculated | Activate | Straightforward calculation — divide known team cost (salaries + overhead) by known decision count. Can be automated as a quarterly report. |
| 6 | Increase Operational Efficiency | Analyst Productivity (Decisions per Analyst) | Corporate credit decisions per quarter ÷ FTE analysts | F1 | Already tracked — decision volumes per analyst/team reported | Keep as-is | Metric is production-ready. No changes needed. |
| 7 | Increase Operational Efficiency | Manual Processing Hours per Application | Analyst hours per corporate application processed | F2 | Estimated at ~3 weeks per cycle; not tracked per-application | Activate | Can be derived from team capacity (total available hours) ÷ applications processed. For more precision, introduce lightweight time-logging per application. |

---

**Summary of decisions:**
- **Keep as-is:** 5 metrics (#1, #2, #3, #4, #6)
- **Activate:** 2 metrics (#5, #7)
- **Replace with proxy:** 0
- **Defer:** 0
- **Eliminate:** 0
- **STOP condition triggered:** No

All 7 metrics proceed to data collection.
