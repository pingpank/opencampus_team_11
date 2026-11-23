# Glossary

One entry per term, variable or code the project uses. Keep the canonical name, the meaning, the unit and anything that is easy to get wrong.

| Term | Meaning | Unit / values | Notes |
|---|---|---|---|
| Umsatz (turnover) | Turnover of one product group in the branch on one day | € (float) | Not pieces; on sold-out days it understates demand. Target of the forecast. |
| Warengruppe (product group) | Product category | 1 Bread, 2 Rolls, 3 Croissant, 4 Confectionery, 5 Cake, 6 Seasonal bread | Group 6 only sold late Oct – early Jan (5 seasons in data). |
| id | Row key of the sales file | YYMMDD·10 + Warengruppe (e.g. 1307011) | Redundant with Datum + Warengruppe; not a feature. |
| Bewoelkung | Mean cloud cover | octas, 0 = clear … 8 = overcast | Observed, not forecast. |
| Temperatur | Mean daily temperature in Kiel | °C | Observed, not forecast. |
| Windgeschwindigkeit | Mean wind speed | m/s | Observed, not forecast. |
| Wettercode | WMO present-weather code | 00–99 (41 distinct values in data) | Missing on 669 days, most likely "no notable weather"; not missing at random. |
| KielerWoche | Kiel Week day flag | 1 = Kiel Week day, 0 = not (set after merge) | 9 days per year; known well in advance. |
| Season (group 6) | Period in which seasonal bread is sold | late Oct – early Jan | Start varies by ~10 days between years. |
| Datum | Calendar day of the sale | date, 2013-07-01 – 2018-07-31 | 38 days without any sales (holidays, likely closed). |
| MAPE | Mean Absolute Percentage Error: average of \|forecast − actual\| / actual | % | Course metric; computed per product group. Over- and under-forecasting count equally. |
| Naive baseline ("last-week rule") | Forecast for t+1 = turnover of the same group on the same weekday one week earlier (t+1−7) | € | Stand-in for the unknown current practice. If that day has no value, go back further in steps of one week. |
| Known in advance | Information available at closing time of day t | – | See canvas block 6; everything else is leakage. |
| Forecast horizon | How far ahead the forecast is made | 1 day | Made at closing time for the next day. |
