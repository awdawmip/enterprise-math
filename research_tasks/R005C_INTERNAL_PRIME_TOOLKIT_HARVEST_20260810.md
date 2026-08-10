<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R005-INTERNAL-PRIME-TOOLKIT-HARVEST",
  "title": "R005-C Internal Prime Toolkit Harvest and Toolization",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Audit the prime-related mathematics already produced inside Enterprise Math, separate stable reusable methods from route-local research helpers, and turn the validated reusable subset into a compact exact Prime Toolkit without moving theorem ownership or inventing new mathematics merely to fill an API.",
  "next_action": "Build a provenance-aware inventory of project-native prime methods across P017/P018/P023/P025/R005 and current canonical/executable surfaces; classify each method by theorem status, input/output contract, exactness, ownership, and reuse value; then expose only stable reusable items through the smallest shared toolkit facade and regression suite, leaving WIP methods referenced rather than copied.",
  "dependencies": [
    {"target": "R005-A Enterprise Prime Algorithm Lab", "action": "INFORM", "satisfied": true},
    {"target": "R005-B Prime-Collapse Field Geometry", "action": "INFORM", "satisfied": true},
    {"target": "canonical P018/P023 power-free action basis", "action": "CONSUME", "satisfied": true},
    {"target": "canonical centered-prime-radius specialization", "action": "CONSUME", "satisfied": true},
    {"target": "noncanonical prime-related owner/bridge results", "action": "INFORM", "satisfied": false}
  ],
  "source_refs": [
    "research_tasks/R005C_INTERNAL_PRIME_TOOLKIT_HARVEST_20260810.md",
    "research_tasks/R005A_ENTERPRISE_PRIME_ALGORITHM_LAB_20260810.md",
    "research_tasks/R005B_PRIME_COLLAPSE_FIELD_GEOMETRY_20260810.md",
    "research_common_surface.json",
    "src/enterprise_math/legendre.py",
    "src/enterprise_math/factor_precision.py",
    "src/enterprise_math/p017_precision_horizon.py",
    "src/enterprise_math/prime_gap_slack.py",
    "src/enterprise_math/centered_prime_radius.py",
    "PR #333 P018/P023 primitive prime generator bridge",
    "PR #170 P017/P018 adaptive prime-support bridge",
    "PR #339 P025 centered-prime atom bridges"
  ],
  "evidence_status": "INTERNAL_METHOD_HARVEST_AND_TOOLIZATION",
  "last_progress_ref": "Driver decision to prioritize prime tooling",
  "last_progress_at": "2026-08-10T20:48:00+08:00",
  "hard_block": null,
  "tags": ["R005", "prime", "toolkit", "toolization", "inventory", "provenance", "factor-precision", "carry", "witness", "certificate"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED"
}
-->

# R005-C — 项目内素数方法收割与工具化

Status: `READY / P0 / HIGH / INTERNAL HARVEST / NOT CANONICAL`

## 0. 任务性质

这个任务不是再做一轮“素数研究”。

它的目标是解决当前已经暴露出来的工程性研究缺口：

> Enterprise Math 已经在不同研究路线中产生了不少与素数、因子、筛选、证明精度、prime gap、centered coordinates、quotient-word generator 等有关的方法，但它们仍散落在 P017/P018/P023/P025/R005 等不同 owner 中，很多只能被原研究者知道，不能被后续研究直接复用。

本任务负责把这些已有方法**发现出来、验证身份、整理接口、工具化**。

原则：

- 不重新证明已有 theorem，除非工具化暴露出 statement/API 与 theorem 不一致；
- 不把 WIP 冒充 canonical；
- 不为了“统一”而移动 theorem ownership；
- 不复制一份已有数学到 `prime_toolkit` 造成第二真相源；
- 工具层应尽量薄：adapter / registry / exact facade，而不是新理论仓库。

---

# 1. 第一阶段：项目内 Prime Method Inventory

至少审计以下家族，并继续追索所有直接相关的 current-main / validated WIP / Lean / executable 资产。

## 1.1 基础 oracle / enumeration

- `primes_up_to`
- `is_prime`
- squarefree divisor / Möbius helpers

这些可能只是 classical baseline。不要因为在仓库里就称为 Enterprise Math 新工具。

## 1.2 Square-basin / factor-precision

重点抽取：

- finite root-factor horizon；
- factor witness state；
- least witness compression；
- first-factor shells；
- survivor-prime horizon；
- factor-certificate persistence；
- square-basin terminal primality completeness。

这里要特别区分：

`CLASSICAL PRIME ALGORITHM`

与

`ENTERPRISE-MATH PROOF-PRECISION ORGANIZATION`。

## 1.3 Carry / Möbius / centered basin tools

审计：

- exact square interval hit count；
- Euclidean basin descent；
- square carry / centered square carry；
- Möbius prime-count identity；
- binary carry pairing；
- anchor primes / anchor transfer / centered survivor discrepancy。

目标不是把整个 `legendre.py` 暴露为公共 API，而是找出哪些函数实际上已经形成可复用算术 primitive。

## 1.4 Factor-proof slack / centered prime coordinates

审计：

- survivor-prime horizon `H(k)`；
- factor proof slack `sigma(k)=k-H(k)`；
- near-diagonal shell；
- fixed even-gap correspondence；
- centered prime radius；
- difference-of-squares localization。

把“有限坐标变换工具”与“外部 bounded-gap theorem”严格分开。

