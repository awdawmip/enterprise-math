# Driver Review — Prime Fusion Publication Attribution and Claim Review

Status: `SUBSTANTIVE_PASS / PUBLICATION_DISPOSITION_ACCEPTED / RUNTIME_IDENTITY_PROVENANCE_REPAIR_REQUIRED`
Date: `2026-08-25`
Driver-ID: `EM-DVR-R63A21 / CONTROL_PLANE`
Task-ID: `GS-PRIME-FUSION-PUBLICATION-ATTRIBUTION-AND-CLAIM-REVIEW`
Taskbook source: `9d1aceb5d98c4e029a68734ef89f7b80e6c1bf8c`
Owner branch: `review/prime-fusion-publication-attribution`

## 1. Driver verdict

The publication-attribution review is substantively accepted.

Accepted primary disposition:

`PRIME_FUSION_PUBLICATION_READY_AS_STRUCTURAL_OR_EXPOSITORY_NOTE`

Accepted Lean/publication synchronization:

`F1_LEAN_SCOPE_CORRECTLY_DISCLOSED`

The review does **not** support a theorem-centered paper claiming fifteen historically new results, a new general prime theory, a factoring speedup, Bateman–Horn/asymptotic consequences, or a global three-sector seam theorem.

The task hard target is mathematically/publication-semantically satisfied. However, the frozen branch artifacts contain a runtime Researcher-ID provenance defect that must be repaired before the branch is admitted to main as a final publication-review package.

## 2. Artifact completeness

The owner branch adds exactly the seven requested review artifacts and no theorem/Lean/Foundation source mutation:

1. `research/PRIME_FUSION_PUBLICATION_ATTRIBUTION_LEDGER_20260825.csv`;
2. `research/PRIME_FUSION_CLASSICAL_PRIOR_ART_REVIEW_20260825.md`;
3. `research/PRIME_FUSION_PUBLICATION_PACKAGE_20260825.md`;
4. `research/PRIME_FUSION_PUBLICATION_CLAIM_GUARDS_20260825.md`;
5. `research/PRIME_FUSION_PUBLICATION_BIBLIOGRAPHY_20260825.bib`;
6. `research_output/evidence/PRIME_FUSION_PUBLICATION_REVIEW_MANIFEST_20260825.json`;
7. `research_returns/PRIME_FUSION_PUBLICATION_ATTRIBUTION_AND_CLAIM_REVIEW_RETURN_20260825.md`.

No T16/T17 or new mathematics was added.

## 3. Theorem-by-theorem attribution audit

The final 15-row ledger is complete and internally consistent with the frozen theorem/evidence package.

Accepted attribution counts:

- `CLASSICAL_DIRECT_COROLLARY`: T1, T2, T5, T11, T12;
- `CLASSICAL_COMPOSITION`: T3, T4, T8, T10, T13;
- `PROJECT_SPECIFIC_REPACKAGING`: T6, T7, T15;
- `POSSIBLE_NEW_COMBINATION_NOT_ESTABLISHED`: T9, T14;
- `HISTORICAL_NOVELTY_ESTABLISHED`: none.

This is the correct conservative direction. In particular, failure to locate an exact antecedent for T9/T14 is not converted into priority or novelty.

## 4. Independent prior-art spot check

Driver independently spot-checked the review's principal bibliographic anchors and theorem-family search logic.

Verified bibliographic anchors include:

- David A. Cox, *Primes of the Form x^2 + ny^2*, 2nd ed., Wiley, 2013, DOI `10.1002/9781118400722`;
- Kenneth Ireland and Michael Rosen, *A Classical Introduction to Modern Number Theory*, 2nd ed., GTM 84, Springer, 1990, DOI `10.1007/978-1-4757-2103-4`;
- Lawrence C. Washington, *Introduction to Cyclotomic Fields*, 2nd ed., GTM 83, Springer, 1997, DOI `10.1007/978-1-4612-1934-7`;
- Tom M. Apostol, “Resultants of Cyclotomic Polynomials”, *Proc. AMS* 24 (1970), 457–462, DOI `10.1090/S0002-9939-1970-0251010-X`;
- Stacks Project, Lemma 10.15.4, Tag `00DT`, Chinese remainder theorem.

