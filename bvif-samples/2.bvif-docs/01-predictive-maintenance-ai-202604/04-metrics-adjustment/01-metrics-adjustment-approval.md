# Stage 4 — Metrics Adjustment Approval

## Decision Summary

All 7 metrics are measurable with existing data:
- **1 metric** is ready to use (Feasibility 1): On-Time Delivery Rate %
- **6 metrics** require activation (Feasibility 2): Establish extraction and reporting mechanisms

No metrics were eliminated, deferred, or replaced with proxies. All metrics proceed to data collection.

## Decision Log

| Business Value Category | Metric Name | Arithmetic Definition | Feasibility | Situation | Decision | Reasoning |
|---|---|---|---|---|---|---|
| Increase Operational Efficiency | Unplanned Downtime Rate % (highlighted) | (Unplanned Downtime Hours / Total Available Hours) × 100 | F2 | Datapoints exist but metric not established. Requires consolidation and regular reporting setup. | Activate | Critical operational metric. Data exists; establish automated extraction and reporting mechanism. |
| Increase Operational Efficiency | Mean Time Between Failures (MTBF) (highlighted) | Total Operating Hours / Number of Unplanned Failures | F2 | Datapoints exist but not reported regularly. Requires extraction mechanism and reporting cadence. | Activate | Key reliability indicator. Data exists; implement regular calculation and reporting process. |
| Increase Operational Efficiency | Maintenance Cost per Unit Produced | Total Maintenance Costs (Planned + Unplanned) / Total Units Produced | F2 | Annual data available but metric not calculated. Requires calculation setup and regular reporting. | Activate | Important efficiency metric. Annual data exists; establish quarterly or monthly calculation cadence. |
| Increase Operational Efficiency | Unplanned Work Order Rate (highlighted) | Number of Unplanned Work Orders / Total Work Orders × 100 | F2 | Work order classification exists (planned vs unplanned). Metric calculation and reporting needed. Replaces "Emergency Repair Cost" as more measurable proxy. | Activate | Proxy metric for emergency maintenance activity. Work order data exists; implement automated calculation from work order system. |
| Increase Operational Efficiency | Planned vs Unplanned Maintenance Ratio | Planned Maintenance Hours / Unplanned Maintenance Hours | F2 | Per-equipment logs exist but consolidation needed. Requires aggregation mechanism across facilities. | Activate | Tracks shift to proactive maintenance. Data exists across facilities; establish cross-site aggregation and reporting. |
| Grow Revenue | On-Time Delivery Rate % (highlighted) | (Orders Delivered On-Time / Total Orders) × 100 | F1 | Metric already tracked weekly via dashboards. Ready to use. | Keep as-is | Already tracked and available. No changes needed. |
| Grow Revenue | Production Capacity Utilization % (highlighted) | (Actual Production Output / Maximum Production Capacity) × 100 | F2 | Both actual output and expected capacity data available. Metric calculation needed. | Activate | Critical capacity metric. Data exists; establish regular calculation and reporting mechanism. |

## Final Metrics List

| Business Value Category | Metric Name | Arithmetic Definition | Explanation |
|---|---|---|---|
| Increase Operational Efficiency | Unplanned Downtime Rate % (highlighted) | (Unplanned Downtime Hours / Total Available Hours) × 100 | Measures the percentage of time manufacturing equipment is unavailable due to unplanned failures. Lower downtime rate directly translates to increased manufacturing capacity and reduced disruption costs. |
| Increase Operational Efficiency | Mean Time Between Failures (MTBF) (highlighted) | Total Operating Hours / Number of Unplanned Failures | Tracks the average time equipment operates before experiencing an unplanned failure. Increasing MTBF indicates improved equipment reliability and reduced disruption frequency. |
| Increase Operational Efficiency | Maintenance Cost per Unit Produced | Total Maintenance Costs (Planned + Unplanned) / Total Units Produced | Measures the efficiency of maintenance spending relative to production output. Predictive maintenance should reduce this ratio by optimizing maintenance timing and preventing costly emergency repairs. |
| Increase Operational Efficiency | Unplanned Work Order Rate (highlighted) | Number of Unplanned Work Orders / Total Work Orders × 100 | Tracks the percentage of maintenance work orders that are unplanned/emergency. Lower rate indicates shift to proactive maintenance. Serves as proxy for emergency repair activity. |
| Increase Operational Efficiency | Planned vs Unplanned Maintenance Ratio | Planned Maintenance Hours / Unplanned Maintenance Hours | Measures the shift from reactive to proactive maintenance. A higher ratio indicates better control over maintenance scheduling and reduced emergency interventions. |
| Grow Revenue | On-Time Delivery Rate % (highlighted) | (Orders Delivered On-Time / Total Orders) × 100 | Measures the percentage of customer orders fulfilled by the committed delivery date. Improved equipment uptime enables more reliable production schedules and delivery commitments. |
| Grow Revenue | Production Capacity Utilization % (highlighted) | (Actual Production Output / Maximum Production Capacity) × 100 | Measures how much of the available manufacturing capacity is being used. Reduced downtime increases utilization, creating headroom for additional orders without capital investment. |

---

## Question 4
Do you approve the metrics adjustment decisions and final metrics list?

A) Approve and continue to Stage 5 — Data Collection
B) Request changes (please describe what needs adjustment after [Answer]: tag below)

[Answer]:
Yes, I approve the metrics adjustments. That's the final metrics list.
