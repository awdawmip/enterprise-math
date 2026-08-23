<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PRIME-FUSION-T4-T7-T8-FINAL-EXACT-CLOSURE",
  "title": "Prime Fusion — T4/T7/T8 Final Exact Closure",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "PRIME_FUSION_T4_T7_T8_EXACT_STATEMENT_STRENGTH_INDEPENDENTLY_VERIFIED_OR_NARROWED_OR_REFUTED",
  "next_action": "Using only the final statement packet and already independently accepted prerequisites encoded there, independently verify, strengthen, narrow, or refute the remaining T4/T7/T8 exact-strength claims; classify their minimal hypotheses and composition DAG; write an exact-integer checker; freeze one return; and stop before later package comparison.",
  "dependencies": [
    "RS-PRIME-FUSION-INDEPENDENT-REPLICATION",
    "RS-PRIME-FUSION-PHASE-EXTENSION-TARGETED-INDEPENDENT-VERIFICATION",
    "driver_reviews/PRIME_FUSION_INDEPENDENT_REPLICATION_DRIVER_REVIEW_20260823.md@ffaf098cb612f8a54f1d49df33484d3d36019a92",
    "driver_reviews/PRIME_FUSION_PHASE_EXTENSION_TARGETED_VERIFICATION_DRIVER_REVIEW_20260823.md@ffaf098cb612f8a54f1d49df33484d3d36019a92",
    "research_inputs/PRIME_FUSION_T4_T7_T8_FINAL_EXACT_CLOSURE_PACKET_20260823.md@d8e3df5e2ceb61e63fe12ad38524fa5f5968f5cf"
  ],
  "source_refs": [
    "research_inputs/PRIME_FUSION_T4_T7_T8_FINAL_EXACT_CLOSURE_PACKET_20260823.md@d8e3df5e2ceb61e63fe12ad38524fa5f5968f5cf",
    "driver_reviews/PRIME_FUSION_INDEPENDENT_REPLICATION_DRIVER_REVIEW_20260823.md@ffaf098cb612f8a54f1d49df33484d3d36019a92",
    "driver_reviews/PRIME_FUSION_PHASE_EXTENSION_TARGETED_VERIFICATION_DRIVER_REVIEW_20260823.md@ffaf098cb612f8a54f1d49df33484d3d36019a92"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "prime-fusion",
    "final-exact-closure",
    "targeted-verification",
    "T4",
    "T7",
    "T8",
    "quotient",
    "idempotent-reconstruction",
    "dual-prime-characterization"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PFCLOSE",
  "origin_kind": "REPLAY_OR_INTEGRATION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-PRIME-FUSION-PHASE-EXTENSION-TARGETED-INDEPENDENT-VERIFICATION",
  "successor_gate": {
    "new_information_gap": "The clean blind replay left T4, T7, and T8 at substantial partial convergence rather than standalone exact source-statement strength. The later phase-extension verification independently supplied the missing T3 product-algebra and T6 idempotent prerequisites and closed the T3/T6/T10/T11 gap, leaving exactly T4/T7/T8 as the remaining theorem-package evidence gap.",
    "why_parent_result_does_not_close_it": "The phase-extension parent explicitly targeted only T3, T6, T10, and T11. Its Driver review states that T4, T7, and T8 were not re-run as standalone verification targets, so exact package-level closure cannot be inferred from the parent's success.",
    "discriminating_outcomes": [
      "T4, T7, and T8 all hold at exact source statement strength or stronger minimal-hypothesis forms",
      "one or more statements require explicit hypothesis or wording narrowing",
      "only a strict subset of T4, T7, and T8 survives exact verification",
      "a material counterexample invalidates a theorem-critical statement"
    ],
    "kill_condition": "If any target relies only on cardinality coincidence, silently assumes cyclicity, treats an abstract ring isomorphism as a labelled channel decomposition, omits a necessary primitivity/interiority hypothesis, or fails an exact counterexample test, the statement must be narrowed or rejected rather than accepted by composition shorthand.",
    "alternative_route_or_free_exploration_considered": "Closure with the existing evidence matrix was considered and is mathematically defensible, but it would leave three rows at partial rather than exact independent statement strength. Re-running the whole blind task or the phase task would duplicate closed mathematics. A narrow compositional verification of exactly T4/T7/T8 is the minimal experiment capable of deciding whether the full package reaches exact independent audit coverage.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The blind parent is already frozen and the phase parent has a different hard target. Reopening either would mix evidence types and duplicate solved work. A separate final-closure task isolates the three remaining claims and can terminate the package-evidence route with a precise yes/narrow/no classification."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:9c1f03a5086432f83d1a3821893be5589124293bc5be5b14d4b7e196220271c7",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Prime Fusion — T4/T7/T8 Final Exact Closure

Task-ID: `RS-PRIME-FUSION-T4-T7-T8-FINAL-EXACT-CLOSURE`

Origin: `REPLAY_OR_INTEGRATION`

Lineage: `CONTINUATION` from `RS-PRIME-FUSION-PHASE-EXTENSION-TARGETED-INDEPENDENT-VERIFICATION`.

Identity lane: `PFCLOSE`.

Intended owner branch:

`research/prime-fusion-t4-t7-t8-final-exact-closure`

## 0. Evidence type and mathematical read boundary

This is the final statement-exposed exact verification step for the three source claims that remain only partially independently reconstructed.

Before freezing the return, use as mathematical input only:

`research_inputs/PRIME_FUSION_T4_T7_T8_FINAL_EXACT_CLOSURE_PACKET_20260823.md`

at source:

`d8e3df5e2ceb61e63fe12ad38524fa5f5968f5cf`.

The packet already contains the independently accepted prerequisites needed for this task. Do not open the withheld source proofs, source checker, source research narrative, or later package-comparison materials as proof evidence before freeze.

The target statements are intentionally visible. The evidence question is whether their exact proofs, hypotheses, labelling semantics, and iff directions survive independent reconstruction and counterexample pressure.

## 1. Hard target

Classify:

`PRIME_FUSION_T4_T7_T8_EXACT_STATEMENT_STRENGTH_INDEPENDENTLY_VERIFIED_OR_NARROWED_OR_REFUTED`.

Produce one exact verdict for each target:

- T4 primitive pointed quotient collapse;
- T7 unordered reconstruction from `(H,e)`;
- T8 dual-prime finite-quotient characterization.

The task succeeds with a proof, a stronger minimal-hypothesis theorem, a justified scope narrowing, or a material counterexample. Agreement with historical wording is not required.

## 2. Do not reopen closed mathematics

Do not re-run the full prime-arrangement, reciprocity, local-sieve, adjacency, phase-orbit, or sixth-power programs.

Use the packet's accepted prerequisite layer and spend the task only on:

1. quotient/cyclicity and pointed-carrier exactness for T4;
2. idempotent-to-channel-to-cell iff composition for T7;
3. dual-prime iff finite-product-of-fields characterization for T8;
4. theorem-critical versus redundant hypotheses.

## 3. T4 proof obligation

For the primitive pointed quotient claim:

- construct every ring map explicitly;
- prove kernel/surjectivity or otherwise prove the exact quotient isomorphism;
- identify the exact criterion under which each component quotient is cyclic;
- prove the pointed image of `xi` is the claimed residue;
- separate ring-isomorphism strength from pointed-isomorphism strength;
- preserve the smallest nonprimitive/boundary counterexample if a hypothesis is necessary.

Cardinality equality alone is not sufficient.

## 4. T7 proof obligation

For reconstruction from `(H,e)`:

- prove the idempotent factor split at the exact strength actually used;
- prove necessity and sufficiency of the two square conditions;
- audit same-parity, positivity, integrality, and primitivity;
- determine whether `NC=H` and `gcd(N,C)=1` are redundant once `e` is idempotent;
- determine the exact role of `C<N<2C`;
- classify channel swap under `e -> 1-e`;
- produce explicit arithmetically legal but geometrically inadmissible idempotent splits.

## 5. T8 proof obligation

For the dual-prime quotient characterization:

- prove both directions;
- distinguish canonical labelled channel components from an abstract unlabelled product ring;
- determine whether square-free semiprime total cardinality plus primitive channel coprimality already forces the two channel primes;
- prove the prime factors are distinct;
- audit the necessity of `primitive`, `interior`, and `N,C>1`;
- include composite/prime-power controls.

## 6. Composition and minimal-hypothesis DAG

Produce the shortest valid dependency DAG for T4/T7/T8 using only independently accepted prerequisites.

At minimum determine whether:

- T4 is exactly product algebra plus component cyclicity;
- T7 is exactly universal idempotent splitting plus the channel-pair square gate;
- T8 is a formal consequence of T4 plus primitive coprimality and channel nontriviality;
- any source hypotheses can be removed without changing theorem meaning.

If a stronger theorem subsumes one of the three source statements, state both the stronger theorem and the exact source corollary.

## 7. Executable evidence

Write an independently authored exact-integer checker.

Recommended path:

`experiments/prime_fusion_t4_t7_t8_final_exact_closure_checker.py`.

Record the actual finite ranges and exact result. Include positive and negative controls for all three claims.

Finite computation is audit evidence only; general acceptance must rest on written proofs.

## 8. Frozen return

Write one return at:

`research_returns/PRIME_FUSION_T4_T7_T8_FINAL_EXACT_CLOSURE_RETURN_20260823.md`.

Required sections:

1. evidence status and exact files/sources read;
2. T4/T7/T8 verdict table;
3. independent proofs and exact counterexamples;
4. corrected/minimal-hypothesis theorem statements;
5. dependency DAG;
6. checker path, ranges, and actual result;
7. stronger independent consequences, if any;
8. final classification:
   - `T4_T7_T8_EXACT_CLOSURE_VERIFIED`,
   - `T4_T7_T8_VERIFIED_WITH_SCOPE_NARROWING`,
   - `T4_T7_T8_PARTIALLY_VERIFIED`, or
   - `T4_T7_T8_MATERIAL_COUNTEREXAMPLE`.

## 9. PASS / KILL / STOP

PASS means all three exposed claims have exact theorem-strength classifications, including any necessary narrowing or negative result.

Independent-verification strength is lost if withheld source proofs/checker are used before freeze; preserve any mathematics obtained but type it accordingly.

After the return is frozen, stop. Do not perform the later 15-theorem package comparison yourself.
