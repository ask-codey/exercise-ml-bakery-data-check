# Exercise: Bakery Data Check

Exercise code for the lesson **Exercise: Bakery Data Check** in the Machine Learning with Python course on [ask-codey.com](https://www.ask-codey.com).

Before a model can learn anything, two things have to be right: the toolkit installed at the versions the course uses, and the data loading the way you expect. Sunrise Bakery has 120 days of bread sales in `bakery_days.csv`. You'll write three small functions in `check.py`: one that reports the version of each package you installed, one that loads the bakery's days into a table, and one that counts the table's rows and columns. Tests call each function and check what it returns.

## What's here

- `bakery_days.csv`: the 120 days, our own made-up data: each day's `day` number, `weekday`, `high_temp_f` (the day's high, in °F), `is_holiday` (1 on a holiday, 0 otherwise) and `loaves_sold`. The lessons, the tests and `report.py` all read this file. Ready to use.
- `seed_data.py`: the script that made `bakery_days.csv`, so you can see how the data was built and the pattern planted in it. You don't need to run it: NumPy doesn't promise the same random numbers from a seed on every version, so the CSV, not the script, is what keeps everyone's numbers the same. Ready to use.
- `check.py`: the three functions, `toolkit_versions`, `load_days` and `count_days`. Each one stops with `NotImplementedError: Not built yet.` for now. The docstring under each says what it should do, with examples. For you to finish.
- `explore.ipynb`: a notebook for looking at the days and trying your functions as you write them. The tests don't read it. Ready to use, and yours to change.
- `report.py`: runs your three functions and prints what each one gave, so you can see them at work. Ready to use.
- `tests/test_check.py`: tests that call your functions and check what comes back. You don't need to change this file.
- `tests/conftest.py`: gives each test that needs it a fresh copy of the 120 days from `bakery_days.csv`. Ready to use.
- `requirements.txt`: the packages this exercise needs, each at an exact version: scikit-learn, pandas, NumPy, matplotlib, ipykernel (so VS Code can run the notebook) and pytest. Ready to use.
- `pytest.ini`: tells pytest where the tests are and where to find `check.py`. Ready to use.
- `.gitignore`: tells Git to leave out the virtual environment and the files Python, pytest and the notebook make as they run. Ready to use.

## Before you start

The packages go in a virtual environment: a private set of packages for this folder only. In VS Code's terminal, in this folder, run these three commands.

On Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

On a Mac (zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- The first command makes the virtual environment, in a folder named `.venv`.
- The second turns it on for this terminal: the prompt starts with `(.venv)` from then on.
- The third installs the packages `requirements.txt` lists into it, at exactly the versions it names. It takes a minute or two and ends with a line that starts `Successfully installed`.

*Virtual Environments and pip* explains all three, and *Installing the Machine Learning Toolkit* says what each package is for. The `.venv` folder is in `.gitignore`, so Git leaves it out: these commands make it again on any computer.

If PowerShell answers that running scripts is disabled on this system, run this once, then run the second command again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Each new terminal starts with the virtual environment off. If the prompt doesn't start with `(.venv)`, run the second command again. (VS Code often turns it on for you.)

To check the install, run this (it prints scikit-learn's version, then the versions of everything it uses):

```bash
python -c "import sklearn; sklearn.show_versions()"
```

To look at the days, open `explore.ipynb`, choose the `.venv` kernel with **Select Kernel** (top right), and run the cells.

## Check your work

```bash
python -m pytest
```

- `python -m pytest` runs pytest with the virtual environment's Python, so the tests see the packages you just installed.

At first every test fails: that is expected, because each function stops with a `NotImplementedError` for now. Each function you finish turns its tests green. A failing test's message says what it called, what it expected and what came back, for example *count_days(the 120 bakery days) should return {'days': 120, 'columns': 5}, but it returned {'days': 5, 'columns': 120}.*

The version tests compare what your Python really has installed with the versions `requirements.txt` pins. If one of them fails after you've written `toolkit_versions`, check that the prompt starts with `(.venv)` and run `pip install -r requirements.txt` again.

To see your functions at work, run:

```bash
python report.py
```

## The rules

- Keep each function's name and parameters as they are.
- Return each answer; don't only print it.
- In `load_days`, read the file at the `path` you're given, not a file name of your own.
- Don't change the tests, `conftest.py`, `bakery_days.csv`, `seed_data.py`, `requirements.txt` or `report.py`.

## Tips

- Try each step in `explore.ipynb` first, then move the lines that work into `check.py`.
- Every package has a `__version__`: `sklearn.__version__` is scikit-learn's.
- A table's `.shape` is its number of rows and its number of columns, in that order.
- After you change `check.py`, restart the notebook's kernel before you try it there, so the notebook imports your newest code.

## Hand it in

When it works, push your solution to a public repo of your own on GitHub, then paste that repo's address into **Submit your exercise** on the lesson page at [ask-codey.com](https://www.ask-codey.com). That's what completes the lesson. The lesson page shows the Git commands, step by step, for a cloned copy and for a downloaded ZIP.
