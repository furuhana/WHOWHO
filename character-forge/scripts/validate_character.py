#!/usr/bin/env python3
"""Lightweight JSON validator for character-forge generated records."""

import json
import sys
from pathlib import Path


REQUIRED_TOP_LEVEL = [
    "basic",
    "world_context",
    "identity",
    "outfit",
    "grooming",
    "muse",
    "blackwall",
    "azoth",
]
REQUIRED_BASIC = [
    "name",
    "gender",
    "age",
    "nationality",
    "body_type",
    "personality",
    "temperament",
    "wealth",
    "danger",
    "desire",
    "execution",
    "social",
]
REQUIRED_WORLD_CONTEXT = [
    "era_background",
    "culture_system",
    "culture_stage",
    "street_texture",
    "technology_level",
    "order_level",
    "material_ecology",
    "visual_taboo",
]
REQUIRED_OUTFIT = [
    "outerwear",
    "base_layer",
    "pants",
    "socks",
    "shoes",
    "accessories",
    "styling_algorithm",
    "base_garment_prototype",
    "outer_shell_prototype",
    "structural_event",
    "material_behavior",
    "anti_shirt_jacket_default",
    "design_operators",
    "panel_paths",
    "craft_boundaries",
    "complexity_budget",
    "design_failure_avoidance",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: validate_character.py <character.json>")

    path = Path(sys.argv[1])
    data = json.loads(path.read_text(encoding="utf-8-sig"))

    for key in REQUIRED_TOP_LEVEL:
        if key not in data:
            fail(f"missing top-level key: {key}")

    for key in REQUIRED_BASIC:
        if key not in data["basic"]:
            fail(f"missing basic key: {key}")

    for key in REQUIRED_WORLD_CONTEXT:
        if key not in data["world_context"]:
            fail(f"missing world_context key: {key}")

    for key in REQUIRED_OUTFIT:
        if key not in data["outfit"]:
            fail(f"missing outfit key: {key}")

    if not isinstance(data["outfit"]["structural_event"], dict):
        fail("outfit.structural_event must be an object")

    if not isinstance(data["outfit"]["material_behavior"], dict):
        fail("outfit.material_behavior must be an object")

    if not data["outfit"]["outer_shell_prototype"]:
        fail("outfit.outer_shell_prototype must name a precise outer shell")

    for key in ["wealth", "danger", "desire", "execution", "social"]:
        value = data["basic"][key]
        if not isinstance(value, int) or not 1 <= value <= 10:
            fail(f"basic.{key} must be an integer from 1 to 10")

    print("OK: character record shape looks valid")


if __name__ == "__main__":
    main()
