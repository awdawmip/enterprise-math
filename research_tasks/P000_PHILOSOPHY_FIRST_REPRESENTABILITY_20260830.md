<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-PHILOSOPHY-FIRST-REPRESENTABILITY",
  "title": "哲学先行 Q6：Observation Profile 的表示性与虚拟 Cell 边界",
  "kind": "RESEARCH",
  "owner": "research/p000-phil-q6-representability",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "MEDIUM",
  "frontier": "After defining a probe category, determine which compatible observation profiles are represented by an actual native Cell or Full-Cell state and which profiles are merely formally consistent virtual objects in a presheaf-like completion.",
  "next_action": "Fix the smallest validated probe family from the reconstruction task or an independent toy substrate, enumerate compatible profiles, test exact realizability by native finite models, and identify the first representability obstruction or a finite representability theorem.",
  "dependencies": [],
  "source_refs": [
    "projects/enterprise-math/00_CURRENT_FOUNDATION.md@global-main",
    "classical lens: representable functors / presheaf completion",
    "dependency-by-result: consume Q2 probe definitions only if Q2 has frozen an exact probe family"
  ],
  "evidence_status": "DIRECT_USER_PHILOSOPHY_FIRST_DIRECTION / FIRST_WAVE_UNEXECUTED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "P000",
    "representability",
    "observation-profile",
    "virtual-cell",
    "presheaf",
    "completion"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-PHILOSOPHY-FIRST-REPRESENTABILITY",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PHQ6",
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

# 哲学先行 Q6：Observation Profile 的表示性与虚拟 Cell 边界

Status: `READY / P1 / REPRESENTABILITY`

## Mother question

即使一个 observation profile 对所有 probes 都内部一致，它是否一定来自一个真实 native Cell？

若把所有 probe responses 组成形式对象，可能存在：

\[
F:\mathcal P^{op}\to \mathbf{FinSet}
\]

满足局部兼容，却没有任何实际 \(X\) 使 \(F\cong \mathrm{Obs}_X\)。

这条边界决定“形式完备化”是否引入了虚拟 Cell。

## Frozen inputs and scope

若 Q2 已冻结 exact probe family，则直接复用；否则可在独立 toy finite substrate 上先建立最小 representability 实验，不得猜测 Q2 的结论。presheaf 只是候选语言，不默认所有形式对象都有 native 含义。

## Hard target and required outputs

Hard target: `P000_OBSERVATION_PROFILE_REPRESENTABILITY_BOUNDARY_CLASSIFIED`

1. 明确 actual native objects 到 observation profiles 的映射。
2. 枚举 bounded profile space 与 realizable image。
3. 构造最小 nonrepresentable compatible profile，或证明指定有限类全部 representable。
4. 分类 representability obstruction 来自哪类全局约束。
5. 判断加入虚拟 profiles 是否提高推理能力，还是只产生无 native 语义的冗余。
6. 给出 actual/virtual 边界的 exact checker。

## Research value to preserve

格罗滕迪克式扩充空间只有在“新对象为什么必须存在”被严格回答时才有价值。该任务防止我们因抽象诱惑而把所有形式 presheaf 自动称为 Cell。

## Success, kill, and return criteria

有效终态：`NONREPRESENTABLE_PROFILE_EXACTLY_WITNESSED` / `FINITE_REPRESENTABILITY_THEOREM` / `PROBE_LANGUAGE_NOT_READY_FOR_REPRESENTABILITY`。若依赖对象尚未定义，应返回 precise dependency boundary，而不是虚构完成。
