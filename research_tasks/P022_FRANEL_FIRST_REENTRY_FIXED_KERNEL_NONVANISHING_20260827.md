<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P022-FRANEL-FIRST-REENTRY-KERNEL-NONVANISHING",
  "title": "P022 Franel First-Reentry Fixed-Kernel Nonvanishing",
  "kind": "RESEARCH",
  "owner": "program/p022-geometry-v2",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Prove or refute all-parameter nonvanishing of the fixed truncated Franel kernel R_m(q) for the admissible twin-boundary constellation q=18m-1 with 12m-1 and 12m+1 prime, thereby deciding the sole arithmetic residue left by RR-8323CFDCB99F7832F51F.",
  "next_action": "Rewrite the fixed rational-parameter truncated 3F2 kernel as a finite-field hypergeometric or Jacobi-sum object, or construct a modular/Cartier realization, and derive a proof-level nonvanishing theorem or the smallest admissible zero witness. Use finite computation only to falsify proposed identities.",
  "dependencies": [
    "research_result_records/RS-P022-OBSERVATION-HISTORY/RR-8323CFDCB99F7832F51F.json",
    "research_returns/P022_OBSERVATION_HISTORY_ARITHMETIC_CORE_RETURN_20260827.md@blob:948893fadf1abcbdd80f8aa229e9d5698a9f00fa",
    "scripts/check_p022_observation_history_arithmetic_core.py@blob:7d41ab81d34e7adbefffe0269ac6947833a820a0"
  ],
  "source_refs": [
    "research_returns/P022_OBSERVATION_HISTORY_ARITHMETIC_CORE_RETURN_20260827.md",
    "research_artifacts/P022_OBSERVATION_HISTORY_ARITHMETIC_CORE/boundary_census_q_lt_50000.json",
    "research_artifacts/P022_OBSERVATION_HISTORY_ARITHMETIC_CORE/driver_audit_q_lt_200000_20260827.json"
  ],
  "evidence_status": "DRIVER_ACCEPTED_EXACT_REDUCTION / ALL_M_FIXED_KERNEL_NONVANISHING_OPEN",
  "last_progress_ref": "main@bbdea1ae2858b861ce0d8e2c1596e1aacfe972c0",
  "last_progress_at": "2026-08-27T11:44:00+00:00",
  "hard_block": null,
  "tags": [
    "P022",
    "Franel",
    "finite-field-hypergeometric",
    "Jacobi-sum",
    "Cartier",
    "nonvanishing"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P022-FRANEL-FIRST-REENTRY-KERNEL-NONVANISHING",
  "parent_objective_id": "P022_OBSERVATION_HISTORY_IDENTIFIABILITY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P022KERN",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P022-OBSERVATION-HISTORY",
  "successor_gate": {
    "new_information_gap": "The accepted parent result reduces the first dangerous boundary exactly to nonvanishing of one fixed rational-parameter truncated kernel, but does not decide that nonvanishing for all admissible m.",
    "why_parent_result_does_not_close_it": "RR-8323 proves the equivalence, q-adic unit structure, and failure of one finite terminating-transform orbit; it explicitly leaves R_m(q) congruent to zero or nonzero undecided in general.",
    "discriminating_outcomes": [
      "A proof that R_m(q) is nonzero modulo q for every admissible twin-boundary m closes the q=3r-1 escape.",
      "One admissible m with R_m(q) equal to zero refutes universal nonvanishing and freezes an exact exceptional family or witness.",
      "A proof that the kernel equals a named finite-field or modular invariant but remains conditionally nonzero sharply relocates the blocker."
    ],
    "kill_condition": "Kill any route that only enlarges the finite census, assumes generic hypergeometric nonvanishing, or treats exhaustion of the coded 12-type transform orbit as exhaustion of all transformations.",
    "alternative_route_or_free_exploration_considered": "Closure without continuation was rejected because the fixed kernel is the sole load-bearing residue. The sibling composite equal-depth route is separately rebound, and free exploration remains available outside this typed arithmetic task.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The legacy task id contains several unrelated P022 subfrontiers and has been single-valued operationally. A typed task isolates the exact kernel, prevents further claim collisions, and gives a falsifiable source boundary."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:497a0467870c4d495d4dbf161cf492e9d3d4a51d0a7b34e685086f25daa395f4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P022 Franel First-Reentry Fixed-Kernel Nonvanishing

Status: `PUBLISHED_REGISTERED / CONTINUATION / TYPED_P022_ARITHMETIC_FRONTIER`

## Mother question

At the first dangerous primitive-twin Franel boundary, write

\[
r=6m,\qquad q=18m-1,
\]

with `q`, `12m-1`, and `12m+1` prime. The accepted parent result proves that the remaining escape is equivalent to vanishing modulo `q` of the fixed truncated kernel

\[
R_m(q)=\sum_{j=0}^{3m}
\frac{(-1/6)_j^3}{(1/2)_j(-1/2)_j\,j!}.
\]

Decide whether `R_m(q)` is nonzero for every admissible `m`, or produce and classify an admissible zero.

## Frozen inputs and scope

The exact normalization, the equivalence with the integer kernel and `F_(6m)`, the q-adic unit property of every summand, and the 12-type audit of the stated terminating-transform closure may be consumed from `RR-8323CFDCB99F7832F51F`.

The preferred proof routes are finite-field hypergeometric functions, Jacobi or Gauss sums, modular forms, Cartier operators, or another exact arithmetic/geometric realization of this fixed kernel. A different exact route is allowed if it preserves the admissible twin-boundary hypotheses.

Finite scans may test candidate identities or find a counterexample. They are not proof of all-parameter nonvanishing.

## Hard target and required outputs

Hard target:

`P022_FIXED_TRUNCATED_FRANEL_KERNEL_ALL_M_NONVANISHING_PROVED_OR_REFUTED`

Required outputs:

1. an exact finite-field, modular, Cartier, or equivalent interpretation of `R_m(q)`, or a proof that a proposed interpretation is false;
2. a proof of nonvanishing for every admissible `m`, or the smallest verified admissible zero and its exact mechanism;
3. an explicit reconnection to `q | F_(6m)` and the P022 first-reentry visibility question;
4. exact computation only as falsification or regression, separated from proof;
5. a frozen return that states whether the q=3r-1 boundary closes, fails, or reduces to a strictly smaller named invariant.

## Research value to preserve

The parent work has already compressed a large P022 branch to one fixed rational-parameter object. Solving this task would decide the first dangerous re-entry boundary rather than merely increasing a determinant or prime cutoff. A negative result is equally valuable if it gives a genuine admissible zero or a structurally defined exceptional class.

## Success, kill, and return criteria

Success is either a proof that `R_m(q)` never vanishes in the admissible constellation, or a verified admissible zero with an exact explanation.

Kill a proposed proof if it uses only the absence of zeros below a numerical cutoff, assumes a generic nonvanishing theorem not proved under the present parameters, drops the twin-boundary prime hypotheses, or promotes the finite 12-type transform audit into a universal transformation theorem.

If the best exact route reduces `R_m(q)` to a smaller established invariant whose nonvanishing is independently open, freeze that precise invariant and stop this task at the corresponding exact reduction.
