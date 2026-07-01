from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

CHECK_PATHS = [
    ROOT / "black-market" / "SKILL.md",
    ROOT / "black-market" / "inventory.md",
    ROOT / "black-market" / "inventory" / "styling.md",
    ROOT / "black-market" / "inventory" / "styling",
    ROOT / "character-forge" / "references" / "sanzhai.md",
]

FORBIDDEN_FRAGMENTS = [
    "鍚嶇О",
    "鎻忚堪",
    "绫诲埆",
    "鏍囩",
    "",
    "\ufffd",
]


def iter_files(path: Path) -> list[Path]:
    if not path.exists():
        return []
    if path.is_file():
        return [path]
    return [
        item
        for item in path.rglob("*")
        if item.is_file()
        and "archive" not in item.parts
        and item.suffix.lower() in {".md", ".yaml", ".yml", ".json"}
    ]


def check_file(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        raw = path.read_bytes()
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        return [f"{path}: not valid UTF-8: {exc}"]

    for fragment in FORBIDDEN_FRAGMENTS:
        if fragment in text:
            errors.append(f"{path}: contains mojibake fragment {fragment!r}")

    lines = text.splitlines()
    for lineno, line in enumerate(lines, start=1):
        if line.count('"') % 2 == 1 and not line.lstrip().startswith("#"):
            errors.append(f"{path}:{lineno}: odd number of double quotes")
    return errors


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    files: list[Path] = []
    for path in CHECK_PATHS:
        files.extend(iter_files(path))

    errors: list[str] = []
    for path in sorted(set(files)):
        errors.extend(check_file(path))

    if errors:
        print("Inventory encoding check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Inventory encoding check passed ({len(set(files))} files).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
