# Example: Bilingual Technical Debt Report

## Prompt

Make this business-friendly for a VP, bilingual:

> Auth service is a 5-year-old monolith with 0% test coverage, hardcoded secrets, and no CI pipeline. Every auth change takes 2 days of manual testing.

## Expected Output Shape

### English

Our login system has become a delivery and security risk. Because it lacks automated quality checks and contains outdated security practices, every change requires about two days of manual testing and carries higher release risk.

Business impact:

- Delivery speed: Login-related changes are slower than they need to be, delaying product work that depends on account access.
- Security risk: Hardcoded credentials create unnecessary exposure and should be removed.
- Operational risk: Manual testing increases the chance of missed issues and inconsistent release quality.

Recommendation:

Approve a modernization effort focused on automated testing, credential cleanup, and automated delivery. Success should be measured by reducing login-related change validation from two days to hours, while lowering security exposure.

### Traditional Chinese

我們的登入系統已成為交付速度與資安風險。由於缺少自動化品質檢查，且仍存在過時的安全做法，每次登入相關變更都需要約兩天人工測試，發布風險也較高。

商業影響：

- 交付速度：登入相關變更耗時過長，會延後依賴帳號存取功能的產品工作。
- 資安風險：硬編碼憑證造成不必要的暴露風險，應優先移除。
- 營運風險：人工測試提高遺漏問題與發布品質不一致的機率。

建議：

核准一項現代化改善計畫，重點包含自動化測試、憑證清理與自動化交付。成功指標應包含將登入相關變更驗證時間從兩天縮短到數小時，並降低資安暴露。
