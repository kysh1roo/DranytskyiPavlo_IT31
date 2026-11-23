import json
from datetime import date
from pathlib import Path

OWNER = "Pavlo Dranytskyi"
GROUP = "IT-31"
BASE_DIR = Path(__file__).resolve().parent
SOURCE_PATH = BASE_DIR / "data" / "expenses.json"
OUTPUT_PATH = BASE_DIR / "data" / "expenses_updated.json"

def main():
    print(f"{OWNER}, {GROUP}")

    with SOURCE_PATH.open("r", encoding="utf-8") as file:
        records = json.load(file)

    new_record = {
        "date": date.today().isoformat(),
        "category": "food",
        "amount": 150.0,
        "comment": "Added test expense"
    }
    records.append(new_record)
    added = 1

    filtered_records = [record for record in records if float(record["amount"]) >= 10]
    deleted = len(records) - len(filtered_records)

    with OUTPUT_PATH.open("w", encoding="utf-8") as file:
        json.dump(filtered_records, file, indent=2, ensure_ascii=False)

    print(f"added: {added}")
    print(f"deleted (amount < 10): {deleted}")
    print(f"saved: data/expenses_updated.json ({len(filtered_records)} records)")

if __name__ == "__main__":
    main()
