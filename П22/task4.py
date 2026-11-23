import sys

from task2 import Money
from task3 import CSV_PATH, ExpenseBook, load_expenses

BUDGET = Money(2000)


class BudgetBook(ExpenseBook):
    """ExpenseBook, яку можна порівнювати з бюджетом (Money)."""

    def __gt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return other < self.total()

    def __lt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.total() < other


def main():
    try:
        book = BudgetBook(load_expenses(CSV_PATH))
    except (OSError, ValueError, KeyError) as e:
        print(f"Cannot read {CSV_PATH}: {e}", file=sys.stderr)
        sys.exit(1)

    print("Pavlo Dranytskyi, IT-31")
    print("budget:  ", BUDGET)
    print("expenses:", book.total())
    print("book > budget:", book > BUDGET)
    if book > BUDGET:
        print("over budget by", book.total() - BUDGET)
    else:
        print("within budget, left", BUDGET - book.total())


if __name__ == "__main__":
    main()
