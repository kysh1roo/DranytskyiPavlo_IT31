import math
import sys
from datetime import datetime
from pathlib import Path

NAME = "Pavlo Dranytskyi"
GROUP = "IT-31"
UNITS = ["B", "KB", "MB", "GB"]
USAGE = "usage: python3 task3.py [--dry-run] <dir>"


def human_size(size):
    """Розмір у зручному вигляді; одиницю визначає math.log(size, 1024)."""
    if size <= 0:
        return "0 B"
    idx = min(int(math.log(size, 1024) + 1e-9), len(UNITS) - 1)
    if idx == 0:
        return f"{size} B"
    return f"{size / 1024 ** idx:.1f} {UNITS[idx]}"


def parse_args(argv):
    """Повертає (dry_run, Path) або None, якщо аргументи неправильні."""
    dry_run = False
    paths = []
    for arg in argv:
        if arg == "--dry-run":
            dry_run = True
        elif arg.startswith("--"):
            return None
        else:
            paths.append(arg)
    if len(paths) != 1 or argv.count("--dry-run") > 1:
        return None
    return dry_run, Path(paths[0])


def main():
    print(f"{NAME}, {GROUP}")

    parsed = parse_args(sys.argv[1:])
    if parsed is None:
        print(USAGE, file=sys.stderr)
        sys.exit(2)
    dry_run, directory = parsed

    if not directory.is_dir():
        print(f"error: {directory} is not a directory", file=sys.stderr)
        sys.exit(1)

    items = []
    try:
        for path in directory.iterdir():
            if path.is_file():
                st = path.stat()
                items.append((datetime.fromtimestamp(st.st_mtime), path, st.st_size))
    except OSError as exc:
        print(f"error: cannot read {directory}: {exc}", file=sys.stderr)
        sys.exit(1)

    if not items:
        print(f"no files to organize in {directory}")
        return

    items.sort(key=lambda item: (item[0], item[1].name))

    width = max(len(path.name) for _, path, _ in items)
    plan_lines = []
    folders = set()
    for modified, path, size in items:
        month = f"{modified:%Y-%m}"
        folders.add(month)
        plan_lines.append(
            f"{path.name:<{width}}  {human_size(size):>10}  "
            f"{modified:%d.%m.%Y %H:%M}  -> {month}/"
        )
    for line in plan_lines:
        print(line)

    summary = f"{len(items)} files, {len(folders)} folders"

    for modified, path, _ in items:
        target = directory / f"{modified:%Y-%m}" / path.name
        if target.exists():
            print(f"error: {target} already exists, nothing was moved",
                  file=sys.stderr)
            sys.exit(1)

    if dry_run:
        print(f"{summary} (dry run, nothing moved)")
        return

    for modified, path, _ in items:
        target_dir = directory / f"{modified:%Y-%m}"
        try:
            target_dir.mkdir(exist_ok=True)
            path.rename(target_dir / path.name)
        except OSError as exc:
            print(f"error: cannot move {path}: {exc}", file=sys.stderr)
            sys.exit(1)
    print(summary)

    now = datetime.now()
    reports_dir = Path(__file__).resolve().parent / "reports"
    report = reports_dir / f"organize_{now:%Y%m%d_%H%M}.txt"
    lines = [f"{NAME}, {GROUP}", f"run: {now:%d.%m.%Y %H:%M}",
             f"directory: {directory}", ""] + plan_lines
    try:
        reports_dir.mkdir(exist_ok=True)
        report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    except OSError as exc:
        print(f"error: cannot write report: {exc}", file=sys.stderr)
        sys.exit(1)
    print(f"report saved to: reports/{report.name}")


if __name__ == "__main__":
    main()
