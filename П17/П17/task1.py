import sys

import requests

AUTHOR = "Dranytskyi Pavlo, IT-31"
URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"


def main():
    try:
        response = requests.get(URL, params={"json": ""}, timeout=10)
        response.raise_for_status()
        rates = response.json()
    except requests.RequestException as e:
        print(f"Request error: {e}", file=sys.stderr)
        sys.exit(1)

    print(AUTHOR)
    print("status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("currencies:", len(rates))

    for code in ("USD", "EUR"):
        item = next((r for r in rates if r["cc"] == code), None)
        if item is None:
            print(f"{code}: not found in response", file=sys.stderr)
            sys.exit(1)
        print(f"{code}: {item['rate']} UAH (date {item['exchangedate']})")


if __name__ == "__main__":
    main()
