<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-SIX-AXIS-JOHNSON-PLUCKER-DECOMPOSITION",
  "title": "P000 六轴 Johnson–Plücker 谱分解、互补对偶与 Pfaffian 算术不变量",
  "kind": "RESEARCH",
  "owner": "research/p000-six-axis-johnson-plucker-decomposition",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Determine whether the frozen six carrier-labelled native axis types admit a useful exact J(4,2)-spectral and exterior-bivector calculus that yields canonical projectors and arithmetic invariants without reducing P000 native dimension or identifying carrier symmetry with the full native rotation group.",
  "next_action": "Freeze the AB,AC,AD,BC,BD,CD labelling and carrier S4 action, derive the J(4,2) adjacency/complement operators and exact spectral projectors, then construct the Lambda^2 four-label representation and classify the Pfaffian quadratic under S4, complement and the frozen a_xi,b_xi actions.",
  "dependencies": [
    "research_tasks/P000_BASE_CELL_RA_STAR_ORBIT_V12_20260830.md@main",
    "enterprise_toolbox_registry.json@main"
  ],
  "source_refs": [],
  "evidence_status": "DRIVER_EXTERNAL_THEORY_SCOUTING_COMPLETE / NO_EXACT_TASK_DUPLICATE_FOUND / STRUCTURAL_BRIDGE_UNPROVED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "P000",
    "six-axis",
    "J(4,2)",
    "S4",
    "C2",
    "association-scheme",
    "exterior-algebra",
    "Gr(2,4)",
    "Plucker",
    "Pfaffian",
    "arithmetic-invariant"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-SIX-AXIS-JOHNSON-PLUCKER-DECOMPOSITION",
  "parent_objective_id": "OBJ-P000-SIX-AXIS-REPRESENTATION-ARITHMETIC",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000JP1",
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

# P000 六轴 Johnson–Plücker 谱分解、互补对偶与 Pfaffian 算术不变量

Status: `READY / P1 / HIGH / P000-BOUND / STRUCTURAL-DECOMPOSITION-FIRST`

## Mother question

冻结六个 carrier-labelled native axis types
`E1=AB, E2=AC, E3=AD, E4=BC, E5=BD, E6=CD`
之后，能否在**不降低 P000 原生六维空间、不把 carrier S4 当成 bare P000 完整旋转群**的前提下，把同一个六轴对象同时组织成 `J(4,2)` 的六顶点表示与 `Lambda^2` 的六基 bivector 表示，并由此导出真正可计算、可判伪的谱投影、互补对偶和整数二次不变量？

目标不是给既有 `S4` 换语言，而是判断这些经典结构是否产生项目当前还没有的 exact observables、decomposition certificates 或 arithmetic residues。

## Frozen inputs and scope

1. P000 作为无条件起始公理保持不变：原生 Enterprise 空间是 6D，时间单独类型化；任何 `A3`、`R^4`、`Lambda^2(R^4)` 或图表示只能是 derived calculus / representation facade。
2. 冻结 carrier 标号：`AB, AC, AD, BC, BD, CD` 对应 `E1,...,E6`。
3. 冻结当前 carrier-compatible generators：`a_xi=(E1 E2 E3)(E4 E6 E5)`，`b_xi=(E2 E4)(E3 E5)`，并保持 `E1,E6` fixed under `b_xi`。
4. `CARRIER_S4 != FULL_NATIVE_P000_ROTATION_GROUP`。本任务最多建立 axis-label/carrier-derived calculus；若要提升到 Cell/enriched automorphism，必须回到拥有该问题的现有 Gen12，而不是在本任务中偷换层级。
5. 若定义 Johnson 邻接，只允许使用“两个二元 carrier 标签共享一个端点”这一明确组合规则；不得从图形直观反向推导新的 native adjacency。
6. 外代数编码只允许把六轴量写成 `X=sum x_ij e_i wedge e_j`。不得据此声称 native space 实际是 4D。
7. Pfaffian/Plücker 二次式 `Q=x_AB*x_CD-x_AC*x_BD+x_AD*x_BC` 是待研究 observable。不得把 `Q=0` 预置为所有 P000 state 的约束。
8. `Spin(6)` 双覆盖及中心 relation residue 已作为 Gen12 的候选 residue classifier；本任务不得另做一个重复的 Spin-lift 主线。
9. 工具复用优先：有限群作用/轨道/稳定子使用现有 `T7_FINITE_SYMMETRY_EQUIVARIANCE`；circuit/cocircuit/incidence 检查使用现有 `T3_TYPED_INCIDENCE_CIRCUIT`。除非出现经证明的能力缺口，不建立同义新工具族。

## Hard target and required outputs

Hard target:

`P000_SIX_AXIS_JOHNSON_PLUCKER_DECOMPOSITION_AND_ARITHMETIC_INVARIANTS_EXACTLY_CLASSIFIED`.

至少完成以下六组输出。

