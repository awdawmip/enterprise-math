# PREFIX-646-R6: A two-parameter open neighborhood of negative third cumulants

Date: 2026-11-10. Task: independent TASK_RESEARCH, no formal CLAIM. Frozen science pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Status: AUTHOR_PROVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Scientific question and result

PREFIX-645 (enterprise-math@f11c0345bf89321aba48d90671c244bdec25d416) established for the frozen signed two-informative-direction 189-layer BRC first-stop statistical observer, at (p0,z0)=(1/6,19/128):
E[Y0]<109, Var(Y0)>336, kappa_3(Y0)<-1209.
It also proved kappa_3(T_q) = q^3 kappa_3(Y)-3q^2 Var(Y)+q E[Y] for all valid marked-action models q>=12.

Theorem 646.1 (two-dimensional robust negative skewness):
Let h=1/134217728=2^(-27). For every p,z satisfying
|p-1/6|<=h and |z-19/128|<=h,
the same frozen statistical observer obeys
E[Y(p,z)]<110, Var(Y(p,z))>335, kappa_3(Y(p,z))<-567.
For every q>=12 for which the original marked-action sampling law is defined,
kappa_3(T_q)/q < -567 q^2-1005q+110 <0.
In particular, actual slots q=12,24 have negative third cumulant on a *nonzero-area closed rectangle*, not just at a parameter point. The rectangle contains an open neighborhood of that point.

## General all-order coupling lemma

Let N=189. In the frozen model each direction's stopping decision is a deterministic functional of its first N Bernoulli marks (survivor row extinction at layer N). Two directions have independent unit-rate Poisson arrival clocks, independent of marks. Write Y(p,z) for their stopping-time maximum, and m_r(p,z)=E[Y(p,z)^r]. For every pair of admissible parameter points and each integer r>=1,
|m_r(p,z)-m_r(p',z')| <= 2 N (N)_r (|p-p'|+|z-z'|),
where (N)_r=N(N+1)...(N+r-1). Also m_r<=2(N)_r and m_1<199 uniformly.

Proof: Couple both parameter settings using the same N independent uniform random marks for each direction, thresholded respectively at p,p' and z,z'; use the same independent Poisson clocks for each setting. The event E of any disagreement among 2N thresholded marks has probability at most N(|p-p'|+|z-z'|) by a union bound, and is independent of the Poisson clocks. Off E the complete stopping decisions agree, hence the two Y variables agree. Let G1,G2 be the Nth arrival times of the respective clocks, independent Gamma(N,1), and M=max(G1,G2). Both stopping times lie in [0,M]. Thus
|Y(p,z)^r-Y(p',z')^r| <= M^r 1_E.
Taking expectations and using M^r<=G1^r+G2^r, E G_i^r=(N)_r, proves the Lipschitz inequality. Finally,
E M = N + E|G1-G2|/2 <= N + sqrt(Var(G1-G2))/2 = N+sqrt(N/2)<199,
since N=189<200. QED.

## Third-cumulant estimate

With m1=m_1, m2=m_2, m3=m_3:
W=m2-m1^2; C3=m3-3m2 m1+2m1^3.
From the coupling lemma, exact integer constants for the first three raw moments are
L1=71442, L2=13573980, L3=2592630180.
Moreover m1<199 and m2<=71820.

If delta=|p-p'|+|z-z'|, product-difference bounds give
|W-W'| <= [L2+2(199)L1]delta=42007896 delta,
|C3-C3'| <= [L3+3(71820 L1+199 L2)+6(199)^2 L1]delta
             =43064237412 delta.

In the closed theorem rectangle delta<=2h=1/67108864. Exact rational arithmetic yields:
71442 delta <1,
42007896 delta <1,
43064237412 delta <642.
Apply the strict PREFIX-645 point bounds:
m1<109+1=110; W>336-1=335; C3<-1209+642=-567.

The exact all-order Poisson/native index conversion from PREFIX-645 therefore gives
kappa_3(T_q)/q = q^2 C3-3q W +m1 < -567q^2-1005q+110.
For q>=12 the upper-bound polynomial is strictly negative and strictly decreasing (derivative -1134q-1005). QED.

## Exact verification and scope

Companion Python integer/Fraction certificate checks the constants, strict perturbation margins and q-polynomial sign. Output is ALL_CHECKS_PASS. Companion JSON records exact rational perturbation bounds. The certificate checks a newly proved implication from PREFIX-645's exact finite witness; it does not rerun 189-layer survivor rows or the underlying 96-port native dynamics.

Model and source: frozen science pin f42f2906d77f24085c123f3ccfe9667d41caa96d; PREFIX-645 paper and executable witness at f11c0345bf89321aba48d90671c244bdec25d416. Typed BRC carrier: signed prefix-count Bernoulli mark paths retaining complete branch/mark history through N=189. The readout is a two-direction first-stop index and Poissonized time; no physical phase or full native 96-port transfer is asserted. This theorem does not determine third-cumulant sign on the full [3/20,1/6] x [37/256,39/256] valley strip.

Next discriminating unit: replace the coarse global union-bound moment Lipschitz estimates by local Bernstein/score-function interval certificates, enlarge the sign-stable rectangle, then resolve the sign boundary or produce an exact sign-change witness on the full valley strip. The mother target remains the two-parameter sampling-variance global maximum. The present contribution carries no formal Result or review admission.
