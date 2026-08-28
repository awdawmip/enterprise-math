<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-A3-SHELL-PARTIAL-MOVE-SCALE-COHERENCE-REVISION",
  "title": "A3 外壳递归部分动作的跨尺度一致性与径向缺陷修订",
  "kind": "RESEARCH",
  "owner": "research/a3-shell-partial-move-scale-coherence-revision",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "The prior frame-only double-coset defect fails to classify the actual align-then-restrict versus restrict-then-align square when prefix move support shifts with scale; repair H4 on the existing A3 finite carrier without restarting H1-H3.",
  "next_action": "Freeze the actual depth-d partial action maps and restriction maps on B1 subset B2 subset B3, replay the n=2 g=(23) interior-marker counterexample, then derive the strongest correct support-aware radial defect or exact no-go before re-evaluating dependent H5/H6 observables.",
  "dependencies": [
    "research_tasks/A3_RECURSIVE_SHELL_ALIGNMENT_TOMOGRAPHY_20260828.md@main",
    "driver_reviews/A3_RECURSIVE_SHELL_ALIGNMENT_TOMOGRAPHY_DRIVER_PREMERGE_REVIEW_20260828.md@main",
    "research_returns/A3_RECURSIVE_SHELL_ALIGNMENT_TOMOGRAPHY_RETURN_20260828.md@main"
  ],
  "source_refs": [
    "scripts/check_a3_recursive_shell_alignment_tomography.py@main",
    "research_artifacts/A3_RECURSIVE_SHELL_ALIGNMENT_TOMOGRAPHY/prototype_certificate.json@main"
  ],
  "evidence_status": "DRIVER_REQUEST_CHANGES / H4_FRAME_ONLY_IFF_REFUTED / H1_H3_PARTIAL_EXACT_RESULTS_PRESERVED / FIXED_H_GROUPOID_SIDE_EVIDENCE_AVAILABLE",
  "last_progress_ref": "driver_reviews/A3_RECURSIVE_SHELL_ALIGNMENT_TOMOGRAPHY_DRIVER_PREMERGE_REVIEW_20260828.md",
  "last_progress_at": "2026-08-28T08:24:05+00:00",
  "hard_block": null,
  "tags": [
    "A3",
    "recursive-shell",
    "revision",
    "partial-move",
    "scale-coherence",
    "radial-defect",
    "groupoid",
    "operation-safe",
    "counterexample"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-A3-SHELL-PARTIAL-MOVE-SCALE-COHERENCE-REVISION",
  "parent_objective_id": "OBJ-A3-RECURSIVE-SHELL-ALIGNMENT-AND-BULK-OBSERVATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "A3SCR",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-A3-RECURSIVE-SHELL-ALIGNMENT-TOMOGRAPHY",
  "successor_gate": {
    "new_information_gap": "Independent Driver review found an exact state-level counterexample to the submitted H4 criterion: equal adjacent frame aligners give identity double-coset defect while scale-dependent depth-2 support still changes S1 on restrict-then-align but not align-then-restrict.",
    "why_parent_result_does_not_close_it": "The parent checker verifies frame groups, stabilizers and double-coset algebra, but not the actual cross-scale square as maps or relations on nested states. The later fixed-H pair-groupoid calculation repairs compressed-label composition only and explicitly leaves partial-move coherence open.",
    "discriminating_outcomes": [
      "Construct a support/domain-aware radial object for which the actual nested-state scale square has an exact iff coherence criterion.",
      "Prove no finite frame-phase quotient can classify the square for the declared partial move family and return the strongest relation/groupoid-valued replacement.",
      "Show the chosen move semantics must be narrowed or changed for restriction descent, with an exact minimal obstruction and revised nontriviality boundary.",
      "Reduce the defect to a strictly smaller typed support-transition invariant with a deterministic complete checker."
    ],
    "kill_condition": "Any repair that depends only on Hg_n g_(n+1)^(-1) H, or tests only double-coset multiplication without evaluating the two state-level paths, is non-closing. Do not restart shell counting or enlarge the same S4/H census.",
    "alternative_route_or_free_exploration_considered": "Closing the Rubik-shell route, accepting the fixed-H algebra as sufficient, and opening a larger finite census were considered. The explicit counterexample shows the smallest unresolved unit is instead the existing task's partial-move scale-commutation law.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The original task generation now contains a merged false H4 terminal claim and a separate redispatch side result. A typed revision task isolates the exact invalid theorem boundary, preserves verified H1-H3 work, and prevents further same-task result ambiguity."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# A3 外壳递归部分动作的跨尺度一致性与径向缺陷修订

Status: `PUBLISHED_REGISTERED / CONTINUATION / H4 REVISION`

## Mother question

For the existing nested A3 shell model, what is the strongest exact object that classifies the actual cross-scale comparison

\[
\widehat\rho_{n+1,n}\circ C_{n+1}
\quad\text{versus}\quad
C_n\circ\rho_{n+1,n}
\]

when legal aligning moves have scale-dependent partial support, so that the same frame element may act on different radial shells at adjacent scales?

The target is not another double-coset census. It is an exact repair of the state-level scale square.

## Frozen inputs and scope

Preserve the already checked finite carrier

\[
\Lambda_3=\{x\in\mathbb Z^4:\sum_i x_i=0\},
\qquad
B_n=\{x:\max_i|x_i|\le n\},
\qquad
S_n=B_n\setminus B_{n-1},
\]

together with the exact shell census, the sign-twisted 24-frame action, the pointer-target stabilizer calculation, and the depth-1 shielding / depth-2 first-coupling support convention at the operational carrier layer.

Do not restart H1-H3 unless a direct dependency failure is found.

Freeze the Driver counterexample as a mandatory regression. At adjacent scales 3 and 2, use the same aligner \(g=(23)\), pointer targets \(a_k=(k,-k,0,0)\), compatible shell markers \(p_k=R_g^{-1}a_k\), and the interior marker

\[
p=(1,-1,0,0)\in S_1.
\]

For the declared depth-2 prefix action, scale 3 acts on \(S_3\cup S_2\) while scale 2 acts on \(S_2\cup S_1\). Hence align-then-restrict fixes \(p\), while restrict-then-align sends it to

\[
R_g p=(-1,0,1,0).
\]

The residual stabilizer \(H=\{e,(12)\}\) fixes \(p\), so the two outputs are not residual-\(H\)-equivalent even though the frame double-coset label is the identity class.

The fixed-\(H\) double-coset / pair-groupoid calculations may be reused only as a compressed special case after their exact hypotheses are matched. They are not the repaired H4 conclusion by themselves.

Continue to compose the current symmetry, operation-safe quotient, relation/BRC, precision/refinement, and holonomy/gluing tools. A new shared family requires a demonstrated input/output gap after composition.

## Hard target and required outputs

Hard target:

`A3_PARTIAL_MOVE_SCALE_COMMUTATION_AND_RADIAL_DEFECT_EXACTLY_CLASSIFIED`.

Required outputs:

1. Define the actual scale-indexed partial actions \(D_{n,d}\), their domains/supports, the restriction maps \(\rho_{n+1,n}\), the alignment relation \(C_n\), residual target stabilizers, and the observed state language with explicit types.
2. Prove or refute operation descent:
   \[
   \rho_{n+1,n}D_{n+1,d}(g)
   \stackrel{?}{=}
   D_{n,d}(g)\rho_{n+1,n}
   \]
   on the exact domain where each side is defined.
3. Add the frozen \(n=2,\ g=(23),\ p=(1,-1,0,0)\) counterexample as a deterministic regression and verify both paths on serialized states.
4. Derive the strongest correct radial defect. It may be group-, groupoid-, relation-, cocycle-, support-profile-, or quotient-valued, but it must distinguish every state-level coherence class claimed by the theorem.
5. State exactly how the fixed-\(H\) left-coset pair groupoid and double-coset relation algebra arise as a quotient/special case, and prove the relevant projection law.
6. Re-evaluate the parent task's H5/H6 scale observables and three-radius prototype wherever they depended on the false frame-only iff criterion.
7. Provide an exact checker that tests the two paths themselves, not only the compressed class algebra.
8. Return either a corrected theorem, an exact no-go showing which compression is insufficient, or a strictly smaller typed obstruction with a complete next frontier.

## Research value to preserve

This revision protects the central scientific idea of recursive outer-shell alignment while removing a false simplification. The key unresolved phenomenon is precisely what makes the user's construction interesting: a nominally identical rotation may penetrate to different interior depth after the world is resized.

A correct scale defect can therefore separate frame mismatch from support/domain mismatch and may become the actual boundary-to-bulk observable of the recursive microscope. A negative theorem is equally valuable if it proves that no frame-only quotient can reconstruct the interior effect of partial shell moves.

The exact shell census, 24-frame action, residual stabilizer analysis, shielding theorem, and fixed-\(H\) relation algebra should be preserved rather than recomputed.

## Success, kill, and return criteria

Success requires an exact state-level classification of the cross-scale square for the declared finite move semantics, with the frozen counterexample handled correctly and every claimed quotient proved operation-safe.

Kill any route that:

- reinstates the identity-double-coset iff criterion without support/domain data;
- verifies only group multiplication while omitting the nested-state action;
- treats a solver word as canonical without stabilizer/quotient proof;
- enlarges the same finite census instead of resolving the scale-support mismatch;
- imports physical or Foundation meaning from the Rubik carrier.

If no compact invariant survives, return the strongest exact relation/groupoid formulation and the smallest collision witness preventing further compression.
