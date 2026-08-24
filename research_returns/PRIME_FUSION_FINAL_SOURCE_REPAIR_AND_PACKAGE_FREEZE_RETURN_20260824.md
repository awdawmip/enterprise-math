# Research Return — Prime Fusion Final Source Repair and Package Freeze

Status: `FROZEN / TASK_COMPLETE / REVIEW_READY`  
Date: `2026-08-24`  
Researcher-ID: `EM-PFFINAL-0AA882`  
Task-ID: `GS-PRIME-FUSION-FINAL-SOURCE-REPAIR-AND-PACKAGE-FREEZE`  
Owner branch: `integration/prime-fusion-evidence-typed-package`  
Taskbook source: `0aa8824250c609283363c662ed875d661972dd43`

Final classification:

`PRIME_FUSION_FINAL_PACKAGE_FROZEN`

Hard target:

`PRIME_FUSION_15_THEOREM_CORRECTED_SOURCE_PACKAGE_FROZEN_AND_REVIEW_READY = SATISFIED`

## 1. Scope discipline

This execution was a source/integration freeze only.

- `NEW_MATHEMATICS_ADDED = false`
- `T16_T17_ADDED = false`
- `REPLICATION_RERUN = false`
- `FOUNDATION_DEFINITIONS_CHANGED = false`
- `NEGATIVE_CONTROLS_ERASED = false`

The controlling evidence state remains:

`15/15 retained theorem rows have independent audit coverage`.

This is **not** relabeled as `15/15 blind replication`.

## 2. T10 mandatory repair completed

The final package now defines the channel-oriented mixed locus explicitly:

`M_{p,q}={x mod pq : x^2+1=0 mod p and x^2+x+1=0 mod q}`.

Under the retained dual-prime hypotheses, the corrected theorem states:

`M_{p,q}={r,r^5,r^7,r^11}`.

The shared-coefficient pair remains exactly:

`{r,r^11}={r,r^(-1)}`.

The package explicitly rejects the overbroad reading that these four elements are always the complete root set of

`F(X)=(X^2+1)(X^2+X+1)`

modulo `pq`.

The exact pressure witness is preserved as a regression guard:

- `(a,b)=(2,3)`;
- `(p,q,H,r)=(13,7,91,60)`;
- oriented mixed roots: `{18,44,60,86}`;
- full fused roots: `{9,16,18,44,60,74,81,86}`.

Thus `T10_PRESSURE_WITNESS_H = 91` remains frozen.

## 3. Final T1–T15 evidence ledger

The final evidence matrix contains exactly fifteen rows with these statuses:

| Row | Final independent evidence status |
|---|---|
| T1 | `INDEPENDENT_EXACT` |
| T2 | `INDEPENDENT_EXACT` |
| T3 | `INDEPENDENT_EXACT_STATEMENT_EXPOSED` |
| T4 | `INDEPENDENT_EXACT_STATEMENT_EXPOSED` |
| T5 | `INDEPENDENT_EQUIVALENT_EXACT` |
| T6 | `INDEPENDENT_EXACT_STATEMENT_EXPOSED` |
| T7 | `INDEPENDENT_EXACT_STATEMENT_EXPOSED` |
| T8 | `INDEPENDENT_EXACT_STATEMENT_EXPOSED` |
| T9 | `INDEPENDENT_EXACT` |
| T10 | `INDEPENDENT_EXACT_AFTER_SCOPE_REPAIR` |
| T11 | `INDEPENDENT_EXACT_STATEMENT_EXPOSED` |
| T12 | `INDEPENDENT_EXACT` |
| T13 | `INDEPENDENT_EXACT` |
| T14 | `INDEPENDENT_EXACT` |
| T15 | `INDEPENDENT_EXACT_STRONGER_FORM` |

There are no final `PARTIAL` or `MISSED` theorem rows.

## 4. Source-strength notes preserved without adding theorem rows

The final package preserves already-audited explanatory strengthenings as notes only:

- T4: component quotient Smith normal form gives cyclicity iff `gcd(a,b)=1`;
- T6: `F(r)=0` already forces `r` to be a unit; reciprocal trace gives the universal idempotent factor split;
- T7: for idempotent `e`, `NC=H` and `gcd(N,C)=1` are automatic, and positive-cell versus strict-interior conditions are distinguished;
- T8: abstract `F_p x F_q` ring shape is distinguished from canonical Gaussian/Eisenstein channel labels;
- T11: the exact composite parity extension is retained as a note, not substituted for the source dual-prime theorem;
- T15: the source finite-sieve mean law is identified as a special case of the independently proved all-function unimodular slice identity.

No additional theorem row is created.

