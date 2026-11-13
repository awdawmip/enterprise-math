# R5: the six adjacent 14-edge pivots form an exact five-simplex, with a certified common four-parameter box

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / INDEPENDENT_REVIEW_PENDING. This is a theorem for the frozen seven-LR P/Q-BRC Blackwell auxiliary transport model, not a native X6-dimension claim.

## Scope and immutable inputs

Frozen science remains global `a01383f825ef9d43b4b754254303298c64041568` and EM `86149263e38c22292c9def1e0f69092efa1be77e`. Reuse the exact 14-edge physical/transport affine chart of PR #1877, immutable `a402aeedef23843fb0bb618e35e2012ee244aeb2`, and the exact six pivot classifications and positivity of PR #1881, immutable `3c7a5446db05fe6c84ec8755b530e88a3e3c3c23`. Their complete rational source vectors and masses are duplicated in `VERIFY.py` for independent reproducibility. P000 retains six native spatial dimensions and an independent time dimension; here the 7 likelihood-ratio indices and the 4+5 parameters are auxiliary statistics and transport degrees of freedom, respectively.

Fix the previously lawful seedless F target `Y`. Let `S` be the 14-edge chart of PR #1877, `r=(5,5)`, `S0=S\\{r}` (13 edges), and let
```
T={(6,1),(6,2),(6,3),(0,5),(2,5),(3,5)}
C=S0 union T         # 19 edges
Delta = 904888979/2817677416250
c = 16537/12960
```
Along the exact PR #1881 physical ray `p=rho_star+delta, q=r=-rho_star-delta, epsilon=3H/4`, `0<=delta<=Delta`, the affine old transport `E_old(delta)` satisfies the 21 Blackwell equalities and has `E_old[r]=-c*delta`. Every 13 other old entry is strictly positive on this interval. Each corresponding physical source is lawful, with `g=b` and the same two stopping times as `Y`.

## Theorem 1: exact five-simplex of all couplings on C

For **every real** `0<delta<=Delta`, the complete nonnegative Blackwell coupling polytope **restricted to support C** is exactly a five-dimensional simplex whose six vertices are the previously constructed six 14-positive-edge pivot couplings `E^(e)(delta)` indexed by `e in T`.

Let `A` be the full 21-by-14 old-column constraint matrix, of rank 14. All six new columns belong to its span. Define the unique rational `alpha_e` by `A alpha_e = A_e` and `beta_e=-alpha_e[r]`. Exact elimination yields
```
e           (6,1) (6,2) (6,3) (0,5) (2,5) (3,5)
beta_e      13/5  13/5  13/5  23/5  2     1
```
For any coupling `E` supported in `C`, put `t_e=E[e]`. The equalities and rank 14 uniquely force, for `k in S0`,
```
E[k] = E_old[k] - sum_{e in T} t_e alpha_e[k].
```
The absent coordinate `E[r]=0` gives the **exact positive budget law**
```
sum_{e in T} beta_e*t_e = c*delta.                       (1)
```
Conversely, define `lambda_e=beta_e*t_e/(c*delta)`. All `lambda_e>=0`, `sum lambda_e=1`, and
```
E = sum_{e in T} lambda_e E^(e)(delta);
E^(e)[e]=c*delta/beta_e, and E^(e)[e']=0 for e' != e in T.
```
Prior exact endpoint positivity (rechecked by this verifier) proves each `E^(e)` is feasible on the whole ray. Hence every such convex combination is feasible, proving both inclusion directions. The six vertices are affinely independent because they have different unique nonzero T-edge coordinates. At `delta=0`, equation (1) forces every new edge to vanish and the restricted polytope collapses to the single 13-edge coupling.

**Face/support classification.** Each nonempty subset `J subset T`, with `|J|=k`, defines one relative-open face of dimension `k-1`; precisely its k T-edges and the 13 common S0-edges carry positive mass, hence there are exactly `13+k` positive edges. This yields 6 vertices (14 edges), 15 open edges (15 transport edges), 20 open triangles (16), 15 open tetrahedral faces (17), 6 open 4-faces (18), and one 5D interior (19). There are `2^6-1=63` nonempty faces. The complete C-restricted affine coupling space has dimension `19-rank(A_C)=19-14=5`.

## Theorem 2: six charts have an explicit common open four-dimensional physical domain

Set `rho_star=17774559/225414193300`, `H=17774559/17507527960` and
```
p0 = (rho_star+Delta/2, -rho_star-Delta/2, -rho_star-Delta/2, 3H/4)
eta = 1/1000000.
B = { (p,q,r,epsilon): |coordinate-p0_coordinate| <= eta }.
```
For **every real point** in the closed four-dimensional box `B`, the source `X0+pU1+qU2+rU3+epsilon U4` is physically lawful, has `g=b`, and matches `Y` at both stopping times. The old affine transport has negative `(5,5)` mass. Each of the six explicit pivot expressions is a lawful Blackwell coupling with 14 strictly positive edges. All six distinct support charts therefore overlap on the **same** full-dimensional physical region, rather than merely sharing a ray.

Certificate: test the 16 rational vertices of `B` for each of the six pivot expressions (96 endpoint charts) and all 21 exact coupling equalities, the physical slacks and equality constraints. Across the vertices:
```
min physical slack, excluding identically zero g-b:
    359701449667/901656773200000 > 0
min pivoted coupling mass across six supports:
    199445082527/4514554080000000 > 0
```
Every relevant expression is affine on `B`; positivity on all 16 vertices implies positivity at every real interior point by convexity. The four physical directions are independent (their `u,v,w,z` components form an identity matrix), and the six barycentric coupling choices span a five-dimensional simplex for every physical point of `B`. Thus the source-flow/coupling pairs supported in `C` include an **injectively parameterized 9-dimensional product-like family** `B x simplex_5`. The statistical marginal observation has rank three on these four source directions by the predecessor exact calculation; the remaining physical parameter is an observer-fiber residual.

## Precision, observer semantics and unresolved target

All assertions are exact rational arithmetic and algebraic arguments extended to all real `delta`, box parameters and barycentric weights. The 63 subset-centroid checks are additional finite consistency tests, not the reason the continuous statement holds. The exact simplex describes the couplings **on the specified 19-edge carrier**; it is a reusable local BRC branch-allocation representation preserving positive edge labels and observer fibers. The project-wide objective remains: decide whether every lawful Blackwell-feasible `g=b` pair admits <=14 positive transport edges or construct a genuine 15-edge-necessary pair.

Next unit: classify which of the other 11 allowed Blackwell edges enlarge this local C-carrier, test neighboring degeneracy walls, and attempt a 15-edge necessity certificate (e.g. exact support-LP infeasibility for every 14-edge candidate in one physical feasible pair). Preserve owner/CLAIM scope and mathematical independent review.

## Evidence

`VERIFY.py`: self-contained Fraction script with exact ranks/column solves, 96 box-corner charts, ray endpoint checks, 63 simplex-face checks per positive ray sample, and all 21 row/column/LR moment equations. `EXACT_OUTPUT.txt`: stdout from actual local execution of that script. Canonical project Source task owner/CLAIM and native scientific checkpoint are separate from GitHub author-side persistence; no independent review or formal acceptance is asserted.
