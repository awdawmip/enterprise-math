# R5 — Exact pointwise seedless lifting of the nonnegative-history-residual half-space

Date: 2026-11-07 (Asia/Shanghai). Research mode: TASK_RESEARCH; author-side portable evidence only. Frozen scientific pins remain GLOBAL `a01383f825ef9d43b4b754254303298c64041568` and EM `86149263e38c22292c9def1e0f69092efa1be77e`. Predecessor: `research_notes/brc_r5_four_observer_convex_hull_20261107/RESEARCH.md` at `f20b9a0bdc8c1fc8f69a2abeb7c231181d1a0d27` (equality of *convex hulls* only).

## New all-real constructive theorem

In the frozen four-stage, seven-likelihood-key P/Q-BRC observer, **every valid FULL_HIST policy with history residual `R=9*b*z-4*a*(v-z)>=0` has one valid seedless LR policy with exactly the same `W=(e_P,e_Q,T_P,T_Q)`, for any seven declarations in [0,1]**. The output is one seedless policy, not an external randomized mixture of seedless policies. Strict R>0 gives genuinely history-dependent source flows that still admit this lift.

## Frozen model and observers

A FULL_HIST flow is `x=(g,a,b,u,v,w,z)`, where `0<=a,b<=g<=1`, `0<=u<=c0=13*a/40+b/80`, `0<=w<=c2=3*a/40+21*b/80`, `0<=z<=a/10`, `0<=v-z<=9*b/40`. The seven LR keys are `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`. Stopping Q masses `M_j(x)` are the frozen rational affine expressions in `VERIFY.py` (identical to the prior paper). For declarations `d_j in [0,1]`, `e_Q=sum_j M_j*d_j`, `e_P=1-sum_j r_j*M_j*d_j`, and

`T_P=1+g+3*a/8+5*b/8+u/2+v+3*w/2`;

`T_Q=1+g+(a+b)/2+u+v+w`.

Seedless LR adds the equality `9*b*z=4*a*(v-z)`.

## Exact construction and proof

Write `A=a/10`, `B=9*b/40`, `c1=A+B=(4*a+9*b)/40`. Valid FULL_HIST implies `0<=v=z+(v-z)<=c1`. If `c1>0`, put `theta=v/c1`, `z_*=theta*A=4*a*v/(4*a+9*b)`, and `x_*=(g,a,b,u,v,w,z_*)`. If `c1=0`, then `a=b=v=z=0` and take `z_*=0`.

Since `0<=theta<=1`, `0<=z_*<=a/10`, `v-z_*=theta*9*b/40`, and `9*b*z_*=4*a*(v-z_*)`. Thus `x_*` is legal seedless LR. The two stopping-time formulas depend on v but not z, so they are unchanged. For positive c1,

`z-z_*=(9*b*z-4*a*(v-z))/(4*a+9*b)=R/(4*a+9*b)`.

If R>=0 let `delta=(247/1620)*(z-z_*)>=0`. Direct symbolic subtraction of the frozen affine stopping masses gives exactly

`M_0(x_*)=M_0(x)+delta`, `M_6(x_*)=M_6(x)+delta`, `M_3(x_*)=M_3(x)-2*delta`,

and `M_j(x_*)=M_j(x)` for j=1,2,4,5. The exact derivatives are `47/180-67/162=-247/1620` for each extreme and `43/90-14/81=247/810` at LR=1. The gain of symmetric LR tail masses from the middle is a mean-preserving spread: `r_0+r_6=1/10+19/10=2*r_3`.

For any original declarations d, preserve all d_j except at j=0,6. Define

`d_*j=(M_j(x)*d_j+delta*d_3)/(M_j(x)+delta)` for j=0,6 if the denominator is positive, and choose any number in [0,1] otherwise. Each new declaration belongs to [0,1] as a convex combination of d_j and d_3. Using the three mass identities, `sum_j M_j(x_*)*d_*j=sum_j M_j(x)*d_j`. The P-weighted equality also holds since `r_0*delta+r_6*delta=2*r_3*delta`. Therefore `e_Q,e_P,T_P,T_Q` all match exactly for every real input including boundaries. The theorem is algebraic; no finite sample is used to infer universal validity.

For A,B>0, `z=theta_A*A`, `v-z=theta_B*B` and R>=0 precisely when `theta_A>=theta_B`. This covers an entire ordered half of the independent-history square for every valid base flow and declaration. It uses BRC branch-mass provenance and the actual P/Q readout, rather than only a total-mass quotient.

## A nontrivial exact witness

At `x=(1,1,1,0,1/10,0,1/10)`, R=9/10>0, times both 31/10. With `d_0=d_6=1` and other d_j=0, the exact point is `W=(853/900,47/900,31/10,31/10)`. The seedless flow `x_*=(1,1,1,0,1/10,0,2/65)` has `delta=19/1800` and achieves W by `d_*0=d_*6=47/66` (other d_j zero). Thus strict history dependence alone does not separate four-observer images.

## Reverse-sector partial lifting and its boundary

For R<0, the same time-preserving seedless flow loses D>0 from each tail and gains 2D at the center, where `D=(247/1620)*(z_*-z)`. Keeping d_1,d_2,d_3,d_4,d_5 fixed, if the two denominators are positive then

`d_*j=(M_j(x)*d_j-D*d_3)/(M_j(x)-D)` for j=0,6

gives exact errors *provided* both values are in [0,1]. The necessary and sufficient conditions for this particular transfer are `D*d_3 <= M_j(x)*d_j <= M_j(x)-D+D*d_3` for each j=0,6. If a denominator is zero the associated numerator must vanish and its new declaration is free. Constant declarations on the three affected keys always lift. Failure of this **fixed-flow** transfer does not establish global nonconvex separation, because other seedless flows with matching times might work.

## Execution, scope, next

`VERIFY.py` and captured `EXACT_OUTPUT.txt` provide standard-library `Fraction` verification of affine coefficients, P/Q normalization, the strict example, all 128 binary declarations at that example, 405 rational legal flow/label checks including boundary cases, and reverse-sector constant declarations. All-real scope rests on the symbolic proof above.

The theorem concerns the frozen seven-key four-stage observer, not native X6 physics, not FULL_HIST/seedless *global* pointwise equality, and not independent review or canonical admission. Native active owner/CLAIM cannot be asserted while the authenticated EM service returns `BACKEND_IDENTITY_OR_VERSION_MISMATCH` with `operation_sent=false`.

**Next discriminating unit:** use the reverse corner `(g,a,b,u,v,w,z)=(1,1,1,0,9/40,0,0)`, R=-9/10, times both 129/40. For exact rational declarations, test *global* seedless feasibility jointly over all legal flows, two times, two errors and the bilinear seedless equation. A rational lift or rigorous global polynomial-infeasibility certificate provides a meaningful outcome; floating failure is not proof. Alternatively construct a time-preserving change of early flows that Blackwell-dominates the reverse corner. See `NEXT_UNIT.md`.