## 1.5 P018/P023 quotient-root / action-language tools

至少纳入：

- exact quotient-root denominator fiber；
- power-free one-step semantic action basis；
- primitive prime generator basis under composition；
- prime-horizon / word-length / `Omega` compiler filtration；
- storage-depth tradeoff。

如果某项仍是 WIP/PR-only，只做 provenance link 和 adapter proposal，不复制未晋升代码。

## 1.6 P025 / cross-route prime compilers

检查能否复用而不引入 abc-specific 语义：

- radical/support selectors；
- centered prime-square / prime-cube coordinates；
- squarefree/full-block token descent；
- prime-support / divisor-token compilers。

默认保守：应用专用工具不自动进入 shared Prime Toolkit。

---

# 2. 每个方法必须进入统一 Method Card

建立 machine-readable inventory。每个 method 至少记录：

```text
method_id
name
source_owner
source_ref / commit / PR
mathematical_status
prior_art_status
inputs
outputs
exactness
preconditions
failure_modes
time/space character
integer_only?
Lean_status
current_tests
reusable_for
not_safe_for
toolization_status
```

建议状态：

- `CANONICAL_TOOL_READY`
- `VALIDATED_WIP_ADAPTER_ONLY`
- `APPLICATION_LOCAL`
- `CLASSICAL_BASELINE`
- `DUPLICATE`
- `DEPRECATED_OR_SUPERSEDED`
- `NEEDS_AUDIT`

Inventory 是本任务最重要的产物之一。

---

# 3. Prime Toolkit 的设计原则

## 3.1 不做大一统对象

不要把所有东西封装成一个万能 `PrimeState`。

至少保留用途差异：

- enumeration；
- primality decision；
- factor witness；
- proof precision；
- interval/basin counting；
- future-action separation；
- certificate/witness geometry；
- centered/gap diagnostics。

## 3.2 Facade，不复制 theorem owner

如果稳定函数已经存在于 owner module：

Prime Toolkit 只允许：

- re-export；
- thin adapter；
- registry lookup；
- normalized result schema。

不要复制算法实现。

## 3.3 Exact integer first

共享工具默认要求：

- exact integer arithmetic；
- deterministic finite output；
- explicit preconditions；
- no floating theorem oracle。

## 3.4 Status must travel with tool

一个工具如果来自 WIP，不允许调用者误以为它 canonical。

工具注册信息必须暴露：

`CANONICAL_MAIN / LEAN_CHECKED_MAIN / PROVED_WIP / EXECUTABLE_CHECKED / CLASSICAL_BASELINE / CONJECTURAL`。

---

# 4. 工具化优先级

第一轮优先找出 5–12 个真正高复用 primitive，不追求数量。

优先级建议：

1. bounded exact primality/factor oracle baseline；
2. factor witness / least witness / proof horizon；
3. square-basin factor shell decomposition；
4. carry / Möbius exact interval count primitives；
5. centered prime radius/slack coordinate conversion；
6. quotient-root denominator fiber / action-basis query（若当前 canonical surface 可安全调用）；
7. reusable provenance/status registry。

如果最终只有 6 个真正值得公共化，就只做 6 个。

---

# 5. 文件纪律：防止“工具化 = 再造一堆 MD”

默认最多新增这些 durable artifacts：

1. 一个 machine-readable inventory（JSON）；
2. 一个最小 shared facade/registry Python module 或 package；
3. 一个 focused unittest 文件；
4. 一个 handoff/report（如果仓库规则要求）。

不要为每个 method 单独生成 Markdown。

已有 docs/source comment 足够表达的，不另造文档。

---

# 6. 验证要求

至少完成：

- inventory source refs 可解析；
- facade 结果与 owner implementation 一致；
- canonical/WIP status 不被抹平；
- exact integer regression；
- representative cross-method composition tests；
- no circular imports；
- no owner duplication。

如果一个方法在 toolization 后发现 theorem/API mismatch，立即标：

`TOOLIZATION_EXPOSED_SEMANTIC_BUG`

把最小失败点交回真正 owner，不在 R005-C 里偷偷修新数学。

---

# 7. 与 R005-A 的接口

R005-A 负责把外部成熟素数工具重新放进 Enterprise Math 语言中研究。

R005-C 负责告诉 R005-A：

> 我们现在已经有什么 primitive 可以用，哪些是真正 canonical，哪些只是 WIP，哪些缺口值得外部工具来补。

R005-A 返回的新方法不得自动进入 Prime Toolkit。

必须先经过：

`external reconstruction -> exact validation -> novelty/prior-art classification -> Driver review -> toolization candidate`

再由本任务或后续 toolkit maintenance 收录。

---

# 8. 第一轮最终交付

1. `Prime Method Inventory`；
2. project-native prime method taxonomy；
3. stable reusable method shortlist；
4. minimal Prime Toolkit facade/registry；
5. focused regression evidence；
6. duplicated/unsafe/WIP-only exclusion list；
7. top 3 missing prime-tool capabilities；
8. 给 R005-A 的内部 capability packet；
9. `proposal_candidates`（如工具化暴露出真正新研究问题，集中放一处，不另造 taskbook）。

## 最终问题

必须回答：

\[
\boxed{
\text{Enterprise Math 到今天究竟已经拥有了哪些真正可复用的素数工具，而不只是散落的研究代码？}
}
\]

并把答案变成下一位研究员可以直接调用的工具面。
