# Event calendar

`events.csv` (in this folder) collects special days that may affect bakery sales. It covers the whole project period: the training data (from 2013-07-01) **and** the test period of the course contest (2018-08-01 – 2019-07-31).

## Format

One row per day **and** event, in long format:

| Column  | Meaning                                                     |
|---------|-------------------------------------------------------------|
| `Datum` | Date as `YYYY-MM-DD` (same name and format as in the course files, so it joins directly) |
| `tag`   | Short lowercase name of the event; must be listed in the table below |

- A day with two events gets two rows (for example `2019-06-22,kiwo` and `2019-06-22,something_else`).
- Only days *with* an event are listed. A day that is not in the file has no event.
- Rows are sorted by date; the order of rows does not matter for analysis.
- No dummy coding here. Turning tags into model features (for example a 0/1 column per tag, or flags for the days *before* an event) happens later, in the feature step.

## Tags

| Tag    | Event | Days marked | Source | Added |
|--------|-------|-------------|--------|-------|
| `kiwo` | Kieler Woche (Kiel Week), the sailing festival in June | Every festival day, 9 days per year, 2012–2019 (72 rows) | Course file [`kiwo.csv`](https://raw.githubusercontent.com/opencampus-sh/intro-to-data-science-and-ml/main/data/bakery/kiwo.csv), all rows with `KielerWoche = 1` | 2026-11-24, Thore Pingpank |

## How to add an event

1. Add a row to the table above: tag name, what the event is, which days count, where the dates come from (link), date and your name.
2. Append the dates to `events.csv` as `Datum,tag` rows (one row per day). Cover the training period *and* the test period.
3. Only add events whose dates are **known in advance** (see DECISIONS.md, 2026-11-17). Example: a public holiday or a planned festival is fine; "a day with unusually high sales" is not.
