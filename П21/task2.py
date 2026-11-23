import sys
from datetime import datetime

CSV_PATH = "data/expenses.csv"


class Expense:
    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment

    @staticmethod
    def is_valid_date(text):
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return True
        except (ValueError, TypeError):
            return False

    @staticmethod
    def is_valid_amount(value):
        try:
            return float(str(value).replace(",", ".")) > 0
        except ValueError:
            return False

    @classmethod
    def from_csv_line(cls, line):
        """Повертає Expense або None (з повідомленням), якщо рядок некоректний."""
        parts = line.strip().split(";")
        if len(parts) != 4:
            print(f"skipped (need 4 fields): {line.strip()!r}", file=sys.stderr)
            return None
        date, category, amount, comment = parts
        if not cls.is_valid_date(date):
            print(f"skipped (bad date): {line.strip()!r}", file=sys.stderr)
            return None
        if not cls.is_valid_amount(amount):
            print(f"skipped (bad amount): {line.strip()!r}", file=sys.stderr)
            return None
        return cls(date, category, float(amount.replace(",", ".")), comment)


def main():
    print("Pavlo Dranytskyi, IT-31")
    print('is_valid_date("2026-02-30"):', Expense.is_valid_date("2026-02-30"))
    print('is_valid_date("2026-10-01"):', Expense.is_valid_date("2026-10-01"))
    print('is_valid_amount("abc"):', Expense.is_valid_amount("abc"))
    print('is_valid_amount(85.5):', Expense.is_valid_amount(85.5))

    try:
        with open(CSV_PATH, encoding="utf-8") as f:
            lines = [line for line in f if line.strip()]
    except OSError as e:
        print(f"Cannot read {CSV_PATH}: {e}", file=sys.stderr)
        sys.exit(1)

    lines += [
        "2026-02-30;food;10.00;bad date\n",
        "2026-10-20;food;abc;bad amount\n",
        "just some text\n",
    ]
    loaded = [e for e in map(Expense.from_csv_line, lines) if e is not None]
    print(f"lines: {len(lines)}, loaded: {len(loaded)}")


if __name__ == "__main__":
    main()
