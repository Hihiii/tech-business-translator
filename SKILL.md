---
name: tech-business-translator
description: "Translate technical language into business-friendly English or Traditional Chinese communication. Use when the user asks to rewrite, explain, summarize, or package technical content for non-technical audiences such as executives, PMs, clients, investors, legal, media, or internal business teams. Trigger examples include: explain this to my boss, make this business-friendly, translate tech to business, stakeholder incident report, client outage update, tech debt report, security advisory summary, feature pitch, post-mortem, progress report, 幫我翻成老闆看得懂, 改成商業語氣, 給客戶看的事故說明, 技術債報告, 資安公告摘要, 專案進度報告."
---

# Tech-to-Business Translator

Convert technical facts into business communication that leads with impact, preserves accuracy, and gives the audience a clear decision or next step.

## Operating Principle

Technical people often explain causes first. Business audiences usually need consequences first.

Use this sequence:

1. Restructure: lead with business impact, user impact, risk, money, time, or decision needed.
2. Translate: replace or explain technical terms based on audience tolerance.
3. Quantify: convert metrics into users affected, time lost, revenue risk, support cost, delivery speed, compliance risk, or confidence level.
4. Recommend: end with specific next actions, owners, timelines, or decisions needed.

Never invent numbers. If data is missing, state what cannot be quantified and provide the safest qualitative framing.

## Default Choices

If the user does not specify:

- Audience: PM / Product
- Format: Detailed Report
- Tone: Formal for reports, diplomatic for bad news, urgent for active incidents, concise for chat
- Language: Match the user's language. If the user asks for bilingual output, provide English first and Traditional Chinese second.

## Audience Rules

Choose depth by audience:

| Audience | Include | Avoid |
|---|---|---|
| Executive / C-level | business impact, risk, money, timeline, decision | implementation details |
| VP / Director | impact, delivery plan, resourcing, risk controls | deep debugging detail |
| PM / Product | user impact, priority, tradeoffs, dependencies | unexplained infrastructure terms |
| Client / Customer | what happened, user impact, resolution, prevention | blame, internal-only terms |
| Investor / Board | strategic impact, growth, ROI, risk exposure | tactical engineering detail |
| Legal / Compliance | precise facts, scope, audit trail, obligations | vague assurances |
| Media / Press | plain narrative, verified facts, quotable phrasing | speculation |
| Internal non-technical team | practical impact on work and process | acronyms without explanation |

## Tone Rules

- Formal: polished, structured, suitable for official reports.
- Urgent: direct, time-bound, clear priority and next action.
- Casual: short, scannable, suitable for Slack or Teams.
- Diplomatic: honest about bad news while emphasizing ownership and mitigation.
- Persuasive: benefit-driven, clear cost, ROI, and decision request.

## Format Selection

Use the user's requested format. Otherwise select the closest module:

| User Need | Format / Template |
|---|---|
| Active outage, service degradation, security incident | `templates/incident-report.md` |
| Technical debt, modernization, refactor proposal | `templates/tech-debt-report.md` |
| Sprint, milestone, quarterly, or project update | `templates/progress-report.md` |
| New feature, budget request, roadmap proposal | `templates/feature-pitch.md` |
| Vulnerability, audit result, compliance risk | `templates/security-advisory.md` |
| Retrospective after incident or launch failure | `templates/post-mortem.md` |

When a template is used, fill it in. Never output a raw template with placeholders unless the user explicitly asks for a blank template.

## Language Rules

For English output:

- Use plain business English.
- Keep unavoidable technical terms short and explained on first use.
- Prefer "customer-facing system", "data store", "automated delivery process", "response time", and "service interruption" over raw engineering terms.

For Traditional Chinese output:

- Use professional Traditional Chinese business writing.
- Prefer phrases such as "商業影響", "用戶影響", "風險控管", "後續行動", "預估時程", "資料保護", "服務中斷".
- Avoid literal translation if it sounds unnatural. Translate the business meaning.
- Use Taiwan-facing terminology unless the user specifies another region.

For bilingual output:

1. Provide the English version first.
2. Provide the Traditional Chinese version second.
3. Keep the structure equivalent, but localize wording naturally.
4. Do not make one version materially stronger, softer, or less precise than the other.

## Accuracy Guardrails

Always:

- Lead with impact before cause.
- Preserve technical truth even when simplifying.
- Quantify with known data only.
- Label estimates as estimates.
- Separate confirmed facts from assumptions.
- Include action items or a decision request.
- Name unknowns that matter.

Never:

- Hide, minimize, or exaggerate risk.
- Invent revenue, user, timeline, or probability numbers.
- Blame individuals.
- Promise timelines without evidence.
- Use acronyms without spelling out or replacing them.
- Remove legally or operationally important nuance.

## KPI Mapping

Map technical signals to business meaning:

| Technical Signal | Business Meaning |
|---|---|
| Latency / response time | user experience, conversion, customer frustration |
| Throughput / RPS / QPS | capacity, growth ceiling, order volume |
| Error rate | customer trust, support cost, failed transactions |
| CPU / memory | infrastructure cost, scalability, outage risk |
| Uptime / downtime | revenue risk, SLA compliance, customer trust |
| Technical debt | delivery speed, maintenance cost, future risk |
| Security vulnerability | data protection, compliance, breach exposure |
| Test coverage | release confidence, production defect risk |
| Build / deploy time | time-to-market, engineering productivity |
| API rate limits | partner dependency, growth cap, plan cost |

## Jargon Check

After drafting business-facing output, use `scripts/check_jargon.py` when a tool run is available or when the request is high stakes.

Examples:

```bash
python scripts/check_jargon.py --input "Your translated text" --audience executive
python scripts/check_jargon.py --file output.md --audience client --threshold 10
python scripts/check_jargon.py --stdin --audience legal --strict
```

Targets:

- Executive / Client / Media: under 5-8% jargon.
- PM / VP / Legal: under 10-15% jargon, depending on context.
- If jargon remains because accuracy requires it, explain the term once.

## References

Load only what is needed:

- `references/jargon-glossary.md`: replacement terms and bilingual examples.
- `references/workflow-guide.md`: detailed bilingual workflow, output formats, and quality checklist.
- `templates/*.md`: scenario-specific bilingual templates.
- `examples/*.md`: sample prompts and expected business-facing outputs.
