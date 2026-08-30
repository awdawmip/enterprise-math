<!-- ENTERPRISE_MATH_TASK_V1
{
  "kind": "RESEARCH",
  "owner": "research/seed6-pairing-opposite-frame-axiom-cohomology",
  "base_state": "READY",
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "parent_objective_id": "OBJ-SEED6-MULTIPLICATIVE-GROWTH-GEOMETRY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-SEED6-RESONANCE-OPERATOR-CONNECTION-CANONICALITY",
  "claim_lease_minutes": 240,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "task_id": "RS-SEED6-PAIRING-OPPOSITE-FRAME-AXIOM-COHOMOLOGY",
  "title": "Seed-6 配对反向框架新公理：C2 联络的一致性与上同调分类",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Treat the exact residual marked-cell C2 frame bit as an explicit new support-faithful primitive PAIRING_OPPOSITE_FRAME_CONNECTION_V1 rather than pretending it is derivable from the frozen arithmetic carrier, and classify the resulting global consistency, gauge classes, resonance-loop degrees of freedom, relation to carrier-row C2 height parity, and the remaining S4/V4 atom-lift boundary.",
  "next_action": "Define PAIRING_OPPOSITE_FRAME_CONNECTION_V1 as one compatible marked-state-preserving C2 transition on each generating carrier-groupoid edge; classify existence and gauge equivalence on the support-typed carrier/resonance groupoid, identify the exact H1 or torsor parameter space, compare it with the intrinsic carrier-height mod-2 class, and determine what additional V4-breaking data are necessary for atom-level S4 transport.",
  "dependencies": [
    "research_returns/SEED6_RESONANCE_OPERATOR_CONNECTION_CANONICALITY_RETURN_20260830.md@main",
    "driver_reviews/SEED6_RESONANCE_OPERATOR_CONNECTION_CANONICALITY_DRIVER_REVIEW_20260830.md@main",
    "research_returns/SEED6_DECORATED_CARRIER_RESONANCE_GLOBAL_GEOMETRY_RETURN_20260830.md@main",
    "driver_reviews/SEED6_DECORATED_CARRIER_RESONANCE_GLOBAL_GEOMETRY_DRIVER_REVIEW_20260830.md@main"
  ],
  "evidence_status": "CANONICAL_S3_CONNECTION_NO_GO_DRIVER_ACCEPTED / RESIDUAL_C2_FRAME_BIT_EXPLICIT_NEW_AXIOM_OPEN",
  "tags": [
    "seed6",
    "new-axiom",
    "pairing-frame",
    "C2",
    "connection",
    "cohomology",
    "groupoid",
    "gauge",
    "S4",
    "V4",
    "positive-growth"
  ],
  "registry_key": "RS-SEED6-PAIRING-OPPOSITE-FRAME-AXIOM-COHOMOLOGY",
  "identity_lane": "S6POFAC",
  "successor_gate": {
    "new_information_gap": "The accepted operator-canonicality no-go proves that the frozen arithmetic/support interface leaves exactly one residual C2 frame bit on every cross-cell marked pairing transport. What is still unknown is whether explicitly promoting that missing bit to a new support-faithful primitive yields a coherent global theory, how many gauge-inequivalent choices exist, and whether any part of the new operator class is forced to coincide with the intrinsic carrier-row C2 height class.",
    "why_parent_result_does_not_close_it": "The parent result classifies non-derivability from the old interface, but deliberately does not add the missing relation. This task changes the interface explicitly: PAIRING_OPPOSITE_FRAME_CONNECTION_V1 is new axiom data, not an inferred theorem. Its global consistency and consequences are therefore a different mathematical question.",
    "discriminating_outcomes": [
      "prove that coherent marked-frame connections modulo vertex gauge are classified exactly by H1 of the support-typed carrier complex with C2 coefficients, and compute the resonance-loop degrees of freedom",
      "find a support-faithful composition or naturality constraint that collapses the apparent C2 freedom to the carrier-height parity class or another strict subset",
      "prove the candidate axiom is redundant, inconsistent, or introduces only arbitrary gauge degrees of freedom with no new invariant beyond standard flat C2 connection data"
    ],
    "kill_condition": "Do not claim the new C2 bit was derived from the frozen arithmetic carrier; do not globally name the two opposite pairing states by convention; do not erase support or row typing; do not choose an S4 lift by hand; do not treat standard H1, flat C2 connections, torsors or extension theory as external novelty; do not introduce factorization, additive-distance or performance semantics.",
    "alternative_route_or_free_exploration_considered": "Closing the parent objective at the no-go is logically possible, and repeating more canonicality searches on unchanged data would be invalid. The only narrow continuation justified here is an explicit minimal-axiom extension that makes the missing C2 bit first-class and tests its consequences. Broader new rectangles or larger censuses add no information.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The old task asked whether a connection is canonically derivable and answered no. This task no longer asks that question; it introduces exactly the relation type identified by the obstruction and classifies the extended theory. It is therefore a genuine interface change rather than a renamed continuation of the failed derivation route."
  }
}
-->
# Seed-6 配对反向框架新公理：C2 联络的一致性与上同调分类

