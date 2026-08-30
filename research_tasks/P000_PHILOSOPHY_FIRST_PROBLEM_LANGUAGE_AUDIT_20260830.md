<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-PHILOSOPHY-FIRST-PROBLEM-LANGUAGE-AUDIT",
  "title": "哲学先行 Q1：P000 问题语言与对象层级审判",
  "kind": "RESEARCH",
  "owner": "research/p000-phil-q1-problem-language-audit",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Audit whether current P000 questions are posed at the correct mathematical object level: distinguish native objects, presentations, observations, chosen coordinates, automorphism groups, lift data and equivalence classes, and identify cases where proving the stated theorem would answer a presentation-dependent or strictly weaker question.",
  "next_action": "Take the current rotation/lift/canonicality mother questions one by one, write their object/equivalence/observable signatures, then construct exact paired formulations or countermodels showing which formulations are invariant, equivalent, strictly weaker, or ill-posed.",
  "dependencies": [],
  "source_refs": [
    "projects/enterprise-math/00_CURRENT_FOUNDATION.md@global-main",
    "research_tasks/P000_S4_LIFT_UNIVERSALITY_EXTENSION_V13_20260830.md@main",
    "projects/enterprise-math/P000_NATIVE_FCC_STRICT_BRIDGE.json@global-main",
    "classical lens: Grothendieck relative viewpoint / functoriality / representability"
  ],
  "evidence_status": "DIRECT_USER_PHILOSOPHY_FIRST_DIRECTION / FIRST_WAVE_UNEXECUTED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "P000",
    "philosophy-first",
    "problem-language",
    "object-level",
    "invariance",
    "countermodel",
    "definition-audit"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-PHILOSOPHY-FIRST-PROBLEM-LANGUAGE-AUDIT",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PHQ1",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 哲学先行 Q1：P000 问题语言与对象层级审判

Status: `READY / P0 / QUESTION-BEFORE-PROOF`

## Mother question

在进入证明之前，当前 P000 研究究竟在问“真实的 native 对象”还是在问某个 presentation、坐标、frame、carrier readout 或任意选择的性质？

对每个主要问题建立签名：

\[
(\text{object},\ \text{allowed equivalence},\ \text{observable},\ \text{claimed invariant},\ \text{quantifier level}).
\]

尤其审判“旋转群是什么”“某个 lift 是否存在”“某个 lift 是否典范”“某个 frame 是否自然”等问题是否处于正确对象层。

## Frozen inputs and scope

P000 本身保持基础起点，不在本任务中证明或证伪。Gen12 的一个忠实 split \(S_4\) witness 与 Gen13 的普遍性/规范性/残差问题可作当前事实输入，但不得把单一 witness 当作对象定义。允许使用范畴、群胚、模型论、结构主义语言作为比较工具；任何工具只有在产生严格区分或等价定理时才保留。

## Hard target and required outputs

Hard target: `P000_PROBLEM_LANGUAGE_AND_OBJECT_LEVEL_EXACTLY_AUDITED`

1. 列出当前至少 8 个 load-bearing mother questions，并给出各自的对象层级与量词层级。
2. 对每个问题标记：`WELL_POSED_NATIVE` / `PRESENTATION_DEPENDENT` / `STRICTLY_WEAKER_PROXY` / `UNDERDETERMINED` / `EQUIVALENT_AFTER_EXPLICIT_HYPOTHESES`。
3. 至少构造 3 对有限模型或 presentation，证明“同一 native 内容、不同表面答案”或“同一表面答案、不同 native 内容”。
4. 对被杀死的问题给出最小改写，不允许只写哲学评论。
5. 给出一个可复用的 question-signature checker 规范，能在后续任务中检查对象、等价关系、观察量与量词是否混层。
6. 明确哪些现有目标可以继续，哪些应暂停直到对象重定义完成。

## Research value to preserve

如果一个困难问题从一开始就问错对象，继续提高证明强度只会加固错误坐标。该任务保留“先审判问题语言”的可证证据，使后续研究把算力用于 native invariant，而不是 presentation artifact。

## Success, kill, and return criteria

有效终态：`PROBLEM_LANGUAGE_REPAIRED_WITH_EXACT_COUNTERMODELS` / `CURRENT_MAJOR_QUESTIONS_PROVED_OBJECT_LEVEL_SOUND` / `MIXED_RESULT_WITH_EXPLICIT_KILLED_QUESTIONS`。没有有限反例、等价证明或严格对象签名的纯哲学陈述不算完成。
