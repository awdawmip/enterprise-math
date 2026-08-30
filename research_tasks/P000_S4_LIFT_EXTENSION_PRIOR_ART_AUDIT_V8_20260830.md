<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-6D-ROTATION-PRIOR-ART-DUPLICATION-AUDIT",
  "title": "P000 S4 lift / group-extension / canonical-section 外部先例审计 V8",
  "kind": "RESEARCH",
  "owner": "research/p000-6d-rotation-prior-art-audit",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "foundation_level": "P000_ROOT_AXIOM_BOUND",
  "p000_required": true,
  "frontier": "Classify external antecedents for the Gen12/Gen13 common-model S4 lift and its general lifting problem: group extensions, split sections/complements, relation residues in kernels, central/noncentral extension theory, faithful permutation degree, canonicality/nonuniqueness of sections, and model-theoretic universal/canonical choice boundaries.",
  "next_action": "Audit authoritative group-theory/cohomology/permutation-representation/model-theory sources claim-by-claim. Separate standard extension/splitting machinery from P000-specific opaque-Cell/no-quotient semantics. Include a strict applicability guard for H^2 and nonabelian kernels, and classify the Gen12 four-point faithful S4 witness as classical representation structure rather than novelty.",
  "dependencies": [
    "research_returns/P000_BASE_CELL_RA_STAR_ORBIT_V12_RETURN_20260830.md@main",
    "driver_reviews/P000_BASE_CELL_RA_STAR_ORBIT_V12_DRIVER_REVIEW_20260830.md@main",
    "research_returns/P000_AXIS_CHANNEL_FRAME_PRIOR_ART_AUDIT_V7_RETURN_20260830.md@main"
  ],
  "evidence_status": "FRAME_TORSOR_CONNECTION_CORE_PRIOR_ART_V7_ACCEPTED / S4_EXTENSION_SPLITTING_BOUNDARY_OPEN",
  "hard_block": null,
  "tags": ["P000","prior-art","S4","group-extension","splitting","section","kernel","cohomology","permutation-degree","canonicality"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-6D-ROTATION-PRIOR-ART-DUPLICATION-AUDIT",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P0006DPA8",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "REVISION",
  "parent_task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE"
}
-->

# P000 `S4` lift / group-extension / canonical-section 外部先例审计 V8

Status: `READY / GENERATION-8 / P1 / EXTERNAL-DUPLICATION-GATE`

## Hard target

`P000_S4_LIFT_EXTENSION_SPLITTING_EXTERNAL_DUPLICATION_BOUNDARY_CLASSIFIED`

## Mandatory audit map

逐条分类为 `EXACT_DUPLICATE / PARTIAL_ANTECEDENT / ADJACENT_METHOD / NO_MATERIAL_MATCH`：

1. `1 -> K -> G~ -> S4 -> 1` group extension language；
2. split extension / semidirect product / complement / homomorphic section；
3. lifted presentation relations landing in `K`；
4. central/abelian extensions and `H^2` classification under correct hypotheses；
5. nonabelian extension / Schreier-type theory when `K` nonabelian；
6. change of lift / section and conjugacy/nonuniqueness of complements；
7. faithful permutation representations of `S4`, especially degree 4 and the natural action；
8. the fact that a 24-element faithful permutation image needs at least four points；
9. projective/covering-group analogies only where exact hypotheses match；
10. automorphism/definability obstruction to a canonical section；
11. universal existence versus existence in one model；
12. exact P000 compound semantics: opaque Cell identity, no carrier quotient, native-axis typing, downstream frame/PF10 decorations.

## H^2 guard

不得把所有 kernel 都写成普通 `H^2(S4,K)`。

必须明确：

- coefficient group 是否 abelian；
- 是否 central extension；
- `S4` module action；
- cocycle convention and equivalence；
- nonabelian kernel 时使用何种更一般 extension formalism。

## Gen12 representation guard

必须检查并冻结：

- 4-point faithful action of `S4` is classical；
- natural `S4` action on four objects and induced action on six 2-subsets/edges is classical；
- Gen12 的新信息若有，只能在 P000 typed Full-Cell semantic assembly / no-quotient constraints，而不是 `S4` representation 本身。

## Terminology carry-forward

继续冻结 V7：

`STANDARD_FLATNESS != TRIVIAL_GLOBAL_HOLONOMY`。

需要全局平行 frame 时使用：

`TRIVIAL_HOLONOMY / SYNCHRONIZABLE / PURE_GAUGE`。

## Required outputs

- claim map；
- source ledger with authoritative sources；
- exact finite checker for any small group/permutation claims used；
- synthesis distinguishing classical extension theory from P000 compound semantics；
- explicit statement `NO_MATERIAL_MATCH != NOVELTY`。

## Valid terminal class

`CLASSICAL_S4_EXTENSION_SPLITTING_CORE_CLASSIFIED_P000_COMPOUND_LIFT_SEMANTICS_BOUNDARY_FROZEN`.
