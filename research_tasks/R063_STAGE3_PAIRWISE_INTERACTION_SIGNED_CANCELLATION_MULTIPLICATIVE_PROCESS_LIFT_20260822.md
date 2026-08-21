<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R063-STAGE3-PAIRWISE-INTERACTION-SIGNED-CANCELLATION-MULTIPLICATIVE-PROCESS-LIFT",
  "title": "R063 Stage 3 — Pairwise Interaction, Signed Cancellation, and Multiplicative Process Lift",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "PAIRWISE_INTERACTION_SIGNED_CANCELLATION_MULTIPLICATIVE_PROCESS_CLASSIFICATION",
  "next_action": "Derive the local pair-interaction table from the frozen Stage 2 bilinear root law, build the finite interaction process, classify cancellation confluence and information retention, and prove or falsify a canonical multiplicative process lift without a target-path selector.",
  "dependencies": [
    "RS-R063-STAGE2-MULTIPLICATIVE-PATH-NORM-ROOT-PROVENANCE-ALGEBRA"
  ],
  "source_refs": [
    "research/r063-stage2-multiplicative-provenance-algebra@96fbcd431f4cbb8263347bffb5c8bf33b7639e98",
    "driver_reviews/R063_STAGE2_MULTIPLICATIVE_PATH_NORM_ROOT_PROVENANCE_DRIVER_REVIEW_20260822.md@b31419774f6d7190a4ed51332a9f69f4c7359b31"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "R063",
    "path-norm-root",
    "pairwise-interaction",
    "signed-cancellation",
    "process-lift",
    "multiplicative-path",
    "axiom-extraction"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R063S3",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:5683a6782b9af905fb74e78425be8b1b6373977856368b52c46710b439fb4467",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R063 Stage 3 — Pairwise Interaction, Signed Cancellation, and Multiplicative Process Lift

Task-ID: `RS-R063-STAGE3-PAIRWISE-INTERACTION-SIGNED-CANCELLATION-MULTIPLICATIVE-PROCESS-LIFT`

Driver: `EM-DVR-R63A21 / CONTROL_PLANE`
Identity policy: `AUTO_RESOLVE_OR_ALLOCATE`
Identity lane: `R063S3`

Intended owner branch:

`research/r063-stage3-interaction-cancellation-path-lift`

## 0. Read first / frozen inputs

Treat the following as frozen inputs:

1. `driver_reviews/R063_STAGE2_MULTIPLICATIVE_PATH_NORM_ROOT_PROVENANCE_DRIVER_REVIEW_20260822.md` at `b31419774f6d7190a4ed51332a9f69f4c7359b31`;
2. R063 Stage 2 frozen owner payload `research/r063-stage2-multiplicative-provenance-algebra@96fbcd431f4cbb8263347bffb5c8bf33b7639e98`;
3. R063 Stage 2 taskbook source `74cacc89ec09a8af7dd7ff01c10f2baf082daf81`;
4. frozen R061 component-trace/path semantics used by Stage 2;
5. current `native_semantics_admissibility.json` before any native/intrinsic/process-primitive promotion claim.

Freeze from Stage 2:

- supported-domain provenance multiplication is exact;
- `URoot=SRoot/U` is an exact graded commutative monoid;
- full ordered nonnegative component roots have a square-axis orientation obstruction;
- oriented component/trace multiplication is exact only after retaining an ordered orientation;
- native path multiplicity is not multiplicative under root product;
- concatenation/interleaving/commutation preserve additive component counts and therefore cannot generate the multiplicative trace in general;
- no single-valued multiplicative path operation is already present in the frozen R061 operation closure;
- the whole-target-fiber relation is exact but may erase all source path-order information.

Do not reopen Stage 2 algebra unless an exact contradiction is found under the same premises.

## 1. Hard objective

Determine whether the Stage 2 bilinear root product is the collapse of a **minimal finite pairwise interaction process on path letters**.

Hard target:

`PAIRWISE_INTERACTION_SIGNED_CANCELLATION_MULTIPLICATIVE_PROCESS_LIFT_CLASSIFIED`.

The stage must classify all of the following separately:

1. exact trace-level pair-interaction realization;
2. signed-cancellation normal form;
3. orientation/unit-state dependence;
4. representative-level source-order retention or loss;
5. relation-valued versus single-valued path readout;
6. associativity/coherence of the process under repeated multiplication;
7. whether the required new process law is derivable/conditional/minimal or merely an arbitrary selector.

## 2. Frozen working theorem candidate

The Stage 2 oriented raw component law is

`(a,b) * (c,d) -> (ac-bd, ad+bc)`

before unit normalization.

Research the following working theorem aggressively:

`MULTIPLICATIVE_ROOT_PRODUCT_IS_THE_COLLAPSE_OF_A_LOCAL_PAIRWISE_LETTER_INTERACTION_PROCESS`.

The proposed local interaction table is:

`X_i tensor X_i -> +X_i`

`X_i tensor X_j -> +X_j`

`X_j tensor X_i -> +X_j`

`X_j tensor X_j -> -X_i`.

For source traces with counts `(a,b)` and `(c,d)`, this produces raw interaction counts

`#+X_i = ac`,

`#-X_i = bd`,

`#+X_j = ad+bc`.

After the cancellation rule

`(+X_i)+(-X_i) -> 0`,

the aggregate signed trace is exactly

`(ac-bd, ad+bc)`.

This table is a theorem candidate to derive from the frozen Stage 2 algebra. It is **not** a free new native axiom at task start.

## 3. Simplicity constraint

The preferred carrier is deliberately elementary:

- finite words;
- finite rectangular arrays of pair interactions;
- integer counts;
- local labels;
- finite cancellation/rewrite rules;
- finite order/linearization data when needed.

Do not use continuum angle, analytic phase, Euclidean rotation, numerical approximation, optimization, probability, or a hidden real-valued residual variable to define the process.

An auxiliary implementation coordinate may be used only as a typed checker carrier and must not become the claimed process semantics.

## 4. Derive or falsify the interaction table

Let the two basis path letters be `X_i,X_j`.

Prove whether the four-entry table in Section 2 is uniquely forced by all of:

1. bilinearity of component counts;
2. the frozen Stage 2 raw product formula;
3. symmetry/commutativity of factor order at the trace level;
4. identity behavior of `X_i` under the chosen orientation;
5. no target-path selector.

If the table is not unique under these assumptions, classify the complete smallest family of admissible tables and identify the missing axiom/choice.

Do not simply restate Gaussian multiplication as the proof. Extract the finite basis interaction law explicitly and show exactly what data are necessary and sufficient.

Required result:

`R063_STAGE3_INTERACTION_TABLE_CLASSIFICATION.md`.

## 5. Build the interaction rectangle

For source paths

`p=w_1...w_m`,

`q=v_1...v_n`,

define the finite interaction rectangle

`I(p,q)={(r,s):1<=r<=m,1<=s<=n}`.

Each cell receives the local label determined by `(w_r,v_s)`.

At minimum retain:

- source position `(r,s)`;
- source letters;
- signed output label;
- row order inherited from `p`;
- column order inherited from `q`.

A product-order/partial-order representation is allowed if useful, but it must be presented in elementary finite terms as well.

Prove exactly that forgetting all order and retaining only signed counts gives the raw Stage 2 component product.

Required theorem:

`INTERACTION_RECTANGLE_COUNT_COLLAPSE_EQUALS_RAW_ROOT_PRODUCT`.

## 6. Cancellation confluence is the central gate

At the count level,

`+X_i` and `-X_i` annihilate uniquely by total count.

At the representative/process level, different choices of which positive and negative interaction cells cancel may retain different inherited order relations.

Classify this exactly.

Required questions:

1. Is there a cancellation rule that is local, deterministic and choice-independent without adding a global ranking?
2. If cancellation pairings differ, do all pairings yield isomorphic residual process objects?
3. If not, does taking the relation/set of all residual objects give a canonical quotient?
4. Does the set of target path linearizations depend on cancellation pairing?
5. What is the smallest exact nonconfluence witness, if any?
6. Can a confluent normal form be defined using only the finite interaction structure itself?

A lexicographic position rule, first-available match, numeric rank, external path order, or target-word choice is not accepted as canonical unless independently derived from the frozen semantics.

Required result:

`R063_STAGE3_CANCELLATION_CONFLUENCE_OR_NO_GO.md`.

## 7. Preserve unit/orientation information explicitly

The raw interaction process naturally contains a signed `X_i` channel.

When the residual signed real component is negative, Stage 2 ordered readout applies a unit normalization.

Do not hide that step.

Classify two levels separately:

### 7.1 Unit-equivariant process level

Attempt to retain the signed process plus a finite unit/orientation state so that multiplication is defined before choosing `(i)` versus `(j)` ordered readout.

Determine whether this yields an orientation-free `URoot`-compatible process object.

### 7.2 Ordered readout level

Only after choosing an ordered sector orientation may the signed process collapse to the Stage 2 ordered nonnegative target trace.

The square-axis witness

`(1,1)^2`

must continue to expose the distinction between `(0,2)` and `(2,0)`.

Required classification:

`UNIT_EQUIVARIANT_PROCESS = EXACT / PARTIAL / NO_GO`.

## 8. A path lift must retain more than the trivial whole-target-fiber relation

Stage 2 already has the trivial exact relation that maps every source path pair to the entire target native path fiber.

Stage 3 counts as a genuine path-process advance only if it determines whether the interaction process retains **source path-order information**.

For each source pair `(p,q)`, define the strongest choice-free target relation generated by the interaction/cancellation structure itself.

Then classify:

- whether two different source path pairs with the same source traces can produce different target relations;
- whether the relation is always the entire target path fiber;
- whether it can be a proper nonempty subset;
- whether it can carry multiplicity/weight information even when its support is the full target fiber;
- whether any single-valued target path is forced for nontrivial fibers.

If every choice-free construction collapses to the entire target fiber, preserve that as a strong negative theorem:

`PAIRWISE_INTERACTION_PROCESS_RETains_NO_NATIVE_PATH_ORDER_AFTER_COLLAPSE`.

If source-sensitive structure survives, isolate the exact invariant.

## 9. Mandatory witnesses

### W1 — minimal multiplicity collapse

`r=s=(1,1)`.

Every source pair has four interaction cells:

one `+X_i`, two `+X_j`, one `-X_i`.

After count cancellation the target is `(0,2)`.

Use this to verify the local table and basic cancellation.

### W2 — source-order discrimination

`r=s=(2,1)` corresponding to norm `5`.

There are `3 x 3 = 9` source native path pairs and target root `(3,4)` has `35` native paths.

Compute the Stage 3 interaction relation for all nine source path pairs.

This witness must decide whether source path order survives the multiplicative process in any nontrivial way.

### W3 — negative raw component / unit normalization

Use

`r=s=(1,2)`.

Raw product:

`(-3,4)`.

Ordered Stage 2 readout under the `i` convention is `(4,3)`.

The process must expose the negative channel and the subsequent unit normalization explicitly.

### W4 — orientation obstruction

Use `(1,1)^2` to compare the two ordered readouts `(0,2)` and `(2,0)` from one unit-orbit target.

### W5 — repeated multiplication

Use at least one triple drawn from

`(1,1)`, `(2,1)`, `(1,2)`

to test process associativity/coherence rather than trace associativity alone.

## 10. Associativity and coherence

A trace-level multiplication can be associative while a chosen process lift is not.

Classify binary process multiplication under triple products.

At minimum compare

`I(I(p,q),r)`

against

`I(p,I(q,r))`

under whatever precise enriched carrier is proposed.

Because the intermediate object may not itself be an ordinary positive-letter path, define the typed domains carefully.

Acceptable outcomes include:

- strict associativity;
- canonical isomorphism/associator;
- relation-level associativity;
- associativity only after trace projection;
- exact no-go with smallest counterexample.

Do not infer process associativity merely from Gaussian/root associativity.

Required result:

`R063_STAGE3_PROCESS_ASSOCIATIVITY_COHERENCE.md`.

## 11. Minimality / axiom extraction

If a successful nontrivial process carrier is found, identify the **smallest additional structure** beyond frozen R061 paths that is sufficient.

Test at least these ingredients separately:

- pairwise interaction rectangle;
- signed output channel;
- cancellation rule;
- unit/orientation state;
- source-position/order inheritance;
- provenance labels.

For each ingredient classify:

`NECESSARY`, `DERIVABLE`, `SUFFICIENT_WITH_OTHERS`, `REDUNDANT`, or `UNRESOLVED`.

The goal is not to accumulate machinery. The goal is to discover the minimum law that changes additive positive-letter path semantics into a multiplicative process.

If a minimal law is isolated, write it as a candidate axiom/derived law in

`R063_STAGE3_MINIMAL_PROCESS_AXIOM_CANDIDATE.md`.

Its semantic status must remain exact:

`N0_NATIVE`, `N1_DERIVED_OPERATIONAL`, or `UNRESOLVED`.

No promotion to native is authorized merely because the law reproduces the Stage 2 formula.

## 12. Multiplicity spectrum

Keep distinct:

1. source native path-pair count;
2. interaction-cell count;
3. number of cancellation matchings, if nontrivial;
4. number of residual process objects;
5. number of target path linearizations generated by the process;
6. full target native path multiplicity;
7. Gaussian/provenance preimage multiplicity;
8. R062 `N_BRC`;
9. Boolean support.

Search for exact formulas and smallest counterexamples to false equalities.

A new multiplicity is useful only if its carrier and projection are explicit.

Required artifact:

`R063_STAGE3_MULTIPLICITY_SPECTRUM.json`.

## 13. BRC remains downstream

Only after the interaction/process relation is fixed may it be projected to R062 enrichment.

Determine whether the new process generates a meaningful multiplicity or formal-support map before `N_BRC`, but do not use BRC to choose cancellation pairings, orientation, process representatives or target paths.

If no new compatible structure exists, state the strongest exact noncommuting diagram.

## 14. Deterministic checker

Create

`scripts/r063_stage3_validate_pairwise_interaction_process.py`.

It must use exact finite/integer combinatorics only for theorem decisions.

The checker must independently verify at least:

- frozen Stage 2 target component product on tested witnesses;
- interaction table count collapse;
- cancellation count normal form;
- all mandatory witnesses;
- source-order relation equality/difference claims;
- smallest nonconfluence counterexample, if one exists;
- process associativity/coherence claims on the declared tested domain;
- multiplicity-layer separation;
- zero unclassified mismatches.

The checker must not select a target path by an arbitrary global ordering and then report that selection as a theorem.

## 15. Regression domain

Because representative-level interaction structures can grow rapidly, prioritize proof and smallest exact counterexamples over brute scale.

Mandatory exhaustive word-level domain:

- all ordered component roots with `a+b<=6`;
- all native source path representatives for those roots;
- all ordered source-path pairs whose interaction rectangle has at most `36` cells.

Mandatory targeted larger witnesses:

- the full `5 x 5` source-path witness from Section 9;
- `(1,2)^2`;
- selected triple products for associativity/coherence.

Extend beyond this only when computation remains straightforward.

## 16. Required outputs

Produce at least:

1. `research_results/R063_STAGE3/R063_STAGE3_INTERACTION_TABLE_CLASSIFICATION.md`;
2. `research_results/R063_STAGE3/R063_STAGE3_INTERACTION_COUNT_COLLAPSE_THEOREM.md`;
3. `research_results/R063_STAGE3/R063_STAGE3_CANCELLATION_CONFLUENCE_OR_NO_GO.md`;
4. `research_results/R063_STAGE3/R063_STAGE3_UNIT_EQUIVARIANT_PROCESS_CLASSIFICATION.md`;
5. `research_results/R063_STAGE3/R063_STAGE3_SOURCE_ORDER_RETENTION_CLASSIFICATION.md`;
6. `research_results/R063_STAGE3/R063_STAGE3_PROCESS_ASSOCIATIVITY_COHERENCE.md`;
7. `research_results/R063_STAGE3/R063_STAGE3_MINIMAL_PROCESS_AXIOM_CANDIDATE.md` if a genuine minimal law is isolated;
8. `research_results/R063_STAGE3/R063_STAGE3_MULTIPLICITY_SPECTRUM.json`;
9. `research_results/R063_STAGE3/R063_STAGE3_SEMANTIC_SCOPE_CLAIM_LEDGER.json`;
10. `research_results/R063_STAGE3/R063_STAGE3_MISMATCHES.json`;
11. `research_results/R063_STAGE3/R063_STAGE3_REGRESSION.json`;
12. `research_results/R063_STAGE3/R063_STAGE3_FINAL_CLASSIFICATION.md`;
13. `scripts/r063_stage3_validate_pairwise_interaction_process.py`.

## 17. Acceptance gates

Stage 3 may return complete only when all are classified:

1. `STAGE2_FROZEN_DEPENDENCY_REPLAY_INTACT`;
2. `PAIRWISE_INTERACTION_TABLE_DERIVED_OR_NONUNIQUENESS_CLASSIFIED`;
3. `INTERACTION_COUNT_COLLAPSE_EQUALS_RAW_ROOT_PRODUCT`;
4. `SIGNED_CANCELLATION_TRACE_NORMAL_FORM_EXACT`;
5. `REPRESENTATIVE_LEVEL_CANCELLATION_CONFLUENCE_OR_MINIMAL_COUNTEREXAMPLE`;
6. `UNIT_EQUIVARIANT_PROCESS_LEVEL_CLASSIFIED`;
7. `SOURCE_PATH_ORDER_RETENTION_OR_TOTAL_ERASURE_CLASSIFIED`;
8. `TRIVIAL_WHOLE_TARGET_FIBRE_RELATION_STRICTLY_IMPROVED_OR_PROVED_UNIMPROVABLE`;
9. `PROCESS_ASSOCIATIVITY_COHERENCE_OR_NO_GO_CLASSIFIED`;
10. `MINIMAL_ADDITIONAL_PROCESS_STRUCTURE_CLASSIFIED`;
11. `ALL_MULTIPLICITY_LAYERS_SEPARATED`;
12. `SEMANTIC_SCOPE_CLAIM_LEDGER_COMPLETE`;
13. `DETERMINISTIC_CHECKER_ZERO_UNCLASSIFIED_MISMATCHES`.

## 18. Allowed final classifications

Examples include:

`PAIRWISE_INTERACTION_SIGNED_CANCELLATION_MULTIPLICATIVE_PROCESS_LIFT_CLASSIFIED_WITH_CANONICAL_SOURCE_SENSITIVE_RELATION`

`PAIRWISE_INTERACTION_TRACE_COLLAPSE_EXACT_BUT_CANCELLATION_PROCESS_NONCONFLUENT`

`PAIRWISE_INTERACTION_PROCESS_CANONICAL_BUT_ASSOCIATIVITY_ONLY_AFTER_TRACE_PROJECTION`

`PAIRWISE_INTERACTION_ADDS_NO_PATH_INFORMATION_BEYOND_WHOLE_TARGET_FIBRE`

`MINIMAL_SIGNED_INTERACTION_AXIOM_IS_N1_DERIVED_OPERATIONAL_AND_SUFFICIENT_FOR_MULTIPLICATIVE_PROCESS`

or a stronger exact classification supported by the evidence.

## 19. Stop rule

Stop after Stage 3 classification and evidence return.

Do not open R063 Stage 4 inside this task.
