import csv
import sys
from datetime import datetime

from task2 import Money

CSV_PATH = "data/expenses.csv"


class Expense:
    def __init__(self, date, category, amount, comment=""):
        self.date = date            # datetime.date
        self.category = category
        self.amount = amount        # Money
        self.comment = comment

    def __str__(self):
        return f"{self.date:%d.%m.%Y} {self.category} {self.amount} ({self.comment})"


class ExpenseBook:
    def __init__(self, expenses=None):
        self.expenses = list(expenses or [])

    def __len__(self):
        return len(self.expenses)

    def __contains__(self, category):
        return any(e.category == category for e in self.expenses)

    def __iter__(self):
        return iter(self.expenses)

    def __getitem__(self, index):
        return self.expenses[index]

    def __add__(self, other):
        if not isinstance(other, ExpenseBook):
            return NotImplemented
        return ExpenseBook(self.expenses + other.expenses)

    def total(self):
        return sum((e.amount for e in self.expenses), Money(0))

    def __str__(self):
        return f"ExpenseBook: {len(self)} records, total {self.total()}"


def load_expenses(path):
    result = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            date = datetime.strptime(row["date"], "%Y-%m-%d").date()
            amount = Money(float(row["amount"].replace(",", ".")))
            result.append(Expense(date, row["category"], amount, row.get("comment", "")))
    return result


def main():
    try:
        expenses = load_expenses(CSV_PATH)
    except (OSError, ValueError, KeyError) as e:
        print(f"Cannot read {CSV_PATH}: {e}", file=sys.stderr)
        sys.exit(1)

    first = ExpenseBook(e for e in expenses if e.date.day < 15)    # 1-14
    second = ExpenseBook(e for e in expenses if e.date.day >= 15)  # 15-31
    merged = first + second

    print("Pavlo Dranytskyi, IT-31")
    print("first half: ", first)
    print("second half:", second)
    print("merged:     ", merged)
    print("len:", len(first), "+", len(second), "=", len(merged))
    print('"food" in merged:', "food" in merged)
    print('"travel" in merged:', "travel" in merged)
    print("merged[0]:", merged[0])
    print("iteration:")
    for e in merged:
        print(" ", e)


if __name__ == "__main__":
    main()
