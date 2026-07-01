#!/usr/bin/env python3
"""Lightweight JSON validator for character-forge generated records."""

import json
import sys
from pathlib import Path


REQUIRED_TOP_LEVEL = ["basic", "identity", "outfit", "grooming", "muse", "blackwall", "azoth"]
REQUIRED_BASIC = [
    "name",
    "gender",
    "age",
    "nationality",
    "body_type",
    "personality",
    "wealth",
    "danger",
    "desire",
    "execution",
    "social",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: validate_character.py <character.json>")

    path = Path(sys.argv[1])
    data = json.loads(path.read_text(encoding="utf-8"))

    for key in REQUIRED_TOP_LEVEL:
        if key not in data:
            fail(f"missing top-level key: {key}")

    for key in REQUIRED_BASIC:
        if key not in data["basic"]:
            fail(f"missing basic key: {key}")

    for key in ["wealth", "danger", "desire", "execution", "social"]:
        value = data["basic"][key]
        if not isinstance(value, int) or not 1 <= value <= 10:
            fail(f"basic.{key} must be an integer from 1 to 10")

    print("OK: character record shape looks valid")


if __name__ == "__main__":
    main()
