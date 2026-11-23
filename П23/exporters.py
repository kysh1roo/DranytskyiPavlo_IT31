import csv
import json
from abc import ABC, abstractmethod
from html import escape
from pathlib import Path


class Exporter(ABC):
    @abstractmethod
    def export(self, expenses, path):
        """Write expenses to the file at path."""

    def target(self, name):
        return Path(f"{name}.{self.extension()}")

    @abstractmethod
    def extension(self):
        """Return file extension without dot."""


class CsvExporter(Exporter):
    def extension(self):
        return "csv"

    def export(self, expenses, path):
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "category", "amount", "comment"])
            for e in expenses:
                writer.writerow([e.date, e.category, f"{e.amount:.2f}", e.comment])


class JsonExporter(Exporter):
    def extension(self):
        return "json"

    def export(self, expenses, path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump([e.as_dict() for e in expenses], f, ensure_ascii=False, indent=2)


class TxtExporter(Exporter):
    def extension(self):
        return "txt"

    def export(self, expenses, path):
        lines = [f"{'date':<12}{'category':<16}{'amount':>10}  comment",
                 "-" * 52]
        for e in expenses:
            lines.append(f"{e.date:<12}{e.category:<16}{e.amount:>10.2f}  {e.comment}")
        lines.append("-" * 52)
        lines.append(f"{'total':<28}{sum(e.amount for e in expenses):>10.2f}")
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")


class HtmlExporter(Exporter):
    def extension(self):
        return "html"

    def export(self, expenses, path):
        rows = "\n".join(
            "    <tr><td>{}</td><td>{}</td><td class=\"num\">{:.2f}</td><td>{}</td></tr>".format(
                escape(e.date), escape(e.category), e.amount, escape(e.comment))
            for e in expenses
        )
        total = sum(e.amount for e in expenses)
        page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Expenses report</title>
  <style>
    body {{ font-family: sans-serif; margin: 2rem; }}
    table {{ border-collapse: collapse; }}
    th, td {{ border: 1px solid #999; padding: 6px 12px; }}
    th {{ background: #eee; }}
    .num {{ text-align: right; }}
  </style>
</head>
<body>
  <h1>Expenses report</h1>
  <table>
    <tr><th>Date</th><th>Category</th><th>Amount</th><th>Comment</th></tr>
{rows}
    <tr><th colspan="2">Total</th><th class="num">{total:.2f}</th><th></th></tr>
  </table>
</body>
</html>
"""
        with open(path, "w", encoding="utf-8") as f:
            f.write(page)


if __name__ == "__main__":
    try:
        Exporter()
    except TypeError as error:
        print("error:", error)
