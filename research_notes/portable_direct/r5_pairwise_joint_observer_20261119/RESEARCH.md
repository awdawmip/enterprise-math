# R5 — exact pairwise carrier and indispensable joint observation direction

Date: 2026-11-19. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Scope: independently saved portable scalar-observer research; no Task CLAIM/RUN, Result, Review, native X6 identity claim, or mathematical promotion.

## Preserved frozen inputs

Frozen scientific lineage: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`.
The original 101-budget by 256-state center table `EXACT_R5_ALL_101_BUDGETS.json` retains byte SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. Its exact 18-stage thresholds are in the original `stages_18.json`; this research reuses those frozen bytes without changing the input or its interpretation. The original complete family census is `research_notes/portable_direct/r5_full18_chamber_cross_quotient_20261119/RESEARCH.md` at commit `a661f387ef8819ef95a7121d4e73e6b677f64ee5`.

The 30,876 named nine-slot instances are `(18,24,82,34,17,x,144,208,y)`, with `x<y` outside the fixed seven H. The 101 action budgets are k=214,...,314. The scalar observation diameter is within the fifth noise interval `L=25845652773852463277015040000`, `U=58182461585441404127941754880`. All 17 interior threshold differences over all 101×256 frozen center arrays are represented in the 18 stages; no further gap arises before U.

## Theorem 1: lossless indexed pairwise-clique carrier

At budget k and noise diameter tau, write c_i for the exact integer center attached to named slot i. An observation support is a nonempty slot subset S contained in a single scalar closed window of length tau, or equivalently `max(c_i:i in S)-min(c_i:i in S)<=tau`. Write F for its inclusion-maximal supports.

Define the indexed graph G on named slots 0,...,8 with edge ij iff `abs(c_i-c_j)<=tau`. Then **F equals the family of maximal vertex cliques of G**. Each window-supported set is a clique. Conversely, for a clique the minimum and maximum center belong to the clique and their distance is <=tau, so one length-tau window contains the whole clique. Furthermore, G can be reconstructed from F: ij is an edge exactly when some member of F contains both i and j. This proves a *two-way exact equivalence of indexed representations*.

Let o_ij(k) be the first of the 18 threshold stages at which ij becomes an edge (use 18 when it never does). Its full 18-stage membership sequence is `1[j>=o_ij]`. Among 36 edges of nine slots, 21 fixed-H edges are constant across all candidate pairs; the remaining 15 include 7 x–H edges, 7 y–H edges and the joint x–y edge. Equality of the 18-stage complete maximal-support signatures over all 101 budgets is therefore exactly equivalent to equality of these 15 onsets per budget. The statement is for this scalar closed-interval observer only; it does not erase signed branch, source, amplitude or native X6 residual information.

## Theorem 2: exact finite class census and joint-direction nonredundancy

An exhaustive independently repeated census over the pinned 30,876 instances and all budgets/stages returned:

| Indexed edge-onset carrier | Distinct profiles |
| --- | ---: |
| 14 x–H and y–H onsets, excluding x–y | **1,663** |
| x–y onset alone | 145 |
| All 15 onsets | **2,711** |
| All 15 onsets, only at the interval endpoints | 2,563 |

Exactly **448** unary-only profile classes split when adding the x–y joint onset; the full quotient has 1,048 more classes than the unary quotient. The 2,563 endpoint classes refine into 2,711 entire-interval classes: 108 split, of which 68 have two daughters and 40 three daughters. These totals independently reproduce the previously verified direct maximal-family census.

A fully explicit information-loss witness is A=(x,y)=(0,1) and B=(0,49): all their 14 variable–fixed onsets coincide for every budget and every stage. Yet for budget k=294 and tau=L, c_0=c_1=`296770704568869882883347578880`, while c_49=`342162737216429487140162764800`. The gaps x–y are respectively 0 and `45392032647559604256815185920` (> L). Each individual variable state is still L-compatible with each of the seven fixed states, but the maximal named support masks are `F_A={511}` and `F_B={255,479}`. Therefore the x–y joint relationship is essential even though every unary compatibility comparison agrees. This supplies a concrete scoped joint-relation residual, not a universal BRC/X6 nonredundancy assertion.

## Independent reproduction and operation accounting

`VERIFY_PAIRWISE_ONSETS.py` checks the frozen original JSON hash and independently counts all onset equivalence classes, using only exact integer gaps and stage insertion points, not the earlier C++ maximal-support signatures. `VERIFY_PAIRWISE_CLIQUES.py` separately compares graph maximal cliques with direct center-window supports for 72 reproducibly selected candidate pairs x 101 budgets x 18 stages = 130,896 exact families and checks the concrete witness. A separately executed C++ implementation and full frozen input, exact 18 thresholds, logs and checksums are included in the accompanying full-reproduction ZIP.

To reconstruct all 15 variable onset arrays by caching, it suffices to evaluate 7·249·101=176,043 unary distances and C(249,2)·101=3,118,476 joint distances; the 21·101 fixed-background distances are shared. This is an exact *representation and recomputation reduction*, not a benchmarked speedup: onset calculations and the previous 56,132,568 maximal-support evaluations are different operation units. Time, memory, table acquisition and end-to-end verification costs are not inferred from these counts.

The full census is author-checked, and independent mathematical review remains NOT_REVIEWED.

## Next exact research unit

Test nonconvex or disconnected response supports: pairwise edges need no longer imply a jointly realizable observation, so derive the minimum higher-order intersection witness, preserving named provenance. Separately continue the unresolved nine-state Bellman C8>8335 lower-bound search. Existing full-256 eight-error bounds remain 8335<=C8*<=8343, unchanged by this observer-only theorem.
