# R5 — Non-nested endpoint observation partitions for all 30,876 nine-state pairs

**Date:** 2026-11-19. **Status:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. This is a portable scalar-observer result, not a native X6 identification, canonical Result/Review, new formal CLAIM or RUN.

## Scientific input (unchanged)

- Frozen scientific Source: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`.
- Frozen exact center table: `EXACT_R5_ALL_101_BUDGETS.json`, SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`, 1,549,048 bytes.
- Physical query costs and budgets: `k=214,...,314`; 256 *named* integer-center scalar hypotheses `N_h(k)`. Correct response interval at diameter `tau` is `|y-N_h(k)| <= tau/2`.
- Context `H=(18,24,82,34,17,144,208)`. Each unordered pair `x<y` outside H defines the nine *distinct named slots* `(18,24,82,34,17,x,144,208,y)`. Do not merge independent error counters.
- Fifth-diameter interval endpoints: `L=25845652773852463277015040000` and `U=58182461585441404127941754880`; the rightmost included integer test is `U-1=58182461585441404127941754879`.

## Finite theorem: the L and U-1 signature quotients are not nested

For a query k and state pair P, define the response-support family `S_k(P,tau)` as the inclusion-maximal subsets of the nine indexed states simultaneously consistent with one correct scalar response. Define `P ~_tau Q` iff these maximal-support families are **exactly equal as indexed mask families for every one of the 101 physical budgets**.

Exhaustive grouping of every `binom(249,2)=30,876` state pair using full exact-byte signatures yields:

| Invariant | Exact count |
| --- | ---: |
| Classes of `~_L` | 1,460 |
| Classes of `~_(U-1)` | 2,026 |
| Nonempty intersections of the two partitions (joint endpoint signatures) | **2,563** |
| L-classes split across multiple U-1 classes | 508 |
| U-1 classes split across multiple L-classes | 509 |
| Maximum U-1 classes in one L-class | 8 |
| Maximum L-classes in one U-1 class | 3 |

Thus **neither endpoint equivalence partition refines the other**. These 2,563 are *two-endpoint joint-signature* classes; equality at both endpoints is not here asserted to imply signature equality at the 16 interior chamber representatives, at every real tau, or for a native X6 model.

For an additional exact consistency count, among all unordered pairs of pair-instances, 2,399,087 are equivalent at L, 1,447,239 at U-1, and 1,364,220 at both. Of these, 1,034,867 are equivalent only at L and 83,019 only at U-1. These are cross-tabulation counts, not numbers of distinct physical states.

### Explicit two-sided counterexamples

Set `A=(0,3)`, `B=(0,5)`, `C=(0,4)`. For **all 101 actions**:

- `A ~_L B`, but `A !~_(U-1) B`. At budget 221, the U-1 maximal-support mask families are `S(A)=(45,192,274)` and `S(B)=(18,45,192,256)`.
- `A ~_(U-1) C`, but `A !~_L C`. At budget 221, the L maximal-support mask families are `S(A)=(13,18,32,192,256)` and `S(C)=(13,32,192,274)`.

Masks use the frozen ordered nine slots and least-significant-bit first. Each endpoint equality was checked over **every physical action**, not merely k=221. The differing k=221 supports witness strict inequivalence.

### Proof of exact support enumeration and classification

For centers `c_0,...,c_8` at a fixed k, a real response y accepts precisely the centers in the closed interval `[y-tau/2, y+tau/2]` of width tau. For every nonempty maximal accepted set, shift this window so its left boundary is the smallest accepted center. All formerly accepted centers remain inside; the shifted window contains no fewer centers, and maximality forces equality. Therefore every maximal support is one of the nine **center-rooted closed windows** `[c_i,c_i+tau]` after deleting duplicates and proper-subset masks. This is a complete finite enumeration for arbitrary integer or real tau.

