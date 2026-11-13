# Stage319-B — twentyfold exact near-floor Pareto germ and quantitative allocation separation

Status: **PORTABLE_AUTHOR_PROOF / EXACT_RATIONAL_BOUNDARY_EXECUTED / UNREVIEWED / NOT_ADMITTED**. Research2 independent portable author work, 2026-10-31. Results concern the declared *external positive-rational two-source, locked-Bernoulli, three-visit BRC auxiliary observer*, not P000-native X6 motion.

Frozen GLOBAL_KNOWLEDGE_V1 main: baeff603b41316acbcca77548b3225dfb33b6fe0. Enterprise Math main: 3f8a74801fe26740a2dfeb56e1999590ec12424c. P000 original global Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc (startup projection matched); actual EM P000 V5 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. ACTIVE worldview Git blob 99238c3466eb0805748bae01fd1a20868a5a351e. Parent full proof and executed exact 274-leaf exterior interval certificate: Stage318-B immutable e3517f652de0c11bae9cfd39cc1ebd1dc1459a22, directory research_notes/n12_aux_iid_stage318b_local_pareto_germ_20261031_RESEARCH2. These predecessor assertions are explicitly used as previously author-proved lemmas; no independent review is inferred. Stage307-B.2 unique algebraic optimum: immutable 128d2ce6aeb0299cdf842d0ad65082a64ba9d475.

## Model and established exact interfaces

Two hidden sources S, private h=(J,W,Y) with source-conditional weights [(63,1),(21,3),(21,3),(7,9),(9,7),(3,21),(3,21),(1,63)]/256, three future accesses to eight permanently locked Bernoulli rates t_h. Public observation G=(W,Y), provenance-tagged (S,J,G), actions H (independent fair) or F (rate port) chosen adaptively from public history. Worst total variation agrees with three all-F future outputs, as shown in the frozen parent. Stage315-B exactly resets inner t001=t010=1/4, t101=t110=3/4 at tagged optimum; Stage316-B exactly reduces the resulting complete eight-real-rate optimum to two complementary two-rate groups.

Define B_k(z)=z^k(1-z)^(3-k), r_k(x,y)=(4B_k(x)+B_k(y))/5-p_k with p=(61,21,9,9)/160,
d(x,y)=(1/2) sum_{k=0}^3 binom(3,k)|r_k|, b(x,y)=(5/16)d(x,y), and
c(x,y)=[63D3(1/4,x)+D3(3/4,x)+9D3(1/4,y)+7D3(3/4,y)]/256.
Here D3 is TV distance of independent three-Bernoulli-word laws. Set C(s)=min_{b(x,y)<=s} c(x,y), beta*=min b, Pmin=2beta*, K=33/1024, and F3(z)=min_{P3(t)<=z} T3(t). Stage316 gives the **exact** scalar infimal convolution
F3(z)=K+min_{s in [beta*,z-beta*]}[C(s)+C(z-s)].
Stage307 gives unique (x*,y*) with r0=r1=0, x*=1-a*, and
a* in (768916059144478,768916059144479)/10^15,
y* in (555508857277,555508857278)/10^12.

## Theorem 319A: complete eight-rate global germ extends 20-fold

For every real 0<=epsilon<=delta=1/5000000 (previously 0<=epsilon<=1/100000000), the unique global single-block minimizer of C(beta*+epsilon) is the rightward r1=0 branch (x_epsilon,y_epsilon) with b=beta*+epsilon and x_epsilon>=x*. Consequently

F3(Pmin+epsilon)=33/1024+c(x*,y*)+c(x_epsilon,y_epsilon).

For epsilon>0 the complete eight-rate tagged problem has exactly two global minimizers, corresponding to placing the changed block in either source-complemented group. For epsilon=0 its tagged minimizer is unique. Throughout the new interval C is strictly decreasing and -41<C''(s)<-38 for beta*<s<=beta*+delta. At the floor 1.197917< -C'(beta*+) <1.197919.

**Proof.** The immutable Stage318 global 274-leaf exterior cover certifies d(x,y)-d* >1/200000 outside B=[23/100,24/100] x [55/100,56/100]. Hence outside B, b-beta*>1/640000>delta; no feasible competitor can be there. Inside B, the existing Stage307/318 sharpness lemma d-d* >= (|x-x*|+|y-y*|)/120 gives

|x-x*|+|y-y*|<=384 delta=6/78125=0.0000768.

The exact algebraic root brackets above give distance to **each** boundary of the previous interval-certified R=[231/1000,2312/10000] x [555/1000,556/1000] greater than 6/78125; the minimum is the left x margin, >0.000083940855521. Thus **every** feasible block is in R. The previous Stage318 rational certificates for all four open residual chambers, nonzero det(grad b,grad c), r0/r1 kink transversality, slope ordering, and curvature were certified **uniformly across R** and require no new numerical assumptions.

