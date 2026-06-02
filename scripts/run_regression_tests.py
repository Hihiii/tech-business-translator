#!/usr/bin/env python3
"""
Validate static prompt routing fixtures.

This does not call an AI model. It checks that the repository's regression
fixtures are well-formed and that expected templates exist.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    fixture_path = ROOT / "tests" / "fixtures" / "prompt_cases.json"
    cases = json.loads(fixture_path.read_text(encoding="utf-8"))
    failures: list[str] = []

    for case in cases:
        for field in ("id", "prompt", "expected_audience", "expected_language", "expected_template"):
            if not case.get(field):
                failures.append(f"{case.get('id', '<missing id>')} missing {field}")

        template = case.get("expected_template")
        if template:
            template_path = ROOT / "templates" / f"{template}.md"
            if not template_path.exists():
                failures.append(f"{case['id']} references missing template: {template}.md")

        if not case.get("must_include"):
            failures.append(f"{case['id']} must_include should not be empty")
        if not case.get("avoid_terms"):
            failures.append(f"{case['id']} avoid_terms should not be empty")

    if failures:
        print("REGRESSION FIXTURES FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"REGRESSION FIXTURES PASSED ({len(cases)} cases)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
