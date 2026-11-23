import json
import sys

JSON_PATH = "data/expenses.json"


class Expense:
    currency = "UAH"   # змінна класу, спільна для всіх витрат
    count = 0          # лічильник створених об'єктів

    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment
        Expense.count += 1

    @classmethod
    def from_dict(cls, data):
        return cls(data["date"], data["category"],
                   float(data["amount"]), data.get("comment", ""))

    @classmethod
    def set_currency(cls, code):
        cls.currency = code

    def describe(self):
        return f"{self.date} {self.category} {self.amount:.2f} {self.currency} ({self.comment})"


def main():
    try:
        with open(JSON_PATH, encoding="utf-8") as f:
            expenses = [Expense.from_dict(d) for d in json.load(f)]
    except (OSError, ValueError, KeyError) as e:
        print(f"Cannot load {JSON_PATH}: {e}", file=sys.stderr)
        sys.exit(1)

    print("Pavlo Dranytskyi, IT-31")
    print("objects created:", Expense.count)
    print("--- currency:", Expense.currency)
    for e in expenses[:3]:
        print(e.describe())

    Expense.set_currency("USD")
    print("--- currency:", Expense.currency)
    for e in expenses[:3]:
        print(e.describe())
    print("(only the label changes, amounts are not converted)")


if __name__ == "__main__":
    main()
