# EC49FOQ — Complete three-key neighborhood: exact native BRC terminal/profile injectivity

Date: 2026-11-14. Research mode: independent portable work, NOT_REVIEWED. Continuation of EC49FOP [PR #2419](https://github.com/awdawmip/enterprise-math/pull/2419); this document is a new finite result, not a formal Task/CLAIM/Result/Review.

## Frozen input and precise theorem

The same pinned original BRC corpus is used: scientific pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; `master_and_radius3_cases.txt` SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`. It has 94 signed-prefix word families, 178850 words and 38169 distinct seven-key configurations. The reference cache is case 32315, `{0,4,5,11,37,39,81}`.

Let `E_K(l)` be the named legal-root set for each of the 24 demand labels. Define
`N3 = {i: |K_i \\ K_32315| <= 3 AND E_i(l)=E_32315(l) for all 24 labels}`.
Root identities are 03,05,06,07; the seven optional labels and permitted roots are
`5:{05,07}, 7:{06,07}, 13:{06,07}, 15:{03,05,07}, 17:{03,06,07}, 19:{03,05,07}, 21:{03,06,07}`.
All other 17 labels are forced. Thus each case has exactly `2^3*3^4 = 648` complete legal root allocations.

For root r let `D^K_r(S)` be the exact minimum number of non-root native byte-trie vertices needed to cover named root demands S using selected signed-prefix codewords. `P(K)` denotes the 168 reachable named root-subset costs `D^K_r(S)`. `T(K)` denotes the 648-vector of complete allocation costs `sum_r D^K_r(S_r(rho))`.

**Finite exact result:** `N3` consists of **966** configurations, partitioned by exact number of key substitutions as `1,73,337,555` for distance `0,1,2,3` respectively. There are **427** distinct vectors `T(K)` and **427** distinct vectors `P(K)`. For all **466095** unordered case pairs in `N3`,

`T(K)=T(K') iff P(K)=P(K')`.

Exactly **10702** unordered pairs are equal under either observation. There are zero observed nonzero globally invisible cross-root cost gauges in this **entire N3 finite set**. Exactly 38 cases, including the baseline 32315, retain both its terminal and root-cost vectors.

Compared with the previously certified radius-2 census (411 cases, 178 classes, 4068 equivalent pairs), this adds 555 radius-3 cases, 249 further observer classes and 6634 additional same-cost pairs.

## Exact enumeration proof and implementation evidence

1. Parse the original 38169 seven-key cases. For every key, obtain each label's allowed root from the first byte of its original signed-prefix words. For each case compare the exact 24-label root-domain tuple to case 32315. Select distance at most three by set difference of the seven keys. This yields all 966 indices, exhaustively from the frozen corpus.
2. Use the *same native rooted byte-trie min-plus DP* as EC49FOP, not a substituted numeric or Euclidean model: at each trie vertex combine child covered label masks by bitwise OR and additive costs, count one per used non-root vertex, then close over supersets. Output every mandatory-plus-optional reachable rooted subset as an integer. There are 168 root-subset coordinates per case; **162288** unique case/root/mask/cost entries were checked. All root-domain/mask coordinates match the reference.
3. Earlier EC49FOP certified 411 cases (69048 entries). A C++17 -O3 expansion emitted 518 *complete* 168-row case blocks before the process was interrupted, with the incomplete last case excluded. Its 215 cases overlapping the previous verified set agree on all **36120** exact integers. A separate, clean C++17 run for the remaining 252 cases completed successfully (42336 entries, 17.18 seconds). The new complete blocks contribute 50904 + 42336 entries, with the old rows supplying the other 69048. The merged 966-case table has no duplicate or missing case/root/subset coordinates. Interrupted or truncated rows are not used as evidence.
4. Independently in Python, enumerate the `648` product assignments for each case; form exact complete costs by summing the four named root table entries. Group all 966 complete-cost vectors *by exact integer-tuple equality*; separately group all 966 reachable root-cost vectors. Every terminal group contains one and only one root-cost vector. The converse follows immediately by summation, giving the biconditional for every pair. The 427 groups yield `sum(group_size*(group_size-1)//2)=10702` equal pairs. The 38 baseline-equal terminal cases are exactly the same 38 baseline-equal projected-profile cases.
5. The comparison uses exact integers, not tolerances or hash equality. Frozen corpus SHA256 is checked before counting. The included local reproducibility bundle contains the original input, the previously verified C++ source, selection and exact grouping verifiers, full profile tables, raw run logs, the 966-case index list, result JSON, and checksums. The original GitHub EC49FOP reproduction source remains at [PR #2419](https://github.com/awdawmip/enterprise-math/pull/2419).

Original completion evidence in the local bundle: `EC49FOQ_RADIUS3_PROFILES.csv` includes interrupted prefix blocks (only certified complete case blocks are used); `EC49FOQ_REMAINDER_PROFILES.csv` is a separate fully completed run. The new `VERIFY_EC49FOQ_RADIUS3.py` performs exact overlap, coverage, domain, all assignment costs and collision assertions. The result file is `EC49FOQ_RESULTS.json`. Scientific inputs remained frozen.

## Scope, interpretation and next question

This is an **exhaustive finite author-checked theorem for N3**, not a universal injectivity theorem. Abstract nonzero gauges exist in the rank-11 kernel constructed in EC49FON, and EC49FOO exhibits such a gauge in a separately constructed native prefix model. The natural next discriminating problem is to search the remaining `38169-966` rows by named legal-root domains for a same-terminal/different-root-cost pair, preferably first in the 32315 domain outside radius three. A more scalable scheme should cache rooted prefix signatures and compare exact terminal groups before a full pairwise enumeration; any candidate collision requires a complete signed-prefix witness and four-root cost delta.

P000 (six discrete native axes in Heartbeat World, time separately typed) remains unchanged. This is a BRC native signed-prefix observer calculation; it makes no additional claim about complete X6 cell states or time evolution.

Status: `AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED`. GitHub publication is a portable research artifact, not formal Task authorization or mathematical admission.
