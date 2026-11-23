import sys

from exporters import CsvExporter, HtmlExporter, JsonExporter, TxtExporter
from expense import load_expenses

CSV_PATH = "data/expenses.csv"

# Новий формат = новий клас + один рядок тут.
EXPORTERS = {
    "csv": CsvExporter(),
    "json": JsonExporter(),
    "txt": TxtExporter(),
    "html": HtmlExporter(),
}


def main():
    available = ", ".join(sorted(EXPORTERS))
    if len(sys.argv) != 2 or sys.argv[1] not in EXPORTERS:
        asked = sys.argv[1] if len(sys.argv) == 2 else "(none)"
        print(f"Unknown format: {asked}. Available formats: {available}",
              file=sys.stderr)
        sys.exit(2)

    exporter = EXPORTERS[sys.argv[1]]
    try:
        expenses = load_expenses(CSV_PATH)
        path = exporter.target("report")
        exporter.export(expenses, path)
    except OSError as e:
        print(f"I/O error: {e}", file=sys.stderr)
        sys.exit(1)

    print("Pavlo Dranytskyi, IT-31")
    print(f"saved: {path} ({len(expenses)} records)")


if __name__ == "__main__":
    main()
