"""Checks for the event calendar 0_DataPreparation/events.csv (documented in EVENTS.md).

Run all checks with:  uv run pytest checks
"""

import re
from pathlib import Path

import pandas as pd

FOLDER = Path(__file__).resolve().parent.parent / "0_DataPreparation"
EVENTS_CSV = FOLDER / "events.csv"
EVENTS_MD = FOLDER / "EVENTS.md"


def load_events():
    return pd.read_csv(EVENTS_CSV, dtype=str)


def test_events_columns():
    assert list(load_events().columns) == ["Datum", "tag"]


def test_events_dates_are_valid():
    events = load_events()
    assert events["Datum"].str.fullmatch(r"\d{4}-\d{2}-\d{2}").all()
    pd.to_datetime(events["Datum"], format="%Y-%m-%d")  # raises on impossible dates


def test_events_no_duplicate_rows():
    assert not load_events().duplicated(["Datum", "tag"]).any()


def test_every_tag_is_documented():
    tags_section = EVENTS_MD.read_text(encoding="utf-8").split("## Tags")[1].split("\n## ")[0]
    documented = set(re.findall(r"^\|\s*`([^`]+)`\s*\|", tags_section, re.M))
    used = set(load_events()["tag"])
    assert used <= documented, f"Tags missing in EVENTS.md: {used - documented}"


def test_kiwo_has_nine_days_per_year():
    kiwo = load_events().query("tag == 'kiwo'")
    per_year = kiwo["Datum"].str[:4].value_counts()
    assert (per_year == 9).all(), per_year


def test_holidays_per_year():
    # Schleswig-Holstein: 9 statutory holidays per year, plus Reformation Day from 2017 on
    holidays = load_events().query("tag.str.startswith('holiday_')", engine="python")
    per_year = holidays["Datum"].str[:4].astype(int).value_counts().sort_index()
    expected = {year: 10 if year >= 2017 else 9 for year in range(2012, 2020)}
    assert per_year.to_dict() == expected, per_year
    assert not holidays["Datum"].duplicated().any()  # one holiday tag per day


def test_special_days_once_per_year():
    # Christmas Eve, New Year's Eve, Easter Sunday, Whit Sunday: each once per year 2012-2019
    events = load_events()
    special = events[events["tag"].str.startswith("special_")]
    counts = special.groupby(["tag", special["Datum"].str[:4]]).size()
    assert len(counts) == 4 * 8 and (counts == 1).all(), counts
    assert special.query("tag == 'special_heiligabend'")["Datum"].str.endswith("-12-24").all()
    assert special.query("tag == 'special_silvester'")["Datum"].str.endswith("-12-31").all()
    weekdays = pd.to_datetime(special.query("tag in ['special_ostersonntag', 'special_pfingstsonntag']")["Datum"]).dt.dayofweek
    assert (weekdays == 6).all()  # both are Sundays
