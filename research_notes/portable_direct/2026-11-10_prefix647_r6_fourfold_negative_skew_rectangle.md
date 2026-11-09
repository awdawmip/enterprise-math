# PREFIX-647-R6 — Fourfold expansion of negative third-cumulant rectangle

Date: 2026-11-10 (Asia/Shanghai). Research mode: independent TASK_RESEARCH, no formal shared CLAIM. Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d. Status: AUTHOR_DERIVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Scientific question

PREFIX-645 (enterprise-math@f11c0345bf89321aba48d90671c244bdec25d416) precisely certified the signed two-informative-direction BRC first-stop statistical observer at (p0,z0)=(1/6,19/128):
E[Y0]<109; 336<Var(Y0)<337; kappa_3(Y0)<-1209.

PREFIX-646 (enterprise-math@d64c99d8e6ea82f6c1d803df9f93b91e70eaf7b0) proved a negative-third-cumulant rectangle of coordinate half-width 2^(-27), using a global second raw-moment bound of 71820. This iteration replaces that global cap by a strictly tighter local envelope inherited from the exact central-point witness.

BRC carrier: the original pair of signed prefix-count Bernoulli mark histories through N=189 informative arrivals, with two independent unit-rate Poisson clocks. Observer: maximum first-stop time Y, action stopping index T_q, and their cumulants. Preserved future operations: the original independent mark thinning, Poissonization and cumulant evaluation; the branch identity, multiplicity and signed source provenance are unchanged.

## Theorem 647.1

For every admissible pair of Bernoulli parameters satisfying
|p-1/6| <= 2^(-25) and |z-19/128| <= 2^(-25),
the frozen BRC statistical observer satisfies

E[Y(p,z)] < 110,
Var(Y(p,z)) > 334,
kappa_3(Y(p,z)) < -322.

For every real q >= 12 for which the marked sampling law is defined, its discrete stopping count T_q satisfies

kappa_3(T_q)/q < -322 q^2 - 1002 q + 110 < 0.

In particular q=12 and q=24 have negative third cumulants throughout the closed rectangle. The certified coordinate half-width is four times that of PREFIX-646; the certified area is sixteen times as large.

## Proof

Let m_r=E[Y^r] and delta=|p-p0|+|z-z0|. At the stated rectangle delta<=2^(-24). Reuse PREFIX-646's common-uniform-mark and Gamma-arrival coupling lemma: for every positive integer r,

|m_r(p,z)-m_r(p0,z0)| <= L_r delta, with L_r=2N (N)_r.

The rising factorial uses N=189. For r=1,2,3 the exact coefficients are L1=71442, L2=13573980, L3=2592630180.

At the center m2=W+mu^2<337+109^2=12218. The exact rational inequalities

L1*2^(-24)=35721/8388608<1,
L2*2^(-24)=3393495/4194304<1

therefore imply, at the center and throughout the rectangle, mu<110 and m2<12219. This sharper LOCAL second-moment envelope is the key difference from PREFIX-646.

For any two endpoints of the segment from the center to a parameter point, using the bound on m1 gives the product-difference inequality

|W-W0|=|m2-m1^2-(m2_0-m1_0^2)|
 <= (L2+2*110*L1)*delta
 = 29291220*delta.

Similarly C3=m3-3*m2*m1+2*m1^3, with the same endpoint bounds, obeys

|C3-C3_0| <= [L3+3*(12219*L1+110*L2)+6*110^2*L1]*delta
 = 14877582174*delta.

The exact certificate verifies the strict comparisons

29291220*2^(-24)=7322805/4194304<2,
14877582174*2^(-24)=7438791087/8388608<887.

It follows that W>336-2=334 and C3<-1209+887=-322. The mean is already bounded by 110.

By the exact all-order transform from PREFIX-645,
kappa_3(T_q)=q^3 C3 -3q^2 W +q*mu.
Divide by q>0 and use the strict local bounds:
kappa_3(T_q)/q < -322q^2-1002q+110.
At q=12 this polynomial is -58282; its derivative -644q-1002 is negative on q>=12. Hence the polynomial, and kappa_3(T_q), are strictly negative for every valid real q>=12. QED.

## Exact author certificate

Companion file PREFIX647_R6_LOCAL_MOMENT_ENVELOPE_CERTIFICATE.py runs using only standard-library exact integers and fractions.Fraction. Its output is ALL_CHECKS_PASS. It regenerates PREFIX647_R6_RESULTS.json containing the tested rational margins, half-width and dependency pins. It tests the mathematical implication under the strict PREFIX-645 point witness, using PREFIX-646's proven all-order coupling lemma. Neither the 189 survivor-layer exact witness nor the original 96-port native dynamics were reexecuted for this increment.

All displayed rectangle coordinates remain strictly within the Bernoulli probability domain (0,1). When reusing the result on the earlier restricted valley slice p<=1/6, take the intersection; the sign bounds persist.

## Next discriminating research step

Derive local Bernstein/score-function bounds for the **centered** third moment rather than taking a union bound on three raw moments. Attempt a certified 2D bisection covering a larger portion of [3/20,1/6] x [37/256,39/256]. Either a positive lower sign certificate or an exact sign-change counterexample will settle the corresponding local universal-sign claim. This side result contributes distributional structure to the mother problem: globally maximizing sampled stopping-time variance over the frozen two-parameter observer.

Formal source CLAIM/Result/Review not created; no independent mathematical review.
