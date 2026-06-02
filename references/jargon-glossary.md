# Jargon Glossary / 技術術語商業轉譯表

Use this reference when technical wording remains too dense for the target audience. Do not replace every term mechanically. Keep terms that the audience needs for accuracy, and explain them once.

## Common Replacement Pattern

| Technical Term | English Business Wording | Traditional Chinese Business Wording |
|---|---|---|
| API | integration, connection, data service | 系統整合、資料連接、資料服務 |
| endpoint | connection point, service URL | 連接點、服務網址 |
| backend | processing system | 後端處理系統、資料處理系統 |
| frontend | user interface | 使用者介面、前端畫面 |
| server | processing infrastructure | 處理系統、基礎設施 |
| deploy | launch, release, deliver | 上線、發布、交付 |
| CI/CD | automated delivery process | 自動化交付流程 |
| pipeline | automated workflow | 自動化流程 |
| database | data store | 資料庫、資料儲存系統 |
| Redis | caching system | 快取系統 |
| query | data request | 資料查詢 |
| schema | data structure | 資料結構 |
| migration | data structure update | 資料結構更新 |
| latency | response time, delay | 回應時間、延遲 |
| P99 | worst-case response time | 最差情境回應時間 |
| cache miss | temporary memory lookup failure | 快取未命中、暫存資料未找到 |
| throughput | processing capacity | 處理量、處理能力 |
| rate limit | usage cap | 使用量上限 |
| error rate | failure rate | 錯誤率、失敗率 |
| outage | service interruption | 服務中斷 |
| downtime | service interruption duration | 服務中斷時間 |
| uptime | service availability | 服務可用率 |
| bug | problem, defect | 問題、缺陷 |
| exception | unexpected error | 非預期錯誤 |
| P0 / P1 | critical / high-priority incident | 重大 / 高優先級事故 |
| technical debt | deferred maintenance | 技術債、延後維護 |
| refactor | improve code quality | 改善程式品質、重整系統結構 |
| code review | peer quality review | 同儕品質檢查 |
| PR | change proposal | 變更提案 |
| rollback | revert to previous version | 回復到前一版本 |
| feature flag | feature switch | 功能開關 |
| Kubernetes / K8s | infrastructure management platform | 基礎設施管理平台 |
| Docker / container | isolated application package | 隔離式應用程式封裝 |
| load balancer | traffic distributor | 流量分配器 |
| auto-scaling | automatic capacity adjustment | 自動調整容量 |
| memory leak | gradual resource waste | 資源逐步耗損 |
| OOM | memory exhaustion | 記憶體資源耗盡 |
| authentication | user verification | 使用者驗證 |
| authorization | access permission | 存取權限 |
| OAuth | secure login system | 安全登入機制 |
| JWT | security token | 安全憑證 |
| encryption | data protection | 資料保護 |
| vulnerability | security weakness | 資安弱點 |
| CVE | security advisory number | 資安公告編號 |
| exploit | attack method | 攻擊方式 |
| patch | security fix | 修補、資安修補 |
| unit test | component-level test | 元件層級測試 |
| integration test | system interaction test | 系統互動測試 |
| E2E test | complete user journey test | 完整使用流程測試 |
| regression | compatibility check | 相容性回歸檢查 |

## Before and After Examples

### Incident

Technical:

> Redis cache misses caused P99 API latency to increase by 400%.

Business English:

> Customer-facing response times became four times slower because our temporary data storage system was overloaded.

Traditional Chinese:

> 由於暫存資料系統負載過高，客戶端回應時間變成平常的四倍。

### Technical Debt

Technical:

> The authentication monolith has no CI/CD pipeline and 0% test coverage.

Business English:

> Our login system lacks automated quality checks, so every change requires manual validation and carries higher release risk.

Traditional Chinese:

> 我們的登入系統缺少自動化品質檢查，因此每次變更都需要人工驗證，發布風險也較高。

### Security

Technical:

> CVE in a dependency may allow prototype pollution.

Business English:

> A security weakness was found in a third-party component we use. We are applying the available fix to reduce risk to customer data.

Traditional Chinese:

> 我們使用的第三方元件發現資安弱點。團隊正在套用可用修補，以降低客戶資料風險。

## Judgment Rules

- Keep a technical term if the audience expects it, but explain it once.
- Replace terms when the audience only needs the business effect.
- Do not turn precise security, legal, or compliance terms into vague assurances.
- Prefer "not yet quantified" over invented numbers.
- For Traditional Chinese, translate the business implication, not the English sentence structure.

## Traditional Chinese Checker Notes

`scripts/check_jargon.py` also flags common Traditional Chinese technical terms. Use it as a signal, not a strict replacement engine. Some terms, such as "資料庫", "資安", "驗證", or "技術債", may be acceptable for PM or internal audiences but should often be explained for clients or executives.

Common Traditional Chinese replacements:

| Technical Chinese | Business-Friendly Chinese |
|---|---|
| 部署 | 上線、發布、交付 |
| 回滾 | 回復到前一版本 |
| 容器 | 隔離式應用程式封裝 |
| 叢集 | 基礎設施群組 |
| 節點 | 處理資源 |
| 快取 | 暫存資料 |
| 佇列 | 等待處理的工作清單 |
| 延遲 | 回應時間 |
| 限流 | 使用量限制 |
| 重構 | 改善系統結構 |
| 漏洞 | 資安弱點 |
| token | 存取憑證 |
| 測試覆蓋率 | 測試完整度 |
