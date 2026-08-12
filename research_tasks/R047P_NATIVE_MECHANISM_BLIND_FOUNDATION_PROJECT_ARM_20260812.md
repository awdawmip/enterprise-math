<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R047P-NATIVE-MECHANISM-BLIND-FOUNDATION-PROJECT-ARM",
  "title": "R047P Native Mechanism Blind Foundation Generation — Project Arm",
  "kind": "RESEARCH",
  "owner": "program/foundational-logic-engineering-inversion",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_MECHANISM_GENERATION / BLIND_CALIBRATION",
  "frontier": "Generate and freeze a diverse family of small native mechanisms from a target-withheld relational substrate before any engineering calibration criteria are revealed.",
  "next_action": "Consume only the frozen R047 blind native foundation packet and mandatory repository policy; generate 4-8 internally justified native mechanisms, freeze the candidate set, and return without opening the sealed calibration target.",
  "dependencies": [
    {
      "target": "research_inputs/R047_BLIND_NATIVE_FOUNDATION_PACKET_20260812.md @ 2f52b395de8d0bf356c0bc460c485b6dfcd03b9b",
      "action": "CONSUME_ONLY_FROZEN_BLIND_FOUNDATION_PACKET",
      "satisfied": true
    },
    {
      "target": "research_inputs/R047_CALIBRATION_TARGET_SEAL_20260812.json @ ebab0689f40ff55c224f978dd1413d0b347762a8",
      "action": "VERIFY_TARGET_PRECOMMITTED_WITHOUT_OPENING_CONTENT",
      "satisfied": true
    },
    {
      "target": "Foundational Logic V1 and Native-Semantics Admissibility Gate V3",
      "action": "CONSUME_FOUNDATIONAL_AND_SEMANTIC_GATES",
      "satisfied": true
    }
  ],
  "source_refs": [
    "R047 blind foundation packet",
    "precommitted calibration-target seal only; target content withheld"
  ],
  "evidence_status": "BLIND_FOUNDATION_CANDIDATE_GENERATION",
  "last_progress_ref": "R046 calibration target frozen before R047 candidate generation; content intentionally withheld.",
  "last_progress_at": "2026-08-12T22:49:00+08:00",
  "hard_block": null,
  "tags": [
    "R047P",
    "native-mechanism",
    "blind-generation",
    "foundation",
    "theory-explosion",
    "target-withheld",
    "anti-retrofit"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R047P",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:5e1e1e3dd925c9c1a434e8dae7eafd4b5a8e62a88cd725f43d5aa7b400cad242",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R047P — Native Mechanism Blind Foundation Generation — Project Arm

Status: `READY / P0 / BLIND FOUNDATION GENERATION / CALIBRATION SEALED / NOT CANONICAL`

## 0. 母问题

在不知道后续工程校准目标具体内容的前提下，仅从最小 native relational substrate 与进取数论现有 foundational logic 出发：

> **能否自然地产生一组小而强、可递归、可组合、有限信息的 native mechanism，使其本身具有值得后续校准的宏观生成潜力？**

本任务只做 FOUNDATION GENERATION，不做 CALIBRATION。

## 1. 严格输入隔离

允许读取：

1. `AGENTS.md` 中执行规则；
2. `FOUNDATIONAL_LOGIC.md` / `foundational_logic.json`；
3. `native_semantics_admissibility.json` V3；
4. `research_inputs/R047_BLIND_NATIVE_FOUNDATION_PACKET_20260812.md`；
5. `research_inputs/R047_CALIBRATION_TARGET_SEAL_20260812.json`，但只允许确认 seal metadata，不允许寻找被封存 target 内容。

在候选集冻结之前，禁止消费其它项目研究成果作为 startup direction，特别禁止：

- R046 outputs、PR #534、R046 Global Knowledge、R046 对话内容；
- 任何后续 calibration interface；
- 任何根据经典输出倒推 native primitive 的方案。

如果当前项目上下文不可避免地暴露了 target-specific 信息，必须在 contamination audit 里记录，但不得据此生成、调整、排序或杀死候选。

## 2. THEORY_EXPLOSION 执行方式

本任务不预选“最可能正确”的 collapse。

允许错误、奇怪结构和多条并行分支。不要自动把所有候选快速收敛成一个赢家。

第一阶段至少形成 4 个、最多 8 个 serious candidate branches；每个 branch 都必须来自 packet 中允许的 native-side construction language，而不是来自对工程目标的猜测。

只有语义非法、内部自相矛盾或立即退化为空结构的候选可以早杀；其它失败应保留其暴露出的结构。

## 3. 每个候选必须冻结的内容

对每个 candidate `M_i`：

- exact N0 substrate；
- introduced N1/N2 choices，若有；
- typed dependency DAG；
- state carrier；
- local/update law；
- collapse/quotient/support semantics，若有；
- scale/refinement semantics，若有；
- deterministic / branching / stochastic typing；
- exact invariants / monotones / conservation laws；
- recursive/composition closure；
- finite-information cost；
- free parameters 与 arbitrary choices；
- internal counterexamples / degeneracies；
- productive failure lesson；
- candidate exposed new question/object；
- contamination statement。

禁止写任何“它可能对应某个具体 R046 kernel member”的内容。

## 4. 允许的内部比较

只能按 native-side internal criteria 比较：

- semantic admissibility；
- closure / recursion；
- composition safety；
- finite-information economy；
- choice-independence / equivariance；
- nontrivial scale behavior；
- generative richness；
- internal theorem density；
- parameter economy。

这些比较只能用于描述 Pareto 结构，不得选定 calibration winner。

## 5. Candidate freeze gate

候选只有在以下对象全部写入 artifacts 后才算冻结：

- candidate definitions；
- exact parameter domains；
- update/collapse laws；
- internal theorem/counterexample ledger；
- candidate hashes/IDs；
- contamination audit。

冻结后不得再因后续 calibration target 而改 candidate definition 或参数范围。以后若修改，必须作为新 generation，不得沿用 blind claim。

## 6. Prior art 边界

候选定义冻结前，不要用外部 classical/effective prior art 去引导候选结构。

冻结后可做 prior-art rooting，但只用于归因和边界，不得改变已冻结 candidate。

## 7. 必须返回

至少：

- `research/r047p/R047P_FOUNDATION_REPORT.md`；
- `research/r047p/R047P_FOUNDATION_CANDIDATE_SET.json`；
- `research/r047p/R047P_NATIVE_DERIVATION_LEDGER.json`；
- `research/r047p/R047P_INTERNAL_STRUCTURE_MATRIX.json`；
- `research/r047p/R047P_PRODUCTIVE_FAILURES.json`；
- `research/r047p/R047P_CONTAMINATION_AUDIT.json`；
- exact checker/tests for any machine-checkable claims。

返回时不要打开 calibration target，也不要提出针对目标的候选修改。

可接受返回：

`DIVERSE_NATIVE_CANDIDATE_SET_FROZEN / FOUNDATION_PHASE_COMPLETE / CALIBRATION_NOT_OPENED / NOT_CANONICAL`

或更强的 ontology replacement / small mechanism family result。

如果最小 substrate 被严格证明太弱，也允许返回一个 precise missing-primitive theorem/counterexample，但新增 primitive 必须由 native-side necessity 驱动，不能由 calibration target 驱动。
