<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "title": "P000 faithful/canonical S4 lift 的最小下游关系增强 V14",
  "kind": "RESEARCH",
  "owner": "research/p000-l1-native-carrier-contact-bridge",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "foundation_level": "P000_ROOT_AXIOM_BOUND",
  "p000_required": true,
  "frontier": "Classify the minimal downstream relational condition package that is necessary/sufficient for existence of a faithful S4 section and, separately, for a canonical automorphism-invariant section in the framed Full-Cell model class, while excluding the Gen13 P4 no-lift and GL(2,3) nonsplit regimes without quotienting hidden kernels or modifying P000.",
  "next_action": "Use the S4 presentation a^3=b^2=(ab)^4=1 to prove the exact section criterion for q:Gtilde->S4; separate existence from canonicality via the automorphism action on Sec(q); search for minimal non-tautological Cell/hidden-relation conditions that force surjectivity, vanishing relation residues and an automorphism-fixed section, with independence/countermodel witnesses for every proposed condition.",
  "dependencies": [
    "research_returns/P000_S4_LIFT_UNIVERSALITY_EXTENSION_V13_RETURN_20260830.md@main",
    "driver_reviews/P000_S4_LIFT_UNIVERSALITY_EXTENSION_V13_DRIVER_REVIEW_20260830.md@main",
    "research_returns/P000_BASE_CELL_RA_STAR_ORBIT_V12_RETURN_20260830.md@main",
    "projects/enterprise-math/P000_NATIVE_FCC_STRICT_BRIDGE.json@global"
  ],
  "evidence_status": "GEN13_SPLIT_NONSPLIT_NO_LIFT_CANONICALITY_REGIMES_DRIVER_ACCEPTED / MINIMAL_POSITIVE_STRENGTHENING_OPEN",
  "hard_block": null,
  "tags": ["P000","native-6D","S4","section","kernel","relation-residue","canonicality","automorphism","minimal-axioms","no-quotient"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000FCC14",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "REVISION",
  "parent_task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "successor_gate": {
    "new_information_gap": "Gen13 proves bare P000 does not universally force an S4 lift and does not canonically select a section, but it does not identify the weakest non-tautological downstream relational conditions that recover faithful or canonical lifting.",
    "why_parent_result_does_not_close_it": "The split/nonsplit/no-lift witnesses classify failure regimes but do not isolate a minimal sufficient/necessary strengthening package or prove independence/redundancy of its components.",
    "discriminating_outcomes": [
      "derive a minimal exact condition package equivalent to existence of a faithful S4 section",
      "derive a strictly stronger minimal package equivalent to an automorphism-invariant canonical section",
      "prove that no non-tautological finite local relational package of the declared form can force canonicality, with exact countermodels"
    ],
    "kill_condition": "Do not add 'the desired S4 section' itself as a primitive; do not quotient K; do not identify carrier vertices with native Cells; do not assume K=1 unless derived; do not confuse split with canonical; do not claim necessity from one convenient witness; do not mutate P000 root ontology.",
    "alternative_route_or_free_exploration_considered": "After Gen13, another existence witness or another classical extension example has low leverage. The direct frontier is the minimal positive relational strengthening theorem.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Generation 14 changes the problem from model-class counterexample classification to minimal sufficient/necessary downstream structure for a positive native rotation theorem."
  }
}
-->

# P000 faithful/canonical `S4` lift 的最小下游关系增强 V14

Status: `READY / GENERATION-14 / P0 / P000-BOUND / MINIMAL-POSITIVE-STRENGTHENING-FIRST`

## Mother question

Gen13 已冻结四种结构区间：

1. `K=1` faithful split（Gen12）；
2. `K!=1` but split（`C2^4 ⋊ S4`）；
3. surjective nonsplit（`GL(2,3)->PGL(2,3)~=S4`）；
4. no-lift（native `P4` adjacency）。

因此 bare P000 在当前 primitive/model class 下**既不强制 universal lift，也不强制 canonical section**。

本任务不再重复举 extension 例子，而问：

\[
\boxed{\text{若要得到一个真正可复用的正定理，最少还需要哪些下游 native relations？}}
\]

必须严格区分：

- `EXISTENCE`: 至少存在一个 faithful `S4` section；
- `CANONICALITY`: primitive-preserving automorphisms 不会把所选 section 移到另一个 section。

## Hard target

`P000_MINIMAL_DOWNSTREAM_RELATIONAL_PACKAGE_FOR_FAITHFUL_OR_CANONICAL_S4_LIFT_EXACTLY_CLASSIFIED`

## A. Exact section criterion from the frozen presentation

令

\[
q:\widetilde G\to S_4
\]

为 enriched Full-Cell automorphism 到冻结 axis/carrier `S4` readout 的 homomorphism，`K=ker(q)`。

冻结

\[
S_4=\langle a,b\mid a^3=b^2=(ab)^4=1\rangle,
\]

其中 `a=(BCD)`, `b=(AB)`。

必须证明/精确否定以下 criterion：

> `q` 有 homomorphic section `s:S4->Gtilde`
> 当且仅当存在 lifts `A in q^-1(a)`, `B in q^-1(b)` 满足
> `A^3=B^2=(AB)^4=1`。

若该 presentation 还需额外 relation 才能唯一得到 `S4`，必须指出并修正，禁止默认。

同时证明 section 自动 injective，因此给 faithful copy of `S4`。

## B. Residue formulation

对任意 generator lifts 定义：

`z_a=A^3 in K`,
`z_b=B^2 in K`,
`z_ab=(AB)^4 in K`。

