# R5 — Exact observer identifiability and information residuals at budgets 292–954

Date: 2026-11-14. Status: **AUTHOR_PROVED / EXACT_BIGINT_CHECKED / NOT_REVIEWED**. This is a new derived-observer result on the frozen R5 scientific input `435e77af0d180eac32bd1f9c4c464bc4010b7551`. It reuses the exact 24-row source at commit `69b0fa35b6c0f191190c66f8d857a175b289370c`, blob `2c6d2ec1e966384d1befd01b5b48825452d5d320`, and the proved optimizer-family prerequisite-mask theorem in PR #2412. It makes no new native X6/P000 or BRC-arithmetic claim.

## Statement: exact observational partitions of all 28-bit closure masks

Let B be any subset of the 28 cuttable gaps, X=1 if cut 15 is closed and Y=1 if cut 17 is closed. For each K, let `F_K(B)=Opt_B(K)` be the **full family of original-index optimal center subsets**, `N_K(B)=|F_K(B)|`, and `J_K(B)` the optimal distance cost. The previous theorem proves that for 292<=K<=954, `F_K(B)` is determined by (X,Y). For 293<=K<=314,

```
N_K(X,Y)=a+bX+cY+dXY,
(a,b,c,d) = (a_empty,a_15,a_17,a_15_17),
```

where cohorts are disjoint, nonnegative, and (b,c)>0 componentwise. The 24 integer rows have been verified with BigInt against the pinned source.

**Theorem 1 (strict count decoder / boundary tie).** Exactly the following cases occur:

| Budget K | Number of distinct N_K values | Exact ordering | Distinct full optimizer families |
|---|---:|---|---:|
| 292 and 315<=K<=954 | 1 | all equal | 1 |
| 293 and 314 | 3 | N00 < N10 = N01 < N11 | 4 |
| 294<=K<=313 | 4 | N00 < N10 < N01 < N11 | 4 |

The middle ordering is strictly `N10<N01` for **every integer K=294..313**, because the exact coefficient difference `c-b` is positive at each of these 20 budgets. Thus **one exact optimizer count at any one of K=294..313 fully decodes the two effective cut bits**. At K=293 or 314 a count leaves the two singleton masks ambiguous; the full index-labelled optimizer family still distinguishes them. No such distinction appears at K=292 or K>=315.

*Proof.* For any K, the four counts are `a,a+b,a+c,a+b+c+d`. The exact source establishes `b,c>0` for K293..314; `b=c>0,d=0` at K293/314; `0<b<c,d>0` at K294..313; and `b=c=d=0` at K292/315. Previous family-invariance theorem extends the invariant case to K315..954. The cohort representation gives disjoint sets of optimal configurations whose prerequisite masks are empty, {15}, {17}, or {15,17}. Positive singleton cohorts make F10 and F01 different sets even when their cardinalities tie, and make all four families different. QED.

**Theorem 2 (exact equivalence-class sizes across all 2^28 masks).** In the fixed-budget count observation, all other 26 closure bits are irrelevant. Consequently:

- K294..313: four equivalence classes, each containing exactly `2^26=67,108,864` full 28-bit closure masks.
- K293 and 314: three classes, with sizes `2^26, 2^27, 2^26`, in increasing count order.
- K292 and K315..954: one class of `2^28=268,435,456` masks.

For the **full optimizer-family** observation, there are exactly four classes of size 2^26 at K293..314 and one class otherwise. Each conclusion is a full 28-bit finite classification proved by the two-effective-bit theorem and the four exact coefficient comparisons; there is no claim to enumerate 268 million masks individually.

**Theorem 3 (exact information content).** Take all 28 closure bits to be independent fair bits. Shannon information (base 2) about the *full 28-bit closure mask* revealed by a deterministic observation equals the entropy of that observation. For K>=292:

| K | H(optimizer count) | H(full optimizer family) | H(optimal cost) |
|---|---:|---:|---:|
| 292 or 315..954 | 0 bits | 0 bits | 0 bits |
| 293 or 314 | 3/2 bits | 2 bits | 0 bits |
| 294..313 | 2 bits | 2 bits | 0 bits |

The 3/2-bit boundary value comes from output probabilities (1/4,1/2,1/4). The 2-bit value comes from four equally likely classes, and the cost observer is constant on all closure masks for K>=214 by the earlier proved cost-invariance theorem. Hence *count* merges two distinct optimizer-family fibers at exactly K293 and K314: their unresolved distinction is one bit conditional on observing a singleton-class count, or **1/2 bit in unconditional expectation**.

For independent but not necessarily equiprobable cut bits X~Bernoulli(p), Y~Bernoulli(q), the strict-decoder region's count entropy equals `h2(p)+h2(q)`. At either boundary budget it equals the ternary entropy of `((1-p)(1-q), p(1-q)+(1-p)q, pq)`. Family entropy remains `h2(p)+h2(q)` for K293..314; invariance budgets give zero. The remaining 26 bits may have any independent distribution and do not alter these equations.

## Independent exact classification and validation scope

The attached `VERIFY_R5_INFORMATION_DECODER.js` is a standard-Node reproducible checker reading the original adjacent `EXACT_R5_REQUIREMENT_ZETA.json`. The same `classify` function was **actually executed** in the connected JavaScript runtime over original pinned GitHub JSON, using BigInt for every optimizer count and class size. It asserted the input pin, all 24 K/J matches, source cohort sign/order conditions, partition sums of 2^28 and the expected exact observation classes. Output: `PASS_EXACT_R5_INFORMATION_DECODER`, with 20 four-valued, two three-valued, and two one-valued rows in K292..315. The 315..954 extension uses the separately proved and cited endpoint-invariance theorem.

Exact examples at K294:
```
N00=296770704568869882883347578880
N10=318932696645557965243033845760
N01=319008985823713925209994035200
N11=342162737216429487140162764800
```
At K293: `N10=N01=13102659259476980304288153600`, while F10 and F01 are different original-index families.

**Mathematical status**: author-side derivation combining previously reported R5 theorems with 24-row exact integer comparisons, not independent proof review. Validation is exact finite classification on the specified frozen integer observer. The original JSON and predecessor mathematical proof are dependencies; no new computation of the 954-event optimization DP was performed here.

## Next unresolved scientific unit

Return to worst-case nearest-old-optimum recourse for cuts 15 and 17 at K293..314. Preserve the exact `max_(new optimum S) min_(old optimum T) |S\\T|` order and use the already established minimal-enabling-mask reduction: only the two minimal backgrounds {} and {the other cut} are needed. Compute and independently verify the actual maximum and extremizing center-index witnesses, rather than inferring them from optimizer counts or entropy. Investigate K214..291 separately.

## Provenance

- Frozen scientific input: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
- Parent theorem/certificate: `research_notes/portable_direct/r5_requirement_zeta_20261114/RESEARCH.md`, PR #2412, immutable commit `69b0fa35b6c0f191190c66f8d857a175b289370c`.
- Exact prerequisite cohorts: `research_notes/portable_direct/r5_requirement_zeta_20261114/EXACT_R5_REQUIREMENT_ZETA.json`, blob `2c6d2ec1e966384d1befd01b5b48825452d5d320`.
- Previous cost invariance: Draft PR #2373; optimizer family / recourse: Draft PRs #2379, #2398, #2402, #2407.
- Current writer: independent research-notes continuation. Historical Researcher `EM-DIRECT-B78E55` and Activity `RA-33C87C2B703418F0706695E9` are provenance, not a new Task CLAIM.
