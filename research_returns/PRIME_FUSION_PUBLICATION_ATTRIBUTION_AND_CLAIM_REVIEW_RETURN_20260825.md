# Prime Fusion — Publication Attribution and Claim Review Return

Status: `FROZEN / HARD_TARGET_REACHED / STOP`  
Date: `2026-08-25`  
Researcher-ID: `EM-PFPUB-9D1ACE`  
Task-ID: `GS-PRIME-FUSION-PUBLICATION-ATTRIBUTION-AND-CLAIM-REVIEW`  
Taskbook source: `9d1aceb5d98c4e029a68734ef89f7b80e6c1bf8c`  
Owner branch: `review/prime-fusion-publication-attribution`

Hard target:

`PRIME_FUSION_PUBLICATION_PACKAGE_ATTRIBUTION_CLAIM_STRENGTH_AND_RELEASE_FORM_INDEPENDENTLY_CLASSIFIED`

## 0. Final verdict

Hard target reached.

Primary publication disposition:

`PRIME_FUSION_PUBLICATION_READY_AS_STRUCTURAL_OR_EXPOSITORY_NOTE`

Lean/publication synchronization:

`F1_LEAN_SCOPE_CORRECTLY_DISCLOSED`

The accepted T1–T15 mathematics is not reopened or enlarged. The strongest honest publication positioning is a structural/expository research note, optionally with a formalization-backed secondary emphasis. The current evidence does not support presenting Prime Fusion as fifteen historically new theorems or as a new general prime/factoring theory.

## 0A. Runtime identity metadata correction

This return is frozen again only to repair runtime identity provenance under the controlling Driver review

`driver_reviews/PRIME_FUSION_PUBLICATION_ATTRIBUTION_AND_CLAIM_REVIEW_DRIVER_REVIEW_20260825.md@2f9a46f0aedc72c79155ada053486dd0d02f7e23`.

The unbound metadata literal `EM-PFPUB-7C3E91` in the affected publication-review artifacts was corrected to the dispatch-bound `EM-PFPUB-9D1ACE`.

No prior-art search, mathematics, Lean work, replication, attribution class, T10 guard, Lean label, or publication disposition was changed.

`METADATA_CORRECTION_ONLY = true`

`RUNTIME_IDENTITY_METADATA_CORRECTED = true`

`PRIME_FUSION_PUBLICATION_PROVENANCE_GATE = PASS`

## 1. Recovery and execution note

This execution resumed from the highest durable frontier on the owner branch rather than restarting completed review work.

Recovered as `VERIFIED_COMPLETE`:

- `research/PRIME_FUSION_PUBLICATION_ATTRIBUTION_LEDGER_20260825.csv`;
- `research/PRIME_FUSION_CLASSICAL_PRIOR_ART_REVIEW_20260825.md`.

Recovered as missing / `UNFINISHED` and completed in this continuation:

- `research/PRIME_FUSION_PUBLICATION_PACKAGE_20260825.md`;
- `research/PRIME_FUSION_PUBLICATION_CLAIM_GUARDS_20260825.md`;
- `research/PRIME_FUSION_PUBLICATION_BIBLIOGRAPHY_20260825.bib`;
- `research_output/evidence/PRIME_FUSION_PUBLICATION_REVIEW_MANIFEST_20260825.json`;
- this frozen return.

No verified-complete artifact was replayed merely because the prior conversation ended before the task-level return was visible.

## 2. Frozen mathematical/evidence authority used

The review preserved the exact source boundaries required by the taskbook:

- final corrected theorem package: `research/PRIME_FUSION_THEOREM_PACKAGE_EVIDENCE_TYPED_FINAL_20260824.md@blob:055bdaaca81c5ac7ab350a71acf3b69fe5e564a9`;
- final T1–T15 evidence matrix: `research/PRIME_FUSION_T1_T15_FINAL_EVIDENCE_MATRIX_20260824.csv@blob:3c9f6fa670f9405eebbab6eae5d5374c2de4a037`;
- final dependency graph: `research/PRIME_FUSION_FINAL_DEPENDENCY_GRAPH_20260824.md@blob:54d1fbb8c3fb657ac55f556c982501386a8eaf25`;
- final package manifest: `research_output/evidence/PRIME_FUSION_FINAL_PACKAGE_MANIFEST_20260824.json@blob:6b388f3b17eddf1443de12ec6cf9f6db3e6999c2`;
- F1 Driver review: `driver_reviews/PRIME_FUSION_F1_LEAN_FINITE_ALGEBRA_FORMALIZATION_DRIVER_REVIEW_20260825.md@d94be81c99bb9b300969a7a8cabb26299e248941`;
- F1 integration: `main@9825c13ff368a1feda37f2baacc7a777d967b8db`.

