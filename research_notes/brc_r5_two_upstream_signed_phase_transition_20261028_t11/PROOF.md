# R5: Exact signed-support phase transition in a two-upstream LR collision

2026-10-28 Asia/Shanghai. AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED. This is a finite external two-measure statistical observation model, not a native X6 physical result or admitted theorem. Author-side portable research, not a native CLAIM, Result, review, or active ownership assertion.

**Frozen source input:** GLOBAL_KNOWLEDGE_V1 `main@2a24dd5d0e16a1b273d49ae4a49242efc6b2d6cd`; Enterprise Math `main@94fbdca156237439661e74007165261b9b493eed`. Read global bootstrap/manual, project AGENTS/P000/ACTIVE worldview, Heartbeat X6/time, portable research and `research_notes/brc_r5_two_upstream_scalar_price_blindspot_20261028_t11/{PROOF.md,NEXT_TASK.md}`. P000 keeps the native six-dimensional discrete Cell space with separately typed time. The external U/V history tree is a typed observer example with no asserted native X6 dynamics. The applied BRC carrier is **labeled positive rational P/Q branch mass**; signed coefficients occur only in the output linear objective.

## Exact tree

Parameters `0<theta<1, 0<d<1, 0<b<a<1/2`. At t=1 two distinguishable sources U,V have Q masses 1/2 and likelihood ratios `r_U=1+(1-theta)d`, `r_V=1-(1-theta)d`. Each root has a t=2 C branch with conditional Q probability theta and cumulative LR=1, or an O branch with conditional Q probability 1-theta and terminal LR `1+d` (U.O) / `1-d` (V.O). At collided U.C/V.C, another optional sample yields terminal LR values (1/2,1,3/2) with conditional Q kernels (a,1-2a,a) and (b,1-2b,b), respectively. All eight final P/Q masses are positive and each measure sums to 1. At t=1 and t=2 C a policy may stop declaring P or Q, or continue. O stops at t=2; terminal C leaves stop at t=3. Full policies see history; seedless-LR policies see only (time,LR), with arbitrary real local behavioral randomization and no persistent common seed.

Observer: `O=(e_P,e_Q,T_P,T_Q)=(P[declare Q],Q[declare P],E_P tau,E_Q tau)`. Write `V_full(lambda)` and `V_LR(lambda)` for minima of a signed real four-vector dot O.

## Theorem: necessary AND sufficient all-signed hull-equality gate

Set `H=(2+theta)b-theta*a`. For `0<d<=1/2` the following are equivalent:

1. `V_full(lambda)=V_LR(lambda)` for every signed real `lambda in R^4`;
2. `conv(O_full)=conv(O_LR)`;
3. `H >= theta*(1-theta)*d / [1/2-(1-theta)*d]`.

For `1/2<d<1`, a strict signed linear separation exists for every `0<b<a<1/2`. If H>0, within `d<=1/2` the equality condition is equivalently `d<=H/[2*(1-theta)*(theta+H)]`. If H<=0, every d>0 yields a strict separation. Convex-hull equality here does NOT assert equality of the two true behavioral images.

### Bellman proof, including all early stops and signed time costs

For `lambda=(alpha,beta,gamma,delta)`, put `f(r)=min(alpha*r,beta)`, `c(r)=gamma*r+delta`; f is concave for all signed alpha,beta. Define `D=2*f(1)-f(1/2)-f(3/2)>=0`, `C=c(1)`, and `g_U=aD,g_V=bD`. For source i=U,V, with sign +,- respectively, put

`r_i=1+sign*(1-theta)*d`, `r_iO=1+sign*d`,
`J_i=f(r_i)-theta*f(1)-(1-theta)*f(r_iO)>=0`,
`S_i=[f(r_i)+c(r_i)]/2`,
`B_i=[2c(r_i)+theta*f(1)+(1-theta)*f(r_iO)]/2`.

Exact backward induction yields

`V_full = sum_i min{S_i, B_i-(theta/2)*max(g_i-C,0)}`,
`V_LR = min_(y in {0,1}) sum_i min{S_i,B_i-(theta/2)*y*(g_i-C)}`.

A t=3 declaration at shared LR has the same locally optimal action for both sources. The affine time price c commutes with the likelihood-ratio martingale mean. Root stops are in both min expressions. Since any time-indexed policy information set is visited at most once along a path, each score is multi-affine in local randomization variables, so the above deterministic minimization is **exact for every real behavioral policy**.

