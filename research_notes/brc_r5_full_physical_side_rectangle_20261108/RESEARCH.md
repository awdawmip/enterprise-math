# R5: full physical side-flow rectangle has exact seedless Blackwell lift

Date: 2026-11-08 (Asia/Shanghai). Frozen science GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`, unchanged; four-stage seven-likelihood-key P/Q-BRC model. P000 and ACTIVE worldview unchanged. Direct predecessor: `cb5fd08f777c9e4cd1ea11afbd2acbbe45bf654e` (partial rectangle). Author-side proof, exact Fraction certificate; independent review and formal native admission pending.

## Theorem: complete physical side-flow range for a fixed source face

For **every real** `0<=u<=53/160`, `0<=w<=33/160`, `0<=t<=1`, consider the legal FULL_HIST source flow
`x(u,w)=(1,1,1/2,u,9/80,w,0)`, and `x_t=(1-t)*x+t*y(u,w)`. There exists a **single legal seedless LR target** `y(u,w)` and calibrated nonnegative seven-key kernel which, **for every** real terminal declaration `d in [0,1]^7`, reproduces its two P/Q error probabilities and two P/Q stopping times exactly. The same target/kernel works for every declaration. The intervals of u and w are the **entire physical legal domain** for the chosen source `(g,a,b,v,z)=(1,1,1/2,9/80,0)`: `13a/40+b/80=53/160`, `3a/40+21b/80=33/160`. Thus the local two-side-flow variability question for this fixed source face is settled.

## Four exact corner certificates

Likelihood keys: `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`. Four source corners are `(u,w)=(0,0),(53/160,0),(0,33/160),(53/160,33/160)`. Coordinates below are `(g,a,b,u,v,w,z)`. For the corresponding seedless target corners take
```
y00=(89/93,89/93,85/186,0,1477/7440,0,89/930)
y10=(183601/186000,4543/4650,974/2325,1571/4960,4463/23250,0,4543/46500)
y01=(177799/186000,4357/4650,1151/2325,0,19073/93000,951/4960,4357/46500)
y11=(917/930,89/93,85/186,1571/4960,1477/7440,951/4960,89/930).
```
All four targets are legal, share the same **affine seedless face** `z=a/10, v-z=9b/40`, and agree with corresponding source corners on both stopping times:
```
T_P=1+g+3a/8+5b/8+u/2+v+3w/2
T_Q=1+g+(a+b)/2+u+v+w.
```
All four sources have historical residual `R=9bz-4a(v-z)=-9/20`; all four targets have `R=0`.

The exact executable `VERIFY.py` contains four sparse **nonnegative rational 7x7 Q-mass matrices**, respectively with 14,13,13,9 nonzero entries. Rows i are target likelihood keys, columns j source likelihood keys. All exact entries are included. If `M` is the seven-key affine Q stopping-mass function copied from the frozen model in `VERIFY.py:masses`, then each corner matrix `Q_c` satisfies the complete 21 equations
```
sum_j Qc[i,j]            = M_i(yc)       for each i,
sum_i Qc[i,j]            = M_j(xc)       for each j,
sum_i r_i*Qc[i,j]        = r_j*M_j(xc)   for each j.
```
The checker verifies legal flows, normalized P/Q masses, stopping-time equality, the seedless face and all the exact identities using `fractions.Fraction`.

## All-real proof by bilinear interpolation

For any real u,w in the **entire** rectangle set `p=u/(53/160)`, `q=w/(33/160)`; define nonnegative weights `h=((1-p)(1-q),p(1-q),(1-p)q,pq)`, summing to one. Set `y(u,w)=sum_c h_c*y_c` and `Q(u,w)=sum_c h_c*Q_c`. The target remains on the same seedless face because `z=a/10` and `v-z=9b/40` are affine constraints; it remains legal since all flow legality inequalities are affine. Source `x(u,w)` is affine in u,w. Q-mass functions and stopping times are affine in the flow, so the 21 Q/P calibration identities and two stop-time equalities at all corners extend to all real u,w by bilinear interpolation. `Q(u,w)` remains nonnegative.

For arbitrary `0<=t<=1`, let `Q_t=(1-t)*Q(u,w)+t*diag(M(y(u,w)))`. Its rows are `M(y)`; its Q columns and r-weighted P columns are exactly the masses of `x_t=(1-t)*x+t*y`. The source `x_t` is legal by convexity and has the same stopping times as y. For any real declaration `d in [0,1]^7`, put `k_i=(sum_j Q_t[i,j]*d_j)/M_i(y)` when row mass is positive and `k_i=0` otherwise. Each k_i belongs to [0,1]; the two column equations show equal Q and P terminal declaration probabilities, hence equal P/Q errors. This proves the theorem for **all real p,q,t,d**, including irrational inputs and every boundary point. Finite tests are only implementation regressions.

## Verification and next

Numerical LP was used solely to discover feasible corner supports; each resulting kernel was solved exactly over rationals and then validated with the standalone Python standard-library Fraction checker. Actual local run passed all four 7x7 corner certificates and 125 rational (p,q,t) test triples, including declaration conservation, as captured in `EXACT_OUTPUT.txt`. No floating-point arithmetic is used in released checking. No native-heartbeat π/trigonometric computation or physical residual attribution is asserted.

Previous certified regions `u<=503/1600,w<=32383/175840` and `u<=1571/4960,w<=951/4960` are now extended to the **entire legal physical source rectangle**. The crucial move is to vary the seedless target flows across a *common affine face*, not force the target side flows to equal the source side flows. This supplies a reusable general local lemma: an affine family of source flows over a finite parameter polytope has an all-real Blackwell lift if each vertex has a nonnegative calibrated transport into targets on a common affine seedless face and the affine interpolation preserves legality and stopping times.

Next: vary source a,b or v,z around this fixed source face, construct exact calibrated corner certificates (or a scoped dual obstruction), and continue the global four-observer FULL_HIST vs seedless LR **pointwise** equality/separation mother question. Mathematical status: `AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY`.
