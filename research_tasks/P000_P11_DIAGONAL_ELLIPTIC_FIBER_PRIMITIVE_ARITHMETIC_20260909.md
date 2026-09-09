<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-P11-DIAGONAL-ELLIPTIC-FIBER-PRIMITIVE-ARITHMETIC",
  "title": "P000 P11 diagonal elliptic-fiber primitive arithmetic",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Driver-accepted fixed-locus work reduces each primitive Euclidean Pythagorean core to an explicit smooth genus-one fiber with exact parity, positivity and recovered-root-gcd filters; the global primitive arithmetic of the fiber family remains open.",
  "next_action": "Derive an exact uniform arithmetic interface for the fiber family, test descent and rational/integral-point structure without losing core provenance, and prove an infinite primitive family, a complete uniform classification, or the smallest exact remaining obstruction.",
  "dependencies": ["RR-764F6E463528167708E9"],
  "source_refs": [
    "research_result_records/RS-P000-SIX-AXIS-P11-DIAGONAL-SHARED-LEG-PYTHAGOREAN-TRIPLE/RR-764F6E463528167708E9.json",
    "research_returns/P000_SIX_AXIS_P11_DIAGONAL_SHARED_LEG_PYTHAGOREAN_TRIPLE_RETURN_20260904.md",
    "definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json",
    "p000_reality_foundation.json"
  ],
  "evidence_status": "PARENT_RESULT_DRIVER_ACCEPTED_REQUIRED / EXPLICIT_ELLIPTIC_FIBERS / UNIFORM_PRIMITIVE_ARITHMETIC_OPEN / DERIVED_ARITHMETIC_ONLY",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": ["P000", "P11", "elliptic", "Diophantine", "primitive", "fixed-locus", "BRC-observer-preservation"],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-P11-DIAGONAL-ELLIPTIC-FIBER-PRIMITIVE-ARITHMETIC",
  "parent_objective_id": "OBJ-P000-SIX-AXIS-ARITHMETIC-TROPICAL-INTEGRATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000P11E1",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P000-SIX-AXIS-P11-DIAGONAL-SHARED-LEG-PYTHAGOREAN-TRIPLE",
  "successor_gate": {
    "new_information_gap": "The accepted diagonal fixed-locus Result reduces every primitive Euclidean core to an explicit smooth genus-one fiber, but it does not determine the rational/integral-point structure uniformly across those fibers or whether the primitive P11 fixed-locus population is globally infinite.",
    "why_parent_result_does_not_close_it": "The parent is terminal at exact genus-one obstruction strength. It supplies a birational quartic, exact reconstruction filters and a finite falsification census, while explicitly leaving uniform Mordell-Weil, descent and global primitive-point classification open.",
    "discriminating_outcomes": [
      "a uniform arithmetic mechanism produces and proves one or more infinite primitive fixed-locus families with exact reconstruction",
      "a finite set of explicitly characterized fiber types controls all primitive solutions under a proved uniform descent",
      "the family cannot be uniformly reduced at the requested strength and the exact remaining arithmetic obstruction is isolated with its parameter dependence"
    ],
    "kill_condition": "Do not promote any finite census to a global theorem, do not erase Euclidean-core or recovered-root provenance by an uncertified quotient, and do not reinterpret this derived elliptic arithmetic as native P000 geometry.",
    "alternative_route_or_free_exploration_considered": "Closing the local line was considered because the parent already reaches genus one, and immediately returning to the off-diagonal branch was also considered. This task is retained as one of two parallel continuations because the fixed locus is a canonically distinguished subvariety with a sharply smaller arithmetic object and a concrete unresolved global question.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent hard target was to classify the fixed locus or isolate its exact higher arithmetic obstruction; that target is complete. This task changes the mother question from reduction to the uniform arithmetic of the resulting elliptic-fiber family."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:1f84e78de591605da6106f3f14ffad3cd7fad66aa5bf67e29beb44906b976c8a",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P000 P11 diagonal elliptic-fiber primitive arithmetic

## Mother question

For the exact `h=0` P11 fixed locus, the preceding task reduced each primitive Euclidean core to the smooth genus-one fiber

\[
C_{P,Q}:\quad U^2+D^2=P^2Z^2,\qquad V^2+D^2=Q^2Z^2
\]

and to the quartic

\[
Y^2=((P+Q)^2-T^2)(T^2-(P-Q)^2).
\]

What uniform arithmetic controls the primitive integral P11 points across this family? In particular, is there a provable infinite primitive family, a complete uniform descent/classification, or a precise parameter-dependent obstruction that prevents either conclusion?

## Frozen inputs and scope

Freeze the accepted Result `RR-764F6E463528167708E9` at derived-arithmetic strength. Preserve the Euclidean core `(r,s)`, the scale and denominator data, parity, strict inequalities, recovered outer-root gcd, and the exact map back to the P11 datum throughout any elliptic transformation.

Current P000 is the locked six-axis native ontology; these Euclidean Pythagorean and elliptic objects are arithmetic facades inside the already-derived P11 coordinate calculus. They do not define a native right angle, native direction, native force balance, or a reduction of native dimension.

Because this task compares fibers and reconstruction maps, retain joint relation and provenance coordinates until an exact observer-safe factorization or descent certificate proves a quotient sufficient for the stated arithmetic outputs. Apply the current BRC gate to the selected carrier/observer when it is genuinely typed; if no useful branching interface exists, record the exact applicability boundary rather than inventing one.

## Hard target and required outputs

Hard target:

`P000_P11_DIAGONAL_ELLIPTIC_FIBER_PRIMITIVE_ARITHMETIC_CLASSIFIED_OR_UNIFORM_OBSTRUCTION`.

Required outputs:

1. derive a canonical Weierstrass/Jacobian presentation for `C_{P,Q}` or prove why the quartic/intersection model is the sharper uniform carrier, with exact forward and inverse maps on the task-relevant domain;
2. compute the torsion and the strongest exact uniform local or descent information available as functions of the primitive Euclidean core;
3. distinguish rational points from integral P11-reconstructible points and carry all denominator, parity, positivity and recovered-root-gcd filters through the transformation;
4. prove at least one explicit infinite primitive fixed-locus family, or prove an exact obstruction to the natural parameter families tested; do not infer infinitude from increasing finite counts;
5. determine whether the current evidence supports a uniform finite classification of primitive points; if it does not, identify the smallest precise arithmetic quantity that remains uncontrolled;
6. use the known points `(176,57,185;105,208,56)` and `(2720,165,2725;1533,2444,2044)` as regression/falsification inputs, not as assumed generators of all solutions;
7. test the observer/provenance safety of every normalization or quotient used and retain a repair coordinate whenever the P11 reconstruction does not factor exactly;
8. separate classical elliptic-curve, descent, height, Pell or local-global machinery from any task-specific P11 specialization;
9. supply exact symbolic derivations plus deterministic checks for every finite certificate used;
10. return a NEW immutable Result with complete output bindings and an explicit statement of what remains global, conditional, finite, or unproved.

## Research value to preserve

The preceding task shows that the diagonal collision branch is not an elementary one-seed scaling phenomenon: its primitive arithmetic lives on a family of elliptic curves indexed by Euclidean cores. The next high-value question is therefore not a larger census, but whether the family itself has a uniform arithmetic mechanism that can be carried back to exact P11 primitive data.

A positive family theorem would expose a genuine infinite arithmetic structure. A negative or obstruction result would identify precisely where uniform classification fails and prevent repeated bounded searches from masquerading as progress.

## Success, kill, and return criteria

Terminal success is one of:

- `DIAGONAL_ELLIPTIC_FIBER_INFINITE_PRIMITIVE_FAMILY_PROVED`;
- `DIAGONAL_ELLIPTIC_FIBER_UNIFORM_PRIMITIVE_CLASSIFICATION_PROVED`;
- `DIAGONAL_ELLIPTIC_FIBER_EXACT_UNIFORM_ARITHMETIC_OBSTRUCTION_ISOLATED`.

Kill any argument that uses only finite enumeration, drops the Euclidean core or outer-root provenance without an exact safety theorem, conflates rational with integral reconstructible points, or promotes the derived Euclidean model into native P000 geometry.

The Researcher returns theorem-strength statements, exact evidence, BRC applicability/resolution, prior-mathematics attribution, and the smallest unresolved arithmetic unit. Downstream line decisions belong to the line Driver.
