# Agentic Data Science Canvas

**Project:** Team 11 – Sales forecasting for a bakery branch
**Team:** Thore Pingpank, Anne Eilrich, Lennard Goronzy, Katharina Helzel
**Version:** 2026-11-17

> Owners: 👤 human decides · 🤖 agent drafts, human approves.
> Keep each block short. Details go in linked files; decisions go in `DECISIONS.md`.

---

## Problem

### 1. Decision 👤
<!-- Who decides what, when and how often? What happens today without this analysis? -->
The **branch manager** decides **every day at closing time** how much of each of the six product groups to bake **for the next day** (forecast horizon: 1 day ahead). The forecast gives the expected **turnover in € per product group** as a guide for the baking quantity.
- Scope: baking only; staffing is parked (see Open questions).
- Today without the model: **unknown** (see Open questions).
- Limits: turnover ≠ pieces (no prices in the data); on sold-out days turnover understates true demand.

### 2. Questions 👤
<!-- The analysis questions that would change the decision. For each: what the data can answer, and what it cannot. -->
**Main question:** What turnover (€) will each of the six product groups have tomorrow?
- *Answer looks like:* one number in € per group for the next day, plus the typical error (MAPE) of the model for that group.
- *Data can answer:* daily turnover per group 2013-07-01 – 2018-07-31, with weekday, holidays, Kiel Week and weather as possible influences.
- *Data cannot answer:* number of pieces to bake (no prices); true demand on sold-out days; anything about other branches.
- *Thin basis:* group 6 (seasonal bread) – only 4 seasons (2013–2017), 292 days; result reported separately and flagged as uncertain. Kiel Week effect rests on only 6 Kiel Weeks.

### 3. Audiences 👤
<!-- Who receives which result, in which form? At least: the decision-maker and the technical reader. -->
- **Branch manager (decision-maker):** a simple table "expected turnover tomorrow per product group" and a presentation with the key message and limits in plain words.
- **Technical readers (course instructors, other teams):** notebooks and README with MAPE per group, baselines, data decisions and limits.

### 4. Success 👤
<!-- Metric(s), the baseline to beat, what is good enough to act on. Which errors are worse than others? -->
- **Metric:** MAPE per product group (course metric), plus overall.
- **Baselines to beat:** (1) naive rule "same weekday last week"; (2) linear regression (course baseline model).
- **Good enough to recommend:** lower MAPE than both baselines, overall **and** in every product group (group 6 only with a caveat).
- **Error costs:** too little and too much count equally (as in MAPE). We also report whether the model tends to forecast too high or too low.

---

## Data and method

### 5. Data 🤖
<!-- Sources, unit of observation, period covered, keys, known gaps. Link the data fact sheet. -->

### 6. Known in advance 👤
<!-- What information is available at the moment the result is needed? Everything else is leakage. -->
**Moment of prediction:** closing time of day *t*, forecast for day *t+1*.
- **Allowed:** turnover of all groups **up to and including day t**; calendar of t+1 (weekday, month, holidays, school holidays); Kiel Week dates (known well in advance); weather of t+1 – measured weather used as a stand-in for the forecast (limit: real-use results will be slightly worse).
- **Not allowed:** any turnover from day t+1 or later; aggregates that include t+1 (e.g. un-shifted rolling means, monthly totals).

### 7. Data decisions 👤
<!-- Joins, missing values, encodings, exclusions, each with a reason. Link the entries in DECISIONS.md. -->

### 8. Checks 🤖
<!-- Checkpoints and the invariants that must hold at each (row counts, keys, date ranges, IDs, baseline). Link checks/. -->

---

## Evidence and action

### 9. Experiments 🤖
<!-- Experiment cards and their status; best result so far vs. baseline. Link experiments/LOG.md. -->

### 10. Findings 🤖
<!-- What we learned, how sure we are, and what the data cannot tell. -->

### 11. Recommendation 👤
<!-- What the decision-maker should do, under which conditions. Signed off by the team. -->

---

## Open questions
<!-- Parking lot. Each item names who resolves it. -->
- **Staffing:** could the same forecast support staff planning? Parked; later use. *Resolves: team.*
- **Current practice:** how does the branch decide baking quantities today without a model? Unknown; the naive rule "same weekday last week" serves as stand-in reference (block 4). *Resolves: team, if instructors can tell.*
- **Data split:** how to split training / validation (by time, test period Aug 2018 – Jul 2019 set by the course). *Resolves: team, before the first model.*

## Decision log
See `DECISIONS.md`.
