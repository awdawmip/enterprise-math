<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "GS-PRIME-FUSION-PUBLICATION-ATTRIBUTION-AND-CLAIM-REVIEW",
  "title": "Prime Fusion — Publication Attribution, Claim-Strength, and Release-Form Review",
  "kind": "GOVERNANCE",
  "owner": "review/prime-fusion-publication-attribution",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "PRIME_FUSION_PUBLICATION_PACKAGE_ATTRIBUTION_CLAIM_STRENGTH_AND_RELEASE_FORM_INDEPENDENTLY_CLASSIFIED",
  "next_action": "Independently review the accepted Prime Fusion T1–T15 package for publication: map each retained theorem to classical antecedents and adjacent literature, separate theorem truth from novelty and presentation value, audit all publishable claims against the frozen evidence and Lean status, preserve the corrected T10 universe, and freeze a venue-neutral publication package or an explicit expositional/rewrite/block disposition without adding mathematics.",
  "dependencies": [
    "driver_reviews/PRIME_FUSION_FINAL_SOURCE_REPAIR_AND_PACKAGE_FREEZE_DRIVER_REVIEW_20260824.md@86df3a53417ddc810b3c51ac906288b54bef5e63",
    "driver_reviews/PRIME_FUSION_F1_LEAN_FINITE_ALGEBRA_FORMALIZATION_DRIVER_REVIEW_20260825.md@d94be81c99bb9b300969a7a8cabb26299e248941",
    "main@9825c13ff368a1feda37f2baacc7a777d967b8db",
    "research/PRIME_FUSION_THEOREM_PACKAGE_EVIDENCE_TYPED_FINAL_20260824.md@blob:055bdaaca81c5ac7ab350a71acf3b69fe5e564a9",
    "research/PRIME_FUSION_T1_T15_FINAL_EVIDENCE_MATRIX_20260824.csv@blob:3c9f6fa670f9405eebbab6eae5d5374c2de4a037",
    "research/PRIME_FUSION_FINAL_DEPENDENCY_GRAPH_20260824.md@blob:54d1fbb8c3fb657ac55f556c982501386a8eaf25",
    "research_output/evidence/PRIME_FUSION_FINAL_PACKAGE_MANIFEST_20260824.json@blob:6b388f3b17eddf1443de12ec6cf9f6db3e6999c2"
  ],
  "source_refs": [
    "integration/prime-fusion-evidence-typed-package:research/PRIME_FUSION_THEOREM_PACKAGE_EVIDENCE_TYPED_FINAL_20260824.md#blob=055bdaaca81c5ac7ab350a71acf3b69fe5e564a9",
    "integration/prime-fusion-evidence-typed-package:research/PRIME_FUSION_T1_T15_FINAL_EVIDENCE_MATRIX_20260824.csv#blob=3c9f6fa670f9405eebbab6eae5d5374c2de4a037",
    "integration/prime-fusion-evidence-typed-package:research/PRIME_FUSION_FINAL_DEPENDENCY_GRAPH_20260824.md#blob=54d1fbb8c3fb657ac55f556c982501386a8eaf25",
    "integration/prime-fusion-evidence-typed-package:research_output/evidence/PRIME_FUSION_FINAL_PACKAGE_MANIFEST_20260824.json#blob=6b388f3b17eddf1443de12ec6cf9f6db3e6999c2",
    "driver_reviews/PRIME_FUSION_F1_LEAN_FINITE_ALGEBRA_FORMALIZATION_DRIVER_REVIEW_20260825.md@d94be81c99bb9b300969a7a8cabb26299e248941",
    "EnterpriseMath/PrimeFusion.lean@main:9825c13ff368a1feda37f2baacc7a777d967b8db"
  ],
  "evidence_status": "MATHEMATICS_ACCEPTED_F1_LEAN_MAIN_PUBLICATION_ATTRIBUTION_UNRESOLVED",
  "last_progress_ref": "main@9825c13ff368a1feda37f2baacc7a777d967b8db",
  "last_progress_at": "2026-08-25T11:30:00+08:00",
  "hard_block": null,
  "tags": [
    "prime-fusion",
    "publication",
    "prior-art",
    "classical-attribution",
    "claim-strength",
    "evidence-typing",
    "Lean-status",
    "no-new-mathematics"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PFPUB",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-PRIME-FUSION-F1-LEAN-FINITE-ALGEBRA-FORMALIZATION",
  "successor_gate": {
    "new_information_gap": "Prime Fusion now has an accepted corrected mathematical package and an F1 finite-algebra Lean slice merged to main, but publication readiness is still unresolved: theorem truth and machine checking do not determine historical novelty, classical attribution, permissible claim wording, paper architecture, or whether the strongest honest release form is a theorem paper, structural research note, or expository/formalization note.",
    "why_parent_result_does_not_close_it": "F1 verifies a bounded finite-algebra proof kernel only. It does not search external literature, classify classical antecedents, establish novelty, audit all fifteen statements for publication wording, or determine which theorem rows are machine-checked versus only independently proved in prose.",
    "discriminating_outcomes": [
      "a venue-neutral publication package is release-ready with theorem-by-theorem attribution and bounded claims",
      "the package is publishable only as an expository/structural/formalization note after classical attribution removes novelty framing",
      "specific theorem claims require wording or organization repair before submission",
      "material prior art or unsupported novelty framing blocks the proposed research-paper positioning"
    ],
    "kill_condition": "If publication positioning requires asserting novelty without adequate literature support, erasing classical antecedents, overstating the F1 Lean coverage as all fifteen theorems, restoring the pre-repair T10 full-root reading, adding a new theorem, or introducing asymptotic/factoring-speedup claims outside the frozen package, stop and return an explicit rewrite/expository/block disposition.",
    "alternative_route_or_free_exploration_considered": "The alternative user-authorized route was further formalization. F1 is now merged to main; further theorem formalization is not required to answer the publication-attribution question and would not itself resolve prior art or claim strength. The user explicitly prioritized Prime Fusion, so publication review is the minimal next gate while preserving theorem closure.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The theorem-package and F1 tasks are closed at their own scopes. Reopening them for literature positioning would mix proof evidence with publication governance. A separate review owner makes attribution and claim-strength judgments independently auditable without changing the accepted mathematics."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:9c1f03a5086432f83d1a3821893be5589124293bc5be5b14d4b7e196220271c7",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Prime Fusion — Publication Attribution, Claim-Strength, and Release-Form Review

Status: `READY / DRIVER_APPROVED / PUBLICATION REVIEW / NO NEW MATHEMATICS`

Task-ID:

`GS-PRIME-FUSION-PUBLICATION-ATTRIBUTION-AND-CLAIM-REVIEW`

Owner branch:

`review/prime-fusion-publication-attribution`

Hard target:

`PRIME_FUSION_PUBLICATION_PACKAGE_ATTRIBUTION_CLAIM_STRENGTH_AND_RELEASE_FORM_INDEPENDENTLY_CLASSIFIED`

## 0. Purpose and separation

This is a publication/prior-art review, not another theorem-discovery or replication task.

Frozen facts at task start:

- corrected T1–T15 package accepted by Driver;
- all fifteen retained theorem rows have independent audit coverage, with mixed evidence types explicitly preserved;
- corrected T10 is the channel-oriented mixed locus `M_{p,q}`, not the full root set of the fused polynomial;
- F1 finite algebra is Lean-checked on main at `9825c13ff368a1feda37f2baacc7a777d967b8db`;
- F1 does **not** mean all fifteen theorem rows are Lean formalized.

The review must keep four questions separate:

1. is the statement mathematically accepted at frozen scope? — already answered by prior Driver reviews;
2. is it machine checked? — only where current Lean declarations actually cover it;
3. what is its classical/prior-art status? — this task must investigate;
4. what may a publication honestly claim? — this task must decide.

Do not reopen theorem truth unless external literature exposes an exact contradiction or the frozen package is being misquoted.

## 1. External literature / prior-art search

Perform a serious external literature search for each theorem family, not just a keyword scan.

At minimum investigate classical antecedents around:

- Gaussian and Eisenstein norm forms and primitive representations;
- `Phi_4`, `Phi_3`, comaximal polynomial factors, CRT/product quotient rings and discriminants/resultants;
- roots of `x^2+1` and `x^2+x+1` modulo primes and composite CRT moduli;
- quadratic reciprocity / supplementary laws underlying T9;
- local orders 4, 3, 12, inversion orbits and cyclotomic-unit actions underlying T10/T11;
- representation reconstruction from pairs of quadratic-form values;
- square-free semiprime/product-of-fields characterizations;
- local root counts in one-parameter quadratic corridors;
- finite-torus/unimodular change-of-variables mean preservation underlying T15;
- graph/matching consequences analogous to T14.

Prefer primary papers, standard monographs, MathSciNet/zbMATH-style bibliographic records where accessible, journal articles, and authoritative books. arXiv is acceptable for relevant modern work but must not substitute for older primary/classical attribution when that literature is known.

For every material citation record enough metadata to identify the work reliably: author, title, year, publication/source and DOI/URL where available.

Absence of a found reference is **not** proof of novelty. Use explicit confidence labels.

## 2. Theorem-by-theorem attribution ledger

For each T1–T15, assign exactly one primary attribution class:

- `CLASSICAL_STANDARD` — essentially a standard theorem/identity in established language;
- `CLASSICAL_DIRECT_COROLLARY` — immediate or routine from standard named results;
- `CLASSICAL_COMPOSITION` — the exact row is a composition of established ingredients, with no demonstrated new theorem strength;
- `PROJECT_SPECIFIC_REPACKAGING` — information-equivalent but organized around the Prime Fusion interface/coordinates;
- `POSSIBLE_NEW_COMBINATION_NOT_ESTABLISHED` — no exact antecedent found after serious search, but novelty is not established;
- `MATERIAL_PRIOR_ART_OVERLAP_REQUIRES_REWRITE` — existing literature materially overlaps the intended research claim;
- `ATTRIBUTION_UNRESOLVED` — search coverage is inadequate to classify responsibly.

Do not use `NOVEL` as a final class merely because no exact phrase was found.

For each row also record:

- exact frozen theorem statement/scope;
- independent evidence type from the final evidence matrix;
- Lean status: `LEAN_F1_MAIN`, `NOT_YET_LEAN_FORMALIZED`, or an exact narrower description;
- nearest classical object/result;
- strongest citation(s);
- what, if anything, is project-specific;
- confidence (`HIGH`, `MEDIUM`, `LOW`);
- publication-safe wording;
- forbidden/unsupported wording.

## 3. Mandatory claim guards

The publication package must retain all of these guards:

### T10

Define explicitly

`M_{p,q}={x mod pq : x^2+1=0 mod p and x^2+x+1=0 mod q}`

and state the four-phase result only for this oriented locus.

Preserve the `H=91` 4-vs-8 witness or an equivalent explicit note showing why the full fused-root reading is false.

### Evidence language

Allowed:

`15/15 retained theorem rows independently audited`.

Not allowed:

`15/15 blindly replicated`.

### Lean language

Allowed:

`the F1 finite-algebra kernel is Lean-checked on main`.

Not allowed unless separately proved later:

`all fifteen theorems are Lean-verified`.

### Result-level language

Do not promote Prime Fusion to L3/L4 merely from package completeness or formalization.

No claim of:

- infinitely many dual-prime cells;
- Bateman–Horn asymptotics as a theorem;
- factoring speedup or efficient factorization algorithm;
- global three-sector seam theorem;
- historical novelty without evidence.

## 4. Publication architecture review

Determine the strongest honest venue-neutral release form.

Evaluate at least these architectures:

### A. Research theorem note

A small number of main results, with T1–T15 grouped into logical theorem families and technical lemmas, only if the attribution review identifies a defensible research contribution beyond standard repackaging.

### B. Structural/expository research note

Prime Fusion presented as a coherent interface joining Gaussian/Eisenstein/cyclotomic/CRT structures, with original value claimed only in organization, typed readouts, or project-specific interpretation where supportable.

### C. Formalization-backed note

A paper whose distinctive value is the evidence pipeline plus Lean-checked finite-algebra kernel, while clearly marking unformalized theorem rows.

### D. No submission in current form

Use if prior-art overlap or claim ambiguity is too strong and publication would overstate contribution.

Do not choose a specific journal unless the evidence naturally justifies a venue class. This task is venue-neutral.

## 5. Required publication package

Produce all of:

1. `research/PRIME_FUSION_PUBLICATION_ATTRIBUTION_LEDGER_20260825.csv` — T1–T15 attribution/claim matrix;
2. `research/PRIME_FUSION_CLASSICAL_PRIOR_ART_REVIEW_20260825.md` — literature review with citations and search coverage;
3. `research/PRIME_FUSION_PUBLICATION_PACKAGE_20260825.md` — venue-neutral abstract, introduction positioning, grouped theorem statements, evidence/formalization note, limitations and corrected T10 wording;
4. `research/PRIME_FUSION_PUBLICATION_CLAIM_GUARDS_20260825.md` — allowed vs forbidden wording, including novelty and Lean claims;
5. `research/PRIME_FUSION_PUBLICATION_BIBLIOGRAPHY_20260825.bib` or an equivalent complete bibliographic source file;
6. `research_output/evidence/PRIME_FUSION_PUBLICATION_REVIEW_MANIFEST_20260825.json` with source refs, searched literature domains/queries or equivalent search log, and artifact digests;
7. `research_returns/PRIME_FUSION_PUBLICATION_ATTRIBUTION_AND_CLAIM_REVIEW_RETURN_20260825.md`.

The publication package may reorganize T1–T15 into theorem families for readability, but it must preserve a machine/audit-readable mapping back to every retained row.

## 6. Review discipline

Do not add T16/T17.

Do not prove new theorems to rescue publication positioning.

Do not change Foundation definitions.

Do not infer novelty from unusual notation or from the Enterprise coordinate vocabulary.

Do not treat Lean formalization as novelty evidence.

Do not hide negative controls, especially the T10 full-root counterexample.

If a theorem is standard but its project-specific packaging is useful, say exactly that.

If the exact combination may be new but literature coverage cannot establish it, use `POSSIBLE_NEW_COMBINATION_NOT_ESTABLISHED` rather than a novelty claim.

## 7. Final classifications

Return exactly one primary publication disposition:

- `PRIME_FUSION_PUBLICATION_READY_WITH_BOUNDED_RESEARCH_CLAIMS`;
- `PRIME_FUSION_PUBLICATION_READY_AS_STRUCTURAL_OR_EXPOSITORY_NOTE`;
- `PRIME_FUSION_PUBLICATION_REWRITE_REQUIRED_BEFORE_SUBMISSION`;
- `PRIME_FUSION_PUBLICATION_BLOCKED_BY_MATERIAL_PRIOR_ART_OR_UNSUPPORTED_CLAIMS`;
- `PRIME_FUSION_ATTRIBUTION_REVIEW_INCOMPLETE`.

Also return one Lean/publication synchronization status:

- `F1_LEAN_SCOPE_CORRECTLY_DISCLOSED`;
- `LEAN_SCOPE_DISCLOSURE_REQUIRES_REPAIR`.

## 8. Stop condition

Stop when every retained theorem row has an attribution class, citation/confidence record, evidence/Lean label and publication-safe wording; the venue-neutral package and bibliography are frozen; and one final publication disposition is selected.

Do not open another Prime Fusion research or formalization task from this review.
