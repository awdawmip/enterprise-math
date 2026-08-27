<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P022-HASSE-MIDPOINT-FIRST-JET-COMPATIBILITY",
  "title": "P022 Hasse-Midpoint First-Jet Compatibility",
  "kind": "RESEARCH",
  "owner": "program/p022-geometry-v2",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Classify the joint first-jet status of the scalar-Hasse quotient jet W_p and the forced-midpoint jet J_p=2C_p-3U_p on the surviving P022 composite equal-depth locus.",
  "next_action": "Derive an exact arithmetic relation or obstruction between W_p and J_p under the admissible scalar-Hasse and earlier-escape hypotheses; prove first-order incompatibility or freeze the smallest admissible simple-simple or double-deep witness.",
  "dependencies": [
    "research_result_records/RS-P022-COMPOSITE-FRANEL-EQUAL-DEPTH-ESCAPE/RR-B8672BDFC2C7814E4EE8.json",
    "research_task_records/RS-P022-COMPOSITE-FRANEL-EQUAL-DEPTH-ESCAPE/TP2-E4537008BB8B0CCFF88F.json",
    "program/p022-geometry-v2@603ef1c72245612359f8b59cab7a492de21a9166"
  ],
  "source_refs": [
    "research_returns/P022_COMPOSITE_FRANEL_EQUAL_DEPTH_ESCAPE_RETURN_20260827.md@blob:803098821d267ffd2ce90cf4894e3f340826fe83",
    "src/enterprise_math/p022_barlow_forced_midpoint_scale_hasse.py@program/p022-geometry-v2",
    "src/enterprise_math/p022_barlow_franel_midpoint_harmonic_pairing.py@program/p022-geometry-v2",
    "src/enterprise_math/p022_barlow_franel_third_index_minus_hasse.py@program/p022-geometry-v2"
  ],
  "evidence_status": "ACCEPTED_PARENT_EXACT_FIRST_JET_REDUCTION / JOINT_COMPATIBILITY_OPEN",
  "last_progress_ref": "RR-B8672BDFC2C7814E4EE8",
  "last_progress_at": "2026-08-27T15:03:07+00:00",
  "hard_block": null,
  "tags": [
    "P022",
    "Franel",
    "Hasse",
    "p-adic",
    "first-jet",
    "compatibility",
    "identifiability"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P022-HASSE-MIDPOINT-FIRST-JET-COMPATIBILITY",
  "parent_objective_id": "P022_OBSERVATION_HISTORY_IDENTIFIABILITY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P022JET",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P022-COMPOSITE-FRANEL-EQUAL-DEPTH-ESCAPE",
  "successor_gate": {
    "new_information_gap": "The accepted parent result gives exact separate first-jet tests for the third-minus depth and forced-midpoint depth, but no theorem currently determines whether W_p and J_p=2C_p-3U_p can be simultaneously nonzero, exactly-one-zero, or simultaneously zero under the admissible P022 hypotheses.",
    "why_parent_result_does_not_close_it": "The parent task proves the p^2 midpoint correction and the first-jet trichotomy only. It neither excludes the simple-simple equal-depth locus nor proves or refutes nonemptiness of the double-deep locus.",
    "discriminating_outcomes": [
      "An exact relation forces exactly one of W_p and J_p to vanish on every admissible scalar-Hasse prime, closing this equal-depth escape channel at first order.",
      "An admissible prime satisfying the already-frozen earlier-escape hypotheses has W_p nonzero and J_p nonzero, freezing a concrete simple-simple equal-depth witness.",
      "A proof or exact admissible witness establishes W_p=J_p=0, certifying nonemptiness of the double-deep locus and making a later second-jet comparison mathematically justified."
    ],
    "kill_condition": "Kill any route that only increases a numerical cutoff, assumes generic p-adic independence, drops the earlier-escape or admissibility hypotheses, merely renames the same two jets without a new relation, or begins second-jet mathematics before double-deep nonemptiness is established.",
    "alternative_route_or_free_exploration_considered": "The live legacy P022 first-reentry route was checked and concerns the distinct q=3r-1 Hahn/conductor-18 boundary. Free exploration or another owner would not remove the need to decide this already-isolated first-order compatibility question, while closing the route now would leave two falsifiably different first-jet outcomes unresolved.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent task reached its authorized exact-blocker stopping point. A new narrow task prevents the broad composite Franel problem from being reopened, isolates one joint-status question, and forbids premature second-jet expansion."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:497a0467870c4d495d4dbf161cf492e9d3d4a51d0a7b34e685086f25daa395f4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P022 Hasse-Midpoint First-Jet Compatibility

Status: `PUBLISHED_REGISTERED / CONTINUATION / TYPED_P022_ARITHMETIC_FRONTIER`

## Mother question

The accepted parent result reduces the surviving composite equal-depth mechanism to two exact first-jet tests at a target prime

\[
p=6k-1,\qquad m=(p-1)/2,\qquad n=2k-1.
\]

On the scalar-Hasse locus

\[
P_p(1)=0,
\]

put

\[
W_p:=2^{-n}F_n/p\pmod p
\]

and

\[
J_p:=2C_p-3U_p
\equiv 2F_m/p\pmod p.
\]

The equal-depth escape survives at first order when both jets are nonzero, dies immediately when exactly one vanishes, and enters a genuinely deeper branch only when both vanish.

Determine the exact joint-status law for \(W_p\) and \(J_p\) under the admissible P022 hypotheses and the already-frozen earlier-escape conditions.

## Frozen inputs and scope

Consume `RR-B8672BDFC2C7814E4EE8` at its accepted strength only. In particular, the forced-midpoint mod-\(p^2\) correction, the harmonic pairing \(U_p=2T_p\), the Whipple mod-\(p\) scalar-Hasse zero bridge, and the first-jet trichotomy are frozen inputs.

The task is restricted to first-order compatibility between \(W_p\) and \(J_p\). It does not reopen the broad composite Franel route, the separate first-reentry Hahn boundary, or any bounded midpoint census.

A useful route may pass through finite-field hypergeometric/Jacobi-sum structure, Cartier/Frobenius structure, an exact Hasse-period quotient relation, recurrence transfer, or another exact arithmetic realization. The target is a relation between the two jets, not a larger numerical search.

Do not compute a second p-adic jet merely because the double-deep case is logically possible. Higher-order work becomes justified only after this task proves or freezes nonemptiness of the double-deep locus.

## Hard target and required outputs

Hard target:

`P022_HASSE_MIDPOINT_FIRST_JET_COMPATIBILITY_CLASSIFIED_OR_ADMISSIBLE_WITNESS_FROZEN`

Required outputs:

1. derive an exact relation, obstruction, or equivalence connecting \(W_p\) and \(J_p\) on the admissible scalar-Hasse locus;
2. determine which of the joint patterns
   \[
   (\ne0,\ne0),\quad (0,\ne0),\quad (\ne0,0),\quad (0,0)
   \]
   can occur under the full frozen P022 hypotheses;
3. if the simple-simple pattern occurs, freeze the smallest exact admissible witness and reconnect it to the equal-depth escape;
4. if the double-deep pattern is proved nonempty, freeze the theorem or exact witness and stop at that boundary rather than beginning the second-jet comparison inside this task;
5. if first-order incompatibility kills all equal-depth patterns, reconnect the conclusion to composite-defect row visibility;
6. keep finite regression or search evidence explicitly separate from proof-level conclusions.

## Research value to preserve

The parent route has already compressed a vague valuation-equality problem to two scalar first jets. This task decides whether those jets actually interact.

A first-order incompatibility would close an independent P022 escape channel. A simple-simple witness would refute universal first-order escape closure with an explicit arithmetic exception. A double-deep witness would establish, for the first time, that higher p-adic comparison is genuinely necessary rather than merely logically conceivable.

Any of these outcomes is materially more informative than another cutoff extension.

## Success, kill, and return criteria

Success is one of the following:

- a proof that the admissible hypotheses force a joint status incompatible with equal positive depths;
- an exact admissible simple-simple witness with \(W_p\ne0\) and \(J_p\ne0\);
- a proof or exact admissible witness that \(W_p=J_p=0\), thereby certifying a nonempty double-deep locus;
- a complete exact classification of the possible first-jet patterns.

Kill a proposed route if it only raises a finite cutoff, imports an unproved generic independence heuristic, drops a frozen admissibility or earlier-escape condition, merely reparameterizes \(W_p\) and \(J_p\) without creating a new relation, or starts second-jet analysis before double-deep nonemptiness is established.

Return the strongest exact theorem, obstruction, or witness separately from any finite regression. If the double-deep locus is certified nonempty, stop there and identify the precise higher-order quantity a later task would need to compare.
