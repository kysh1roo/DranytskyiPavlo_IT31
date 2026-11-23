class Money:
    def __init__(self, amount, currency="UAH"):
        self.cents = round(amount * 100)   # зберігаємо в копійках (int)
        self.currency = currency

    def _check(self, other):
        if self.currency != other.currency:
            raise ValueError("different currencies")

    def __add__(self, other):
        self._check(other)
        return Money((self.cents + other.cents) / 100, self.currency)

    def __sub__(self, other):
        self._check(other)
        return Money((self.cents - other.cents) / 100, self.currency)

    def __mul__(self, k):
        return Money(self.cents * k / 100, self.currency)

    def __eq__(self, other):
        return self.cents == other.cents and self.currency == other.currency

    def __lt__(self, other):
        self._check(other)
        return self.cents < other.cents

    def __hash__(self):
        return hash((self.cents, self.currency))

    def __str__(self):
        return f"{self.cents / 100:.2f} {self.currency}"

    def __repr__(self):
        return f"Money({self.cents / 100}, {self.currency!r})"


if __name__ == "__main__":
    print("Pavlo Dranytskyi, IT-31")
    print("float: 0.1 + 0.2 == 0.3 ->", 0.1 + 0.2 == 0.3)
    print("Money: 0.1 + 0.2 == 0.3 ->", Money(0.1) + Money(0.2) == Money(0.3))
    print("Money(0.1) + Money(0.2) =", Money(0.1) + Money(0.2))
    print("Money(100) - Money(30.5) =", Money(100) - Money(30.5))
    print("Money(25.5) * 3 =", Money(25.5) * 3)
    print("Money(10) < Money(20):", Money(10) < Money(20))
    print("repr:", repr(Money(85.5)))
    try:
        Money(10, "UAH") + Money(10, "USD")
    except ValueError as e:
        print("UAH + USD ->", "ValueError:", e)
