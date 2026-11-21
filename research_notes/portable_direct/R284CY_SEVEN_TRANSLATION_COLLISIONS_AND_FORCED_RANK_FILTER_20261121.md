# R284CY — Seven endpoint-translation collisions and the forced-rank filter

Date: 2026-11-21 (Asia/Shanghai)
Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**
Research mode: independent portable Port observer; no shared Task CLAIM.

## Frozen input and previous frontier

- Immutable source: `awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py`, Git blob `b46e0f682b58e47c27094b4bea6fa4e55119a3ee`. Current-main read yielded this same blob.
- Frozen site enumeration SHA-256: `b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4`.
- `P=17179869143`, 65,536 distinct sites, 64 labeled circular arcs. At each site `x`, let `d_k(x)` be the `k`-th **smallest** exact integer distance to these arcs. Thus `d_64(x)` is the farthest-arc distance.
- R284CW gave the entire minimum-core uniqueness classification. R284CX explained four exceptional equalities by two arc-endpoint shifts. This note exhausts **all site pairs for exactly those two shifts**, then distinguishes endpoint equality from a genuinely unforced top-R cutoff.

The shifts from R284CX are

```
Delta_A = P - (s_19+w_19) + (s_18+w_18) = 6669045998
Delta_B = s_21 - s_37                 = 4503221351
```

The label direction is A: 19 to 18; B: 37 to 21. These are external finite Port observer arcs, not native X6 spatial axes or physical time.

## New finite theorem

**Theorem (exact two-shift collision census).** Let `X` be precisely the frozen 65,536-site set. For `delta` in `{Delta_A,Delta_B}`, inspect every **ordered** pair `(x,y)` with `x in X`, `y=(x+delta) mod P in X`. Then:

