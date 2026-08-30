<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-SIX-AXIS-P11-COLLISION-LOCUS-CONDITIONAL-SELECTOR",
  "title": "P000 six-axis P11 collision locus and conditional selector",
  "kind": "RESEARCH",
  "owner": "research/p000-six-axis-p11-collision-locus-conditional-selector",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "The accepted mixed-invariant result proves that H,T,P11 leaves at most a two-state K/Gamma fiber and that a second full integer moment resolves it, but the exact collision locus and the minimal conditional information needed only on that locus remain unclassified.",
  "next_action": "Classify the exact P11 two-fiber locus, derive or obstruct a symmetric quadratic resolvent for the two candidate second-moment values, and determine whether one conditional branch bit suffices to recover K/Gamma without carrying a second integer moment off the collision locus.",
  "dependencies": [
    "RR-B96585874709743F94BC"
  ],
  "source_refs": [
    "research_result_records/RS-P000-SIX-AXIS-MIXED-INVARIANT-ALIGNMENT-COMPRESSION/RR-B96585874709743F94BC.json",
    "research_returns/P000_SIX_AXIS_MIXED_INVARIANT_ALIGNMENT_COMPRESSION_RETURN_20260830.md"
  ],
  "evidence_status": "PARENT_RESULT_DRIVER_ACCEPTED_REQUIRED / P11_FIBER_AT_MOST_TWO / DERIVED_ARITHMETIC_ONLY",
  "hard_block": null,
  "tags": [
    "P000",
    "six-axis",
    "P11",
    "collision-locus",
    "resolvent",
    "conditional-selector",
    "arithmetic-compression"
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
  "identity_lane": "P000P11C1",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P000-SIX-AXIS-MIXED-INVARIANT-ALIGNMENT-COMPRESSION",
  "successor_gate": {
    "new_information_gap": "The parent minimizes the number of retained integer moments inside a frozen three-moment grammar, but it does not characterize the exact P11 collision locus or whether the second integer moment can be replaced by one conditional branch bit used only when the P11 fiber has size two.",
    "why_parent_result_does_not_close_it": "The parent proves a global fiber bound and supplies sufficient pairs, but it never eliminates the alignment variables on the two-fiber stratum, derives a quadratic resolvent for the two candidate second-moment values, or measures the conditional rather than unconditional information cost.",
    "discriminating_outcomes": [
      "the P11 collision locus has an exact symmetric criterion and a two-root second-moment resolvent, yielding one conditional branch bit",
      "the collision locus is exact but no uniform low-degree resolvent exists in the frozen algebra, forcing a larger conditional packet",
      "the claimed two-state conditional compression fails on an exact integer-pairable collision family"
    ],
    "kill_condition": "Do not enlarge into native orientation, a signed native carrier, Full-Cell dynamics, factorization, or an unbounded invariant search. Stop with an exact no-go if the frozen resolvent grammar is insufficient.",
    "alternative_route_or_free_exploration_considered": "Closure would preserve a two-integer sufficient packet but leave its conditional information cost unresolved. Native orientation routes are separately owned. A bounded collision-locus/resolvent analysis is the smallest route that can decide whether the second integer is genuinely needed away from collisions.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent hard target concerned minimal subsets of P11,P21,P12 and is complete. This continuation changes the object from global subset sufficiency to the geometry and algebra of the exceptional P11 collision fiber, with different terminal outcomes and evidence."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P000 six-axis P11 collision locus and conditional selector

## Mother question

Given the accepted derived six-axis marginals `H={h1,h2,h3}`, `T={t1,t2,t3}` and the mixed invariant `P11=sum_i h_i t_i`, exactly when does the residual aligned packet `K=multiset{(h_i,t_i)}` have two admissible `Gamma=C2 wr S3` orbits rather than one, and can the extra information needed on that exceptional locus be reduced from a second full integer moment to one exact conditional branch bit?

## Frozen inputs and scope

Freeze accepted Result `RR-B96585874709743F94BC` at derived arithmetic strength. In particular, freeze the parent facts that `P11` has global residual fiber at most `2`, that `P11` plus `P21` or `P12` reconstructs `K/Gamma`, and that the integer-pairability gate is `h^2-4t=d^2>=0` with `d congruent h (mod 2)`.

The task must freeze the resolvent grammar before examining outcomes. The allowed alignment-sensitive scalars are `P11`, `P21`, and `P12`; the separate symmetric data of `H` and `T` are already available. It may form symmetric polynomial/rational combinations of the marginal elementary symmetric functions together with `P11`, and may use `P21` or `P12` only as the candidate second coordinate whose two possible values are to be eliminated. It may not add higher mixed moments after seeing collisions.

All objects remain a derived six-coordinate arithmetic facade. P000 remains six-dimensional discrete Cell space plus one-dimensional time. Classical assignment/permutation geometry, symmetric-polynomial elimination, resolvent theory, and finite-group invariant theory must be treated as prior mathematics where applicable.

## Hard target and required outputs

Hard target:

`P000_P11_COLLISION_LOCUS_AND_CONDITIONAL_SELECTOR_EXACTLY_CLASSIFIED_OR_FROZEN_RESOLVENT_GRAMMAR_INSUFFICIENT`.

Required outputs:

1. prove an exact necessary-and-sufficient criterion for a two-orbit `P11` fiber, including all repeated-`H` and repeated-`T` strata and the distinct-marginal stratum;
2. classify which relative permutations can collide at equal `P11` and give an exact algebraic/Diophantine form of the collision equation;
3. on the two-fiber locus, eliminate the alignment variables and derive a symmetric polynomial or rational quadratic whose roots are the two candidate `P21` values, or prove that no such quadratic exists in the frozen resolvent grammar;
4. perform the dual analysis for `P12` sufficiently to determine whether the `P21` and `P12` branch choices encode the same binary residue, opposite residues, or a stratum-dependent relation;
5. if a two-root resolvent exists, define a deterministic ordering of the two candidate `K/Gamma` packets from the already-known marginals and prove that exactly one conditional bit selects the actual packet; outside the collision locus the bit must be absent rather than carried redundantly;
6. give explicit infinite or parametrized integer-pairable collision families and exact minimal witnesses for every positive collision class, plus adversarial controls that attempt to create a three-state `P11` fiber;
7. quantify the conditional information cost and compare it with the parent's unconditional `{P11,P21}` / `{P11,P12}` two-integer packets without using arbitrary integer encodings as fake compression;
8. preserve the Pfaffian-orientation firewall: recovering `K/Gamma` or a collision branch may not be relabeled as selection of the oriented negative product slot;
9. separate classical resolvent/assignment/invariant-theory ingredients from the task-specific integer-pairable specialization and make no historical novelty claim;
10. supply a task-local exact checker/certificate and a NEW immutable Result with complete Git blob SHA-1 plus SHA-256 output binding.

## Research value to preserve

The parent result shows that two mixed integers are sufficient globally, but it also proves that `P11` alone already leaves at most two states. The unresolved issue is therefore sharply localized: a second integer may be unnecessary on the generic one-state fiber and may contain only one bit of useful information on the collision fiber. An exact collision-locus/resolvent theorem would turn the current global compression into a conditional information law; an exact obstruction would show why the full second moment remains algebraically load-bearing.

## Success, kill, and return criteria

Terminal success is one of: `EXACT_COLLISION_LOCUS_WITH_ONE_BIT_CONDITIONAL_SELECTOR`, `EXACT_COLLISION_LOCUS_BUT_RESOLVENT_REQUIRES_MORE_THAN_ONE_BIT`, or `FROZEN_RESOLVENT_GRAMMAR_INSUFFICIENT_WITH_EXACT_COUNTEREXAMPLE`. Success requires symbolic proof plus exact integer witnesses and deterministic regression.

Kill any attempt to infer native orientation, signed native carrier structure, native dimension reduction, factorization, or Full-Cell dynamics from the derived collision selector. Do not enlarge the mixed-moment grammar after observing failures. Do not create a new general-purpose tool when existing algebraic machinery and a task-local checker suffice. Return a NEW immutable Result for Driver review and make no downstream task decision from the researcher lane.
