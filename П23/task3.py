import sys

from exporters import Exporter, HtmlExporter
from expense import load_expenses

CSV_PATH = "data/expenses.csv"


class IncompleteHtmlExporter(Exporter):
    """Реалізує лише extension() — export() відсутній."""

    def extension(self):
        return "html"


def main():
    print("Pavlo Dranytskyi, IT-31")
    try:
        IncompleteHtmlExporter()
    except TypeError as error:
        print("error:", error)

    try:
        expenses = load_expenses(CSV_PATH)
        exporter = HtmlExporter()      # повна реалізація з exporters.py
        path = exporter.target("report")
        exporter.export(expenses, path)
    except OSError as e:
        print(f"I/O error: {e}", file=sys.stderr)
        sys.exit(1)
    print(f"saved: {path} ({len(expenses)} records)")


if __name__ == "__main__":
    main()
