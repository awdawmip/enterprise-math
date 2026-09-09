<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-P11-OFF-DIAGONAL-EQUAL-AREA-FIBER-PRODUCT",
  "title": "P000 P11 off-diagonal equal-area fiber-product arithmetic",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "The simultaneous C1/C2 arithmetic component has an exact two-equal-area-triangle normal form. Its h=0 fixed locus is now reduced to elliptic fibers, leaving the h!=0 primitive locus with two distinct triangle factors, nonzero row coupling and two square cuts unclassified.",
  "next_action": "Keep both triangle-factor identities and the exact P11 reconstruction data, derive the smallest arithmetic model for the h!=0 locus, and prove primitive families, a complete component classification, or the exact higher arithmetic obstruction.",
  "dependencies": ["RR-DA840CA11911B721506F", "RR-764F6E463528167708E9"],
  "source_refs": [
    "research_result_records/RS-P000-SIX-AXIS-P11-SIMULTANEOUS-C1-C2-AP-PAIRABILITY/RR-DA840CA11911B721506F.json",
    "research_returns/P000_SIX_AXIS_P11_SIMULTANEOUS_C1_C2_AP_PAIRABILITY_RETURN_20260902.md",
    "research_result_records/RS-P000-SIX-AXIS-P11-DIAGONAL-SHARED-LEG-PYTHAGOREAN-TRIPLE/RR-764F6E463528167708E9.json",
    "research_returns/P000_SIX_AXIS_P11_DIAGONAL_SHARED_LEG_PYTHAGOREAN_TRIPLE_RETURN_20260904.md",
    "definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json",
    "p000_reality_foundation.json"
  ],
  "evidence_status": "SIMULTANEOUS_PARENT_DRIVER_ACCEPTED / DIAGONAL_SUBLOCUS_TERMINAL / OFF_DIAGONAL_PRIMITIVE_ARITHMETIC_OPEN / JOINT_OBSERVER_DATA_RETAINED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": ["P000", "P11", "off-diagonal", "equal-area", "fiber-product", "Diophantine", "joint-observer"],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-P11-OFF-DIAGONAL-EQUAL-AREA-FIBER-PRODUCT",
  "parent_objective_id": "OBJ-P000-SIX-AXIS-ARITHMETIC-TROPICAL-INTEGRATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000P11O1",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P000-SIX-AXIS-P11-SIMULTANEOUS-C1-C2-AP-PAIRABILITY",
  "successor_gate": {
    "new_information_gap": "The simultaneous C1/C2 parent gives a necessary-and-sufficient equal-area two-triangle normal form. The diagonal h=0 sublocus is now terminally reduced to elliptic fibers, but the complementary h!=0 primitive locus with two distinct equal-area triangle factors remains unclassified.",
    "why_parent_result_does_not_close_it": "The simultaneous parent proved existence and exact reduction but deliberately left global primitive classification open. The diagonal successor removes only the fixed locus; it provides no theorem for distinct triangle factors, nonzero row coupling, or the off-diagonal primitive quotient.",
    "discriminating_outcomes": [
      "explicit infinite primitive off-diagonal families are proved and parametrized at the strongest exact level",
      "the off-diagonal locus decomposes into finitely many exact arithmetic components with a complete primitive classification",
      "the locus reduces to a precise elliptic, higher-genus, surface, or fiber-product obstruction with exact reconstruction filters"
    ],
    "kill_condition": "Do not collapse the two triangle factors to an unordered or factor-only summary before proving observer safety, do not delete composite/joint relation data from reconstructibility alone, and do not turn finite search or derived Euclidean structure into native P000 claims.",
    "alternative_route_or_free_exploration_considered": "Closing the line after the diagonal result was considered, as was pursuing only the elliptic fixed-locus family. The complementary h!=0 locus is retained as a parallel task because it is a disjoint structural branch of the already-accepted simultaneous arithmetic component and contains the original zero-column primitive witness that the diagonal branch cannot represent.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The simultaneous parent is terminal at exact-component strength and the diagonal task is terminal on h=0. A separate off-diagonal task prevents the harder two-factor arithmetic from contaminating the completed fixed-locus theorem while preserving the remaining parent objective."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:1f84e78de591605da6106f3f14ffad3cd7fad66aa5bf67e29beb44906b976c8a",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P000 P11 off-diagonal equal-area fiber-product arithmetic

## Mother question

Classify the primitive `h != 0` part of the accepted simultaneous C1/C2 arithmetic component.

The full derived normal form consists of two ordered integer right triangles of the same area,

\[
x^2+y^2=b^2,\qquad X^2+Y^2=g^2,\qquad xy=XY=2e,
\]

together with

\[
g^2-b^2=4hd
\]

and the two exact middle-row square cuts. The diagonal `h=0` branch is now separately reduced to elliptic fibers. What is the exact arithmetic structure of the complementary branch where the two equal-area triangle factors are distinct?

## Frozen inputs and scope

Freeze the accepted simultaneous Result `RR-DA840CA11911B721506F` and the terminal diagonal Result `RR-764F6E463528167708E9` at their stated derived-arithmetic strengths.

The two triangle factors are labeled relational data before the accepted swap involution is taken. Preserve their identities, common-area coupling, row-coupling sign, square-cut witnesses, parity, recovered roots and common-root primitive normalization. An unordered quotient may be used only after proving that the declared reconstruction and all task outputs factor through it.

The current joint-relation observer constraint is load-bearing here: knowledge that each triangle or composite datum can be reconstructed from constituents is not by itself a certificate that the interaction direction is redundant. Retain the equal-area and cross-factor relations until an exact scoped descent/span certificate is proved.

Current P000 remains the locked native six-axis ontology. Classical right triangles, congruent-number curves and any resulting algebraic varieties are derived arithmetic carriers only.

## Hard target and required outputs

Hard target:

`P000_P11_OFF_DIAGONAL_EQUAL_AREA_FIBER_PRODUCT_PRIMITIVE_ARITHMETIC_CLASSIFIED_OR_EXACT_OBSTRUCTION`.

Required outputs:

1. write an exact necessary-and-sufficient h-nonzero system starting from the accepted two-triangle normal form, with no loss of sign, parity, zero/composite values, multiplicity or factor provenance;
2. parameterize each integer right-triangle factor completely and impose the equal-area condition as an exact joint relation rather than treating the factors independently;
3. express `g^2-b^2=4hd` and both middle-row square cuts in the smallest exact parameter carrier, proving every denominator and integrality condition;
4. derive the common recovered-root gcd and prove the primitive quotient in the new coordinates;
5. determine whether the off-diagonal locus contains explicit infinite primitive families; if yes prove at least one family and its P11 reconstruction, and if not isolate the exact arithmetic obstruction to the tested natural families;
6. classify the zero-product-column witness family and other sign chambers separately, without treating a boundary family as representative of the entire off-diagonal locus;
7. identify the exact algebraic object controlling the residual arithmetic—fiber product, elliptic curve, higher-genus curve, surface, or another object—and prove the reduction rather than naming it by analogy;
8. apply BRC to the labeled two-factor carrier when it preserves the required observer data, or record a precise inapplicability boundary; any compression must list retained and erased information and prove reconstruction safety;
9. predeclare any finite control and use it only for falsification/regression;
10. distinguish classical Pythagorean/congruent-number/descent machinery from task-specific P11 specialization and return a NEW immutable Result with complete evidence bindings.

## Research value to preserve

The off-diagonal branch is the part of the simultaneous collision problem that still genuinely couples two different equal-area representations. It is therefore the strongest remaining test of whether the one-bit alignment ambiguity discovered earlier hides a richer Diophantine interaction or only a collection of classical arithmetic fibers.

Keeping the two factors and their joint relation visible also directly exercises the current project rule against deleting composite/joint observation directions merely because factor data exist.

## Success, kill, and return criteria

Terminal success is one of:

- `OFF_DIAGONAL_EQUAL_AREA_INFINITE_PRIMITIVE_FAMILIES_PROVED`;
- `OFF_DIAGONAL_EQUAL_AREA_PRIMITIVE_COMPONENTS_COMPLETELY_CLASSIFIED`;
- `OFF_DIAGONAL_EQUAL_AREA_EXACT_HIGHER_ARITHMETIC_OBSTRUCTION_ISOLATED`.

Kill any proof that silently identifies the two factors, drops their pairing/provenance without a scoped certificate, relies on a bounded census as a global theorem, or assigns native P000 meaning to the derived Euclidean carrier.

Return exact formulas, proofs or falsifiers, the full primitive reconstruction map, BRC observer accounting, and the smallest unresolved unit. The line Driver decides subsequent routing.
