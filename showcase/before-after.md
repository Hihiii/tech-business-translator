# Showcase: Before and After

## Raw Technical Input

P0: Kubernetes node pool exhausted. Checkout API pod scheduling failed. Error rate hit 18% for 22 minutes. Rolled back v2.3.1 to v2.2.8. No data loss.

## Poor Business Output

K8s ran out of nodes and pods could not schedule, so the checkout API failed. We rolled back the deployment.

Problems:

- Leads with infrastructure.
- Does not explain customer impact.
- Does not state current status.
- Does not preserve "no data loss".
- No next steps.

## Improved Business Output

### English

Checkout experienced a critical 22-minute service disruption that caused some customers to receive errors during purchase. The failure rate reached 18% at peak. Engineering restored service by reverting to the previous stable version, and current evidence shows no data loss.

Next steps:

1. Confirm affected customer and failed order counts.
2. Review the capacity failure that blocked checkout processing.
3. Add safeguards before re-releasing version 2.3.1.

### Traditional Chinese

結帳服務發生 22 分鐘重大中斷，部分客戶在購買流程中遇到錯誤。錯誤率最高達 18%。工程團隊已回復至前一個穩定版本並恢復服務，目前證據顯示沒有資料遺失。

後續行動：

1. 確認受影響客戶數與失敗訂單數。
2. 檢視造成結帳處理受阻的容量問題。
3. 在重新發布 2.3.1 前加入防護措施。
