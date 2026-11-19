"""Makes bakery_days.csv: 120 made-up days of bread sales at Sunrise Bakery.

Ready to use; you don't need to run it. The CSV it made is already in this folder,
and the lessons, the tests and report.py all read that file.

Every number in the file is made up, and the pattern is built in on purpose, so you
can check whether a guess finds it. A real dataset's pattern is what you're trying
to find; this one is planted:

    loaves_sold = 90 on a weekday (Monday to Friday)
                  135 on a Saturday
                  120 on a Sunday
                  + 25 on a holiday
                  - 0.8 for each degree the day's high is above 85°F
                  + a random wobble (a standard deviation of 8 loaves)
    then rounded to a whole number of loaves.

The days are in time order: day 1 is a Monday, and day 120 is the last day in the
file. The weather warms up through the summer and cools off again at the end.

The random numbers come from a fixed seed, 101, so this script makes the same file
every time on the same version of NumPy. NumPy doesn't promise the same random
numbers from a seed across its versions (NEP 19), so the CSV in this folder, not
this script, is what keeps every learner's numbers the same.
"""
import csv
import math

import numpy as np

SEED = 101
DAYS = 120
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
USUAL_LOAVES = {"Saturday": 135, "Sunday": 120}  # every other day: 90
HOLIDAYS = [8, 36, 64, 113]  # the day numbers of the four holidays in the file


def make_days(seed=SEED, count=DAYS):
    """Return the made-up days as a list of dictionaries, one per day, in time order."""
    rng = np.random.default_rng(seed)
    days = []
    for number in range(1, count + 1):
        weekday = WEEKDAYS[(number - 1) % 7]
        season = 74 + 14 * math.sin(math.pi * number / count)
        high_temp_f = round(float(season + rng.normal(0, 5)))
        is_holiday = 1 if number in HOLIDAYS else 0
        loaves = USUAL_LOAVES.get(weekday, 90) + 25 * is_holiday
        loaves -= 0.8 * max(0, high_temp_f - 85)
        loaves += rng.normal(0, 8)
        days.append({
            "day": number,
            "weekday": weekday,
            "high_temp_f": high_temp_f,
            "is_holiday": is_holiday,
            "loaves_sold": round(float(loaves)),
        })
    return days


if __name__ == "__main__":
    days = make_days()
    with open("bakery_days.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(days[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(days)
    print("Wrote bakery_days.csv:", len(days), "days.")
