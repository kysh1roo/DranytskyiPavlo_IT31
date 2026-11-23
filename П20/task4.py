import sys

from task3 import CSV_PATH, Expense, build_expenses, print_total


class YearlyExpense(Expense):
    def monthly_cost(self):
        return self.amount / 12


if __name__ == "__main__":
    try:
        items = build_expenses()
    except (OSError, ValueError, KeyError) as err:
        print(f"Cannot read {CSV_PATH}: {err}", file=sys.stderr)
        sys.exit(1)

    items.append(YearlyExpense("01.10.2026", "subscription", 1200.00))

    print("Pavlo Dranytskyi, IT-31")
    print_total(items)   # цикл підрахунку той самий, без змін
