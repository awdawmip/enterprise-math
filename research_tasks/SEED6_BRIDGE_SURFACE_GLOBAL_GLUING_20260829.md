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
  "task_id": "RS-SEED6-BRIDGE-SURFACE-GLOBAL-GLUING",
  "title": "Seed-6 乘法桥面：列族、矩形胞拼接、环路与全局拓扑",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "The seed-6 column family C_r=(2r,3r) generates a bridge rectangle for every pair of distinct primes p,q>3. Determine the exact global incidence/topology obtained when many columns and pairing cells are glued together, rather than studying each identity in isolation.",
  "next_action": "For the first k primes r>3, build finite column/rectangle/pairing-cell complexes under several explicit gluing conventions, derive exact counts and connectedness/cycle formulas, and test whether nontrivial loop, holonomy-like, or local-to-global invariants survive after quotienting tautological rank-one structure.",
  "dependencies": [],
  "source_refs": [],
  "evidence_status": "DIRECT_USER_DIRECTION / LOCAL_TO_GLOBAL_POSITIVE_GEOMETRY / NO_ALGORITHMIC_TARGET",
  "tags": ["seed6", "bridge-surface", "cell-complex", "gluing", "cycle", "holonomy", "global-geometry"],
  "registry_key": "RS-SEED6-BRIDGE-SURFACE-GLOBAL-GLUING",
  "identity_lane": "S6G"
}
-->

# Seed-6 乘法桥面：列族、矩形胞拼接、环路与全局拓扑

## Mother question

对每个素数 \(r>3\)，定义一列 \(C_r=(2r,3r)\)。任取两列 \(C_p,C_q\)，得到矩形数据

\[
\begin{pmatrix}2p&2q\\3p&3q\end{pmatrix},\qquad (2p)(3q)=(2q)(3p).
\]

当很多列同时存在时，所有两列都会闭合一个局部矩形。研究问题是：这些局部胞如何拼成一个全局乘法桥面？重点是 incidence、cycle、boundary、gluing consistency 与可能的 holonomy-like 量，而不是数值大小。

## Frozen inputs and scope

1. 固定 Seed-6 两行结构 \(2r,3r\)，主索引集先取前 \(k\) 个 \(r>3\) 素数。
2. 至少比较三种全局模型：仅列顶点 + 两列矩形；加入 \(6\) 与 \(pq\) pairing vertices；以三配对胞为 2-cell 的 matching complex。
3. 每个模型必须给精确等价关系，禁止为了得到漂亮拓扑任意粘点。
4. 标准 rank-one 外积恒等式要显式剥离；若所有结构都由 \((2,3)^T(p,q)\) 的 rank-one 性完全解释，必须如实冻结。
5. 禁止因子搜索、分解、端点、复杂度收益。
6. 允许图论、胞复形、simplicial/CW-like 模型、群作用、同调的有限计算，但不得先选经典目标再倒推结构。

## Hard target and required outputs

Hard target: `SEED6_BRIDGE_SURFACE_GLOBAL_GLUE_CLASSIFIED`

A. 对每个候选全局模型给出 \(V,E,F\) 或相应 incidence 数据的 exact formula，至少做到有限 \(k\) 的闭式计数或递推。

B. 分类 connected components、cycle rank、边界、每条边/顶点参与多少局部胞。

C. 研究三个不同列 \(p,q,r\) 形成的闭环 \(C_p\leftrightarrow C_q\leftrightarrow C_r\leftrightarrow C_p\)。定义并测试可能的 composition/transport/holonomy-like 量；若所有环路必然平凡，给出证明。

D. 检查局部 pairing switch 的不同组合是否存在 path dependence，还是只取决于最终 matching。

E. 寻找最小非平凡 2-cycle / 3-cycle / higher cell，并给 exact examples，例如从 \(5,7,11,13\) 开始。

F. 至少对 \(k=3,\dots,50\) 做 exact census，生成机器可读 incidence summary；图形展示可选，但结论必须由整数/组合证书支撑。

G. 给出“桥面”一词的最小合法定义：若二维结构只是视觉隐喻而无非平凡 gluing invariant，应明确降格为图/匹配复形。

## Research value to preserve

局部恒等式是否能成长为真正的几何，关键在全局拼接。这个任务专门防止把每个矩形单独看起来很漂亮就误判为新几何；只有局部胞之间产生一致且可复核的全局结构时，“乘法桥面”才有实质内容。

## Success, kill, and return criteria

Success：至少一个全局模型被完整分类；有非平凡局部到全局规律，或证明合理模型全部退化到标准组合对象；cycle / gluing / path dependence 有明确 verdict。

Kill：只画图不定义 quotient/incidence；用视觉对称代替 exact combinatorics；把 rank-one 恒等式重复计数为不同规律；转向分解大整数。

Return：task-terminal；可返回 `NONTRIVIAL_GLOBAL_GEOMETRY / STANDARD_CELL_COMPLEX_REIDENTIFIED / GLOBAL_FLATNESS_PROVED / MODEL_DEPENDENT_BOUNDARY`。
