<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-THIRD-SECTOR-FACTOR-PHASE-INDEPENDENT-RECONSTRUCTION",
  "title": "Third-Sector Factor Phase — Independent Two-Square Bridge Reconstruction",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "THIRD_SECTOR_FACTOR_PHASE_BRIDGE_INDEPENDENTLY_RECONSTRUCTED_OR_REFUTED",
  "next_action": "Using only the blind 2+1 overlay packet, independently derive or refute the factor-fiber classification, exact square-cell parameterization, scale bridge, recursive generator, and reverse factor recovery from two primitive additive states.",
  "dependencies": [
    "research_inputs/THIRD_SECTOR_FACTOR_PHASE_BLIND_RECONSTRUCTION_PACKET_20260823.md@87f32a3df7625b76a85944769be82f44e122bc7e"
  ],
  "source_refs": [
    "research_inputs/THIRD_SECTOR_FACTOR_PHASE_BLIND_RECONSTRUCTION_PACKET_20260823.md@87f32a3df7625b76a85944769be82f44e122bc7e"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "prime",
    "third-sector",
    "factor-fiber",
    "sum-of-two-squares",
    "gaussian-integers",
    "independent-reconstruction"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "TSFPR",
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

# Third-Sector Factor Phase — Independent Two-Square Bridge Reconstruction

Task-ID: `RS-THIRD-SECTOR-FACTOR-PHASE-INDEPENDENT-RECONSTRUCTION`

Intended owner branch:

`research/third-sector-factor-phase-independent-reconstruction`

Hard target:

`THIRD_SECTOR_FACTOR_PHASE_BRIDGE_INDEPENDENTLY_RECONSTRUCTED_OR_REFUTED`

## Context

A free-research experiment proposed a 2+1 arithmetic overlay: two additive square-sum channels and one auxiliary multiplicative factor channel. The elementary factor fiber is straightforward, but the source report claims a substantially stronger bidirectional relation between factor choices and all nonnegative two-square cells.

The source formulas and source checker are withheld. This task must independently determine whether the complete bridge exists, what quotient and normalization make it exact, and which parts are merely classical Gaussian factorization in spatial notation.

## Parent-Chain Identity

Lineage is `REPLAY` from a blind primitive packet.

The parent chain is:

`USER THIRD-SECTOR PROPOSAL -> PRIME BATCH DRIVER -> INDEPENDENT FACTOR-PHASE RECONSTRUCTION`.

No source worker identity or source formula is inherited. Runtime Researcher-ID allocation is external.

## Locked Source Package

Read and execute only:

`research_inputs/THIRD_SECTOR_FACTOR_PHASE_BLIND_RECONSTRUCTION_PACKET_20260823.md@87f32a3df7625b76a85944769be82f44e122bc7e`.

Before the independent return is frozen, do not read or search for the GLOBAL_KNOWLEDGE third-sector event, source conversation, source formulas, source enumeration ranges, or any task/result derived from them.

Classical theorems may be reconstructed and cited, but the researcher must derive the exact quotient, scale formula, generator, and reverse recovery independently rather than locating the withheld source statement.

## Previous Outputs

No prior taskbook output is admitted.

The elementary two-square theorem, Gaussian unique factorization, and composition identity are classical prerequisites that may be independently invoked with exact citations. They do not by themselves prove the overlay-specific forward and reverse bridges.

## Input Artifact Provenance

The packet preserves only the primitive additive and multiplicative fibers and the questions to be answered. It intentionally removes every outcome-bearing source formula.

The withheld comparison source is frozen in GLOBAL_KNOWLEDGE, but its content is not an input to this replay.

## Exact Research Question

Determine whether there is an exact, complete, and bidirectional factor-phase description of nonnegative two-square cells compatible with the third-sector multiplicative fiber.

The task must independently classify:

1. prime/composite/square/fiber-cardinality/least-factor readouts;
2. the exact factorization criterion for two-square existence;
3. the correct factor object controlling all square cells;
4. the quotient by swap, conjugation, unit action, and any global reflection;
5. the exact count of unordered nonnegative square cells, including fixed-point corrections;
6. the common-scale formula for `gcd(a,b)`;
7. a factor-driven generator that is sound and complete;
8. reverse recovery of complementary factors from two distinct primitive cells;
9. all parity, `2`-adic, prime-power, repeated-representation, and nonprimitive failure modes.

Assign one final classification:

- `FULL_BIDIRECTIONAL_BRIDGE_INDEPENDENTLY_RECONSTRUCTED`;
- `FORWARD_BIJECTION_ONLY`;
- `EXACT_AFTER_SCOPE_OR_QUOTIENT_REPAIR`;
- `PARTIAL_CLASSICAL_REPACKAGING`;
- `MATERIAL_COUNTEREXAMPLE`;
- `OPEN_AFTER_CERTIFIED_PARTIAL_PROGRESS`.

The hard target requires an exact verdict on both the forward parameterization and the reverse two-state recovery.

## Scope Guard

### In scope

- ordered and unordered multiplicative fibers;
- ordered, unordered, sign-quotiented, and unit/conjugation-quotiented square representations, with explicit transitions between them;
- Gaussian-integer factorization reconstructed independently;
- split/inert/ramified prime exponent bookkeeping;
- exact counting formulas and fixed-point analysis;
- primitive versus imprimitive square cells;
- factor-driven generation and direct-enumeration comparison;
- bilinear gcd recovery from two primitive representations;
- classification of the spatial overlay as a presentation, computational index, or stronger structure.

### Out of scope

- declaring the auxiliary multiplicative readout a native metric or native sector semantics;
- claiming Fermat's two-square theorem, Gaussian factorization, or Brahmagupta-Fibonacci composition as new;
- treating a finite zero-mismatch range as proof of bijection or completeness;
- importing the source formulas before freeze;
- using a factorization oracle inside the purported factor-recovery algorithm without disclosing it;
- conflating two representations related only by signs, swap, or conjugation.

Kill condition:

If any purported bijection is noninjective or nonsurjective after the declared quotient, or if the reverse gcd rule fails on one valid primitive pair, preserve the smallest exact counterexample and narrow or reject the corresponding claim.

## Required Outputs

Produce:

1. Full report:
   `research_output/THIRD_SECTOR_FACTOR_PHASE_INDEPENDENT_RECONSTRUCTION_20260823.md`
2. Reducer result:
   `research_output/reducer_results/THIRD_SECTOR_FACTOR_PHASE_INDEPENDENT_RECONSTRUCTION_REDUCER_20260823.md`
3. Independent exact checker:
   `experiments/third_sector_factor_phase_independent_checker.py`
4. Normalized forward/reverse test corpus:
   `research_output/THIRD_SECTOR_FACTOR_PHASE_TEST_CORPUS_20260823.csv`
5. Theorem and quotient dictionary:
   `research_output/THIRD_SECTOR_FACTOR_PHASE_QUOTIENT_DICTIONARY_20260823.md`
6. Evidence event stream:
   `research_output/evidence/THIRD_SECTOR_FACTOR_PHASE_INDEPENDENT_RECONSTRUCTION_20260823.jsonl`

The checker must keep direct enumeration, factor-driven generation, and reverse recovery as separate modules.

## Validation Standard

Required validation includes:

- a self-contained proof of every retained formula;
- explicit unit, conjugation, swap, ordering, parity, and primitivity conventions;
- proof of injectivity and surjectivity for the forward map;
- proof of soundness and completeness for the recursive generator;
- proof or exact counterexample for reverse factor recovery;
- direct-versus-factor-driven checking on a declared range containing every required degenerate class;
- separate checking of all primitive representation pairs on a declared range;
- negative controls removing the `2`-adic normalization and admitting an odd inert-prime exponent;
- normalized hashes of all generated cell sets so equality is not judged visually.

The report must distinguish existence, counting, parameterization, generation, and reverse recovery. Success on one layer does not certify the next.

## Evidence Policy

Keep classical theorem evidence, independently derived overlay theorems, finite exact checks, and post-freeze source comparison separate.

The overlay may be classified as an exact presentation even when every arithmetic ingredient is classical. Historical novelty is not part of this task's success criterion.

## Reporting Requirements

Use the repository-standard six report sections and add:

- `Quotient and Convention Ledger`;
- `Forward Bijection`;
- `Scale/Shape Bridge`;
- `Factor-Driven Generator`;
- `Reverse Two-State Recovery`;
- `Degenerate and Failure Cases`;
- `Classical Boundary`;
- `Final Classification`.

Freeze the report before source comparison and stop. The Driver will later compare the independent theorem package with the withheld source event.

## Repository Closure Protocol

Use the inherited repository closure protocol with no task-specific deviation. Promote the full proof, reducer, checker, corpus, quotient dictionary, and evidence stream together before archival.
