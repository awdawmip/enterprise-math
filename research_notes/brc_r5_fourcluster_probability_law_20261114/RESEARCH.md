# R5 — Exact probability law and unique variance maximum for the four-cluster center-cover observer

Date: 2026-11-14. Status: author-side exact proof; **NOT_REVIEWED**.
Frozen scientific input: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Dependency: the exact 15-bit Boolean identity and 13 globally inert cut bits proved in research_notes/brc_r5_effective15_curvature_20261114/SPARSE_BOOLEAN_DECOMPOSITION.md at immutable Git commit e47ab205e5e5cdbe4ae5801d95595635fd98204c. This continuation is **conditional on that already-checked finite identity** and does not repeat its full 954-event computation.
Scope: derived 1D radius-two minimum-center-count observer D, not native X6 geometry, full BRC provenance, optimal-center configurations or fixed-budget total correction cost.

## Theorem: complete random-closure law

Let x_i be independently Bernoulli(p), 0 <= p <= 1, for all 28 original length-three cut gaps. The previously established four disjoint cluster gains, where OR/NOT have Boolean 0/1 values, are

~~~
A = (x5 OR x6) + x2*x3*x4*(NOT x5 OR x6)
B = (x8 OR x9) + x12*(x13 OR x10*x11*(x8 OR NOT x9))
C = x16
E = x25*x26*x27
D = 213 - A - B - C - E.
~~~

The other 13 cut bits have no effect on D, for any closure background. Disjointness of the four variable clusters implies that A, B, C, E are independent under the stated product distribution. Writing Y=213-D and H(z,p)=E[z^Y],

\[
H(z,p)=P_A(z,p)P_B(z,p)(1-p+pz)(1-p^3+p^3z),
\]

with P_A=A0+A1 z+A2 z^2, P_B=B0+B1 z+B2 z^2, and

~~~
A0 = 1-2p+p²-p³+2p⁴-p⁵
A1 = 2p-p²+p³-3p⁴+p⁵
A2 = p⁴
B0 = 1-2p+p³+2p⁴-3p⁵+p⁶
B1 = 2p-3p³-2p⁴+4p⁵-p⁶
B2 = 2p³-p⁵.
~~~

Consequently Pr(D=213-j) is precisely the z^j coefficient of H, for j=0,...,6. The entire seven-class law follows by four small polynomial multiplications, without enumerating 2^28 cut patterns. For **nonidentical independent** closure probabilities p_i, the same factorization holds, replacing each factor by its at-most-64-assignment local weighted truth-table polynomial. The independence hypothesis is essential: correlations between clusters need not factor.

## New exact variance theorem

Differentiation at z=1 gives the previously known mean and the new exact variance:

\[
\mathbb E D=213-5p+p^2-3p^3+3p^4-3p^5+p^6,
\]

\[
\operatorname{Var}(D)=p(1-p)Q(p),
\]
\[
Q(p)=5-5p+6p^2-4p^3+11p^4-7p^5+5p^6-6p^7+6p^8-3p^9+p^{10}.
\]

Here Var(D)=H_{zz}(1,p)+H_z(1,p)-H_z(1,p)^2, since D=213-Y. In particular Var(D)=0 at p=0 and p=1, and Var(D)=4115/4096 at p=1/2.

**Unique-maximizer theorem:** Var(D) has exactly one stationary point on 0<p<1; it is the strict global maximum, at a unique p_max satisfying

\[
0.631922 < p_{\max} < 0.631923.
\]

Numerically p_max is about 0.6319225700, and the maximum variance is about 1.0390415780. The displayed rational enclosure, rather than numerical root-finding, establishes the asserted interval.

**Proof.** Put t=p/(1-p) and V=Var(D). Differentiating the exact polynomial and multiplying by the positive factor (1+t)^11 yields

~~~
(1+t)^11 V'(t/(1+t)) =
5+35t+108t²+182t³+193t⁴+179t⁵+199t⁶
+145t⁷+18t⁸-56t⁹-35t¹⁰-9t¹¹.
~~~

The descending nonzero coefficient signs are (-,-,-,+,+,+,+,+,+,+,+,+), exactly **one** sign change. By Descartes' rule the right-hand polynomial has at most one positive root, counting multiplicity. It is positive at t=0 and tends to minus infinity, so it has one positive root. V'(0)=5 and V'(1)=-9 show this is a strict global maximum. Exact rational substitution into V' gives V'(631922/1000000)>0 and V'(631923/1000000)<0, proving the bracket. QED.

The unique **variance** maximum is different from the previously proved mean-curvature transition near 0.142932. No physical variance or full-state entropy interpretation follows from this observer theorem.

## Reproducibility and boundary

A pure-standard-library checker, VERIFY_R5_CLUSTER_LAW.py, explicitly enumerates 2^5+2^6+2^1+2^3=**106 local assignments** and expands every Bernoulli weight as an integer polynomial, checks the six displayed local factor coefficients, multiplies the four factors, verifies normalization and the complete exact mean/variance coefficients, Descartes transform and signs at the rational bracket. It also reproduces the prior fair-probability seven-class histogram

~~~
gain j=0..6: [539,4298,11404,11462,4413,624,28],
sum=32768,
E[D]=13471/64, Var(D)=4115/4096.
~~~

The checker produces EXACT_R5_CLUSTER_LAW.json. All exact arithmetic is integer or Fraction, with no floating-point acceptance. The 32,768-pattern frozen-event calculation is a **dependency** from the cited prior commit, not a new independent rerun here. Project Result/independent review and native 2,520-byte/28-coordinate/8,192-query benchmark remain pending.

**Next falsifiable question:** does any of the 13 cuts inert for minimum center count D become effective for fixed-budget optimum total correction cost J_K under some closure background? Seek the smallest exact witness; if found, a provenance-retaining min-plus block transfer must replace this coarse four-cluster observer factorization. Separately derive A/B directly from the frozen 29-block interval-cost transfer rather than Möbius enumeration.
