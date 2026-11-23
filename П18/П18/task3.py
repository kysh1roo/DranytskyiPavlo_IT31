import csv
import sys
from datetime import datetime

CSV_PATH = "data/expenses.csv"
BIG_LIMIT = 300.0


class Expense:
    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment

    def is_big(self, limit):
        return self.amount > limit

    def describe(self):
        text = f"{self.date} {self.category} {self.amount:.2f}"
        if self.comment:
            text += f" ({self.comment})"
        return text


def load_expenses(path):
    expenses = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            date = datetime.strptime(row["date"], "%Y-%m-%d").strftime("%d.%m.%Y")
            expenses.append(
                Expense(
                    date,
                    row["category"],
                    float(row["amount"].replace(",", ".")),
                    row.get("comment", ""),
                )
            )
    return expenses


if __name__ == "__main__":
    try:
        expenses = load_expenses(CSV_PATH)
    except (OSError, ValueError, KeyError) as e:
        print(f"Cannot read {CSV_PATH}: {e}", file=sys.stderr)
        sys.exit(1)

    print("Pavlo Dranytskyi, IT-31")
    print("objects created:", len(expenses))
    print(f"big expenses (> {BIG_LIMIT:.0f}):")
    for e in expenses:
        if e.is_big(BIG_LIMIT):
            print(" ", e.describe())
