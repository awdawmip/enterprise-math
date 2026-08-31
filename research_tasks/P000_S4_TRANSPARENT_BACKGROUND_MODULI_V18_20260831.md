<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "title": "P000 S4 透明背景的局部表示与非平凡模空间 V18",
  "kind": "RESEARCH",
  "owner": "research/p000-l1-native-carrier-contact-bridge",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "foundation_level": "P000_ROOT_AXIOM_BOUND",
  "p000_required": true,
  "frontier": "Within the Gen17 charged transparency grammar, classify finite/local presentations and nontrivial moduli of S4-equivariant PF10 profiles and independent connections/holonomy on the K4/tetra Full-Cell structural models, and prove that the conditional S4 lift supports non-degenerate content or identify the exact obstruction.",
  "next_action": "Reduce PF10_STRUCTURAL_AUT_EQ and CONNECTION_STRUCTURAL_AUT_EQ to generator/orbit-representative checks when valid; classify base-cell stabilizer orbit parameters for I/O/M; classify equivariant independent connection transports up to gauge and reverse-edge law; construct or obstruct a nonidentity, preferably nonflat, fully S4-equivariant connection; then combine with a nonconstant PF10 family in one common Full-Cell S4 model.",
  "dependencies": ["research_returns/P000_BACKGROUND_S4_EQUIVARIANCE_GATE_V17_RETURN_20260830.md@main","driver_reviews/P000_BACKGROUND_S4_EQUIVARIANCE_GATE_V17_DRIVER_REVIEW_20260831.md@main","research_artifacts/P000_BACKGROUND_S4_EQUIVARIANCE_GATE_V17/BACKGROUND_EQUIVARIANCE_CERTIFICATE.json@main"],
  "evidence_status": "GEN17_CHARGED_BACKGROUND_EQUIVARIANCE_GATES_DRIVER_ACCEPTED / NONTRIVIAL_EQUIVARIANT_CONTENT_MODULI_OPEN",
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
  "identity_lane": "P000FCC18",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "REVISION",
  "parent_task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE"
}
-->

# P000 `S4` 透明背景的局部表示与非平凡模空间 V18

Status: `READY / GENERATION-18 / P0 / P000-BOUND / NONTRIVIAL-EQUIVARIANT-CONTENT`

## Mother problem

Gen17 已接受两个有成本的背景透明 gate：

`PF10_STRUCTURAL_AUT_EQ`

以及在独立 connection 被声明时的

`CONNECTION_STRUCTURAL_AUT_EQ`。

这些条件足以把 structural `S4` lift 从背景 symmetry leak 中保护出来，但还没有回答：

\[
\boxed{\text{这些 gate 是否允许真正非平凡的 Full-Cell 内容，还是只剩常数/恒等退化模型？}}
\]

本任务必须把全局 automorphism-transparency 条件变成可检查的有限局部/生成元条件，并分类其非平凡解空间。

## Hard target

`P000_S4_TRANSPARENT_BACKGROUND_LOCAL_PRESENTATION_AND_NONTRIVIAL_MODULI_EXACTLY_CLASSIFIED`

## A. Freeze Gen17 boundary

不得修改：

- G15 relation/constraint grammar；
- Gen17 atomic charged gates 与各自 `g+=1` 成本；
- Gen16 裸 `{K4_ADJ}` frontier 的拒绝；
- `CARRIER_S4 != COMPLETE_NATIVE_P000_ROTATION_GROUP`；
- `NO_KERNEL_QUOTIENT`；
- `TIME_FIXED`。

本任务研究的是 downstream charged models，不是 P000 root 变更。

## B. Finite/local presentation of PF-10 transparency

对 K4/tetra structural `S4` action，证明或精确否定：

1. 同时检查 frozen generators `a,b` 的 PF-10 equivariance 是否等价于 `PF10_STRUCTURAL_AUT_EQ`；
2. 在一个 Cell orbit 上是否可由一个 representative Cell 的 stabilizer-fixed profile 唯一生成全局 equivariant family；
3. 给出 base Cell stabilizer 在 6 channel 上的 orbit partition；
4. 给出 `I`、`O` 与 ordered-pair `M` 的全部 orbit 参数；
5. 区分 full local pointwise `S4` invariance 与 orbitwise Cell-equivariance，禁止把后者错误收缩为所有 Cell 都携带同一个常数 tensor。

