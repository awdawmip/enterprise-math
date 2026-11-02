# EC49EI — Exact rank dichotomy within a positive-BRC count fiber

**2026-11-02 · Parent EC49EH · author-side analytic proof, two exact checkers PASS, portable Draft PR, unreviewed/not admitted.** Frozen scientific sources: global `773d538180bfb49e24cffeb35c3ee75eb0628e2e`, Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Current project and global behavioral policy were independently read from canonical main. P000 and ACTIVE world unchanged.

## Theorem (all returning word lengths, all strictly positive double-channel BRC weights)

Use original complete native six-axis signed primitive operations:

```
a=(-1,-1), b=(-2,-2),
c=(+1,+2,-1,-2), d=(+2,+1,-2,-1),
e=(+3,+1,+1,-3), f=(+1,-1), g=(+2,-2).
```

Each signed integer `+i/-i` means the primitive `+E_i/-E_i`, not an independent spatial dimension. The historical chart displacement is `-2E1`; future returning operation words have displacement `+2E1`. Observe first occurrence order of `A=(+E1,+E2)` and `B=(+E2,+E1)` through five terminal buckets `N,A,B,AB,BA` on the nine historical seam atoms `N0,N1,N2,A0,A2,B0,B1,AB0,BA0`.

For each nonempty future-word set `F(h,p)` of **exactly h operations** and exactly equal **six-axis positive native-step counts** `p=(p1,p2,p3,0,0,0)`, let `O(h,p)` be the nine-row matrix containing all five terminal indicator columns of all words in the set. Define

```
r=p1+p2-h-1,       e=p3>=1,
f0=p1-2e-r>=0,      g0=p2-r>=0.
```

**Exact Q-rank, for every integer h>=1 and every nonempty fiber:**

```
rank O(h,p) = 9,                       if r>=1;
              5+2*I[f0>0]+2*I[g0>0],  if r=0.
```

Hence rank belongs to `{5,7,9}`. If `r>=1`, four distinct words are necessary and sufficient for full nine-feature observation, representing exactly the four transfer types of `ce,ec,de,ed`. If `r=0`, two words are necessary and sufficient iff `f0>0` and `g0>0`; otherwise the complete fiber itself has rank 5 or 7. The result concerns the declared five-bucket observer, actual ordered six-axis native primitives, strict-positive BRC and the fixed-horizon equal-positive-count fiber.

## Analytic proof

**Fiber algebra.** The native return displacement forces `n_b=0`, `n_e-n_a=1`. Write `r=n_c+n_d`, `e=n_e`, `f0=n_f`, `g0=n_g`. Counting positive signed primitives gives
`p1=2e+r+f0`, `p2=r+g0`, `p3=e`, and `h=2e-1+r+f0+g0`. This proves the displayed inverse formulas and that all nonempty fibers have `r>=0`.

**Only eight event-bearing and three no-internal-event types.** Each operation ends with a negative signed native primitive, so no adjacent-positive A/B pair crosses an operation-to-operation boundary. The only internal events are A within `c`, and B within `d`. The history/future seam depends solely on the first future primitive `+E1,+E2`, or another direction. If `r=0`, there are exactly three transfer possibilities: `O` (first `e`), `F` (first `f`), `G` (first `g`). If `r>=1`, there are exactly eight possibilities. Their nine-row terminal matrices are completely determined by the earliest event(s) and seam and are explicitly reconstructed in the executable checker; the eight exact ranks are `3,3,3,3,2,2,2,2`.

**No-event fiber.** Because `e>=1`, an O-type word always exists. An F-type word exists exactly when `f0>0`, and G exactly when `g0>0`, by placing that letter first and ordering all other letters freely. Their exact observation spans satisfy `rank(O)=5`, `rank(O,F)=rank(O,G)=7`, `rank(F,G)=9`. The F/G representatives `feg,gef` have an integer 9-by-9 observation minor of determinant `-1`. Their transfer matrices are the same for all words beginning with the corresponding first primitive and no internal `c/d` event. These facts give the rank formula and the two-word minimum.

