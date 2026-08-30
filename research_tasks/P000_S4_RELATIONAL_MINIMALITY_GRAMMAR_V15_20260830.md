<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "title": "P000 S4 正向定理的关系最小化语法与成本冻结 V15",
  "kind": "RESEARCH",
  "owner": "research/p000-l1-native-carrier-contact-bridge",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "foundation_level": "P000_ROOT_AXIOM_BOUND",
  "p000_required": true,
  "frontier": "Make the downstream relational-minimality problem well-posed by freezing an admissible finite relational grammar, parameter/definitional-equivalence policy, package preorder/cost, and finite regression/search envelope; only then classify Pareto-minimal faithful/canonical S4 strengthening candidates without mutating P000 or restating the desired section as a primitive.",
  "next_action": "Audit accepted downstream sorts/relations; freeze background-vs-candidate relation catalog; define parameter-free definitional equivalence and Pareto cost; include Gen12/Gen13/Gen14 finite witnesses in the envelope; prove the grammar can express no-lift, nonsplit, split-noncanonical and canonical regimes; then enumerate or structurally classify minimal packages inside the frozen grammar.",
  "dependencies": [
    "research_returns/P000_MINIMAL_RELATIONAL_STRENGTHENING_FOR_CANONICAL_S4_V14_RETURN_20260830.md@main",
    "driver_reviews/P000_MINIMAL_RELATIONAL_STRENGTHENING_V14_DRIVER_REVIEW_20260830.md@main",
    "driver_reviews/P000_S4_LIFT_UNIVERSALITY_EXTENSION_V13_DRIVER_REVIEW_20260830.md@main",
    "projects/enterprise-math/P000_NATIVE_FCC_STRICT_BRIDGE.json@global"
  ],
  "evidence_status": "GEN14_REVISION_REQUIRED / ABSTRACT_SECTION_RESIDUE_FIXED_POINT_CRITERIA_ACCEPTED / RELATIONAL_MINIMALITY_GRAMMAR_OPEN",
  "hard_block": null,
  "tags": ["P000","native-6D","S4","relational-grammar","definability","Pareto-minimality","canonical-section","no-quotient"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000FCC15",
  "origin_kind": "DRIVER_REVIEW_REVISION",
  "task_lineage": "REVISION",
  "parent_task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "successor_gate": {
    "new_information_gap": "Gen14 proved exact section/residue/fixed-point criteria but showed that primitive/native package minimality is presentation-dependent because the admissible relation grammar, definitional-equivalence policy, package preorder and finite search envelope were not frozen.",
    "why_parent_result_does_not_close_it": "Without a frozen minimization universe there is no invariant meaning of 'the minimal non-tautological relation package'; Gen14 therefore cannot legitimately produce the requested Pareto frontier.",
    "discriminating_outcomes": [
      "freeze a finite admissible downstream relation grammar and prove it expressive enough for all mandatory positive/negative regimes",
      "freeze a parameter-free definitional-equivalence rule and Pareto package cost",
      "classify Pareto-minimal faithful/canonical S4 packages inside that grammar",
      "prove no chosen finite grammar can support the requested classification and return an exact grammar obstruction"
    ],
    "kill_condition": "Do not declare the desired S4 section, R_a/R_b, K=1, or a carrier/native identity equation as a primitive. Do not add arbitrary named constants merely to rigidify a witness. Do not quotient hidden kernel state. Do not mutate P000. Do not redo Gen14 section/residue/fixed-point algebra except as regression.",
    "alternative_route_or_free_exploration_considered": "Continuing to propose ad hoc relation packages under an open-ended vocabulary cannot produce an invariant minimality theorem. Grammar/cost freeze is the necessary next control point.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Generation 15 repairs the mathematical specification exposed by Gen14 and converts 'minimal' into a checkable finite/Pareto statement."
  }
}
-->

# P000 `S4` 正向定理的关系最小化语法与成本冻结 V15

