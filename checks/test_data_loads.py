"""Starter check: the main sales dataset can be loaded and has the expected columns.

Run all checks with:  uv run pytest checks
"""

import pandas as pd

BASE_URL = "https://raw.githubusercontent.com/opencampus-sh/intro-to-data-science-and-ml/main/data/bakery/"


def test_sales_data_loads():
    sales = pd.read_csv(BASE_URL + "umsatzdaten_gekuerzt.csv")
    assert len(sales) > 0
    assert {"Datum", "Warengruppe", "Umsatz"}.issubset(sales.columns)