When D=0, g_U=g_V=0 and a common C action is optimal. For D>0 with a>b, disagreement is possible only when `bD<C<aD`: U privately wants C-continue, V privately wants C-stop. Their respective strict root continuation advantages over t=1 stop are

`A_U=J_U+theta*a*D-(1+theta)*C-gamma*(1-theta)*d`,
`A_V=J_V-C+gamma*(1-theta)*d`.

A strict full-versus-LR gap occurs iff **both** A_U and A_V are positive: otherwise a privately optimal full policy can stop the masked source at t=1, so one shared collision action remains optimal. Because gamma is arbitrary and delta=C-gamma, a gamma with A_U,A_V>0 exists iff

`(2+theta)*C < J_U+J_V+theta*a*D`.

A C in the required open interval `(bD,aD)` exists iff

`(J_U+J_V)/D > H`.

Thus there is a strict all-signed separation iff some signed alpha,beta satisfy that inequality.

For D>0 the two-line concave f has one kink `k=beta/alpha` in (1/2,3/2) with downward slope jump `m=|alpha|`. Put `s=|k-1|<1/2`. At most one of J_U,J_V is nonzero. For `0<s<d` an interpolation calculation gives

`J_U+J_V=m*min(theta*s,(1-theta)*(d-s))`, `D=m*(1/2-s)`;

for s>=d, the numerator is zero. If d<=1/2, this ratio rises to s=(1-theta)d and then decreases (or remains constant at the d=1/2 endpoint), giving its exact maximum

`Rmax=theta*(1-theta)*d/[1/2-(1-theta)*d]`.

For d>1/2, taking s up to 1/2 from below keeps J positive while D tends to zero, so the supremum is infinite. Inserting Rmax into the strict-gap criterion proves the theorem. For finite trees, all signed support values characterize the compact convex hulls by the separating hyperplane theorem. QED.

## A NEW strict-positive rational all-direction equality frontier

Take `theta=3/4, a=1/4, b=1/8` (distinct C kernels). Then `H=5/32` and the exact phase boundary is

`d_critical=10/29`.

For **every 0<d<=10/29**, including rational d=1/10, the full and seedless-LR **convex hulls coincide in every signed four-dimensional direction**, while their true real-behavioral images remain an independent open decision problem. This supplies a previously missing equal-hull candidate, without prematurely claiming the mother problem.

For contrast, choose rational `d=2/5`, `lambda=(400,440,220,-199)`. Here `D=160, g_U=40, g_V=20, C=21, J_U=30, J_V=0`, `gamma*(1-theta)*d=22`; the two active continuation margins are 5/4 and 1. Bellman minimization gives

`V_full=3359/8`, `V_LR=1681/4`, exact difference **3/8**.

An explicit full-history policy continues U and V at t=1; continues at U.C and stops declaring Q at V.C; declares P at U.O, Q at V.O; at t=3 U.C low/mid declare Q and high declare P. It realizes

`O*=(219/320,7/32,19/8,19/8)`,
`lambda dot O*=3359/8`.

Every real seedless LR policy obeys
`400e_P+440e_Q+220T_P-199T_Q >= 1681/4`,
which O* violates by exactly 3/8. This d=2/5 model therefore has unequal convex hulls and is EXCLUDED from the mother candidates.

## Executed exact check and boundary

`VERIFY.py` uses standard-library Fraction and enumerates 20736 full and 864 seedless-LR deterministic decision descriptions for each of d=1/10, 10/29, 2/5. It verifies all eight leaf P/Q masses, normalization, six signed objectives per d, both Bellman formulas, the exact d=2/5 witness and 3/8 gap. Actual stdout in `EXACT_OUTPUT.txt`: `ALL EXACT PHASE-GATE CHECKS PASSED`. The finite direction sample is a regression check, **not** the proof of universal signed support equality; that is the symbolic theorem above. No native Source authority, CLAIM/Result, independent Driver review or physical X6 verification was obtained.

Next: for d=1/10 decide whether the **true seedless-LR four-observable image** is convex/equal to the full image. Provide exact polynomial elimination and a real nonattainment certificate, or constructive realization of every full-image point. Preserve all upstream stop and declaration actions. Numerical misses alone are not certificates.