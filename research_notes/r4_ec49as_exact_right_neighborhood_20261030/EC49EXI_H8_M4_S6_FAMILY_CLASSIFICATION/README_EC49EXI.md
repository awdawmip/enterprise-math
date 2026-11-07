# EC49EXI — Exact H8/M4/S<=6 BRC key-family classification and h8-first-use minimum

Date: 2026-11-03 (Asia/Shanghai). Author-side finite symbolic native-X6 research; Draft PR #1730. Parent EC49EXH at `75d87a7277b12808b0e295297afa5356bc15d608`. Frozen scientific inputs inherited unchanged: GLOBAL_KNOWLEDGE_V1 `773d538180bfb49e24cffeb35c3ee75eb0628e2e`; Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Current behavioral sources were separately read at GK main `5dc525fe0cd48ccab8d5515c6f27721e53719431`, EM main `c9cb7d5659bfa8376d3955ba07a835062c9d188e`. P000 startup projection checked against original blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`; ACTIVE worldview preserved.

## The finite mathematical problem

Continue the exact seven-operation model and nine-history rational observer of EC49EXF/EXH, with six signed native axes, ordered full primitive-step paths, two strictly positive *symbolic* BRC channels separately indexed by the complete six-axis positive-count key, and prescribed displacement (2,0,0,0,0,0) at each horizon h=2,...,8. Let E denote the union count of distinct nonempty native primitive-step prefixes, M the number of globally distinct complete positive-count keys, and S the number of distinct observer transfer signatures. The base horizon h2 forces four rank-nine signatures T4 and key (3,1,1,0,0,0); if S<=6, the full-rank horizon fiber is either T4 (four required signatures) or the additional pair T2 (two required signatures), by EC49EXF's complete 11-signature/21-pair rank classification.

**Theorem EC49EXI-1 (complete family classification).** For H=8, exactly M=4 and S<=6, there are **14,092** sets of four BRC keys that can serve full-rank horizon fibers, and **55,493** assignments of a chosen key and a full-rank T4/T2 family to every horizon h2..h8 using all four keys. Exactly **42** of the 64 conceivable T4/T2 seven-horizon family patterns occur. The 55,493 assignments partition as follows:

| When fourth key first appears | h8=T2 | h8=T4 | Total |
| --- | ---: | ---: | ---: |
| h8 (first seven use three keys) | 5,456 | 23,104 | 28,560 |
| by h7 (first seven already use four keys) | 11,582 | 15,351 | 26,933 |
| Total | 17,038 | 38,455 | 55,493 |

Counts by total number of T2 horizons are 0:630, 1:13,104, 2:26,025, 3:13,694, 4:2,040, 5:0, 6:0.

**Theorem EC49EXI-2 (exact first-use h8 subfamily optimum).** Restrict to all H8/M4/S<=6 solutions for which the fourth distinct BRC key first appears at h8. Then

    min E = 90.

If that eighth-horizon fiber is T4, the separate bound is E>=94. Therefore every possible E<90 global M4 solution must have already used all four BRC keys by h7. The previously verified EC49EXH native witness has E=90 and first introduces its fourth key at h8, with T2 at h8.

## Exhaustive proof and verification

Operation b is excluded from return by its unique negative axis-2 net displacement. For any returning h-operation word, #e=#a+1. Write w=#e, r=#c+#d, f=#f, g=#g and complete positive count key p=(u,v,w,0,0,0). The exact counts are

    r=u+v-h-1, a=w-1, f=u-r-2w, g=v-r.

At each h=2..8, enumerate all nonnegative (w,r,f,g) satisfying 2w-1+r+f+g=h, split c+d=r and enumerate all multiset permutations of a,c,d,e,f,g. Expand every word into its original signed primitive-step path; apply the original nine-history transfer automaton and calculate the full key. The complete returning-word counts are 8, 51, 304, 1,770, 10,224, 58,947, and 340,064, totaling 411,368. The observed transfer universe has exactly 11 signatures.

