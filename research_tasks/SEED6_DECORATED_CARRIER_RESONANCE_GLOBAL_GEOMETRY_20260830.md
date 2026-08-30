<!-- ENTERPRISE_MATH_TASK_V1
{
  "kind": "RESEARCH",
  "owner": "research/seed6-decorated-carrier-resonance-global-geometry",
  "base_state": "READY",
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "parent_objective_id": "OBJ-SEED6-MULTIPLICATIVE-GROWTH-GEOMETRY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-SEED6-DEGENERATE-STRATA-GLOBAL-GLUING",
  "claim_lease_minutes": 240,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "task_id": "RS-SEED6-DECORATED-CARRIER-RESONANCE-GLOBAL-GEOMETRY",
  "title": "装饰载体对的共振拼接：一般化 pinch、分层拓扑与 carrier-height holonomy",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Generalize the accepted support-retaining 3:2 Seed-6 resonance pinch from fixed carrier rows (2,3) to an arbitrary decorated carrier pair Sigma=(a,b), using the complete primewise valuation profile and canonical core/excess coordinates, and classify the exact cross-row resonance locus, support-faithful global normal form, homology and carrier-row holonomy without introducing factorization or additive-distance semantics.",
  "next_action": "For d=gcd(a,b), a=dA, b=dB with gcd(A,B)=1, classify all exact cross-row collisions in rectangles [[ar,as],[br,bs]], prove or refute the primitive resonance parametrizations br=as and ar=bs, build the support-retaining stratified CW complex across multiple bundle objects, and determine exactly when each legal collision contributes a pinch loop and nonexact carrier-height class.",
  "dependencies": [
    "research_returns/SEED6_DECORATED_CARRIER_PAIR_STRATIFIED_GROWTH_RETURN_20260830.md@main",
    "driver_reviews/SEED6_DECORATED_CARRIER_AND_DEGENERATE_GLOBAL_GLUE_DRIVER_REVIEW_20260830.md@main",
    "research_returns/SEED6_DEGENERATE_STRATA_GLOBAL_GLUING_MANIFEST_REFREEZE_RETURN_20260830.md@main",
    "driver_reviews/SEED6_DEGENERATE_GLOBAL_GLUING_REFREEZE_V2_DRIVER_REVIEW_20260830.md@main"
  ],
  "evidence_status": "DECORATED_CARRIER_ATLAS_DRIVER_ACCEPTED / FIXED_2_3_RESONANCE_PINCH_DRIVER_ACCEPTED / GENERAL_DECORATED_RESONANCE_OPEN",
  "tags": [
    "seed6",
    "decorated-carrier",
    "valuation-profile",
    "resonance",
    "stratified-gluing",
    "pinch",
    "homology",
    "carrier-height",
    "holonomy",
    "positive-growth"
  ],
  "registry_key": "RS-SEED6-DECORATED-CARRIER-RESONANCE-GLOBAL-GEOMETRY",
  "identity_lane": "S6DCRG",
  "successor_gate": {
    "new_information_gap": "The fixed carrier pair (2,3) has an accepted support-retaining 3:2 resonance pinch with extra H1 and a carrier-row C2 holonomy, while the decorated-carrier atlas proves the true local state is the full valuation profile of (a,b). What remains unknown is the exact resonance law and global topology when both facts are combined for arbitrary decorated carriers.",
    "why_parent_result_does_not_close_it": "The accepted fixed-row gluing theorem only treats cross-row equality 3r=2s. The decorated-carrier atlas classifies local valuations but does not determine which non-fresh outer bundle collisions are operation-safe globally, nor whether the fixed-row wedge-of-circles normal form survives.",
    "discriminating_outcomes": [
      "prove an exact decorated resonance classification, for example via the reduced carrier pair (A,B), and obtain a support-faithful global normal form with explicit homology and carrier-height cohomology",
      "find decorated overlap/rank strata where legal collisions interact and the fixed-row one-pinch-one-circle rule fails",
      "prove that after full support typing all apparent generalized resonances reduce to standard point identifications with no additional invariant beyond the fixed-row mechanism"
    ],
    "kill_condition": "Do not assume r,s are fresh when the resonance equations force seed-support reuse; do not glue merely equal numerical values across unrelated supports; do not erase valuation/support ports to manufacture topology; do not infer a canonical global S3 connection or S4 lift; do not convert the result into a factorization target or additive-distance geometry.",
    "alternative_route_or_free_exploration_considered": "Larger Seed-6 censuses and arbitrary new rectangles would repeat already-classified standard matching/product structure. The only justified positive continuation is to combine the accepted decorated-carrier state with the accepted resonance-pinch mechanism.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The integrity revision is terminal and contains no new mathematics. A separate continuation is needed because the obligation now changes from repairing evidence for the fixed (2,3) theorem to classifying a genuinely broader decorated-carrier mechanism."
  }
}
-->
# 装饰载体对的共振拼接：一般化 pinch、分层拓扑与 carrier-height holonomy

## Mother question

前一阶段已经分别冻结了两个事实：

1. 正向乘法局部状态不能只写成标量种子，而应至少保留装饰载体对
   \[
   \Sigma=(a,b)
   \]
   的完整 primewise valuation profile；
2. 对固定载体行 \((2,3)\)，精确交叉行共振
   \[
   3r=2s
   \]
   在保留 support port 的条件下产生真实 pinch loop、额外 \(H_1\) 与非平凡 carrier-height 类。

本任务只问二者结合以后发生什么。令
\[
d=\gcd(a,b),\qquad a=dA,\qquad b=dB,\qquad \gcd(A,B)=1.
\]
对外层 bundle objects \(r,s\)，研究矩形
\[
\begin{pmatrix}
ar&as\\
br&bs
\end{pmatrix}.
\]

