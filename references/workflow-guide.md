# Workflow Guide / 工作流程指南

Use this when the task needs more detail than the main `SKILL.md` provides.

## Decision Flow

1. Identify audience.
2. Identify language: English, Traditional Chinese, or bilingual.
3. Identify format: summary, report, chat, email, presentation outline, or one of the templates.
4. Extract confirmed facts, metrics, unknowns, and requested decisions.
5. Convert technical facts into business consequences.
6. Draft the output.
7. Run or mentally apply the jargon check.
8. Revise for clarity, accuracy, and tone.

## Output Formats

### Executive Summary

Use 1 paragraph:

1. What happened or what is proposed.
2. Business impact.
3. Action, decision, or next step.

### Detailed Report

Use:

- Background
- Business Impact
- Root Cause or Driver
- Action Plan
- Risks and Mitigation
- Decision Needed or Next Steps

### Slack / Chat

Use:

- 3-5 short bullets.
- Start with status and impact.
- Include ETA only when evidence supports it.
- Avoid emoji unless the user asks for it.

### Email

Use:

- Subject line.
- Short opening summary.
- Structured sections.
- Clear next step or decision request.

### Presentation Outline

Use:

- Slide title.
- Main message.
- Talking points.
- Suggested visual.

## Bilingual Output Pattern

Use this structure when the user asks for bilingual output:

```markdown
## English

[English output]

## Traditional Chinese

[Traditional Chinese output]
```

For long reports, keep section order the same in both languages.

## Quantification Prompts

If the source includes technical metrics, ask what they mean in business terms:

| Source Metric | Conversion Question |
|---|---|
| Error count | How many users, orders, sessions, or support tickets were affected? |
| Latency | How much slower did the user experience become? |
| Downtime | Was revenue, SLA, customer trust, or operations affected? |
| Engineering effort | What roadmap work is delayed or accelerated? |
| Infrastructure usage | Does this increase cost or limit growth? |
| Security weakness | What data, obligation, or customer commitment is at risk? |

## Missing Data Language

Use these phrases instead of inventing numbers:

- "The financial impact has not been quantified yet."
- "Current evidence does not indicate customer data exposure."
- "The affected user count is still being validated."
- "This is an estimate and should be confirmed after log review."
- "Based on current information, the risk appears limited to..."

Traditional Chinese:

- "目前尚未量化財務影響。"
- "目前證據未顯示客戶資料外洩。"
- "受影響用戶數仍在確認中。"
- "此為初步估算，需待紀錄檢視後確認。"
- "依目前資訊判斷，風險範圍限於..."

## Quality Checklist

Before finalizing:

- Impact appears before technical cause.
- Audience depth is appropriate.
- Unknowns are clearly labeled.
- Metrics are translated into business value where possible.
- No unexplained acronyms remain.
- Recommendations are specific and actionable.
- Risk is neither hidden nor exaggerated.
- English and Traditional Chinese versions are equivalent in meaning when bilingual.
