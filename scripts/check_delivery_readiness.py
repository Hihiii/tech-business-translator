#!/usr/bin/env python3
"""
Check whether a delivery artifact contains the minimum sections expected for
virtual engineering, visual QA, or document-heavy research work.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


MODE_REQUIREMENTS = {
    "project": [
        ["objective", "目標"],
        ["scope", "範圍"],
        ["phases", "階段"],
        ["validation", "驗證"],
        ["risks", "風險"],
    ],
    "delegation": [
        ["goal", "目標"],
        ["inputs", "輸入"],
        ["output", "產出"],
        ["validation", "驗證"],
        ["integration", "整合"],
    ],
    "visual": [
        ["source", "原始設計"],
        ["implementation", "實作"],
        ["viewport", "視窗"],
        ["findings", "發現"],
        ["re-test", "複測"],
    ],
    "research": [
        ["research question", "研究問題"],
        ["source", "來源"],
        ["findings", "發現"],
        ["confidence", "信心"],
        ["risks", "風險"],
        ["next steps", "後續"],
    ],
    "communication": [
        ["impact", "影響"],
        ["status", "狀態"],
        ["action", "行動"],
        ["risk", "風險"],
    ],
}


def check(text: str, mode: str) -> dict:
    lower = text.lower()
    missing = []
    for alternatives in MODE_REQUIREMENTS[mode]:
        if not any(term.lower() in lower for term in alternatives):
            missing.append(alternatives)
    return {
        "mode": mode,
        "passed": not missing,
        "missing": missing,
        "required_groups": MODE_REQUIREMENTS[mode],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check delivery artifact readiness.")
    parser.add_argument("--file", "-f", help="UTF-8 artifact file")
    parser.add_argument("--input", "-i", help="Artifact text")
    parser.add_argument("--mode", choices=sorted(MODE_REQUIREMENTS), required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if args.file:
        text = Path(args.file).read_text(encoding="utf-8")
    else:
        text = args.input or sys.stdin.read()

    if not text.strip():
        print("No text provided.", file=sys.stderr)
        return 2

    result = check(text, args.mode)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("PASSED" if result["passed"] else "FAILED")
        for group in result["missing"]:
            print(f"- Missing one of: {', '.join(group)}")

    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
