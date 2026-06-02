#!/usr/bin/env python3
"""
Check business-facing text for technical jargon.

The script is intentionally ASCII-safe so it works in Windows terminals and CI.

Usage:
    python scripts/check_jargon.py --input "Our Redis API latency is high"
    python scripts/check_jargon.py --file report.md
    echo "The endpoint failed" | python scripts/check_jargon.py --stdin
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Iterable


TECH_JARGON = {
    # Interfaces and protocols
    "API": "integration, connection, data service",
    "APIs": "integrations, connections, data services",
    "endpoint": "connection point, service URL",
    "REST": "web service",
    "GraphQL": "data query service",
    "gRPC": "service communication",
    "HTTP": "web protocol",
    "HTTPS": "secure web protocol",
    "TCP": "network protocol",
    "UDP": "network protocol",
    "DNS": "domain name system",
    "webhook": "automatic notification",
    "callback": "automatic notification",
    # Security and identity
    "SSL": "encryption",
    "TLS": "encryption",
    "TLS handshake": "security connection",
    "OAuth": "secure login system",
    "OAuth2": "secure login system",
    "JWT": "security token",
    "SAML": "login system",
    "LDAP": "directory service",
    "RBAC": "access control",
    "IAM": "access management",
    "ACL": "access control list",
    "authentication": "user verification",
    "authorization": "access permission",
    "encryption": "data protection",
    "hash": "security fingerprint",
    "token": "access credential",
    "certificate": "security credential",
    "PKI": "security infrastructure",
    "XSS": "security vulnerability",
    "CSRF": "security vulnerability",
    "CVE": "security advisory number",
    "OWASP": "security standard",
    "SQL injection": "security vulnerability",
    "DDoS": "availability attack",
    "zero-day": "unknown vulnerability",
    "pentest": "security test",
    "pen test": "security test",
    "vulnerability": "security weakness",
    "vulnerabilities": "security weaknesses",
    "exploit": "security attack",
    "patch": "security fix",
    "hotfix": "emergency fix",
    # Application architecture
    "backend": "processing system",
    "back-end": "processing system",
    "frontend": "user interface",
    "front-end": "user interface",
    "fullstack": "complete system",
    "full-stack": "complete system",
    "server": "processing system, infrastructure",
    "client": "user application",
    "microservice": "service module, component",
    "microservices": "service modules, components",
    "monolith": "single large system",
    "middleware": "intermediate layer",
    "daemon": "background process",
    "sidecar": "supporting service",
    "service mesh": "service communication layer",
    "gateway": "access point",
    "proxy": "intermediary, relay",
    # Delivery and operations
    "deploy": "launch, release, deliver",
    "deployment": "launch, release",
    "CI/CD": "automated delivery process",
    "CICD": "automated delivery process",
    "pipeline": "automated process, workflow",
    "container": "isolated application package",
    "containerization": "application packaging",
    "Docker": "container technology",
    "Kubernetes": "infrastructure management",
    "K8s": "infrastructure management",
    "Helm": "configuration tool",
    "Terraform": "infrastructure automation",
    "Pulumi": "infrastructure automation",
    "Ansible": "configuration automation",
    "provisioning": "setup and configuration",
    "rollback": "revert to previous version",
    "roll back": "revert to previous version",
    "canary": "gradual rollout test",
    "blue-green": "parallel deployment",
    "feature flag": "feature switch",
    "toggle": "feature switch",
    # Data and storage
    "database": "data store",
    "SQL": "database query",
    "NoSQL": "flexible data store",
    "PostgreSQL": "database system",
    "MySQL": "database system",
    "MongoDB": "database system",
    "Redis": "caching system",
    "Elasticsearch": "search system",
    "Cassandra": "database system",
    "DynamoDB": "database system",
    "index": "search optimization",
    "indexes": "search optimizations",
    "query": "data request",
    "queries": "data requests",
    "schema": "data structure",
    "table": "data collection",
    "sharding": "data distribution",
    "replication": "data backup or copy",
    "ORM": "data access layer",
    "migration": "database update",
    "migrations": "database updates",
    "ETL": "data processing workflow",
    "data lake": "data repository",
    "data warehouse": "analytical data store",
    # Performance and reliability
    "latency": "response time, delay",
    "throughput": "processing capacity",
    "bandwidth": "data transfer rate",
    "P99": "worst-case response time",
    "P95": "nearly worst-case response time",
    "P50": "median response time",
    "QPS": "queries per second",
    "RPS": "requests per second",
    "TPS": "transactions per second",
    "cache": "temporary memory",
    "caching": "temporary memory",
    "cache miss": "memory lookup failure",
    "cache hit": "memory lookup success",
    "CDN": "content delivery network",
    "load balancer": "traffic distributor",
    "auto-scaling": "automatic capacity adjustment",
    "autoscaling": "automatic capacity adjustment",
    "rate limit": "usage cap",
    "throttling": "usage limiting",
    "outage": "service interruption",
    "downtime": "service interruption",
    "uptime": "service availability",
    "SLA": "service guarantee",
    "SLO": "service target",
    "SRE": "reliability engineering team",
    # Development
    "refactor": "improve code quality",
    "refactoring": "improving code quality",
    "technical debt": "deferred maintenance",
    "code review": "peer quality review",
    "codebase": "source code",
    "repository": "code storage",
    "repo": "code storage",
    "branch": "parallel work stream",
    "merge": "combine changes",
    "commit": "save changes",
    "push": "upload changes",
    "pull": "download changes",
    "PR": "change proposal",
    "MR": "change proposal",
    "debug": "find and fix problems",
    "debugging": "finding and fixing problems",
    "stack trace": "error details",
    "trace ID": "tracking number",
    "trace_id": "tracking number",
    "traceId": "tracking number",
    "log": "record, log entry",
    "logging": "recording events",
    # Incidents and quality
    "bug": "problem, defect",
    "issue": "problem, concern",
    "exception": "unexpected error",
    "error": "problem, failure",
    "failure": "problem, breakdown",
    "incidents": "service problems",
    "incident": "service problem",
    "P0": "critical incident",
    "P1": "high priority incident",
    "P2": "medium priority incident",
    "P3": "low priority incident",
    "unit test": "individual component test",
    "integration test": "system interaction test",
    "E2E test": "complete user journey test",
    "end-to-end": "complete system test",
    "regression": "backwards compatibility test",
    "TDD": "test-first development",
    "BDD": "behavior-driven development",
    "mock": "simulated component",
    "stub": "simulated component",
    "fixture": "test setup",
    # Cloud
    "cloud": "hosted infrastructure",
    "serverless": "managed computing",
    "FaaS": "managed computing",
    "IaaS": "infrastructure hosting",
    "PaaS": "platform hosting",
    "SaaS": "software service",
    "VPC": "private network",
    "subnet": "network segment",
    "firewall": "security barrier",
    "spot instance": "cost-efficient server",
    "on-demand": "standard server",
    "reserved instance": "pre-paid server",
    # Miscellaneous
    "SDK": "development toolkit",
    "CLI": "command-line tool",
    "GUI": "visual interface",
    "UX": "user experience",
    "UI": "user interface",
    "API key": "access key",
    "payload": "data package",
    "async": "background processing",
    "asynchronous": "background processing",
    "sync": "immediate processing",
    "synchronous": "immediate processing",
    "queue": "waiting line",
    "queueing": "waiting in line",
    "worker": "background processor",
    "thread": "processing task",
    "process": "running program",
    "goroutine": "concurrent task",
    "coroutine": "concurrent task",
    "deadlock": "processing block",
    "race condition": "timing problem",
    "memory leak": "gradual resource waste",
    "OOM": "memory exhaustion",
    "GC": "memory cleanup",
    "garbage collection": "automatic memory cleanup",
    "heap": "memory area",
    "stack": "memory structure",
    "serialization": "data conversion",
    "deserialization": "data recovery",
    "marshaling": "data conversion",
    "unmarshaling": "data recovery",
    "JSON": "data format",
    "XML": "data format",
    "YAML": "data format",
    "TOML": "data format",
    "protobuf": "data format",
    "avro": "data format",
    "parquet": "data format",
    "CSV": "spreadsheet format",
    "regex": "text pattern",
    "regular expression": "text pattern",
    "event-driven": "event-based",
    "event sourcing": "event recording",
    "CQRS": "separate read/write processing",
    "event bus": "message distribution system",
    "message queue": "message waiting line",
    "pub/sub": "publish-subscribe system",
    "stream": "continuous data flow",
    "batch": "grouped processing",
    "real-time": "instant",
    "near real-time": "almost instant",
    "eventual consistency": "delayed synchronization",
    "strong consistency": "immediate synchronization",
    "CAP theorem": "distributed system trade-off",
    "ACID": "data reliability guarantee",
    "BASE": "flexible data model",
    "idempotent": "safe to repeat",
    "idempotency": "safety when repeated",
    "idempotency key": "repetition prevention",
}

ZH_TECH_JARGON = {
    "API": "系統整合、資料連接、資料服務",
    "endpoint": "連接點、服務網址",
    "後端": "資料處理系統",
    "前端": "使用者介面",
    "伺服器": "處理系統、基礎設施",
    "部署": "上線、發布、交付",
    "回滾": "回復到前一版本",
    "發布": "上線、交付",
    "CI/CD": "自動化交付流程",
    "pipeline": "自動化流程",
    "容器": "隔離式應用程式封裝",
    "叢集": "基礎設施群組",
    "節點": "處理資源",
    "Kubernetes": "基礎設施管理平台",
    "K8s": "基礎設施管理平台",
    "Docker": "應用程式封裝工具",
    "資料庫": "資料儲存系統",
    "查詢": "資料查詢、資料請求",
    "索引": "搜尋最佳化",
    "schema": "資料結構",
    "migration": "資料結構更新",
    "快取": "暫存資料",
    "佇列": "等待處理的工作清單",
    "延遲": "回應時間",
    "吞吐量": "處理能力",
    "流量": "使用量、請求量",
    "限流": "使用量限制",
    "錯誤率": "失敗率、問題比例",
    "中斷": "服務中斷",
    "當機": "服務無法正常運作",
    "技術債": "延後維護",
    "重構": "改善系統結構、改善程式品質",
    "程式碼審查": "同儕品質檢查",
    "PR": "變更提案",
    "debug": "找出並修正問題",
    "bug": "問題、缺陷",
    "例外": "非預期錯誤",
    "漏洞": "資安弱點",
    "弱點": "風險點、資安弱點",
    "CVE": "資安公告編號",
    "修補": "修正、資安修補",
    "加密": "資料保護",
    "驗證": "使用者驗證",
    "授權": "存取權限",
    "token": "存取憑證",
    "JWT": "安全憑證",
    "OAuth": "安全登入機制",
    "測試覆蓋率": "測試完整度",
    "單元測試": "元件層級測試",
    "整合測試": "系統互動測試",
    "端到端測試": "完整使用流程測試",
    "回歸測試": "確認既有功能仍正常",
}


AUDIENCE_ALLOWLIST = {
    "executive": {"AI", "app", "cloud", "security", "software", "system", "data"},
    "vp": {"AI", "app", "cloud", "security", "software", "system", "data", "SLA"},
    "pm": {"AI", "API", "app", "cloud", "database", "server", "SLA", "UX", "UI"},
    "client": {"AI", "app", "security", "software", "system", "data"},
    "legal": {"CVE", "SLA", "security", "encryption", "authentication", "authorization"},
    "media": {"AI", "app", "security", "software", "system", "data"},
}


def _term_pattern(term: str) -> re.Pattern[str]:
    return re.compile(r"(?<![A-Za-z0-9_])" + re.escape(term) + r"(?![A-Za-z0-9_])", re.IGNORECASE)


def _contains_cjk(term: str) -> bool:
    return any("\u4e00" <= char <= "\u9fff" for char in term)


def _find_matches(term: str, text: str) -> list[re.Match[str]]:
    if _contains_cjk(term):
        return list(re.finditer(re.escape(term), text, re.IGNORECASE))
    return list(_term_pattern(term).finditer(text))


def check_jargon(text: str, audience: str = "pm", allow_terms: Iterable[str] = ()) -> dict:
    allow = {term.lower() for term in AUDIENCE_ALLOWLIST.get(audience, set())}
    allow.update(term.lower() for term in allow_terms)

    found = []
    combined_jargon = {**TECH_JARGON, **ZH_TECH_JARGON}
    for term, suggestion in sorted(combined_jargon.items(), key=lambda item: -len(item[0])):
        if term.lower() in allow:
            continue
        matches = _find_matches(term, text)
        if not matches:
            continue
        count = len(matches)
        found.append(
            {
                "term": term,
                "suggestion": suggestion,
                "count": count,
                "severity": "high" if count > 2 else "medium" if count > 1 else "low",
            }
        )

    total_words = len(re.findall(r"\b[\w'-]+\b", text))
    jargon_words = sum(item["count"] for item in found)
    jargon_score = (jargon_words / total_words * 100) if total_words else 0.0

    return {
        "audience": audience,
        "text_length": len(text),
        "word_count": total_words,
        "jargon_found": len(found),
        "jargon_score": jargon_score,
        "jargon_items": found,
        "recommendation": get_recommendation(jargon_score),
    }


def get_recommendation(score: float) -> str:
    if score > 20:
        return "HIGH JARGON - Rewrite significantly. Target: <15%."
    if score > 10:
        return "MODERATE JARGON - Replace highlighted terms. Target: <10%."
    if score > 5:
        return "LOW JARGON - Minor cleanup recommended."
    return "CLEAN - Text is business-friendly."


def format_report(result: dict) -> str:
    lines = [
        "=" * 60,
        "JARGON CHECK REPORT",
        "=" * 60,
        f"Audience: {result['audience']}",
        f"Words: {result['word_count']}",
        f"Jargon terms found: {result['jargon_found']}",
        f"Jargon score: {result['jargon_score']:.1f}%",
        f"Recommendation: {result['recommendation']}",
        "",
    ]

    if not result["jargon_items"]:
        lines.append("No technical jargon detected.")
        lines.append("=" * 60)
        return "\n".join(lines)

    lines.append("FOUND JARGON:")
    lines.append("-" * 60)
    for severity in ("high", "medium", "low"):
        items = [item for item in result["jargon_items"] if item["severity"] == severity]
        if not items:
            continue
        lines.append(f"\n{severity.upper()} ({len(items)} terms):")
        for item in items:
            lines.append(f"  - {item['term']} ({item['count']}x): {item['suggestion']}")

    lines.extend(["", "SUGGESTED REPLACEMENTS:", "-" * 60])
    for item in result["jargon_items"][:12]:
        first_suggestion = item["suggestion"].split(",")[0].strip()
        lines.append(f"  - Replace '{item['term']}' with '{first_suggestion}' where appropriate.")
    lines.append("=" * 60)
    return "\n".join(lines)


def read_text(args: argparse.Namespace) -> str:
    if args.input:
        return args.input
    if args.file:
        return Path(args.file).read_text(encoding="utf-8")
    if args.stdin:
        return sys.stdin.read()
    return ""


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check text for technical jargon that non-technical audiences may not understand."
    )
    parser.add_argument("--input", "-i", help="Text to check")
    parser.add_argument("--file", "-f", help="UTF-8 text file to check")
    parser.add_argument("--stdin", "-s", action="store_true", help="Read text from stdin")
    parser.add_argument("--audience", "-a", default="pm", choices=sorted(AUDIENCE_ALLOWLIST))
    parser.add_argument("--allow-term", action="append", default=[], help="Term to ignore. Repeat as needed.")
    parser.add_argument("--threshold", "-t", type=float, default=10.0, help="Jargon score threshold")
    parser.add_argument("--strict", action="store_true", help="Fail if any jargon is found")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    text = read_text(args)
    if not text.strip():
        print("No text provided.", file=sys.stderr)
        return 2

    result = check_jargon(text, audience=args.audience, allow_terms=args.allow_term)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(format_report(result))

    if args.strict and result["jargon_found"] > 0:
        return 1
    if result["jargon_score"] > args.threshold:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
