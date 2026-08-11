<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R029-RESEARCH-REASONING-KERNEL-LOGIC-PHILOSOPHY-TOOLS",
  "title": "R029 Research Reasoning Kernel: Logic and Philosophy as Typed Research Tools",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "META_RESEARCH_INFRASTRUCTURE",
  "frontier": "Treat logic, modality, ontology, epistemology, causality distinctions, reduction, adversarial counterexample generation, and proof-evidence discipline as typed reusable research tools rather than background prose; mine the strongest recurring reasoning moves from recent Enterprise Math work, define a trusted/heuristic tool taxonomy, and determine which operators genuinely reduce repeated conceptual rediscovery across research lanes.",
  "next_action": "Mine R015-R028 for repeated reasoning operators and failure modes, define a machine-readable reasoning-tool contract, build a seed registry plus executable validators where appropriate, root each operator in prior logic/philosophy/mathematics, adversarially test composition and misuse, and return the minimal reusable Research Reasoning Kernel suitable for context compilation.",
  "dependencies": [
    {
      "target": "R015-R028 recent Enterprise Math research corpus",
      "action": "MINE_REPEATED_REASONING_OPERATORS_FAILURES_AND_NEGATIVE_BOUNDARIES",
      "satisfied": true
    },
    {
      "target": "R023/R023I canonical BRC Boolean-support semantic core",
      "action": "USE_AS_ONE_GROUND_TRUTH_EXAMPLE_OF_TYPED_MODAL_AND_CARRIER_REASONING",
      "satisfied": true
    },
    {
      "target": "R020/R022 future-language and dynamic-completeness results",
      "action": "USE_AS_GROUND_TRUTH_FOR_STATIC_DYNAMIC_CARRIER_AND_FUTURE_MODALITY_TOOLS",
      "satisfied": true
    },
    {
      "target": "current taskbook authoring contract",
      "action": "PRESERVE_TASK_SPECIFIC_CONTRACT_LAYER_AND_PROPOSE_META_TOOL_CONTEXT_AS_SEPARATE_REUSABLE_LAYER",
      "satisfied": true
    }
  ],
  "source_refs": [
    "R015/R016 support-branch semantics and carrier discipline",
    "R017/R018/R019 carrier-completeness and precision-object distinctions",
    "R020 dynamic-completeness reaudit",
    "R021/R022 BRC tool calculus, precision debt, distinction cover and certificate discipline",
    "canonical R023/R023I Boolean/result-support semantic core",
    "R024 representation/runtime Pareto methodology",
    "R025 regime classification and hypothesis-kill atlas",
    "R028 retrospective distinction-credit foundation probe",
    "docs/RESEARCH_COMMON_SURFACE.* and research_common_surface.json"
  ],
  "evidence_status": "REASONING_TOOL_CALCULUS_DISCOVERY_GATE",
  "last_progress_ref": "User observed that researchers repeatedly appear to restart from halfway because mathematical results are shared but the reasoning operators that produced them are not; Driver identified missing logic/philosophy tooling and context compilation as a probable research-productivity bottleneck",
  "last_progress_at": "2026-08-12T00:29:00+08:00",
  "hard_block": null,
  "tags": [
    "R029",
    "meta-research",
    "reasoning-kernel",
    "logic",
    "philosophy",
    "modal-logic",
    "ontology",
    "epistemology",
    "causality",
    "type-discipline",
    "counterexample",
    "research-tools",
    "context"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R029",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:a03b06c1c6d29ca2776592fd12aa77406f45a21afb8fc1a8431b25cd41963c77",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R029 — Research Reasoning Kernel: Logic and Philosophy as Typed Research Tools

Status: `READY / P0 / META-RESEARCH INFRASTRUCTURE / TOOL-CALCULUS DISCOVERY / NOT CANONICAL`

## 0. 母问题

近期 Enterprise Math 的多个关键推进并不是来自更大的计算，而是来自“把问题重新分对类型”：

- static statistic 与 dynamically reusable state 分离；
- state / observation / carrier / representation / resource 分离；
- one-step exact 与 composition-safe 分离；
- Boolean support / path count / witness provenance 分离；
- declared future 与 realized future 分离；
- existence / necessity / sufficiency / minimality 的量词边界分离；
- research evidence 与 compiler/root coverage 的证据边界分离；
- prior-art reduction 与 project-specific residue 分离。

这些推理动作现在主要散落在各研究报告中。后来的研究员可以读取结论，却往往仍需重新发现产生结论的逻辑区分，形成明显的 conceptual restart cost。

本任务要研究：

> 能否把逻辑与哲学中的可复用推理动作，像 Python/Lean/certificate 一样定义成有输入、有输出、有适用前提、有保真性、有失效模式、可组合或明确不可组合的正式研究工具？

本任务不以“整理哲学概念”为目标，也不以“给研究员更多提示词”为成功。成功标准是得到一个**可调用、可审计、可反例攻击、可被 context compiler 选择的 reasoning-tool calculus**。

---

## 1. Tool 的工作定义

候选统一定义：

> Research Tool = 一个可重复调用的 research-state transformation，具有显式输入类型、输出类型、前提、保留性质、非保留性质、失败/反例边界和证据等级。

必须检验这个定义是否足够覆盖：

- executable tool；
- theorem/proof-preserving rewrite；
- logical diagnostic；
- modal distinction；
- ontology/type checker；
- epistemic evidence checker；
- counterexample generator；
- prior-art reduction；
- interpretive/philosophical lens。

不得因为一个概念“有启发性”就自动把它登记为 trusted tool。

---

## 2. Reasoning Tool Contract

优先设计机器可读 schema，建议 artifact：

`reasoning_tools.json`

每个 Tool 至少包含：

```text
id
name
layer
status
input_types
output_types
preconditions
transformation_or_question
preserves
may_destroy_or_not_preserve
trigger_signals
required_evidence
kill_tests
known_counterexamples
prior_art_root
project_specific_residue
composition_notes
executable_oracle
lean_declaration
source_refs
examples
anti_examples
```

必须区分至少四种 trust class：

1. `PROOF_PRESERVING`
2. `EXACT_SEMANTIC_TRANSFORMATION`
3. `ADVERSARIAL_DIAGNOSTIC`
4. `INTERPRETIVE_LENS`

研究员和 context compiler 不得把 3/4 类工具的输出当成 theorem evidence。

---

## 3. 必须挖掘的逻辑工具家族

### 3.1 Quantifier / implication tools

至少审计并尝试注册：

- `QUANTIFIER_SCOPE_CHECK`
- `EXISTS_FORALL_SEPARATION`
- `NECESSARY_SUFFICIENT_SPLIT`
- `CONVERSE_CHECK`
- `CONTRAPOSITIVE_CHECK`
- `BOUNDED_TO_GLOBAL_CHECK`
- `LOCAL_TO_GLOBAL_CHECK`
- `ONE_STEP_TO_ALL_HORIZONS_CHECK`
- `MINIMAL_IN_DECLARED_CLASS_VS_GLOBAL_MINIMAL`

必须给出 Enterprise Math 历史上的正例/反例来源。

### 3.2 Type / ontology tools

至少：

- `STATE_OBSERVATION_SPLIT`
- `STATE_CARRIER_REPRESENTATION_RESOURCE_SPLIT`
- `QUOTIENT_LABEL_VS_FULL_FIBRE_SPLIT`
- `BOOLEAN_COUNT_PROVENANCE_CARRIER_SPLIT`
- `SEMANTICS_VS_RUNTIME_REPRESENTATION`
- `METADATA_IS_INFORMATION_CHECK`
- `OBJECT_IDENTITY_VS_OBSERVATIONAL_EQUIVALENCE`

目标是让 category error 在研究开始阶段就显式暴露。

### 3.3 Modal tools

至少：

- `DECLARED_VS_REALIZED_FUTURE`
- `POSSIBLE_ACTUAL_NECESSARY_SPLIT`
- `CURRENT_VS_FUTURE_SAFE_EQUALITY`
- `FUTURE_LANGUAGE_EXTENSION_REFINEMENT`
- `HORIZON_RELATIVITY_CHECK`
- `HINDSIGHT_IRRELEVANCE_NOT_EX_ANTE_DISPENSABILITY`

R028 是重要压力测试，但 R029 不得预设 R028 的候选 scalar credit 结构成立。

### 3.4 Dynamic/composition tools

至少：

- `STATIC_CORRECT_NOT_DYNAMIC_STATE`
- `ONE_STEP_EXACT_NOT_COMPOSITION_SAFE`
- `MIDDLE_INCIDENCE_CORRELATION_CHECK`
- `GENERATORWISE_CLOSURE_CHECK`
- `FACTOR_THROUGH_COMPLETE_ENCODING`
- `NO_RESURRECTION_CHECK`
- `RECOALESCENCE_SUFFIX_SAFETY_CHECK`

### 3.5 Epistemic / evidence tools

至少：

- `CLAIM_EVIDENCE_GRADE_CHECK`
- `EXECUTABLE_EVIDENCE_NOT_PROOF`
- `ROOT_COVERAGE_EVIDENCE_CHECK`
- `BOUNDARY_OF_VALIDATION_CHECK`
- `NEGATIVE_RESULT_AS_RESOURCE`
- `SOURCE_PROVENANCE_VS_SEMANTIC_AUTHORITY`

必须使用 R023/R023I 的历史 validation-coverage bug 作为强制 fixture：成功的 root command 若未覆盖新模块，不能给新模块 credit。

### 3.6 Causal / attribution tools

至少：

- `CAUSAL_PREDICTIVE_RETROSPECTIVE_RELEVANCE_SPLIT`
- `COUNTERFACTUAL_DEPENDENCE_CHECK`
- `REALIZED_PATH_VS_DECLARED_LANGUAGE_CREDIT`
- `CORRELATION_NOT_CAUSATION_CHECK`

不得把 causal contribution、predictive sufficiency、retrospective distinction relevance 混为一类。

### 3.7 Reduction / novelty tools

至少：

- `PRIOR_ART_REDUCTION`
- `RENAME_NOT_NOVELTY_CHECK`
- `PROJECT_SPECIFIC_RESIDUE_EXTRACTION`
- `GENERIC_THEOREM_VS_SPECIALIZATION`
- `EQUIVALENCE_TO_KNOWN_ALGORITHM_CHECK`

R022 的 MITM negative、R024/R026 的 known-method rooting 都可作为 fixture。

### 3.8 Research-neighborhood generators

至少研究：

- `DUALITY_SEARCH`
- `COUNTEREXAMPLE_MINIMIZATION`
- `REGIME_EXHAUSTION`
- `ASSUMPTION_WEAKENING`
- `EXTREMAL_CASE_SEARCH`
- `COMPOSITION_CLOSURE_SEARCH`
- `QUOTIENT_STABILITY_SEARCH`
- `REFINEMENT_STABILITY_SEARCH`
- `CARRIER_CHANGE_SEARCH`

它们更可能属于 adversarial diagnostic / research generator，而不是 proof-preserving tool。

---

## 4. Philosophy Tooling 的严格边界

本任务必须证明“哲学工具化”不是把哲学词汇贴在数学上。

优先把以下哲学问题转成 typed check：

### Ontology

- 当前对象是 actual state、possible state、observation、representation、equivalence class、resource 还是 epistemic claim？
- 一个新对象真是新 primitive，还是已有 product/quotient/Set/function 的重新命名？

### Modality

- 命题针对 actual、possible、declared future、realized future、all futures 还是 one horizon？
- 从 hindsight 到 ex-ante 的推理是否改变了模态量词？

### Epistemology

- 当前结论是 proved、Lean-covered、executable checked、bounded exhaustive、heuristic、inferred、conjectural 还是 prior-art rooted？
- 证据到底覆盖了 claim 的哪一层？

### Identity

- 两个状态是 literal equal、same quotient label、same current observable、same future signature，还是仅当前任务无法区分？

### Causality / explanation

- “有用”指 causally necessary、predictively sufficient、counterfactually relevant、retrospectively correlated，还是 resource-saving？

每个 philosophy tool 都必须有 anti-example，说明不做这个 distinction 会导致什么具体错误。

---

## 5. Historical Mining

必须至少回放 R015–R028，并建立：

`R029_REASONING_OPERATOR_LINEAGE_MATRIX.md`

每个历史关键节点记录：

- 当时的母问题；
- 最终突破依赖的 reasoning distinction；
- 该 distinction 在任务启动时是否已经显式可用；
- 如果没有，研究员在哪个阶段重新发现它；
- 它是否在后续任务再次被重复发现；
- 可否抽象成通用 tool；
- 若抽象，会不会过强或误导其他 carrier/domain。

重点寻找“重复支付”的 reasoning cost。

至少覆盖：

- R017 carrier completeness；
- R020 static/dynamic distinction；
- R022 future kernel / precision debt / certificate separation；
- R023 support carrier and suffix safety；
- R023I validation coverage correction；
- R025 regime/exhaustion and aligned-island boundary；
- R028 declared/realized future distinction。

---

## 6. Composition Calculus

必须研究 reasoning tools 是否可以安全组合。

例如：

`STATE_OBSERVATION_SPLIT`
→ `FUTURE_LANGUAGE_RELATIVITY`
→ `FACTOR_THROUGH_COMPLETE_ENCODING`
→ `NO_RESURRECTION_CHECK`

是否形成合法 pipeline？

相反：

`REALIZED_PATH_IRRELEVANCE`
→ `SAFE_DELETE`

必须被拒绝，除非另有 declared-language sufficiency theorem。

建立：

`R029_TOOL_COMPOSITION_MATRIX.json`

分类：

- always safe composition；
- safe with preconditions；
- diagnostic-only composition；
- known invalid composition。

至少给出最小反例。

---

## 7. Trigger / Selection Problem

Reasoning tool 若必须由研究员先知道答案才会触发，则没有减少 cold-start cost。

因此必须研究工具如何被选择：

- task tags；
- claim syntax；
- carrier declarations；
- words such as “minimal”, “all”, “always”, “composition”, “future”, “same”, “equivalent”, “causal”, “proof”, “benchmark” 等；
- declared dependencies；
- known downstream interfaces；
- shared-surface theorem types。

设计 explicit `trigger_signals`，并测试 false-positive / false-negative。

不要求本任务完成最终 context compiler；但 registry 必须足以支持 R030 编译器消费。

---

## 8. Tool Quality Metrics

候选 reasoning tool 至少按以下轴评价：

- `REUSE_COUNT`
- `EARLY_ERROR_DETECTION_VALUE`
- `FALSE_POSITIVE_RISK`
- `FALSE_NEGATIVE_RISK`
- `SEMANTIC_SCOPE_SHARPNESS`
- `TRUST_CLASS`
- `COMPOSITION_SAFETY`
- `PRIOR_ART_ROOTING_CONFIDENCE`
- `CONTEXT_COST`
- `COUNTEREXAMPLE_STRENGTH`

不得以“听起来深刻”作为 high-value tool 标准。

---

## 9. Adversarial Kill Targets

必须主动攻击：

1. `LOGIC_TOOL_IS_ALWAYS_PROOF_PRESERVING`
2. `PHILOSOPHY_LENS_CAN_BE_USED_AS_THEOREM`
3. `MORE_CONTEXT_ALWAYS_HELPS`
4. `EVERY_HISTORICAL_DISTINCTION_SHOULD_BE_INJECTED_EVERYWHERE`
5. `ONE_UNIVERSAL_REASONING_CHECKLIST_SUITS_ALL_TASKS`
6. `TRIGGER_KEYWORD_MATCH_IS_SEMANTICALLY_COMPLETE`
7. `A_TOOL_THAT_HELPED_ONCE_IS_REUSABLE`
8. `TOOL_COMPOSITION_IS_AUTOMATICALLY_SAFE`
9. `PRIOR_ART_ROOTING_DESTROYS_PROJECT_SPECIFIC_VALUE`
10. `THE_RESEARCH_REASONING_KERNEL_SHOULD_BECOME_A_NEW_MATHEMATICAL_FOUNDATION_PRIMITIVE`

对每条给最小反例或明确 survival 条件。

---

## 10. Seed Registry Minimum

即使部分候选被杀，最终至少尝试给以下工具冻结状态：

- `QUANTIFIER_SCOPE_CHECK`
- `NECESSARY_SUFFICIENT_SPLIT`
- `STATE_OBSERVATION_SPLIT`
- `CARRIER_TYPE_SPLIT`
- `STATIC_CORRECT_NOT_DYNAMIC_STATE`
- `ONE_STEP_EXACT_NOT_COMPOSITION_SAFE`
- `DECLARED_VS_REALIZED_FUTURE`
- `FACTOR_THROUGH_COMPLETE_ENCODING`
- `SUPPORT_COUNT_PROVENANCE_SPLIT`
- `RESOURCE_EQUAL_SEMANTIC_FIBRE_CHECK`
- `ROOT_COVERAGE_EVIDENCE_CHECK`
- `CAUSAL_PREDICTIVE_RETROSPECTIVE_SPLIT`
- `PRIOR_ART_REDUCTION`
- `COUNTEREXAMPLE_MINIMIZATION`
- `REGIME_EXHAUSTION`

每个必须返回 `KEEP / NARROW / MERGE / KILL / INTERPRETIVE_ONLY`。

---

## 11. Executable Prototype

建议建立：

- `experiments/r029_reasoning_tool_registry.py`
- `experiments/r029_reasoning_tool_oracle.py`
- `tests/test_r029_reasoning_tools.py`

Executable 层不需要“自动证明哲学”，而应至少能：

- validate registry schema；
- 检查 tool trust class；
- 检查 required fields / anti-examples；
- 对声明的 composition rule 做 consistency check；
- 给 task/claim metadata 产生候选 tool ranking；
- 对 mutation fixtures 检查关键工具是否被触发。

---

## 12. Prior-art Rooting

必须系统比较但不得简单同一化：

- classical propositional / first-order logic；
- modal and temporal logic；
- type theory / refinement types；
- abstract interpretation / static analysis；
- proof tactics / proof planning；
- model checking；
- program logics；
- epistemic logic；
- causal inference / counterfactual reasoning；
- philosophy of science / explanation / theory reduction；
- automated theorem proving heuristics；
- scientific discovery / hypothesis generation systems；
- decision procedures and counterexample-guided abstraction refinement。

目标不是声称“逻辑是 Enterprise Math 发明的工具”，而是判断：

> 现有逻辑/哲学方法怎样被编译成 Enterprise Math researcher 的 typed, evidence-aware, future-relative context layer；项目特有的 residue 到底在哪里？

---

## 13. Required Deliverables

至少：

1. `docs/R029_RESEARCH_REASONING_KERNEL_REPORT.md`
2. `reasoning_tools.json`
3. `R029_REASONING_OPERATOR_LINEAGE_MATRIX.md`
4. `R029_TOOL_COMPOSITION_MATRIX.json`
5. `R029_TOOL_PRIOR_ART_MATRIX.md`
6. executable registry/oracle prototype；
7. focused tests；
8. machine summary；
9. minimal counterexamples for killed universal tool claims；
10. proposed `META_TOOL_DELTA` return schema for future research tasks。

---

## 14. META_TOOL_DELTA Proposal

研究一个最小回流格式，使未来研究 return 除 theorem / counterexample / executable 外，可额外返回：

```text
META_TOOL_DELTA:
- new_tool
- strengthened_tool
- narrowed_tool
- killed_tool
- new_trigger
- new_counterexample
- composition_rule
```

但不得在本任务中预设所有研究都必须产生 meta-tool delta；先用历史回放验证该机制是否高信号、低噪声。

---

## 15. Success / Kill Returns

优先成功返回：

`RESEARCH_REASONING_KERNEL_FOUND / LOGIC_PHILOSOPHY_TOOLS_TYPED / HISTORICAL_RESTART_COST_CLASSIFIED / TOOL_COMPOSITION_BOUNDARIES_FROZEN / CONTEXT_COMPILER_READY / NOT_CANONICAL`

如果只有小核稳定：

`SMALL_TRUSTED_REASONING_KERNEL_FOUND / MOST_PHILOSOPHY_TOOLS_INTERPRETIVE_ONLY / HIGH_VALUE_DIAGNOSTICS_FROZEN / NOT_CANONICAL`

如果工具化本身过度：

`UNIVERSAL_REASONING_TOOLING_KILLED / TASK_RELATIVE_META_TOOLS_ONLY / CONTEXT_OVERLOAD_BOUNDARY_FOUND / NOT_CANONICAL`

不得为了建立“大而全 reasoning OS”而保留低价值工具。
