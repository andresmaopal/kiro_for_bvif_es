# Clube Esportivo Bandeirantes — Membership Churn Prediction: Business Value Summary

## Executive Summary

Clube Esportivo Bandeirantes, a Brazilian Série A football club with 75,000 active sócio torcedor members and $206.8M in 2025 operating revenue, proposes deploying an AI model to predict membership cancellations before they occur and trigger personalized retention interventions.

The 2025 annual sócio renewal rate stood at **54%** — the bottom of the Brazilian Série A range (54–66%) and well below comparable subscription-style sports memberships (NFL 85–90%, English Premiership Rugby 62–74%). The renewal rate has drifted down steadily from 65% in 2021 and 60% in 2022. 2025 was also the first year on record with a net membership decline (−3,200), driven by 36,000 total exits — 19,800 voluntary cancellations and 16,200 payment-failure lapses — against 32,800 new acquisitions. The lapsed segment, running 40–45% of total exits across the entire 2021–2025 period, is a structural feature of Brazilian monthly-subscription products and is one of the highest-precision targets the model can act on.

This BVIF assessment, drawing on five years of annual data and eight quarters of operational data unified in BOLALAKE, identified two primary financial mechanisms: revenue protection from members who would otherwise have churned, and avoided cost from not having to acquire replacements.

**The initiative delivers an estimated $4.04M in quantified annual business value** at the conservative end of the benchmark range (+10 pp renewal uplift), scaling to \$7.28M at the top of the range (+18 pp). Beyond the quantified financial benefit, the initiative reverses the club's first net membership decline and protects the compounding match-day revenue tied to long-tenured sócios.

---

## Total Quantified Annual Business Value

| Business Value Driver | Annualized Value | Calculation Basis |
|---|---|---|
| Renewal rate uplift (revenue protection) | $3,675,400 / yr | +10 pp annual renewal rate (54% → 64%) × 78,200 active members at year start = 7,820 members retained × $470 gross margin per member |
| Avoided acquisition cost | $367,540 / yr | 7,820 members retained × $47 blended CAC |
| **Total** | **$4,042,940 / yr** | |

### Calculation Methodology

**1. Renewal Rate Uplift ($3.68M annually)**

Each percentage point of annual renewal rate equates to **782 members retained** (1% of 78,200 active on Jan 1, 2025). Industry benchmarks across sports, streaming, and telecommunications report **+12 to +22 percentage points** of renewal uplift in Year 1 of an AI churn-prediction program. We use the conservative **+10 pp** target, both to undercut the benchmark range and to avoid compounding optimistic assumptions:

- 7,820 members retained × **\$470** gross margin per member (after servicing costs) = **$3,675,400 / year**

We use gross margin rather than gross revenue ($541) because the figure must net out the cost of servicing the retained member — credit-card processing, app entitlements, partial benefits delivered.

**2. Avoided Acquisition Cost ($0.37M annually)**

Each member retained is one less new member that has to be acquired. Blended CAC across the six current acquisition channels is **$47**:

- 7,820 members retained × **\$47 CAC** = **\$367,540 / year**

This is an operational efficiency benefit — distinct from, and additive to, the gross-margin protection captured in (1).

### Sensitivity

| Renewal Uplift | Total Annual Value |
|---|---|
| +10 pp (conservative — used for headline) | **$4.04M** |
| +14 pp (midpoint) | $5.66M |
| +18 pp (top of benchmark) | $7.28M |

### Double-Counting Verification

Three Grow Revenue metrics (Renewal Rate, Members Cancelled, Sócio Membership Revenue) all describe the same population of retained members; financial value is attributed to **Renewal Rate** only — the other two are kept for operational/financial reporting. Avoided CAC is structurally distinct (cost the club does not spend) and is therefore additive.

---

## Consolidated Metrics Table — Handoff Artifact

| # | Category | Metric | Definition | Baseline (2025) | Target | Expected Improvement | Annualized $ Value | Cadence | Owner | Provenance | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Grow Revenue | Sócio Annual Renewal Rate % | (Members active Jan 1 still active Dec 31 / Members active Jan 1) × 100 | 54% | 64% | +10 pp | **$3,675,400** | Quarterly + annual | Chief Commercial Officer | storyline-v2-2026-05-27 | Headline metric. |
| 2 | Grow Revenue | Members Exited per Year (Voluntary + Lapsed) | Count of exits in calendar year, split into voluntary cancellations and payment-failure lapses | 36,000 (19,800 + 16,200) | 28,180 | −7,820 | Captured in Metric 1 | Monthly | Chief Commercial Officer | storyline-v2-2026-05-27 | Operational counterpart. Voluntary/lapsed split exposes which signals the model is acting on. |
| 3 | Grow Revenue | Sócio Membership Revenue $ | Sum of fees collected | $40.8M | ~$45.0M (range, Metric 1 outcome) | +$4.2M topline | Captured in Metric 1 | Monthly | CFO | storyline-v2-2026-05-27 | Topline reported in financials. |
| 4 | Grow Revenue | Avg Match-Day Spend per Sócio Fan $ | Match-day spend by sócio fans / sócio attendance | Blended $25.90 (range $19.80–$38.40) | Expected positive | Non-financial | $0 (non-financial) | Quarterly | CDO + F&B Ops | storyline-v2-2026-05-27 | Held at $0 in Stage 6. |
| 5 | Increase Operational Efficiency | Avoided Acquisition Cost $ | Members retained × CAC | $0 (not previously calculated) | $367,540 | +$367K | **$367,540** | Quarterly | CDO + Marketing | storyline-v2-2026-05-27 | Additive to Metric 1. |

