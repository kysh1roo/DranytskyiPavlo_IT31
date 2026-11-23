import csv
import sys

CSV_PATH = "data/expenses.csv"


class Money:
    def __init__(self, amount, currency="UAH"):
        self.cents = round(amount * 100)
        self.currency = currency

    def _check(self, other):
        if self.currency != other.currency:
            raise ValueError("different currencies")

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented        # Python сам згенерує TypeError
        self._check(other)
        return Money((self.cents + other.cents) / 100, self.currency)

    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        self._check(other)
        return Money((self.cents - other.cents) / 100, self.currency)

    def __mul__(self, k):
        if not isinstance(k, (int, float)):
            return NotImplemented
        return Money(self.cents * k / 100, self.currency)

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.cents == other.cents and self.currency == other.currency

    def __lt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        self._check(other)
        return self.cents < other.cents

    def __hash__(self):
        return hash((self.cents, self.currency))

    def __str__(self):
        return f"{self.cents / 100:.2f} {self.currency}"

    def __repr__(self):
        return f"Money({self.cents / 100}, {self.currency!r})"


def load_money(path):
    with open(path, newline="", encoding="utf-8") as f:
        return [Money(float(row["amount"].replace(",", "."))) for row in csv.DictReader(f)]


def main():
    try:
        items = load_money(CSV_PATH)
    except (OSError, ValueError, KeyError) as e:
        print(f"Cannot read {CSV_PATH}: {e}", file=sys.stderr)
        sys.exit(1)

    print("Pavlo Dranytskyi, IT-31")
    print("original:", [str(m) for m in items])
    print("sorted:  ", [str(m) for m in sorted(items)])   # працює завдяки __lt__
    print("total:", sum(items, Money(0)))
    # Другий аргумент sum() — початкове значення. За замовчуванням це 0,
    # а 0 + Money(...) не підтримується, тому стартуємо з Money(0).

    try:
        Money(10) + 5
    except TypeError as e:
        print("Money(10) + 5 -> TypeError:", e)


if __name__ == "__main__":
    main()
