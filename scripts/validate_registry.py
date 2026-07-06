#!/usr/bin/env python3
"""Validate registry.yaml: required fields, unique names, sane URLs.

Run in CI on every PR. Exits non-zero on any problem.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REQUIRED = ["name", "source_url", "description", "license", "download"]
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def main() -> int:
    path = Path(__file__).resolve().parent.parent / "registry.yaml"
    data = yaml.safe_load(path.read_text()) or []
    if not isinstance(data, list):
        print("registry.yaml must be a list of entries")
        return 1

    errors: list[str] = []
    seen: set[str] = set()
    for i, e in enumerate(data):
        where = e.get("name", f"entry #{i}")
        for field in REQUIRED:
            if not e.get(field):
                errors.append(f"{where}: missing required field '{field}'")
        name = e.get("name", "")
        if name and not NAME_RE.match(name):
            errors.append(f"{where}: name must be kebab-case [a-z0-9-]")
        if name in seen:
            errors.append(f"{where}: duplicate name")
        seen.add(name)
        dl = e.get("download", "")
        if dl and not (dl.startswith("https://") and dl.endswith(".zip")):
            errors.append(f"{where}: download must be an https URL ending in .zip")
        src = e.get("source_url", "")
        if src and not src.startswith(("http://", "https://")):
            errors.append(f"{where}: source_url must be a URL")

    if errors:
        print("Registry validation failed:")
        for err in errors:
            print(f"  ✗ {err}")
        return 1
    print(f"registry.yaml OK — {len(data)} bundle(s), all fields valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