Status: `READY / GENERATION-15 / P0 / P000-BOUND / GRAMMAR-FIRST`

## Mother problem

Gen14 已精确冻结：

\[
Sec(q)\cong Z(q)
\]

其中 `Z(q)` 是满足

\[
A^3=B^2=(AB)^4=1
\]

的冻结生成元 lift-pair 集合；canonical section 则是声明的 `Aut_prim(M)` 在 `Sec(q)` 上作用的 fixed point。

但 Gen14 同时证明：在没有冻结 relation grammar / definitional equivalence / package cost 的情况下，所谓“最小原生关系包”不是不变量。

因此本任务先解决：

\[
\boxed{\text{我们到底在什么有限、可比较的关系宇宙里谈“最小”？}}
\]

只有这个问题被精确关闭后，才允许恢复 Pareto-minimal package classification。

## Hard target

`P000_S4_RELATIONAL_MINIMALITY_GRAMMAR_EQUIVALENCE_COST_AND_PARETO_ENVELOPE_EXACTLY_FROZEN`

允许在同一任务中继续完成：

`P000_PARETO_MINIMAL_FAITHFUL_OR_CANONICAL_S4_PACKAGES_CLASSIFIED_WITHIN_FROZEN_GRAMMAR`

但后者不是前者的替代品。

## A. Freeze background sorts and zero-cost accepted structure

必须逐项读取当前 accepted downstream source，明确哪些是**背景结构**而不是本任务新增成本。至少处理：

- opaque `NativeCell` sort；
- six native axis types `E1..E6`；
- accepted frame `f_x:A->C_x`；
- PF-10 `I/O/M` local relation tensor；
- accepted connection/transport（若模型声明保留）；
- derived star types `J_A..J_D` 的当前 accepted strength；
- native adjacency/incidence 的当前来源与是否已是背景 primitive。

禁止把 FCC carrier vertex identity 当 native Cell identity。

## B. Freeze a finite candidate-relation grammar

必须给出一个**有限 catalog**。每个 candidate relation form 必须明确：

- source/target sorts；
- arity；
- symmetry/typing law；
- 是否允许参数/常数；
- preservation law under enriched automorphisms；
- 它为何不是 `R_a/R_b` 或 desired section 的改名。

优先从已有 downstream language 中选择，例如：

- Cell–Cell adjacency/incidence refinement；
- Cell–Axis incidence；
- star-overlap/gluing relation；
- Hidden–Cell / Hidden–Axis incidence（若 hidden sort 被证明必要）；
- parameter-free hidden-state relational rigidity；
- frame/connection equivariance constraints。

**禁止**开放式“任意新 predicate”。若 catalog 无法覆盖 Gen13 `GL(2,3)` hidden-residue witness，必须显式增加最弱 hidden relation form 或宣告 grammar 不充分。

## C. Parameter and tautology policy

至少冻结：

- 默认 `NO_NEW_DISTINGUISHED_CONSTANTS`；
- 不允许用常数逐点命名 Cells/hidden states 来人为杀死 automorphism；
- 不允许把 `there exists a section`、`R_a`、`R_b`、`K=1` 作为 candidate primitive；
- 如果允许某类 distinguished feature，必须给 parameter-free intrinsic admissibility test。

## D. Definitional-equivalence policy

必须精确定义什么时候两个 relation packages 视为同一方案。

首选：在固定背景 sorts 上，**无新参数的 mutual definability** 视为同一 equivalence class。

必须处理 Gen14 regression：

- `K4` Cell adjacency；
- tetrahedral Cell–axis incidence。

判定它们在冻结 grammar 下是同一 definitional class、严格不同，还是只在新增 derived sort 后 bi-interpretable。禁止含糊写“差不多一样”。

## E. Package preorder / Pareto cost

冻结一个显式偏序，至少包含：