必须分类：

- lift choice 如何改变 residue triple；
- `0-residue triple` 是否与 split 完全等价；
- 在 nonabelian `K` 情形是否需要 ordering/conjugacy 修正；
- Gen13 `GL(2,3)` 的 invariant `z_ab=-I` 作为强 regression。

不得通过 quotient `K` 让 residue 消失。

## C. Separate four positive-strength layers

至少区分：

1. `READOUT_SURJECTIVE`：`q(Gtilde)=S4`；
2. `SPLIT_EXISTS`：存在某个 faithful section；
3. `SECTION_AUTOMORPHISM_FIXED`：至少一个 section 被声明模型的全部 primitive-preserving automorphisms 固定；
4. `SECTION_UNIQUE/CANONICAL`：若需要更强唯一性，必须说明是 strict uniqueness 还是 uniqueness up to an explicitly allowed equivalence。

证明各层蕴含关系，并给严格分离 witness。

Gen13 regressions：

- `P4`: 1 失败；
- `GL(2,3)`: 1 成功、2 失败；
- `C2^4 ⋊ S4`: 2 成功、3 失败；
- Gen12 `K=1`: 2 成功；是否自动满足 3 必须按完整 model automorphism group 检查，不能只因 `K=1` 宣告 canonical。

## D. Minimal downstream relational package search

候选增强只能来自/作用于 downstream native relational language，例如：

- Cell adjacency/incidence orbit structure；
- star-object overlap/gluing；
- hidden-state relation rigidity；
- frame/connection equivariance；
- distinguished but **independently meaningful** Cell/hidden relational features；
- automorphism-rigidity conditions。

禁止把以下 tautology 当“最小条件”：

- `there exists an S4 section`；
- 直接把 `R_a,R_b` 本身加为 primitive；
- 直接宣布 `K=1` 而不给 native relational cause；
- 把 carrier label 当 native Cell identity。

每个候选 package 必须说明具体 primitive/derived relation、typing、preservation law，以及为何它排除 Gen13 哪个反例。

## E. Necessity / sufficiency / redundancy

对 faithful-lift package 与 canonical-lift package 分别做：

- sufficiency proof；
- necessity test；
- redundancy elimination；
- one-condition-at-a-time deletion countermodels。

若不存在唯一“最小” package，而只有若干 incomparable minimal packages，必须完整分类 Pareto-minimal families，而不是任选一组。

## F. Canonicality as automorphism fixed-point problem

令 `Sec(q)` 为 homomorphic sections 集合，令 `Aut_prim(M)` 为保持当前 primitive model data 的 automorphism group。

必须建立明确 action：

\[
Aut_{prim}(M)\curvearrowright Sec(q).
\]

优先尝试证明：

\[
\boxed{\text{canonical section exists}\iff Sec(q)\text{ has an }Aut_{prim}(M)\text{-fixed point}}
\]

并区分：

- fixed point existence；
- unique fixed point；
- all sections one orbit；
- section only canonical after adding independently justified extra structure。

`C2^4 ⋊ S4` 的 kernel-conjugation no-fixed-section 为 mandatory regression。

## G. Gen12 / Gen13 regression suite

必须同时保留：

- Gen12 `K=1`, order 24, trivial relation residue；
- Gen13 split `C2^4 ⋊ S4`, 16 sections, no K-invariant canonical section；
- Gen13 nonsplit `GL(2,3)`, invariant `(AB)^4=-I`；
- Gen13 `P4` no-lift；
- carrier/native sorts disjoint；
- local channel `S6` remains gauge only；
- no P000 mutation；
- no kernel quotient；
- time fixed。

## H. Bare-P000 boundary

由于 Gen13 已给合法 countermodels，本任务不得重新声称 bare P000 当前即 universal/canonical `S4` theorem。

合法的更强结论只能是：

> 在某个**明确新增或从现有结构推导出的 downstream relational package**下，faithful/canonical lift 得到必要充分分类。

若候选 strengthening 无法从当前已接受结构推导，则必须标记为 `NEW_DOWNSTREAM_MODEL_ASSUMPTION_CANDIDATE`，不得偷升为 P000 root axiom。

## I. Deterministic checker / exact certificates

至少覆盖：

- `(2,3,4)` presentation quotient/order check；
- section criterion；
- residue triple search；
- `Sec(q)` enumeration for finite witnesses；
- `Aut_prim(M)` action on sections；
- fixed-point/canonicality test；
- deletion countermodels for proposed minimal package；
- all Gen12/Gen13 regressions；
- no quotient / no P000 mutation。

## Valid terminal classes

- `MINIMAL_FAITHFUL_S4_LIFT_RELATIONAL_PACKAGE_IFF_CLASSIFIED`；
- `MINIMAL_CANONICAL_S4_SECTION_RELATIONAL_PACKAGE_IFF_CLASSIFIED`；
- `MULTIPLE_INCOMPARABLE_MINIMAL_POSITIVE_PACKAGES_CLASSIFIED`；
- `NO_NONTAUTOLOGICAL_DECLARED_RELATIONAL_PACKAGE_CAN_FORCE_CANONICAL_SECTION_EXACTLY_PROVED`。

允许前两类同时成立。

External prior-art lane remains:

`RS-P000-6D-ROTATION-PRIOR-ART-DUPLICATION-AUDIT / TP2-2F8C6A1D9E7043B5C812 / Generation 8`.

该 lane 负责 classical group extension / splitting / H^2 / complements / canonical-section antecedents；本任务不得把这些成熟理论包装为 P000 新数学。
