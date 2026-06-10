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
- Supports virtual engineering workflows: project decomposition, task delegation, visual QA, self-checking, testing, and document-heavy research briefs.

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

## Installation

Install this skill by cloning the repository into your agent's skills directory.

Codex:

```bash
git clone https://github.com/Hihiii/tech-business-translator.git ~/.codex/skills/tech-business-translator
```

Codex on Windows PowerShell:

```powershell
git clone https://github.com/Hihiii/tech-business-translator.git "$env:USERPROFILE\.codex\skills\tech-business-translator"
```

Hermes Agent:

```bash
git clone https://github.com/Hihiii/tech-business-translator.git ~/.hermes/skills/tech-business-translator
```

Hermes Agent with an optional category folder:

```bash
git clone https://github.com/Hihiii/tech-business-translator.git ~/.hermes/skills/business/tech-business-translator
```

After installation, start a new Codex or Hermes session so the skill metadata can be discovered.

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
    audience-guide.md
    tone-guide.md
    legal-safe-communication.md
    red-team-checklist.md
    domain-kpi-mapping.md
    router.md
    zh-tw-style-guide.md
    virtual-engineer-operating-model.md
    delegation-guide.md
    visual-code-qa.md
    unattended-research-guide.md
    self-check-test-guide.md
  examples/
    incident-bilingual.md
    tech-debt-bilingual.md
    security-advisory-bilingual.md
  scripts/
    check_jargon.py
    check_bilingual_consistency.py
    check_delivery_readiness.py
    score_output.py
    run_regression_tests.py
    validate_skill.py
  output-packs/
    stakeholder-incident-pack.md
    security-communication-pack.md
    virtual-engineer-delivery-pack.md
  showcase/
    before-after.md
```

## Templates

Each template includes an English section and a Traditional Chinese section:

- `incident-report.md`: outages, service degradation, security incidents.
- `tech-debt-report.md`: modernization, refactoring, legacy system risk.
- `progress-report.md`: sprint, milestone, quarterly, or stakeholder updates.
- `feature-pitch.md`: feature proposals and budget requests.
- `security-advisory.md`: vulnerabilities, audit findings, compliance risk.
- `post-mortem.md`: retrospective analysis after incidents or process failures.
- `client-email.md`: customer-facing emails and external updates.
- `slack-update.md`: short internal Slack, Teams, or chat updates.
- `executive-brief.md`: leadership one-pagers and board pre-reads.
- `decision-memo.md`: options, tradeoffs, and recommendation memos.
- `customer-faq.md`: customer support FAQ and talking points.
- `project-plan.md`: project decomposition, phases, workstreams, validation.
- `task-delegation-plan.md`: real subagent or simulated workstream delegation.
- `visual-qa-report.md`: frontend/design visual comparison reports.
- `research-brief.md`: finance, legal, compliance, or diligence research briefs.

## Quality Tools

Jargon check:

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

Bilingual consistency check:

```bash
python scripts/check_bilingual_consistency.py --file output.md
```

Output quality score:

```bash
python scripts/score_output.py --file output.md --audience executive --min-score 70
```

Delivery readiness check:

```bash
python scripts/check_delivery_readiness.py --file output.md --mode research
python scripts/check_delivery_readiness.py --file visual-qa.md --mode visual
```

Regression fixture check:

```bash
python scripts/run_regression_tests.py
```

## Validation

Run the skill validation script:

```bash
python scripts/validate_skill.py
```

It checks required files, `SKILL.md` frontmatter, common mojibake markers, bilingual template sections, and the jargon checker smoke test.

## Advanced References

- `references/audience-guide.md`: audience-specific depth and emphasis.
- `references/tone-guide.md`: tone-specific phrasing and guardrails.
- `references/zh-tw-style-guide.md`: Taiwan-facing Traditional Chinese business style.
- `references/legal-safe-communication.md`: safe wording for legal, security, and customer-facing communication.
- `references/red-team-checklist.md`: final review checklist for high-risk outputs.
- `references/domain-kpi-mapping.md`: SaaS, e-commerce, fintech, healthcare, and B2B KPI mapping.
- `references/router.md`: prompt-to-template routing rules.
- `references/virtual-engineer-operating-model.md`: autonomous project planning, execution, integration, and verification.
- `references/delegation-guide.md`: subagent and workstream assignment rules.
- `references/visual-code-qa.md`: frontend/design screenshot comparison workflow.
- `references/unattended-research-guide.md`: finance, legal, compliance, and document-heavy research workflow.
- `references/self-check-test-guide.md`: testing and delivery readiness checks.
- `output-packs/`: multi-audience communication packs.
- `showcase/before-after.md`: example transformation from technical input to business output.

## Chinese README / 中文說明

`tech-business-translator` 是一個給 AI 使用的 skill，用來把技術內容轉成商業受眾看得懂的英文、繁體中文或中英文雙語訊息。

安裝方式：

Codex：

```powershell
git clone https://github.com/Hihiii/tech-business-translator.git "$env:USERPROFILE\.codex\skills\tech-business-translator"
```

Hermes Agent：

```bash
git clone https://github.com/Hihiii/tech-business-translator.git ~/.hermes/skills/tech-business-translator
```

或依分類放置：

```bash
git clone https://github.com/Hihiii/tech-business-translator.git ~/.hermes/skills/business/tech-business-translator
```

安裝後，請開啟新的 Codex 或 Hermes session，讓系統重新讀取 skill metadata。

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
