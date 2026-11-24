"""Checks for the DWD weather file 0_DataPreparation/dwd_weather.csv (made by dwd_weather.ipynb).

Run all checks with:  uv run pytest checks
"""

from pathlib import Path

import pandas as pd

DWD_CSV = Path(__file__).resolve().parent.parent / "0_DataPreparation" / "dwd_weather.csv"
TRAIN = ("2013-07-01", "2018-07-31")
TEST = ("2018-08-01", "2019-07-31")


def load():
    return pd.read_csv(DWD_CSV, parse_dates=["Datum"])


def test_columns():
    assert list(load().columns) == [
        "Datum", "Niederschlag_mm", "Niederschlagsform", "Sonnenschein_h", "Bewoelkung_dwd",
        "Temperatur_dwd", "Temperatur_max", "Temperatur_min", "Luftfeuchte",
        "Wind_mittel", "Wind_boe_max", "Luftdruck", "Schneehoehe_cm",
    ]


def test_dates_unique_and_in_range():
    dwd = load()
    assert dwd["Datum"].is_unique
    assert dwd["Datum"].min() >= pd.Timestamp("2012-01-01")
    assert dwd["Datum"].max() <= pd.Timestamp("2019-08-01")


def test_every_day_of_training_and_test_period_present():
    days = set(load()["Datum"])
    expected = set(pd.date_range(TRAIN[0], TEST[1]))
    assert expected <= days, sorted(expected - days)[:10]


def test_rain_and_temperature_complete_in_training_and_test():
    dwd = load()
    period = dwd[dwd["Datum"].between(TRAIN[0], TEST[1])]
    for col in ["Niederschlag_mm", "Temperatur_dwd", "Temperatur_max", "Temperatur_min"]:
        assert period[col].notna().all(), col


def test_sunshine_gap_only_known_one():
    # Sunshine is complete in training; in the test period it is missing only from 2019-05-05 on (88 days)
    dwd = load()
    empty = dwd.loc[dwd["Datum"].between(TRAIN[0], TEST[1]) & dwd["Sonnenschein_h"].isna(), "Datum"]
    assert (empty >= pd.Timestamp("2019-05-05")).all()
    assert len(empty) == 88


def test_value_ranges_plausible():
    dwd = load()
    assert dwd["Niederschlag_mm"].dropna().between(0, 150).all()
    assert dwd["Sonnenschein_h"].dropna().between(0, 18).all()      # Kiel: at most ~17 h of daylight
    assert dwd["Bewoelkung_dwd"].dropna().between(0, 8).all()       # eighths
    assert dwd["Temperatur_dwd"].dropna().between(-25, 35).all()
    both = dwd.dropna(subset=["Temperatur_min", "Temperatur_max"])
    assert (both["Temperatur_min"] <= both["Temperatur_max"]).all()
