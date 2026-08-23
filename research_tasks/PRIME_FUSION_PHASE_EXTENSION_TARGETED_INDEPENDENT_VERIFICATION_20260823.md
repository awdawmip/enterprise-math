<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PRIME-FUSION-PHASE-EXTENSION-TARGETED-INDEPENDENT-VERIFICATION",
  "title": "Prime Fusion — Phase/Fusion Extension Targeted Independent Verification",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "PRIME_FUSION_PHASE_EXTENSION_T3_T6_T10_T11_INDEPENDENTLY_VERIFIED_OR_NARROWED_OR_REFUTED",
  "next_action": "Using the statement-only targeted packet and the already independently reconstructed core prerequisites, independently prove, narrow, partially retain, or refute the four unresolved phase/fusion-extension claims; audit their dependency graph; write an exact-integer checker; freeze one verification return; and stop before source-proof comparison.",
  "dependencies": [
    "RS-PRIME-FUSION-INDEPENDENT-REPLICATION",
    "driver_reviews/PRIME_FUSION_INDEPENDENT_REPLICATION_DRIVER_REVIEW_20260823.md@be07e5d9af0ca428ae74c2807fdde586d0d665a3",
    "research_inputs/PRIME_FUSION_PHASE_EXTENSION_TARGETED_VERIFICATION_PACKET_20260823.md@1054ebbf56ae0f9e3cce1e60d743875946d25e18"
  ],
  "source_refs": [
    "driver_reviews/PRIME_FUSION_INDEPENDENT_REPLICATION_DRIVER_REVIEW_20260823.md@be07e5d9af0ca428ae74c2807fdde586d0d665a3",
    "research_inputs/PRIME_FUSION_PHASE_EXTENSION_TARGETED_VERIFICATION_PACKET_20260823.md@1054ebbf56ae0f9e3cce1e60d743875946d25e18",
    "definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md@be07e5d9af0ca428ae74c2807fdde586d0d665a3"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "prime-fusion",
    "phase-extension",
    "targeted-verification",
    "independent-proof",
    "T3",
    "T6",
    "T10",
    "T11"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PFEXT",
  "origin_kind": "REPLAY_OR_INTEGRATION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-PRIME-FUSION-INDEPENDENT-REPLICATION",
  "successor_gate": {
    "new_information_gap": "The clean independent replay achieved the blind R1-R6 hard target and independently converged on the arithmetic, marked-quotient, reciprocity, local-sieve, adjacency, and finite-dimensional-reduction core, but post-freeze comparison found four source-package claims not independently reconstructed: the product fusion algebra/discriminant statement, reciprocal-trace idempotent collapse, four-phase order-12 orbit, and sixth-power phase-blind channel readout.",
    "why_parent_result_does_not_close_it": "The parent task intentionally did not expose the source theorem list and therefore could not be expected to verify source-only representation layers that were never selected by its blind questions. Its FULL_STRUCTURAL_REPLICATION classification is complete for R1-R6 but does not establish independent proof coverage of these four phase/fusion-extension statements.",
    "discriminating_outcomes": [
      "all four target statements are independently proved at the stated scope",
      "the extension is correct only after explicit scope narrowing or hypothesis repair",
      "only a strict subset of the four statements survives independent proof",
      "a material counterexample refutes at least one theorem-critical statement"
    ],
    "kill_condition": "If any target claim relies on a hidden source derivation, an unproved identification of all mixed roots, a missing unit/coprimality hypothesis, or a finite pattern that fails under exact counterexample search, the claim must be narrowed or rejected rather than preserved for package symmetry.",
    "alternative_route_or_free_exploration_considered": "Closure after the core replay was considered, as was re-running the entire blind replication. Closure would leave four theorem-package claims without independent evidence; another full blind replay would duplicate already-verified core mathematics and still would not guarantee selection of the phase representation. A narrow statement-exposed proof audit is the minimal discriminating experiment.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent task has already frozen and its information firewall served its purpose. Reopening it with newly exposed target statements would mix blind-replication evidence with post-comparison verification. A separate continuation preserves evidence typing and isolates the only remaining package-level verification gap."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:9c1f03a5086432f83d1a3821893be5589124293bc5be5b14d4b7e196220271c7",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Prime Fusion — Phase/Fusion Extension Targeted Independent Verification

Task-ID: `RS-PRIME-FUSION-PHASE-EXTENSION-TARGETED-INDEPENDENT-VERIFICATION`

Origin: `REPLAY_OR_INTEGRATION`

Lineage: `CONTINUATION` from `RS-PRIME-FUSION-INDEPENDENT-REPLICATION`.

Identity lane: `PFEXT`.

Intended owner branch:

`research/prime-fusion-phase-extension-targeted-verification`

## 0. Evidence type and execution boundary

This is **statement-exposed independent verification**, not blind discovery and not a rerun of the completed R1-R6 replay.

Before freezing the verification return, use only:

1. `research_inputs/PRIME_FUSION_PHASE_EXTENSION_TARGETED_VERIFICATION_PACKET_20260823.md` at `1054ebbf56ae0f9e3cce1e60d743875946d25e18`;
2. the primitive spatial definition named in the task metadata if a carrier fact must be checked;
3. ordinary exact algebra, elementary number theory, CRT, finite-ring reasoning, and independently authored deterministic computation.

Do not use the withheld source proofs, source checker, source research narrative, or later comparison notes as proof evidence before the return is frozen.

The target statements themselves are intentionally visible. Agreement caused only by seeing the statement is not a defect; the evidence question is whether the proofs and scope survive independent reconstruction and counterexample pressure.

## 1. Hard target

Classify:

`PRIME_FUSION_PHASE_EXTENSION_T3_T6_T10_T11_INDEPENDENTLY_VERIFIED_OR_NARROWED_OR_REFUTED`.

The task must produce an exact verdict for each of the four target clusters in the packet:

- product fusion algebra / discriminant;
- reciprocal-trace idempotent collapse;
- four mixed phases / order-12 orbit;
- sixth-power phase-blind channel readout.

A package-level `PASS` is not required. A corrected theorem or counterexample is valid and preferred over preserving an overbroad statement.

## 2. Do not redo the closed core route

The packet already supplies the independently reconstructed core prerequisites needed for this verification.

Do not spend the task re-deriving the entire gcd, coordinate-recovery, reciprocity, adjacency, or finite-sieve theory unless one of those facts is directly needed to audit a target dependency.

The new work is the phase/fusion extension itself.

## 3. Independent proof obligations

For every retained target statement:

1. give a self-contained proof from the permitted inputs;
2. list every unit, positivity, primitivity, coprimality, primality, or small-prime hypothesis actually used;
3. separate polynomial identities from ring decompositions and from geometric/shared-coefficient interpretation;
4. prove every completeness word such as “all”, “exactly”, or “the orbit”, rather than inferring it from enumeration;
5. identify what changes under coordinate swap and sign convention for the marked residue.

For every rejected or narrowed statement, preserve the smallest exact counterexample or missing hypothesis.

## 4. Dependency graph

Produce a theorem dependency DAG for the four targets.

At minimum determine whether:

- reciprocal-trace idempotence requires the product-ring theorem or only a reciprocal-polynomial identity;
- the four-phase orbit requires the product algebra, or follows directly from CRT plus local root orders;
- the sixth-power readout requires the full phase-orbit theorem, or only local orders;
- any part extends from dual-prime channels to primitive composite coprime channels.

A stronger, simpler dependency theorem discovered here should be retained even if it changes the source package's presentation order.

## 5. Counterexample pressure

Use the packet's mandatory scope tests and add any others needed.

In particular, distinguish:

- roots of the fused polynomial that arise from one shared coefficient pair;
- algebraically valid mixed roots obtained by independent local conjugation;
- arbitrary unit roots when the channel factors are composite;
- ramified/small cases versus the unramified dual-prime case.

Do not globalize beyond the one-sector hypotheses supplied here.

## 6. Executable evidence

Write an independently authored exact-integer checker.

Recommended path:

`experiments/prime_fusion_phase_extension_targeted_verification_checker.py`.

The checker should test the exact claims actually retained, enumerate all fused roots for manageable `H`, verify orbit cardinality/completeness, test coordinate-swap pairing, and exercise small/degenerate and composite-channel cases.

Record actual finite ranges and the exact execution result. Computation supports but does not replace proof.

## 7. Frozen return

Write one return at:

`research_returns/PRIME_FUSION_PHASE_EXTENSION_TARGETED_VERIFICATION_RETURN_20260823.md`.

Required sections:

1. evidence status and exact files/sources read;
2. V3/V6/V10/V11 verdict table;
3. independent proofs or exact counterexamples;
4. corrected theorem statements where needed;
5. dependency DAG;
6. checker path, ranges, and actual result;
7. stronger independent consequences, if any;
8. final classification:
   - `PHASE_EXTENSION_FULLY_VERIFIED`,
   - `PHASE_EXTENSION_VERIFIED_WITH_SCOPE_NARROWING`,
   - `PHASE_EXTENSION_PARTIALLY_VERIFIED`, or
   - `PHASE_EXTENSION_MATERIAL_COUNTEREXAMPLE`.

## 8. PASS / KILL / STOP

PASS means the four exposed target clusters have been independently classified at exact theorem strength, including negative outcomes where appropriate.

The verification claim is killed if source proofs or source checker are used before freeze; any mathematics obtained may still be preserved but must be typed as non-independent review evidence.

After the return is frozen, stop. Do not perform the later package reconciliation yourself.
