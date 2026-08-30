<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-ADDMUL-BINOMIAL-CROSS-EFFECT-CALCULUS",
  "title": "加乘桥 A1：整数二项式 Jet 与高阶 Cross-Effect 演算",
  "kind": "RESEARCH",
  "owner": "research/addmul-binomial-cross-effect-calculus",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Determine the exact integer calculus carried by Q_k(n)=binom(n,k): addition should act by Vandermonde convolution, multiplication should appear at k=2 as an additive cross-effect, and higher mixed cross-effects must be classified without overclaiming that multiplication has ceased to be primitive globally.",
  "next_action": "Prove the all-k convolution and cross-effect formulas over Z, classify r-fold mixed differences and reconstruction strength, then test finite-precision projection/carry compatibility against the existing mixed-difference and precision-defect mechanisms.",
  "dependencies": [],
  "source_refs": [
    "classical: Chu–Vandermonde convolution for binomial polynomials",
    "research_method_inventory.json@main",
    "src/enterprise_math/precision.py@main",
    "research_tasks/FQ008_TRANSVERSE_INDEPENDENCE_STEWARD_VERIFICATION_20260822.md@main"
  ],
  "evidence_status": "DRIVER_ROADMAP_FROM_ADD_MUL_EXTERNAL_THEORY_SCOUT / FIRST_WAVE_UNEXECUTED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "addmul",
    "binomial",
    "cross-effect",
    "finite-difference",
    "integer-valued-polynomial",
    "defect",
    "precision"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-ADDMUL-BINOMIAL-CROSS-EFFECT-CALCULUS",
  "parent_objective_id": "OBJ-ADDMUL-BRIDGE-STRUCTURE",
  "parent_objective_generation_id": "OG-9D6617146723B8E72C6F",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "AMBIN",
  "origin_kind": "DRIVER_ROADMAP",
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

# 加乘桥 A1：整数二项式 Jet 与高阶 Cross-Effect 演算

Status: `READY / P0 / EXACT-INTEGER`

## Mother question

对 \(Q_k(n)=\binom nk\) 与 \(J_K(n)=(Q_0,\ldots,Q_K)\)，精确分类
\[
Q_k(x+y)=\sum_{i=0}^kQ_i(x)Q_{k-i}(y),
\qquad
Q_2(x+y)-Q_2(x)-Q_2(y)=xy.
\]
乘法在什么严格意义上是加法 observable 的二阶 cross-effect？高阶 mixed cross-effect 是否形成可复用整数演算？

## Frozen inputs and scope

以 `Z` 为主；Vandermonde 可作经典输入但不计新发现。允许高阶有限差分/极化。必须区分“从 `(+ ,Q_2)` 可恢复乘法”与“乘法不再是独立原语”。有限精度部分先复用现有 precision、mixed-difference、defect 机制；不以连续极限作底层定义。

## Hard target and required outputs

Hard target: `INTEGER_BINOMIAL_JET_ADDITIVE_CROSS_EFFECT_CALCULUS_CLASSIFIED`

1. 证明 all-k 卷积律、有限截断闭合边界。
2. 给出从 `(+ ,Q_2)` 恢复 `xy` 的最小数据定理。
3. 分类 `Q_k` 的二元/r 元 cross-effect：非零阶、消失阶、整数系数、对称/多线性边界。
4. 比较幂基与二项式基的整数有限差分闭合性。
5. 分类精度投影后 carry/detail/cross-effect defect，并给出现有工具复用判定。
6. exact checker 至少覆盖 `K<=8`；输出最小后续接口。

## Research value to preserve

保留“加法 + 高阶 observable 产生乘法交叉信息”的纯整数机制；若高阶 operation-safe 扩展失败，也冻结最小失败位置，避免只剩哲学解释。

## Success, kill, and return criteria

有效终态：`EXACT_CROSS_EFFECT_CALCULUS_CONSTRUCTED` / `LOW_ORDER_BRIDGE_EXACT_HIGHER_EXTENSION_OBSTRUCTED` / `STANDARD_IDENTITY_ONLY_NO_ADDITIONAL_RESIDUE`。不得把 Vandermonde 冒充原创，不得用低阶拟合代替全阶证明，不得静默用有理除法破坏整数闭合。
