# Self-check and Test Guide

Use this before delivering substantial work.

## Universal Delivery Checklist

- The output answers the user's latest request.
- Scope and assumptions are stated.
- Required format and language are satisfied.
- Numbers, dates, names, and risk claims are preserved.
- Unknowns are explicit.
- Next steps are actionable.

## Code Work

Run the most relevant checks available:

- Unit tests.
- Typecheck.
- Lint.
- Build.
- Smoke test.
- Browser or UI verification for frontend work.

If a check cannot run, state why.

## Visual Work

Check:

- Rendered screenshot exists.
- Desktop and mobile were inspected when relevant.
- Text does not overlap.
- Assets render.
- Layout matches the design within stated tolerance.
- Interactive states work when relevant.

## Research Work

Check:

- Every material claim has a source.
- Sources are current enough for the task.
- Legal/financial conclusions are caveated.
- Contradictory evidence is disclosed.
- The final deliverable separates facts from interpretation.

## Business Communication

Run or mentally apply:

- `scripts/check_jargon.py`
- `scripts/check_bilingual_consistency.py` for bilingual output.
- `scripts/score_output.py` for substantial artifacts.
- `references/red-team-checklist.md` for high-risk outputs.

## Final Response

Include:

- What changed or was produced.
- Validation performed.
- Any residual risk.
- Where the artifact is located, if applicable.
