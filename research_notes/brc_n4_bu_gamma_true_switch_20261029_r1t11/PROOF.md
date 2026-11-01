# BRC N=4 BU-bit observer — exact high-b phase switch at gamma

Date: 2026-10-29. **AUTHOR ANALYTIC PROOF / EXACT SYMBOLIC AND FRACTION CHECKS / UNREVIEWED / NOT_ADMITTED.** External finite probability stopping tree only; no proved native X6/BRC-heartbeat correspondence or native physical residual.

## Fixed inputs and sourced reduction

Reuse the full-observer, actual-causal-policy reduction and event duals in `awdawmip/enterprise-math@bfc03aa8c3e11c6ddf1a28704febe114313b0930:research_notes/brc_n4_bu_zero_iff_beta_extension_20261029_r11/PROOF.md` (source Git blob `d0580011168b08bd81ce2eed991cbadf2d2db37d`); its predecessor is `awdawmip/enterprise-math@01959291d98e6d666cf6b769889bcca623caf12c:research_notes/brc_n4_bu_expanded_rectangle_zero_wedge_20261029_r1t11/PROOF.md`. The source theorem establishes that all original lawful causal S2/S23 random policies can be observation-preservingly postprocessed into an actual realizable compressed five-variable competitor, without increasing either TV. Thus `d2=d23` is exactly the global minimax below, **not** a free-flow relaxation.

The strictly positive four-branch Q masses for AU, AV, BU, BV are `(1/6,1/3,1/4,1/4)`; their P/Q ratios are `(1,1/4,1,2)`. The AU descendants' ratios are `9/10,11/10`, BU descendants' `1/5,9/5`, and each is duplicated at stage four: 16 strictly positive P/Q leaves, both laws normalizing to 1. Fix target `F=(a,b,1,0)`, `a=49/50`, `0<b<=1`, observer `(T,Decision,Z_BU)`. The origin bit records a BU prefix only upon stage-three arrival, and equal-likelihood AU/BU share the competitor's instantaneous continuation c.

A lawful compressed competitor satisfies `0<=A,B,c<=1, 0<=U<=A, 0<=V<=B`. Here U,V are AV/BV unconditional continuation masses. Put

```
s=(A-a+B-b)/2;       t=(A-a+3(B-b))/4;    H=B*c/4;
rQ=a/6-A*c/6-U/3-V/4; rP=a/6-A*c/6-U/12-V/2;
DeltaQ=(s,H-s-rQ,rQ,-H);
DeltaP=(t,H-t-rP,rP,-H).
```

These are target-minus-competitor signed complete four-observation-atom masses. Each sums to zero. `e=max(TV_Q,TV_P)` dominates the absolute mass of every observable event in either law.

## Exact new theorem

Define
```
beta = 1641/1525 - sqrt(3002689)/1830 = 0.12916563872152901812... ;
gamma = (sqrt(38494)-83)/750 = 0.15093183825600634856... ;
c_p=(7-a-21*b)/(4*a+12*b+2);
e_p=c_p*(a+3*b-1)/12;
c_0=(2*a-7*b)/(2*a+4*b);
e_0=b*c_0/4=b*(2*a-7*b)/(8*(a+2*b)).
```

**For all real `3/50<=b<=1`, minimizing over all lawful real-valued causal random competitors,**

```
d2(49/50,b)=d23(49/50,b)=
  e_p,  for 3/50 <= b <= gamma;
  e_0,  for gamma <= b <= 7/25;
  0,    for 7/25 <= b <= 1.
```

The pieces agree at gamma and 7/25. The previously proven `[3/50,beta]` capacity segment and global `zero iff b>=2a/7` segment are sourced above. New mathematics is the continuous `[beta,gamma]` optimality extension and the continuous `[gamma,7/25]` competing-strategy exact optimum. The old beta endpoint is *not* the true minimax switch; gamma is.

## Reused complete-event TV certificates

The pinned source establishes, by nonnegative weighted full-observer events and corrections involving `V-B<=0` or `A-1<=0`, that for any feasible competitor
```
L0(c)=[4a-14b-3ac-(a+3b)c^2]/[2(23-2c)] <= e  (0<=c<=3/7);
L3(c)=c[a-(a+3b)c]/[2(7-2c)]             <= e  (0<=c<=1);
R(c)=c(a+3b-1)/12                        <= e  (0<=c<=1).
```

The source event decompositions and their weight sums are rechecked symbolically in VERIFY.py; they do not ignore BU origin or the causality constraints. `L0` is strictly decreasing on `[0,3/7]` because its derivative has the strictly negative numerator `2(a+3b)c^2-46(a+3b)c-61a-28b`. `L3` has no interior minimum on any subinterval of `[0,1]`: its derivative has numerator `D(c)=7a-14(a+3b)c+2(a+3b)c^2`, with `D'(c)=(a+3b)(4c-14)<0`. Thus `L3(c)>=min(L3(u),L3(v))` on every `[u,v]`.

