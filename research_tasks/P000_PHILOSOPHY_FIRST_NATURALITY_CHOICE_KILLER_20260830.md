<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-PHILOSOPHY-FIRST-NATURALITY-CHOICE-KILLER",
  "title": "哲学先行 Q7：自然性与任意选择杀手",
  "kind": "RESEARCH",
  "owner": "research/p000-phil-q7-naturality-choice-killer",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Build exact finite certificates that distinguish a genuinely natural construction from an arbitrary representative choice by testing equivariance under primitive-preserving automorphisms of the input model, then apply the criterion to frames, lift sections, probe bases and coordinate selections.",
  "next_action": "Define the smallest naturality square for model automorphisms and candidate constructions, enumerate automorphism orbits in symmetric finite models, and exhibit constructions that exist pointwise but cannot be selected equivariantly.",
  "dependencies": [],
  "source_refs": [
    "research_tasks/P000_S4_LIFT_UNIVERSALITY_EXTENSION_V13_20260830.md@main",
    "projects/enterprise-math/P000_NATIVE_FCC_STRICT_BRIDGE.json@global-main",
    "classical lens: natural transformations / equivariant choice obstructions"
  ],
  "evidence_status": "DIRECT_USER_PHILOSOPHY_FIRST_DIRECTION / FIRST_WAVE_UNEXECUTED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "P000",
    "naturality",
    "canonicality",
    "automorphism",
    "choice",
    "equivariance",
    "symmetry"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-PHILOSOPHY-FIRST-NATURALITY-CHOICE-KILLER",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PHQ7",
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

# 哲学先行 Q7：自然性与任意选择杀手

Status: `READY / P1 / NO-ARBITRARY-REPRESENTATIVE`

## Mother question

“每个模型都能选到一个对象”不等于“存在自然选择”。

给定 primitive-preserving automorphism \(\phi:M\to M'\) 与构造 \(C\)，应检查：

\[
C(\phi(x))\stackrel{?}{=}\phi(C(x)).
\]

如果所有候选都被对称群移动，就不存在不依赖 presentation 的自然选择。

## Frozen inputs and scope

只审计实际存在的 frame、lift section、probe basis、coordinate selection 等候选。允许 automorphism orbit、equivariance、自然变换语言。不得因某个代表计算最简单就赋予它 native 优先地位。

## Hard target and required outputs

Hard target: `P000_NATURALITY_AND_ARBITRARY_CHOICE_EXACTLY_SEPARATED`

1. 定义 model-level naturality/equivariance criterion。
2. 构造至少 3 个 symmetric finite models，计算 primitive-preserving automorphism group 及候选选择的轨道。
3. 给出至少一个 `EXISTS_POINTWISE_BUT_NO_EQUIVARIANT_SELECTION` 证书。
4. 对 current frame/lift/probe/coordinate 候选逐一测试。
5. 区分唯一对象、唯一同构类、固定点、自然 section 四种强度。
6. 形成一个可复用的 finite naturality checker 规范。

## Research value to preserve

大量“看起来天然”的数学对象只是把对称性打破后任取代表。这个任务把“自然”从审美词汇变成可证的 equivariance 条件。

## Success, kill, and return criteria

有效终态：`NONCANONICAL_CHOICE_CERTIFICATES_CONSTRUCTED` / `NATURAL_SELECTION_PROVED_FOR_DECLARED_CLASS` / `CURRENT_AUTOMORPHISM_LANGUAGE_INSUFFICIENT`。不存在 automorphism 计算或自然性方程验证的主观判断不算完成。
