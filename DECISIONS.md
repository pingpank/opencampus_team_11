# Decisions

Newest first. One entry per decision taken at a stop point.

## 2026-11-23: Checks for block 8
**Canvas block:** 8
**Decision:** All four proposed check groups are kept: raw data, join, time & leakage, content & baseline (details in CANVAS block 8).
**Reason:** Each protects a fact found in profiling or a rule from block 6.
**Alternatives considered:** A subset of the groups.
**Decided by:** Team 11

## 2026-11-23: Last-week rule falls back further when last week has no value
**Canvas block:** 4
**Decision:** If the same weekday one week earlier has no turnover (closed day, missing group-4 row), the rule uses the same weekday 2 weeks earlier, and so on back until a value exists.
**Reason:** Uses only the past and gives a baseline value for every day the model is evaluated on, so both are compared on the same days.
**Alternatives considered:** Drop those days from the baseline comparison.
**Decided by:** Team 11

## 2026-11-23: 31 December peaks kept, with a New Year's Eve feature
**Canvas block:** 7
**Decision:** The group-5 peaks on 31 Dec (1,432–1,879, 5–7× median) stay in the data; a "New Year's Eve" feature (known in advance) will be added.
**Reason:** Real values that recur every year; removing them would guarantee a bad forecast for 31 Dec.
**Alternatives considered:** Keep without a feature; remove from training.
**Decided by:** Team 11

## 2026-11-23: Missing weather filled with the previous day's value
**Canvas block:** 7
**Decision:** Days without a weather row (3 in the sales period, 13 in the test period) and missing `Bewoelkung` (10 days in 2017) are filled with the last known value (forward fill).
**Reason:** Uses only past information (no leakage) and works in the test period, where every day must be forecast.
**Alternatives considered:** Monthly mean from training; dropping rows (impossible in the test period).
**Decided by:** Team 11

## 2026-11-23: Wettercode not used
**Canvas block:** 7
**Decision:** The column `Wettercode` is not used as a feature.
**Reason:** Missing on 669 days and not at random (missing days are warmer and less cloudy); team prefers the simpler weather variables (temperature, cloud cover, wind).
**Alternatives considered:** Missing as own category "no notable weather" with grouped codes; own category with all 41 codes.
**Decided by:** Team 11

## 2026-11-23: Left join with sales as the base; no rows added
**Canvas block:** 7
**Decision:** Weather and Kiel Week are left-joined to the sales file on `Datum`. Consequences: the 38 closed days, the 53 missing group-4 days and group-6 days outside its season stay absent (no zeros added); group 6 is only forecast on days it is on sale; `KielerWoche` missing after the join is set to 0.
**Reason:** We do not know whether missing rows mean 0 € or missing records; MAPE cannot be computed for 0; the manager knows closed days and whether seasonal bread is offered in advance. The Kiel Week file lists only Kiel Week days (documentation).
**Alternatives considered:** Fill missing days/groups with 0; forecast group 6 all year.
**Decided by:** Team 11

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
**Reason:** The course asks for all six groups; only 5 seasons of data (corrected 2026-11-23 from "4" after profiling).
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