核心问题是：

\[
\boxed{\text{一般 }(a,b)\text{ 下，哪些精确 cross-row collisions 是真正 support-safe resonance？}}
\]

以及这些 resonance 在多胞拼接后是否仍遵循“一次合法 pinch 增加一个 \(S^1\) 与一个 carrier-height period”的规律。

## Frozen inputs and scope

1. 接受的 decorated-carrier 局部状态为完整 valuation profile；不得退回只用 \(ab\)、\(\gcd(a,b)\) 或 \(\Delta_T\) 表示全部状态。
2. 接受
   \[
   (a,b)\leftrightarrow(d;A,B),\quad \gcd(A,B)=1
   \]
   作为 lossless core/excess 坐标。
3. 接受固定 \((2,3)\) 的 support-retaining resonance-pinch 结果：
   \[
   X_{\rm str}(R)\simeq K_R\vee\bigvee^{m(R)}S^1,\qquad H_2=0,
   \]
   以及相应 carrier-height cocycle / mod-2 row holonomy。
4. 不得假设 resonance 中的 \(r,s\) 对 \(ab\) 是 fresh；若方程强制 seed-support reuse，必须显式保留并分类。
5. 只允许 local accepted collision partition 或精确 support-typed attaching rule 产生几何识别；数值相等本身不是全局 gluing 权限。
6. pairing-state \(S_3\) transport 与 atom-level \(S_4\) lift 仍未自然给出；不得选择 gauge 后宣称 intrinsic。
7. 禁止 additive distance、Fermat/square-shell locality、factor recovery、factorization performance、smooth curvature 或 manifold 解释。
8. 有限 census 只能做 regression / falsification，核心结论必须来自 exact symbolic classification。

## Hard target and required outputs

Hard target:

`DECORATED_CARRIER_RESONANCE_STRATIFIED_GLOBAL_GEOMETRY_CLASSIFIED`

A. **Exact resonance locus.**
完整分类矩形四位置之间所有 cross-row equality，至少处理
\[
br=as,\qquad ar=bs.
\]
利用 \(a=dA,b=dB,\gcd(A,B)=1\) 给出必要充分条件与 primitive parametrization；明确何时两种方向重合、冲突或退化。

B. **Support-faithful local singular cell.**
对每一种合法 resonance，定义保留：
- carrier row；
- exact bundle/support port；
- valuation decoration；
- edge/face germ；
的局部 pinched cell。证明哪些识别 operation-safe，哪些只是 value-only quotient。

C. **Global normal form.**
对有限 decorated bundle family，构造 stratified CW complex，计算
\[
H_0,\ H_1,\ H_2
\]
并证明正常形。重点检验但不得预设：
\[
\text{one legal independent pinch}\stackrel{?}{\longmapsto}\text{one new }S^1.
\]
若 resonance identifications 发生链式、共享 port 或非独立关系，必须给出修正公式。

D. **Carrier-height cohomology.**
定义一般 \((a,b)\) 两载体行的 height / row cocycle，判断：
- clean region 是否 exact；
- resonance 后何时 nonexact；
- period 是否总为 \(\pm1\) 或受 \(A,B\)、valuation thickness 影响；
- mod-2 row holonomy 是否仍为 intrinsic。

E. **Interaction with decorated strata.**
至少覆盖：
- coprime prime-pair；
- coprime thick；
- coprime multisupport；
- O1 common-base rank-1 overlap；
- O2 rank-2 overlap；
- equality。
判断哪些 stratum 只做 decoration，哪些会改变合法 resonance graph 或 global topology。

F. **Operator boundary.**
审计 resonance path 是否自然诱导 pairing-state \(S_3\) connection。若没有，给出 no-canonical-connection 边界；若提出 lift，必须消除 \(V_4\) ambiguity，而不是选一个 lift。

G. **Exact checker.**
建立独立 exact-integer checker，覆盖：
- symbolic resonance iff 条件；
- 多种 carrier strata；
- mixed resonance chains；
- support-safe vs unsafe quotient controls；
- homology / cocycle 公式。
主动寻找 fixed-\((2,3)\) normal form 的反例。

## Research value to preserve

本任务要保留的价值不是“把 3:2 换成别的比例”这么简单，而是判断：

\[
\boxed{
\text{valuation-decorated carrier state}
+
\text{exact cross-row resonance}
\Longrightarrow
\text{什么真正的全局乘法几何？}
}
\]

若一般 resonance 仍然只产生标准 point-identification wedge loops，也要精确证明并冻结；若 O1/O2 等 decorated strata 让 pinch 发生耦合，则必须把这种耦合与 support-erasure 伪拓扑分开。

Seed-6 保持参考坐标，但不得预设 \((2,3)\) 的现象在一般 \((a,b)\) 下必然特殊或必然泛化。

## Success, kill, and return criteria

SUCCESS：
- exact resonance locus 完成必要充分分类；
- support-safe local singular model 明确；
- global homology/normal form 有证明；
- carrier-height class 有 exact 判定；
- decorated strata interaction 完成；
- checker 主动反例搜索通过。

NEGATIVE BOUNDARY 也可成功：
- 若证明一般 decorated resonance 全部归约为标准 point-identification topology，且没有新的 valuation-sensitive global invariant，则按精确强度冻结。

RETURN / REVISION：
- 把数值相等直接当 support identity；
- 为得到非平凡 \(H_2\) 而跨 support 过度 gluing；
- 假设 freshness 导致漏掉 resonance 主族；
- 把选定的 \(S_3/S_4\) lift 当 intrinsic；
- 只做大 census 而没有 exact iff theorem；
- 将结果改写成分解算法或距离几何。
