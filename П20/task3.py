import csv
import sys
from datetime import datetime

CSV_PATH = "data/expenses.csv"


class Expense:
    def __init__(self, date, category, amount):
        self.date = date
        self.category = category
        self.amount = amount

    def monthly_cost(self):
        return self.amount


class RecurringExpense(Expense):
    def __init__(self, date, category, amount, times_per_month):
        super().__init__(date, category, amount)
        self.times_per_month = times_per_month

    def monthly_cost(self):
        return self.amount * self.times_per_month


class SharedExpense(Expense):
    def __init__(self, date, category, amount, people):
        super().__init__(date, category, amount)
        self.people = people

    def monthly_cost(self):
        return self.amount / self.people


def load_expenses(path):
    result = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            date = datetime.strptime(row["date"], "%Y-%m-%d").strftime("%d.%m.%Y")
            result.append(Expense(date, row["category"],
                                  float(row["amount"].replace(",", "."))))
    return result


def build_expenses():
    expenses = load_expenses(CSV_PATH)
    expenses += [
        RecurringExpense("01.10.2026", "transport", 15.00, 20),
        RecurringExpense("01.10.2026", "coffee", 45.00, 8),
        SharedExpense("01.10.2026", "rent", 6000.00, 3),
        SharedExpense("01.10.2026", "internet", 300.00, 2),
    ]
    return expenses


def print_total(expenses):
    total = 0.0
    for e in expenses:
        cost = e.monthly_cost()
        total += cost
        print(f"{e.date} {e.category:<14} {type(e).__name__:<18} {cost:9.2f}")
    print(f"total per month: {total:.2f} UAH")
    return total


if __name__ == "__main__":
    try:
        items = build_expenses()
    except (OSError, ValueError, KeyError) as err:
        print(f"Cannot read {CSV_PATH}: {err}", file=sys.stderr)
        sys.exit(1)
    print("Pavlo Dranytskyi, IT-31")
    print_total(items)
