# Shared set-up for the tests. You don't need to change this file.
# Each test that asks for days gets its own fresh copy of the 120 days in bakery_days.csv, read from this
# exercise's folder with pandas, so one test can't change the table another test reads.
from pathlib import Path

import pandas as pd
import pytest

BAKERY_DAYS = Path(__file__).parent.parent / "bakery_days.csv"


@pytest.fixture
def days():
    """The 120 days in bakery_days.csv, freshly read for one test."""
    return pd.read_csv(BAKERY_DAYS)
