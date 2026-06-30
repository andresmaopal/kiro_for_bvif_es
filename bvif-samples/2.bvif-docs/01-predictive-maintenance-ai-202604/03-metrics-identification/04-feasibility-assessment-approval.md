# Stage 3 / Task 2 — Metrics Feasibility Assessment Approval

## Feasibility Summary

Based on your responses, here's the feasibility classification for each metric:

### Feasibility 1 (Ready to Use)
- **On-Time Delivery Rate %** — Already tracked weekly via dashboards

### Feasibility 2 (Data Exists, Calculation Needed)
- **Unplanned Downtime Rate %** — Datapoints exist, metric not established
- **Mean Time Between Failures (MTBF)** — Datapoints exist, not reported regularly
- **Maintenance Cost per Unit Produced** — Annual data available, metric not calculated
- **Unplanned Work Order Rate %** — Work order classification exists (replaces Emergency Repair Cost)
- **Planned vs Unplanned Maintenance Ratio** — Per-equipment logs exist, consolidation needed
- **Production Capacity Utilization %** — Actual output and expected capacity data available

### Removed Metrics
- **Customer Retention Rate %** — Removed due to infeasibility (long purchase cycles, no lifecycle tracking)
- **Emergency Repair Cost** — Replaced with "Unplanned Work Order Rate %" as more measurable proxy

## Complete Feasibility Table

| Business Value Category | Metric Name | Arithmetic Definition | Explanation | Feasibility | Comments |
|---|---|---|---|---|---|
| Increase Operational Efficiency | Unplanned Downtime Rate %* | (Unplanned Downtime Hours / Total Available Hours) × 100 | Measures the percentage of time manufacturing equipment is unavailable due to unplanned failures. Lower downtime rate directly translates to increased manufacturing capacity and reduced disruption costs. | Feasibility 2 | Datapoints exist but metric not established. Requires consolidation and regular reporting setup. |
| Increase Operational Efficiency | Mean Time Between Failures (MTBF)* | Total Operating Hours / Number of Unplanned Failures | Tracks the average time equipment operates before experiencing an unplanned failure. Increasing MTBF indicates improved equipment reliability and reduced disruption frequency. | Feasibility 2 | Datapoints exist but not reported regularly. Requires extraction mechanism and reporting cadence. |
| Increase Operational Efficiency | Maintenance Cost per Unit Produced | Total Maintenance Costs (Planned + Unplanned) / Total Units Produced | Measures the efficiency of maintenance spending relative to production output. Predictive maintenance should reduce this ratio by optimizing maintenance timing and preventing costly emergency repairs. | Feasibility 2 | Annual data available but metric not calculated. Requires calculation setup and regular reporting. |
| Increase Operational Efficiency | Unplanned Work Order Rate* | Number of Unplanned Work Orders / Total Work Orders × 100 | Tracks the percentage of maintenance work orders that are unplanned/emergency. Lower rate indicates shift to proactive maintenance. Serves as proxy for emergency repair activity. | Feasibility 2 | Work order classification exists (planned vs unplanned). Metric calculation and reporting needed. Replaces "Emergency Repair Cost" as more measurable proxy. |
| Increase Operational Efficiency | Planned vs Unplanned Maintenance Ratio | Planned Maintenance Hours / Unplanned Maintenance Hours | Measures the shift from reactive to proactive maintenance. A higher ratio indicates better control over maintenance scheduling and reduced emergency interventions. | Feasibility 2 | Per-equipment logs exist but consolidation needed. Requires aggregation mechanism across facilities. |
| Grow Revenue | On-Time Delivery Rate %* | (Orders Delivered On-Time / Total Orders) × 100 | Measures the percentage of customer orders fulfilled by the committed delivery date. Improved equipment uptime enables more reliable production schedules and delivery commitments. | Feasibility 1 | Metric already tracked weekly via dashboards. Ready to use. |
| Grow Revenue | Production Capacity Utilization %* | (Actual Production Output / Maximum Production Capacity) × 100 | Measures how much of the available manufacturing capacity is being used. Reduced downtime increases utilization, creating headroom for additional orders without capital investment. | Feasibility 2 | Both actual output and expected capacity data available. Metric calculation needed. |

---

## Question 3
Do you approve this feasibility assessment?

A) Approve and continue to Stage 4 — Metrics Adjustment
B) Request changes (please describe what needs adjustment after [Answer]: tag below)

[Answer]:
A) Approved