The final evidence matrix confirms mixed evidence modes across T1–T15. The F1 review confirms warning-fatal Lean build success, no `sorry`, no `admit`, no custom axioms, and preservation of the corrected T10 oriented-locus regression guard.

## 3. Prior-art search result

The literature search was organized by theorem family rather than Enterprise vocabulary alone. It covered:

- Gaussian/Eisenstein norm forms and binary quadratic forms;
- quadratic reciprocity and supplementary laws;
- `Phi_4`, `Phi_3`, cyclotomic resultants/discriminants;
- polynomial/ring CRT and product quotient structure;
- Gaussian/Eisenstein principal quotients and Smith-normal-form mechanisms;
- finite-field roots and local orders 3, 4, and 12;
- square-free product-of-fields characterizations;
- one-parameter quadratic root counts;
- graph matching terminology;
- finite unimodular changes of variables and double counting;
- exact-formula/exact-combination searches for the project-specific T2, T9, T10, T11, T13, T14, and T15 formulations.

Authoritative anchors located and recorded in the bibliography include Cox, Ireland–Rosen, Serre, Lemmermeyer, Washington, Apostol, Lidl–Niederreiter, the Stacks Project CRT lemma, and Diestel.

The search found substantial classical overlap for the mathematical mechanisms underlying almost every row. It did not locate a reliable exact published antecedent for the full T9 reciprocity lock or the exact T14 sector-local matching statement. Those two rows remain:

`POSSIBLE_NEW_COMBINATION_NOT_ESTABLISHED`.

This is deliberately weaker than a novelty claim. Absence of an exact hit is not evidence of historical priority.

## 4. Theorem-by-theorem publication classification

| Row | Primary attribution class | Confidence | Lean publication label |
|---|---|---:|---|
| T1 | `CLASSICAL_DIRECT_COROLLARY` | HIGH | `LEAN_F1_MAIN` |
| T2 | `CLASSICAL_DIRECT_COROLLARY` | HIGH | `LEAN_F1_MAIN` |
| T3 | `CLASSICAL_COMPOSITION` | HIGH | `LEAN_F1_MAIN_PARTIAL` |
| T4 | `CLASSICAL_COMPOSITION` | HIGH | `LEAN_F1_MAIN_CORE` |
| T5 | `CLASSICAL_DIRECT_COROLLARY` | HIGH | `LEAN_F1_MAIN` |
| T6 | `PROJECT_SPECIFIC_REPACKAGING` | HIGH | `LEAN_F1_MAIN` |
| T7 | `PROJECT_SPECIFIC_REPACKAGING` | HIGH | `NOT_YET_LEAN_FORMALIZED` |
| T8 | `CLASSICAL_COMPOSITION` | HIGH | `NOT_YET_LEAN_FORMALIZED` |
| T9 | `POSSIBLE_NEW_COMBINATION_NOT_ESTABLISHED` | MEDIUM | `NOT_YET_LEAN_FORMALIZED` |
| T10 | `CLASSICAL_COMPOSITION` | HIGH | `LEAN_F1_MAIN` |
| T11 | `CLASSICAL_DIRECT_COROLLARY` | HIGH | `LEAN_F1_MAIN` |
| T12 | `CLASSICAL_DIRECT_COROLLARY` | HIGH | `NOT_YET_LEAN_FORMALIZED` |
| T13 | `CLASSICAL_COMPOSITION` | HIGH | `NOT_YET_LEAN_FORMALIZED` |
| T14 | `POSSIBLE_NEW_COMBINATION_NOT_ESTABLISHED` | MEDIUM | `NOT_YET_LEAN_FORMALIZED` |
| T15 | `PROJECT_SPECIFIC_REPACKAGING` | HIGH | `NOT_YET_LEAN_FORMALIZED` |

Counts:

- `CLASSICAL_DIRECT_COROLLARY = 5`;
- `CLASSICAL_COMPOSITION = 5`;
- `PROJECT_SPECIFIC_REPACKAGING = 3`;
- `POSSIBLE_NEW_COMBINATION_NOT_ESTABLISHED = 2`;
- `HISTORICAL_NOVELTY_ESTABLISHED = 0`.

Every retained row has a primary attribution class, confidence level, evidence/Lean label, strongest citation family, publication-safe wording, and forbidden/unsupported wording in the frozen attribution ledger.

