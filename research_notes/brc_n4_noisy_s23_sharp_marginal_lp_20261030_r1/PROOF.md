# BRC N=4 — sharp noisy-source S23 marginal minimax and universal finite-S2 dual

**2026-10-30; author mathematical result, exact witness and executed checker; UNREVIEWED / NOT_ADMITTED.** This is the fixed external 16-leaf positive-weight BRC P/Q experiment, not a native six-axis physical theory. Source details in SOURCES.md. Reuses frozen predecessor PR #1738 commit `4b05eff9aa9779034ffed6694aa2b6dec6393a7c`.

## Population and lawful observers
For `s=AU,AV,BU,BV`, `j,k=0,1`: `Q(s,j,k)=q_s/4`, `P(s,j,k)=q_s r_sj/4`; `q=(1/6,1/3,1/4,1/4)`, `r_AU=(9/10,11/10)`, `r_AV=(1/4,1/4)`, `r_BU=(1/5,9/5)`, `r_BV=(2,2)`. Both laws are normalized, 16 leaves strictly positive. BU has mass 1/4 in each, but conditional prior `P(j=0|BU)=p=1/10`, `Q(j=0|BU)=1/2`. The source sensor `Z=j XOR Bernoulli(epsilon)`, independent, is common to both laws, `0<=epsilon<=1/2`. Decoder sees `(C,Z)` where old `C=(E,A,B)` is identically distributed under both laws, and must reconstruct only `(C,Y)`, **discarding the source sensor from the scored marginal**. All E/A outputs are exactly reconstructible; BU contributes factor 1/4 to global TV.

In the lawful S23 terminal-Q subfamily, BU branch 0 continues to T4 at rate `u`, branch 1 at `v`; then the actual sampled k is read, not changed, and the decision is Q. `u,v in [0,1]`. The BU alphabet is `Y=(B3,B4Q0,B4Q1)` with common kernels `F0=(1-u,u/2,u/2)`, `F1=(1-v,v/2,v/2)`.

## THEOREM 1 (all-real exact S23 terminal-Q marginal radius)
Define `q=(u+v)/2`, `delta=2|v-u|/5`, `rho=4(1-2epsilon)/5` and `s=sign(v-u)`. If `u=v` the radius is zero; otherwise

```
R_marg(epsilon,u,v) =
  (1/4) max(0, [delta-rho*q]/[2+s*rho],
                [delta-rho*(1-q)]/[2-s*rho]).
```

This includes epsilon=1/2: `R=|u-v|/20`; and fixed G4 `(u,v)=(0,1)`: `R=epsilon/(6+8epsilon)`. The denominators are positive for the full real domain.

**Reduction.** Both targets have equal masses on Q0 and Q1. Swap k labels in an arbitrary common decoder and average it with its swap. TV convexity does not increase either error. Thus an optimal decoder has a symmetric terminal law and two rates `x=P_dec(T4|Z=0)`, `y=P_dec(T4|Z=1)`. Write `a=p+(1-2p)epsilon`, `p=1/10`. The BU objective is exactly
`min_{0<=x,y<=1} max(|a*x+(1-a)*y-(q+s*delta)|, |(x+y)/2-q|)`.
Put `w=(x+y)/2`, `r=(y-x)/2`. Then `|r|<=min(w,1-w)` and `a*x+(1-a)*y=w+rho*r`.

**Lower certificate.** Suppose both errors <=E. If `s=+1`, `w<=q+E`, `w+rho*r <= (1+rho)w` and `w+rho*r <= (1-rho)w+rho`. Comparing each upper envelope at w=q+E against the needed value `q+delta-E` gives `E >= (delta-rho*q)/(2+rho)` and `E >= (delta-rho*(1-q))/(2-rho)`. If `s=-1`, use `w>=q-E` with lower envelopes `w+rho*r >= (1-rho)w` and `w+rho*r >= (1+rho)w-rho`; comparison with `q-delta+E` gives the same two inequalities with denominators reversed. Together with E>=0 these are the stated global lower bounds, for every real stochastic decoder.

**Attainment.** Set E equal the displayed max, `w=q+sE`. Since `|u-v|<=2min(q,1-q)`, `0<=rho<=4/5` and the two facet bounds hold, `0<=E<=delta/2<=min(q,1-q)`; hence w is feasible. For rho>0 set `r=s*min(min(w,1-w),(delta-E)/rho)`; for rho=0 use r=0. Put `x=w-r,y=w+r`. They lie in [0,1]. Q error is E; the P error is `max(0,delta-E-rho*min(w,1-w))<=E` because the facet inequalities imply `rho*min(w,1-w)>=delta-2E`. If u=v, choose x=y=u. This proves the formula without finite-grid extrapolation.

