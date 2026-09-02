<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-SIX-AXIS-P11-DIAGONAL-SHARED-LEG-PYTHAGOREAN-TRIPLE",
  "title": "P000 P11 diagonal shared-leg Pythagorean triple-of-triples classification",
  "kind": "RESEARCH",
  "owner": "research/p000-six-axis-p11-diagonal-shared-leg-pythagorean-triple",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "The accepted simultaneous C1/C2 normal form identifies the involution fixed locus exactly by h=0, where the two equal-area triangle factors coincide. The locus reduces to one integer right triangle (x,y,b) together with two additional right triangles (d,mu,x+y) and (d,nu,x-y) sharing the same leg d. One primitive witness is known, but the complete primitive Diophantine structure of this fixed locus is open.",
  "next_action": "Parameterize the base integer right triangle and the two shared-leg square cuts, quotient common recovered-root scaling, and prove a complete primitive family classification or isolate the exact Pell, elliptic, higher-genus, or other arithmetic obstruction; actively falsify the hypothesis that every primitive fixed-locus point scales from the known witness.",
  "dependencies": [
    "RR-DA840CA11911B721506F"
  ],
  "source_refs": [
    "research_result_records/RS-P000-SIX-AXIS-P11-SIMULTANEOUS-C1-C2-AP-PAIRABILITY/RR-DA840CA11911B721506F.json",
    "research_returns/P000_SIX_AXIS_P11_SIMULTANEOUS_C1_C2_AP_PAIRABILITY_RETURN_20260902.md"
  ],
  "evidence_status": "PARENT_RESULT_DRIVER_ACCEPTED_REQUIRED / H0_FIXED_LOCUS_PRIMITIVE_CLASSIFICATION_OPEN / DERIVED_ARITHMETIC_ONLY",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "P000",
    "six-axis",
    "P11",
    "simultaneous-C1-C2",
    "fixed-locus",
    "Pythagorean",
    "Diophantine",
    "shared-leg"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-SIX-AXIS-P11-DIAGONAL-SHARED-LEG-PYTHAGOREAN-TRIPLE",
  "parent_objective_id": "OBJ-P000-SIX-AXIS-ARITHMETIC-TROPICAL-INTEGRATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000P11D2",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P000-SIX-AXIS-P11-SIMULTANEOUS-C1-C2-AP-PAIRABILITY",
  "successor_gate": {
    "new_information_gap": "The parent proves the complete equal-area Pythagorean normal form for simultaneous C1/C2 data and identifies its involution fixed locus by h=0, but it does not classify the primitive integer points on that lower-dimensional fixed locus. There the two triangle factors coincide and the remaining square cuts become a coupled triple of Pythagorean equations with a shared leg.",
    "why_parent_result_does_not_close_it": "The parent is terminal at existence-plus-exact-component strength. Its h=0 theorem is a structural reduction, not a primitive-point classification: only one fixed-locus primitive witness is frozen, and no completeness, infinite-family theorem, or arithmetic obstruction is proved for the shared-leg system.",
    "discriminating_outcomes": [
      "all primitive diagonal fixed-locus points are covered by finitely many explicit integer or rational parameter families",
      "there are one or more explicit infinite primitive families but additional components remain and can be exactly separated",
      "complete elementary parametrization is obstructed by a precisely identified Pell, elliptic, higher-genus, descent, or higher-dimensional arithmetic component"
    ],
    "kill_condition": "Do not treat any bounded census as a global theorem, do not assume every primitive point is a scale or symmetry image of the known seed, do not widen to the off-diagonal two-triangle fiber product before this fixed-locus task is terminal, and do not infer native orientation, Pfaffian-slot choice, P000 dimension reduction, factorization, or Full-Cell dynamics.",
    "alternative_route_or_free_exploration_considered": "Closing the arithmetic route was considered because simultaneous existence and the full equal-area normal form are established. A global attack on all off-diagonal primitive points was also considered, but it retains two independent equal-area triangle factors. The h=0 fixed locus is preferred because it is canonically selected by the accepted involution, removes one triangle factor, and exposes a smaller shared-leg Diophantine system.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent hard target is satisfied by existence plus exact reduction to an arithmetic component. The new task changes the mother question from existence/reduction of the full simultaneous locus to primitive classification of its exact involution-fixed subvariety, with separate completion and obstruction outcomes."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P000 P11 diagonal shared-leg Pythagorean triple-of-triples classification

## Mother question

Classify the primitive integer points on the exact `h=0` fixed locus of the accepted simultaneous C1/C2 arithmetic component.

On this locus the two equal-area triangle factors coincide. Write the common ordered integer right triangle as

`x^2 + y^2 = b^2`, with `x>y>0`,

and let `d>0` be the AP half-gap. The two remaining pairability cuts become

`d^2 + mu^2 = (x+y)^2`,

`d^2 + nu^2 = (x-y)^2`.

Thus one simultaneous fixed-locus point is equivalent to three coupled integer right triangles, the last two sharing the same leg `d`. What is the complete primitive Diophantine structure of this system modulo the already-known common recovered-root scaling?

## Frozen inputs and scope

Freeze accepted Result `RR-DA840CA11911B721506F` at derived six-coordinate arithmetic strength.

Use exactly the accepted facts:

- simultaneous genuine C1/C2 data are represented by the equal-area Pythagorean normal form;
- the C1/C2 AP involution is triangle-factor swap with `h -> -h`;
- its fixed locus is exactly `h=0`, equivalently equality of the two ordered equal-area triangle factors;
- on `h=0`, the two middle-row square cuts reduce to the shared-leg equations displayed in the mother question;
- the primitive quotient is the gcd of all recovered outer roots;
- the fixed locus lies in the nonpositive-product chamber under the accepted AP reconstruction.

Retain zero roots, negative roots, even roots, composite roots and small-prime factors wherever the exact equations allow them. Euclidean Pythagorean parameterization, Pell equations, elliptic curves, descent and higher-genus curve theory may be used as classical mathematics with explicit attribution.

All conclusions remain a derived arithmetic facade. This task does not define or select native orientation, a Pfaffian sign slot, a lower native dimension, factorization semantics, or Full-Cell dynamics.

## Hard target and required outputs

Hard target:

`P000_P11_DIAGONAL_FIXED_LOCUS_PRIMITIVE_TRIPLE_OF_TRIPLES_CLASSIFIED_OR_EXACT_ARITHMETIC_OBSTRUCTION`.

Required outputs:

1. prove the exact necessary-and-sufficient equivalence between a primitive `h=0` simultaneous datum and the coupled system
   `x^2+y^2=b^2`,
   `d^2+mu^2=(x+y)^2`,
   `d^2+nu^2=(x-y)^2`,
   including the exact parity and AP reconstruction conditions;
2. express the common recovered-root gcd in the shared-leg coordinates and prove the primitive normalization is complete;
3. apply a complete integer parameterization of the base Pythagorean triangle and derive the induced arithmetic conditions on `d,mu,nu` rather than treating the three equations independently;
4. determine whether all primitive solutions lie in finitely many explicit parameter families; if yes, prove completeness, and if not, isolate the exact arithmetic component obstructing such a parametrization;
5. recover the known primitive witness
   `(x,y,b;d,mu,nu)=(176,57,185;105,208,56)`
   from the classification rather than inserting it as an exceptional case;
6. actively search for and either exhibit or rule out a primitive solution not obtained from the known witness by common scaling and the declared finite presentation symmetries;
7. classify zero-root and sign-boundary subfamilies permitted by the AP reconstruction and distinguish genuine primitive strata from nonprimitive scaling artifacts;
8. derive and use exact secondary identities such as `mu^2-nu^2=4xy` only at the strength justified by the system;
9. choose a finite full-integer control range before inspecting its outcomes and use the census only as regression/falsification evidence;
10. identify any classical Pythagorean, Pell, congruent-number, elliptic, descent, local-global, or higher-genus machinery as prior mathematics and separate it from the task-specific specialization;
11. supply an exact task-local checker/certificate and a NEW immutable Result with complete Git blob SHA-1 and SHA-256 bindings for every frozen output.

## Research value to preserve

The simultaneous C1/C2 problem unexpectedly has genuine integer solutions and an exact equal-area Pythagorean description. Its involution fixed locus is the first place where that broad fiber product collapses to a visibly smaller object: a triple of integer right triangles coupled through one shared leg.

A complete classification here would identify the arithmetic source of the diagonal primitive branch and show whether the current negative-product witness is isolated, part of an elementary infinite family, or merely one rational/integral point on a harder arithmetic component. A precise obstruction would be equally valuable because it would locate the remaining difficulty without reopening broader invariant or native-geometric routes.

## Success, kill, and return criteria

Terminal success is one of:

- `DIAGONAL_FIXED_LOCUS_FINITE_PRIMITIVE_PARAMETER_FAMILIES_COMPLETE`;
- `DIAGONAL_FIXED_LOCUS_INFINITE_PRIMITIVE_FAMILIES_WITH_EXACT_RESIDUAL_COMPONENTS`;
- `DIAGONAL_FIXED_LOCUS_REDUCED_TO_EXACT_NONRATIONAL_OR_HIGHER_ARITHMETIC_COMPONENT`.

A successful Return must prove equivalence and primitive normalization symbolically, distinguish global theorem from bounded computation, and stop at the first exact classification or obstruction. It must not widen to the off-diagonal simultaneous locus merely because the fixed-locus arithmetic becomes difficult. Return a NEW immutable Result for Driver review; the Researcher lane makes no downstream task decision.