---

## Non-Financial Highlights

- **Reverses the net-decline trend.** 2025 was the first year on record with a net loss of sócio members. The +10 pp uplift turns a 2025-style year into roughly +4,500 net members.
- **Reaches Brazilian Série A best-in-class.** A 64% renewal rate moves the club from the bottom of the peer range (54%) to the upper end (66% — comparable to the strongest Série A clubs).
- **Compounds match-day spend.** High-attendance sócios spend 48% more per match day than the blended fan average. Retaining this segment protects F&B and merchandise revenue lines beyond the renewal-rate value alone.
- **Operationalizes BOLALAKE.** This is the first commercial AI workload running on top of the unified data platform — proving the investment in Phase 1 of Projeto Bandeira and clearing the path for the next two AI initiatives (dynamic ticket pricing, in-stadium personalization).

---

## Strategic Value Beyond the Numbers

The financial case is only part of the picture. The strategic context for the board:

- **Membership is the most fan-powered revenue line the club operates.** Unlike TV rights (fixed by collective contract) or transfers (irregular), the sócio program is the one revenue stream where the club's commercial decisions directly determine the outcome.
- **Renewal performance is a leading indicator of fan sentiment.** When renewal rates fall, every other commercial KPI follows within 12–18 months — match-day attendance, merchandise pull-through, app engagement. Stabilizing renewal stabilizes the rest of the commercial portfolio.
- **The data foundation has already been paid for.** BOLALAKE was built in Phase 1 of Projeto Bandeira. Deploying churn prediction is incremental work — model, MLOps, retention treatment design — not a net-new platform investment.

---

## Risk of Inaction

If the 2024→2025 trend continues unchecked:

- **2026 renewal rate** is on track to drop further from 54% (Brazilian Série A bottom-quartile territory).
- **Net membership change in 2026** is on track to be worse than 2025's −3,200 — extrapolating exit growth (10% YoY 2024→2025: 32,700 → 36,000) and acquisition decline (−6% YoY 2024→2025: 34,900 → 32,800) gives a likely net change in the range of −4,500 to −5,500 members.
- **Sócio revenue** declines for a second consecutive year for the first time in the club's recorded history.
- **Compounding match-day loss** as the highest-spending sócio segment thins — a churned high-attendance sócio is worth not just the $470 margin lost on the membership but the recurring match-day spend differential ($38.40 vs. $16.40 for non-members).
- **Payment-failure lapses (16,200 in 2025) continue growing** without an active intervention layer; this is the most directly addressable component for the AI model.

The cost of inaction is therefore higher than a flat extrapolation of membership revenue suggests. The renewal rate is the single most leveraged commercial metric the club currently has.

---

## Appendix A — Initiative Definition (condensed)

**Initiative**: Membership Churn Prediction for the sócio torcedor program.
**Mechanism**: AI model scores every active member weekly on cancellation risk using attendance, app engagement, F&B/merchandise transactions, payment history, and tier changes. High-risk members trigger differentiated retention treatments 30–60 days before typical cancellation events.
**Sponsor**: Chief Digital Officer (Marcos Alves) with the Chief Commercial Officer.
**Data foundation**: BOLALAKE — operational since July 2024 — provides the unified fan ID and behavioral signals required.

## Appendix B — AI-BVIF Methodology (one-page)

**Discovery Phase** — defined the initiative, mapped it to CAF v3 categories (primary: Grow Revenue; secondary: Increase Operational Efficiency).

**Metrics Phase** — identified 6 candidate metrics, assessed feasibility (3×F1, 2×F2, 1×F3), and through Stage 4 adjustment retained 5 (eliminated NPS as F3 with no defensible methodology).

**Quantification Phase** — extracted all data points from a single source document with full provenance attribution; calculated $4.04M annualized value at the conservative end of the +10 to +18 pp benchmark range; verified no double-counting between the Grow Revenue metrics (consolidated to Metric 1) and the Operational Efficiency metric (Metric 5, structurally distinct).

The methodology favors transparency over precision: every figure ties back to a documented baseline, every benchmark to a published comparison, and every calculation to an arithmetic that a reviewer can reproduce in five minutes.

---

*Document version: 1.0 | Date: 2026-05-26 | BVIF run on storyline v2 (Scenario B — Sport Club).*
