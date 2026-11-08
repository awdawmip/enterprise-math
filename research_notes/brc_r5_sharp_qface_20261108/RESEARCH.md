# R5 — sharp q-capacity threshold on the fixed C_(3/4) Blackwell face

**Date:** 2026-11-08. **Status:** AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

**Provenance:** Continue the frozen seven-likelihood-ratio P/Q-BRC observer and R5 PR #1802 at `75bd2dd4b317f5bbd80e8678ca717e937ab01e64`. Scientific pins remain Global `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. Applicable norms read independently at canonical current main. The result concerns exactly the four statistical observers `(eP,eQ,TP,TQ)`; it is neither native Heartbeat X6 dynamics nor preservation of unspecified future branch observers.

## Exact statement

Let a lawful FULL_HIST source be the boundary slice
`x(q)=(1,0,1,0,9/160,21q/80,0)`, with `0<=q<=1`. In the original parameterization this is `t=0,p=0,kappa=1/4` (theta is immaterial). Fix the seedless target chart

`C_(3/4)={z'=3a'/40, v'-z'=27b'/160}`.

Write `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`. The seven Q-terminal masses `M(f)`, and `TP(f),TQ(f)`, are exactly the affine functions in `VERIFY.py`, unchanged from R5 PR #1802. A Blackwell lift is a lawful `y` on the chart and nonnegative `7x7` matrix `Q` satisfying, for all `i,j`,

`sum_j Q[i,j]=M_i(y)`, `sum_i Q[i,j]=M_j(x)`, `sum_i r_i Q[i,j]=r_j M_j(x)`,

and `TP(y)=TP(x)`, `TQ(y)=TQ(x)`. Such a declaration-independent kernel preserves both terminal declaration errors and both stopping times.

**Sharp face theorem:**

```text
There is such a lift on C_(3/4) for x(q)  iff  0 <= q <= 1343/1589.
```

The `iff` is **only for the declared fixed chart and this source slice**. In particular `x(1)` itself is legal and seedless; the failure of `C_(3/4)` beyond the threshold says nothing about the global seedless LR reachable set. The source lies in chart `C_(1/4)` for every `q`, which supplies the identity kernel globally.

## Upper bound: exact separation by stopping and target capacities

Write a chart target as `y=(g,a,b,u,z+27b/160,w,z)` with `z=3a/40`. Since the target is lawful, put

`m4=(g-b)/2 >= 0`, `m5=3a/40+21b/80-w >= 0`,

with `a,u >=0`. Direct substitution into the two stopping-time equations gives

`TP(y)-1 = (350/160)b+(9/16)a+u/2+2*m4-(3/2)*m5`,

`TQ(y)-1 = (309/160)b+(13/20)a+u+2*m4-m5`.

Eliminate `b` to obtain the **exact universal fixed-face inequality**

```text
350*(TQ(y)-1) - 309*(TP(y)-1)
 = (859/16)*a + (391/2)*u + 82*m4 + (227/2)*m5 >= 0.
```

For the source, `TP(x(q))-1=(269+63q)/160` and `TQ(x(q))-1=(249+42q)/160`; hence

`350*(TQ(x)-1)-309*(TP(x)-1)=(4029-4767*q)/160`.

If the source and target stopping times agree, the above inequality forces `q<=4029/4767=1343/1589`. This uses no numerical optimizer or kernel-support assumption.

## Attainment, all-real interpolation, exact witness

At `q*=1343/1589`, choose

`(g',a',b',u',w')=(209/227,0,209/227,0,4389/18160)`.

Here `g'=b'` and `w'=21b'/80`. The full target is

`y*=(209/227,0,209/227,0,5643/36320,4389/18160,0)`.

The exact 13-edge `Q*` is given in `VERIFY.py`, along with a separately reconstructed 12-edge `Q0` for `q=0` and its lawful fixed-face target. The accompanying independent Fraction checker verifies every row mass, every source column mass, all seven likelihood-ratio-weighted columns, P/Q normalization, physical bounds, the seedless equation, and both stop-time equalities at both endpoints.

For any **real** `q in [0,q*]`, let `lambda=q/q*`; define `y(q)=(1-lambda)y0+lambda*y*` and `Q(q)=(1-lambda)Q0+lambda*Q*`. The source `x(q)` is affine in `q`; the target's fixed chart and all lawful capacity constraints are affine, and all transport and stop-time equalities are linear. Nonnegative convex interpolation therefore proves existence for every real `q`, not merely the exact rational grid. The source–target mixture also preserves the four observer quantities by `(1-h)Q+h*diag(M(y))` for real `0<=h<=1`.

The independent `VERIFY.py` executes the two exact endpoint checks and 1001 additional Fraction regression cases, with stdout in `EXACT_OUTPUT.txt`. The exhaustive mathematical inference is the symbolic separating identity plus linear interpolation, **not** finite tests.

## Interpretation and next actionable question

The earlier five-parameter box stopped at `q=3/4`; at this specific boundary slice, the same common chart can be extended **sharply** to `q=1343/1589` (about 0.845186). The old claim that `q=1` fails on `C_(3/4)` is refined by an exact threshold and exact equality witness. Meanwhile `C_(1/4)` contains `x(q)` itself for `t=0`, so the chart obstruction is not global impossibility. Continue at `t>0, q=1` with an alternative chart and a common-face/multichart interpolation that respects full source parameter dependence.

**Authority:** GitHub author-side research note only; no active CLAIM, Result, Review, Working Truth, Foundation, or independent mathematical admission implied.
