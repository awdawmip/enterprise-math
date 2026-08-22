# R064 Phase A — Final Classification

Researcher: `EM-R064A-9D3DB8`  
Freeze: `2026-08-22T15:49:42+08:00`  
Taskbook source: `9d3db83d0c276e8bb3a06eadc4b9f910c4888ba7`

## Final classification

`N0_DEFINABLE_LOCAL_PROCESS_RELATION_FAMILY_NONUNIQUE_WITH_EXACT_MISSING_AXIOM`

Precise refinement:

`COMPONENT_TAG_QUOTIENT_HAS_A_UNIQUE_NONTRIVIAL_S3_EQUIVARIANT_COMPLEMENT_LAW_AFTER_PROJECTIONS_ARE_EXCLUDED; FULL_N0_EVENT_CONTEXT_DOES_NOT_FORCE_FACTOR_THROUGH_THAT_QUOTIENT; SINGLE_EVENT_OUTPUT_REQUIRES_AN_ADDITIONAL_LIFT`.

## Frozen findings

1. The exact N0 relabeling/automorphism group used by the theorem is `S3`.
2. The smallest pair-local relational reduct has 11 automorphism classes.
3. On the primitive three-axis component carrier, there are exactly three total `S3`-equivariant binary laws: left projection, right projection, and unique-third-axis component complement. Only the last is nontrivial under the task's exclusion rule.
4. The component-complement law has an N0 definability DAG, is closed on the three primitive axes, is commutative and idempotent, and satisfies `x⊙(x⊙y)=y`; it has no identity and is not associative.
5. Full N0 local context is richer than component tags. At the minimal axis-output strength, the 11 trivial-stabilizer context orbits yield exactly `3^11 = 177147` equivariant deterministic laws.
6. A length-2 path already witnesses inequivalent N0-definable context-sensitive and component-only laws.
7. For distinct same-sector inputs, the component output axis has two compatible incident output sectors; N0 does not canonically lift the component state to one event occurrence.
8. Therefore N0 supplies a nontrivial intrinsic **component relation**, but not a unique full local interaction process without an explicit additional operational factorization/lift axiom.

## Acceptance gates

| Gate | Status |
|---|---|
| `PHASEA_FOUNDATION_ONLY_CONTEXT_BOUNDARY_RECORDED` | PASS |
| `N0_SUBSTRATE_DECLARATION_COMPLETE` | PASS |
| `NO_DOWNSTREAM_RESULT_USED_AS_PHASEA_PREMISE` | PASS |
| `LOCAL_CONTEXT_EQUIVALENCE_CLASSES_CLASSIFIED` | PASS |
| `N0_AUTOMORPHISM_OR_RELABELING_GROUP_CLASSIFIED` | PASS — `S3` |
| `LOCAL_INTERACTION_LAW_UNIQUE_FAMILY_OR_NO_GO_CLASSIFIED` | PASS — exact nonunique family + component quotient subfamily |
| `EVERY_INTERNAL_STATE_HAS_N0_DEFINABILITY_DAG_OR_IS_REJECTED` | PASS |
| `CLOSURE_AND_REPEATED_COMPOSITION_CLASSIFIED` | PASS |
| `ALGEBRAIC_LAWS_DERIVED_OR_FALSIFIED_NOT_ASSUMED` | PASS |
| `MINIMALITY_OR_EXACT_MISSING_AXIOM_CLASSIFIED` | PASS |
| `SEMANTIC_SCOPE_CLAIM_LEDGER_COMPLETE` | PASS |
| `TARGET_LEAKAGE_AUDIT_PASS` | PASS |
| `DETERMINISTIC_CHECKER_PASS_OR_MINIMAL_UNCLASSIFIED_COUNTEREXAMPLE_PRESERVED` | PASS — mismatch count `0` |
| `RAW_CANDIDATE_OR_EXACT_NO_GO_FROZEN` | PASS |
| `PHASEB_DOWNSTREAM_COMPARISON_NOT_STARTED` | PASS |

## Stop rule

Candidate/family freeze is complete at Phase-A scope. No prior downstream process/algebra route was compared, no Working Truth was activated, no missing N1 axiom was added, and no Phase B work was started.
