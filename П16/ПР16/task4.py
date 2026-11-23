import json
from datetime import date
from pathlib import Path

OWNER = "Pavlo Dranytskyi"
GROUP = "IT-31"
BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DEFAULT = BASE_DIR / "date_default.json"
OUTPUT_CUSTOM = BASE_DIR / "date_custom.json"

def date_default(value):
    if isinstance(value, date):
        return value.isoformat()
    raise TypeError(f"Object of type {type(value).__name__} is not JSON serializable")

def convert_dates_to_strings(value):
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: convert_dates_to_strings(item) for key, item in value.items()}
    if isinstance(value, list):
        return [convert_dates_to_strings(item) for item in value]
    if isinstance(value, tuple):
        return [convert_dates_to_strings(item) for item in value]
    return value

def restore_dates(value):
    if isinstance(value, dict):
        restored = {}
        for key, item in value.items():
            if key == "date" and isinstance(item, str):
                restored[key] = date.fromisoformat(item)
            else:
                restored[key] = restore_dates(item)
        return restored
    if isinstance(value, list):
        return [restore_dates(item) for item in value]
    return value

def main():
    print(f"{OWNER}, {GROUP}")
    original = {
        "owner": OWNER,
        "date": date.today(),
        "details": {"created": date(2026, 11, 23)}
    }

    try:
        json.dumps(original)
    except TypeError as error:
        print(f"TypeError: {error}")

    # Method 1: default= converts date objects to ISO strings.
    with OUTPUT_DEFAULT.open("w", encoding="utf-8") as file:
        json.dump(original, file, default=date_default, indent=2, ensure_ascii=False)
    with OUTPUT_DEFAULT.open("r", encoding="utf-8") as file:
        loaded_default = json.load(file)
    print(f"default method saved: {OUTPUT_DEFAULT.name}")
    print(f"default method date: {loaded_default['date']}")

    # Method 2: explicitly convert before saving and restore after reading.
    converted = convert_dates_to_strings(original)
    with OUTPUT_CUSTOM.open("w", encoding="utf-8") as file:
        json.dump(converted, file, indent=2, ensure_ascii=False)
    with OUTPUT_CUSTOM.open("r", encoding="utf-8") as file:
        loaded_custom = restore_dates(json.load(file))

    print(f"custom method saved: {OUTPUT_CUSTOM.name}")
    print(f"data equal after restoring: {loaded_custom == original}")
    print(f"date restored as date: {isinstance(loaded_custom['date'], date)}")

if __name__ == "__main__":
    main()
