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
  "task_id": "RS-SEED6-BRIDGE-TRIANGLE-LOCAL-GROWTH",
  "title": "从 6 出发的乘法桥三角：局部生长、载体标记与非平凡不变量",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Starting from the fixed seed 6=2*3, study the positive family T_r={6,2r,3r} for primes r>3 as a local multiplicative cell. Separate identities forced by commutativity from genuinely useful carrier/incidence/orientation invariants, and determine the exact local symmetry and growth rules before any global or algorithmic interpretation.",
  "next_action": "Freeze T_r for primes r>3, enumerate the first several hundred prime columns, classify pairwise gcd/carrier labels, conserved products and automorphisms, and search for local invariants that persist under r variation but are not tautological rewrites of 6=2*3.",
  "dependencies": [],
  "source_refs": [],
  "evidence_status": "DIRECT_USER_DIRECTION / POSITIVE_GROWTH_ONLY / SEED6_FIXED / NO_FACTORIZATION_OBJECTIVE",
  "tags": ["seed6", "multiplicative-growth", "bridge-triangle", "carrier", "local-cell", "positive-research"],
  "registry_key": "RS-SEED6-BRIDGE-TRIANGLE-LOCAL-GROWTH",
  "identity_lane": "S6T"
}
-->

# 从 6 出发的乘法桥三角：局部生长、载体标记与非平凡不变量

## Mother question

固定 \(6=2\cdot3\)。对每个素数 \(r>3\)，考虑局部三元组

\[
T_r=\{6,2r,3r\}.
\]

研究问题不是这些整数在普通数轴上“离多远”，也不是如何由它们恢复某个因子，而是：从最小双质种子 6 出发，一个新乘法原子 \(r\) 会生成怎样的最小局部胞？要求先把显然由交换律、结合律推出的恒等式与真正能组织多个 \(T_r\) 的结构量分开。

## Frozen inputs and scope

1. 固定种子 \(6=2\cdot3\)；本任务不先一般化成任意 \(ab\)。
2. 主样本先取素数 \(r>3\)；重复素数、\(r=2,3\)、素数幂和合数由退化任务处理。
3. 允许使用乘法、整除、gcd、素因子支撑、指数向量、有限图/超图/胞复形语言。
4. 禁止把 \(|x-y|\)、Fermat offset、平方壳距离、factor-edit L1 当作主几何。
5. 禁止提出因子搜索、端点恢复、分解成功率或性能收益。
6. 恒等式 \(6(2r)(3r)=(6r)^2\) 可作为观察起点，但不得仅因它成立就宣称发现新结构。
7. 至少覆盖前 500 个 \(r>3\) 的素数做 exact-integer census；有限统计只用于发现/反驳规律。

## Hard target and required outputs

Hard target: `SEED6_LOCAL_BRIDGE_TRIANGLE_GEOMETRY_CLASSIFIED`

A. 给出 \(T_r\) 的精确定义、顶点/边/载体标记规则，并至少比较两种自然的局部图或超图模型。

B. 计算并证明 \(\gcd(6,2r),\gcd(6,3r),\gcd(2r,3r)\)，判断这些标签是否足以唯一重建局部三角的 carrier-incidence 类型。

C. 分类局部自同构：哪些置换保持数值、carrier 标签、乘积守恒、方向或其他拟议结构；区分 unlabeled 与 labeled 模型。

D. 搜索至少三类候选局部不变量：carrier-incidence signature、valuation-support signature、product-square relation、orientation / ordered-pair data、可与其他三角拼接的边类型等。

E. 对每个候选不变量标注 `TAUTOLOGICAL / MODEL_DEPENDENT / EXACT_STRUCTURAL / COUNTEREXAMPLE_FOUND`。

F. 给出 exact checker 与 census，主动寻找不同 \(r\) 之间看似相同但实际不等价、或看似不同但结构同构的例子。

G. 产出一份“可供全局拼接任务使用的最小局部接口”，但不得提前规定全局拓扑。

## Research value to preserve

这个任务的价值在于建立整个 Seed-6 计划的最小局部语法。若最小三角中只有交换律的重述，也要把这个负边界精确冻结；若存在稳定的 carrier-incidence 或 orientation 结构，则它将成为后续桥矩形和桥面的合法局部 building block。

## Success, kill, and return criteria

Success：对主样本族给出完整局部分类；至少一个非纯数值距离的局部结构接口被证明可复用，或证明不存在这样的非平凡接口；所有新术语都有 exact definition 和反例审计。

Kill：只罗列 \(6,10,15,14,21,\dots\) 而无结构分类；把交换律/结合律恒等式直接命名为新定理；把任务转向分解或搜索某个隐藏因子；以数值接近、大小差或加法邻居解释桥。

Return：task-terminal；允许 `SUCCESS / NEGATIVE_BOUNDARY / MIXED_CLASSIFICATION`；必须明确哪些观察只是恒等式，哪些结构值得进入下一层。
