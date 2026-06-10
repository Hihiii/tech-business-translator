# Delegation Guide

Use this when the user asks to delegate tasks or when the work is large enough to benefit from subagents or simulated workstreams.

## Delegation Decision

Use real subagents only when the runtime supports them. If unavailable, simulate delegation by splitting the work into named workstreams and executing sequentially.

Good delegation targets:

- Independent research questions.
- Separate document sets.
- Frontend visual QA vs code review.
- Test generation vs implementation.
- Drafting separate audience versions.
- Risk review after a first draft exists.

Avoid delegation when:

- The task is small.
- Outputs would be tightly coupled.
- The subagent would need hidden context not available in the prompt.
- The work requires a single source of truth or exact file edits.

## Assignment Format

Each delegated task should include:

| Field | Content |
|---|---|
| Task ID | Stable short name |
| Goal | One concrete outcome |
| Inputs | Files, URLs, screenshots, constraints |
| Output | Required artifact format |
| Guardrails | What not to do |
| Validation | How success will be checked |
| Integration | How output will be used |

## Subagent Prompt Pattern

Use this shape:

```text
Use the skill at [path/name] to complete this task:

Goal: [goal]
Inputs: [files or facts]
Output: [artifact]
Guardrails: [constraints]
Validation: [checks]
Do not modify files unless explicitly asked.
```

Do not leak expected answers unless the subagent is validating a known target.

## Integration Checklist

- Did every workstream return the expected artifact?
- Are claims consistent across outputs?
- Are numbers, dates, and source references consistent?
- Are open questions still visible?
- Did final synthesis remove duplicated or contradictory recommendations?

## Bilingual Delegation

If a workstream drafts bilingual output:

- English and Traditional Chinese sections must preserve the same facts.
- Numbers and dates must match.
- Risk language must not be softened in one language.
- Use `scripts/check_bilingual_consistency.py` when available.
