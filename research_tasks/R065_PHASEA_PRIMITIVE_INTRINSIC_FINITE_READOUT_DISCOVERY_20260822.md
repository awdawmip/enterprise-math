<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R065-PHASEA-PRIMITIVE-INTRINSIC-FINITE-READOUT-DISCOVERY",
  "title": "R065 Phase A — Primitive Intrinsic Finite Readout Discovery",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "PRIMITIVE_SUBSTRATE_INTRINSIC_READOUT_OR_NO_GO_CLASSIFICATION",
  "next_action": "Using only the blind primitive packet, classify all theorem-relevant intrinsic finite relation/readout candidates or prove exact underdetermination, freeze one independent candidate/no-go packet, and stop before any post-freeze project comparison.",
  "dependencies": [
    "research_inputs/R065_PHASEA_BLIND_PRIMITIVE_PACKET_20260822.md@00765cc76ea71f789481fbe91c29d852bbf6b209"
  ],
  "source_refs": [
    "research_inputs/R065_PHASEA_BLIND_PRIMITIVE_PACKET_20260822.md@00765cc76ea71f789481fbe91c29d852bbf6b209"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "R065",
    "phase-a",
    "blind-discovery",
    "primitive-substrate",
    "finite-readout",
    "independent-context",
    "foundation-facing"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R065A",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
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

# R065 Phase A — Primitive Intrinsic Finite Readout Discovery

Task-ID: `RS-R065-PHASEA-PRIMITIVE-INTRINSIC-FINITE-READOUT-DISCOVERY`

Origin: `DIRECT_USER_DIRECTION`

Lineage: `NEW_DIRECTION`

Identity lane: `R065A`

Intended owner branch:

`research/r065-phasea-primitive-intrinsic-readout`

## 0. Phase-A information firewall

This task is an independent discovery attempt.

Before the Phase-A candidate/no-go packet is frozen, read only:

`research_inputs/R065_PHASEA_BLIND_PRIMITIVE_PACKET_20260822.md`

at source:

`00765cc76ea71f789481fbe91c29d852bbf6b209`.

Do not open other project-specific mathematical sources before freeze. In particular, do not use numbered research routes, current metric/length/root/line definitions, Driver reviews, journals, Foundation-question results, route summaries, or prior candidate packets as mathematical evidence.

The taskbook intentionally supplies no target formula, target state count, target relation, target algebra, or known successful readout.

Ordinary finite/discrete mathematics is allowed.

If the information boundary is violated before freeze, preserve the mathematics but mark the independent-discovery status as not clean.

## 1. Mother question

Given only the finite typed component substrate in the blind primitive packet, determine whether it canonically supports any nontrivial intrinsic finite relation, quotient, observable, or scalar readout that could encode a meaningful notion of finite magnitude/scale without importing an external formula.

Hard target:

`PRIMITIVE_SUBSTRATE_INTRINSIC_FINITE_READOUT_CLASSIFIED`.

A complete answer may be positive, nonunique, or negative.

The task must distinguish:

1. primitive structure already supplied by the packet;
2. parameter-free relations/objects definable from that structure;
3. scalar/cardinal readouts derived from such objects;
4. extra operational or semantic assignments not forced by the substrate;
5. presentation artifacts or arbitrary encodings.

## 2. Start from the definability space, not from a formula

First enumerate the smallest theorem-relevant classes of finite constructions available from the primitive packet.

Possible construction ingredients may include only what is actually justified from the packet and ordinary finite mathematics, such as:

- token equality/inequality;
- component-type equality/inequality;
- sector incidence;
- finite subsets and relations;
- quotients/equivalence relations if independently motivated;
- products, unions, intersections or other finite constructions if independently motivated;
- component-content composition by admissible disjoint union;
- finite cardinal/readout operations only after the underlying object being counted is specified.

This list is not a menu of preferred answers. Derive the relevant construction language and record why each theorem-critical operation is admissible.

Do not assume in advance:

- polynomial degree;
- squaring;
- pair capacity;
- bilinearity;
- additivity;
- multiplicativity;
- monotonicity;
- an inner product;
- a norm;
- a metric;
- a preferred observation resolution;
- a preferred component erasure;
- a target scalar formula.

Required artifact:

`research_results/R065_PHASEA/R065_PHASEA_DEFINABILITY_SPACE.md`.

## 3. Intrinsicness and symmetry gate

Any retained candidate must be presentation-independent at the exact strength claimed.

At minimum classify:

- invariance under renaming of individual finite tokens;
- behavior under the full `S3` relabeling of component types;
- dependence or independence on choosing one two-component sector;
- dependence or independence on ordering the two component names inside a sector;
- whether the construction survives passage to an unlabeled structural isomorphism class.

A construction that depends on arbitrary token indices, lexical ordering, a preferred axis name, or a hidden orientation without an independent certificate is not intrinsic.

Required artifact:

`research_results/R065_PHASEA/R065_PHASEA_INVARIANCE_CERTIFICATE.json`.

## 4. Candidate generation

Generate every serious minimal candidate family that survives the intrinsicness gate at the declared semantic type.

For each candidate `C`, record:

- carrier/object type;
- exact construction from primitive data;
- definability DAG;
- free parameters, if any;
- invariance group;
- whether it is relation-valued, quotient-valued, multiset-valued, scalar-valued, or another finite type;
- whether repeated/admissible content composition induces any law on `C`;
- smallest input on which it differs from another surviving candidate.

Do not select one candidate merely because it is simple or familiar.

If a relation/object is more canonical than a scalar readout of it, preserve that distinction.

Required artifact:

`research_results/R065_PHASEA/R065_PHASEA_CANDIDATE_FAMILY.md`.

## 5. Scalar/readout gate

If a scalar-valued candidate is proposed, determine exactly what makes the scalar intrinsic.

Separate:

`underlying finite object`

from

`numerical readout of that object`.

If the readout is a cardinality or another valuation, state the axioms actually used to derive or select that valuation and classify whether those axioms are themselves forced by the primitive packet.

If multiple inequivalent scalarizations of the same finite object survive, preserve the family and identify the missing principle.

If a scalar is only meaningful after assigning it a role such as magnitude, scale, distance, energy, or any other interpretation, classify that role assignment separately from the mathematical scalar construction.

## 6. Composition laws must be discovered or falsified

The primitive packet supplies component-content composition but no law for an unknown readout.

For every serious candidate, test rather than assume:

- identity behavior at empty and unit contents;
- behavior under repetition of one component;
- behavior under component-disjoint union;
- behavior when two nonzero component multiplicities coexist;
- symmetry under component relabeling;
- associativity/commutativity only if the candidate itself defines a composition;
- functoriality under admissible typed bijections.

If an algebraic law fails, preserve the smallest counterexample.

If a law holds only after adding an extra assumption, mark it conditional and do not fold that assumption into the primitive substrate.

Required artifact:

`research_results/R065_PHASEA/R065_PHASEA_COMPOSITION_LAW_CLASSIFICATION.md`.

## 7. Uniqueness / no-go pressure test

A positive uniqueness claim must defeat all alternatives of the same declared semantic type using a theorem, not aesthetic preference.

Actively search for inequivalent competitors produced by:

- retaining more primitive distinctions;
- forgetting more primitive distinctions;
- using a different finite relation/quotient construction;
- using a different admissible valuation/readout;
- changing only a theorem-irrelevant presentation.

Do not preselect which of these should win.

If two inequivalent intrinsic candidates satisfy every justified requirement, freeze nonuniqueness and state the weakest additional datum/axiom that would separate them.

If no nontrivial candidate survives without extra choices, prove the strongest exact no-go and stop.

Required artifact:

`research_results/R065_PHASEA/R065_PHASEA_UNIQUENESS_OR_NO_GO.md`.

## 8. Semantic typing

Create a current-schema claim ledger:

`research_results/R065_PHASEA/R065_PHASEA_SEMANTIC_SCOPE_CLAIM_LEDGER.json`.

For every theorem-critical object distinguish at minimum:

- primitive relation/object;
- definable derived relation/object;
- numerical readout;
- conditional operational assumption;
- semantic role assignment;
- implementation-only carrier.

A finite scalar is not automatically primitive merely because it is exact or canonical as a number.

No Phase-A result may install a new Foundation primitive inside this task.

## 9. Blind candidate/no-go freeze

Before any post-freeze comparison, write:

`research_results/R065_PHASEA/R065_PHASEA_BLIND_CANDIDATE_OR_NO_GO_FREEZE.json`.

If positive, it must contain at least:

- `candidate_id`;
- `candidate_statement`;
- `foundation_snapshot_ref` set to the blind packet source;
- `worldview_snapshot_ref_or_none`;
- `primitive_dependencies`;
- `semantic_layer`;
- `structural_motivation_without_active_route_reference`;
- `immediate_consequences`;
- `obvious_falsifiers`;
- `blindness_status`;
- `created_at_or_content_hash`.

If negative, record an equivalent exact no-go statement, weakest hypotheses, smallest counterexample/model where applicable, and the same blindness/provenance information.

Also create:

`research_results/R065_PHASEA/R065_PHASEA_CONTEXT_INDEPENDENCE_CERTIFICATE.json`.

The certificate must state whether any project-specific source other than the blind packet was accessed before freeze.

## 10. Deterministic checker

Create:

`scripts/r065_phasea_validate_primitive_intrinsic_readout.py`.

Use exact finite/integer/relational operations only for theorem decisions.

The checker must not contain a hidden target formula used to choose the candidate.

At minimum it must:

1. instantiate every sector-supported content with each component multiplicity `0..6`;
2. verify all admitted `S3` relabelings on the tested domain;
3. verify invariance under token renaming symbolically or by canonical finite-isomorphism reduction;
4. reproduce every claimed candidate construction from primitive data;
5. test all claimed composition laws on the declared domain;
6. exhibit smallest counterexamples for rejected laws/candidates where finite search applies;
7. compare all retained candidate families on the tested domain;
8. report zero unclassified mismatches or preserve the exact residual mismatch set.

Finite checking supports but does not replace general proofs.

## 11. Required outputs

Produce at minimum:

1. `research_results/R065_PHASEA/R065_PHASEA_PRIMITIVE_INVENTORY.json`;
2. `R065_PHASEA_DEFINABILITY_SPACE.md`;
3. `R065_PHASEA_CANDIDATE_FAMILY.md`;
4. `R065_PHASEA_INVARIANCE_CERTIFICATE.json`;
5. `R065_PHASEA_COMPOSITION_LAW_CLASSIFICATION.md`;
6. `R065_PHASEA_UNIQUENESS_OR_NO_GO.md`;
7. `R065_PHASEA_SEMANTIC_SCOPE_CLAIM_LEDGER.json`;
8. `R065_PHASEA_BLIND_CANDIDATE_OR_NO_GO_FREEZE.json`;
9. `R065_PHASEA_CONTEXT_INDEPENDENCE_CERTIFICATE.json`;
10. `R065_PHASEA_COUNTEREXAMPLES.json`;
11. `R065_PHASEA_REGRESSION.json`;
12. `R065_PHASEA_MISMATCHES.json`;
13. `R065_PHASEA_FINAL_CLASSIFICATION.md`;
14. `scripts/r065_phasea_validate_primitive_intrinsic_readout.py`.

## 12. Acceptance gates

The final packet must classify:

1. `BLIND_PACKET_IS_ONLY_PROJECT_SPECIFIC_PHASEA_INPUT`;
2. `PRIMITIVE_INVENTORY_COMPLETE`;
3. `NO_TARGET_FORMULA_OR_PRIOR_CANDIDATE_USED_BEFORE_FREEZE`;
4. `DEFINABILITY_SPACE_EXPLICIT`;
5. `TOKEN_RENAMING_INVARIANCE_CLASSIFIED`;
6. `S3_COMPONENT_RELABELING_EQUIVARIANCE_CLASSIFIED`;
7. `SERIOUS_CANDIDATE_FAMILY_OR_EXACT_NO_GO_CLASSIFIED`;
8. `UNDERLYING_OBJECT_SEPARATED_FROM_NUMERICAL_READOUT`;
9. `COMPOSITION_LAWS_DERIVED_OR_FALSIFIED_NOT_ASSUMED`;
10. `UNIQUENESS_OR_EXACT_MISSING_DATUM_CLASSIFIED`;
11. `SEMANTIC_SCOPE_CLAIM_LEDGER_COMPLETE`;
12. `BLIND_CANDIDATE_OR_NO_GO_FROZEN`;
13. `CONTEXT_INDEPENDENCE_CERTIFICATE_COMPLETE`;
14. `DETERMINISTIC_CHECKER_ZERO_UNCLASSIFIED_MISMATCHES_OR_RESIDUALS_PRESERVED`;
15. `POST_FREEZE_PROJECT_COMPARISON_NOT_STARTED`.

## 13. Valid final classifications

Use one exact classification or a strictly stronger precise result:

- `UNIQUE_INTRINSIC_FINITE_RELATION_WITH_DERIVED_READOUT_RECONSTRUCTED`;
- `INTRINSIC_RELATION_CANONICAL_BUT_NUMERICAL_OR_SEMANTIC_ROLE_NONUNIQUE`;
- `MULTIPLE_INTRINSIC_FINITE_READOUTS_SURVIVE_WITH_EXACT_MISSING_DATUM`;
- `NO_CANONICAL_NONTRIVIAL_FINITE_READOUT_FORCED_BY_PRIMITIVE_PACKET`;
- `EXACT_NEGATIVE_OBSTRUCTION_FROZEN`.

## 14. Stop rule

Stop immediately after the Phase-A candidate/no-go packet, checker, ledger and context-independence certificate are frozen.

Do not perform post-freeze comparison with other Enterprise results inside this task.

Do not open a follow-on phase inside this task.

Return the frozen packet to the Driver for classification.
