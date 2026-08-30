<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id":"RS-ADDMUL-WITT-GHOST-MULTISCALE-BRIDGE",
  "title":"加乘桥 A4：Witt / Ghost 多尺度坐标桥",
  "kind":"RESEARCH","owner":"research/addmul-witt-ghost-multiscale-bridge","base_state":"READY","priority":"P1","leverage":"HIGH",
  "frontier":"Extract the finite exact content of big and p-typical Witt ghost coordinates as a multiscale addition–multiplication bridge, with divisor and prime-power indexing, and determine whether an Enterprise-compatible finite interface adds information beyond binomial/delta/valuation routes.",
  "next_action":"Freeze finite ghost formulas, classify forward/inverse integrality and truncation compatibility, then compare divisor-indexed and p-power-indexed coordinates against current scale/valuation tools before proposing any Witt-lite Enterprise interface.",
  "dependencies":[],
  "source_refs":["classical: big Witt and p-typical Witt ghost-coordinate formulas","research_method_inventory.json@main","src/enterprise_math/precision.py@main"],
  "evidence_status":"DRIVER_ROADMAP_FROM_ADD_MUL_EXTERNAL_THEORY_SCOUT / FIRST_WAVE_UNEXECUTED","last_progress_ref":null,"last_progress_at":null,"hard_block":null,
  "tags":["addmul","Witt","ghost-coordinate","divisor","prime-power","multiscale","precision"],"claim_lease_minutes":240,
  "created_by_role":"RESEARCH_DRIVER","task_authority":"PUBLISHED_REGISTERED","publication_contract":"RESEARCH_TASK_PUBLICATION_V1","publication_template":"RESEARCH_TASK_PUBLICATION_TEMPLATE_V1","registry_key":"RS-ADDMUL-WITT-GHOST-MULTISCALE-BRIDGE","parent_objective_id":"OBJ-ADDMUL-BRIDGE-STRUCTURE","parent_objective_generation_id":"OG-9D6617146723B8E72C6F","identity_policy":"AUTO_RESOLVE_OR_ALLOCATE","final_response_identity_policy":"INHERIT_GLOBAL","identity_lane":"AMWITT","origin_kind":"DRIVER_ROADMAP","task_lineage":"NEW_DIRECTION","parent_task_id":null,"successor_gate":null,
  "policy_review":{"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c","review_state":"PASS","temporary_overrides":[]}
}
-->

# 加乘桥 A4：Witt / Ghost 多尺度坐标桥

Status: `READY / P1 / MULTISCALE`

## Mother question

Witt 向量把复杂环运算设计成 ghost 坐标中的逐坐标运算；big Witt 按 divisor 尺度组织，p-typical 按 \(1,p,p^2,\ldots\) 组织。能否抽取出有限、整数、operation-safe 的多尺度加乘桥，而不是整体搬入成熟理论？

## Frozen inputs and scope

允许标准 big/p-typical ghost polynomials，但先做有限截断。forward map 必须 exact；inverse 必须逐项检查整除性。只比较 operation、scale、information loss；与现有 precision/valuation 工具去重。无限序列不作为自然底层状态。

## Hard target and required outputs

Hard target: `WITT_GHOST_MULTISCALE_ADD_MUL_BRIDGE_ENTERPRISE_TRANSLATION_CLASSIFIED_OR_OBSTRUCTED`

1. 固定 big Witt convention，例如 \(w_n(a)=\sum_{d\mid n}d\,a_d^{n/d}\)，并在 finite divisor-closed truncation 验证运算。
2. 固定 p-typical ghost coordinates，证明 forward triangular structure。
3. 分类 ghost-to-Witt inverse 的 integrality、唯一性和失败 witness。
4. 比较 divisor index、prime-power index 与当前 precision/valuation scale。
5. 分类 truncation projection 是否 commute；若否定义 exact projection defect。
6. 只在确有新增信息时提出最小 `WITT_LITE_BRIDGE`；否则返回 no-go。
7. exact checker 覆盖小 `N` 与 `p=2,3,5`。

## Research value to preserve

真正要测试的是 `ghost coordinate + integrality gate + scale projection defect`，而不是 Witt 名称本身；负结果也能防止后续重复引入过重理论。

## Success, kill, and return criteria

有效终态：`FINITE_WITT_GHOST_BRIDGE_CLASSIFIED` / `FORWARD_EXACT_INVERSE_INTEGRALITY_OBSTRUCTED` / `DUPLICATES_EXISTING_SCALE_DEFECT_TOOLING`。不得隐藏整除条件，不得把 infinite coordinate 当有限状态，不得用引用代替有限验证。
