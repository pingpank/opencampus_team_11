# Glossary

One entry per term, variable or code the project uses. Keep the canonical name, the meaning, the unit and anything that is easy to get wrong.

| Term | Meaning | Unit / values | Notes |
|---|---|---|---|
| Umsatz (turnover) | Turnover of one product group in the branch on one day | € (float) | Not pieces; on sold-out days it understates demand. Target of the forecast. |
| Warengruppe (product group) | Product category | 1 Bread, 2 Rolls, 3 Croissant, 4 Confectionery, 5 Cake, 6 Seasonal bread | Group 6 only sold late Oct – Jan (4 seasons in data). |
| Datum | Calendar day of the sale | date, 2013-07-01 – 2018-07-31 | 38 days without any sales (holidays, likely closed). |
| MAPE | Mean Absolute Percentage Error: average of \|forecast − actual\| / actual | % | Course metric; computed per product group. Over- and under-forecasting count equally. |
| Naive baseline ("last-week rule") | Forecast for t+1 = turnover of the same group on the same weekday one week earlier (t+1−7) | € | Stand-in for the unknown current practice. |
| Known in advance | Information available at closing time of day t | – | See canvas block 6; everything else is leakage. |
| Forecast horizon | How far ahead the forecast is made | 1 day | Made at closing time for the next day. |