**Event-bearing fiber: four independent necessary types.** In the eight-type universe, omit the type of `ce`: the historical rows `A0,A2` coincide under every remaining type. Omit `ec`: `A2,AB0` coincide. Omit `de`: `B0,B1` coincide. Omit `ed`: `B1,BA0` coincide. The four differences of the corresponding standard basis row vectors are exact integer left-kernel witnesses. Therefore every rank-nine selected family contains all four types, even if it includes any number of words of the other four types. Conversely, the combined four transfer matrices of `ce,ec,de,ed` possess an exact 9-by-9 minor of determinant `-1`, so four types suffice.

Every nonempty fiber with `r>=1` realizes all four types at **identical positive-step counts**: use all `r` event letters as `c` or all as `d`, place that event letter first for the `ce/de`-type history seam, or place an available `e` first for the `ec/ed`-type history seam, and append remaining `a,e,f,g` as needed. The ensuing transfer depends only on the first seam and whether the sequence contains A or B internal events. This proves all-h exact rank 9 and the four-word minimum.

**BRC multipliers and preserved information.** For any strict-positive six-axis weight vectors `x,y`, define positive monomials `X(w)=prod_i x_i^p_i(w)`, `Y(w)=prod_i y_i^p_i(w)`. At one fiber, X and Y are respectively shared nonzero scalars, and for each full ordered history `u` one has exact `X(uw)=X(u)X(w)`, `Y(uw)=Y(u)Y(w)`. Thus the fixed-fiber typed positive-BRC future readout retains the nine-atom observability rank. These are two positive-weight instruments, not a signed/phase cancellation claim. Retain the word identity, native path order and terminal bucket when factoring a shared BRC multiplier.

**Readout-cost distinction.** The four necessary event-bearing type matrices each occupy three nonzero bucket columns (12 raw columns total, nine independent). The two necessary F/G types each occupy five nonzero columns (10 raw, nine independent). This is a certified observer-column count under the given DFA, distinct from trie primitive edge count, BRC arithmetic operations, total storage and wall-clock time.

## Actual exact verification and finite scope

The published `VERIFY_EC49EI.js` was executed in V8 and returned `PASS`, independently of a Python standard-library implementation using exact rational linear algebra (also `PASS`), which is preserved as a separate local evidence archive. JS reconstructs all valid words and equal-positive-count fibers at h=2...7, checks every transfer type and the rank formula using GF(2), exact BigInt Bareiss determinants `-1` for both 9-by-9 witness sets, integer left-kernel row coincidences, and the two strict-positive BRC multiplication identities on actual signed native paths.

| h | returning words | complete p-fibers | fiber ranks 5 / 7 / 9 |
|---:|---:|---:|---|
| 2 | 8 | 3 | 0 / 2 / 1 |
| 3 | 51 | 7 | 1 / 2 / 4 |
| 4 | 304 | 13 | 0 / 4 / 9 |
| 5 | 1770 | 22 | 1 / 4 / 17 |
| 6 | 10224 | 34 | 0 / 6 / 28 |
| 7 | 58947 | 50 | 1 / 6 / 43 |

These are exhaustive **finite** checks through h=7. The every-h theorem follows from the algebra, complete eight/three transfer-type proof, exact necessary kernel and nonzero determinant witnesses, and all-fiber realizations above.

## Actual project status and continuation

GitHub authenticated account: `awdawmip` with repository push. Native Enterprise Math service observed `research_authority_granted=false`; current active-owner listing returned `CONTROL_QUOTA`. This publication is author-side portable evidence in Draft PR #1730 and does not create a native CLAIM, Result, independent Driver review or theorem admission. Original scientific pins, P000 and protected ACTIVE worldview remain unchanged.

**Next EC49EJ:** use the proved 2/4 mandatory-type fiber classification to simplify EC49EH exact prefix MILP and investigate `H>=7` unrestricted equal-positive-count cross-window cost. Decide or produce a concrete counterexample to the candidate `U_eq(H)=min(8H+12,4H+30)`. Report true native prefix-edge cost, shared BRC monomial cost, and observer-column/readout cost as distinct quantities.
