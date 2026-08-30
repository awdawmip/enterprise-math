<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-SIX-AXIS-MIXED-INVARIANT-ALIGNMENT-COMPRESSION",
  "title": "P000 six-axis mixed-invariant alignment compression",
  "kind": "RESEARCH",
  "owner": "research/p000-six-axis-mixed-invariant-alignment-compression",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "The accepted Johnson–Tropical integration isolates a sharp at-most-six-state ambiguity: separate complementary-pair sum and product multisets do not retain their relative matching, while the aligned packet K is complete modulo the declared carrier-plus-complement symmetry.",
  "next_action": "Freeze a small simultaneous mixed-moment grammar before examining outcomes and classify the smallest exact subpacket that reconstructs the H-to-T alignment modulo the declared derived symmetry, including repeated-value strata, sharp collision families, and the orientation-sensitive Pfaffian boundary.",
  "dependencies": [
    "RR-2FFF3D2DFED3FF2535E3"
  ],
  "source_refs": [
    "research_result_records/RS-P000-SIX-AXIS-JOHNSON-TROPICAL-ARITHMETIC-INTEGRATION/RR-2FFF3D2DFED3FF2535E3.json",
    "research_returns/P000_SIX_AXIS_JOHNSON_TROPICAL_ARITHMETIC_INTEGRATION_RETURN_20260830.md"
  ],
  "evidence_status": "PARENT_RESULT_DRIVER_ACCEPTED / SHARP_SIX_STATE_ALIGNMENT_RESIDUE / DERIVED_ARITHMETIC_ONLY",
  "hard_block": null,
  "tags": [
    "P000",
    "six-axis",
    "mixed-invariants",
    "alignment",
    "multisymmetric",
    "Q_orb",
    "pair-packet",
    "arithmetic-compression"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-SIX-AXIS-MIXED-INVARIANT-ALIGNMENT-COMPRESSION",
  "parent_objective_id": "OBJ-P000-SIX-AXIS-ARITHMETIC-TROPICAL-INTEGRATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000MIAC1",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P000-SIX-AXIS-JOHNSON-TROPICAL-ARITHMETIC-INTEGRATION",
  "successor_gate": {
    "new_information_gap": "The parent proves that separate H and T multisets leave a sharp six-way relative-alignment residue, but it does not classify whether that finite residue has a smaller exact algebraic encoding by natural simultaneous mixed invariants.",
    "why_parent_result_does_not_close_it": "The parent establishes completeness only after retaining the fully aligned packet K and gives the six-state fiber bound; it neither freezes a mixed-invariant grammar nor proves a minimal separator or an irreducibility theorem for the remaining alignment state.",
    "discriminating_outcomes": [
      "a strict subpacket of the frozen mixed moments separates every admissible alignment orbit",
      "all frozen mixed moments are required on some exact integer stratum",
      "the frozen grammar still has exact alignment collisions and must close with an insufficiency certificate"
    ],
    "kill_condition": "Do not turn the alignment residue into native orientation, a signed native carrier, a Full-Cell lift, a native dimension claim, or a new general-purpose invariant engine. Stop at the exact derived arithmetic boundary if the frozen grammar cannot separate.",
    "alternative_route_or_free_exploration_considered": "Closure would leave a quantified six-state information cost without knowing its minimal algebraic encoding. Native signed-carrier and Full-Cell routes are already owned elsewhere and would duplicate active work. A bounded derived invariant-compression continuation isolates the new residue without crossing those owners.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent hard target is already satisfied and its joint-information atlas is terminal. The new question changes the target from discovering joint fibers to minimizing the exact representation of the newly isolated alignment fiber, so a distinct continuation gives a clean result boundary."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P000 six-axis mixed-invariant alignment compression

## Mother question

Given the accepted derived six-axis data consisting of the unordered complementary-pair sum multiset `H={h1,h2,h3}` and product multiset `T={t1,t2,t3}` (equivalently exact `Q_orb` for `T`), can the remaining relative matching needed to recover `K=multiset{(h_i,t_i)}` modulo `Gamma=C2 wr S3` be encoded by a strictly smaller exact packet of natural simultaneous mixed invariants, and what is the minimal packet inside one frozen finite grammar?

## Frozen inputs and scope

Freeze the accepted parent Result `RR-2FFF3D2DFED3FF2535E3` at its exact derived representation/carrier strength. Use the six integer coordinates in the frozen order `(AB,AC,AD,BC,BD,CD)`, the three complementary pairs, `H=(h1,h2,h3)`, `T=(t1,t2,t3)`, exact `Q_orb`, `K=multiset{(h_i,t_i)}`, and `Gamma=<S4,C>=C2 wr S3` of order `48`. The separate multisets of `H` and `T` are already known input and therefore their pure symmetric polynomials do not count as new alignment information.

Before inspecting separator outcomes, freeze the mixed-moment grammar
`P11=sum_i h_i t_i`,
`P21=sum_i h_i^2 t_i`,
`P12=sum_i h_i t_i^2`.
This grammar is a derived arithmetic facade only. P000 remains a native six-dimensional discrete Cell space plus one-dimensional time. The task may use classical finite-group or multisymmetric invariant theory as prior mathematics, but it must identify exactly which statements are classical baseline and which are task-specific integer specializations.

## Hard target and required outputs

Hard target:

`P000_SIX_AXIS_ALIGNMENT_RESIDUE_MINIMAL_MIXED_INVARIANT_PACKET_CLASSIFIED_OR_FROZEN_GRAMMAR_INSUFFICIENT`.

Required outputs:

1. prove exact `Gamma`-invariance of the declared simultaneous mixed moments and state precisely what information is already supplied by the separate `H` and `T` multisets;
2. classify every subset of `{P11,P21,P12}` as sufficient or insufficient to reconstruct the aligned packet `K` from the separate multisets, with no outcome-dependent enlargement of the grammar;
3. give symbolic reconstruction formulas on the distinct-`H` stratum and exact handling of `2+1` and triple multiplicity strata; repeat the analysis with repeated `T` where it changes stabilizers or minimality;
4. for every claimed insufficient subpacket, provide exact integer collision families or minimal explicit witnesses having identical frozen inputs and retained mixed data but different `Gamma` orbits;
5. determine the smallest globally sufficient subpacket inside the frozen grammar, or prove by exact collisions that all frozen candidates remain insufficient;
6. quantify residual fiber sizes after each candidate packet and verify the sharp cases by a deterministic bounded census that is declared before reading the census outcomes;
7. prove the orientation firewall: a `Gamma`-invariant alignment packet may reconstruct `K/Gamma` but may not be relabeled as the oriented Pfaffian scalar `Q=t1-t2+t3`; classify any remaining one/two/three-candidate scalar ambiguity without opening a signed-native or Full-Cell route;
8. include a prior-art classification for the finite-group/multisymmetric invariant ingredients so no standard invariant-theory generator theorem is presented as an Enterprise novelty;
9. supply a task-local exact checker/certificate and a NEW immutable Result whose output manifest pins every frozen output with Git blob SHA-1 plus SHA-256.

## Research value to preserve

The parent result turns a vague coupling question into a sharp information problem: the separate raw-sum and product packets can leave exactly six admissible alignment orbits, while the fully aligned packet is complete modulo the declared derived symmetry. Finding the smallest natural exact algebraic encoding of that finite residue would compress the useful arithmetic state without carrying redundant Tropical or Johnson coordinates. A negative answer is equally valuable because it establishes an exact irreducibility boundary for this frozen grammar.

## Success, kill, and return criteria

Terminal success is one of: `MINIMAL_MIXED_PACKET_FOUND`, `ALL_FROZEN_MOMENTS_REQUIRED`, or `FROZEN_GRAMMAR_INSUFFICIENT_WITH_EXACT_COLLISIONS`, provided the conclusion is exact and accompanied by reconstruction proofs or counterexamples. Kill any inference from these coordinate invariants to native P000 orientation, native signed carrier structure, native dimension reduction, factorization, or Full-Cell dynamics. Do not extend the candidate grammar after seeing collisions; a richer grammar, if later justified, is a separate control decision. Do not create a new general-purpose tool when the task-local exact checker and existing algebraic machinery suffice. Return a NEW immutable Result for Driver review and make no downstream task decision from the researcher lane.