A second exact-formula search around the T9 mod-8/mod-12 lock and the T14 Gaussian/Eisenstein prime-cell matching formulation did not expose an obvious exact antecedent. This is sufficient only for the retained class `POSSIBLE_NEW_COMBINATION_NOT_ESTABLISHED`; it is not novelty evidence.

The stated limitation — no subscription MathSciNet/zbMATH citation-tree review by a specialist — is appropriate and must remain visible if T9/T14 are ever used in a stronger research-paper positioning.

## 5. Claim-strength audit

PASS.

The review correctly freezes:

- publication-safe evidence phrase: `15/15 retained theorem rows independently audited`;
- forbidden homogenization: `15/15 blindly replicated`;
- publication-safe Lean phrase: `the F1 finite-algebra kernel is Lean-checked on main`;
- forbidden Lean overstatement: `all fifteen theorems are Lean-verified`.

T10 remains scoped to

`M_{p,q}={x mod pq : x^2+1=0 mod p and x^2+x+1=0 mod q}`

with the `H=91` four-oriented-versus-eight-full-root pressure witness retained.

No factoring-speedup, prime-infinitude, Bateman–Horn, historical novelty, L3/L4, or global seam claim is introduced.

## 6. Publication architecture

Accepted architecture hierarchy:

1. primary: `STRUCTURAL_OR_EXPOSITORY_RESEARCH_NOTE`;
2. optional secondary emphasis: `FORMALIZATION_BACKED_NOTE_WITH_EXPLICIT_SCOPE_BOUNDARY`;
3. rejected at current evidence strength: theorem-centered new-number-theory paper claiming broad novelty.

This disposition does not select a venue and does not imply journal acceptance.

## 7. Runtime identity provenance defect

The authoritative manual dispatch envelope is:

`driver_handoffs/PRIME_FUSION_PUBLICATION_ATTRIBUTION_AND_CLAIM_REVIEW_DISPATCH_20260825.md@83a36a7eee31552206c92255b6b895c754c3304f`

and binds:

`Researcher-ID: EM-PFPUB-9D1ACE`.

The frozen return, prior-art review, publication package, claim guards and manifest instead record:

`Researcher-ID: EM-PFPUB-7C3E91`.

No repository dispatch/rebinding record or conversation-level allocation for `EM-PFPUB-7C3E91` was located. Therefore `EM-PFPUB-7C3E91` is not accepted as a valid runtime binding for this execution.

This is a governance/provenance defect only. It does not invalidate the literature review, theorem attribution, claim guards, or selected publication disposition.

Required same-task repair:

- do **not** rerun literature search or mathematics;
- restore the dispatch-bound runtime identity `EM-PFPUB-9D1ACE` in all affected publication-review artifacts;
- record that the prior `EM-PFPUB-7C3E91` literal was an unbound metadata error;
- refresh manifest artifact digests affected by the metadata correction;
- freeze the corrected return and stop.

No new taskbook or Prime Fusion research successor is authorized for this repair.

## 8. Formal Driver status

`PRIME_FUSION_PUBLICATION_REVIEW_SUBSTANTIVE_GATE = PASS`

`PRIME_FUSION_PUBLICATION_DISPOSITION = PRIME_FUSION_PUBLICATION_READY_AS_STRUCTURAL_OR_EXPOSITORY_NOTE`

`PRIME_FUSION_PUBLICATION_LEAN_DISCLOSURE = F1_LEAN_SCOPE_CORRECTLY_DISCLOSED`

`PRIME_FUSION_PUBLICATION_HISTORICAL_NOVELTY_ESTABLISHED = false`

`PRIME_FUSION_PUBLICATION_PROVENANCE_GATE = REPAIR_REQUIRED`

`PRIME_FUSION_PUBLICATION_REVIEW_MAIN_ADMISSION = BLOCKED_ONLY_ON_RUNTIME_IDENTITY_METADATA`

After the metadata-only repair, ordinary Driver reference/digest verification is sufficient; no additional theorem, Lean, replication, or prior-art research pass is required.
