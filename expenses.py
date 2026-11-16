from pathlib import Path


def parse_line(line: str) -> dict:
    parts = line.strip().split(";")
    if len(parts) != 4:
        raise ValueError(f"Очікується 4 поля, отримано {len(parts)}: {line!r}")

    date_str, category, amount_str, comment = parts
    try:
        amount = float(amount_str)
    except ValueError as exc:
        raise ValueError(f"Нечислова сума {amount_str!r} у рядку: {line!r}") from exc

    return {
        "date": date_str,
        "category": category,
        "amount": amount,
        "comment": comment,
    }


def total_by_category(records: list[dict]) -> dict[str, float]:
    totals: dict[str, float] = {}
    for rec in records:
        cat = rec["category"]
        totals[cat] = totals.get(cat, 0.0) + rec["amount"]
    return {cat: round(total, 2) for cat, total in totals.items()}


def load_expenses(path: str | Path) -> list[dict]:
    records: list[dict] = []
    with open(path, "r", encoding="utf-8") as file:
        for raw_line in file:
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            records.append(parse_line(line))
    return records
