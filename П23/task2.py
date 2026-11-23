import sys

from exporters import CsvExporter, JsonExporter, TxtExporter
from expense import load_expenses

CSV_PATH = "data/expenses.csv"


def main():
    try:
        expenses = load_expenses(CSV_PATH)
    except OSError as e:
        print(f"Cannot read {CSV_PATH}: {e}", file=sys.stderr)
        sys.exit(1)

    print("Pavlo Dranytskyi, IT-31")
    for exporter in (CsvExporter(), JsonExporter(), TxtExporter()):
        path = exporter.target("report")
        try:
            exporter.export(expenses, path)       # без перевірки типу експортера
        except OSError as e:
            print(f"Cannot write {path}: {e}", file=sys.stderr)
            sys.exit(1)
        print(f"saved: {path} ({len(expenses)} records)")


if __name__ == "__main__":
    main()
