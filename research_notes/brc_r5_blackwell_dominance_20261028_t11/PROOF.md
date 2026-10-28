# R5: constructive Blackwell-dominating likelihood-ratio compression

Date: 2026-10-28. **AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED**. External finite two-measure sequential-observation model; no native-X6 physical conclusion. Fixed knowledge read: `awdawmip/chatgpt-global-knowledge main@60f1ae4c8b389a7aadbe19be6827163b39b70dcc`; fixed project startup: `main@a7a5e8abcc42f90b435eec193c55a8b3067a359c`. Source predecessor (signed support gate): `research_notes/brc_r5_two_upstream_signed_phase_transition_20261028_t11/PROOF.md` at `ba9ef097c127d683bbecc0de2f45826457984a24`.

## Scope and theorem

Let `0<theta<1`, `0<b<a<1/2`, `0<d<1`. U and V are observed at time 1 with Q masses 1/2, likelihood ratios `1+q,1-q`, where `q=(1-theta)d`. Either can stop or continue. At time 2, C edges both have cumulative LR=1, Q conditional probability theta, and may stop or take a third observation; O edges have ratios `1+d,1-d`, respective Q probability `1-theta`, and must stop. After U.C the three time-3 ratio values `(1/2,1,3/2)` have Q probabilities `(a,1-2a,a)`; after V.C they have `(b,1-2b,b)`. All P,Q leaf masses are positive and normalized. Full policies know U/V history; seedless LR policies use a *common* action at collided time-2 C signature. Both allow all real local randomizations.

Write `I_full,I_LR` for **actual** images of `(e_P,e_Q,T_P,T_Q)` with `e_P=P[declare Q]`, `e_Q=Q[declare P]`, `T_m=E_m tau`. Put
`H=(2+theta)*b-theta*a`, and, for `d<=1/2`,
`R=theta*(1-theta)*d/(1/2-(1-theta)*d)=2*theta*q/(1-2*q)`.

**Theorem:** When `0<d<=1/2` and `H>=R`, every full-history policy has a seedless LR policy with *exactly the same four observables*. More strongly, every full *stopping flow* has an explicitly constructible LR flow with the same two expected times and a Blackwell-more-informative terminal binary experiment. Together with the signed Bellman converse proved below:

`I_full=I_LR  iff  conv(I_full)=conv(I_LR)  iff  (0<d<=1/2 and H>=R)`

for the entire stated parameter family. At `theta=3/4,a=1/4,b=1/8`, `H=5/32` and the threshold is `d=10/29`. Hence **all** `0<d<=10/29`, including the previous `d=1/10` hull-equality candidate, have equal true images and cannot solve the mother problem.

## Proof I: full-history flow and preserved time coordinates

Let `x_U,x_V in [0,1]` denote the root continuation probabilities; let `z_U in [0,x_U]`, `z_V in [0,x_V]` be the unconditional probabilities of root continuation *and* taking the third observation. Define `S=x_U+x_V`, `D=x_U-x_V`, `L=z_U+z_V`, `Z=S+theta*L`, `A=a*z_U+b*z_V`.

Under Q the terminal likelihood-ratio masses are exactly:

- LR `1+q`: `(1-x_U)/2`; LR `1-q`: `(1-x_V)/2`.
- LR `1+d`: `(1-theta)*x_U/2`; LR `1-d`: `(1-theta)*x_V/2`.
- LR `1/2` and `3/2`: `theta*A/2` each.
- LR `1`, including C-stop and the third-stage center: `theta*(S-2*A)/2`.

At equal ratios masses are summed. Their Q-total and LR-weighted P-total are both 1. The exact expected times satisfy `T_Q=1+Z/2`, `T_P=1+(Z+q*D)/2`.

For any fixed stopping flow, randomized terminal declarations yield a planar zonotope: if `m_r` is Q mass at ratio r, choose `t_r in [0,1]` and obtain `e_P=sum_r r*m_r*t_r`, `e_Q=sum_r m_r*(1-t_r)`. Multiple hidden histories with the same r generate parallel segments and can be aggregated; the LR policy can realize every point of its own zonotope via local declarations by observed signature.

## Proof II: explicit spread-improving compression

Keep D and Z fixed and define
`S'=max(|D|,Z/(1+theta))`,
`x'_U=(S'+D)/2`, `x'_V=(S'-D)/2`,
`L'=(Z-S')/theta`, `y'=L'/S'` (or 0 if `S'=0`),
`z'_U=y'*x'_U`, `z'_V=y'*x'_V`,
`A'=a*z'_U+b*z'_V`, and `Delta=S-S'`.

Since `|D|<=S`, `L<=S`, `|D|<=Z` and `Z/(1+theta)<=S`, we have `0<=S'<=S`, `0<=x'_i<=1`, `0<=L'<=S'`: this is a legitimate single shared-C LR stopping flow. D and Z are unchanged, so both T_P,T_Q are unchanged.

**Sharp spread gain:** `A'-A >= H*Delta/(2*theta)` for every real stopping flow. Proof by cases:

