"""Sunrise Bakery: three functions for you to finish.

The docstring under each function says what it should do, with examples.
Replace each raise NotImplementedError("Not built yet.") line with your own code.
Return each answer: the tests read what comes back, not what's printed.

The imports below are everything the three functions need. scikit-learn is
installed as scikit-learn but imported as sklearn.
"""
import ipykernel
import matplotlib
import numpy
import pandas as pd
import sklearn


def toolkit_versions():
    """Return the installed version of each of the five toolkit packages, as a dictionary.

    The keys are the names pip installs them by, the ones in requirements.txt:
    "scikit-learn", "pandas", "numpy", "matplotlib" and "ipykernel".
    Each value is that package's __version__, a string, read from the package
    this folder's Python imported (sklearn.__version__ for scikit-learn).

    In a virtual environment installed from this folder's requirements.txt:
    toolkit_versions()["scikit-learn"] -> "1.9.1"
    toolkit_versions()["pandas"]       -> "3.1.1"
    """
    raise NotImplementedError("Not built yet.")


def load_days(path):
    """Read the CSV file at path into a pandas table (a DataFrame), and return it.

    Use the path you're given, not a file name of your own: the tests call it
    with other files too.

    load_days("bakery_days.csv") -> a table of 120 rows and 5 columns:
    day, weekday, high_temp_f, is_holiday and loaves_sold
    """
    raise NotImplementedError("Not built yet.")


def count_days(days):
    """Return how many days (rows) and columns the table holds, as a dictionary.

    days is a table like the one load_days gives you. The keys are "days" and
    "columns", and each value is a whole number (int).

    With the 120 days in bakery_days.csv:
    count_days(days) -> {"days": 120, "columns": 5}
    """
    raise NotImplementedError("Not built yet.")
