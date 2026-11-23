import json
import sys
import time
from pathlib import Path

import requests

AUTHOR = "Dranytskyi Pavlo, IT-31"
URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
CACHE = Path("cache/rates.json")
MAX_AGE = 3600  # 1 hour


def read_cache():
    try:
        cached = json.loads(CACHE.read_text(encoding="utf-8"))
        age = time.time() - cached["saved_at"]
        if 0 <= age < MAX_AGE:
            return cached["data"], age
    except (OSError, ValueError, KeyError):
        pass
    return None, None


def main():
    data, age = read_cache()
    print(AUTHOR)
    if data is not None:
        print(f"source: cache (age {age:.0f} s)")
        return

    try:
        response = requests.get(URL, params={"json": ""}, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"Request error: {e}", file=sys.stderr)
        sys.exit(1)

    CACHE.parent.mkdir(exist_ok=True)
    CACHE.write_text(
        json.dumps({"saved_at": time.time(), "data": data}, ensure_ascii=False),
        encoding="utf-8",
    )
    print("source: api (cache saved)")


if __name__ == "__main__":
    main()
