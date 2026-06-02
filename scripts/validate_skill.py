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
        "scripts/check_bilingual_consistency.py",
        "scripts/score_output.py",
        "scripts/run_regression_tests.py",
        "scripts/validate_skill.py",
        "references/jargon-glossary.md",
        "references/workflow-guide.md",
        "references/audience-guide.md",
        "references/tone-guide.md",
        "references/zh-tw-style-guide.md",
        "references/legal-safe-communication.md",
        "references/red-team-checklist.md",
        "references/domain-kpi-mapping.md",
        "references/router.md",
        "templates/incident-report.md",
        "templates/tech-debt-report.md",
        "templates/progress-report.md",
        "templates/feature-pitch.md",
        "templates/security-advisory.md",
        "templates/post-mortem.md",
        "templates/client-email.md",
        "templates/slack-update.md",
        "templates/executive-brief.md",
        "templates/decision-memo.md",
        "templates/customer-faq.md",
        "examples/incident-bilingual.md",
        "examples/tech-debt-bilingual.md",
        "examples/security-advisory-bilingual.md",
        "examples/progress-report-bilingual.md",
        "examples/feature-pitch-bilingual.md",
        "examples/post-mortem-bilingual.md",
        "examples/client-email-bilingual.md",
        "examples/slack-update-bilingual.md",
        "examples/decision-memo-bilingual.md",
        "examples/customer-faq-bilingual.md",
        "output-packs/stakeholder-incident-pack.md",
        "output-packs/security-communication-pack.md",
        "showcase/before-after.md",
        "tests/fixtures/prompt_cases.json",
        ".github/workflows/validate.yml",
        "LICENSE",
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
    proc = subprocess.run(cmd, capture_output=True)
    if proc.returncode not in {0, 1}:
        stdout = proc.stdout.decode("utf-8", errors="replace")
        stderr = proc.stderr.decode("utf-8", errors="replace")
        fail(f"check_jargon.py failed unexpectedly: {stderr or stdout}", failures)
        return
    try:
        data = json.loads(proc.stdout.decode("utf-8", errors="replace"))
    except json.JSONDecodeError as exc:
        fail(f"check_jargon.py did not return valid JSON: {exc}", failures)
        return
    if data.get("jargon_found", 0) < 1:
        fail("check_jargon.py smoke test did not detect expected jargon.", failures)


def check_auxiliary_scripts(failures: list[str]) -> None:
    commands = [
        [
            sys.executable,
            str(ROOT / "scripts" / "check_bilingual_consistency.py"),
            "--file",
            str(ROOT / "examples" / "incident-bilingual.md"),
            "--json",
        ],
        [
            sys.executable,
            str(ROOT / "scripts" / "score_output.py"),
            "--input",
            "## English\nCustomer impact is clear. Next steps: monitor risk.\n\n## Traditional Chinese\n客戶影響明確。後續行動：監控風險。",
            "--audience",
            "client",
            "--json",
        ],
        [
            sys.executable,
            str(ROOT / "scripts" / "run_regression_tests.py"),
        ],
    ]
    for cmd in commands:
        proc = subprocess.run(cmd, capture_output=True)
        if proc.returncode != 0:
            stdout = proc.stdout.decode("utf-8", errors="replace")
            stderr = proc.stderr.decode("utf-8", errors="replace")
            fail(f"Auxiliary script failed: {' '.join(cmd)}\n{stderr or stdout}", failures)


def main() -> int:
    failures: list[str] = []
    check_required_files(failures)
    check_frontmatter(failures)
    check_mojibake(failures)
    check_templates(failures)
    check_jargon_script(failures)
    check_auxiliary_scripts(failures)

    if failures:
        print("VALIDATION FAILED")
        for item in failures:
            print(f"- {item}")
        return 1

    print("VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
