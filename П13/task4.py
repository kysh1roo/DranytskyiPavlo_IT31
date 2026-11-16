import math
import random
import sys
from datetime import datetime
from pathlib import Path

NAME = "Pavlo Dranytskyi"
GROUP = "IT-31"
YEAR = 2009  
HISTORY = Path(__file__).resolve().parent / "results" / "history.csv"
HEADER = "# datetime;score;seconds"


def make_questions():
    random.seed(YEAR)  

    root = random.randint(5, 25)
    fact = random.randint(3, 7)
    a, b = random.randint(12, 99), random.randint(12, 99)
    n = random.randint(6, 12)
    k = random.randint(2, n - 2)
    percent = random.choice([5, 10, 15, 20, 25])
    base = 20 * random.randint(5, 25)

    return [
        (f"sqrt({root * root})", math.isqrt(root * root)),
        (f"{fact}!", math.factorial(fact)),
        (f"gcd({a}, {b})", math.gcd(a, b)),
        (f"comb({n}, {k})", math.comb(n, k)),
        (f"{percent}% of {base}", base * percent // 100),
    ]


def read_int(text):
    """Нечислова відповідь -> None (вважається неправильною)."""
    try:
        return int(text.strip())
    except ValueError:
        return None


def read_history():
    rows = []
    if not HISTORY.exists():
        return rows
    text = HISTORY.read_text(encoding="utf-8")
    for number, line in enumerate(text.splitlines(), start=1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(";")
        try:
            if len(parts) != 3:
                raise ValueError
            when = datetime.strptime(parts[0], "%Y-%m-%d %H:%M")
            score = int(parts[1])
            seconds = float(parts[2])
        except ValueError:
            print(f"warning: line {number} skipped: {line}", file=sys.stderr)
            continue
        rows.append((when, score, seconds))
    return rows


def save_attempt(started, score, seconds):
    HISTORY.parent.mkdir(exist_ok=True)
    is_new = not HISTORY.exists()
    with HISTORY.open("a", encoding="utf-8") as file:
        if is_new:
            file.write(HEADER + "\n")
        file.write(f"{started:%Y-%m-%d %H:%M};{score};{seconds:.1f}\n")


def main():
    print(f"{NAME}, {GROUP}")
    questions = make_questions()

    started = datetime.now()
    score = 0
    for number, (text, answer) in enumerate(questions, start=1):
        try:
            raw = input(f"{number}) {text} = ")
        except EOFError:
            raw = ""
        if read_int(raw) == answer:
            score += 1
            print("   correct")
        else:
            print(f"   wrong, answer: {answer}")
    seconds = (datetime.now() - started).total_seconds()

    print(f"score: {score}/{len(questions)}, time: {seconds:.1f} s")

    try:
        save_attempt(started, score, seconds)
        rows = read_history()
    except OSError as exc:
        print(f"error: history file problem: {exc}", file=sys.stderr)
        sys.exit(1)

    best_when, best_score, best_seconds = max(rows, key=lambda r: (r[1], -r[2]))
    print(f"attempts: {len(rows)}, best: {best_score}/{len(questions)} "
          f"in {best_seconds:.1f} s ({best_when:%Y-%m-%d %H:%M})")


if __name__ == "__main__":
    main()