至少回归 Gen17 数值：base tetra Cell stabilizer vector orbits `2`、ordered-pair orbits `8`；full local S4 vector orbit `1`、ordered-pair orbits `3`。

## C. Nonconstant PF-10 witness

必须构造一个 exact PF-10 family 满足：

- `PF10_STRUCTURAL_AUT_EQ=true`；
- 至少两个 Cell 的 raw channel presentation 数据不相同；
- 不是所有 `I/O` 常数向量、不是所有 `M` 单一常数矩阵；
- 经 frame/gauge reindexing 后仍是同一 equivariant native content family。

若任何非常数 family 不存在，必须给 exact obstruction。

## D. Independent connection moduli

当 independent connection 被声明时：

1. 明确 connection value group/typed bijection universe，禁止默认为 SO(6)；
2. 选一个 oriented K4 edge 作为 representative，分类其 stabilizer compatibility；
3. 加入 reverse-edge law `T_yx=T_xy^-1`；
4. 证明 generator/local checks 何时等价于 `CONNECTION_STRUCTURAL_AUT_EQ`；
5. 在 gauge equivalence 下分类全部或至少完整 finite connection classes；
6. 计算 loop holonomy conjugacy data。

## E. Nonidentity / nonflat equivariant connection gate

优先寻找：

\[
\boxed{T\neq id,\quad CONNECTION\_STRUCTURAL\_AUT\_EQ=true}
\]

并进一步寻找：

\[
\boxed{Hol(\gamma)\neq id}
\]

但仍满足完整 `S4` holonomy conjugacy law的模型。

若 nonflat fully-equivariant connection 不存在，必须给 exact theorem 并指出 obstruction 来自 reverse-edge law、edge stabilizer、connection value group还是其他 typed condition。

冻结：`NONFLAT != AUTOMATIC_ROTATION_OBSTRUCTION`，但本任务必须决定在当前有限 K4 model 中非平坦等变解是否实际存在。

## F. Common-model integration

必须在**同一个** K4/tetra Full-Cell model 中同时放入：

- nonconstant equivariant PF-10 family；
- nonidentity independent connection（若存在）；
- charged transparency gates；
- 已接受的 `R_a,R_b` structural action。

验证：

`R_a^3=R_b^2=(R_aR_b)^4=id`

在完整 enriched data 上成立，而非只在 Cell/axis labels 上成立。

若只能分别构造，必须标记 `COMMON_MODEL_INTEGRATION_OPEN`。

## G. Moduli output

至少输出：

- `PF10_EQUIVARIANT_MODULI` 的参数/轨道分类；
- `CONNECTION_EQUIVARIANT_MODULI` 或 exact obstruction；
- gauge-equivalence 规则；
- nontrivial witness 数量/代表元；
- holonomy classes；
- common-model existence verdict。

不得把 presentation gauge bit 计成新 native spatial axis。

## H. Deterministic checker

至少覆盖：

- `S4`/stabilizer exact enumeration；
- PF10 orbit partitions and generator equivalence；
- nonconstant PF10 witness；
- connection stabilizer/reverse-edge/gauge enumeration；
- holonomy loops；
- enriched `a^3,b^2,(ab)^4` relations；
- Gen17 deletion regressions；
- no P000 mutation / no kernel quotient / time fixed。

## Valid terminal classes

- `NONTRIVIAL_S4_EQUIVARIANT_PF10_AND_NONFLAT_CONNECTION_COMMON_MODEL_CONSTRUCTED`；
- `NONTRIVIAL_PF10_AND_ONLY_FLAT_EQUIVARIANT_CONNECTIONS_CLASSIFIED`；
- `PF10_MODULI_CLASSIFIED_CONNECTION_EQUIVARIANCE_EXACTLY_OBSTRUCTED`；
- `TRANSPARENCY_GATES_FORCE_DEGENERATE_BACKGROUND_EXACTLY_PROVED`。

External prior-art lane remains separate and must not be duplicated.
