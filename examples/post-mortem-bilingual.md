# Example: Bilingual Post-Mortem

## Prompt

Create a bilingual post-mortem summary:

> Deployment config missed a feature flag default. 12% of users saw blank dashboard for 38 minutes. Alert fired after support tickets, not monitoring. Fix deployed. Need monitoring for blank states.

## Expected Traits

- Avoid blaming individuals.
- Preserve 12%, 38 minutes, support-ticket detection gap.
- Include monitoring improvement.

## English Sample

For 38 minutes, 12% of users saw a blank dashboard because a release configuration did not include the expected feature default. The issue was resolved with a corrective update. The larger process gap is that support tickets detected the issue before monitoring did, so the prevention plan should include automated checks for blank dashboard states.

## Traditional Chinese Sample

有 38 分鐘期間，12% 的用戶看到空白儀表板，原因是發布設定未包含預期的功能預設值。團隊已透過修正更新解決問題。更重要的流程缺口是，問題先由客服工單發現，而不是由監控系統偵測，因此預防計畫應加入空白儀表板狀態的自動監控。
