# EC49AS — exact all-real causal BRC optimum to η=32/103

Date: 2026-10-30. Classification: AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_CERT_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.

## Exact statement

Retain the strictly positive auxiliary 18+18 leaf BRC observer from EC49AQ/AR. Hidden w∈{0,1,2}; observed u∈{0,1}; purchased z∈{0,1,2}. Define t(w,u)=1/2+(2u−1)(1−w)η, P(w,u,z)=t(w,u)(1+1[z=w])/12, Q(w,u,z)=t(w,u)/9 for 0≤η<1/2. First-stage causal action c∈{A0,A1,B0,B1,STOP} has respective costs (1,1,2,2,0) and arbitrary real conditional probabilities x[w,c]. Its expected cost is C1=43/48. Erase hidden w; only (c,u) is observed before a fresh conditional independent coin r(c,u) buys z, at exact C2=13/16. Terminal decisions depend solely on realized observations and independent behavioral randomness. Let H=α−(177/172)β for acceptance probabilities α=P(accept), β=Q(accept).

**Theorem (all real lawful causal strategies).** For every real 175/674≤η≤32/103,

    max H = 77/688 + (674η−175)/16512.

At η=3/10 this equals 293/2580; at η=32/103 it equals 1503/13184. The older EC49AQ/AR theorem gives max H=77/688 on 0≤η≤175/674. Together these establish the full global optimum through 32/103, with a sharp first plateau boundary at η=175/674.

## Causal BRC support upper bound

For each paid action c<4 and u, define q_z=x[z,c]t(z,u)/3, T=Σ_z q_z, and Vη(c,u)=(1/172)Σ_z[43q_z−16T]_+, where [a]_+=max(0,a). Purchased observation scores are precisely [P−(177/172)Q]_+=[43q_z−16T]_+/172. Unpurchased and STOP observations have equal source masses and optimal support zero. Every lawful causal purchase/acceptance mechanism obeys

    H ≤ Σ_{c<4,u} r(c,u)Vη(c,u) ≤ Fη(x):=Σ_{c<4,u} Vη(c,u).

The exact sensor budget requires C2=Σ_{c<4,u}r(c,u)T≤c(x):=Σ_{c<4,u}T=(1/3)Σ_{w,c<4}x[w,c]. The first-stage cost is C1=43/48, hence x is in the η-independent cut polytope

    Π={x≥0: Σ_c x[w,c]=1 (each w), Σ_{w,c}cost(c)x[w,c]=43/16,
       Σ_{w,c<4}x[w,c]≥39/16}.

The identities Σ_u t(w,u)=1 make these resources independent of η. For fixed x each purchased score is affine in η and Fη(x) is convex in η and in x. Thus M(η)=max_{x∈Π}Fη(x) is convex in η and is attained at an extreme point of Π.

## Finite complete endpoint certificate

The four row/cost independent equations admit at most four strictly positive variables at an original vertex. Exhaust C(15,4)=1365 supports with exact Gaussian elimination to obtain 168 distinct original vertices. Of these, 24 have c(x)≥13/16, all with c(x)=43/48; none lies on the purchase boundary. The fifth independent equality Σ_{w,c<4}x[w,c]=39/16 produces 144 new nonnegative 5-support vertices from exhaustive C(15,5)=3003 systems. These 24+144=168 vertices are the complete cut polytope. The included independently executable Fraction verifier reconstructs and checks this enumeration and evaluates original purchased P/Q scores at each endpoint:

| η | maximum F on 24 original high vertices | maximum F on 144 cut vertices | M(η) |
|---|---|---|---|
| 175/674 | 36/337 (4 ties) | 77/688 (24 ties) | 77/688 |
| 32/103 | 1503/13184 (4 ties) | 1503/13184 (8 ties) | 1503/13184 |

The proposed target line connects exactly the displayed endpoint M values. By convexity, for every real η between the two endpoints, M(η) is at most this chord. In particular, the all-real upper bound is established without a parameter grid.

## Legal equality witness

Take x[0]=(0,3/16,1/4,0,9/16), x[1]=(1,0,0,0,0), x[2]=(0,1,0,0,0). Buy the sensor on all paid (c,u) fibers: this has exact purchase cost 13/16. Accept iff (c,z)∈{(A0,1),(A1,2),(B0,0)} OR (c,u,z)=(A1,1,0). The decision observes only (c,u,z); no erased w or shared random seed is used. The first three acceptance classes have constant H=77/688. The added event scores exactly

    P(A1,u=1,z=0)−(177/172)Q(A1,u=1,z=0)
       =(674η−175)/16512≥0.

Thus the legal policy attains the chord for every η in the interval and equality holds. At η=3/10, (α,β,H)=(83/192,223/720,293/2580); at η=32/103, (1423/3296,3053/9888,1503/13184).

## Precisely scoped next obstruction

At η=32/103 four original high-purchase-mass vertices tie the upper envelope. One is x_hi[0]=(0,11/16,0,0,5/16), x_hi[1]=(1,0,0,0,0), x_hi[2]=(0,1,0,0,0). Its paid mass is 43/48>13/16; buying on all paid branches is not a cost-feasible policy. Its *hypothetical full-purchase* support on 32/103≤η≤1/3 is Fη(x_hi)=9/128+9η/64. Every purchased score retains its sign across that interval, as checked exactly at both endpoints. Hence

    Fη(x_hi)−[77/688+(674η−175)/16512]
      =(103/1032)(η−32/103)>0 for η>32/103.

This is a sharp breakdown of **this full-purchase envelope certificate**, NOT proof that the true cost-constrained optimum changes at 32/103. A purchase-aware dual or a lawful improved causal witness is the next mathematical obligation.

## Evidence and boundaries

Actual Python Fraction execution of VERIFY.py produced EXACT_REPORT.json (no floating arithmetic). Finite support exhaustion is complete under the rank vertex argument; convexity plus the legal witness supplies the universal real-parameter inference. This is only a one-step strictly positive auxiliary probability-BRC result. Native signed/phase BRC, six-axis X6 and heartbeat require separate typed observer/update preservation. Independent review, formal proof assistant verification and Source-native Result/CLAIM admission remain pending. No P000 or ACTIVE worldview modification is made.
