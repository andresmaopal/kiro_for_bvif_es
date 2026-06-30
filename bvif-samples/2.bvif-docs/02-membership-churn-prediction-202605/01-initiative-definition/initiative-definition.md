# Initiative Definition — Membership Churn Prediction

## Who We Are
We are Clube Esportivo Bandeirantes, a Brazilian Série A football club founded in 1923, with 6.2 million registered supporters, 75,000 active sócio torcedor members, and a 38,000-seat stadium (Arena Ferradura) in São Bernardo das Minas, Minas Gerais. Our 2025 operating revenue was $206.8M, with the sócio membership program contributing $40.8M (19% of total).

## What We Propose
We propose deploying an AI model that continuously monitors sócio member behavior — match attendance, club app engagement, food & beverage and merchandise transactions, payment history, and tier changes — to predict which members are at risk of cancelling their membership before they do. The model output will trigger personalized retention interventions (offers, communications, account-team outreach) targeted at the highest-risk profiles 30–60 days before typical cancellation events.

## Current State
Today, our retention motion is reactive. Cancellations are processed when a member submits them; the only signal we have is the cancellation itself. Despite having behavioral data for every fan in BOLALAKE (our unified data platform, operational since July 2024), we have no model that translates behavior into risk.

The result is structural churn:
- Annual renewal rate has drifted from 65% (2021) and 60% (2022) to **54% (2025)**.
- 2025 saw the first net membership decline in the club's recorded history: **−3,200 members** (32,800 acquired vs. 36,000 exited — split into 19,800 voluntary cancellations and 16,200 payment-failure lapses).
- Brazilian Série A peers operate in the 54–66% renewal range; we are at the bottom of that distribution.
- The lapsed segment is structurally addressable by the model: payment-failure exits running at 40–45% of total exits across the entire 2021–2025 period reflect Brazilian payment-card behavior, not active member rejection — and are therefore a strong intervention target.

## Future State
With a deployed churn-prediction model, we will:
- Score every active sócio member weekly on cancellation risk.
- Trigger differentiated retention treatments for high-risk members (priority match access, personalized win-back offers, direct outreach for high-tier members).
- Measure intervention effectiveness and feed outcomes back into the model.

The shift is from "retain after cancellation" to "intervene before cancellation."

## Business Impact Areas
1. **Revenue Protection**: Increasing renewal rate directly preserves recurring sócio revenue (≈$541 average annual revenue per member).
2. **Acquisition Cost Avoidance**: Every retained member is one less new member that must be acquired (≈$47 blended CAC, with channel-mix CAC ranging $18–$96).
3. **Lifetime Value Expansion**: Longer-tenured members spend more per match day (high-attendance sócios spend 148 vs. blended index 100), so retention compounds through ancillary revenue.

## Budget Ownership
The budget for this initiative is owned by the **Chief Digital Officer (CDO)**, sponsored jointly with the **Chief Commercial Officer**, who is accountable for sócio program performance and retention outcomes. The technical platform sits in the existing Projeto Bandeira investment envelope; incremental cost is model development, MLOps, and the retention treatment campaigns themselves.