## 5. Mandatory claim guards — PASS

### T10 scope

PASS.

The publication package defines explicitly

`M_{p,q}={x mod pq : x^2+1=0 mod p and x^2+x+1=0 mod q}`

and states the four-phase orbit only on this oriented locus.

The `H=91` pressure witness is preserved:

- oriented locus: `{18,44,60,86}`;
- full fused-root set: `{9,16,18,44,60,74,81,86}`.

Therefore:

`T10_FULL_FUSED_ROOT_SET_CLAIM = false`.

### Evidence wording

PASS.

Allowed:

`15/15 retained theorem rows independently audited`.

Forbidden:

`15/15 blindly replicated`.

### Lean wording

PASS.

Allowed:

`the F1 finite-algebra kernel is Lean-checked on main`.

Forbidden:

`all fifteen theorems are Lean-verified`.

### Result-level boundaries

PASS.

No publication claim is made for:

- infinitely many dual-prime cells;
- Bateman–Horn asymptotics as a theorem;
- factoring speedup or an efficient general factorization algorithm;
- global three-sector seam matching;
- historical novelty;
- L3/L4 promotion from package completeness or formalization.

## 6. Publication architecture decision

Architecture A — research theorem note centered on new theorem claims: **not supported by current attribution evidence**.

Architecture B — structural/expository research note: **supported and selected as primary**.

Architecture C — formalization-backed note: **supported as secondary emphasis** if the F1 boundary remains explicit.

Architecture D — no submission: **not required** provided the bounded structural/expository positioning and claim guards are followed.

No journal is selected. The disposition is venue-neutral.

## 7. Required package status

Required artifacts:

1. `research/PRIME_FUSION_PUBLICATION_ATTRIBUTION_LEDGER_20260825.csv` — complete;
2. `research/PRIME_FUSION_CLASSICAL_PRIOR_ART_REVIEW_20260825.md` — complete;
3. `research/PRIME_FUSION_PUBLICATION_PACKAGE_20260825.md` — complete;
4. `research/PRIME_FUSION_PUBLICATION_CLAIM_GUARDS_20260825.md` — complete;
5. `research/PRIME_FUSION_PUBLICATION_BIBLIOGRAPHY_20260825.bib` — complete;
6. `research_output/evidence/PRIME_FUSION_PUBLICATION_REVIEW_MANIFEST_20260825.json` — complete in this same freeze sequence;
7. `research_returns/PRIME_FUSION_PUBLICATION_ATTRIBUTION_AND_CLAIM_REVIEW_RETURN_20260825.md` — this file, frozen.

The machine-readable manifest records source refs, literature-search clusters/domains, artifact blob digests, and the final disposition.

## 8. Search limitation

The review used accessible primary/authoritative bibliographic sources and broad scholarly web search, but it is not a substitute for a subscription MathSciNet/zbMATH citation-tree review by a specialist. Therefore T9/T14 may not be upgraded from `POSSIBLE_NEW_COMBINATION_NOT_ESTABLISHED` on this record alone.

Any future attempt to reposition Prime Fusion as a theorem-centered research paper must run a dedicated historical-priority review before using `new`, `first`, `first known`, or equivalent language.

## 9. Hard-target freeze

`PRIME_FUSION_PUBLICATION_PACKAGE_ATTRIBUTION_CLAIM_STRENGTH_AND_RELEASE_FORM_INDEPENDENTLY_CLASSIFIED = true`

`PRIMARY_PUBLICATION_DISPOSITION = PRIME_FUSION_PUBLICATION_READY_AS_STRUCTURAL_OR_EXPOSITORY_NOTE`

`LEAN_PUBLICATION_SYNCHRONIZATION = F1_LEAN_SCOPE_CORRECTLY_DISCLOSED`

`THEOREM_ROWS_RETAINED = 15`

`NEW_THEOREM_ROWS_ADDED = 0`

`T16_T17_ADDED = false`

`T10_SCOPE = CHANNEL_ORIENTED_MIXED_LOCUS_M_PQ`

`T10_PRESSURE_WITNESS_H = 91`

`ALL_15_LEAN_VERIFIED = false`

`HISTORICAL_NOVELTY_ESTABLISHED = false`

`RUNTIME_IDENTITY_METADATA_CORRECTED = true`

`PRIME_FUSION_PUBLICATION_PROVENANCE_GATE = PASS`

`STOP_CONDITION_REACHED = true`

Stop. Do not open another Prime Fusion research or formalization task from this review.