1. 新增 sort 数；
2. 新增 relation-symbol 数；
3. relation arity multiset；
4. 是否使用 hidden sort；
5. 是否增加额外 global constraints；
6. 是否需要 distinguished parameter/constant（默认禁止）。

不得用未经定义的“更自然”“更简单”排序。

允许 Pareto-minimal 而非强行单值最小。

## F. Finite regression/search envelope

搜索/证书 envelope 必须至少容纳：

- Gen12 `K=1` faithful canonical witness；
- Gen13 `P4` four-Cell no-lift witness；
- Gen13/14 `K_{2,2,2,2}` eight-Cell split/noncanonical witness；
- Gen13 `GL(2,3)` hidden relation witness（9 hidden vectors + 4 projective Cell anchors）；
- Gen14 `K4` adjacency and tetrahedral incidence canonical witnesses。

建议最低 envelope：

`|NativeCell| <= 8`, `|AxisType|=6`, `|Hidden| <= 9`，并按 grammar 明确其他 sort bound。

若 full exhaustive relation-valuation enumeration 不可行，必须区分：

- exhaustive package-subset classification；
- structural theorem/countermodel classification inside each package；
- targeted finite witness regression。

不得把 targeted witness 检查冒充“枚举了所有 finite models”。

## G. Expressivity gate

在开始最小化前，必须证明 frozen grammar 至少能表达/区分：

1. `NO_LIFT`；
2. `SURJECTIVE_NONSPLIT`；
3. `SPLIT_NONCANONICAL`；
4. `CANONICAL_FAITHFUL`。

若某一层无法表达，先修 grammar，不得继续算 Pareto frontier。

## H. After grammar freeze: minimality classification

只有 A–G 通过以后，才执行：

- faithful section package 的 sufficiency/necessity/redudancy；
- canonical section package 的 fixed-point sufficiency/necessity；
- one-condition deletion countermodels；
- definitional-equivalence quotient 后的 Pareto frontier。

Gen14 的 exact criteria作为 mandatory regression，不重做：

\[
Sec(q)\cong Z(q)
\]

及

\[
\text{canonical}\iff Sec(q)^{Aut_{prim}(M)}\neq\varnothing.
\]

## I. Boundary

本任务是 P000 下游模型语言规范，不是 P000 root ontology 修改。

冻结：

`BARE_P000_UNIVERSAL_S4_LIFT_DERIVABLE = FALSE`。

`BARE_P000_CANONICAL_S4_SECTION_DERIVABLE = FALSE`。

`CARRIER_S4 != COMPLETE_NATIVE_P000_ROTATION_GROUP`。

`NO_KERNEL_QUOTIENT`。

`TIME_FIXED`。

## Deterministic checker / certificate

至少验证：

- grammar catalog finite；
- no forbidden direct-generator/section primitive；
- definitional-equivalence test on Gen14 K4/incidence pair；
- package-cost partial order antisymmetry/transitivity on catalog subsets；
- all five mandatory finite witness classes fit the envelope；
- expressivity four-regime gate；
- if Pareto classification is attempted, exact frontier and deletion witnesses。

## Valid terminal classes

- `RELATIONAL_MINIMALITY_GRAMMAR_EQUIVALENCE_COST_AND_ENVELOPE_FROZEN`；
- `PARETO_MINIMAL_FAITHFUL_AND_CANONICAL_S4_PACKAGES_CLASSIFIED_WITHIN_FROZEN_GRAMMAR`；
- `FINITE_GRAMMAR_EXPRESSIVITY_OBSTRUCTION_EXACTLY_PROVED`；
- `NO_PARAMETER_FREE_FINITE_GRAMMAR_IN_DECLARED_CATALOG_CAN_SEPARATE_REQUIRED_REGIMES_PROVED`。

External prior-art lane remains:

`RS-P000-6D-ROTATION-PRIOR-ART-DUPLICATION-AUDIT / TP2-2F8C6A1D9E7043B5C812 / Generation 8`.