### A. Johnson / association-scheme exact layer

在冻结六标签上：

- 构造 `J(4,2)` adjacency matrix `A_J`；
- 精确求其 spectrum、eigenspace dimensions 与 minimal polynomial；
- 构造所有对 `S4`-equivariant 的 rational spectral projectors；
- 明确验证六维 permutation module 的 `1+3+2` 分解，或给出与当前冻结作用不一致的精确原因；
- 构造 complement involution `c=(E1 E6)(E2 E5)(E3 E4)`，计算它与 carrier `S4`、`a_xi,b_xi` 的交换关系；
- 区分 `c` 作为组合 automorphism 与任何 native geometric rotation 的地位。

### B. K4 circuit/cocircuit layer

把四个 star objects

`J_A={E1,E2,E3}`，`J_B={E1,E4,E5}`，`J_C={E2,E4,E6}`，`J_D={E3,E5,E6}`

放入 `K4` graphic-matroid typing 中，精确判断哪些是 bonds/cocircuits、哪些三元集合是 circuits，并把 Gen12 的 star transport 改写为可核验的 incidence transport statement。不得把这一改写当作额外几何存在定理。

### C. Exterior / Plücker layer

给出从六轴坐标到 `Lambda^2` 六基坐标的显式双射，并计算：

- carrier `S4` 在 bivector coordinates 上的作用；
- `Q` 在 `S4`、`c`、`a_xi,b_xi` 下的 exact transformation law；
- 在选定 orientation 后的 Hodge-star matrix、`+/-` sectors 与 orientation dependence；
- Hodge pairing 与 Johnson complement pairing 是一致、带符号一致，还是仅共享同一三对 complementary edges；
- `Q` 的 bilinear polarization、rank、signature 以及这些量在允许的 coefficient rings 上的变化。

### D. Arithmetic layer

对整数六轴数据，至少研究：

- `Q(X)` 的 orbit behavior；
- `gcd(Q(X),m)` 与 `v_p(Q(X))` 是否只复述已有 valuation，还是提供新的 axis-coupled residue；
- complement-even / complement-odd、`1+3+2` sectors 与 `Q` 的关系；
- 一组明确声明、factor-blind 的整数 state families 上的 exact finite census；
- 最小反例：相同已有 project observables 但不同 `Q`，或相同 `Q` 但不同已有 observables。

任何 factorization 现象都只能作为 residue 记录；没有独立总成本和机制证明时不得宣称算法优势。

### E. Relation to current Gen12

把 `a_xi,b_xi` 在全部 projectors、`c`、`Q` 上的作用做成 regression table。若出现 central sign、kernel 或 projective residue，只记录为 Gen12 可消费的 classifier，不在本任务中把 axis-level 现象提升成 Full-Cell theorem。

### F. Deterministic certificate

提交一个 exact checker/certificate，至少验证：

- 六标签与 Johnson adjacency；
- `S4` generator relations；
- complement commutation；
- spectral projectors 的 idempotence/orthogonality/sum-to-identity；
- `Lambda^2` action；
- `Q` transformation；
- 声明的 finite arithmetic census。

浮点近似不能代替 exact spectrum、projector 或 quadratic-form 结论。

## Research value to preserve

当前六轴同时是 `K4` 的六条 edge labels、`J(4,2)` 的六个 vertices、以及一个六维 exterior-coordinate system 的候选基。若三种表示真正兼容，就能把当前以“六个符号 + S4 permutation”为主的 carrier 语言升级成：

`finite symmetry -> canonical spectral sectors -> complement duality -> quadratic arithmetic observable`.

这可能提供一批不依赖人为挑三根轴的六维观测量，同时给 Gen12、后续 valuation/tropical 研究和数论实验提供统一输入。若证明这些结构只是在重述已有 `S4`，同样应以 exact no-new-information boundary 关闭，避免长期重复借名。

## Success, kill, and return criteria

成功有两档：

1. `STRUCTURAL_CALCULUS_SURVIVES`：得到至少一个当前 toolbox/定义中没有直接等价物的 exact projector、quadratic invariant 或 decomposition certificate，并明确其 P000 typing；
2. `REPRESENTATION_ONLY_NO_NEW_INFORMATION`：完整证明所有候选量都可由现有 `S4`/incidence observables 重构，因此关闭该路线。

立即 kill / narrow 的情况：

- 需要把 native 6D 解释成 3D 或 4D 才成立；
- 需要全局预设 `Q=0`；
- 把 complement involution 或 Hodge star 无证明地称为 native rotation；
- 用数值拟合代替 exact representation calculation；
- 只得到术语映射而没有新的可计算 quantity/certificate；
- 为已有 T3/T7 能力重新建立同义工具。

Return 必须明确列出：proved statements、counterexamples、new reusable quantities、与现有工具的复用关系、对 Gen12 的可消费 residue，以及仍然开放但**不自动生成后续任务**的问题。
