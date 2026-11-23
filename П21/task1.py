import json
import sys

CSV_PATH = "data/expenses.csv"
JSON_PATH = "data/expenses.json"


class Expense:
    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment

    @classmethod
    def from_csv_line(cls, line):
        date, category, amount, comment = line.strip().split(";")
        return cls(date, category, float(amount), comment)

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["date"],
            data["category"],
            float(data["amount"]),
            data.get("comment", ""),
        )

    @classmethod
    def from_input(cls):
        date = input("date (YYYY-MM-DD): ")
        category = input("category: ")
        amount = float(input("amount: ").replace(",", "."))
        comment = input("comment: ")
        return cls(date, category, amount, comment)

    def as_tuple(self):
        return (self.date, self.category, self.amount, self.comment)


def main():
    try:
        with open(CSV_PATH, encoding="utf-8") as f:
            from_csv = [Expense.from_csv_line(line) for line in f if line.strip()]
        with open(JSON_PATH, encoding="utf-8") as f:
            from_json = [Expense.from_dict(d) for d in json.load(f)]
    except (OSError, ValueError, KeyError) as e:
        print(f"Cannot load data: {e}", file=sys.stderr)
        sys.exit(1)

    print("Pavlo Dranytskyi, IT-31")
    print("from CSV: ", len(from_csv))
    print("from JSON:", len(from_json))
    same = [a.as_tuple() for a in from_csv] == [b.as_tuple() for b in from_json]
    print("data identical:", same)

    if "--input" in sys.argv:
        try:
            e = Expense.from_input()
        except ValueError as err:
            print(f"Invalid input: {err}", file=sys.stderr)
            sys.exit(1)
        print("created from input:", e.as_tuple())


if __name__ == "__main__":
    main()