Exact all-variable identities:
```
L0(c_0)=L3(c_0)=e_0;
L3(c_p)=R(c_p)=e_p;
c_p-c_0=(1-a)(5a+21b)/[2(a+2b)(2a+6b+1)]>0.
```
At `a=49/50`, factor exactly:
```
e_p-e_0=
7*(37500*b^2+8300*b-2107)/[4800*(75b+37)*(100b+49)].
```
The numerator quadratic is strictly increasing on `b>=0`, with unique positive root gamma. Hence `e_p<=e_0` when `b<=gamma`, and the opposite inequality when `b>=gamma`. This comparison alone does **not** establish optimality; the following exhaustive dual partitions do.

## New optimality proof: beta <= b <= gamma

Here `9/70<beta<13/100<gamma<4/25` and `9/70>8a/61=196/1525`; hence `0<c_0<3/7` and `0<c_0<c_p<1`. For *every* competitor c in [0,1]:
1. If `0<=c<=c_0`, `e>=L0(c)>=L0(c_0)=e_0>=e_p`.
2. If `c_0<=c<=c_p`, `e>=L3(c)>=min(L3(c_0),L3(c_p))=e_p`.
3. If `c_p<=c<=1`, `e>=R(c)>=R(c_p)=e_p` since `a+3b-1=3b-1/50>0`.

A **real lawful causal** matching strategy is `A=1, B=(a+3b-1)/3=b-1/150, c=c_p, U=B(1+c_p), V=B`. Feasible because `B>0`, `0<c_p<1`, and `U<=2B<2*(4/25)<1=A`. Its complete signed observations are
```
DeltaQ=((1-a)/3,e_p-(1-a)/3,0,-e_p);
DeltaP=(0,0,e_p,-e_p).
```
Both TV values equal e_p: indeed `c_p>=c_p(4/25)=19/56` and `3b-1/50>=3*(9/70)-1/50`, hence `e_p>=(19/56)*(3*(9/70)-1/50)/12=38/3675>1/150=(1-a)/3`. This proves exact global optimality throughout `[beta,gamma]`, and the prior theorem covers `[3/50,beta]`.

## New optimality proof: gamma <= b <= 7/25

The lawful alternative is
```
A=a, B=b, c=c_0, U=b*(1+c_0), V=b.
```
Since `b>=gamma>3/20` and `b<=7/25`, `0<=c_0<=c_0(3/20)<3/8` and `U<=(7/25)*(11/8)<a`. Its signed observations are
```
DeltaQ=(0,e_0,0,-e_0);  DeltaP=(0,0,e_0,-e_0).
```
Hence both TV values are exactly e_0.

Set `c_1=3*b*c_0/(a+3*b-1)`; then `R(c_1)=e_0`. On `[gamma,7/25]` we have `0<=c_0<=c_1<1`, because `c_1/c_0=3b/(3b-1/50)<=45/43` for c_0>0 and `c_0<3/8`, whence `c_1<135/344<1`. Also `c_0<3/7`. The *new endpoint event-dual factorization* is exactly
```
L3(c_1)-e_0 =
-7*b*(25b-7)*(37500b^2+8300b-2107)
 /[4*(100b+49)*(150b-1)*(22500b^2+5150b-49)] >= 0.
```
The denominator is positive; `25b-7<=0`, and the quadratic is >=0 by b>=gamma. Therefore partition *every* competitor c:
1. `0<=c<=c_0`: `e>=L0(c)>=L0(c_0)=e_0`.
2. `c_0<=c<=c_1`: `e>=L3(c)>=min(L3(c_0),L3(c_1))>=e_0`.
3. `c_1<=c<=1`: `e>=R(c)>=R(c_1)=e_0`.

Upper and lower bounds match for all real b, proving the second interval. At `b=7/25` the alternative becomes the zero-loss policy; for every `b>=7/25`, the valid `A=a,B=b,c=0,U=V=2a/7` achieves zero error.

## Exact rational strict witness and verification

At `b=4/25>gamma` the globally optimal causal strategy is `(A,B,c,U,V)=(49/50,4/25,21/65,344/1625,4/25)`, with `TV_Q=TV_P=21/1625`. Mechanical extension of the old capacity formula gives `437/33600`, **strictly larger by `181/2184000`**. This is both an independently checkable strict feasible counterexample to the old formula outside its phase and, using the event duals, the exact true global optimum.

Local `VERIFY.py` ran 19 exact SymPy identity groups, independently enumerated all 16 strictly positive Q/P leaves, checked 5 exact capacity, 5 alternate and 4 zero-loss causal policies and the strict rational witness; PASS output and exact provenance are recorded separately. The continuous-real theorem follows from the analytic all-c partitions, **not** finite tests or LP scans. No independent Driver/Lean review, canonical CLAIM/Result, or native-P000 X6 faithful dynamics is claimed. Site-scoped native research authority was false and owner inventory returned CONTROL_QUOTA; this remains an author-side portable research artifact.

**Next:** solve the remaining `0<b<3/50` for fixed `a=49/50` (notably `b<1/150`, where capacity B would be negative); independently study the gamma switch as an open a,b curve by signed event certificates. Preserve exact observer and native/finite-model boundaries.
