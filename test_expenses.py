from pathlib import Path
import pytest
from expenses import parse_line, total_by_category, load_expenses


# Завдання 2. Перші тести з assert (щонайменше 3 тести для parse_line)
def test_parse_line_valid():
    record = parse_line("2026-09-21;food;85.50;lunch")
    assert record["date"] == "2026-09-21"
    assert record["category"] == "food"
    assert record["amount"] == 85.5
    assert record["comment"] == "lunch"


def test_parse_line_integer_amount():
    record = parse_line("2026-09-21;transport;20;metro")
    assert isinstance(record["amount"], float)
    assert record["amount"] == 20.0


def test_parse_line_strips_whitespace():
    record = parse_line("  2026-09-22;food;14.50;coffee  \n")
    assert record == {
        "date": "2026-09-22",
        "category": "food",
        "amount": 14.5,
        "comment": "coffee",
    }


# Завдання 3. Перевірка винятків (нечислова сума та неправильна кількість полів)
def test_parse_line_bad_amount():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;abc;lunch")


def test_parse_line_too_few_fields():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;85.50")


def test_parse_line_too_many_fields():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;85.50;lunch;extra")


# Завдання 4. Параметризований тест на 5 рядках із data/expenses.csv
@pytest.mark.parametrize(
    "line, expected_category, expected_amount",
    [
        ("2026-09-21;food;85.50;lunch", "food", 85.5),
        ("2026-09-21;transport;20.00;metro", "transport", 20.0),
        ("2026-09-23;entertainment;250.00;cinema", "entertainment", 250.0),
        ("2026-09-24;utilities;420.75;internet", "utilities", 420.75),
        ("2026-09-27;books;199.90;python book", "books", 199.9),
    ],
)
def test_parse_line_parametrized(line, expected_category, expected_amount):
    record = parse_line(line)
    assert record["category"] == expected_category
    assert record["amount"] == expected_amount


# Завдання 5. Тест з тимчасовим файлом (tmp_path) та реальним data/expenses.csv
def test_total_by_category_tmp(tmp_path):
    path = tmp_path / "expenses.csv"
    path.write_text(
        "# date;category;amount;comment\n"
        "2026-09-21;food;85.50;lunch\n"
        "\n"
        "2026-09-22;food;14.50;coffee\n",
        encoding="utf-8",
    )
    totals = total_by_category(load_expenses(path))
    assert totals == {"food": 100.0}


def test_total_by_category_real_file():
    csv_path = Path(__file__).parent / "data" / "expenses.csv"
    records = load_expenses(csv_path)
    totals = total_by_category(records)
    assert totals == {
        "food": 235.2,
        "transport": 65.0,
        "entertainment": 250.0,
        "utilities": 420.75,
        "books": 199.9,
    }