Build each nine-slot full signature by concatenating, in physical-budget order, the sorted list of maximal indexed masks. Enumerate all unordered x,y and group by the *entire exact signature bytes*, not a hash prefix. Intersect the two resulting equivalence partitions by pair identity, count their nonempty cells, and exhibit the counterexamples above. This proves the finite theorem independent of any author-side optimization heuristic. An independently implemented doubled-response-endpoint/cell sweep also agrees with the center-rooted construction on the sampled cases.

### Consequence for adaptive f-error costs

At one **fixed** tau, exact full 101-action indexed-support equality gives identical Bellman successors and action costs for *all* finite error budgets f, with one error counter for each named slot. Thus equivalent pair-instances have the same value and all forced-first-action values at that fixed tau. The theorem does *not* infer such equality from distinct endpoint representatives across different tau.

The existing 110 certified U-1 classes covering 15,203 pair-instances still yield the original throughout-[L,U) cost conclusion via **upper-endpoint monotonicity plus the separately proved 8-state lower bound of 8335**. The new joint quotient is a structural diagnostic and guard against invalid chamberwise class reuse, not a reason to repeat those solved costs or to claim a new full-256 lower bound. The latter stays `8335 <= C_8^* <= 8343`.

## Reproducibility and validation boundaries

1. Input file SHA-256 checked against the frozen source. Exhaustively visited all 30,876 pairs in disjoint index chunks [0,6000), [6000,12000), [12000,18000), [18000,24000), [24000,30876). Serialized each *complete* endpoint mask signature as binary with support-count delimiters; groups compared full byte strings.
2. Reconstructed L and U-1 partitions: 1,460 and 2,026 classes, matching independently published endpoint class counts. Reconstructed the entire U-1 ordered partition, representative IDs and exact multiplicities against the earlier immutable 2,026-class `partition_2026.json` SHA-256 `a690289267b06e82b0b76bc91d9cf19a2be42548b5a7076b4d715da40911987b`.
3. Reconciled all joint cross-tabulation cells and checked both counterexamples as whole 101-action equalities. **13,534 independent interval-endpoint/cell sweep comparisons** on three witness pairs plus 64 deterministic sampled pairs, 101 budgets and two endpoints all passed: `PASS_R5_CROSS_ENDPOINT_RECONCILED`.
4. The full 17 distinct global internal noise thresholds of the frozen 256-state table in (L,U) were separately enumerated exactly. **No exhaustive 18-chamber nine-state quotient was computed**; endpoint joint-signature classes must not be advertised as whole-interval equivalence classes.
5. Verifier files `cross_chunk.py`, `analyze_cross.py`, `VERIFY_CROSS_ENDPOINT.py`, and `VERIFY_CROSS_CACHED.py` plus result JSON and execution output comprise the local reproducibility package. For rebuilding, supply the unchanged frozen table and preceding nine-state partition. The direct one-pass verifier can be slower than bounded chunk runs; no time-based theorem assertion is made.

**What is new:** a precise double non-refinement theorem, explicit counterexamples, and the complete 2,563-class endpoint-crossing census. **Not new:** the already verified 110 nine-state cost classes; no extra C8 solve or fresh f=8 cost reduction was claimed this round.

## Next discriminating research question

Classify the 30,876 nine-state pair-instances by their *complete 18-chamber support signatures*, using the 17 exact internal thresholds and safe reuse of the endpoint cross-tabulation. Test whether any jointly endpoint-equivalent pair-instances split in an interior chamber; give an explicit first witness or prove stability for this frozen table. Separately, for the still-unsolved 1,916 U-1 classes, prioritize a strict `C_8>8335` certificate or a full-256 strategy costing at most 8342, without repeating the 110 solved classes.

Provenance: original R5 author/activity `EM-DIRECT-4C3E47 / RA-F2257922D00B2FE4C4818DBD`. This branch publication preserves the frozen science and all historical contributors. Independent review remains `NOT_REVIEWED`.
