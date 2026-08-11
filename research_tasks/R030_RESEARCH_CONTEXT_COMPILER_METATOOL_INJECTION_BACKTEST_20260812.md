<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R030-RESEARCH-CONTEXT-COMPILER-METATOOL-INJECTION-BACKTEST",
  "title": "R030 Research Context Compiler: Reasoning-Tool Injection, Cold-Start Replay, and Context-Budget Backtest",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "RESEARCH_PRODUCTIVITY_INFRASTRUCTURE",
  "frontier": "Test whether Enterprise Math researchers can start materially closer to the current conceptual frontier by compiling a compact task-relative context pack that injects relevant reasoning operators, carrier/modal/evidence distinctions, negative boundaries, and source-grounded alerts instead of merely listing documents to read.",
  "next_action": "Build a deterministic and inspectable research-context compiler, define a typed context-pack schema and selection contract, replay recent tasks against post-hoc gold reasoning requirements, measure critical-tool recall versus context cost/noise, attack keyword-only and over-injection failure modes, and return whether reasoning-tool injection should become reusable research infrastructure.",
  "dependencies": [
    {
      "target": "current Enterprise Math taskbook/common-surface architecture",
      "action": "CONSUME_EXISTING_TASK_METADATA_DEPENDENCIES_SHARED_SURFACE_AND_SOURCE_REFS_WITHOUT_REPLACING_THEM",
      "satisfied": true
    },
    {
      "target": "R017-R028 accepted research history",
      "action": "USE_POST_HOC_ACCEPTED_REASONING_DISTINCTIONS_AS_BACKTEST_GOLD_LABELS",
      "satisfied": true
    },
    {
      "target": "R029 reasoning-tool contract task",
      "action": "MAINTAIN_SCHEMA_COMPATIBILITY_WITH_R029_WHILE_ALLOWING_PARALLEL_PROVISIONAL_SEED_TOOLS",
      "satisfied": true
    }
  ],
  "source_refs": [
    "research_taskbook_contract.json",
    "research_taskbook_policy.json",
    "docs/RESEARCH_TASKBOOK_AUTHORING_AND_REVIEW.md",
    "research_common_surface.json and docs/RESEARCH_COMMON_SURFACE.*",
    "R017/R020/R022/R023/R023I/R024/R025/R028 taskbooks and accepted returns",
    "R029 taskbook c59c2ad1e56fcae3bf858b874a5a636c242e62c5 as sibling schema target"
  ],
  "evidence_status": "CONTEXT_COMPILER_PRODUCTIVITY_BACKTEST_GATE",
  "last_progress_ref": "User identified that researchers repeatedly restart conceptual work despite shared theorem context; Driver separated reasoning-tool definition from a parallel compiler/backtest lane to test whether compact meta-tool injection actually raises the starting frontier",
  "last_progress_at": "2026-08-12T00:29:00+08:00",
  "hard_block": null,
  "tags": [
    "R030",
    "meta-research",
    "context-compiler",
    "reasoning-tools",
    "cold-start",
    "research-productivity",
    "task-relative-context",
    "backtest",
    "context-budget",
    "negative-boundaries"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R030",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:a03b06c1c6d29ca2776592fd12aa77406f45a21afb8fc1a8431b25cd41963c77",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R030 — Research Context Compiler: Reasoning-Tool Injection, Cold-Start Replay, and Context-Budget Backtest

Status: `READY / P0 / RESEARCH PRODUCTIVITY INFRASTRUCTURE / CONTEXT-COMPILER BACKTEST / NOT CANONICAL`

## 0. 母问题

当前研究员已经有：

- taskbook；
- source refs；
- common research surface；
- dependencies；
- prior return artifacts。

但这些主要回答“去哪里读”。它们没有自动回答：

> 对这个具体任务，哪些已经学到的 reasoning distinctions 必须在研究第一步就进入工作记忆？

因此出现一种重复成本：数学结果已存在，但 carrier split、modal split、composition boundary、evidence boundary、prior-art reduction 等推理动作仍被不同研究员重新发现。

本任务要实测：

> 一个可审计的 Research Context Compiler 能否根据 task contract 和当前知识面，选择少量真正相关的 reasoning tools 与 negative boundaries，生成 compact context pack，并显著减少“研究到一半才发现问题类型搞错”的 cold-start loss？

本任务不是要求自动替代研究员，也不是把所有历史文本塞进 prompt。

---

## 1. Context Pack 不等于 Taskbook

必须保持：

`TASKBOOK = task-specific problem contract`

`COMMON SURFACE = reusable accepted knowledge router`

`REASONING REGISTRY = reusable reasoning operators`

`CONTEXT PACK = task-relative compiled working context`

Context Pack 应是派生物，不应成为另一本手工维护的大 taskbook。

建议 schema：

```text
schema
compiler_version
task_id
task_signature
source_snapshot
registry_snapshot
selected_exact_tools
selected_diagnostic_tools
selection_reasons
carrier_alerts
modal_alerts
quantifier_alerts
evidence_alerts
negative_boundaries
prior_art_alerts
required_source_refs
known_non_implications
excluded_tools
context_budget
context_digest
```

---

## 2. Task Semantic Signature

编译器首先应从 taskbook + machine common surface 提取显式 signature，而不是直接做关键词拼接。

至少包括：

- object/state types；
- carrier types；
- deterministic / relational / stochastic / signed 等 semantics；
- current observable；
- future language / horizon；
- theorem target vs executable target vs empirical target；
- minimality scope；
- composition requirement；
- representation/resource comparison requirement；
- evidence target；
- known dependencies；
- explicit exclusions。

对无法确定的字段返回 `UNKNOWN`，不得猜成确定事实。

---

## 3. Provisional Seed Tool Set

R030 可与 R029 并行，因此先用以下**已由近期研究事实支持**的 provisional seed；R029 返回后再比较 schema/命名，不得假装 R030 seed 已是最终 registry。

至少：

1. `QUANTIFIER_SCOPE_CHECK`
2. `STATE_OBSERVATION_SPLIT`
3. `CARRIER_TYPE_SPLIT`
4. `STATIC_CORRECT_NOT_DYNAMIC_STATE`
5. `ONE_STEP_EXACT_NOT_COMPOSITION_SAFE`
6. `DECLARED_VS_REALIZED_FUTURE`
7. `FACTOR_THROUGH_COMPLETE_ENCODING`
8. `SUPPORT_COUNT_PROVENANCE_SPLIT`
9. `RESOURCE_EQUAL_SEMANTIC_FIBRE_CHECK`
10. `MIDDLE_INCIDENCE_CORRELATION_CHECK`
11. `ROOT_COVERAGE_EVIDENCE_CHECK`
12. `PRIOR_ART_REDUCTION`
13. `COUNTEREXAMPLE_MINIMIZATION`
14. `REGIME_EXHAUSTION`
15. `CAUSAL_PREDICTIVE_RETROSPECTIVE_SPLIT`

每个 provisional tool 必须带 source evidence 与 trust class。

---

## 4. Two-Channel Selection

必须把工具选择分成两路：

### EXACT / REQUIRED channel

来自明确的：

- task semantic signature；
- carrier declaration；
- dependency；
- theorem family；
- accepted negative boundary；
- explicit task constraint。

例如要求 composition-safe Boolean support 时，应确定性选择 `ONE_STEP_EXACT_NOT_COMPOSITION_SAFE` 与 matching carrier alert。

### DIAGNOSTIC / SUGGESTED channel

来自：

- textual signals；
- analogical similarity；
- research-neighborhood heuristics；
- prior historical patterns。

该 channel 只能提示检查，不能把 tool conclusion 注入为事实。

这一区分本身是强制输出字段。

---

## 5. Context Budget Problem

更多上下文不一定更好。必须将 context selection 写成资源问题。

对每个 candidate tool 记录：

- estimated context bytes/tokens；
- critical coverage；
- redundancy overlap；
- expected false-positive cost；
- trust class；
- source count。

研究至少三种策略：

1. `ALL_MATCHES`
2. `TOP_K`
3. `MINIMUM_CRITICAL_COVER` 或近似的 weighted distinction-cover selection

不得把一个大型 universal checklist 当默认最优。

---

## 6. Historical Gold Backtest

建立 post-hoc gold matrix：

`R030_HISTORICAL_CONTEXT_GOLD.json`

至少回放下列任务。

### R017

Gold distinctions 至少包括：

- deferred selector carrier ≠ universal future-complete carrier；
- representation size 与 future sufficiency 分离。

### R020

Gold：

- static exact statistic ≠ dynamically reusable state；
- Boolean support / N-count / provenance 分离；
- one-step exact ≠ composition-safe。

### R022

Gold：

- branch selector ≠ full state；
- certificate validity ≠ heuristic search quality；
- future-language-relative precision；
- metadata/storage must be charged。

### R023

Gold：

- Boolean/result-support carrier scope；
- suffix-safe recoalescence relative to remaining future；
- current coarse equality insufficient。

### R023I / proof-coverage incident

Gold：

- successful build claim must cover the actual new module；
- source provenance ≠ compiler coverage evidence。

### R024

Gold：

- compare resources only for equal semantic contract；
- cache/hazard metadata is charged information；
- exact fallback boundary。

### R025

Gold：

- exhaustive regime classification；
- aligned islands invalidate naive `r>=2^p -> binary`；
- zero root-index invalidates blanket doubling；
- finite data does not itself prove universal law。

### R028

Gold：

- declared-language credit ≠ realized-suffix hindsight credit；
- causal ≠ predictive ≠ retrospective relevance。

---

## 7. Backtest Metrics

至少报告：

### Critical Tool Recall

`selected_gold_tools / total_gold_tools`

### Critical Tool Precision

`selected_gold_tools / selected_tools`

### Context Cost

- bytes；
- approximate tokens；
- number of source refs；
- number of tools。

### Cold-Start Recovery Gain

定义一个可审计 proxy：

- gold distinction 若原 taskbook/common surface 启动上下文已显式包含，baseline credit = 1；
- 若只在后续研究中出现，baseline credit = 0；
- compiler 在启动包中正确注入则 recovered = 1。

汇总 `RECOVERED_LATE_DISTINCTIONS`。

不要声称这个 proxy 等于真实人类研究时间。

### Noise / Overload

记录 injected but irrelevant tools，并测试是否会引导错误路线。

---

## 8. Adversarial Trigger Tests

必须攻击简单关键词方案。

至少构造：

- 不出现 “future” 一词但实际有 horizon/future-language 语义的任务；
- 出现 “support” 但不是 Boolean support carrier 的任务；
- 出现 “minimal” 但只要求 declared search class minimality；
- 出现 “proof” 但目标只是 executable validation；
- 出现 “causal” 但实际只要求 predictive relation；
- 出现 “same” 但实际可能是 observational equivalence 而非 identity。

编译器应优先依赖 semantic signature；关键词只能辅助。

---

## 9. Mutation Suite

建立 mutation cases，至少包括：

1. 删除 carrier declaration；
2. 将 Boolean support 换成 N-count 但保持相似文字；
3. 将 one-step 改为 arbitrary finite words；
4. 将 declared future 改为 realized trace；
5. 将 bounded minimality 改成 global minimality；
6. 删除 actual module coverage information但保留“build passed”字样；
7. 将 equal semantic contract resource comparison改成不同 carrier；
8. 加入一个非常相关但证据等级不足的 interpretive lens。

要求 compiler 选择集或 warning 明显变化。

---

## 10. Philosophy Injection Boundary

Context Pack 可注入 philosophy tool，但必须标记 trust class。

例如：

- ontology/type distinction 可作为 mandatory diagnostic；
- modal warning 可作为 mandatory diagnostic；
- causal interpretation可能只是 interpretive/adversarial；
- explanation style 不得变成 theorem assumption。

必须有 UI/textual formatting 使研究员一眼区分：

`FACT / FORMAL TOOL / EXACT DIAGNOSTIC / HEURISTIC ALERT / INTERPRETIVE LENS`。

---

## 11. Source-Grounded Injection

每条 injected tool/alert 必须携带：

- source refs；
- scope；
- evidence grade；
- why selected；
- what not to infer。

禁止无来源的“最新理念”在编译过程中逐渐演化成项目事实。

---

## 12. Context Freshness

Context pack 必须可检测过期：

至少 digest：

- taskbook content；
- reasoning registry；
- relevant common surface；
- selected source refs 的 pinned identities。

任何输入变化都必须改变 `context_digest`。

研究是否需要全局知识面变化就使全部 context pack 失效，还是只对 relevant dependency closure 失效。优先选择局部失效模型，避免无关 main movement 造成无意义重编译。

---

## 13. Prototype

优先建立：

- `tools/research_context.py`
- `research_context_contract.json`
- `research_reasoning_tools_seed.json`
- `tests/test_research_context.py`
- `experiments/r030_context_backtest.py`

建议接口：

```text
compile <taskbook>
inspect <context-pack>
audit <context-pack>
backtest <task-set>
```

实际命名可调整，但必须保持 deterministic / inspectable output。

---

## 14. Compact Human Pack

机器 JSON 之外，生成紧凑 human-readable pack，优先结构：

```text
TASK SEMANTIC SIGNATURE
CRITICAL REASONING TOOLS
KNOWN NON-IMPLICATIONS
CARRIER / MODAL / QUANTIFIER ALERTS
EVIDENCE BOUNDARY
NEGATIVE BOUNDARIES
PRIOR-ART ALERTS
SOURCE POINTERS
WHAT WAS INTENTIONALLY OMITTED
```

目标是让研究员立即站到正确 problem space，而不是再给一堵文档墙。

---

## 15. R029 Compatibility Test

若 R029 在本任务期间已有返回：

- 映射 provisional seed tool IDs 到 R029 registry；
- 记录 semantic equivalents / renamed / killed / narrowed；
- 用 R029 trust class 重新跑历史 backtest；
- 不得为了维持 R030 指标而保留 R029 已杀掉的工具。

若 R029 尚未返回，R030 仍可完成 provisional compiler/backtest；最终明确标为 `SEED_REGISTRY`，不能宣称 registry finalized。

---

## 16. Kill Targets

必须优先攻击：

1. `MORE_CONTEXT_ALWAYS_IMPROVES_RESEARCH`
2. `ALL_RELEVANT_TOOLS_SHOULD_ALWAYS_BE_INJECTED`
3. `KEYWORD_SELECTION_IS_ENOUGH`
4. `ONE_STATIC_CONTEXT_PACK_CAN_SERVE_ALL_HORIZONS`
5. `INTERPRETIVE_PHILOSOPHY_CAN_BE_INJECTED_AS_FACT`
6. `COMMON_SURFACE_AND_CONTEXT_PACK_ARE_DUPLICATES`
7. `CONTEXT_PACK_SHOULD_BE_HAND_MAINTAINED`
8. `GLOBAL_REPOSITORY_MOVEMENT_MUST_INVALIDATE_EVERY_CONTEXT`
9. `A_HIGH_RECALL_PACK_IS_GOOD_EVEN_IF_NOISY`
10. `A_COMPILER_CAN_INFER_UNDECLARED_CARRIER_SEMANTICS_WITHOUT_UNCERTAINTY`

---

## 17. Required Deliverables

至少：

1. `docs/R030_RESEARCH_CONTEXT_COMPILER_REPORT.md`
2. compiler prototype；
3. machine-readable contract；
4. provisional seed registry；
5. historical gold matrix；
6. replay/backtest result JSON；
7. context-budget Pareto report；
8. mutation suite；
9. sample compiled packs for at least R020, R023, R025, R028；
10. integration recommendation：`ADOPT / ADOPT_NARROW / RESEARCH_ONLY / KILL`。

---

## 18. Integration Recommendation Must Answer

最终必须明确回答：

1. context compiler 是否真的找回了历史上“后来才发现”的关键 distinction？
2. 哪些 tool 是 high-value injection，哪些会制造噪声？
3. 最好的 context budget 大约在哪里？
4. exact-required 与 diagnostic-suggested 两路是否必要？
5. context freshness 应依赖哪些 digest？
6. reasoning registry 与 common surface 如何分层？
7. 是否应把 compiled context 作为未来 researcher startup 的正式 companion artifact？
8. 是否应该建立 `META_TOOL_DELTA` 回流闭环？

---

## 19. Success / Kill Returns

优先：

`RESEARCH_CONTEXT_COMPILER_USEFUL / CRITICAL_REASONING_RECALL_HIGH / CONTEXT_BUDGET_PARETO_FROZEN / COLD_START_REDISCOVERY_REDUCED / META_TOOL_INJECTION_CANDIDATE / NOT_CANONICAL`

若只能窄用：

`CONTEXT_COMPILER_NARROWLY_USEFUL / EXACT_TOOL_CHANNEL_POSITIVE / HEURISTIC_PHILOSOPHY_INJECTION_NOISY / NOT_CANONICAL`

若失败：

`CONTEXT_COMPILER_OVERLOADS_RESEARCH / STATIC_COMMON_SURFACE_DOMINATES / META_TOOL_INJECTION_KILLED / NOT_CANONICAL`

负结果完全允许。
