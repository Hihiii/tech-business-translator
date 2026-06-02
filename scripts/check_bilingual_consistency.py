#!/usr/bin/env python3
"""
Check basic consistency between English and Traditional Chinese sections.

The script checks structure, numbers, dates, and action item counts. It is a
guardrail, not a semantic translation judge.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


EN_MARKERS = ["## English", "## English Version", "### English"]
ZH_MARKERS = ["## Traditional Chinese", "## Traditional Chinese Version", "### Traditional Chinese"]


def split_sections(text: str) -> tuple[str, str] | None:
    en_pos = min((text.find(marker) for marker in EN_MARKERS if marker in text), default=-1)
    zh_pos = min((text.find(marker) for marker in ZH_MARKERS if marker in text), default=-1)
    if en_pos == -1 or zh_pos == -1:
        return None
    if en_pos < zh_pos:
        return text[en_pos:zh_pos], text[zh_pos:]
    return text[en_pos:], text[zh_pos:en_pos]


def extract_numbers(text: str) -> list[str]:
    return re.findall(r"\b\d+(?:\.\d+)?%?|\$\d+(?:,\d{3})*(?:\.\d+)?\b", text)


def extract_dates(text: str) -> list[str]:
    patterns = [
        r"\b\d{4}-\d{2}-\d{2}\b",
        r"\b(?:Jan|Feb|Mar|Apr|May|Jun|June|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2}\b",
        r"\b\d{1,2}\s*月\s*\d{1,2}\s*日\b",
    ]
    dates: list[str] = []
    for pattern in patterns:
        dates.extend(re.findall(pattern, text, flags=re.IGNORECASE))
    return dates


def count_action_items(text: str) -> int:
    return len(re.findall(r"(?m)^\s*(?:\d+\.|- )", text))


def check_consistency(text: str) -> dict:
    sections = split_sections(text)
    if not sections:
        return {
            "passed": False,
            "issues": ["Missing English and Traditional Chinese section markers."],
        }

    en, zh = sections
    issues = []
    en_numbers = extract_numbers(en)
    zh_numbers = extract_numbers(zh)
    if sorted(en_numbers) != sorted(zh_numbers):
        issues.append(f"Number mismatch: English={en_numbers}, Traditional Chinese={zh_numbers}")

    en_dates = extract_dates(en)
    zh_dates = extract_dates(zh)
    if en_dates and not zh_dates:
        issues.append("English contains dates but Traditional Chinese has no matching date-like values.")

    en_actions = count_action_items(en)
    zh_actions = count_action_items(zh)
    if abs(en_actions - zh_actions) > 1:
        issues.append(f"Action/bullet count differs: English={en_actions}, Traditional Chinese={zh_actions}")

    risk_terms = ["risk", "security", "compliance", "breach", "風險", "資安", "合規", "外洩"]
    en_has_risk = any(term in en.lower() for term in risk_terms[:4])
    zh_has_risk = any(term in zh for term in risk_terms[4:])
    if en_has_risk and not zh_has_risk:
        issues.append("English mentions risk/security/compliance but Traditional Chinese may not.")

    return {
        "passed": not issues,
        "issues": issues,
        "english_numbers": en_numbers,
        "traditional_chinese_numbers": zh_numbers,
        "english_action_count": en_actions,
        "traditional_chinese_action_count": zh_actions,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check bilingual output consistency.")
    parser.add_argument("--input", "-i", help="Text to check")
    parser.add_argument("--file", "-f", help="UTF-8 text file to check")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if args.file:
        text = Path(args.file).read_text(encoding="utf-8")
    else:
        text = args.input or sys.stdin.read()

    result = check_consistency(text)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("PASSED" if result["passed"] else "FAILED")
        for issue in result.get("issues", []):
            print(f"- {issue}")

    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
