# Visual and Code QA Workflow

Use this when comparing a frontend implementation against a design, PDF, screenshot, mockup, or visual specification.

## Goal

Verify that implementation and design match in layout, visual hierarchy, spacing, typography, states, and responsive behavior.

## Required Inputs

- Source design: screenshot, PDF, Figma export, mockup, or reference image.
- Implementation target: local app URL, HTML file, screenshot, or code.
- Viewports to test: desktop, tablet, mobile, or specified sizes.
- Acceptance threshold: exact match, close match, or functional equivalence.

## Workflow

1. Inspect the source design.
2. Identify visual requirements:
   - Layout grid.
   - Component hierarchy.
   - Spacing.
   - Typography.
   - Colors.
   - Imagery.
   - Interactive states.
   - Responsive behavior.
3. Inspect implementation code.
4. Render the implementation when possible.
5. Capture screenshots at required viewports.
6. Compare screenshot against source design.
7. Record mismatches with severity.
8. Fix code or provide a QA report.
9. Re-run screenshot comparison after fixes.

## Comparison Dimensions

| Dimension | Check |
|---|---|
| Layout | positions, alignment, grid, wrapping |
| Spacing | margins, padding, gaps, density |
| Typography | font size, weight, line height, hierarchy |
| Color | palette, contrast, state colors |
| Assets | correct image, crop, aspect ratio, quality |
| Components | buttons, inputs, cards, nav, tables |
| States | hover, active, loading, empty, error |
| Responsive | mobile/desktop behavior, overflow, text fit |

## Severity

- P0: blocks use, blank screen, unreadable, major layout break.
- P1: large visual mismatch, missing key content, broken responsive layout.
- P2: noticeable mismatch, spacing, color, or typography drift.
- P3: minor polish issue.

## Report Format

Use `templates/visual-qa-report.md`.

Include:

- Source artifact.
- Implementation artifact.
- Viewports tested.
- Findings by severity.
- Screenshots or file references when available.
- Code areas likely responsible.
- Re-test result.

## Guardrails

- Do not claim visual match without rendering or inspecting the implementation when tools are available.
- Do not rely only on code review for visual fidelity.
- Do not ignore mobile unless the user explicitly says desktop-only.
- If source design is missing, state that comparison is against inferred requirements.
