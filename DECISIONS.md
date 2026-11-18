# Decisions

Newest first. One entry per decision taken at a stop point.

<!--
## YYYY-MM-DD: <short title>
**Canvas block:** <number>
**Decision:** <what was decided>
**Reason:** <why>
**Alternatives considered:** <what else, and why not>
**Decided by:** <names>
-->

## 2026-11-17: Known in advance – turnover up to today, measured weather as forecast stand-in
**Canvas block:** 6
**Decision:** Forecasts for t+1 may use turnover up to and including day t, calendar and Kiel Week of t+1, and measured weather of t+1 as a stand-in for the weather forecast.
**Reason:** At closing time today's turnover is known; a next-day weather forecast is close to the measured weather, and no forecast data is available.
**Alternatives considered:** Turnover only up to yesterday; no weather for t+1.
**Decided by:** Team 11

## 2026-11-17: Success = beat both baselines on MAPE, overall and per group
**Canvas block:** 4
**Decision:** Metric MAPE per group; baselines are the naive "same weekday last week" rule and linear regression; the model is recommended only if it beats both overall and in every group (group 6 with caveat). Over- and under-forecasting count equally.
**Reason:** MAPE is the course metric; current practice is unknown, so the naive rule stands in for it.
**Alternatives considered:** Only one baseline; fixed MAPE target; only overall improvement; asymmetric error costs.
**Decided by:** Team 11

## 2026-11-17: Audiences – branch manager and course
**Canvas block:** 3
**Decision:** Branch manager gets a simple table per group and a presentation; technical readers get notebooks and README.
**Reason:** Covers the decision-maker and the technical reader.
**Alternatives considered:** Course audience only.
**Decided by:** Team 11

## 2026-11-17: Seasonal bread (group 6) included, flagged as uncertain
**Canvas block:** 2
**Decision:** Group 6 is forecast but reported separately with a caveat.
**Reason:** The course asks for all six groups; only 4 seasons of data.
**Alternatives considered:** Exclude group 6.
**Decided by:** Team 11

## 2026-11-17: Forecast target is turnover in € per product group
**Canvas block:** 1
**Decision:** The forecast gives the expected turnover (€) per product group for the next day, as a guide for baking quantities.
**Reason:** The data only contains turnover in €; there are no prices or quantities, and the course evaluates turnover with MAPE.
**Alternatives considered:** Number of pieces – not possible without prices or quantity data.
**Decided by:** Team 11

## 2026-11-17: Forecast needed the evening before, by the branch manager
**Canvas block:** 1
**Decision:** The branch manager makes the baking plan daily at closing time for the next day; forecast horizon is 1 day.
**Reason:** Bakers start before the shop opens, so the plan must exist the evening before.
**Alternatives considered:** Same-morning planning by the bakery team; weekly plan (horizon up to 7 days).
**Decided by:** Team 11

## 2026-11-17: Scope is baking only; staffing parked
**Canvas block:** 1
**Decision:** The canvas covers the baking decision only. Staffing moved to Open questions.
**Reason:** One decision per canvas keeps success criteria clear; the team's question is about baking.
**Alternatives considered:** Baking + staffing in one canvas.
**Decided by:** Team 11
