<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "title": "P000 S4 等变 PF10/connection 模空间与共同非平凡模型 V19",
  "kind": "RESEARCH",
  "owner": "research/p000-l1-native-carrier-contact-bridge",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "foundation_level": "P000_ROOT_AXIOM_BOUND",
  "p000_required": true,
  "frontier": "Classify the moduli and gauge/holonomy classes of nonconstant S4-equivariant PF10 families and independent connections on the accepted K4/tetra structural models, and construct one common non-degenerate enriched Full-Cell S4 model or prove the exact obstruction.",
  "next_action": "Use Gen18 full-lift-fiber verification only as a gate checker; enumerate stabilizer-orbit PF10 parameters; classify K4 independent connection values satisfying S4 equivariance, reverse-edge law and gauge equivalence; compute holonomy classes; then combine a nonconstant PF10 profile and nonidentity/nonflat connection in one common model and recheck enriched a^3,b^2,(ab)^4 relations.",
  "dependencies": ["research_returns/P000_LOCAL_TO_GLOBAL_BACKGROUND_EQUIVARIANCE_V18_RETURN_20260831.md@main","driver_reviews/P000_LOCAL_TO_GLOBAL_BACKGROUND_EQUIVARIANCE_V18_DRIVER_REVIEW_20260831.md@main","research_returns/P000_BACKGROUND_S4_EQUIVARIANCE_GATE_V17_RETURN_20260830.md@main"],
  "evidence_status": "GEN18_LOCAL_TO_GLOBAL_GENERATOR_FIBER_CRITERION_DRIVER_ACCEPTED / NONTRIVIAL_EQUIVARIANT_MODULI_AND_COMMON_MODEL_OPEN",
  "hard_block": null,
  "tags": ["P000","native-6D","S4","PF10","connection","holonomy","equivariance","moduli","nonflat","gauge"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000FCC19",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "REVISION",
  "parent_task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE"
}
-->

# P000 `S4` 等变 PF-10 / connection 模空间与共同非平凡模型 V19

Status: `READY / GENERATION-19 / P0 / P000-BOUND / MODULI-AND-COMMON-MODEL`

## Mother problem

Gen17 已给出两个 independently charged semantic transparency gates；Gen18 又证明它们可以用 frozen carrier generators `a,b` 的**完整 lift fibers**做有限 local-to-global 验证，并构造了一个 nonflat-but-fully-equivariant connection 正例。

因此当前问题不再是“gate 是否存在/是否可有限检查”，而是：

\[
\boxed{\text{这些透明 gate 下究竟有多丰富的非平凡 Full-Cell 内容？}}
\]

## Hard target

`P000_S4_EQUIVARIANT_PF10_CONNECTION_MODULI_AND_COMMON_NONDEGENERATE_MODEL_EXACTLY_CLASSIFIED`

## A. Freeze prior boundaries

不得修改：

- P000 root ontology；
- G15 grammar；
- Gen17 `PF10_STRUCTURAL_AUT_EQ` / `CONNECTION_STRUCTURAL_AUT_EQ` 的 semantic count/cost；
- Gen18 full-lift-fiber verification criterion；
- `NO_KERNEL_QUOTIENT`；
- `CARRIER_S4 != COMPLETE_NATIVE_P000_ROTATION_GROUP`；
- `TIME_FIXED`。

禁止把 chosen one-pair lift criterion 偷换成 full transparency。

## B. PF-10 equivariant moduli

在 K4/tetra Cell orbit 上：

1. 精确给出 base Cell stabilizer 在 6 channel 上的 orbit partition；
2. 分类 `I`、`O` 全部 stabilizer-fixed参数；
3. 分类 ordered channel-pair 上 `M` 的全部 stabilizer orbits；
4. 从 representative Cell profile 通过 structural transport 重建完整 global equivariant family；
5. 证明该参数化完备且无重复，或给出 gauge quotient 后的完备版本；
6. 给出至少一个 raw Cell-to-Cell 非恒定、但 native-equivariant 的 PF-10 family。

至少回归：full local `S4` vector orbits=1 / ordered-pair orbits=3；base tetra Cell stabilizer vector orbits=2 / ordered-pair orbits=8。

## C. Connection value universe and local constraints

当 independent connection 被声明时，必须明确 transport 的 typed finite universe（例如 channel bijections/permutations；不得默认为 `SO(6)`）。

选择一个 oriented K4 edge 作为 representative，分类：

- oriented-edge stabilizer condition；
- reverse-edge law `T_yx=T_xy^-1`；
- full-lift-fiber `a,b` naturality；
- gauge transformation law。

证明这些条件如何生成全部 global equivariant connection。

## D. Connection moduli / gauge quotient

在冻结 transport universe 下：

1. 枚举或结构分类全部 `CONNECTION_STRUCTURAL_AUT_EQ` 解；
2. quotient by accepted gauge equivalence；
3. 给出各 gauge class 的 representative；
4. 统计 identity vs nonidentity；
5. 若 finite，给出 exact counts；若参数族，给出 exact parameterization。

不得把 gauge bit 计成新 native spatial axis。

## E. Holonomy classification

对每个 connection gauge class：

- 计算 K4 triangle/cycle basis holonomy；
- 按 conjugacy class 分类；
- 区分 flat / nonflat；
- 检查 `S4` holonomy conjugacy law。

Gen18 的 edge-to-opposite transposition connection 必须作为 mandatory nonflat-equivariant regression。

## F. Common non-degenerate model

必须在**同一个** Full-Cell model 中同时实现：

- 非恒定 equivariant PF-10 family；
- nonidentity independent connection；
- 优先 nonflat connection；
- Gen17 charged gates；
- accepted `R_a,R_b` structural action。

然后在完整 enriched data 上检查：

\[
R_a^3=R_b^2=(R_aR_b)^4=id.
\]

若无法共存，必须给 exact compatibility obstruction；不允许分别造两个 witness 后拼接。

## G. Degeneracy test

必须回答：

- transparency gates 是否迫使 PF10 退化为 pointwise constant？
- transparency gates 是否迫使 independent connection gauge-equivalent to identity？
- nonflat equivariant connection 是否只是单一偶然 witness，还是属于非平凡 family？

这些问题必须用 exact theorem/certificate 回答。

## H. Deterministic checker

至少验证：

- S4 / Cell stabilizer / oriented-edge stabilizer exact enumeration；
- PF10 orbit parameterization；
- global reconstruction；
- connection reverse-edge + generator-fiber naturality；
- gauge-orbit enumeration；
- triangle/cycle holonomy；
- nonconstant PF10 common-model witness；
- enriched generator relations；
- Gen17/18 regressions and guards。

## Valid terminal classes

- `NONTRIVIAL_PF10_AND_NONFLAT_CONNECTION_MODULI_COMMON_MODEL_CLASSIFIED`；
- `NONTRIVIAL_PF10_AND_ONLY_FLAT_CONNECTION_MODULI_CLASSIFIED`；
- `PF10_MODULI_CLASSIFIED_CONNECTION_COMMON_MODEL_EXACTLY_OBSTRUCTED`；
- `TRANSPARENCY_GATES_FORCE_DEGENERATE_CONTENT_EXACTLY_PROVED`。

## Concurrency reconciliation

A later concurrent Generation-18 draft publication `TP2-D4A7C19E5B306F821472` is noncanonical. Its useful moduli question is absorbed here at Generation 19; scheduler/researchers must follow this publication and not claim the duplicate Gen18.

External prior-art lane remains separate and must not be duplicated.
