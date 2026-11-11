# GEO6 Gen2 — bounded canonical-authority and selector-DAG seed (2026-11-12)

Status: **AUTHOR-CHECKED PARTIAL UNIT / UNREVIEWED / NOT_ADMITTED**. This is a source-preserving evidence note, not a Gen2 Result, review, canonical task checkpoint, or complete current-head delta scan.

Research lane: `chatgpt-research-onhour-enterprise-math-20260923` (ordinary GitHub Chat subject). Old D25 CLAIM was released through `onhour-d25-20261112-0121-source-lambda-checkpoint-release-v1`; current dispatch request `onhour-research-20261112-0336-canonical-dispatch` was still QUEUED when this note was started. This note makes **no** claim of GEO6 ownership.

## Mother objective and frozen input

Current task candidate: `RS-GEO6-OBJECTIVE-SEMANTIC-SELECTOR-SYNTHESIS / TP2-AA14FBBC7B234E6DCD4A`, publication generation 3, taskbook `research_tasks/GEO6_OBJECTIVE_SEMANTIC_SELECTOR_SYNTHESIS_PUBLICATION_ENVELOPE_REPAIR_V3_20261011.md`.

Frozen mathematics: `RR-35C4FE925E9C12E53604`; Gen1 selector atlas and resolver manifest at snapshot `228446b2d797372b2d18503116f612ba03701184`. They encode 12 selectors, 66 pair classifications, 7 direct DAG edges, six roots, 0 fully resolved / 3 partially constrained / 9 unresolved / 0 duplicates, three bounded recommendations. These old files and original authorship are unmodified.

## Completed bounded unit: source review authority

The following seven **exact current-main** review records were fetched from `research_result_reviews/<RR>/<DR>.json`. For each: the file exists, `result_id` and `review_id` match, `disposition=ACCEPTED`, and `terminal=true`:

| Gen1 result | Current canonical review | Observed Git blob SHA-1 |
| --- | --- | --- |
| RR-73C4AC1CB16F08C64FC4 | DR-8F7328B65924F20CE3DA | 6813ff3227391877949d3cc1bffb159db643825e |
| RR-774CF0739BD6CD117CF6 | DR-B84D90C29024FFBB4A22 | c167a18d6a369fc6009b45b9e16ded3976454cb5 |
| RR-0C7464292459CAF82805 | DR-BFFACB80B9FC4584EB37 | 89d2ac7e050dd91533449f4ab13f488afda1a252 |
| RR-7A29C4C19E5F83B602D7 | DR-1E9A6C4B2F7D3058A4C1 | e0f6bf44e90ba489029cab17f0eb5a2ed38e3232 |
| RR-985AEE277DE45AFCC9D8 | **DR-61B4E8C29A705FD31746** | f6718b76318b2535fbc66fa91fe47872dab4ea00 |
| RR-8A7F3C29D14E6B50C2F1 | DR-A43FBD4CE025D9DACC72 | 8c0db26461d57c97b4a74bd40556dda23941e88d |
| RR-5137B2C5D070E4CEA95E | DR-082CBBED2C7411D276E0 | 931a690337f732a216d84761134f4450313b6a33 |

The Gen1 manifest points `RR-985AEE277DE45AFCC9D8` to **superseded** `DR-6D2A91F4C8E3057B1246`, whose expected current-main path returns GitHub 404. The current review `DR-61B4E8C29A705FD31746` is verified `ACCEPTED`, with the same Result-ID. This is a **review-authority correction**, not a new mathematical resolver. The six other Gen1 cited DR paths remain present and ACCEPTED.

The native-rotation/mixed direction task publication `RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE / TP2-D6A41E9C3B705F821847` was separately fetched: `record_state=ACTIVE`, generation `18`. Its existing no-duplicate gate is retained; the publication's task runtime ownership must still be checked at final execution.

## Exact finite graph consistency certificate

Read the frozen `selector_atlas.json`: `pair_matrix.upper_rows` has lengths 11,10,...,1, exactly 66 coded pairs. Their multiplicities are `ORTHOGONAL=53`, `STRICT_DEPENDENCY=9`, `OVERLAP_NOT_EQUIVALENT=4`; no `SAME_SELECTOR` or undecided pair appears in this frozen matrix.

