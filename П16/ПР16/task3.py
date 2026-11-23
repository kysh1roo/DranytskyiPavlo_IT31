import json
import sys
from pathlib import Path

OWNER = "Pavlo Dranytskyi"
GROUP = "IT-31"
BASE_DIR = Path(__file__).resolve().parent
SETTINGS_PATH = BASE_DIR / "settings.json"
EXPENSES_PATH = BASE_DIR / "data" / "expenses.json"

DEFAULT_SETTINGS = {
    "owner": OWNER,
    "group": GROUP,
    "currency": "UAH",
    "monthly_limit": 6000,
    "categories": ["food", "transport", "fun"]
}

def main():
    print(f"{OWNER}, {GROUP}")

    if not SETTINGS_PATH.exists():
        with SETTINGS_PATH.open("w", encoding="utf-8") as file:
            json.dump(DEFAULT_SETTINGS, file, indent=2, ensure_ascii=False)
        print("settings.json not found, default created")
        return

    try:
        with SETTINGS_PATH.open("r", encoding="utf-8") as file:
            settings = json.load(file)
    except json.JSONDecodeError as error:
        print(f"Invalid JSON at line {error.lineno}: {error.msg}", file=sys.stderr)
        raise SystemExit(1)

    with EXPENSES_PATH.open("r", encoding="utf-8") as file:
        expenses = json.load(file)

    spent = sum(float(item["amount"]) for item in expenses)
    limit = float(settings["monthly_limit"])
    left = limit - spent

    print(f"owner: {settings['owner']}")
    print(f"group: {settings['group']}")
    print(f"categories: {', '.join(settings['categories'])}")
    print(f"limit: {limit:.2f} {settings['currency']}, spent: {spent:.2f} {settings['currency']}, left: {left:.2f} {settings['currency']}")

if __name__ == "__main__":
    main()
