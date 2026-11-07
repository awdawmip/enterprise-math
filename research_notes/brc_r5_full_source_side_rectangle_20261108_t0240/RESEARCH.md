# R5 — Exact Blackwell lifting over the entire physical source side-flow rectangle

Date: 2026-11-08 Asia/Shanghai. Status: author-proved and exact-Fraction-checked; independent review and native Source admission pending. Scientific inputs held at frozen global pin `a01383f825ef9d43b4b754254303298c64041568` and Enterprise Math pin `86149263e38c22292c9def1e0f69092efa1be77e`. Immediate predecessor: `89fafa8bd1efc4ad543bc81f8d7da9d019989eef:research_notes/brc_r5_full_target_capacity_rectangle_20261108/`. This result is a stricter extension, not a change of P000 or of the task's scientific model.

## Exact problem and observer

Keep the frozen four-stage seven-key P/Q-BRC likelihood carrier `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`. The flow is `q=(g,a,b,u,v,w,z)`, with `0<=a,b<=g<=1`, `0<=u<=13a/40+b/80`, `0<=w<=3a/40+21b/80`, `0<=z<=a/10`, and `0<=v-z<=9b/40`. Seedless LR iff `R(q)=9bz-4a(v-z)=0`. The seven stopping masses `M_j(q)` and times `T_P,T_Q` are exactly as in the predecessor's `VERIFY.py` and repeated in the new `VERIFY.py` here. Terminal declaration `d in [0,1]^7` gives `e_Q=sum_j M_j(q)d_j` and `1-e_P=sum_j r_j M_j(q)d_j`. All results are for these four observables and randomized terminal declarations, retaining the full seven-key carrier.

## Theorem — complete source capacity rectangle

For every real `0<=u<=U=53/160`, `0<=w<=W=33/160`, define the **legal FULL_HIST source**
`x(u,w)=(1,1,1/2,u,9/80,w,0)`. This is the **entire physical side-flow rectangle of this source family** and has `R(x)=-9/20`. For **all** these real `u,w` and **every** `d in [0,1]^7` there exists a single legal seedless LR target `y(u,w)` and a stochastic declaration transformer independent of `d` that reproduces exactly `(e_P,e_Q,T_P,T_Q)`.

Indeed the same target lifts **all** `x_h=(1-h)x+h*y`, `0<=h<=1`, for all real `u,w,h`. The common times of source, target, and interpolation are
`T_P=14/5+u/2+3w/2`, `T_Q=229/80+u+w`.
This solves the predecessor's nominated full-capacity corner `(u,w)=(53/160,33/160)` and goes further to the full rectangular family.

## Four certified corner targets

Index corners by `(i,j)` corresponding to source `(u,w)=(iU,jW)`. The full seven-dimensional seedless targets are:

| corner | g | a | b | u' | v' | w' | z' |
|---|---|---|---|---|---|---|---|
| 00 | 11/12 | 11/12 | 1/2 | 13/480 | 49/240 | 1/160 | 11/120 |
| 10 | 1 | 1 | 7/20 | 507/1600 | 143/800 | 37/1600 | 1/10 |
| 01 | 5/6 | 5/6 | 2/3 | 31/480 | 7/30 | 3/16 | 1/12 |
| 11 | 19/20 | 19/20 | 11/20 | 101/320 | 7/32 | 53/320 | 19/200 |

All four belong to the **same affine seedless face**:
`g=a, z=a/10, v-z=9b/40`, hence `R=9b(a/10)-4a(9b/40)=0`. Each target satisfies all physical inequalities and both source stopping-time equalities exactly. For each corner, the attached checker contains an explicit sparse, nonnegative, rational `7x7` matrix `Q_ij` (9–13 positive edges) with target rows and historical-source columns satisfying
`sum_k Q_ij[l,k]=M_l(y_ij)`,
`sum_l Q_ij[l,k]=M_k(x_ij)`,
`sum_l r_l Q_ij[l,k]=r_k M_k(x_ij)`
for all seven indices. These are **exact rational identities** checked by integer arithmetic, not floating-point fitting. The source's two probability measures are normalized in every corner. In particular the upper-right certificate targets
`y_11=(19/20,19/20,11/20,101/320,7/32,53/320,19/200)`
at exact stopping times `(131/40,17/5)`.

## All-real argument (bilinear transport)

Let `s=u/U`, `t=w/W` in `[0,1]` and set
`b_00=(1-s)(1-t)`, `b_10=s(1-t)`, `b_01=(1-s)t`, `b_11=st`.
Define `y(u,w)=sum_ij b_ij y_ij`, `Q(u,w)=sum_ij b_ij Q_ij`. The source is affine in `u,w`, so `x(u,w)=sum_ij b_ij x_ij` identically. Legal flow constraints, stopping masses, and both times are affine in the flow. The four targets' common face `g=a, z=a/10, v-z=9b/40` is affine and seedless; consequently their convex combination is **exactly seedless for every real s,t**, despite the general seedless quadratic condition. Matrix nonnegativity and all 21 row/column/calibration identities persist by nonnegative interpolation. Stopping times match by linearity.

Set `Q_h=(1-h)Q(u,w)+h*diag(M(y(u,w)))`. It is nonnegative; its target rows are `M(y)`, and its calibrated columns are `M(x_h)` and `r*M(x_h)`. For each positive row `M_i(y)` let `K_ij=Q_h[i,j]/M_i(y)`; zero rows may use arbitrary stochastic rows. For every real `d in [0,1]^7`, `Kd` is a legitimate randomized terminal declaration and exactly preserves both P/Q error readouts, while both times are preserved. Thus the entire stated **three-real-parameter** `(u,w,h)` family lifts pointwise.

This analytic argument covers irrational parameters and every boundary point. It uses the BRC positive exact branch-mass carrier and the history-residual distinction; its observer sufficiency applies to randomized terminal declarations and the four stated observations, not to unlisted future branch operations or native X6 dynamics.

## Verification and discovery notes

`VERIFY.py` uses standard-library `fractions.Fraction` to check 4 exact source/target corner legality and residuals; 7 target row identities, 7 source column identities, 7 likelihood-weighted column identities per corner; zero/one normalization; the common affine seedless face; and 125 exact samples across `u/U,w/W,h` plus three declarations. The continuous theorem follows from the displayed affine/bilinear proof, while the checker supplies reproducible precise corner certificates and regression evidence. The executed output is in `EXACT_OUTPUT.txt`.

Construction route: start from the exact full source corner and solve a *linear* calibrated transport feasibility problem restricted to the seedless affine face, rather than optimize the original quadratic seedless equation. The four rational feasible vertices and their calibrated transports are the reusable certificate. This replaces the predecessor's single fixed-target capacity barrier with a common affine seedless face and convex combinations.

## Open question

This completes the full `(u,w)` capacity rectangle **for the fixed source family `g=a=1,b=1/2,v=9/80,z=0`**. Next vary `(g,a,b,v,z)` outside this source family (especially other negative-residual and low-slack faces), seek other common seedless affine faces and exact calibrated transports, or a scoped nonconvex separating witness. Full FULL_HIST vs seedless LR four-observer pointwise image equality remains the R5 mother problem; independent mathematical review and native acceptance are not claimed.

GitHub researcher identity: authenticated `awdawmip`. Native owner/CLAIM query returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE; operation_sent=false`; Site gateway reported `research_authority_granted=false`. Material is author-side portable evidence.
