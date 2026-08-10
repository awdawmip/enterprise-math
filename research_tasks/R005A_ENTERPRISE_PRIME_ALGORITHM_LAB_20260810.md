<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R005-PRIME-ALGORITHM-LAB",
  "title": "R005-A Enterprise Prime Algorithm Lab",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Translate classical prime enumeration, primality testing, probable-prime filtering, and certification into Enterprise Math observation/quotient/support/witness language and determine whether a reusable Prime Toolkit yields new minimal states, repair theorems, witnesses, certificates, or algorithms.",
  "next_action": "Audit existing prime helpers; then build exact baseline translations for trial division, sieve families, probable-prime tests, and one certificate family. Prioritize pseudoprime-as-fiber and bounded minimal witness-basis theorems before proposing a shared API.",
  "dependencies": [],
  "source_refs": [
    "research_tasks/R005A_ENTERPRISE_PRIME_ALGORITHM_LAB_20260810.md",
    "src/enterprise_math/legendre.py",
    "src/enterprise_math/centered_prime_radius.py",
    "src/enterprise_math/prime_gap_slack.py"
  ],
  "evidence_status": "CANDIDATE_RESEARCH_HANDOFF",
  "last_progress_ref": "research scout taskbook",
  "last_progress_at": "2026-08-10T11:14:00+08:00",
  "hard_block": null,
  "tags": ["R005", "prime", "algorithm", "primality", "sieve", "witness", "certificate"],
  "claim_lease_minutes": 1440
}
-->

# R005-A — 进取数论素数算法实验室

Status: `CANDIDATE RESEARCH HANDOFF / NOT CANONICAL`

## 目标

建立 Enterprise Math 的共享素数工具候选层，但不要把经典算法换名后冒充新数论。核心问题是：经典素数生成、筛选、素性判定、伪素数过滤和素性证书被重写成有限状态、观察、商、future-safe refinement、support/witness 语言后，是否会产生新的最小充分状态、最小修复、witness basis、证书结构或算法。

## 起点

先审计仓库现有素数资产：`legendre.py`、`centered_prime_radius.py`、`prime_gap_slack.py`、P018/P023 power-free action basis，以及相关 tests/Lean。区分一般工具与 P017/P018 application-local helper，不要为了统一破坏 theorem ownership。

## 必须区分

1. prime enumeration / sieve；
2. primality decision；
3. probable-prime filtering；
4. primality certification。

四类不能混成“生成素数”。

## 经典压力测试族

至少覆盖：trial division/root horizon、Eratosthenes、wheel/residue sieve、segmented sieve、Atkin、Fermat/Euler probable-prime language、Miller–Rabin、Lucas/recurrence、AKS，以及至少一种 multiplicative certificate 与一种 richer relation certificate（如 Pratt/APR/ECPP 路线）。

每个算法必须有 exact reference、correctness oracle、bounded exhaustive cross-check，并说明 Enterprise Math 转译到底产生了什么新结构；如果只是 translation，明确标记 `TRANSLATION_ONLY`。

## 第一母问题：pseudoprime = observation fiber

在有限域 `X_N={2,...,N}` 上，把 test language `W` 编译为 signature `Sigma_W(n)`。若 prime `p` 与 composite `c` 有同一 signature，则当前 quotient 对 primality 不安全。研究：

- 最粗 primality-safe quotient；
- 添加哪个 witness/base 后形成最小修复；
- bounded domain 的最小 witness basis；
- 不同算法语言的 partition-refinement order；
- incomparable languages。

## 第二母问题：sieve = support elimination?

把 divisibility/residue 看成有限 relation/support，研究筛法逐层删除、wheel quotient、segment local state、以及哪些粗摘要对后续筛选 composition-safe。

## 第三母问题：certificate = witness geometry?

把 prime certificate 建模成有限 witness graph/DAG，研究最短证书路径、深度、分支、有效证书 multiplicity、minimal support、certificate collapse equivalence 和 refinement/projection。

## 硬成果判据

至少命中一项才算产生 Enterprise Math 结果：新 exact equivalence、新 minimal sufficient state、更粗但安全的 quotient、新 witness/base minimality theorem、新 counterexample boundary、跨算法母结构、可复用 exact oracle/tool、可重复算法改进、或新的证书表示。

## 第一阶段交付

- 经典算法 taxonomy；
- exact baseline implementations；
- 统一 observation/witness model；
- prime-language partition explorer；
- 至少一个非平凡 theorem；
- 至少一个 counterexample/negative boundary；
- pseudoprime-as-fiber 精确结果；
- bounded minimal witness/base experiment；
- prior-art map；
- 推荐的最小 Prime Toolkit API；
- Relay/Foundation Feedback 候选。

## 最终判定

必须回答：进取数论对经典素数算法究竟只是提供了一套统一记号，还是确实发现了能产生新定理、新压缩、新 witness 结构或新算法的 Prime Toolkit？