The seven direct edges are `3→5, 1→6, 6→7, 8→9, 8→10, 8→11, 6→11`. Their transitive closure is **exactly** the nine strict-dependency matrix pairs:
`1→6, 1→7, 1→11, 3→5, 6→7, 6→11, 8→9, 8→10, 8→11`.
The acyclic graph's six indegree-zero roots are `0,1,2,3,4,8`, equal to the stored roots. Status `P` occupies indices `0,2,7`; the old counts and three recommendations are preserved. These finite computations were executed directly against the fetched atlas (66 pairs and 12 nodes).

Focused portable checker: `research_checks/GEO6_GEN2_CANONICAL_AUTHORITY_SEED_CHECK_20261112.py` (GitHub commit `86c3555ddc6fa9e71cc00e4d20e7870b344f18fe`). It checks the original seven accepted review files, exact Gen17 authority replacement, Gen1 graph closure and the Gen18 P000-L1 record in a working checkout. **That Python file has been published; a checkout-level execution of it is not yet evidenced.** The finite graph computation and individual remote review reads above are the checks actually performed this turn.

## Unfinished Gen2 hard target and exact continuation

The complete review-delta inventory from Gen1 snapshot `228446b2d797372b2d18503116f612ba03701184` to a fresh execution base remains open. In particular, the seven known accepted reviews prove only the existing Gen1 cited resolver set; they do not exclude later **new** canonical accepted P000/Full-Cell evidence. The generic Git compare between the Gen1 snapshot and observed main `d113139d0a0e599bb31f7d0c5d745a0438277190` reported over 12,000 intervening commits and a 300-file truncation. That truncated comparison is not an exhaustive delta list.

Next exact action: reconcile original GitHub Chat dispatch request, verify actual selected task/current publication and session eligibility; obtain own valid prepare→CLAIM→open before the formal Gen2 work. Through the current Source/authorized review index or a complete bounded source history, enumerate all canonical ACCEPTED P000/Full-Cell review+Result changes since frozen snapshot, filter against each of the 12 selector contracts with exact type maps, and write complete delta/manifest_v2/atlas_v2/current-head checker/execution record. Reuse unchanged Gen1 mathematics where no new accepted datum forces drift. Only then publish a new formally authorized Result; leave publication of successor tasks to the Driver.

No native benchmark was reclassified; no other conversation's identity or claim was used. The current D25 H0/B0 native experiment and support item #1559 remain separate, still NOT_RUN/PENDING_OWNER at last checked D25 frontier.

## One later Full-Cell scientific datum, classified at its actual evidence level

A distinct 2026-10-17 Full native Cell adjacency result and its nonauthor technical whole review were actually read at current main:

- `research_notes/owner_goal_20261017/native_x6_adjacency_automorphism_cf1677/NATIVE_X6_FULL_CELL_ADJACENCY_AUTOMORPHISMS_ARE_SIGNED_AFFINE_DERIVED_NOTE_V1.md` (blob `45a01f07e9a7b7ebc599029c3e4f62b26b38c9be`).
- `research_notes/owner_goal_20261017/reviews/native_full_cell_adjacency_nonauthor_185026/NATIVE_X6_FULL_CELL_ADJACENCY_SIGNED_AFFINE_NONBLIND_COMPLETE_TECHNICAL_WHOLE_REVIEW_AND_CONTEXT.md` (blob `348d8d7b997cd288fa3ff4ed353aaa20e9f088eb`).

The exact theorem concerns **all graph automorphisms of the undirected signed-unit adjacency graph on the full spatial `Z^6` Cell torsor**. The given proof reconstructs opposite directions by common-neighbor cardinalities and then shows constant signed unit increments, classifying automorphisms as translations followed by signed coordinate permutations. The independent technical report records a complete bounded PASS for that relation but explicitly says it creates no canonical Research Result/Driver Review or P000 promotion. Neither fetched document contains a canonical `RR-...`/`DR-...` record binding.

**Candidate delta:** `ROTATION_CLOSURE_SELECTOR` and `MIXED_DIRECTION_SELECTOR` (also `TRANSLATION_ACTION_SELECTOR` as background). Disposition at this read: `CONTEXT_ONLY`. The type map preserves undirected Cell adjacency `A\subset X_6\times X_6`; it supplies no typed implication that an adjacency graph automorphism is a physically admissible P000 native rotation, a dynamically realizable translation or the required mixed/refinement transport. Thus this author/reviewer material may inform a future route but does not alter the 0/3/9/0 canonical Gen1 classification. This is one explicitly sampled later candidate, not the complete post-snapshot inventory.
