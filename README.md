# Tech-to-Business Translator

An AI skill for translating technical details into business-friendly communication in English, Traditional Chinese, or bilingual output.

This skill helps AI turn engineering facts into stakeholder-ready messages for executives, product managers, clients, investors, legal teams, media, and internal non-technical teams.

## What It Does

- Rewrites technical updates into business language.
- Leads with business impact instead of implementation detail.
- Converts technical metrics into user, revenue, risk, delivery, or compliance impact.
- Produces English, Traditional Chinese, or bilingual output.
- Provides reusable templates for incidents, technical debt, progress reports, feature pitches, security advisories, and post-mortems.
- Includes a jargon checker to flag remaining technical terms.

## Typical Prompts

English:

- "Explain this to my boss."
- "Make this business-friendly."
- "Write a stakeholder incident report."
- "Turn this technical debt into an executive proposal."
- "Write a client-friendly security advisory."
- "Create a bilingual post-mortem."

Traditional Chinese:

- "幫我翻成老闆看得懂。"
- "改成商業語氣。"
- "寫一份給客戶看的事故說明。"
- "幫我整理技術債報告。"
- "產出中英文資安公告摘要。"
- "做一份雙語事後檢討。"

## Core Workflow

The skill follows four steps:

1. **Restructure**: Put impact, risk, decision, or user consequence first.
2. **Translate**: Replace or explain technical terms based on the audience.
3. **Quantify**: Map metrics to business value where data exists.
4. **Recommend**: End with concrete actions, owners, timelines, or decisions needed.

The default output is a detailed report for a PM/Product audience. If the user asks for bilingual output, English appears first and Traditional Chinese second.

## Folder Structure

```text
tech-business-translator/
  SKILL.md
  README.md
  templates/
    incident-report.md
    tech-debt-report.md
    progress-report.md
    feature-pitch.md
    security-advisory.md
    post-mortem.md
  references/
    jargon-glossary.md
    workflow-guide.md
  examples/
    incident-bilingual.md
    tech-debt-bilingual.md
    security-advisory-bilingual.md
  scripts/
    check_jargon.py
    validate_skill.py
```

## Templates

Each template includes an English section and a Traditional Chinese section:

- `incident-report.md`: outages, service degradation, security incidents.
- `tech-debt-report.md`: modernization, refactoring, legacy system risk.
- `progress-report.md`: sprint, milestone, quarterly, or stakeholder updates.
- `feature-pitch.md`: feature proposals and budget requests.
- `security-advisory.md`: vulnerabilities, audit findings, compliance risk.
- `post-mortem.md`: retrospective analysis after incidents or process failures.

## Jargon Checker

Run the checker after drafting business-facing output:

```bash
python scripts/check_jargon.py --input "Our Redis API latency is high" --audience executive
python scripts/check_jargon.py --file output.md --audience client --threshold 10
python scripts/check_jargon.py --stdin --audience legal --strict
```

Useful options:

- `--audience executive|vp|pm|client|legal|media`
- `--allow-term API`
- `--threshold 10`
- `--strict`
- `--json`

## Validation

Run the skill validation script:

```bash
python scripts/validate_skill.py
```

It checks required files, `SKILL.md` frontmatter, common mojibake markers, bilingual template sections, and the jargon checker smoke test.

## Chinese README / 中文說明

`tech-business-translator` 是一個給 AI 使用的 skill，用來把技術內容轉成商業受眾看得懂的英文、繁體中文或中英文雙語訊息。

適用情境包含：

- 給主管或高階主管看的技術摘要。
- 給客戶看的事故說明。
- 技術債或系統現代化投資提案。
- 專案進度報告。
- 功能提案與預算申請。
- 資安公告與合規風險說明。
- 事故後的事後檢討。

核心原則：

1. **先講影響**：先說用戶、營收、風險、時程或決策影響。
2. **再講原因**：用白話說明技術原因，避免不必要的術語。
3. **能量化就量化**：把數據轉成用戶數、時間、金額、風險或交付速度。
4. **提出行動**：最後給出建議、負責人、時程或待決策事項。

範例提示：

```text
幫我把這段技術事故說明改成給客戶看的版本，請中英文雙語。
```

```text
把這段技術債整理成 VP 會關心的商業提案，包含風險、成本與建議。
```

```text
請把這個 CVE 說明改成客戶友善的資安公告。
```

## Extension Guide

To add a new scenario:

1. Add a bilingual template in `templates/`.
2. Add one realistic example in `examples/`.
3. Add any recurring terms to `references/jargon-glossary.md`.
4. Update `SKILL.md` only if the new scenario changes the core trigger or workflow.
5. Run `python scripts/validate_skill.py`.
