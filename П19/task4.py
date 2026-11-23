import csv
import sys
from datetime import datetime

from task3 import Wallet

CSV_PATH = "data/expenses.csv"
BUDGET = 2000


def load_expenses(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = []
        for row in csv.DictReader(f):
            date = datetime.strptime(row["date"], "%Y-%m-%d").strftime("%d.%m.%Y")
            rows.append((date, row["category"], float(row["amount"].replace(",", "."))))
        return rows


def main():
    try:
        expenses = load_expenses(CSV_PATH)
    except (OSError, ValueError, KeyError) as e:
        print(f"Cannot read {CSV_PATH}: {e}", file=sys.stderr)
        sys.exit(1)

    wallet = Wallet("Pavlo Dranytskyi", BUDGET)
    print(f"{wallet.owner}, budget {wallet.balance:.2f}")

    spent = 0.0
    for date, category, amount in expenses:
        try:
            wallet.withdraw(amount)
        except ValueError as e:
            print(f"STOP: {date} {category} {amount:.2f} -> {e} "
                  f"(balance {wallet.balance:.2f})")
            return
        spent += amount
        print(f"{date} {category:<14} -{amount:7.2f}  balance {wallet.balance:.2f}")

    print(f"spent: {spent:.2f}, left: {wallet.balance:.2f}")


if __name__ == "__main__":
    main()
