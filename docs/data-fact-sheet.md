# Data fact sheet

Profiled on 2026-11-23 from `https://raw.githubusercontent.com/opencampus-sh/intro-to-data-science-and-ml/main/data/bakery/`.
All numbers below come from running the profiling code; nothing is estimated.

**Origin:** provided by meteolytix GmbH (former Kiel company producing sales forecasts for bakeries), via the opencampus.sh course ([documentation](https://github.com/opencampus-sh/intro-to-data-science-and-ml/blob/main/data/bakery/README.md)). **License:** not stated.
**Test period:** 2018-08-01 – 2019-07-31 is held back by the course (Kaggle competition); no sales data for it here.

---

## 1. `umsatzdaten_gekuerzt.csv` – sales

- **Shape / grain:** 9,334 rows × 4 columns (`id`, `Datum`, `Warengruppe`, `Umsatz`). One row = one product group on one day, **only for days with sales**.
- **Keys:** (`Datum`, `Warengruppe`) is unique (0 duplicates). `id` is unique and equals `YYMMDD·10 + Warengruppe` for 100 % of rows (it carries no extra information).
- **Time coverage:** 2013-07-01 – 2018-07-31 = 1,857 calendar days, 1,819 with sales. Both edges are complete days. Rows are spread evenly over all seven weekdays (1,311–1,345 each) → shop open every day of the week.
- **Missing values:** none in any column.
- **Days without any sales (38):** mostly public holidays:
  2013-12-25, 12-26, 12-28; 2014-01-01, 04-18, 05-01, 05-03, 05-04, 08-17, 12-25, 12-26; 2015-01-01, 04-03, 05-01, 12-25, 12-26; 2016-01-01, 03-24, 03-25, 07-07, 07-18, 08-14, 08-15, 12-17, 12-25, 12-26; 2017-01-01, 04-14, 05-01, 07-04, 10-23, 10-31, 12-25, 12-26; 2018-01-01, 03-30, 05-01, 05-21.
- **`Umsatz` (turnover):** 7.05 – 1,879.46, median 161.9, no zero or negative values. Currency not stated in the source (assumed €).

| Group | Rows | Median | 1 % | 99 % | Max |
|---|---|---|---|---|---|
| 1 Bread | 1,819 | 120.1 | 43.4 | 234.2 | 416.8 |
| 2 Rolls | 1,819 | 370.8 | 204.2 | 773.3 | 1,203.4 |
| 3 Croissant | 1,819 | 142.8 | 63.0 | 382.3 | 565.9 |
| 4 Confectionery | 1,766 | 80.0 | 38.7 | 213.2 | 430.5 |
| 5 Cake | 1,819 | 266.0 | 156.5 | 469.4 | 1,879.5 |
| 6 Seasonal bread | 292 | 62.9 | 16.8 | 155.0 | 172.9 |

- **Extreme values:** the five highest turnovers are all group 5 on **31 December** (2013–2017: 1,432 – 1,879), about 5–7× the group median. They recur every year.
- **Group 4 gaps:** 53 days on which other groups sold but group 4 has no row. All between 2013-07-12 and 2016-07-26 (2013: 16, 2014: 23, 2015: 10, 2016: 4; none after July 2016). Most in December (16) and July (11); spread over all weekdays. It is unknown whether these are days with zero confectionery sales or missing records.
- **Group 6 seasons:** sold only late October to early January, 5 seasons:

| Season | First day | Last day | Days |
|---|---|---|---|
| 2013/14 | 2013-10-24 | 2014-01-02 | 65 |
| 2014/15 | 2014-10-24 | 2015-01-06 | 66 |
| 2015/16 | 2015-11-02 | 2015-12-31 | 53 |
| 2016/17 | 2016-11-03 | 2016-12-29 | 52 |
| 2017/18 | 2017-10-30 | 2017-12-27 | 56 |

  The season start varies by ~10 days between years.

## 2. `wetter.csv` – weather (Kiel, observed)

- **Shape / grain:** 2,601 rows × 5 columns. One row = one day. `Datum` unique.
- **Time coverage:** 2012-01-01 – 2019-08-01 = 2,770 calendar days; **169 days have no row** (2012: 33, 2013: 120, 2016: 1, 2017: 2, 2018: 12, 2019: 1). Of these, 3 fall into the sales period (1 in 2016, 2 in 2017) and **13 into the test period** (352 of 365 test days covered).
- **Columns:**

| Column | Meaning | Range | Missing |
|---|---|---|---|
| `Bewoelkung` | mean cloud cover, octas (0 clear – 8 overcast) | 0 – 8 | 10 (all in 2017) |
| `Temperatur` | mean temperature, °C | −10.25 – 32.67 | 0 |
| `Windgeschwindigkeit` | mean wind speed, m/s | 3 – 35 | 0 |
| `Wettercode` | WMO present-weather code (00–99), 41 distinct values | 0 – 95 | **669** (all years; 55 in test period) |

- **Missing `Wettercode` is not random:** on days without a code, mean cloud cover is 3.29 vs 5.32 and mean temperature 15.4 °C vs 10.9 °C. Matches the documentation: missing most likely means "no notable weather reported".
- **Observed, not forecast:** at prediction time only the weather forecast would be known (see canvas block 6).

## 3. `kiwo.csv` – Kiel Week

- **Shape / grain:** 72 rows × 2 columns, one row per Kiel Week day; `KielerWoche` is always 1. `Datum` unique.
- **Coverage:** 9 days per year, 2012–2019. Within the sales period: **5 Kiel Weeks** (2014–2018, 45 days, all with sales). Kiel Week 2013 (06-22 – 06-30) ends before the sales data start. Kiel Week 2019 lies in the test period.
- Non-Kiel-Week days must be set to 0 after the merge.

## 5. `0_DataPreparation/dwd_weather.csv` – DWD weather (Kiel-Holtenau, added 2026-11-24)

- **Source:** German Weather Service (DWD), daily climate data, station Kiel-Holtenau (02564), quality-controlled historical record ([directory](https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/historical/)); licence CC BY 4.0 (name DWD as source). Made by `0_DataPreparation/dwd_weather.ipynb`; checks in `checks/test_dwd_weather.py`.
- **Shape / grain:** 2,631 rows × 13 columns, one row per day, `Datum` unique, 2012-01-01 – 2019-08-01. Column meanings and units: see the notebook.
- **Same place as `wetter.csv`:** correlation of daily temperature 0.987, of cloud cover 0.887 (2,599 common days).
- **Coverage:** every day of the training and test period has a row. **Rain (`Niederschlag_mm`) and temperature: no gaps** in training or test. Sunshine (`Sonnenschein_h`): complete in training, **missing from 2019-05-05 on (88 test days)** – DWD stopped measuring sunshine at this station. Cloud cover: empty on 11 training days (2017-10-30 – 11-09) and 25 test days. Before the sales period a block 2012-12-21 – 2013-04-30 is missing (no effect on the model). Snow depth mostly empty – do not use unchecked.
- **Rain is measured 06:00 UTC on the day to 06:00 UTC next day** – it includes the night after closing.
- **What `Wettercode` missing means (compared with DWD, 2026-11-24):** not "clear sky". On the 669 missing-code days DWD shows mean cloud cover 3.6 eighths, only 19 % fully clear (≤ 1/8), and rain on 23 % (154 days; 20 days > 5 mm). Compared month by month, these days are almost identical to days with codes 00–03 (dry 77 % vs 75 %, cloud 3.6 vs 3.6, sunshine 8.0 vs 8.0 h). So missing ≈ "no notable weather at observation time", not "dry".

## 4. Joins (left join on `Datum`, sales as the base)

- **Sales + weather:** 1,816 of 1,819 sales days have a weather row (3 without: 1 in 2016, 2 in 2017). Row count stays 9,334 → 9,334.
- **Sales + Kiel Week:** row count stays 9,334 → 9,334; 45 of 72 Kiel Week days match (the others lie outside the sales period).