Exhaustive fiber classification over these exact finite words establishes:

    T4 full-rank fiber possible iff r>=1;
    T2 full-rank fiber possible iff r=0, f>=1, g>=1.

The conditions also require w>=1 and all counts nonnegative. For h2 the sole full-rank key is p0=(3,1,1,0,0,0). Distinct keys that support at least one required full-rank fiber across h2..8 number exactly 84. Per-horizon full-rank T4 key counts are [1,3,7,13,22,34,50]; T2 counts are [0,1,2,4,6,9,12]. These exact conditions are independently used to count key sets without enumerating operation words.

For each unordered triple K of the 83 other eligible keys, form Q={p0} union K. Enumerate each horizon's allowable key/family pairs and count assignments that use all four keys. Independently obtain the same integer by inclusion-exclusion over the three non-base keys:

    N(Q) = sum_{B subseteq K} (-1)^(3-|B|) product_{h=3..8} [sum_{k in {p0} union B} #AllowedFamilies(h,k)].

The h2 choice is fixed and already uses p0. Exactly 14,092 Q have N(Q)>0; their sum is 55,493. The direct Cartesian assignment count and analytic-key inclusion-exclusion match **for every Q**, not just in aggregate. The first-use split and T2-number histogram are generated from actual assignments; the independently checked count inputs are exact integers, with no floating-point tolerance.

For EC49EXI-2, the earlier exact H7/M3/S<=6 theorem (EC49EV) gives E7>=86. The terminal-prefix lemma proved and used in EC49EXF applies to every returning h8 word: each distinct terminal native operation contributes two primitive suffix edges absent from all complete shorter-horizon words, because the operation encoding is prefix-free. Consequently any rank-nine T2 fiber requires at least four newly used edges, and any T4 fiber at least eight. Hence E8>=86+4=90 (respectively >=86+8=94 for T4). The existing EC49EXH witness has E8=90 and introduces key (5,4,1,0,0,0) only at h8, attaining the subfamily lower bound.

This proof is entirely in the frozen symbolic paired BRC/native-X6 operation model. The explicit four-key unrestricted global optimum remains open. No changes are made to P000, ACTIVE worldview, formal TASK admission, or any earlier signed-path definitions.

## Reproduce and evidence

From a checkout of PR #1730, run:

    python research_notes/r4_ec49as_exact_right_neighborhood_20261030/EC49EXI_H8_M4_S6_FAMILY_CLASSIFICATION/VERIFY_EC49EXI.py

The verifier reuses the unchanged EC49EXH enumerator at ../EC49EXH_H8_M4_S6_E90/BUILD_EC49EXH_FIXED_DP.py. It reconstructs all 411,368 words and 11 signatures; checks the independent r/f/g fiber criterion against every exact key fiber; enumerates 55,493 family assignments; checks each key-set count by inclusion-exclusion; and writes EC49EXI_EXECUTED.json with PASS and the exact partition. The locally executed source produced the published results in this directory.

**Next EC49EXJ:** run exact prefix-tree lower certificates on the remaining 26,933 family assignments with all four keys used by h7. First reuse the H7/M4 schedule-specific exact predecessor bounds; whenever E7 + required terminal suffix >=90, prune without re-solving the H8 trie. Perform exact OR-mask native-prefix DP on the residual schedules; construct a genuine <90 witness if one exists. Keep the separate H8/M3/S<=4 144-edge certificate problem active.

## Authority / research disposition

At this run, authenticated GitHub identity is awdawmip with repository admin/push access. The native owner-list read returned CONTROL_QUOTA; active Source owner and a native research session were not verified. This is **AUTHOR_EXACT_FINITE_CLASSIFICATION / INDEPENDENT_COUNT_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED**. GitHub branch publication is scientific evidence storage, not a native Result or Driver mathematical acceptance.