1. For shift A there are **79** ordered population pairs, of which **6** satisfy `d_64(x)=d_64(y)`. Every one of those six has unique maximizing arc labels `(19,18)`; its source matrices differ only at zero-based lower entry 6.
2. For shift B there are **8** ordered population pairs, of which **1** satisfies `d_64(x)=d_64(y)`. Its unique maximizing arcs are `(37,21)); its lower entries 0 and 1 are exchanged.
3. Every site in the entire 65,536-site population has a unique farthest labeled arc.
4. Of the seven distance-equal pairs, **three** are already absorbed by a forced site at their top-R level-64 cutoff, at `R=3061,3607,6515`; precisely four have both members individually unforced there, at `R=779,1263,1563,7587`. The latter four are exactly the exceptions independently globally classified in R284CW.

This adds three previously unlisted **shadow equalities** to the four R284CX examples; they are real endpoint-aligned equalities but produce no extra minimum-core choice.

## Exact certificate table

For each row, `[a,b]` is the complete descending level-64 tie rank block, and `tau(x),tau(y)` are each site's earliest individually mandatory rank across `k=2,...,64`. A pair is **unforced at its cutoff** precisely when both tau-values exceed `a`.

| Shift | x | y | d64 equality | Tie block | tau(x) | tau(y) | Status at R=a |
|---|---:|---:|---:|---:|---:|---:|---|
| A | 6055669926 | 12724715924 | 8416662779 | [779,780] | 780 | 780 | both unforced |
| A | 6051057018 | 12720103016 | 8412049871 | [1263,1264] | 1264 | 1264 | both unforced |
| A | 6048093436 | 12717139434 | 8409086289 | [1563,1564] | 1564 | 1564 | both unforced |
| A | 6039387349 | 12708433347 | 8400380202 | [3061,3062] | 1664 | 3062 | x already forced (k=36) |
| A | 6036196871 | 12705242869 | 8397189724 | [3607,3608] | 1602 | 3608 | x already forced (k=36) |
| A | 6024527197 | 12693573195 | 8385520050 | [6515,6516] | 1394 | 4286 | both already forced (k=36,8) |
| B | 10044326029 | 14547547380 | 8381496764 | [7587,7588] | 7588 | 7588 | both unforced |

All pairs have exactly two occurrences in the corresponding level-64 tie block. The three shadow pairs, including their original matrix enumeration indices, are captured in the JSON certificate. In each A pair the lower-index 6 bit flip preserves the same upper matrix; for the B pair the two-entry swap preserves the same upper matrix.

## Proof and verification coverage

**Collision enumeration.** Generate all frozen words with the original integer determinant/Port function and check the embedded SHA-256 and distinctness assertions. Construct the site hash set. For each of the two frozen shifts, map each site through `x -> (x+delta) mod P` and retain exactly those images in the hash set. This loop visits every ordered pair for that fixed shift once; by set membership it omits no such pair. It returns 79 and 8 pairs respectively.

**Farthest-arc comparison.** Independently evaluate all 64 exact integer circular distances for each frozen site, retaining the maximum and every attaining arc. The global winner multiplicity is one for every site. For each retained translation pair, compare the two maxima and the arc labels. The integer comparisons yield six A collisions, one B collision, and no other farthest-distance equalities under these two shifts. Direct evaluation validates the endpoint identities above. The code checks actual matrix enumeration indices and the exact lower-entry changes.

**Forced-rank criterion.** For a site `z`, let `b_k(z)` be the final descending rank of the entire equal-value block containing `d_k(z)`; define

```
tau(z) = min_{2 <= k <= 64} b_k(z).
```

At any `R`, the site is forced individually into every top-R-preserving core if and only if `tau(z)<=R`, by the completed equal-block lemma of R284CW. At a level-64 tie block `[a,a+1]`, the cutoff `R=a` requires one of its two sites. If either is already forced from another level, the pair's cutoff quota is already fulfilled; it creates no new minimum-core choice. If both are unforced, a genuine binary residual requirement remains *at that level*. Whether the global minimum core has exactly two choices still depends on all other level quotas and is supplied by the complete independent R284CW classification.

For the 14 sites in the seven pairs, sort each of the 63 nonconstant level rows descending with duplicates intact. The exact block endpoint is the number of values greater than or equal to the given site value; integer binary search returns each `b_k(z)` and the minimizing level(s). The calculated tau values are the table above. This is an exhaustive finite proof with reproducible integer computations, not an extrapolation from the four known R284CX examples.

**Scope and limitations.** The new exhaustive claim covers **only the two explicitly given shifts**. It does not assert that all possible matrix mutations, all equalities of farthest distances or all generalized Port observers are classified by them. No formal peer review or native-X6 model admission has occurred. The code uses Python unbounded exact integers and tests the original population, not a sampled subset.

## Reproduce and follow up

Run `python R284CY_seven_translation_collisions_checker.py` beside the unchanged pinned `R284CO_spectral_witness_checker.py`. It writes `R284CY_seven_translation_collisions_certificate.json`; test the JSON equality of the seven pair records, their rank blocks/tau and shift counts against the published certificate. All 65,536 x 64 distances and the 63 rank sequences are recomputed. No randomness, floating arithmetic or hidden data are used.

**Next question:** Enumerate candidate shifts generated by allowed *single-bit flips* and *two-entry swaps*, then determine which shifts align two upper-envelope arcs over nonempty exact integer intervals. Combine the geometric intervals with the joint forced-rank incidence to predict shadow versus globally free ties without sorting the complete 63-by-65,536 distance spectrum. Preserve labels and residue provenance; do not collapse distinct sites on equality of the scalar farthest distance.

## Source/ownership

P000 and the ACTIVE Heartbeat World X6 premise remain unchanged. The object above is a frozen auxiliary Port observer with its source input pinned; no new shared-task CLAIM, PROGRESS, Result or Review is asserted. Historical source attribution of this line: `EM-DIRECT-20B766` / `RA-617F40704F37299B15489DCA`; current private native execution authority and Activity association must be separately established. Mathematical status: `AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED`.
