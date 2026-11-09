# PREFIX-650-R6 — BRC双采样槽位的二阶曲率与单侧极限外推定理

Date: 2026-11-10 (Asia/Shanghai). Role: independent TASK_RESEARCH. Status: AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d. Mother objective: the global variance maximum of the frozen signed two-informative-direction BRC first-stop statistical observer.

## Statement and domain

Retain the signed 189-layer first-stop observer of PREFIX-645–649. Let Y(p,z) be the Poissonized maximum first-stop time and T_q its marked discrete action count for real model-admissible q>=12. Define a=E[Y], b=Var(Y), c=kappa3(Y), d=kappa4(Y), t=1/q, B=b-a*t.

Throughout R = { (p,z): |p-1/6|<=2^-29 and |z-19/128|<=2^-29 }, PREFIX-649 supplies strict bounds
108<a<110, 335<b<338, -1266<c<-1153, 14638<d<86111.
For every 0<=t<=1/12, B>325.

The standardized skewness and excess kurtosis are
g1(t)=(c-3*b*t+a*t^2)/B^(3/2),
g2(t)=(d-6*c*t+7*b*t^2-a*t^3)/B^2.
At t=0 these extend continuously to g1(0)=c/b^(3/2) and g2(0)=d/b^2, their infinite-slot limits.

**Theorem 650.1 (opposite strict curvature).** For every (p,z) in R and t in [0,1/12]:
-1/4 < g1''(t) < 0 < g2''(t) < 3/4.
Thus g1 is uniformly strictly concave and g2 uniformly strictly convex in reciprocal sampling density.

**Theorem 650.2 (one-sided Richardson extrapolation).** For every (p,z) in R and real model-admissible q>=12 define
E1(q)=2*gamma1(2q)-gamma1(q),
E2(q)=2*gamma2(2q)-gamma2(q), where gamma_i(q)=g_i(1/q).
Then
gamma1(infinity) < E1(q) < gamma1(infinity)+1/(16*q^2),
gamma2(infinity)-3/(16*q^2) < E2(q) < gamma2(infinity).

At the two actual BRC slots 12 and 24:
gamma1(infinity) < 2*gamma1(24)-gamma1(12) < gamma1(infinity)+1/2304,
gamma2(infinity)-1/768 < 2*gamma2(24)-gamma2(12) < gamma2(infinity).

The two-slot operation cancels the leading 1/q error and recovers the infinite-slot standardized cumulants to certified O(q^-2), with a known error direction.

## Proof

Differentiating the exact cumulant transforms from PREFIX-649 twice yields

g1''(t) = -a*(a^2*t^2+a*b*t-15*a*c+28*b^2)/(4*B^(7/2)),

g2''(t) = (6*a^2*d+14*b^3-24*a*b*c+t*(22*a*b^2-12*a^2*c))/B^4.

Because a,b,d>0 and c<0, the first expression is strictly negative, the second strictly positive. Since B>335-110/12>325 and sqrt(B)>18, the inherited strict envelopes imply

-g1''(t) < [110*(110^2/12^2+110*338/12+15*110*1266+28*338^2)]/[4*325^3*18]
            = 2095202087/8897850000 < 1/4,

g2''(t) < [6*110^2*86111+14*338^3+24*110*338*1266+(22*110*338^2+12*110^2*1266)/12]/325^4
           = 23880888404/33469921875 < 3/4.

This proves Theorem 650.1. For any twice continuously differentiable g and h=1/(2q), the exact centered difference identity is

g(2h)-2*g(h)+g(0) = integral_0^h integral_0^h g''(u+v) dv du.

The extrapolated difference E(q)-g(0) is the negative of this integral, so curvature signs provide the one-sided inequalities. Its absolute value is bounded by h^2/4 for g1 and 3*h^2/4 for g2, namely 1/(16q^2) and 3/(16q^2). All inequalities are strict because the derivative inequalities are strict throughout the compact interval. QED.

## Verification, provenance, and next scientific action

The companion standard-library Python certificate recomputes the exact rational bounds and derivative-polynomial identities and generates PREFIX650_R6_RESULTS.json. Execution: ALL_CHECKS_PASS 38. These checks cover the new consequence of previously published exact cumulant envelopes; the symbolic differentiation and centered integral identity are given in the proof. Original 189 survivor-state and 96-port native dynamics computations are not rerun.

Immutable scientific provenance: PREFIX-645@f11c0345bf89321aba48d90671c244bdec25d416; PREFIX-648@6b53f51abe70ac29a591fa9fcd29c1308f6c98e2; PREFIX-649@cb21c9452f5bc094493cd92bfa37be99ab988782.
This mathematical result is model-internal, author-proved and not independently reviewed or canonically admitted. The local statistical coordinates are typed readouts of the fixed signed BRC observer, not an independent two-dimensional native world.

Next: use centered-moment Bernstein and score derivatives to tighten the fourth-cumulant envelope and enlarge R; continue separately toward certified global two-parameter sampling-variance extrema.
