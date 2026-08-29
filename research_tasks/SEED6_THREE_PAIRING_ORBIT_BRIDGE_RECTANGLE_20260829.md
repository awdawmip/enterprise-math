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
  "task_id": "RS-SEED6-THREE-PAIRING-ORBIT-BRIDGE-RECTANGLE",
  "title": "Seed-6 四原子三配对轨道：桥矩形、重配对动作与守恒结构",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "For four distinct prime atoms {2,3,p,q} with p,q>3, the three perfect pairings {6,pq}, {2p,3q}, {2q,3p} share total product 6pq. Classify this three-state pairing orbit and its local re-pairing moves as a multiplicative object without interpreting it as a factorization device.",
  "next_action": "Define ordered and unordered pairing states, enumerate all local swaps induced by permutations of the four atoms, determine the exact orbit/action/quotient structure, and identify which bridge-rectangle identities carry information beyond the common product invariant.",
  "dependencies": [],
  "source_refs": [],
  "evidence_status": "DIRECT_USER_DIRECTION / POSITIVE_REPAIRING_DYNAMICS / DISTINCT_PRIME_ATOMS / NO_ENDPOINT_TARGET",
  "tags": ["seed6", "pairing-orbit", "bridge-rectangle", "re-pairing", "BRC", "conservation"],
  "registry_key": "RS-SEED6-THREE-PAIRING-ORBIT-BRIDGE-RECTANGLE",
  "identity_lane": "S6P"
}
-->

# Seed-6 四原子三配对轨道：桥矩形、重配对动作与守恒结构

## Mother question

取互异素数 \(p,q>3\)。四个乘法原子 \(\{2,3,p,q\}\) 有三个无序完全配对状态：

\[
P_0=\{6,pq\},\qquad P_1=\{2p,3q\},\qquad P_2=\{2q,3p\}.
\]

并且

\[
(6)(pq)=(2p)(3q)=(2q)(3p)=6pq.
\]

本任务研究固定乘法内容时，三种重配对状态本身形成什么轨道与局部动力学。BRC 在本任务中只允许解释为 `balanced re-pairing / coupling` 的候选局部语言，不允许解释成分解算法。

## Frozen inputs and scope

1. 主体固定为 \(\{2,3,p,q\}\)，其中 \(p,q>3\) 为互异素数。
2. 允许把配对看作 perfect matching、分割、无序二元组或带方向的 matching，但必须明确各模型的等价关系。
3. 固定总乘积 \(6pq\) 是基本守恒量；必须寻找它之外的结构或证明无更多结构。
4. 桥矩形
   \[
   \begin{pmatrix}2p&2q\\3p&3q\end{pmatrix},\qquad (2p)(3q)=(2q)(3p)
   \]
   是观察对象，不预设其几何解释。
5. 禁止数值距离、因子恢复、hidden-channel endpoint、分解收益。
6. 主动比较 ordered/unordered、labeled/unlabeled 版本，防止把标签本身误当结构。

## Hard target and required outputs

Hard target: `SEED6_THREE_PAIRING_ORBIT_EXACTLY_CLASSIFIED`

A. 完整列出四原子的三种 perfect matching，并证明没有第四种无序完全配对。

B. 定义最小重配对生成元：交换两个原子的归属、对角线翻转或 matching switch；说明哪些动作在无序配对商上不同。

C. 精确分类 \(S_4\) 对三配对集合的作用：kernel、image、orbit、stabilizer，以及是否自然得到 \(S_3\)、Klein 四元结构或其他等价描述。不得把标准群论事实本身当作新颖性主张。

D. 定义桥矩形与三配对轨道的对应关系，回答一个矩形对应一个还是两个 pairing switch、矩形 orientation 是否增加信息、\(P_0,P_1,P_2\) 组成三角还是别的最小胞更自然。

E. 搜索除总乘积外的 exact invariants：carrier intersection pattern、gcd multiset、valuation support、matching parity/orientation、局部 incidence 等。

F. 对前 300 对 \((p,q)\) 做 exact regression，检查配对结构是否真的与数值大小无关，以及哪些额外标签会破坏同构。

G. 输出一个不涉及分解语义的 `PAIRING_CELL_V1` 候选定义或精确否定理由。

## Research value to preserve

这个任务直接检验“桥不是数之间的路径，而是固定乘法内容下的重新配对”是否能成为一个独立数学对象。即使最后发现三状态轨道完全等价于标准 perfect-matching 作用，也能把 BRC 的局部核心从含混比喻压缩成精确 combinatorial carrier。

## Success, kill, and return criteria

Success：三配对轨道及其动作精确分类；bridge rectangle 与 pairing cell 的关系无歧义；明确区分标准匹配组合学与 Seed-6 特有标记。

Kill：用“balanced”一词代替定义；仅重复三个乘积相等；把配对态偷偷解释成待分解因子的候选；把 \(|P_i-P_j|\) 或任何数值差当作轨道几何。

Return：task-terminal；可返回 `EXACT_CELL_CLASSIFIED / STANDARD_OBJECT_REIDENTIFIED / NONTRIVIAL_SEED6_DECORATION_FOUND / NEGATIVE_BOUNDARY`。