## 5. Dependency graph frozen as non-linear

The final graph rejects the false chain

`T3 -> T6 -> T10 -> T11`.

It freezes the accepted structure:

- T6 uses the reciprocal identity and modular root/local equations and does not logically require T3;
- T10 uses local orders plus CRT and does not logically require T3;
- T11 follows from the two oriented local equations and does not require T10 orbit completeness;
- on the oriented locus `x^6=2e-1 mod H` connects the T6 and T11 readouts;
- T4 uses the T3 product decomposition for the product-quotient presentation;
- T7 uses the channel split and square reconstruction;
- T8 uses quotient/channel structure plus the primality/semiprime equivalence.

## 6. Combined checker composition

`experiments/prime_fusion_final_package_checker.py` is a thin composition layer.

It does **not** copy theorem-checking logic. It addresses the exact frozen Git blob identities of the four existing checker families:

| Family | Frozen Git blob |
|---|---|
| source package | `07db705c1227d86df0fa021e56eb07eaddeee3c5` |
| blind core | `fc67f08f146782728b00472ee0156c64bdf7747e` |
| phase extension | `f2570534c99a92e75ca55b9ba24286854bc48fff` |
| T4/T7/T8 final exact closure | `c2319bf4092e41cc21d70ee6eb407480de0450ed` |

It also checks the final evidence labels, T10 scope guards, pressure witness, dependency-graph guard and manifest artifact digests.

Per the controlling task boundary, the component checker families were **not re-executed in this freeze task**. Their previously frozen executions/reviews remain the evidence authority. The combined checker is frozen for reviewer reproducibility.

Tool reuse classification:

`COMPOSE_EXISTING_TOOLS`.

## 7. Frozen artifact ledger

| Artifact | Git blob SHA-1 |
|---|---|
| `research/PRIME_FUSION_THEOREM_PACKAGE_EVIDENCE_TYPED_FINAL_20260824.md` | `055bdaaca81c5ac7ab350a71acf3b69fe5e564a9` |
| `research/PRIME_FUSION_T1_T15_FINAL_EVIDENCE_MATRIX_20260824.csv` | `3c9f6fa670f9405eebbab6eae5d5374c2de4a037` |
| `research/PRIME_FUSION_FINAL_DEPENDENCY_GRAPH_20260824.md` | `54d1fbb8c3fb657ac55f556c982501386a8eaf25` |
| `experiments/prime_fusion_final_package_checker.py` | `b529d1f2e56d6125b35f09494f417feb38468611` |
| `research_output/evidence/PRIME_FUSION_FINAL_PACKAGE_MANIFEST_20260824.json` | `6b388f3b17eddf1443de12ec6cf9f6db3e6999c2` |

The manifest intentionally omits a self-digest and the return's own digest to avoid self-reference. The return is the final freeze commit and its Git blob identity is obtained from that commit.

## 8. Source authorities consumed

- final 15-theorem evidence reconciliation:
  `driver_reviews/PRIME_FUSION_15_THEOREM_FINAL_EVIDENCE_RECONCILIATION_20260824.md@e19ee6713be002dd9c346261173d39fd8d54f9dc`;
- T4/T7/T8 exact closure review:
  `driver_reviews/PRIME_FUSION_T4_T7_T8_FINAL_EXACT_CLOSURE_DRIVER_REVIEW_20260824.md@ed016687bcd2d75957041ce820e335678aeb1f53`;
- phase-extension targeted verification review:
  `driver_reviews/PRIME_FUSION_PHASE_EXTENSION_TARGETED_VERIFICATION_DRIVER_REVIEW_20260823.md@ffaf098cb612f8a54f1d49df33484d3d36019a92`;
- blind-core independent replication review:
  `driver_reviews/PRIME_FUSION_INDEPENDENT_REPLICATION_DRIVER_REVIEW_20260823.md@be07e5d9af0ca428ae74c2807fdde586d0d665a3`;
- historical theorem package:
  `research/PRIME_FUSION_THEOREM_PACKAGE_20260823.md@e5138e17f8c4009f5e357f43326f2812c9df1359`.

## 9. Freeze verdict and stop condition

The corrected theorem package, final evidence ledger, non-linear dependency graph, thin composed checker and manifest now agree on the same fifteen retained theorem rows. The T10 source-universe ambiguity is eliminated while the `H=91` pressure witness is preserved.

`PRIME_FUSION_FINAL_PACKAGE_FROZEN = true`

`PACKAGE_REVIEW_READY = true`

`SUCCESSOR_RESEARCH_OPENED = false`

Per task instruction, execution stops at this frozen return. No new replication or successor research task is opened.
