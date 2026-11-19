# Tests for check.py. Run them with: python -m pytest (in the exercise folder, with the virtual environment active).
# Each test calls one of your functions, on the 120 days in bakery_days.csv or on a small table written in the test,
# and checks what comes back. A failing test says what it called, what it expected and what came back.
# The version tests compare what your Python really has installed with the versions requirements.txt pins, so they
# pass only in a virtual environment installed from this folder's requirements.txt.
# You don't need to change this file.
from pathlib import Path

import pandas as pd

from check import count_days, load_days, toolkit_versions

FOLDER = Path(__file__).parent.parent
TOOLKIT = ["scikit-learn", "pandas", "numpy", "matplotlib", "ipykernel"]


def check(call, got, expected):
    """Fails with a message that says what the call returned and what it should return."""
    assert got == expected, f"{call} should return {expected!r}, but it returned {got!r}."


def pinned_versions():
    """The exact versions requirements.txt pins, as a dictionary: {"scikit-learn": "1.9.1", ...}."""
    pins = {}
    for line in (FOLDER / "requirements.txt").read_text().splitlines():
        if "==" in line:
            name, version = line.split("==")
            pins[name.strip()] = version.strip()
    return pins


def write_csv(folder, text):
    """Writes a small CSV file for one test and returns its path."""
    path = folder / "small.csv"
    path.write_text(text)
    return path


# toolkit_versions

def test_1_toolkit_versions_has_a_key_for_each_of_the_five_packages():
    check("sorted(toolkit_versions())", sorted(toolkit_versions()), sorted(TOOLKIT))


def test_2_toolkit_versions_scikit_learn_is_the_pinned_1_9_1():
    check('toolkit_versions()["scikit-learn"]', toolkit_versions()["scikit-learn"], pinned_versions()["scikit-learn"])


def test_3_toolkit_versions_pandas_and_numpy_are_the_pinned_3_1_1_and_2_5_5():
    versions = toolkit_versions()
    check('toolkit_versions()["pandas"]', versions["pandas"], pinned_versions()["pandas"])
    check('toolkit_versions()["numpy"]', versions["numpy"], pinned_versions()["numpy"])


def test_4_toolkit_versions_matplotlib_and_ipykernel_are_the_pinned_3_11_2_and_7_4_0():
    versions = toolkit_versions()
    check('toolkit_versions()["matplotlib"]', versions["matplotlib"], pinned_versions()["matplotlib"])
    check('toolkit_versions()["ipykernel"]', versions["ipykernel"], pinned_versions()["ipykernel"])


# load_days

def test_5_load_days_bakery_days_csv_gives_a_table_of_120_rows_and_5_columns():
    days = load_days(FOLDER / "bakery_days.csv")
    assert isinstance(days, pd.DataFrame), \
        f"load_days should return a pandas table (a DataFrame), but it returned {type(days).__name__}."
    check('load_days("bakery_days.csv").shape', days.shape, (120, 5))


def test_6_load_days_keeps_the_csv_columns_in_order():
    days = load_days(FOLDER / "bakery_days.csv")
    check('list(load_days("bakery_days.csv").columns)', list(days.columns),
          ["day", "weekday", "high_temp_f", "is_holiday", "loaves_sold"])


def test_7_load_days_day_1_is_a_monday_that_sold_74_loaves():
    days = load_days(FOLDER / "bakery_days.csv")
    first = days.iloc[0]
    check("the first row's day, weekday and loaves_sold", [int(first["day"]), first["weekday"],
          int(first["loaves_sold"])], [1, "Monday", 74])


def test_8_load_days_reads_the_file_it_is_given_a_3_row_file_gives_3_rows(tmp_path):
    path = write_csv(tmp_path, "day,loaves_sold\n1,90\n2,135\n3,120\n")
    check("load_days(a file of 3 days and 2 columns).shape", load_days(path).shape, (3, 2))


# count_days

def test_9_count_days_on_the_bakery_table_gives_120_days_and_5_columns(days):
    check("count_days(the 120 bakery days)", count_days(days), {"days": 120, "columns": 5})


def test_10_count_days_on_a_3_row_2_column_table_gives_3_days_and_2_columns():
    days = pd.DataFrame({"day": [1, 2, 3], "loaves_sold": [90, 135, 120]})
    check("count_days(a table of 3 days and 2 columns)", count_days(days), {"days": 3, "columns": 2})
