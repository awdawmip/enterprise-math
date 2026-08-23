<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PRIME-FUSION-INDEPENDENT-REPLICATION",
  "title": "Prime Fusion — Blind Independent Structural Replication",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "PRIME_FUSION_CORE_INDEPENDENTLY_RECONSTRUCTED_OR_REFUTED",
  "next_action": "Using only the frozen blind replication packet before return freeze, independently classify the two supplied quadratic readouts, construct or refute any natural finite carrier/recovery mechanism, classify local prime and adjacency structure, write an independent exact-integer checker, freeze the return, and stop before source-package comparison.",
  "dependencies": [
    "research_inputs/PRIME_FUSION_BLIND_INDEPENDENT_REPLICATION_PACKET_20260823.md@096d7f4f3a6347b79bee58ae0973cea518780efa"
  ],
  "source_refs": [
    "research_inputs/PRIME_FUSION_BLIND_INDEPENDENT_REPLICATION_PACKET_20260823.md@096d7f4f3a6347b79bee58ae0973cea518780efa",
    "definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md@88d86e2146c01cbe7a62432e9488b2b4621ec9fa"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "prime-fusion",
    "blind-replay",
    "independent-replication",
    "sector-S12",
    "exact-integer",
    "counterexample-search"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "PFREP",
  "origin_kind": "REPLAY_OR_INTEGRATION",
  "task_lineage": "REPLAY",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:d5cbe89c8620ca6efa2af5219900424485c85bba1fc042576e17034c10e38299",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Prime Fusion — Blind Independent Structural Replication

Task-ID: `RS-PRIME-FUSION-INDEPENDENT-REPLICATION`

Origin: `REPLAY_OR_INTEGRATION`

Lineage: `REPLAY`

Identity lane: `PFREP`

Intended owner branch:

`research/prime-fusion-independent-replication`

## 0. Clean-context information boundary

This task is a clean independent replay of a previously generated free-research object. It is **not** a continuation of the source researcher's derivation.

Before freezing the independent return, read only:

`research_inputs/PRIME_FUSION_BLIND_INDEPENDENT_REPLICATION_PACKET_20260823.md`

at source:

`096d7f4f3a6347b79bee58ae0973cea518780efa`,

plus the exact primitive spatial definition named by that packet if needed.

Do not open any theorem package, source-run checker, PR discussion, Driver comparison, journal summary, source-research conversation, or search result that reveals the withheld source conclusions before return freeze.

If this boundary is violated, continue only if useful, but mark the result non-clean; it cannot count as independent replication evidence.

## 1. Mother question

Starting only from the primitive one-sector substrate and the two raw quadratic readouts supplied in the blind packet, determine the strongest exact finite/algebraic/number-theoretic structure that is independently reconstructible, and actively try to refute every proposed structure.

Hard target:

`PRIME_FUSION_CORE_INDEPENDENTLY_RECONSTRUCTED_OR_REFUTED`.

The task does not require convergence to any hidden theorem list. A materially different exact structure, a partial reconstruction, or a counterexample is valid evidence.

## 2. Required work

Execute the blind packet's R1–R6 questions from the supplied object itself.

At minimum the return must classify:

- exact relations and coordinate recoverability for the two readouts;
- existence or obstruction of a natural unified finite carrier/quotient and the information lost under scalarization;
- prime-modulus direction/root classes and fixed-slice root counts;
- forced congruence/reciprocity relations for simultaneous-prime cells, if any;
- the one-sector nearest-neighbor graph and any uniform component-size bound, including small-prime exceptions;
- any exact finite modular dimensional-reduction/mean identity that survives proof.

For every positive claim, state the hypotheses at the strongest exact scope actually proved.

## 3. Counterexample pressure test

Actively test the negative cases required by the blind packet, including non-primitive cells, boundary/axis degeneracies, primes 2 and 3, coordinate swap, collisions under coarse scalarization, and any attempted seam/globalization claim.

Preserve failed conjectures and smallest counterexamples rather than deleting them from the final return.

## 4. Executable evidence

Write an independently authored deterministic checker using exact integer arithmetic only.

Recommended path:

`experiments/prime_fusion_independent_replication_checker.py`.

The checker must be written from the blind packet and the replicator's own derivations. It must not copy or inspect the withheld source checker before return freeze.

Record the actual finite ranges executed and the exact PASS/FAIL outcome. Finite computation is audit evidence, not a substitute for proof.

## 5. Frozen return

Write one frozen return at:

`research_returns/PRIME_FUSION_INDEPENDENT_REPLICATION_RETURN_20260823.md`.

Required sections:

1. `BLINDNESS_STATUS` and complete files/sources read before freeze;
2. independently introduced definitions;
3. theorem statements with proofs;
4. failed conjectures and counterexamples;
5. checker path, ranges, and execution result;
6. unresolved claims;
7. one final classification:
   - `FULL_STRUCTURAL_REPLICATION`,
   - `PARTIAL_REPLICATION`,
   - `MATERIAL_COUNTEREXAMPLE`, or
   - `NO_RECONSTRUCTION`.

The return must be frozen before any source-package comparison.

## 6. PASS / KILL / STOP

PASS means the researcher freezes a self-contained exact return with explicit blindness provenance, proofs/counterexamples, and independently authored executable evidence, regardless of whether it agrees with the withheld source package.

The clean-independence claim is killed if source conclusions are exposed before freeze. That does not erase any mathematics already obtained; it changes only the evidence type.

After the return is frozen, **stop**. Do not self-compare with the withheld theorem package. The later comparison matrix is a Driver function.

## 7. Provenance note

This replay exists because an earlier free-research run produced a theorem package worth independent checking. The source result has been Driver-classified as derived theorem research rather than a new primitive axiom; therefore this task uses V5 `REPLAY_OR_INTEGRATION / REPLAY` while preserving the free-discovery origin in this provenance note.

No hidden theorem statement is imported by this taskbook.
