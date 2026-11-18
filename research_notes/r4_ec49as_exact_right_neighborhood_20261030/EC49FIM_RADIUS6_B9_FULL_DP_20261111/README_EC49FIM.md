# EC49FIM — Exhaustive six-way union closure of both B=9 six-path BRC neighborhoods (2026-11-11)

**Frozen scientific pin:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Native ordered signed-X6 prefixes, nine-state BRC observer, 24 observation labels and seven full original raw cache keys are held fixed. Follows EC49FIL and EC49FIK on PR #1730.

## Finite theorem

Let W be either pinned seven-key 94-prefix witness A or B. Let Q range over all six-label subsets of the original 24 demands for which (i) neither H2 label is selected, (ii) the fixed 18 witness paths already use all seven original raw keys, and (iii) their prefix union F(Q) contains exactly 84 distinct nonempty native prefixes. There are **8,700** such Q for A and **8,700** for B.

**The minimum possible total native-prefix cost of satisfying all 24 labels by reselecting only the six Q paths, with at most seven full cache keys, is 94 for every Q in this class.**

Proof certificate: 93 total prefixes would allow at most B=93-84=9 new prefixes. Because the fixed paths already occupy seven complete raw keys, every replacement must also use one of these keys. For each label j and legal replacement w, form D_Q(w)=P(w)\F(Q). The complete original catalog contains 178,850 signed-native legal words, and 9,838 belong to these seven keys. A complete one-demand/two-demand exact test (EC49FIK A; EC49FIL B) rejects 8,568 Q per profile by identifying a pair for which every legal union exceeds nine. The remaining **132 Q per profile** are passed to the exact six-level union-set DP.

At DP stage j, every feasible state is a union of candidate D sets for j labels. The recurrence takes all unions X|D with bit_count(X|D)<=9, and removes only inclusion-dominated states. If X subset Y, then X union Z subset Y union Z for every remaining Z; dominance deletion therefore preserves every possible future feasible completion. Both 132-case runs terminate with zero states at **depth 6 in each case**. This rules out all 8,700 Q per witness. Retaining the original six witness paths gives 94 as an upper bound, so the minimum is exactly 94 in the stated domain.

| Profile | B=9 positions | Pairwise rejected | Six-way DP rejected | 93-prefix feasible | Minimum total |
|---|---:|---:|---:|---:|---:|
| A | 8,700 | 8,568 | 132 | 0 | 94 |
| B | 8,700 | 8,568 | 132 | 0 | 94 |

This is a completed finite local theorem and reusable bounded-budget DP specialization, not the global seven-key minimum.

## Reproduction and artifacts

From the containing `research_notes/r4_ec49as_exact_right_neighborhood_20261030/` directory, run `python EC49FIM_RADIUS6_B9_FULL_DP_20261111/VERIFY_EC49FIM.py --profile A` or `--profile B`. The script consumes the sibling EC49FGW original catalog/witness module and the appropriate EC49FIL exact pair-survivor file. GitHub stores all pair survivors and all DP execution traces in lossless gzip-base64 JSON artifacts. Decode by `base64 -d FILE.json.gz.b64 | gzip -dc`; 10087-byte A pair JSON original SHA256 `758c8fcf45faec8d8e2a5bad240d3d69613ec835da52ddcf2b657c3813ee7654`. A/B DP trace SHA256 (initial actual executions) `cffbadf749466c8d05c8e54501fc5698dcff32068f6273dd0cef06454c98e4f3` and `eaa6e7b1010d32dcd58e17d48e724f464556f90bfd2e654ed1d3f26a5bc0f979`; execution-time fields change on rerun. Reexecuted generic code returned A impossible=132/possible=0 and B impossible=132/possible=0. Code Git blob in local test: `de3f9d854d48a426847b86253380d2235d09479f`.

**Resulting six-path pending inventory:** relative to EC49FIJ+EC49FIK+EC49FIL, A/B each have 24,123 unresolved six-replacement positions: 22,111 retain or force back the original seven keys and 2,012 can release other key allocations. These results are author-side exact finite checks; formal Result and independent Driver review remain to be performed.

**Next:** inspect B=11 and B=13 positions with inexpensive multi-demand bounds, then test six-way exact trie/union DP on survivors; separately solve 2,012 released-key allocation instances. The frozen science pin and protected worldview remain unchanged.
