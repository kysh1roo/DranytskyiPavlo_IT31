import csv
import json
from pathlib import Path

OWNER = "Pavlo Dranytskyi"
GROUP = "IT-31"
BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "data" / "expenses.csv"
JSON_PATH = BASE_DIR / "data" / "expenses.json"

def main():
    print(f"{OWNER}, {GROUP}")

    records = []
    with CSV_PATH.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            records.append({
                "date": row["date"],
                "category": row["category"],
                "amount": float(row["amount"]),
                "comment": row["comment"]
            })

    with JSON_PATH.open("w", encoding="utf-8") as file:
        json.dump(records, file, indent=2, ensure_ascii=False)

    size = JSON_PATH.stat().st_size
    print(f"records: {len(records)}")
    print(f"saved: data/expenses.json ({size} bytes)")

if __name__ == "__main__":
    main()