1. If `S'=Z/(1+theta)`, then `y'=1`, `Delta=theta*(S-L)/(1+theta)`, and
   `A'-A=a*(x_U-z_U)+b*(x_V-z_V)-(a+b)*Delta/2 >= b*(S-L)-(a+b)*Delta/2=H*Delta/(2*theta)`.
2. If `S'=|D|` and `D<=0`, then `x'_U=0`, `L'=L+2*x_U/theta`, `Delta=2*x_U`, and
   `A'-A=2*b*x_U/theta-(a-b)*z_U>=H*Delta/(2*theta)`.
3. If `S'=|D|` and `D>=0`, then `x'_V=0`, `L'=L+2*x_V/theta`, `Delta=2*x_V`, and
   `A'-A=2*a*x_V/theta+(a-b)*z_V>=H*Delta/(2*theta)` because `2*a>H`.

The formulas cover equality/ties and zero flows by direct substitution or continuity.

## Proof III: exact signed ROC and Blackwell domination

For any signed real alpha,beta define `f(r)=min(alpha*r,beta)`, `D_f=2*f(1)-f(1/2)-f(3/2)>=0` and
`J_U=f(1+q)-theta*f(1)-(1-theta)*f(1+d)`,
`J_V=f(1-q)-theta*f(1)-(1-theta)*f(1-d)`.

For `d<=1/2` the sharp Jensen bound is `0<=J_U+J_V<=R*D_f`. Indeed, a nontrivial kink of f at `1 +/- s`, `0<s<min(d,1/2)`, with slope drop magnitude m gives
`J_U+J_V=m*min(theta*s,(1-theta)*(d-s))`, `D_f=m*(1/2-s)`. This quotient increases up to `s=q` and does not increase afterwards when `d<=1/2`; hence its maximum is exactly R. If the kink is elsewhere both Jensen gaps vanish.

For a terminal LR law mu let `F_mu(f)=sum_r m_r*f(r)`. Substitution of the complete mass table yields
`2*F_mu=f(1+q)+f(1-q)-x_U*J_U-x_V*J_V-theta*A*D_f`.
Thus the difference of compressed and full terminal scores obeys
`2*(F_new-F_old)=(Delta/2)*(J_U+J_V)-theta*(A'-A)*D_f <=(Delta/2)*(R-H)*D_f <=0`.

For each signed direction (alpha,beta), `F_mu(f)` is the **minimum** of alpha*e_P+beta*e_Q over the zonotope of terminal declarations. Consequently every signed supporting halfspace of the original zonotope also contains the new zonotope in the appropriate inclusion direction, and finite-dimensional convex separation gives `Z_full subseteq Z_new`. Every full terminal declaration point can therefore be reproduced by compressed local declarations, while both expected times agree. As every LR policy is a full policy, this proves equality of the genuine four-dimensional images, over *all real* local randomizations.

## Proof IV: converse for the full phase classification

For completeness take the signed time cost `c(r)=gamma*r+delta`, `C=c(1)`; retain the same f and D_f. At the C collision, U and V have opposite optimal actions when `b*D_f<C<a*D_f`. Both upstream root continuations are strictly preferred under those privately optimal actions iff
`J_U+theta*a*D_f-(1+theta)*C-gamma*q>0`, and `J_V-C+gamma*q>0`.
A real gamma meets both iff `(2+theta)*C<J_U+J_V+theta*a*D_f`, and some C in that interval meets it iff `J_U+J_V>H*D_f`. This produces a strict signed support gap between full and LR policies, even allowing all early stops; finite multiaffine objectives attain extrema at deterministic local actions. For `d<=1/2` the exact maximum Jensen ratio is R, so a gap exists iff H<R. For `d>1/2`, choose the kink approaching 1/2 from above: D_f tends to zero but J_U+J_V stays positive, yielding a gap for finite H. Equality of every signed support is equivalent to equality of convex hulls of these compact finite-policy images. Combining with the constructive implication finishes the iff theorem.

## Exact checks, provenance, limits and next problem

The attached `VERIFY.py` imports the predecessor's pinned `VERIFY.py` solely for tree/observer enumeration and otherwise uses standard-library `Fraction`: 225 exact stopping-flow cases at each d=1/10 and 10/29, exact convex-order stop-loss tests at every LR support breakpoint, and 20,736 full deterministic descriptions (380 distinct vectors) individually passing an exact LR zonotope membership check with the **single endpoint-lift S'**. This is regression evidence; universal scope comes from the algebraic proof. Exact sharp witness: `(x_U,x_V,z_U,z_V)=(1/8,1,1/8,0)` maps to `(x'_U,x'_V,L',Delta)=(0,7/8,11/24,1/4)` and `A'-A=5/192=(5/48)*Delta`.

The transformation preserves only the specified errors and the **two mean times**; it need not preserve full stopped-time distributions, provenance, future operations or native Heartbeat X6 physics. BRC use: labeled positive P/Q mass multiplication and addition, with quotient permitted only after the observer-specific zonotope argument; source identity is kept in the proof. Formal Source CLAIM/Result and independent Driver acceptance remain separate. The next candidate must change the collision topology (e.g. two distinct interacting collision signatures); see NEXT_TASK.md.
