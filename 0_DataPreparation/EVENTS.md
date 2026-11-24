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

| Tag    | Event | Days marked | Source | Open in sales period | Added |
|--------|-------|-------------|--------|----------------------|-------|
| `kiwo` | Kieler Woche (Kiel Week), the sailing festival in June | Every festival day, 9 days per year, 2012–2019 (72 rows) | Course file [`kiwo.csv`](https://raw.githubusercontent.com/opencampus-sh/intro-to-data-science-and-ml/main/data/bakery/kiwo.csv), all rows with `KielerWoche = 1` | 100% (45/45) | 2026-11-24, Thore Pingpank |
| `holiday_neujahr` | Neujahr (New Year's Day), 1 Jan | 1 day per year, 2012–2019 | See *Holidays and special days* below | 0% (0/5) | 2026-11-24, Thore Pingpank |
| `holiday_karfreitag` | Karfreitag (Good Friday), Easter Sunday − 2 days | 1 day per year, 2012–2019 | See *Holidays and special days* below | 0% (0/5) | 2026-11-24, Thore Pingpank |
| `holiday_ostermontag` | Ostermontag (Easter Monday), Easter Sunday + 1 day | 1 day per year, 2012–2019 | See *Holidays and special days* below | 100% (5/5) | 2026-11-24, Thore Pingpank |
| `holiday_maifeiertag` | Tag der Arbeit (Labour Day), 1 May | 1 day per year, 2012–2019 | See *Holidays and special days* below | 20% (1/5) | 2026-11-24, Thore Pingpank |
| `holiday_himmelfahrt` | Christi Himmelfahrt (Ascension Day), Easter Sunday + 39 days | 1 day per year, 2012–2019 | See *Holidays and special days* below | 100% (5/5) | 2026-11-24, Thore Pingpank |
| `holiday_pfingstmontag` | Pfingstmontag (Whit Monday), Easter Sunday + 50 days | 1 day per year, 2012–2019 | See *Holidays and special days* below | 80% (4/5) | 2026-11-24, Thore Pingpank |
| `holiday_einheit` | Tag der Deutschen Einheit (German Unity Day), 3 Oct | 1 day per year, 2012–2019 | See *Holidays and special days* below | 100% (5/5) | 2026-11-24, Thore Pingpank |
| `holiday_reformationstag` | Reformationstag (Reformation Day), 31 Oct | 2017 (one-off nationwide holiday) and every year from 2018 (new SH holiday); not 2012–2016 | See *Holidays and special days* below | 0% (0/1) | 2026-11-24, Thore Pingpank |
| `holiday_weihnachten_1` | 1. Weihnachtstag (Christmas Day), 25 Dec | 1 day per year, 2012–2019 | See *Holidays and special days* below | 0% (0/5) | 2026-11-24, Thore Pingpank |
| `holiday_weihnachten_2` | 2. Weihnachtstag (Boxing Day), 26 Dec | 1 day per year, 2012–2019 | See *Holidays and special days* below | 0% (0/5) | 2026-11-24, Thore Pingpank |
| `special_heiligabend` | Heiligabend (Christmas Eve), 24 Dec; not a public holiday | 1 day per year, 2012–2019 | See *Holidays and special days* below | 100% (5/5) | 2026-11-24, Thore Pingpank |
| `special_silvester` | Silvester (New Year's Eve), 31 Dec; not a public holiday | 1 day per year, 2012–2019 | See *Holidays and special days* below | 100% (5/5) | 2026-11-24, Thore Pingpank |
| `special_ostersonntag` | Ostersonntag (Easter Sunday); not a public holiday in SH | 1 day per year, 2012–2019 | See *Holidays and special days* below | 100% (5/5) | 2026-11-24, Thore Pingpank |
| `special_pfingstsonntag` | Pfingstsonntag (Whit Sunday), Easter Sunday + 49 days; not a public holiday in SH | 1 day per year, 2012–2019 | See *Holidays and special days* below | 100% (5/5) | 2026-11-24, Thore Pingpank |

### Holidays and special days (`holiday_*`, `special_*`)

- All statutory public holidays in Schleswig-Holstein, 2012-01-01 to 2019-12-31: 75 days (9 per year, 10 in 2017–2019).
- Each holiday has its own tag, all starting with `holiday_`. That keeps the detail (Christmas may matter differently from Ascension Day). One "any holiday" flag can be built later with `tag.str.startswith("holiday_")`.
- `special_*`: days that are not statutory holidays but may change sales strongly: Christmas Eve, New Year's Eve, Easter Sunday and Whit Sunday (2012–2019, 32 days). Kept apart from `holiday_*` so an "any public holiday" flag stays clean.
- **Open in sales period:** share of tagged days inside the sales period (2013-07-01 – 2018-07-31) that have at least one row in `umsatzdaten_gekuerzt.csv`. A day without any row is taken as "bakery closed". Computed 2026-11-24.
- How the dates were made: fixed dates plus the Easter dates computed with `dateutil.easter`. The `holiday_*` dates were cross-checked against the [Nager.Date public holiday API](https://date.nager.at/api/v3/PublicHolidays/2019/DE) (entries valid for all of Germany or for `DE-SH`, years 2012–2019). Both lists match exactly.

## How to add an event

1. Add a row to the table above: tag name, what the event is, which days count, where the dates come from (link), date and your name.
2. Append the dates to `events.csv` as `Datum,tag` rows (one row per day). Cover the training period *and* the test period.
3. Only add events whose dates are **known in advance** (see DECISIONS.md, 2026-11-17). Example: a public holiday or a planned festival is fine; "a day with unusually high sales" is not.
