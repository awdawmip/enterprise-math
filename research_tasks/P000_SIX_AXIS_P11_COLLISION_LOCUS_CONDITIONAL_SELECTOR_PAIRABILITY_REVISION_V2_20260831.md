<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-SIX-AXIS-P11-COLLISION-LOCUS-CONDITIONAL-SELECTOR",
  "title": "P000 six-axis P11 admissible collision locus and conditional selector revision V2",
  "kind": "RESEARCH",
  "owner": "research/p000-six-axis-p11-collision-locus-conditional-selector",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Generation 1 correctly classified the combinatorial equal-P11 S3 collision equations and quadratic second-moment resolvents, but Driver review found that it omitted the frozen integer-pairability filter when identifying the exact admissible two-orbit fibre. The mathematical revision is to intersect the algebraic C1/C2 collision classes with pairability of both candidate packets and correct the conditional information law.",
  "next_action": "Preserve the validated C1/C2 and Gram/Vandermonde algebra, classify the exact pairability-filtered admissible two-orbit locus, prove how the algebraic resolvent roots are filtered by admissibility, and re-freeze the selector cost as log2 of the admissible fibre with the mandatory one-branch collision counterexample regression.",
  "dependencies": [
    "RR-B96585874709743F94BC",
    "RR-C3E71A9D4B6052F88E21",
    "DR-C5539B165E52AAAA3C6A"
  ],
  "source_refs": [
    "research_result_records/RS-P000-SIX-AXIS-MIXED-INVARIANT-ALIGNMENT-COMPRESSION/RR-B96585874709743F94BC.json",
    "research_result_records/RS-P000-SIX-AXIS-P11-COLLISION-LOCUS-CONDITIONAL-SELECTOR/RR-C3E71A9D4B6052F88E21.json",
    "driver_reviews/P000_SIX_AXIS_P11_COLLISION_LOCUS_CONDITIONAL_SELECTOR_DRIVER_REVIEW_20260831.md"
  ],
  "evidence_status": "GEN1_REQUEST_REVISION / COMBINATORIAL_COLLISION_AND_RESOLVENT_PAYLOAD_RETAINED / ADMISSIBLE_PAIRABILITY_FILTER_REQUIRED",
  "hard_block": null,
  "tags": [
    "P000",
    "six-axis",
    "P11",
    "pairability",
    "collision-locus",
    "resolvent",
    "conditional-selector",
    "revision-v2"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-SIX-AXIS-P11-COLLISION-LOCUS-CONDITIONAL-SELECTOR",
  "parent_objective_id": "OBJ-P000-SIX-AXIS-ARITHMETIC-TROPICAL-INTEGRATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000P11C2",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P000-SIX-AXIS-MIXED-INVARIANT-ALIGNMENT-COMPRESSION",
  "successor_gate": {
    "new_information_gap": "Generation 1 proved the algebraic equal-P11 assignment locus but did not classify the taskbook's admissible two-orbit fibre after applying the integer-pairability gate to both candidate alignments. The exact pairability-filtered locus and corrected conditional information law remain open.",
    "why_parent_result_does_not_close_it": "RR-C3E71A9D4B6052F88E21 treats C1/C2 algebraic collisions as two admissible states. Driver counterexample H={-2,0,2}, T={-1,0,1}, P11=+/-2 has only one admissible packet on each algebraic double level, so the terminal theorem and checker require a mathematical correction rather than closure.",
    "discriminating_outcomes": [
      "the admissible two-orbit locus is exactly C1/C2 plus explicit pairability of both branches, and the selector cost is 1 bit only there",
      "the pairability intersection simplifies to a stronger exact Diophantine criterion with the same 0-or-1 admissible-fibre law",
      "pairability exposes an additional obstruction to the claimed two-root lossless selector, requiring a narrower exact result"
    ],
    "kill_condition": "Do not enlarge the mixed-moment grammar, introduce higher moments after outcomes, infer native orientation, select the Pfaffian negative slot, reduce P000 dimension, claim factorization, or enter Full-Cell dynamics. Stop at the exact pairability-filtered arithmetic theorem or a frozen exact obstruction.",
    "alternative_route_or_free_exploration_considered": "The algebraic C1/C2 and resolvent route is already validated and the defect is localized to the admissibility gate; restarting from a different route or free exploration would discard useful exact structure without discriminating the identified falsifier.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The stable Task-ID is preserved and this is an explicit superseding revision generation. Closure is invalid because the admissible-fibre theorem is falsified; a new unrelated Task-ID would conceal rather than repair the same mother question."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P000 six-axis P11 admissible collision locus and conditional selector revision V2

## Mother question

Given the accepted derived marginals `H={h0,h1,h2}`, `T={t0,t1,t2}` and `P11=sum_i h_i t_i`, classify the exact residual **admissible** aligned packet fibre after imposing the frozen integer-pairability gate on every `(h,t)` pair. In particular, determine exactly when an algebraic `C1` or `C2` equal-`P11` level contains two admissible `K/Gamma` packets rather than one, and freeze the minimum conditional selector information as a function of that admissible fibre.

## Frozen inputs and scope

Freeze parent accepted Result `RR-B96585874709743F94BC` and retain from Generation 1 Result `RR-C3E71A9D4B6052F88E21` only the payload explicitly preserved by Driver review `DR-C5539B165E52AAAA3C6A`:

- on fully distinct sorted marginals with gaps `A=h1-h0`, `B=h2-h1`, `C=t1-t0`, `D=t2-t1`, the only **combinatorial** equal-`P11` classes are `C1: AC=BD` for `132/213` and `C2: AD=BC` for `231/312`;
- repeated marginal strata are combinatorially `P11`-injective;
- simultaneous `C1+C2` gives two separate algebraic double levels, never a triple level;
- the Gram/Vandermonde `P21` and `P12` quadratics are valid algebraic candidate resolvents;
- on a genuine two-admissible-branch collision, `P21/P12` root-order bits are SAME on `C1` and OPPOSITE on `C2`;
- the positive `B=6` two-branch pairable witnesses and scaling families remain regression requirements.

The frozen admissibility gate is exact:

`PAIRABLE(h,t) iff Delta=h^2-4t is a nonnegative perfect square and sqrt(Delta) congruent h (mod 2)`.

Generation 2 must distinguish

`ALGEBRAIC_P11_COLLISION_LOCUS != ADMISSIBLE_TWO_ORBIT_LOCUS`.

Allowed alignment-sensitive quantities remain `P11`, `P21`, `P12`; no higher mixed moment may be added. Symmetric polynomial/rational combinations of already-known marginal data remain allowed. All conclusions remain a derived six-coordinate arithmetic facade.

## Hard target and required outputs

Hard target:

`P000_P11_PAIRABILITY_FILTERED_ADMISSIBLE_COLLISION_LOCUS_AND_CONDITIONAL_SELECTOR_EXACTLY_CLASSIFIED_OR_FROZEN_RESOLVENT_ROUTE_OBSTRUCTED`.

Required outputs:

1. preserve and restate `C1`/`C2` only as the exact combinatorial equal-`P11` equations;
2. derive an exact necessary-and-sufficient criterion for a **two-admissible-orbit** fibre by imposing pairability on every pair in both colliding packets; give either the explicit discriminant-square/parity system or an exactly equivalent simplified Diophantine form;
3. classify all algebraic collision levels into `ZERO_ADMISSIBLE`, `ONE_ADMISSIBLE`, or `TWO_ADMISSIBLE` candidate packets, noting that valid task inputs have at least one admissible packet;
4. prove repeated-`H`/repeated-`T` admissible strata remain one-orbit whenever valid;
5. retain the Gram/Vandermonde quadratics as algebraic candidate resolvents and prove that, on a one-admissible algebraic collision, the nonadmissible quadratic root reconstructs a packet that fails the frozen pairability gate; on a two-admissible collision the two roots reconstruct exactly the two admissible packets;
6. define the selector from the pairability-filtered candidate set and prove exact side-information cost `log2 |F_adm(H,T,P11)|`: `0` bits for an admissible singleton and `1` bit exactly for an admissible doubleton, with no separate collision flag;
7. include the mandatory Driver falsifier regression `H={-2,0,2}`, `T={-1,0,1}`: at `P11=2` only `213` is admissible, and at `P11=-2` only `312` is admissible;
8. add a deterministic pairability-filtered exhaustive control that directly computes admissible fibres and confirms no admissible fibre exceeds two;
9. preserve the `B=6` genuine two-admissible-branch `C1` and `C2` witnesses, their minimality in the frozen root-box metric, scaling families, and SAME/OPPOSITE `P21/P12` branch relation;
10. audit whether both algebraic collision equations can hold while the two doubled levels have different admissible cardinalities, and state the exact selector behavior per level;
11. preserve classical attribution for assignment geometry, Vandermonde/Gram elimination, symmetric/multisymmetric invariant theory, and make no historical novelty claim;
12. supply a NEW immutable Result with a fresh execution identity, fresh Result-ID, exact checker/certificate, and complete Git blob SHA-1 plus SHA-256 output bindings.

## Research value to preserve

Generation 1 uncovered a sharp algebraic structure: only two equal-`P11` collision equations exist, and a quadratic second-moment resolvent captures their two algebraic branches. The revision should not discard that structure. It must connect it correctly to the original integer-pairable arithmetic state space. This decides whether the practical information residue is a conditional bit only on genuinely pairable doubletons, and prevents algebraic ghost branches from being counted as physical/derived admissible states.

## Success, kill, and return criteria

Terminal success is one of:

- `EXACT_PAIRABILITY_FILTERED_COLLISION_LOCUS_WITH_ONE_BIT_ONLY_ON_ADMISSIBLE_DOUBLETONS`;
- `EXACT_PAIRABILITY_FILTERED_LOCUS_WITH_SIMPLIFIED_DIOPHANTINE_CRITERION`;
- `FROZEN_RESOLVENT_ROUTE_OBSTRUCTED_AFTER_PAIRABILITY_FILTER_WITH_EXACT_COUNTEREXAMPLE`.

A successful Return must explicitly reconcile every retained Generation-1 claim with the pairability filter and identify any corrected statement. The old Result remains immutable history and may not be overwritten. Use a fresh Researcher identity/execution and NEW Result-ID.

Kill any attempt to reinterpret the selector bit as native orientation or Pfaffian negative-slot choice, to infer native dimension reduction, factorization, Full-Cell dynamics, or to enlarge the invariant grammar after failures. The Researcher lane makes no downstream task decision after returning the revised Result.
