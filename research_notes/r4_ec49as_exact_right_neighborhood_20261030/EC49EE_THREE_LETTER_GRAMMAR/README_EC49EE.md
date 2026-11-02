# EC49EE — Minimal three-letter return grammar: sharp native X6 primitive-trie cost

Date: 2026-11-02. **Author-side analytical proof and executed exact checks; portable draft, unreviewed and not admitted.**
Parent EC49ED, preceding immutable PR #1730. Frozen scientific inputs: global `773d538180bfb49e24cffeb35c3ee75eb0628e2e`, Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. P000 and ACTIVE Heartbeat World remain unchanged.

## Definition and scope
Use genuine ordered signed native X6 operations
`c=(+E1,+E2,-E1,-E2)`, `d=(+E2,+E1,-E2,-E1)`, `e=(+E3,+E1,+E1,-E3)`. A historical path has displacement `-2E1`; a future return word of exactly h operation letters has displacement `+2E1`. Adjacent pairs A=(+E1,+E2), B=(+E2,+E1) can straddle the history/future seam. Five mutually exclusive final observations distinguish N (neither), A-only, B-only, AB (A first), BA (B first). The nine historical memory atoms in ordered basis are N0,N1,N2,A0,A2,B0,B1,AB,BA (EC49DX). Real ten-step X6 paths realizing all nine atoms at identical positive counts are embedded in `VERIFY_EC49EE.js`.

The two strictly positive multiplicative BRC channels are `X(w)=prod_i x_i^p_i(w)` and `Y(w)=prod_i y_i^p_i(w)`, where `p_i` counts positive native axis steps; path count is the third instrument. For a returning word set W let `rank(W)` be the rational rank of its 9×5|W| terminal-bucket transfer columns; define T_cde(h) as the smallest number of **distinct nonempty signed native primitive path prefixes** in a trie spanning a rank-nine W. T_cde_equal imposes equal complete positive-count vectors for all selected words. Paths are never reduced to apparent spatial diagonals; the observer retains order and provenance.

## Exact all-h theorem
For **every integer h>=2** and all positive BRC weight vectors,
[
\boxed{T_{cde}(h)=T_{cde,\mathrm{equal}}(h)=16h-4.}
]
At h=1 only e returns and has terminal rank 5. Values at h=2,3,4,5,6,7,8: **28,44,60,76,92,108,124**.

### Proof, part I: return count and BRC
c and d have zero complete X6 displacement; e has +2E1. Thus every returning h-letter word contains **exactly one e**, with the remaining h−1 letters from c,d. All such words have exactly 4h signed native steps and the *same* complete positive-count vector `(h+1,h−1,1,0,0,0)`. Their BRC future factors are the common nonzero constants `x1^(h+1) x2^(h−1) x3` and `y1^(h+1) y2^(h−1) y3`. They may therefore be divided out of each instrument's terminal transfer without discarding any native sequence: `T_cde_equal=T_cde` as optimization problems, for all positive weights.

### Proof, part II: exact transfer classes and four necessities
All c,d,e operations end in a negative primitive, so the only seam effect comes from the first operation. If it is e, the first +E3 creates no seam A/B. A suffix containing only c produces signature C; only d produces D; mixed c and d produce CD or DC according to first internal event. If c is first, its internal A may be preceded by a seam B only when the history ended in +E2; the signatures are lower-case c (no subsequent d) or cD. If d is first the symmetric possibilities are d and dC. The eight classes C,D,CD,DC,c,cD,d,dC are exhaustive for h>=3; at h=2 only C,D,c,d occur. In particular **Z (no A/B future event) never occurs**.

In row order (N0,N1,N2,A0,A2,B0,B1,AB,BA), the terminal-label vectors are:
- C = (A,A,A,A,A,BA,BA,AB,BA);
- D = (B,B,B,AB,AB,B,B,AB,BA);
- c = (A,A,BA,A,AB,BA,BA,AB,BA);
- d = (B,AB,B,AB,AB,B,BA,AB,BA).

