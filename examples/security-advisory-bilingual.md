# Example: Bilingual Security Advisory

## Prompt

Write a client-friendly security advisory, bilingual:

> CVE-2026-1234 in lodash v4.17.20 allows prototype pollution. Affects user data serialization. Fix is upgrade to v4.17.21. No exploitation observed.

## Expected Output Shape

### English

We identified a security weakness in a third-party component used by our service. The issue could affect how user data is processed, but we have not observed evidence of exploitation.

Current status:

- Risk level: [Set based on internal assessment]
- Customer data: No evidence of compromise at this time.
- Remediation: We are upgrading the affected component to the fixed version.
- Customer action: No action is required unless otherwise notified.

Next steps:

1. Complete the component upgrade.
2. Verify that affected data-processing paths are protected.
3. Continue monitoring for related activity.

### Traditional Chinese

我們發現服務使用的第三方元件存在一項資安弱點。此問題可能影響使用者資料的處理方式，但目前沒有發現遭利用的證據。

目前狀態：

- 風險等級：[依內部評估填寫]
- 客戶資料：目前沒有資料遭入侵的證據。
- 修補方式：我們正在將受影響元件升級至已修復版本。
- 客戶行動：除非另行通知，客戶目前不需要採取行動。

後續行動：

1. 完成元件升級。
2. 驗證受影響的資料處理流程已受到保護。
3. 持續監控相關活動。
