# R5 — Complete target-capacity side rectangle by a redesigned Blackwell kernel

Date: 2026-11-08 Asia/Shanghai. Status: author-proved all-real statement, exact rational local verification, unreviewed; not mathematically admitted. Frozen science pins unchanged: global `a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Direct source predecessor: commit `935e1ca8111ed76b7cccbf4d928978da2eb9a5ba`, `research_notes/brc_r5_positive_residual_two_edge_20261108/SIDE_RECTANGLE.md` and `VERIFY_SIDE.py`.

## Exact model, observers, question

Use the frozen four-stage P/Q-BRC model with seven likelihood keys `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`. A legal flow `q=(g,a,b,u,v,w,z)` has `0<=a,b<=g<=1`; `0<=u<=13a/40+b/80`; `0<=w<=3a/40+21b/80`; `0<=z<=a/10`; `0<=v-z<=9b/40`. Seedless LR imposes `R(q)=9bz-4a(v-z)=0`. Exact seven-key stopping masses `M(q)` and stopping times are reproduced in `VERIFY.py`. For terminal declaration `d∈[0,1]^7`, `e_Q=sum M_i d_i` and `1-e_P=sum r_i M_i d_i`. The declared future operations are all randomized terminal declarations and the four observations `(e_P,e_Q,T_P,T_Q)`. Preserve the seven-key branch carrier; the stochastic kernel below certifies sufficiency only for that scope.

The predecessor lifted `0<=u<=503/1600` and `0<=w<=32383/175840` with a particular Q0. The next problem was whether `w` could increase by reallocating its mass without changing the seedless target.

## Theorem: entire physical rectangle of the fixed target family

For **every real** `0<=u<=503/1600`, `0<=w<=303/1600` and `0<=t<=1`, put

```
x(u,w)   = (1,1,1/2,u,9/80,w,0)
y(u,w)   = (39/40,19/20,9/20,u,3/16,w,57/628)
x_t(u,w) = (1-t)x(u,w)+t*y(u,w).
```

Then `x_t` is a legal FULL_HIST flow, `y` is legal seedless LR, and one stochastic seven-key Blackwell map (depending on `u,w,t` but not `d`) reproduces **all four** observations of `(x_t,d)` from `(y,Kd)` for **every real** `d∈[0,1]^7`. Their two common stopping times are `T_P=14/5+u/2+3w/2` and `T_Q=229/80+u+w`. `R(x)=-9/20`, `R(y)=0`. The earlier proof that the `t=0` source family is outside `conv(C∪F∪H_slack)` remains applicable.

## Exact rational transport certificate and all-real proof

Let rows of `Q0` be indexed by the target `y(0,0)` keys and columns by `x(0,0)`. Its seven rows are

```
[67/1440, 3/320, 0, 9167/2260800, 0, 3/800, 0]
[0, 503/1600, 0, 0, 0, 0, 0]
[0, 0, 0, 1/80, 0, 0, 0]
[0, 3/400, 0, 856759/11304000, 119171/11304000, 0, 0]
[0, 0, 0, 17017/628000, 147833/628000, 0, 0]
[0, 0, 0, 0, 0, 303/1600, 0]
[0, 0, 0, 0, 9167/2260800, 21/1600, 67/1440]
```

These 15 exact nonzero entries satisfy `Q0>=0`, `sum_j Q0[i,j]=M_i(y(0,0))`, `sum_i Q0[i,j]=M_j(x(0,0))`, and `sum_i r_i Q0[i,j]=r_j M_j(x(0,0))` for all seven keys. In particular, **both limiting diagonal capacities are saturated**: `Q0[1,1]=503/1600`, `Q0[5,5]=303/1600`.

The source and target mass vectors have the **same** affine side-flow increment

```
D(u,w) = (509u/900+w/100, -u, 0, 191(u+w)/450, 0, -w,
          u/100+509w/900).
```

Define `Q(u,w)=Q0+diag(D(u,w))`, and `Q_t=(1-t)Q(u,w)+t*diag(M(y(u,w)))`. All off-diagonal coefficients are those of nonnegative `Q0`. The only negative diagonal increments are `-u` in position 1 and `-w` in position 5. Their starting diagonal amounts are exactly the theorem's two upper bounds; every other diagonal increment is nonnegative. Thus **every entry of Q and Q_t is nonnegative for all real parameters throughout the box**, including irrational values and all boundaries.

Adding `diag(D)` changes the target row mass and source column mass by exactly `D`, and the likelihood-weighted column by `r_j D_j`; hence the full seven row/column/calibration identities persist. Affine interpolation preserves them for `x_t`. On each positive-mass target row set `K[i,j]=Q_t[i,j]/M_i(y)`; on a zero-mass row choose any stochastic distribution. It is a stochastic map independent of `d`, so `Kd∈[0,1]^7`, `sum M_i(y)(Kd)_i=sum M_j(x_t)d_j`, and `sum r_i M_i(y)(Kd)_i=sum r_j M_j(x_t)d_j`. Combined with identical stopping times, this proves exact pointwise four-observer equivalence for the full real box.

The bounds `u<=503/1600`, `w<=303/1600` coincide with **the physical legality limits of this fixed seedless target with u,w unchanged**. This rectangle is maximal for this target formula, while other seedless targets may reach outside it.

## Quantified gain, exact corner and verification

The old limit `32383/175840` increases to `303/1600` by **`9167/1758400` (approximately 2.83%)**. All `u` are now permitted up to their target physical limit simultaneously with that stronger `w` bound. The upper-right corner is

```
x=(1,1,1/2,503/1600,9/80,303/1600,0)
y=(39/40,19/20,9/20,503/1600,3/16,303/1600,57/628)
(T_P,T_Q)=(2593/800,2693/800).
```

Standalone `VERIFY.py` is the standard-library Fraction checker actually executed for this source publication. It checks full exact 7x7 transport, positivity, legal capacities, seedless residual, exact stop times, both mass normalizations, all weighted-column identities, and declared errors on a 5×5×5 rational parameter grid (125 triples). `EXACT_OUTPUT.txt` is actual captured stdout from this checker. The universal real claim is supplied by the algebraic proof above, not by finite samples.

BRC reuse: exact positive seven-key branch-mass carrier, signed history residual and all-branch calibrated likelihood transport (`REUSE_APPLIED`). The P000/native X6 premises remain unchanged.

Next: vary `(g,a,b,v,z)` to lift sources whose `u` or `w` exceed these particular target capacities. Discriminating input is the legal source corner `(1,1,1/2,53/160,9/80,33/160,0)`; seek a rational seedless seven-key kernel or a precise face-specific dual. The full pointwise four-observer image equality mother question remains open.
