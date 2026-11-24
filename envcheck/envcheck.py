
import argparse
import sys
from pathlib import Path


def read_variables(path):
    variables = set()

    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        if "=" not in line:
            continue

        key = line.split("=", 1)[0].strip()

        if key:
            variables.add(key)

    return variables


def check_files(example, actual):
    expected = read_variables(example)
    existing = read_variables(actual)

    return sorted(expected - existing), sorted(existing - expected)


def main():
    parser = argparse.ArgumentParser(
        description="Check environment files for missing variables."
    )

    parser.add_argument("example", type=Path)
    parser.add_argument("actual", type=Path)

    args = parser.parse_args()

    for path in (args.example, args.actual):
        if not path.is_file():
            print(f"Error: file not found: {path}", file=sys.stderr)
            return 2

    try:
        missing, extra = check_files(args.example, args.actual)
    except (OSError, UnicodeError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2

    print("envcheck")
    print()

    print("Missing:")
    if missing:
        for key in missing:
            print(f"  {key}")
    else:
        print("  None")

    print()
    print("Extra:")
    if extra:
        for key in extra:
            print(f"  {key}")
    else:
        print("  None")

    print()
    print(f"{len(missing)} missing, {len(extra)} extra")

    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