The zero cone at epsilon<1/2 is equivalently nonnegativity and <=1 for both uniquely inverted exact rates `x*=[(1-epsilon)u-epsilon*v]/(1-2epsilon)`, `y*=[(1-epsilon)v-epsilon*u]/(1-2epsilon)`. At epsilon=1/2 zero requires u=v. Joint-fidelity remains a separate objective.

## THEOREM 2 (general exact finite-alphabet S2 marginal LP dual)
For any finite Y and law-common future kernels F0,F1, let `TP=p F0+(1-p)F1`, `TQ=(F0+F1)/2`, `a=p+(1-2p)epsilon`, `b=1-a`. Every shared decoder consists of probability vectors K0,K1. Its conditional minimax TV error `E_*` equals the following **exact** dual optimum:

```
maximize  sum_y(h_y TP_y + t_y TQ_y) - M0 - M1
subject to 0<=lambda<=1,
           0<=h_y<=lambda, 0<=t_y<=1-lambda (all y),
           M0>=a h_y + t_y/2, M1>=b h_y+t_y/2 (all y).
R_marg = E_*/4.
```

**Proof.** On a finite probability simplex, `TV(A,B)=max_{0<=f_y<=1} f·(A-B)`. The max of the P/Q errors is the max over `lambda in [0,1]` of their weighted combination. Let `h=lambda*f`, `t=(1-lambda)*g`; these form a compact convex polytope. Decoder probabilities K0,K1 form a compact convex product of simplices. The resulting payoff is affine in each block:
`h·TP+t·TQ-(a*h+t/2)·K0-(b*h+t/2)·K1`.
Finite minimax/LP strong duality exchanges max and min. Minimizing over each simplex picks the *largest* coefficient; epigraph variables M0,M1 implement those maxima. This yields the exact dual above, without forcing K0 or K1 onto the segment joining F0 and F1. It remains valid for zero-kernel entries and epsilon=1/2.

For lawful S2 with actual k-dependent terminal decisions `d_jk in [0,1]`, choose `Y=(B3,B4P0,B4Q0,B4P1,B4Q1)`, `F0=(1-u,u*d00/2,u*(1-d00)/2,u*d01/2,u*(1-d01)/2)`, `F1=(1-v,v*d10/2,v*(1-d10)/2,v*d11/2,v*(1-d11)/2)`. S23 imposes d_j0=d_j1; changing a terminal Decision label is not a physical change to k.

## Exact non-S23 rational primal–dual witness
At epsilon=1/4, u=1/4, v=3/4 and lawful S2 `d=(1,0,0,1)`, the kernels are `F0=(3/4,1/8,0,0,1/8)`, `F1=(1/4,0,3/8,3/8,0)`, `a=3/10,b=7/10`. A decoder attaining both BU losses 1/16 is `K0=(1,0,0,0,0)`, `K1=(0,1/56,27/56,11/28,3/28)`. A feasible dual certificate with objective exactly 1/16 is `lambda=5/12`, `h=(0,0,5/12,5/12,0)`, `t=(7/12,7/12,0,0,7/12)`, `M0=M1=7/24`. Direct rational substitution proves both feasibility and equality. Hence **global R_marg=1/64**. At the **same** epsilon,u,v with S23 all-terminal-Q decisions, Theorem 1 instead gives **R_marg=0** via x=0,y=1. Correlation between actual observed k and terminal Decision therefore changes marginal-only reconstructibility without changing sensor error or continuation rates.

Other exact terminal-Q points at epsilon=1/4: `(u,v)=(0,1/2):R=1/96`; `(9/10,1):R=1/320`; `(0,1):R=1/32`. The active positivity facets matter; a universal scaling solely by `D=TV(F0,F1)` is invalid for marginal deficiency.

## Evidence and limits
`VERIFY.js` executes BigInt-reduced rational arithmetic over all 16 P/Q leaf masses, 405 S23 rational parameter triples, six rational boundary/witness points and the full five-output S2 primal/dual certificate. `RUN_EVIDENCE.txt` captures its actual output; the all-real claim rests on the proof above. Separate local Python 3.13.5/SciPy 1.17.0 tests also solved 405 S23 and 320 S2 numerical primal/dual LP pairs; these are independent finite cross-checks, not all-real proof. The present scope is an external positive-weight finite observer problem; native P000 six-axis Cell, three-dimensional slice and separately typed time need an explicit observer/future-operation bridge before any physical transfer.
