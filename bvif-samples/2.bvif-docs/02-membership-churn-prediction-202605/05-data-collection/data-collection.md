# Data Collection

**Source**: All data points are extracted from the storyline document `bvif-samples/bvif-scenarios/scenario_B-Sport-club/Scenario B - Sport club - Storyline-v2-2026-05-27.md`.
**Provenance label**: `storyline-v2-2026-05-27` for every value below (Source Fidelity: documented).

---

## Metric 1: Sócio Annual Renewal Rate %

- **Category**: Grow Revenue
- **Definition**: (Members active Jan 1 still active Dec 31 / Members active Jan 1) × 100
- **Current Baseline (2025)**: **54%** (= 42,200 retained on Dec 31 ÷ 78,200 active Jan 1; total cohort exits 36,000 = 19,800 voluntary + 16,200 lapsed)
- **Annual Trend**:
  | Year | Renewal Rate | Source |
  |---|---|---|
  | 2021 | 65% | Annual Membership Flow |
  | 2022 | 60% | Annual Membership Flow |
  | 2023 | 57% | Annual Membership Flow |
  | 2024 | 57% | Annual Membership Flow |
  | 2025 | 54% | Annual Membership Flow |
- **Quarterly Trend (8 quarters, derived)**:
  | Quarter | Quarterly Renewal Rate |
  |---|---|
  | Q1 2024 | 90.3% |
  | Q2 2024 | 89.5% |
  | Q3 2024 | 89.1% |
  | Q4 2024 | 88.6% |
  | Q1 2025 | 89.3% |
  | Q2 2025 | 88.5% |
  | Q3 2025 | 88.2% |
  | Q4 2025 | 87.4% |
- **Financial impact per unit**: A 1-percentage-point lift in annual renewal rate retains **782 members** (≈ 1% of 78,200 active at start of year). Each retained member is worth **$541/year** in revenue (≈$470 gross margin).
- **Industry benchmark**: NFL 85–90%; NBA 80–85%; English Premiership Rugby (closest comp) 62–74%; MLS 70–76%; Brazilian Série A 54–66%.
- **Improvement target**: **+10 percentage points (conservative end of 10–18 pp range)** → renewal rate 64% in Year 1.
- **Target rationale**: AI-driven churn prediction programs across industries report 12–22 pp uplift in Year 1; we use the conservative 10 pp to avoid optimistic double-counting and to align with peer Brazilian Série A best (66%). The model is expected to act on both voluntary churn signals (declining engagement, tier downgrades) and payment-failure signals (the 40–45% of exits that are lapses).

---

## Metric 2: Members Exited per Year (Voluntary + Lapsed)

- **Category**: Grow Revenue
- **Definition**: Count of members who exited during a calendar year, split into voluntary cancellations and payment-failure lapses
- **Current Baseline (2025)**: **36,000 total exits** (19,800 voluntary + 16,200 lapsed)
- **Annual Trend**:
  | Year | Voluntary | Lapsed | Total Exits | Lapse Share |
  |---|---|---|---|---|
  | 2021 | 6,800 | 4,600 | 11,400 | 40% |
  | 2022 | 10,300 | 7,500 | 17,800 | 42% |
  | 2023 | 15,800 | 12,000 | 27,800 | 43% |
  | 2024 | 18,300 | 14,400 | 32,700 | 44% |
  | 2025 | 19,800 | 16,200 | 36,000 | 45% |
- **Quarterly Trend (2024–2025)**:
  | Quarter | Voluntary | Lapsed | Total |
  |---|---|---|---|
  | Q1 2024 | 4,100 | 3,300 | 7,400 |
  | Q2 2024 | 4,500 | 3,500 | 8,000 |
  | Q3 2024 | 4,700 | 3,700 | 8,400 |
  | Q4 2024 | 5,000 | 3,900 | 8,900 |
  | Q1 2025 | 4,600 | 3,800 | 8,400 |
  | Q2 2025 | 4,900 | 4,000 | 8,900 |
  | Q3 2025 | 5,000 | 4,100 | 9,100 |
  | Q4 2025 | 5,300 | 4,300 | 9,600 |
- **Financial impact per unit**: $541 revenue / $470 gross margin per exit avoided.
- **Improvement target**: Reduce 2025 total exits by ≈7,820 (corresponding to the +10 pp renewal rate uplift). Target = ≈28,180 total exits.
- **Note**: Financial value carried by Metric 1 (renewal rate). This metric is the operational counterpart and exposes the voluntary/lapsed split — the model addresses both signals.

---

## Metric 3: Sócio Membership Revenue $

- **Category**: Grow Revenue
- **Definition**: Sum of monthly fees collected from active members during the period
- **Current Baseline (2025)**: **$40.8M**
- **Annual Trend**: $22.3M (2021) → $33.0M (2022) → $39.9M (2023) → $41.2M (2024) → $40.8M (2025)
- **Quarterly Trend**: ~$9.85M / $10.10M / $10.30M / $10.95M / $10.40M / $10.20M / $10.05M / $10.15M
- **Improvement target**: Outcome of Metric 1; not independently set.
- **Note**: Financial value carried by Metric 1 to avoid double-counting.

---

## Metric 4: Average Match-Day Spend per Sócio Fan $

- **Category**: Grow Revenue (ancillary)
- **Definition**: Total match-day F&B + merchandise spend by sócio fans / Sócio fan attendance
- **Current Baseline (2025)**: blended **$25.90** (all fans). Sócio segments specifically: high-attendance $38.40, moderate $27.20, low $19.80.
- **Improvement target**: Not independently quantified — held conservatively at $0 in Stage 6 to avoid speculation about how retention shifts the segment mix.
- **Note**: Reported as a non-financial highlight; expected to grow as more sócios are retained, particularly in the moderate and high-attendance segments.

---

## Metric 5: Avoided Acquisition Cost $

- **Category**: Increase Operational Efficiency
- **Definition**: (Members retained vs. baseline) × Blended CAC ($47)
- **Current Baseline (2025)**: $0 — the metric did not exist; the club acquired 32,800 new members at $47 blended CAC = ~$1.54M total acquisition spend; replacement cost for 36,000 exited members was estimated at $1.69M.
- **Financial impact per unit**: $47 per retained member (blended; range $18–$96 by channel).
- **Improvement target**: Avoid acquiring ~7,820 replacement members (the renewal-rate-uplift equivalent) → **$367,540 annual avoided CAC**.
- **Source**: Membership Economics + Member Acquisition Channel Mix tables.

---

## Reference Constants Used

| Constant | Value |
|---|---|
| Members active Jan 1, 2025 | 78,200 |
| Members active Dec 31, 2025 | 75,000 |
| Avg annual revenue per member | $541 |
| Avg gross margin per member | $470 |
| Blended CAC | $47 |
| 2025 voluntary cancellations | 19,800 |
| 2025 payment-failure lapses | 16,200 |
| 2025 total exits | 36,000 |
| 2025 new members acquired | 32,800 |
