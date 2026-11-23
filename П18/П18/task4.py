import sys

from task3 import CSV_PATH, Expense, load_expenses


class ExpenseBook:
    def __init__(self):
        self.expenses = []

    def add(self, expense):
        self.expenses.append(expense)

    def total(self):
        return sum(e.amount for e in self.expenses)

    def by_category(self, category):
        return sum(e.amount for e in self.expenses if e.category == category)

    def top(self, n):
        return sorted(self.expenses, key=lambda e: e.amount, reverse=True)[:n]


if __name__ == "__main__":
    book = ExpenseBook()
    try:
        for expense in load_expenses(CSV_PATH):
            book.add(expense)
    except (OSError, ValueError, KeyError) as e:
        print(f"Cannot read {CSV_PATH}: {e}", file=sys.stderr)
        sys.exit(1)

    print("Pavlo Dranytskyi, IT-31")
    print(f"records: {len(book.expenses)}")
    print(f"total: {book.total():.2f} UAH")
    print("by category:")
    for category in sorted({e.category for e in book.expenses}):
        print(f"  {category}: {book.by_category(category):.2f}")
    print("top 3:")
    for e in book.top(3):
        print(" ", e.describe())
