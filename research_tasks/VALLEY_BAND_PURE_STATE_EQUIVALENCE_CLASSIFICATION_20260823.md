<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-VALLEY-BAND-PURE-STATE-EQUIVALENCE-CLASSIFICATION",
  "title": "Valley-Band Factoring — Pure-State Equivalence and Root-Sieve Classification",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "VALLEY_STATE_RECURRENCE_CFRAC_EQUIVALENCE_AND_BAND_ROOT_SEMANTICS_CLASSIFIED",
  "next_action": "Independently formalize the closed (A,B,C) recurrence, determine its exact equivalence to continued-fraction or indefinite-form reduction, prove the full-band quadratic-root relation semantics, classify all exceptional cases, and map prior art without making a complexity claim.",
  "dependencies": [
    "research_inputs/VALLEY_BAND_PURE_STATE_AND_BENCHMARK_PACKET_20260823.md@f341b1347939e004e6d55c96e119c53337c0c9a0"
  ],
  "source_refs": [
    "research_inputs/VALLEY_BAND_PURE_STATE_AND_BENCHMARK_PACKET_20260823.md@f341b1347939e004e6d55c96e119c53337c0c9a0"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "factoring",
    "continued-fractions",
    "binary-quadratic-forms",
    "valley-state",
    "equivalence-classification",
    "root-sieve"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "VBSEQ",
  "origin_kind": "REPLAY_OR_INTEGRATION",
  "task_lineage": "REPLAY",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:9c1f03a5086432f83d1a3821893be5589124293bc5be5b14d4b7e196220271c7",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Valley-Band Factoring — Pure-State Equivalence and Root-Sieve Classification

Task-ID: `RS-VALLEY-BAND-PURE-STATE-EQUIVALENCE-CLASSIFICATION`

Intended owner branch:

`research/valley-band-pure-state-equivalence`

Hard target:

`VALLEY_STATE_RECURRENCE_CFRAC_EQUIVALENCE_AND_BAND_ROOT_SEMANTICS_CLASSIFIED`

## Context

A free factoring experiment rewrote a continued-fraction-guided process as a closed integer state `(A,B,C)` with invariant `C^2-AB=T`, then sieved quadratic values across whole semiconvergent-like bands.

The state recurrence may be a classical presentation of real indefinite binary quadratic-form reduction. The full-band factoring use may also overlap CFRAC or intermediate-convergent methods. Before performance work is interpreted, the exact mathematics and historical boundary must be settled.

This task is theorem and equivalence work. It does not compete on wall-clock speed.

## Parent-Chain Identity

Lineage is `REPLAY` from a targeted statement packet.

The parent chain is:

`USER DOWNWARD-COLLAPSE FACTORING DIRECTION -> PRIME BATCH DRIVER -> INDEPENDENT VALLEY-STATE CLASSIFIER`.

No source implementation or free-research worker identity is inherited. Runtime Researcher-ID allocation is external.

## Locked Source Package

Use:

`research_inputs/VALLEY_BAND_PURE_STATE_AND_BENCHMARK_PACKET_20260823.md@f341b1347939e004e6d55c96e119c53337c0c9a0`.

Do not use source prototypes or the source conversation. Independently author every derivation and checker.

External primary and authoritative mathematical sources may be consulted for the equivalence/prior-art classification, but they may not substitute for proving the exact recurrence and relation semantics stated in this packet.

## Previous Outputs

No prior taskbook has formally classified the pure state or the band-root factoring relation.

The source checkpoint's zero-mismatch step count and successful factorizations are empirical motivation only. They do not prove equivalence, correct initialization, or complete handling of exceptional states.

## Input Artifact Provenance

The packet is a statement extraction from GLOBAL_KNOWLEDGE checkpoint `96f685436622d8ce665f3f5acfcb715da8ab5d92`, with source code withheld.

It includes the candidate recurrence, band polynomial, validation instances, and claim boundaries. It does not include initialization code, sign conventions, relation bookkeeping, or prior-art conclusions beyond the warning that the recurrence may be classical.

## Exact Research Question

Give an exact theorem-level classification of the pure valley state and full-band root sieve.

The report must decide:

1. the admissible state space and initialization for odd nonsquare `T`;
2. the exact sign/orientation convention under which the stated quotient `a` is correct;
3. preservation of `C^2-AB=T` and the reduced-domain inequalities;
4. whether the state sequence is bijectively equivalent to a standard continued-fraction, reduced-ideal, or indefinite-form orbit;
5. the exact map in both directions, including terminal and ambiguous cases;
6. whether growing convergent numerators/denominators are mathematically unnecessary or merely omitted from one implementation;
7. the exact congruence-root structure of `D(t)` modulo every factor-base prime class;
8. how a smooth or partially smooth `D(t)` produces a verified square congruence modulo `N`;
9. the role of multiplier `M`, signs, square factors, and large-prime recombination;
10. the closest prior algorithms that already sieve intermediate or semiconvergent values.

Final classification must be one of:

- `EXACT_CLASSICAL_EQUIVALENCE_WITH_CLOSED_STATE_PRESENTATION`;
- `EQUIVALENT_ONLY_AFTER_HYPOTHESIS_OR_SIGN_REPAIR`;
- `STRICTLY_DIFFERENT_ORBIT_OR_BAND_OBJECT_PROVED`;
- `PARTIAL_EQUIVALENCE_WITH_UNRESOLVED_RELATION_SEMANTICS`;
- `MATERIAL_COUNTEREXAMPLE`.

## Scope Guard

### In scope

- real indefinite binary quadratic forms and reduction;
- continued fractions, complete quotients, ideals, and CFRAC relation generation;
- exact initialization and state transport maps;
- modular roots of `A*t^2+2*C*t+B` including ramified and degenerate cases;
- derivation of congruent-square relations modulo `N`;
- sign, multiplier, factor-base, and exponent-vector semantics;
- comparison with intermediate/semiconvergent sieving in the historical literature;
- exact-integer replay against an independently authored standard recurrence.

### Out of scope

- runtime superiority claims;
- pushing bit length as a substitute for proof;
- comparing against NFS or production QS performance;
- treating absence of stored `m,d` or convergents as proof of mathematical novelty;
- copying source code or preserving unexplained implementation conventions;
- calling the method subexponential or assigning a new complexity class.

Kill condition:

Any state convention that fails invariant preservation, misses a standard orbit step, creates an invalid relation, or requires an unstated sign flip must be repaired explicitly or rejected. Preserve the smallest exact failing state.

## Required Outputs

Produce:

1. Full report:
   `research_output/VALLEY_BAND_PURE_STATE_EQUIVALENCE_CLASSIFICATION_20260823.md`
2. Reducer result:
   `research_output/reducer_results/VALLEY_BAND_PURE_STATE_EQUIVALENCE_CLASSIFICATION_REDUCER_20260823.md`
3. Independent equivalence checker:
   `experiments/valley_band_pure_state_equivalence_checker.py`
4. State-map and exceptional-case table:
   `research_output/VALLEY_BAND_STATE_MAP_EXCEPTIONS_20260823.csv`
5. Prior-art map:
   `research_output/VALLEY_BAND_CFRAC_PRIOR_ART_MAP_20260823.md`
6. Evidence event stream:
   `research_output/evidence/VALLEY_BAND_PURE_STATE_EQUIVALENCE_CLASSIFICATION_20260823.jsonl`

The checker must implement both the candidate closed state and an independently authored standard reference orbit.

## Validation Standard

Required validation includes:

- symbolic invariant proof;
- a precise initialization theorem;
- explicit forward and reverse state maps for every retained equivalence claim;
- complete classification of zero, sign, ramification, and coefficient-degenerate cases;
- at least 100,000 exact paired orbit steps across the frozen 80-bit corpus with mismatch logging, not only a final pass flag;
- direct verification that every retained relation satisfies the claimed congruent-square identity modulo `N`;
- exhaustive modular-root comparison for all factor-base primes in a declared finite range;
- negative controls perturbing each recurrence sign and injecting an invalid band root;
- theorem-level citations for the closest prior form-reduction/CFRAC constructions.

Finite replay supports the map but cannot replace its proof.

## Evidence Policy

Separate algebraic proof, exact replay, relation verification, and prior-art evidence.

A classical-equivalence classification is a successful result, not a failure. Any claim of a residual new object must name the object independently of implementation syntax and identify a test distinguishing it from the closest classical construction.

## Reporting Requirements

Use the repository-standard six report sections and add:

- `State Convention Ledger`;
- `Initialization and Orbit Theorem`;
- `Forward/Reverse Equivalence Map`;
- `Band Root and Relation Semantics`;
- `Exceptional-State Catalogue`;
- `Prior-Art Equivalence Table`;
- `Final Classification`.

Freeze and stop after the independent classification. Performance benchmarking is assigned separately and may not be folded into this task.

## Repository Closure Protocol

Use the inherited repository closure protocol with no task-specific deviation. Promote the theorem report, reducer, checker, tables, prior-art map, and evidence stream together before archival.
