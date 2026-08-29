<!-- ENTERPRISE_MATH_TASK_V1
{
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "parent_objective_id": "OBJ-SEED6-MULTIPLICATIVE-GROWTH-GEOMETRY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "claim_lease_minutes": 240,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "task_id": "RS-SEED6-BRIDGE-CELL-DEGENERACY-STRATIFICATION",
  "title": "Seed-6 桥胞退化谱：重复原子、种子碰撞、素数幂与合数列",
  "priority": "P1",
  "leverage": "MEDIUM",
  "frontier": "The clean seed-6 cells use distinct primes p,q>3, but the geometry changes when p=q, when a new atom equals 2 or 3, or when prime powers/composites replace prime atoms. Classify these degenerations as singular strata rather than discarding them as edge cases.",
  "next_action": "Start from the exact three-pairing cell and column models, then systematically impose atom equalities and support overlaps; compute how many pairing states, vertices, gcd labels and cells collapse in each case, and organize the results into a degeneration poset.",
  "dependencies": [],
  "source_refs": [],
  "evidence_status": "DIRECT_USER_DIRECTION / POSITIVE_DEGENERATION_STUDY / NO_FACTORIZATION_OBJECTIVE",
  "tags": ["seed6", "degeneracy", "singular-strata", "prime-powers", "composites", "pairing-collapse"],
  "registry_key": "RS-SEED6-BRIDGE-CELL-DEGENERACY-STRATIFICATION",
  "identity_lane": "S6D"
}
-->

# Seed-6 桥胞退化谱：重复原子、种子碰撞、素数幂与合数列

## Mother question

干净模型使用互异原子 \(2,3,p,q\)。但一旦发生 \(p=q\)、\(p=2\)、\(p=3\)，或者把 \(p,q\) 换成素数幂/合数，三配对态、桥矩形和 gcd 标签都会发生折叠。本任务把这些情形视为几何的 singular strata，研究 Seed-6 桥胞有哪些退化类型，退化之间如何组织。

## Frozen inputs and scope

1. 以干净四原子三配对模型为参考，但不得假设其结论在退化处自动成立。
2. 必须覆盖：\(p=q\)；\(p\) 或 \(q\in\{2,3\}\)；\(p^a,q^b\)；两个合数拥有部分重叠 support；\(r=1\) 作为边界控制可选。
3. 允许 valuation vector、multiset matching、partition、gcd-support lattice。
4. 退化按“状态/边/胞被识别”来定义，不能用数值接近描述。
5. 禁止把退化解释成“更容易分解”。

## Hard target and required outputs

Hard target: `SEED6_BRIDGE_CELL_DEGENERACY_STRATIFICATION_CLASSIFIED`

A. 对四原子 multiset 的 equality pattern 做完整 partition-type 分类，并确定每类有多少不同 perfect pairings。

B. 对 \(p=q\) 精确说明为什么 \(\{6,p^2\}\)、\(\{2p,3p\}\) 只剩两个不同 pairing states，并判断局部胞应视为边、折叠三角还是带重数胞。

C. 对 \(p=2\)、\(p=3\) 等 seed collision，记录 carrier label 重复、顶点重合、幂指数变化。

D. 对 prime-power columns \((2p^a,3p^a)\) 研究 exponent thickness 是否提供新的层级，还是仅为同一 carrier 纤维内的径向参数。

E. 对 composite columns \(r\) 分类为 squarefree、prime power、mixed support，并判断“列”是否仍是原子列或应拆成多 carrier 结构。

F. 构造 degeneration poset / adjacency diagram：哪些 generic cell 通过哪些等式约束退化到哪些 singular class。

G. 给出 exact checker，至少覆盖所有 \(p,q\le200\) 的素数/素数幂和一组小合数，验证状态数与 stratification。

## Research value to preserve

退化往往比 generic 情形更能说明一个几何定义是否自然。若 pairing cell 的定义在 \(p=q\) 或 carrier overlap 时没有一致极限，那么它可能只是漂亮记号；反之，一个清晰的退化谱可以为后续更大胞复形提供真正的奇点/边界结构。

## Success, kill, and return criteria

Success：generic 与各主要 singular class 有统一分类；给出 degeneration poset 或证明不存在自然单一 poset；prime power 与 composite 情形的结构地位明确。

Kill：把所有非互异素数情形一律称为“异常”而不分类；用整数大小差判定退化；把重复因子直接转成算法优势。

Return：task-terminal；可返回 `DEGENERATION_SPECTRUM_CLASSIFIED / MULTIPLE_INCOMPATIBLE_MODELS / PRIME_POWER_FIBER_STRUCTURE_FOUND / NEGATIVE_BOUNDARY`。
