#!/usr/bin/env python3
"""
Score business-facing communication with lightweight heuristic checks.

This is not a substitute for human review. It catches common quality gaps:
- missing impact-first language
- missing action items
- excessive jargon
- weak risk transparency
- weak bilingual structure
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from check_jargon import check_jargon


IMPACT_TERMS = {
    "impact",
    "customer",
    "user",
    "revenue",
    "risk",
    "timeline",
    "support",
    "conversion",
    "商業影響",
    "客戶",
    "用戶",
    "營收",
    "風險",
    "時程",
    "轉換率",
}

ACTION_TERMS = {
    "next step",
    "next steps",
    "action",
    "recommendation",
    "owner",
    "due",
    "decision",
    "後續行動",
    "行動",
    "建議",
    "負責人",
    "期限",
    "決策",
}

UNCERTAINTY_TERMS = {
    "not yet quantified",
    "current evidence",
    "unknown",
    "under review",
    "estimate",
    "尚未量化",
    "目前證據",
    "待確認",
    "審查中",
    "預估",
}

RISK_TERMS = {
    "risk",
    "exposure",
    "mitigation",
    "compliance",
    "security",
    "風險",
    "暴露",
    "緩解",
    "合規",
    "資安",
}


def _contains_any(text: str, terms: set[str]) -> bool:
    lower = text.lower()
    return any(term.lower() in lower for term in terms)


def _section_present(text: str, section_names: list[str]) -> bool:
    lower = text.lower()
    return any(name.lower() in lower for name in section_names)


def score_text(text: str, audience: str = "pm") -> dict:
    jargon = check_jargon(text, audience=audience)
    first_500 = text[:500]

    checks = {
        "impact_first": _contains_any(first_500, IMPACT_TERMS),
        "actionable": _contains_any(text, ACTION_TERMS),
        "risk_transparency": _contains_any(text, RISK_TERMS) or _contains_any(text, UNCERTAINTY_TERMS),
        "uncertainty_labeled": _contains_any(text, UNCERTAINTY_TERMS)
        or "unknown" not in text.lower(),
        "bilingual_structure": (
            ("## English" in text and "## Traditional Chinese" in text)
            or ("## English Version" in text and "## Traditional Chinese Version" in text)
            or ("英文" in text and "中文" in text)
        ),
        "next_steps_section": _section_present(text, ["Next Steps", "Recommendation", "後續行動", "建議"]),
    }

    score = 0
    weights = {
        "impact_first": 20,
        "actionable": 20,
        "risk_transparency": 15,
        "uncertainty_labeled": 10,
        "bilingual_structure": 10,
        "next_steps_section": 15,
    }
    for key, weight in weights.items():
        if checks[key]:
            score += weight

    jargon_penalty = min(20, int(jargon["jargon_score"]))
    score = max(0, score - jargon_penalty)

    return {
        "score": score,
        "max_score": 90,
        "normalized_score": round(score / 90 * 100, 1),
        "checks": checks,
        "jargon_score": jargon["jargon_score"],
        "jargon_found": jargon["jargon_found"],
        "recommendation": recommendation(score / 90 * 100),
    }


def recommendation(normalized: float) -> str:
    if normalized >= 85:
        return "Strong business communication."
    if normalized >= 70:
        return "Usable with minor revision."
    if normalized >= 50:
        return "Needs revision before stakeholder use."
    return "High risk: rewrite before use."


def main() -> int:
    parser = argparse.ArgumentParser(description="Score business-facing communication output.")
    parser.add_argument("--input", "-i", help="Text to score")
    parser.add_argument("--file", "-f", help="UTF-8 text file to score")
    parser.add_argument("--audience", "-a", default="pm")
    parser.add_argument("--min-score", type=float, default=0.0, help="Minimum normalized score")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if args.file:
        text = Path(args.file).read_text(encoding="utf-8")
    else:
        text = args.input or sys.stdin.read()

    if not text.strip():
        print("No text provided.", file=sys.stderr)
        return 2

    result = score_text(text, audience=args.audience)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"Score: {result['normalized_score']}%")
        print(f"Recommendation: {result['recommendation']}")
        print(f"Jargon score: {result['jargon_score']:.1f}%")
        for key, passed in result["checks"].items():
            print(f"- {key}: {'PASS' if passed else 'FAIL'}")

    return 0 if result["normalized_score"] >= args.min_score else 1


if __name__ == "__main__":
    raise SystemExit(main())
