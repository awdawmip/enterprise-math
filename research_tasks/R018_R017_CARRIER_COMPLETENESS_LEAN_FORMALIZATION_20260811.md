<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R018-R017-CARRIER-COMPLETENESS-LEAN-FORMALIZATION",
  "title": "R018 R017 Carrier Completeness Lean Formalization",
  "kind": "FORMALIZATION",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_CRITICAL",
  "frontier": "Formalize the frozen generic core accepted from R017: joint-observation minimality, quotient saturation/completeness, one-step quotient lifting, finite-word repeated re-collapse exactness under explicit hypotheses, and a finite composition counterexample, while keeping the arithmetic p-th-power carrier semantics scoped.",
  "next_action": "Implement a narrow Lean module for R018-L01 through L09, reuse R016 relational-support primitives where suitable, audit axioms/placeholders, and run the repository-pinned warnings-fatal EnterpriseMath build.",
  "dependencies": [
    {
      "target": "RS-R017-PTH-POWER-UNRESOLVED-CARRIER-CLASSIFICATION",
      "action": "FORMALIZE_ACCEPTED_CORE",
      "satisfied": true
    },
    {
      "target": "RS-R016-R015-BRANCH-DEFERRAL-LEAN-FORMALIZATION",
      "action": "REUSE_RELATIONAL_SUPPORT_CORE",
      "satisfied": true
    },
    {
      "target": "current Enterprise Math Lean toolchain",
      "action": "USE_PINNED",
      "satisfied": true
    }
  ],
  "source_refs": [
    "R017 accepted Driver package / journal checkpoint",
    "EnterpriseMath/Precision/BranchDeferral.lean",
    "docs/P023_COMPOSITION_SAFE_COLLAPSE.en.md",
    "research_common_surface.json::A4_P023_relation_observable_bridge"
  ],
  "evidence_status": "LEAN_FOUNDATION_GATE",
  "last_progress_ref": "R017 Driver acceptance and first R009/P023 impact audit",
  "last_progress_at": "2026-08-11T14:27:00+08:00",
  "hard_block": null,
  "tags": [
    "R018",
    "R017",
    "Lean",
    "carrier",
    "quotient",
    "saturation",
    "re-collapse",
    "future-language",
    "support"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R018",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:87a1272862a3d84b01bc6d2a8617486a2ca998c1ab1cfd016f29c6b6edd7f64e",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R018 — R017 Carrier Completeness Lean Formalization

Status: `READY / P0 / FOUNDATIONAL_CRITICAL / LEAN FOUNDATION GATE / NOT CANONICAL`

## 1. Mother question

Formalize the stable mathematical core accepted from R017 without turning the two-neighbour bracket into a universal carrier.

The formalized boundary must preserve these distinctions:

- a pair of endpoint observations retained for later lower/upper selection;
- a quotient/cell label;
- the full fine fibre represented by a cell;
- fine-conservative support evolution;
- repeated quotient saturation after intermediate steps.

R018 does not decide application-level terminology and does not rewrite R009 or P023.

## 2. Required theorem targets

### R018-L01 — joint-observation kernel

For functions `f : X → A` and `g : X → B`, define the joint observation `q x := (f x, g x)`.

Prove the exact equivalence relation statement

`q x = q y ↔ f x = f y ∧ g x = g y`

and derive the coarsest-factorization theorem: any observation through which both `f` and `g` factor also factors through `q`, up to an explicit map on the image or an equivalent clean formulation.

### R018-L02 — p-th-power bracket structure

For `p ≥ 2`, define transparent lower and upper p-th-power anchors `L_p` and `U_p` using integer/Nat root machinery already available in the repository.

Prove at minimum:

1. `L_p n ≤ n ≤ U_p n`;
2. `L_p n = U_p n` exactly at perfect p-th powers;
3. interior points between consecutive p-th powers have the same ordered bracket;
4. exact powers form singleton bracket fibres and each open gap forms one nontrivial fibre.

Do not identify the bracket fibre with literal endpoint alternatives.

### R018-L03 — deferred endpoint selection

Formalize lower/upper selection as a later choice of one component of the joint observation.

Using the existing relational-support theorems where suitable, prove the scoped result that preserving both endpoint observations is sufficient and minimal for a future interface consisting of later lower/upper selection followed by a result-only relational future on the selected anchor.

State the theorem so it does not imply adequacy for arbitrary fine-state operations before selection.

### R018-L04 — quotient saturation

For `q : X → Q`, define a saturation/closure operator equivalent to

`Sat q A = {x | ∃ y ∈ A, q x = q y}`.

Prove extensivity, monotonicity and idempotence, and prove that two supports have the same quotient image exactly when their saturations agree.

### R018-L05 — one-step existential quotient lifting

For a fine relation `R : X → X → Prop`, define the induced quotient relation by existence of representatives.

Prove the exact one-step coarse reachable-support theorem when the input denotes a full quotient fibre/saturated support.

Keep this theorem separate from multi-step exactness.

### R018-L06 — strong completeness / fibre-successor criterion

Let `R_*` be relational support propagation.

Formalize the R017 strong completeness identity

`Sat q (R_* (Sat q A)) = Sat q (R_* A)`

for all `A`.

Prove an iff with the clean fibrewise condition that fine states in one `q`-fibre have the same coarse successor-support signature.

Use the weakest assumptions actually required.

### R018-L07 — finite-word repeated-saturation exactness

For a finite list/family of fine relations satisfying the L06 completeness condition generatorwise, prove by induction that inserting `Sat q` after every step does not change the final saturated reachable support relative to fine-conservative execution.

The theorem must be finite-word and result-support based; it need not preserve path multiplicity.

### R018-L08 — composition counterexample

Formalize a smallest practical finite counterexample in which two fine representatives merge into one intermediate quotient class and separate quotient relations compose to a coarse final result not produced by any valid fine two-step trajectory.

Also prove the direct quotient lift of the composed fine relation does not contain that spurious result.

This negative theorem is mandatory.

### R018-L09 — arithmetic sanity boundary

Formalize the square-gap example around `4 < n < 9` sufficiently to establish:

- `5` and `8` have the same square bracket;
- after `+1`, their brackets differ;
- hence `+1` does not descend as a deterministic operation through that bracket.

If the repository arithmetic API permits a clean proof without broad new infrastructure, also formalize the stronger general positive-translation obstruction from R017. Otherwise return that stronger arithmetic theorem as an explicit unformalized residue; do not weaken L01–L08.

## 3. Proof-integrity and build evidence

The proof-bearing declarations required above must contain no `sorry`, `admit`, custom `axiom`, or postulate used to close targets.

Include `#print axioms` or equivalent audit coverage for the core declarations.

Final acceptance evidence is the exact repository-pinned command:

`lake build --wfail -KCI EnterpriseMath`

A source-only candidate without that successful build remains formalization progress.

## 4. Return criteria

PASS only as:

`R017_CARRIER_CORE_LEAN_CHECKED / NO_SORRY / PINNED_BUILD_PASS / NOT_CANONICAL`

If the accepted R017 statement is false or missing a necessary hypothesis in Lean:

`THEOREM_SPEC_MISMATCH / RETURN_TO_R017_DRIVER_REVIEW`

If proof source advances but the final build is not successful:

`FORMALIZATION_PROGRESS / LEAN_BUILD_FAILED / CONTINUE_SAME_TASK / NO_PROMOTION`

Return a one-to-one map from R018-L01–L09 to exact declaration names and evidence.
