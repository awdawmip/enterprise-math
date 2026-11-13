# R5 — An explicit six-edge Blackwell lift for negative residual with stopping-time slack

**2026-11-07, author-side research.** Frozen science: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Predecessor `602624de161ba40682cab35776aa1188f387bada`, `research_notes/brc_r5_affine_face_join_20261107/`. This is the frozen four-stage seven-likelihood-key P/Q-BRC mathematical experiment with four observations `(e_P,e_Q,T_P,T_Q)`, not a claim about general physical X6 evolution.

## Model and theorem

Let `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`; let the legal real FULL_HIST flow be `x=(g,a,b,u,v,w,z)`, satisfying

~~~
0<=a,b<=g<=1
0<=u<=13*a/40+b/80
0<=w<=3*a/40+21*b/80
0<=z<=a/10
0<=v-z<=9*b/40.
~~~

The seven Q stopping masses `M_i(x)`, the stop times and declarations are the immutable predecessor formulas and are reproduced in `VERIFY.py`. Put `R=9*b*z-4*a*(v-z)`. A flow is seedless LR precisely when `R=0`. The terminal declarations `d in [0,1]^7` give `e_Q=sum_i M_i d_i` and `1-e_P=sum_i r_i M_i d_i`.

**Theorem (all real).** For every legal `x` with `b>0`, `R<=0` and

~~~
delta = -R/(9*b) >= 0,
g-delta >= max(a,b),
~~~

the flow `y=(g-delta,a,b,u,v+delta,w,z+delta)` is legal and seedless LR. It has exactly the same `T_P,T_Q` as `x`. A single explicit nonnegative seven-by-seven Q-mass Blackwell transport, independent of `d`, maps `y` to `x`: consequently, for **every** real `d in [0,1]^7`, one transformed stochastic declaration `Kd` reproduces all four observations. If `b=0`, legality forces `v=z`, so the original source is already seedless and uses the identity kernel.

## Exact proof and transport certificate

Since `0<=v-z<=9*b/40`, the shift obeys `0<=z+delta=4*a*(v-z)/(9*b)<=a/10`. The condition `g-delta>=max(a,b)` establishes all remaining legal inequalities; `u,w` and their capacity bounds are unchanged, as is `v-z`. The residual satisfies `R(y)=R+9*b*delta=0`. Both stop times are affine and contain `g+v` with equal coefficients, so both are preserved.

Substitution into the seven affine mass formulas gives the exact, source-independent identity

~~~
M(y)-M(x) = delta*(47/180, 0, -1/2, 43/90, -1/2, 0, 47/180).
~~~

Define the Q-mass transport `Q` by its diagonal and six off-diagonal entries (all remaining entries are zero):

~~~
Q[i,i] = M_i(x)    for i=0,1,3,5,6
Q[i,i] = M_i(y)    for i=2,4
Q[0,2]=delta/5;       Q[0,4]=11*delta/180
Q[3,2]=43*delta/180; Q[3,4]=43*delta/180
Q[6,2]=11*delta/180; Q[6,4]=delta/5.
~~~

All entries are nonnegative by legal stop masses. The row sums equal `M_i(y)`; the column sums equal `M_j(x)`. P-calibrated columns `2,4` follow from

~~~
(1/10)*(1/5)+(43/180)+(19/10)*(11/180)=(3/4)/2,
(1/10)*(11/180)+(43/180)+(19/10)*(1/5)=(5/4)/2.
~~~

Other P-columns are diagonal. Hence `sum_i r_i Q[i,j]=r_j M_j(x)` for every column. For each positive-mass row set `K[i,j]=Q[i,j]/M_i(y)`, using the identity row on zero-mass rows. Then `K` is row stochastic and, for every declaration `d`,

~~~
e_Q(y,Kd) = sum_j M_j(x)d_j = e_Q(x,d)
1-e_P(y,Kd) = sum_j r_j*M_j(x)*d_j = 1-e_P(x,d).
~~~

Both stopping times also agree. This completes the proof for the entire specified real domain, including irrational coefficients and boundary points.

## Saturated-v corollary and strict enlargement of the earlier convex join

Define the convex saturated-v slack polytope

~~~
H_slack={legal real x : v-z=9*b/40,
         g+z>=max(a,b)+a/10}.
~~~

For `x in H_slack` choose `delta=a/10-z`. The same displayed transport applies, and the target lies in the single affine seedless face `F={legal y: z_y=a_y/10, v_y-z_y=9*b_y/40}`. Both the target map and `Q` are **affine** in `x` on `H_slack`. The predecessor's exact cone-to-F lifts and identity lifts on F can therefore be combined by nonnegative convex interpolation with the new lift. **Every flow in `conv(C union F union H_slack)` has a single seedless LR lift in F and a calibrated kernel preserving all four observations for all declarations.** This is a strict extension of the predecessor's `conv(C union F)` theorem.

A fully legal exact witness, with both side-flow capacities attained, is

~~~
x=(1,3/4,1/2,1/4,9/80,3/16,0)
y=(37/40,3/4,1/2,1/4,3/16,3/16,3/40)
delta=3/40, R(x)=-27/80, R(y)=0,
(T_P,T_Q)=(249/80,127/40) on each side.
~~~

The source lies outside `conv(C union F)`: in that older join, `z=0` forces any F constituent to have `a=0`, while every C constituent has `a=b`; therefore `a<=b` throughout its zero-z slice. The witness has `z=0,a=3/4>b=1/2`. The new polytope covers genuinely new nonzero `u,w` histories.

## Verification and status

`VERIFY.py` runs standard-library Python `Fraction` checks of exact coefficient identities, four maximal-side-flow rectangle corners, and 540 further rational samples with varying unsaturated `v-z`, residual, side flows and endpoints. Every sample checks legality, seedlessness, both times, normalization, both likelihood moments, all seven row, Q-column and P-column constraints, and three declaration vectors. The all-real theorem relies on the displayed exact algebra, not finite sampling. The captured local output is in `EXACT_OUTPUT.txt`; the standalone local checker also exists as the complete companion script to this report.

**BRC interface**: positive rational branch masses, labels and residual remain explicit. The kernel is an exact compression for the *declared four-observer horizon*; hidden joint histories or arbitrary future operations remain separate typed objects.

**Next**: test the low-slack negative-residual region `g-max(a,b)<-R/(9b)`, then positive residual `R>0`, using other affine seedless faces or exact four-dimensional infeasibility witnesses. The full R5 pointwise image-equivalence mother problem and independent review/admission remain open. Native control status/task queries at 2026-11-07T15:38Z returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE`, `operation_sent=false`; no active owner or formal CLAIM was established.