Four explicit *integer left annihilators* force all four types in every rank-nine W: without c the A0 and A2 rows agree; without d the B0 and B1 rows agree; with no Z, without C the A2 and AB rows agree; with no Z, without D the B1 and BA rows agree. These are exact identities across all eight transfer types, verified by the native seam update.

Conversely the nine word/bucket columns `[C:A,C:AB,C:BA,D:B,D:AB,c:A,c:AB,d:B,d:AB]` have **determinant −1** on the nine actual historical atom rows. This integer minor proves that any four words representing C,D,c,d already span all nine features, regardless of h. Explicit representatives are `C=e c^(h−1)`, `D=e d^(h−1)`, `c=c^r e c^(h−1−r)`, `d=d^r e d^(h−1−r)` for 1<=r<=h−1. This gives both sufficiency and the four-class necessity with no finite-h extrapolation.

### Proof, part III: signed primitive prefix lower bound and attainment
Prune any rank-nine W to one word of each of the four indispensable types; removal cannot increase trie size. Each retained word has 4h signed primitives. C and D **must** start with e and then differ at the first primitive of their second letter (+E1 vs +E2). Their exact shared native primitive prefix is therefore the four-step e and nothing longer. Lower-case c and d necessarily start with different +E1 and +E2, and neither shares a nonempty primitive prefix with the e-first words (starting +E3). Hence any rank-nine W has at least `4·(4h)−4=16h−4` distinct nonempty primitive prefixes.

The actual four returning X6 paths
[
W_h=\{e c^{h-1},\ e d^{h-1},\ c^{h-1}e,\ d^{h-1}e\}
]
realize all four transfer signatures, the unimodular minor −1, and exactly four shared edges. They attain 16h−4 for every h>=2. All selected words have equal positive counts, proving the equal-cost claim as well. QED.

## Executed evidence
`VERIFY_EC49EE.js` is the **actual executed self-contained JavaScript checker** and `EC49EE_EXECUTED.json` is its original output. It reconstructs nine genuine ten-step native signed X6 historical paths with identical positive-step counts, the future seam, all returning cde words h=2..10, complete transfer classes, four left-kernel identities, an exact 9×9 BigInt Bareiss determinant, shared-primitive-prefix costs and common BRC positive-count vectors. For h=2..6 it exhausts alternative representatives of the four indispensable types and checks the minimum. Rational rank is certified by reduction mod 1000003 for 0/1 9-row matrices: each minor has absolute value <=k^(k/2)<=19683 for k<=9, strictly below the prime, so rational and modular ranks coincide. Finite tests check the implementation and concrete witnesses; the algebraic proof establishes the all-h statement.

An independently implemented Python standard-library checker also ran locally and audited all h=2..10 and **all 4-word selections at h=2,3,4**. Its original source, JSON output and complete fuller prose proof are retained in the accompanying local evidence archive; this GitHub document and checked JavaScript evidence are sufficient to reconstruct the theorem. Neither check is a Source-native Result or independent Driver review.

## Scope, comparison, next
The result concerns this declared ordered-path terminal observer, strictly positive BRC and primitive *prefix* trie cost; no change to native physical dynamics or external physics is inferred. Compared with EC49ED's unrestricted operation grammar, the three-letter grammar pays an exact additional `7h−14` trie edges for even h and `7h−11` for odd h, while automatically equalizing the BRC count factors.

**Next EC49EF:** require rank-nine return observations for *every* horizon h=2,...,H and minimize the native primitive-prefix trie of their **union**, retaining horizon labels and different known BRC multipliers. Solve H=3..5 exactly, then derive all-H bounds or a formula. Current GitHub author identity is `awdawmip`, but Source-native RESEARCHER session creation was refused as `STATIC_READONLY_SCOPE_DENIED` with `operation_sent=false`; active Owner read returned `CONTROL_QUOTA`. Author storage does not assert activity, CLAIM, Result or admission.