For existence of all four candidate kink arcs throughout the enlarged budget, take an outward x displacement L=1/800000. Uniform |dy/dx|<12 ensures 12L is smaller than either vertical root margin, while L is smaller than either horizontal root margin; implicit continuation stays in R. The Stage318 four kink-arm bound |db/dx|>18/100 with outward positive b displacement yields a gain >9/40000000=2.25*10^-7 >delta=2*10^-7. By continuity and strict monotonicity each arm attains every epsilon in [0,delta]. Uniform certified branch slope separation ranks rightward r1=0 uniquely best. Interior smooth optima are excluded by certified chamber determinants; at positive epsilon the floor junction loses to the decreasing right branch. This proves unique global C, including exactly its original strict curvature bounds on the larger domain. Stage316's exact infimal convolution and strict decreasing concavity force complete budget spending in one source group: strictly concave split costs attain minimum only at the two endpoints. Stage315 handles the remaining four rates. QED.

## Theorem 319B: quantitative two-source allocation gap

For 0<epsilon<=delta and 0<theta<epsilon let f(u)=C(beta*+u) and define

Delta_epsilon(theta)=f(theta)+f(epsilon-theta)-f(0)-f(epsilon).

Then **38 theta(epsilon-theta) < Delta_epsilon(theta) < 41 theta(epsilon-theta)**, with zero at theta=0 or epsilon. Proof: since -41<f''<-38 on the entire interval,

Delta_epsilon(theta)=integral_{t=0}^theta integral_{s=t}^{t+epsilon-theta} [-f''(s)] ds dt,

and the rectangle of integration has measure theta(epsilon-theta). The endpoint second derivative is one-sided, which does not affect this integral. For equal split, 19 epsilon^2/2 <Delta<41 epsilon^2/4. At epsilon=1/5000000, this strict difference is between 3.8e-13 and 4.1e-13 of tagged total variation: a quantitative explanation why floating grids can misclassify source-symmetric allocation.

For a full-budget, central-MAP, two-block representation whose tagged cost is within eta of F3(Pmin+epsilon), the smaller of its two actual per-block budget amounts must satisfy min(theta,epsilon-theta)<eta/(19epsilon) for an interior split. Indeed the exact C lower envelopes give an excess at least Delta>38 theta(epsilon-theta)>=19epsilon min(theta,epsilon-theta). At endpoint allocations the smaller budget is zero.

## New exact endpoint quadratic coefficient

The winning branch obeys r1=0, r0<0, with c=[63(1-x)^3+A(x)-2A(y)-1295/64]/256, A(z)=1-3z^2+2z^3.
Let B1(z)=z(1-z)^2, B2(z)=z^2(1-z); v=y'=-4B1'(x)/B1'(y),
w=y''=-(4B1''(x)+B1''(y)v^2)/B1'(y),
b'=(3/16)(4B2'(x)+B2'(y)v),
b''=(3/16)(4B2''(x)+B2''(y)v^2+B2'(y)w),
E'=c_x+c_y v, E''=c_xx+c_yy v^2+c_y w.
Thus C''(beta*+)=(E''b'-E'b'')/(b')^3 at (x*,y*), an explicit algebraic number. Exact outward Fraction intervals on the displayed root brackets give the new strict rational enclosure

**-39.655469 < C''(beta*+) < -39.655468**,

and 1.19791766< -C'(beta*+) <1.19791767. Hence
F3(Pmin+epsilon)=F3(Pmin)-kappa epsilon + (C''(beta*+)/2) epsilon^2 + o(epsilon^2).
The standard-library exact rational interval checker in this directory was actually executed. Its finite assertions cover the *new* rational endpoint, margin, kink reach, and curvature calculations, not an independent reexecution of Stage318's global cover/determinant certificates.

## Current authority, boundary and next question

2026-10-30 22:04 UTC native em_status: research_authority_granted=false; control_tasks owner read returned CONTROL_QUOTA with 5/5 active native jobs. Thus this author proof has no Source CLAIM/Result or independent Driver acceptance. BRC usage: REUSE_APPLIED of typed positive source-weight and public-vs-tagged future observer split under the exact Stage315/316 source semantics; no signed amplitude, no native X6 embedding. The native P000 six-axis path, third slice coordinate, triadic force closure, ordered time and registered final Cell address remain separate typed mapping tasks.

This proof method's first explicit bottleneck is the **existing R margin**: the coarse bound 384epsilon cannot force localization inside R beyond (x*-231/1000)/384~2.18595978e-7. That ceiling is a limitation of this particular certificate, **not** a proved Pareto phase transition. Stage320-B should enlarge R or sharpen the local sharpness bound and re-certify chamber/kink/curvature inequalities before searching for an actual first competitor.