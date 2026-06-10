# Prompt Router

Use this guide to choose the right output path.

## Routing Rules

| Prompt Signal | Route |
|---|---|
| outage, incident, P0/P1, degraded, error spike | `templates/incident-report.md` |
| vulnerability, CVE, audit, security finding, data exposure | `templates/security-advisory.md` |
| tech debt, refactor, legacy, modernization, test coverage | `templates/tech-debt-report.md` |
| sprint, milestone, progress, quarterly update | `templates/progress-report.md` |
| feature proposal, roadmap, budget request, pitch | `templates/feature-pitch.md` |
| retrospective, post-mortem, lessons learned | `templates/post-mortem.md` |
| email, customer update, client message | `templates/client-email.md` |
| Slack, Teams, chat, short update | `templates/slack-update.md` |
| one-pager, exec brief, leadership summary | `templates/executive-brief.md` |
| decision, options, tradeoff, recommendation | `templates/decision-memo.md` |
| FAQ, support talking points, customer questions | `templates/customer-faq.md` |
| project breakdown, implementation plan, phased plan | `templates/project-plan.md` |
| delegate, subagents, workstreams, task split | `templates/task-delegation-plan.md` |
| visual QA, compare frontend to design, screenshot mismatch | `templates/visual-qa-report.md` |
| finance/legal research, document review, diligence, evidence synthesis | `templates/research-brief.md` |

## Ambiguous Prompts

- If the user asks for "business-friendly" without format, use Detailed Report.
- If the content includes active incident language, prefer Incident Report.
- If external customers are involved, use client-safe tone.
- If security or compliance appears, load `references/legal-safe-communication.md`.
- If bilingual output is requested, preserve the same sections in both languages.

## Output Pack Routing

If the user asks for a full communication package, use `output-packs/stakeholder-incident-pack.md` or `output-packs/security-communication-pack.md`.

If the user asks for autonomous project execution, planning, QA, or research delivery, use `output-packs/virtual-engineer-delivery-pack.md`.
