"""Check (canvas block 8, group 1 "raw data"): the sales file has exactly one row
per date and product group, i.e. the key (Datum, Warengruppe) is unique.

Why it matters: a duplicated day/group would be counted twice in every sum,
mean and model, and joins on Datum would silently multiply rows.

Run all checks with:  uv run pytest checks
"""

import pandas as pd

BASE_URL = "https://raw.githubusercontent.com/opencampus-sh/intro-to-data-science-and-ml/main/data/bakery/"
KEY = ["Datum", "Warengruppe"]


def duplicated_keys(df: pd.DataFrame) -> pd.DataFrame:
    """Return all rows whose (Datum, Warengruppe) appears more than once."""
    return df[df.duplicated(subset=KEY, keep=False)].sort_values(KEY)


def test_one_row_per_date_and_group():
    sales = pd.read_csv(BASE_URL + "umsatzdaten_gekuerzt.csv")
    dupes = duplicated_keys(sales)
    assert dupes.empty, f"{len(dupes)} rows share a (Datum, Warengruppe) key:\n{dupes.head(10)}"


def test_check_detects_a_duplicate():
    """The check itself must catch a duplicate, otherwise a passing result means nothing."""
    toy = pd.DataFrame({
        "Datum": ["2013-07-01", "2013-07-01", "2013-07-01"],
        "Warengruppe": [1, 2, 1],  # group 1 appears twice on the same day
        "Umsatz": [100.0, 200.0, 100.0],
    })
    assert len(duplicated_keys(toy)) == 2