## Mother question

前一阶段已经精确证明：现有 valuation/support/resonance 数据并不能自然决定跨 support cell 的 pairing-state transport。即使保留 Seed 标记的 carrier matching，每条合法跨 cell 边仍有两个 mark-preserving transport，构成没有固定点的 `C2` torsor。

本任务不再把这一个 bit 假装成“可以从旧数据推出来”。相反，显式加入最小新原语：

`PAIRING_OPPOSITE_FRAME_CONNECTION_V1`。

它在每个 support-typed carrier-groupoid 生成边上给出一个与 marked carrier state 相容的 `C2` transition，并满足逆与复合关系。问题是：这个新公理能否形成一致的全局结构？模掉 vertex-frame gauge 后还剩多少真实自由度？它与已经内禀存在的 carrier-row `C2` height/parity 类是什么关系？

## Frozen inputs and scope

1. 冻结并继承 operator-canonicality no-go：旧接口没有 canonical cross-support `S3` connection，残余歧义恰为 marked-cell `C2` torsor。
2. 冻结 `S4 -> S3` 为 split quotient，kernel 为 `V4`；四个 homomorphic sections 都存在，但旧接口不选择任何一个。
3. 冻结 support-faithful decorated resonance carrier complex 及其一般化 normal form；不通过 scalarization 制造共享端点或额外拓扑。
4. `PAIRING_OPPOSITE_FRAME_CONNECTION_V1` 是本任务明确新增的候选公理数据，不得倒写成旧结果的推论。
5. 允许使用有限群作用、groupoid connection、`C2` 上同调、cellular cochain 与 gauge equivalence 等标准工具。
6. 不引入 factor recovery、factorization performance、additive distance、Fermat/square-shell 或 smooth-curvature 目标。
7. 本任务默认只研究 marked-pairing `C2` 层；只有在该层被完整分类后，才讨论 atom-level `S4/V4` lift boundary。

## Hard target and required outputs

Hard target:

`PAIRING_OPPOSITE_FRAME_CONNECTION_V1_GLOBAL_CONSISTENCY_AND_COHOMOLOGY_CLASSIFIED`

Required outputs:

A. 给出 `PAIRING_OPPOSITE_FRAME_CONNECTION_V1` 的精确定义，包括：对象、生成边、`C2` transition、inverse law、composition law、vertex-frame gauge action。

B. 对有限 support-typed carrier/resonance groupoid，精确分类 connection 的存在性与 gauge 等价类。若分类等于某个 `H^1(-;C2)` 或 affine torsor，必须证明，而不是只类比。

C. 在一般 decorated carrier `Sigma=(a,b)` 与有限 bundle set `R` 上，计算 clean backbone 与每个合法 resonance pinch 对 operator connection 自由度的贡献；区分“边上的选择数”和“规范不变量维数”。

D. 比较新 operator class 与既有 carrier-height mod-2 class：证明二者必然相同、可以独立、形成 affine translate，或给出其它精确关系。不得因为二者都取值于 `C2` 就默认等同。

E. 审计是否存在合理的 support-faithful flatness/naturality 条件会把自由度压缩到更小子空间；若没有，给出 no-go。

F. 仅在 `C2` 层完成后，给出 atom-level lift 的边界：要得到 `S4` transport 还缺哪些 `V4`-breaking 数据；不得任意选择 section。

G. 提供独立 exact checker，至少覆盖多个 decorated strata、无 resonance、单 resonance、多 resonance、equality degeneration，以及 gauge-equivalence/holonomy 计数。

## Research value to preserve

1. 把上一阶段发现的“缺一比特”从模糊缺陷变成可检验的新公理候选，而不是偷偷选 gauge。
2. 明确区分内禀 carrier-row `C2` 与新增 pairing-frame `C2`，防止因为群同构就错误合并两个物理/算术角色。
3. 如果新公理只产生标准 `H^1` 自由度，也要把这个负边界精确冻结；如果存在额外自然约束，则只接受 support-faithful 且 equivariant 的约束。
4. 保留 `V4` lift ambiguity，直到有独立 atom-frame 数据真正打破它。
5. 为“寻找新公理”建立最小、可反驳、可复核的接口，而不是无限扩大 Seed-6 图形枚举。

## Success, kill, and return criteria

SUCCESS 可以是正结论或 no-go，但必须完成以下至少一种闭合：

- 完整证明 gauge classes 的精确分类与维数/计数，并给出 carrier-height 类之间的关系；或
- 证明候选新公理在 frozen support/groupoid composition 下不一致或完全冗余；或
- 证明某个额外且独立有动机的 support-faithful relation 唯一压缩连接空间，并给出 exact witness/checker。

必须返回而不能伪装成功的情形：

- 只是给每条边任意选择 0/1，没有做 gauge/复合分类；
- 把新公理说成旧 arithmetic data 的推论；
- 用 `M1/M2` 全局命名或 magnitude order 偷偷定 orientation；
- 抹去 support/row provenance 后制造新的 holonomy；
- 任意选一个 `S4` section 再把得到的 `V4` residue 称作内禀不变量；
- 把标准群上同调结果包装成历史创新。
