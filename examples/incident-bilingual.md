# Example: Bilingual Incident Update

## Prompt

Translate this for executives and clients, bilingual:

> P0: Kubernetes node pool exhausted. Pod scheduling failed for checkout API. Error rate hit 18% for 22 minutes. Rolled back v2.3.1 to v2.2.8. No data loss.

## Expected Output Shape

### English

At [time if known], checkout experienced a critical service disruption that caused some customers to receive errors during purchase. The issue lasted 22 minutes, with the failure rate reaching 18% at peak. Engineering restored service by reverting to the previous stable version. Current evidence shows no data loss.

Business impact:

- Customer impact: Some customers could not complete checkout during the affected window.
- Revenue impact: Not yet quantified.
- Data risk: No evidence of data loss.
- Current status: Service restored and under monitoring.

Next steps:

1. Confirm the number of affected customers and failed orders.
2. Review the capacity failure that prevented checkout processing.
3. Add safeguards before re-releasing version 2.3.1.

### Traditional Chinese

在[時間，如已知]，結帳服務發生重大中斷，部分客戶在購買流程中遇到錯誤。事件持續 22 分鐘，錯誤率最高達 18%。工程團隊已回復至前一個穩定版本並恢復服務。目前證據顯示沒有資料遺失。

商業影響：

- 客戶影響：部分客戶在受影響期間無法完成結帳。
- 營收影響：目前尚未量化。
- 資料風險：目前沒有資料遺失證據。
- 目前狀態：服務已恢復，並持續監控中。

後續行動：

1. 確認受影響客戶數與失敗訂單數。
2. 檢視造成結帳處理容量不足的原因。
3. 在重新發布 2.3.1 前加入防護措施。
