# EC49FJT — 232 high-budget, no-key-release six-path exact local optima

Date: 2026-11-11. Research status: **AUTHOR_EXACT_FINITE / EXECUTED / UNREVIEWED / NOT_ADMITTED**.

## Frozen problem

Frozen science pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Input: the previous EC49FGW native nine-state, signed, ordered X6 microstep operation-word catalogue (178,850 legal words, 94 complete cache-key triples), and the two EC49FGJ 24-demand, seven-key, 94-prefix witnesses A and B. Native prefixes are sequences of *signed and ordered* X6 microsteps, not coordinate endpoints or unsigned sets.

For each witness, choose six demand positions Q, keep the remaining eighteen original operation words fixed, and permit any six replacement words from the same frozen legal catalogue. Let F(Q) be the union of prefixes of the eighteen fixed words, K_F(Q) their complete cache-key set, and B(Q)=93-|F(Q)|. Consider every Q with `|K_F(Q)|=7` and `B(Q) in {24,25,27,28,29}`. Then **the exact minimum total number of distinct native prefixes is 94 for every such Q**.

| B | |F| | A positions | B positions | Both | Minimum added prefixes |
|---:|---:|---:|---:|---:|---:|
|24|69|38|38|76|25|
|25|68|54|54|108|26|
|27|66|12|12|24|28|
|28|65|10|10|20|29|
|29|64|2|2|4|30|
|**Total**||**116**|**116**|**232**||

## Proof and exact coverage

All 24 choose 6 = 134,596 position subsets per witness were scanned using exact prefix/key support masks. The stated filters select exactly the 232 listed contexts. Each fixed background still occupies seven distinct complete cache-key triples; every legal seven-key completion must therefore use precisely those same original keys. This proves completeness of the key choice without assuming that candidate prefixes cannot be shared.

For each position Q and its single allowed key set, take every legal frozen-catalogue word satisfying each omitted labeled demand and construct the trie of signed, ordered X6 microstep prefixes. Entering a trie node costs zero when that complete prefix is already in F(Q), and one otherwise. Let d_v(S) be the minimum additional edge cost for realizing demand subset S in the subtree rooted at v. Include a terminal's demand-mask subsets at zero local cost; merge child u by the subset-convolution recurrence

```
d_new(S union T) = min(d_old(S)+d_u(T)+c(v,u)*[T != empty]), S cap T = empty.
```

Every union of root-to-terminal paths corresponds to a prefix subtree and vice versa, and each distinct new prefix edge is paid once. This recurrence exactly minimizes the new-prefix union for all six omitted demands. Values are clipped at `CAP=B+1`; the root mask result is `B+1` in all 232 cases, and no case has a solution with at most B new edges. The unchanged original witness is an admissible completion with `B+1` added edges, proving each exact optimum equals 94.

The C++17 trie implementation is a source-level adaptation of the already published EC49FJR exact solver; the only algorithmic difference is the accepted CAP set `{25,26,28,29,30}`, appropriate for B={24,25,27,28,29}. Every case was executed, all 232 (profile,Q) identities were checked against the generated input and its B class, and all 232 were found `best_clipped=B+1`, `feasible_93=0`. One valid key option per context, as implied by `|K_F|=7`. Trie sizes ranged from 9,986 to 31,223 nodes.

A separately implemented Python prefix-*set* antichain-union DP reproduced nine selected A-profile instances (covering each of the five budget classes), with exact agreement. This is author-side cross-validation, not independent Driver review. A broader Python sample was attempted but exceeded the bounded compute window; its partial coverage is not counted.

## Verifiable evidence and reproduction

Reproduction dependencies already established in PR #1730: `EC49FGW_RADIUS5_SCREEN.py`, `EC49FGJ_SEVEN_KEY_94_WITNESSES.json`, `ec49fjd_shared.py` (frozen original model), plus `FJR_CATALOG.tsv` regenerable from EC49FJR's `MAKE_B10_B15_RELEASE.py`. Place these four input files beside or as directed by `GENERATE_EC49FJT.py`; the generator needs the frozen dependency module on `PYTHONPATH`.

```sh
PYTHONPATH=<directory-containing-ec49fjd_shared> python GENERATE_EC49FJT.py
g++ -O3 -std=c++17 FJT_EXACT_TRIE.cpp -o fjt_exact
./fjt_exact FJR_CATALOG.tsv FJT_CASES.tsv FJT_CPP_RESULTS.jsonl
```

Author-side executed outputs and SHA256:

- `GENERATE_EC49FJT.py`: `09368a4d4400767adf940cdcd1a09ef50ef9efb124496736c3c679c8dc9fa50a`.
- `FJT_EXACT_TRIE.cpp`: `effee6533ffb1fd99c75ab6976d4a5ad6c4be2b9a8b87a5c81c591f7cf11d53f`.
- `FJT_CASES.tsv` (232 rows): `b3e574011e7a0c60dc48b1eee58799559ad914580a0f5627d4163dc5c9bbde94`.
- `FJT_INPUT_SUMMARY.json`: `94d75b86da34daacc9e8629029a52bc34e835b95dc368ae549868f8f6025d5aa`.
- `FJT_CPP_RESULTS.jsonl`: `5e76cdea8a1fd3c76fc3e3c75ee50fcd2d48c2422f703fea0f4759f74e204ff9`.
- `FJT_PY_CROSSCHECK_REPORT.json`: `ae85d19a58ec13cb672be796e80e6401d111dd1ca62d7251c63881ea74c64db2`.

Full raw catalog, witness JSON, generator dependencies, 232-row input and output and validation report are retained in the author evidence bundle. Other completed classes EC49FJQ (B16–19) and EC49FJR (B10/B12–15) were checked before selecting this not-yet-published high-budget unit; a B16 replication was made locally but not counted as new proof.

## Remaining research

Reconcile the complete radius-six census and separately check whether any uncategorized six-path background persists. Next, test seven-path replacements and direct global 93-prefix searches under the full original seven-key model. The global seven-key minimum `C_min(7)` still has the certified upper bound 94; local radius-six certificates do not substitute for the all-constructions theorem.

**Role/authority:** author-side finite computation on the existing Draft PR. Native session for this run was queued at observation time; no current task CLAIM, formal Result, independent Driver review or admission is asserted.
