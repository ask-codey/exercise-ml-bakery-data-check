# Checks the toolkit and the bakery's data with your three functions from check.py, and prints what each one gave,
# so you can see them at work. Ready to use.
# Run it with: python report.py
from check import count_days, load_days, toolkit_versions

versions = toolkit_versions()
for number, package in enumerate(["scikit-learn", "pandas", "numpy", "matplotlib", "ipykernel"], start=1):
    print(f"{number}) {package}:", versions[package])

days = load_days("bakery_days.csv")
counts = count_days(days)
print("6) days:", counts["days"])
print("7) columns:", counts["columns"])
print("8) column names:", list(days.columns))
print("9) loaves sold on the first three days:", days["loaves_sold"].head(3).tolist())
