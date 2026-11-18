# Addendum — cluster order persists exactly while all boundary gaps remain positive

Date: 2026-11-09. This addendum strengthens the `n*eta<1/q` sufficient condition in the companion PROOF.md; it preserves the definitions, model and frozen science pin there.

## Exact order criterion

With `m>=q`, `n>=m`, the reduced rational `p/q`, sign-reflected positive perturbation `theta_+=k/q+eta` and residue boundary gaps `G_r(n)=1/q+(r_plus-ell_r(n))*eta`, assume

```
G_r(n)>0 for EVERY r=0,...,q-1.                         (2)
```

Then the circular phase cut order consists of q consecutive residue clusters in the cyclic order of `r*k mod q`, each internally ordered by its source indices. Consequently the exact correction formula (1) of PROOF.md is valid **without** requiring `n*eta<1/q`. This holds for rational or irrational theta; for negative epsilon use theta ↔ 1-theta reflection.

**Proof.** In the universal real-line lift, list points of residue r in increasing source index, beginning at `{rk/q}+r*eta`, and write the final lifted point as `{rk/q}+ell_r(n)*eta`. Their adjacent gaps are all `delta=q*eta>0`. The lift of the first point in the next cyclic cluster is one base step `1/q` beyond the first current cluster base, offset by `r_plus*eta` (include a full turn at the wrap). The lifted end-to-next-start gap is precisely `G_r(n)`. Positivity (2) makes this one simple ordered cyclic chain. The sum of all `n` displayed gaps is

```
(n-q)*delta + sum_r G_r(n) = (n-q)*delta + 1-(n-q)*delta =1.
```

Hence the chain completes exactly one turn, gives the circle-cut order, and admits the same subdivision and longest-subarc proof as PROOF.md. QED.

Because every `G_r(t)` is nonincreasing in t, checking (2) at N certifies the full interval `m<=n<=N`. At the first nonpositive `G_r`, the nominal cyclic cluster ordering breaks; that boundary can be treated separately by an adjacent phase-order update. The signed correction formula is an exact `O(q)` algorithm within the largest prefix satisfying (2).

## Frozen S23 stronger interval and first order break

For the frozen S23 auxiliary observer, use `p/q=16/61`, `k=45`, `eta=16/61-theta`, `m=128` and the strict 24-decimal enclosure from PROOF.md. Across the **entire certified theta interval** each `G_r(n)>0` for every `128<=n<=225`, whereas at `n=226` one boundary gap becomes strictly negative:

```
r=42; ell_42(225)=164; ell_42(226)=225; r_plus=0;
G_42(225)=1/61-164*eta >0;
G_42(226)=1/61-225*eta <0.
```

Thus the mixed-cluster exact risk formula continues through n=225, well beyond the old sufficient bound n<=180. For every integer n=128,...,225,

```
R_theta(128,n-128) =
    (n-128)*(16-61*theta)                     if 128<=n<=164,
    36*(16-61*theta)+(n-164)*(164*theta-43)   if 165<=n<=225.
```

In particular, the newly certified full endpoint is

```
R_theta(128,97) = -2047+7808*theta  (n=225).
```

The first nominal cluster boundary exchange is at `n=226`. Independent exact circle-subdivision there gives

```
R_theta(128,98) = -2090+7972*theta,
```

whereas continuing the old cluster correction formula after `G_42<0` incorrectly returns `R_theta(128,97)`. This is a concrete exact signed-residue witness that a post-boundary local order update is necessary.

## Independent exact validation

`VERIFY_ORDER_WINDOW.py` imports the previous exact `direct_risk` reference, evaluates the strengthened cluster formula with no `n*eta<1/q` restriction, and checks 8,840 direct Fraction comparisons across small q, signs, mixed m. Among them, 3,092 satisfy `n*eta>=1/q` while retaining `G_r>0`; 4,242 include nonzero correction. The S23 tests verify every n=128,...,225 independently at both strict rational theta endpoints, plus the exact n=226 counterexample. Actual stdout is in `RUN_ORDER_WINDOW.txt`.

The theorem is proved for every stated real parameter and all integer n in the positive-gap regime; computations are finite witnesses. It remains an author-side auxiliary observer result pending independent review.

## Next unit

Construct the exact two-cluster local transposition at n=226 and check that updated maximizer assignments reproduce the n=226 slope without rerunning an all-phase sort; then seek a piecewise O(q) continuation across multiple cluster exchanges, with residual labels intact.