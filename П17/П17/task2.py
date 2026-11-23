"""Expenses in UAH / USD / EUR at the NBU rate.

Usage:
    python3 task2.py            # normal run
    python3 task2.py 404        # task 4: nonexistent URL -> HTTPError
    python3 task2.py timeout    # task 4: timeout=0.001 -> Timeout
(for the "no internet" case just turn Wi-Fi off and run normally)
"""
import csv
import sys

import requests

AUTHOR = "Dranytskyi Pavlo, IT-31"
URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
CSV_PATH = "data/expenses.csv"
AMOUNT_COLUMNS = ("amount", "sum", "cost", "price", "сума")


def load_total(path):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        column = next(
            (c for c in reader.fieldnames if c.strip().lower() in AMOUNT_COLUMNS),
            None,
        )
        if column is None:
            raise ValueError(f"no amount column in {path}: {reader.fieldnames}")
        return sum(float(row[column].replace(",", ".")) for row in reader)


def get_rate(code, url, timeout):
    response = requests.get(url, params={"valcode": code, "json": ""}, timeout=timeout)
    response.raise_for_status()
    item = response.json()[0]
    return item["rate"], item["exchangedate"]


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    url = URL + "X" if mode == "404" else URL
    timeout = 0.001 if mode == "timeout" else 10

    try:
        total = load_total(CSV_PATH)
    except (OSError, ValueError) as e:
        print(f"Cannot read expenses: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        usd, date = get_rate("USD", url, timeout)
        eur, _ = get_rate("EUR", url, timeout)
    except requests.Timeout:
        print("Error: request timed out", file=sys.stderr)
        sys.exit(1)
    except requests.ConnectionError:
        print("Error: no connection to the server (check internet)", file=sys.stderr)
        sys.exit(1)
    except requests.HTTPError as e:
        print(f"Error: HTTP status {e.response.status_code}: {e}", file=sys.stderr)
        sys.exit(1)
    except (requests.RequestException, IndexError, KeyError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    print(AUTHOR)
    print("rate date:", date)
    print(f"total: {total:.2f} UAH = {total / usd:.2f} USD = {total / eur:.2f} EUR")


if __name__ == "__main__":
    main()
