# Metrics Adjustment — Decision Log

| Business Value Category | Metric Name | Arithmetic Definition | Feasibility | Situation | Decision | Reasoning |
|---|---|---|---|---|---|---|
| Increase Operational Efficiency | Unplanned Downtime Rate % (highlighted) | (Unplanned Downtime Hours / Total Available Hours) × 100 | F2 | Datapoints exist but metric not established. Requires consolidation and regular reporting setup. | Activate | Critical operational metric. Data exists; establish automated extraction and reporting mechanism. |
| Increase Operational Efficiency | Mean Time Between Failures (MTBF) (highlighted) | Total Operating Hours / Number of Unplanned Failures | F2 | Datapoints exist but not reported regularly. Requires extraction mechanism and reporting cadence. | Activate | Key reliability indicator. Data exists; implement regular calculation and reporting process. |
| Increase Operational Efficiency | Maintenance Cost per Unit Produced | Total Maintenance Costs (Planned + Unplanned) / Total Units Produced | F2 | Annual data available but metric not calculated. Requires calculation setup and regular reporting. | Activate | Important efficiency metric. Annual data exists; establish quarterly or monthly calculation cadence. |
| Increase Operational Efficiency | Unplanned Work Order Rate (highlighted) | Number of Unplanned Work Orders / Total Work Orders × 100 | F2 | Work order classification exists (planned vs unplanned). Metric calculation and reporting needed. Replaces "Emergency Repair Cost" as more measurable proxy. | Activate | Proxy metric for emergency maintenance activity. Work order data exists; implement automated calculation from work order system. |
| Increase Operational Efficiency | Planned vs Unplanned Maintenance Ratio | Planned Maintenance Hours / Unplanned Maintenance Hours | F2 | Per-equipment logs exist but consolidation needed. Requires aggregation mechanism across facilities. | Activate | Tracks shift to proactive maintenance. Data exists across facilities; establish cross-site aggregation and reporting. |
| Grow Revenue | On-Time Delivery Rate % (highlighted) | (Orders Delivered On-Time / Total Orders) × 100 | F1 | Metric already tracked weekly via dashboards. Ready to use. | Keep as-is | Already tracked and available. No changes needed. |
| Grow Revenue | Production Capacity Utilization % (highlighted) | (Actual Production Output / Maximum Production Capacity) × 100 | F2 | Both actual output and expected capacity data available. Metric calculation needed. | Activate | Critical capacity metric. Data exists; establish regular calculation and reporting mechanism. |

## Summary

- **Keep as-is**: 1 metric (Feasibility 1)
- **Activate**: 6 metrics (Feasibility 2)
- **Replace with proxy**: 0 metrics (no Feasibility 3 metrics)
- **Defer**: 0 metrics
- **Eliminate**: 0 metrics

All metrics are measurable with existing data. No critical gaps identified.
