<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-MULTIPLICATIVE-NATIVE-SEPARATION-GEOMETRY",
  "title": "乘法原生分离几何：互素纤维、无限分离与桥操作公理化",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "The current factor-edit geometry still measures multiplicative change by an L1-style add/remove token count. Replace additive locality as the primitive notion: define a carrier-preserving multiplicative state space in which disjoint prime-support sectors have no native path unless an explicit support-changing bridge operation is admitted, and determine exactly which operation alphabets make this statement true rather than tautological.",
  "next_action": "Define support-tagged states and the native multiplication/division operation alphabet before defining any distance. Prove or refute disconnectedness for disjoint support under that alphabet, then classify the weakest support-changing operations that create overlap and replace scalar distance by bridge type/rank/depth invariants.",
  "dependencies": [
    "research_result_records/RS-MULTIPLICATIVE-ADJACENCY-NUMBER-AXIS/RR-C28C28A7C8EF8B9C96F6.json@b74c886f5abc78e2a4da5985932f49063bf15b24"
  ],
  "source_refs": [
    "research_returns/MULTIPLICATIVE_ADJACENCY_NUMBER_AXIS_RETURN_20260829.md@b74c886f5abc78e2a4da5985932f49063bf15b24"
  ],
  "evidence_status": "DIRECT_USER_DIRECTION / NEW_MULTIPLICATIVE_GEOMETRY / ADDITIVE_LOCALITY_REJECTED_AS_PRIMITIVE",
  "hard_block": null,
  "tags": ["multiplicative-geometry", "coprime", "prime-support", "fiber", "carrier", "bridge", "gcd", "divisibility", "groupoid", "no-go"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-MULTIPLICATIVE-NATIVE-SEPARATION-GEOMETRY",
  "parent_objective_id": "OBJ-MULTIPLICATIVE-BRIDGE-GEOMETRY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "MBG-G0",
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

# 乘法原生分离几何：互素纤维、无限分离与桥操作公理化

Status: `READY / P1 / HIGH-LEVERAGE / STRUCTURE-FIRST`

## Mother question

若问题本身是乘除结构，是否应取消普通数轴或因子 token 的“加减距离”作为第一性几何，而把没有共同乘法 carrier 的状态视为原生断连？

需要把

\[
\gcd(m,n)=1 \Longrightarrow \text{native separation}
\]

写成依赖**明确操作字母表**的精确定理，而不是把“无限远”直接规定进定义。研究核心是区分 carrier-preserving native motion、首次改变 prime support 的 bridge，以及 bridge 的类型、秩、深度，而不是再造一个标量距离。

## Frozen inputs and scope

1. 以 \(\operatorname{supp}(n)=\{p:v_p(n)>0\}\) 和必要的 support-tagged / carrier-tagged state 为基本对象候选。
2. 必须先定义原生乘法/除法操作再讨论连通性。若允许任意乘入新质因子，则互素断连不成立；这种 support expansion 必须被识别为 bridge 候选，不能偷算 native motion。
3. 不得以 \(|m-n|\)、\(\sqrt n-m\)、Fermat offset、相邻整数间隔或 factor-edit L1 长度作为主几何、不变量或优化目标。
4. 加减可作为代数表达、同余等式或反例构造出现；禁止的是把它们重新包装成局部性或距离。
5. 允许 gcd、整除、商、prime support、自由交换幺半群、局部化、群胚、CRT、零因子与 support lattice。
6. “纯 ×/÷ 无法拆分隐藏 support”必须有精确假设，不得从极窄语法泛化成所有乘法算法不可能。
7. 本任务不要求提出分解算法。

## Hard target and required outputs

**G0 Native state model.** 给出可审计的 state/object 与 carrier-preserving morphism 定义，并解释普通整数投影为何会忘记 carrier。

**G1 Separation theorem or counterexample.** 对选定 native alphabet，证明 disjoint support 时没有 native path；若不成立，给出最小反例并修正操作分类。

**G2 Pure-operation closure boundary.** 精确刻画 multiplication/inversion/division closure 在什么条件下无法产生只属于某一隐藏 prime channel 的非平凡零因子或 endpoint witness。

**G3 Bridge axioms.** 至少提出并比较三种非标量 bridge complexity，例如 support-change rank、carrier coupling arity、first-collapse depth；允许它们不是 metric。

**G4 Minimal bridge classes.** 分类 support expansion、quotient/projection、congruence singularization、zero-divisor extraction、balanced coupling，指出哪些只是记号变化，哪些真正跨越 native sectors。

**G5 Regression examples.** 对 prime powers、共享一个质因子的半素数、互素半素数、平方因子数给出手算与 exact checker 例子。

Required outputs:

- `research_returns/MULTIPLICATIVE_NATIVE_SEPARATION_GEOMETRY_RETURN_20260829.md`
- 一个 exact-integer checker 或形式化伪代码；
- 明确列出 `THEOREM / DEFINITION / MODELING_CHOICE / COUNTEREXAMPLE`，不得混写。

## Research value to preserve

这项工作决定“乘法数空间”是否真的需要一条数轴。若原生对象天然是多个 carrier fibers 加显式 bridge，后续 BRC、CRT 与分解研究就应围绕“如何跨 sector”组织，而不再围绕加法邻近或 token-edit 长度组织。若严格操作语义下无法维持互素断连，也应尽早冻结反例。

## Success, kill, and return criteria

**SUCCESS**：得到非循环定义的 native separation theorem、最小 bridge taxonomy，并清楚标出适用操作类。

**PARTIAL**：某一自然 alphabet 下断连成立、另一自然 alphabet 下不成立；返回 operation-sensitive classification。

**NEGATIVE_BOUNDARY**：证明“互素默认无限分离”无法在合理且不预先锁死 support 的 native alphabet 中成立。

**KILL**：仅把互素定义成距离无穷；通过禁止一切 support-changing 操作循环证明断连；偷用加法邻近作为 bridge quality；从窄语法 no-go 跳到全部 factor-blind 算法 no-go。

Return 必须明确下一步是否值得研究 BRC bridge；不得自动宣称存在新分解算法。
