# Три класи БЕЗ спільного предка: поліморфізм через однаковий інтерфейс.

class Expense:
    kind = "expenses"

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def balance_change(self):
        return -self.amount


class Income:
    kind = "income"

    def __init__(self, source, amount):
        self.source = source
        self.amount = amount

    def balance_change(self):
        return self.amount


class Transfer:
    kind = "transfers"

    def __init__(self, from_card, to_card, amount):
        self.from_card = from_card
        self.to_card = to_card
        self.amount = amount

    def balance_change(self):
        return 0


def main():
    items = [
        Income("scholarship", 1600.00),
        Income("part-time job", 1000.00),
        Expense("food", 250.00),
        Expense("transport", 120.50),
        Expense("books", 310.00),
        Expense("entertainment", 200.00),
        Expense("food", 367.50),
        Transfer("card 1", "card 2", 500.00),
    ]

    totals = {"income": 0.0, "expenses": 0.0, "transfers": 0.0}
    balance = 0.0
    for item in items:                 # без перевірки типу
        change = item.balance_change()
        totals[item.kind] += change
        balance += change

    print("Pavlo Dranytskyi, IT-31")
    for kind in ("income", "expenses", "transfers"):
        print(f"{kind + ':':<10}{totals[kind]:>8.2f}")
    print(f"{'balance:':<10}{balance:>8.2f}")


if __name__ == "__main__":
    main()
