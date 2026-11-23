import sys
from datetime import datetime


class Expense:
    """Клас Expense з роботи 46 (скорочений до потрібного в цій роботі)."""

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
        parts = line.strip().split(";")
        if len(parts) != 4:
            print(f"skipped (need 4 fields): {line.strip()!r}", file=sys.stderr)
            return None
        date, category, amount, comment = parts
        if not cls.is_valid_date(date) or not cls.is_valid_amount(amount):
            print(f"skipped (bad data): {line.strip()!r}", file=sys.stderr)
            return None
        return cls(date, category, float(amount.replace(",", ".")), comment)

    def as_dict(self):
        return {
            "date": self.date,
            "category": self.category,
            "amount": self.amount,
            "comment": self.comment,
        }


def load_expenses(path):
    with open(path, encoding="utf-8") as f:
        items = (Expense.from_csv_line(line) for line in f if line.strip())
        return [e for e in items if e is not None]
