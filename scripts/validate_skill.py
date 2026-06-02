#!/usr/bin/env python3
"""
Validate the tech-business-translator skill folder.

Checks are intentionally lightweight and dependency-free:
- required files exist
- SKILL.md has valid minimal frontmatter
- text files do not contain common mojibake markers
- templates include English and Traditional Chinese sections
- jargon checker can run
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BAD_PATTERNS = [chr(code) for code in (0xFFFD, 0x5697, 0x875C, 0x929D, 0x6470, 0x648C, 0x96FF)]
BAD_PATTERNS.extend(chr(code) for code in (0xE711, 0xEDBD, 0xEDBE, 0xEEA8))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def check_required_files(failures: list[str]) -> None:
    required = [
        "SKILL.md",
        "README.md",
        "scripts/check_jargon.py",
        "scripts/validate_skill.py",
        "references/jargon-glossary.md",
        "references/workflow-guide.md",
        "templates/incident-report.md",
        "templates/tech-debt-report.md",
        "templates/progress-report.md",
        "templates/feature-pitch.md",
        "templates/security-advisory.md",
        "templates/post-mortem.md",
        "examples/incident-bilingual.md",
        "examples/tech-debt-bilingual.md",
        "examples/security-advisory-bilingual.md",
    ]
    for rel_path in required:
        if not (ROOT / rel_path).exists():
            fail(f"Missing required file: {rel_path}", failures)


def check_frontmatter(failures: list[str]) -> None:
    skill = read(ROOT / "SKILL.md")
    match = re.match(r"^---\n(.*?)\n---\n", skill, re.DOTALL)
    if not match:
        fail("SKILL.md is missing YAML frontmatter.", failures)
        return
    frontmatter = match.group(1)
    if "name: tech-business-translator" not in frontmatter:
        fail("SKILL.md frontmatter must include name: tech-business-translator", failures)
    if "description:" not in frontmatter:
        fail("SKILL.md frontmatter must include description.", failures)
    if len(frontmatter.splitlines()) > 2:
        fail("SKILL.md frontmatter should only contain name and description.", failures)


def check_mojibake(failures: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if path.is_dir() or path.suffix.lower() not in {".md", ".py", ".yaml", ".yml"}:
            continue
        text = read(path)
        for pattern in BAD_PATTERNS:
            if pattern in text:
                fail(f"Potential mojibake marker '{pattern}' found in {path.relative_to(ROOT)}", failures)
                break


def check_templates(failures: list[str]) -> None:
    for path in (ROOT / "templates").glob("*.md"):
        text = read(path)
        if "## English Version" not in text:
            fail(f"Template missing English section: {path.name}", failures)
        if "## Traditional Chinese Version" not in text:
            fail(f"Template missing Traditional Chinese section: {path.name}", failures)


def check_jargon_script(failures: list[str]) -> None:
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "check_jargon.py"),
        "--input",
        "Our Redis API latency is high",
        "--audience",
        "executive",
        "--json",
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if proc.returncode not in {0, 1}:
        fail(f"check_jargon.py failed unexpectedly: {proc.stderr or proc.stdout}", failures)
        return
    try:
        data = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        fail(f"check_jargon.py did not return valid JSON: {exc}", failures)
        return
    if data.get("jargon_found", 0) < 1:
        fail("check_jargon.py smoke test did not detect expected jargon.", failures)


def main() -> int:
    failures: list[str] = []
    check_required_files(failures)
    check_frontmatter(failures)
    check_mojibake(failures)
    check_templates(failures)
    check_jargon_script(failures)

    if failures:
        print("VALIDATION FAILED")
        for item in failures:
            print(f"- {item}")
        return 1

    print("VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
