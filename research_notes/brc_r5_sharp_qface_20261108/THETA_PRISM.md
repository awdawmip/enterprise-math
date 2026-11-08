# R5 — four-parameter full q-capacity negative-residual Blackwell prism

**Date:** 2026-11-08. **Status:** AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

**Frozen science unchanged:** Global `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`; earlier PR #1802 source observer, present PR #1803 sharp face study. P000 and the protected ACTIVE worldview unchanged. All claims are within the frozen seven-node typed P/Q-BRC observer for the declared four outputs `(eP,eQ,TP,TQ)`, with no claim about native X6 operations or undisclosed future path observers.

## New exact theorem for all real parameters

For each **real**

```text
0 <= t <= 1/5;  0 <= p <= 1;  0 <= q <= 1;  0 <= theta <= 3/4
g=b=1; a=t; kappa=3/4,
```

consider the lawful FULL_HIST source

```text
x(t,p,q,theta) = (1,t,1,
                  (13t/40+1/80)*p,
                  t*theta/10+27/160,
                  (3t/40+21/80)*q,
                  t*theta/10).
```

There is a lawful seedless target `y` on a **single common chart**

`C_(3/4)={z'=3a'/40, v'-z'=27b'/160}`

and a nonnegative declaration-independent seven-by-seven Blackwell kernel `Q` such that its target-row Q masses, source-column Q masses, r-weighted source-column P masses (r=(1/10,1/2,3/4,1,5/4,3/2,19/10)) and P/Q expected stopping times are exactly preserved. The same holds for all real source-target interpolants `(1-h)x+h*y, 0<=h<=1`. Pulling any seven-node terminal decision vector through Q therefore gives equal terminal error probabilities and stopping times.

The source's signed history residual is `R=9t(theta-3/4)/10`. It is negative whenever `t>0,theta<3/4`, and zero on boundary. Thus the theorem covers a **full four-real-dimensional box**, with both physical side branches independently taking all legal capacities `p,q∈[0,1]`, including `q=1` (not reached by PR #1802's general five-dimensional box).

## The exact 16-vertex proof

The four separate coordinates are `(t,p,q,theta)`, vertices `t∈{0,1/5}`, `p,q∈{0,1}`, `theta∈{0,3/4}` (16 total).

At `t=0`, every source belongs to `C_(3/4)` and is seedless, so choose `y=x` and `Q=diag(M(x))`. At `theta=3/4`, for every t,p,q the source itself lies on `C_(3/4)` and is seedless, giving the same exact diagonal witness.

Thus the only four nontrivial corners occur at `t=1/5,theta=0,p,q∈{0,1}`. `VERIFY_THETA_PRISM.py` explicitly stores **four exact rational seedless targets** and **four nonnegative Blackwell kernels** with respectively 10,9,9,9 positive transfer entries (37 total). The independent Fraction-only checker tests full source-target lawfulness, both P/Q normalizations, all 7 row, 7 column, 7 weighted-column equations, seedless identity and 2 stopping-time equations.

For any real interior input put `s=5t` and `v=4theta/3`. The source is separately affine in t,p,q,theta (only products tp,tq,t*theta occur), so it equals the nonnegative 16-vertex multi-affine combination with weights

```text
W_e = (s if e_t else 1-s)*(p if e_p else 1-p)*
      (q if e_q else 1-q)*(v if e_theta else 1-v).
```

Set `y=sum_e W_e*y_e` and `Q=sum_e W_e*Q_e`. The common seedless chart is linear, physical capacities are affine, the seven-node terminal mass map and both stop-time maps are affine, and the Blackwell row/column/weighted equations are linear. Thus every lawful and calibrated endpoint equality and inequality passes unchanged through nonnegative convex mixing. This is a proof for **all real numbers including irrational points**, not an inference from a numerical grid. For an `h` source-target mixture use `(1-h)Q+h*diag(M(y))`.

Executed `python3 VERIFY_THETA_PRISM.py` gave 16 exact corner passes and 601 exact rational interior regressions. Complete executable and captured stdout are preserved beside this proof.

## Boundaries, relevance, and follow-up

The theorem fixes `kappa=3/4`, and permits `theta≤3/4`; its residual has one sign. It combines with preceding positive-residual R5 results but does **not** declare the mixed-sign, whole cube `theta,kappa∈[0,1]` solved. The separate fixed-face sharp obstruction for `kappa=1/4,t=0` is proved in `RESEARCH.md`; changing faces can overcome chart-specific no-gos. Next evaluate the `theta>3/4` and varying-`kappa` adjoining corners, searching additional charts or an exact scoped separating inequality.

Control status remains author evidence only. GitHub transport and complete remote readback establish durable provenance, not native Owner/CLAIM, Result/Review, independent admission, or Foundation.
