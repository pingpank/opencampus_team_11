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
- *Thin basis:* group 6 (seasonal bread) – only 5 seasons (2013/14 – 2017/18), 292 days; result reported separately and flagged as uncertain. Kiel Week effect rests on only 5 Kiel Weeks (2014–2018).

**Hypotheses about what drives sales** (team, 2026-11-23; not yet tested):
1. **Warm and dry weather → higher croissant sales (group 3).** *Data:* temperature available; "dry" needs `Wettercode`, which is currently not used (see Open questions). *Limit:* measured weather as forecast stand-in; separate weather from season.
2. **During Kiel Week → more roll sales (group 2).** *Data:* `KielerWoche` flag. *Limit:* only 5 Kiel Weeks (2014–2018) – a thin basis.
3. **On rainy days → lower cake sales (group 5).** *Data:* "rainy" needs `Wettercode` (not used); `Bewoelkung` is only a rough stand-in. *Limit:* as for 1.

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
Details: [`docs/data-fact-sheet.md`](docs/data-fact-sheet.md). Source: meteolytix GmbH via opencampus.sh course; license not stated.
- **Sales:** 9,334 rows, one per (day, product group), only days with sales; 2013-07-01 – 2018-07-31. Key (`Datum`, `Warengruppe`) unique. 38 days without any sales (holidays); group 4 missing on 53 further days (2013–2016); group 6 only late Oct – early Jan (5 seasons). 31 Dec = extreme peak in group 5.
- **Weather (observed, Kiel):** 2012-01-01 – 2019-08-01, 169 days without a row (3 in sales period, 13 in test period). `Wettercode` missing on 669 days, not at random (calmer, warmer days); `Bewoelkung` missing on 10 days.
- **Kiel Week:** 9 days per year 2012–2019; 5 Kiel Weeks inside the sales period.
- **Joins:** left joins on `Datum` keep 9,334 rows.
- **Test period** 2018-08-01 – 2019-07-31 held back by the course.

### 6. Known in advance 👤
<!-- What information is available at the moment the result is needed? Everything else is leakage. -->
**Moment of prediction:** closing time of day *t*, forecast for day *t+1*.
- **Allowed:** turnover of all groups **up to and including day t**; calendar of t+1 (weekday, month, holidays, school holidays); Kiel Week dates (known well in advance); weather of t+1 – measured weather used as a stand-in for the forecast (limit: real-use results will be slightly worse).
- **Not allowed:** any turnover from day t+1 or later; aggregates that include t+1 (e.g. un-shifted rolling means, monthly totals).

### 7. Data decisions 👤
<!-- Joins, missing values, encodings, exclusions, each with a reason. Link the entries in DECISIONS.md. -->
See [`DECISIONS.md`](DECISIONS.md), entries of 2026-11-23.
- **Join:** sales file is the base; weather and Kiel Week are left-joined on `Datum` (9,334 rows stay 9,334). No days or zeros are added.
- **Closed days (38):** not in the data → no training, no forecast.
- **Group 4 gaps (53 days):** not in the data → treated as unknown, not as 0.
- **Group 6:** forecast only on days when seasonal bread is on sale (manager knows this in advance).
- **Kiel Week:** missing after the join → 0 (file lists only Kiel Week days).
- **Wettercode:** not used in training (669 missing, not at random). In data exploration only, "rain" = codes 60–69 (narrow, conservative); missing codes stay a separate group.
- **Missing weather (3 sales days, 13 test days; `Bewoelkung` 10 days):** filled with the previous day's value (forward fill, past only).
- **31 December peaks (group 5):** kept; a "New Year's Eve" feature will be added.

### 8. Checks 🤖
<!-- Checkpoints and the invariants that must hold at each (row counts, keys, date ranges, IDs, baseline). Link checks/. -->
Confirmed by the team on 2026-11-23. Run with `uv run pytest checks` ([`checks/`](checks/)). Status: only the starter check (data loads) is implemented so far.
1. **Raw data:** (`Datum`, `Warengruppe`) unique; `id` = YYMMDD·10 + group; `Umsatz` > 0 and never missing; `Warengruppe` only 1–6; dates 2013-07-01 – 2018-07-31.
2. **Join:** still 9,334 rows after the joins; `KielerWoche` only 0/1 with exactly 45 days = 1; no missing weather values after forward fill.
3. **Time & leakage:** training strictly before validation; no date ≥ 2018-08-01 in training; lag features from the past only (e.g. lag-1 = previous day's turnover).
4. **Content & baseline:** group 6 only in Oct–Jan; weekdays ordered Mon–Sun; MAPE of the last-week rule is computed and plausible (> 0 %).

---

## Evidence and action

### 9. Experiments 🤖
<!-- Experiment cards and their status; best result so far vs. baseline. Link experiments/LOG.md. -->

### 10. Findings 🤖
<!-- What we learned, how sure we are, and what the data cannot tell. -->
- **Hypothesis 1 (warm & dry → croissants): partly supported** (draft, 2026-11-24, [`katharina-warm.ipynb`](1_DatasetCharacteristics/katharina-warm.ipynb)). Raw link with temperature is strong (Spearman 0.65; ~110 € below 5 °C vs. 261 € at ≥ 25 °C), but mostly season: within the same month and weekday it shrinks to rho 0.13 (days > 4 °C warmer than the month's average: ~+6.6 % vs. a typical comparable day). "Dry" not supported: at equal temperature rainy days are not lower (from 15 °C even higher); season-adjusted difference only 1.3 %-points, reversed in summer. Limits: observed weather, one daily rain code, 6 summers, exploration used all 2013–2018 data.

### 11. Recommendation 👤
<!-- What the decision-maker should do, under which conditions. Signed off by the team. -->

---

## Open questions
<!-- Parking lot. Each item names who resolves it. -->
- **Staffing:** could the same forecast support staff planning? Parked; later use. *Resolves: team.*
- **Current practice:** how does the branch decide baking quantities today without a model? Unknown; the naive rule "same weekday last week" serves as stand-in reference (block 4). *Resolves: team, if instructors can tell.*
- **Rain / dry for hypotheses 1 and 3:** these need `Wettercode`, which was decided not to be used (DECISIONS 2026-11-23). Use it after all (e.g. as a simple rain yes/no flag, missing = no notable weather), or test with `Bewoelkung` as a rough stand-in? For hypothesis 1, a rain flag was tried in exploration only (DECISIONS 2026-11-24) and showed no clear effect on croissants. *Resolves: team.*
- **Data split:** how to split training / validation (by time, test period Aug 2018 – Jul 2019 set by the course). *Resolves: team, before the first model.*

## Decision log
See `DECISIONS.md`.
