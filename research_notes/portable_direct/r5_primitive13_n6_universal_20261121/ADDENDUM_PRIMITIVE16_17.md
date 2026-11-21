# R5 addendum — primitive 17 threshold classes, primitive 16 at m=1, and cost period 12,252,240

Date: 2026-11-21. Frozen nonadaptive 256-hypothesis, 101-price scalar cost model; exact author-side calculation, NOT_REVIEWED. Continuation of the primitive-13 N^6 result in this directory.

## Primitive 17: complete degree-five threshold classification

Let z be a primitive 17th root, and P17=221*238*255*272*289*306. Among 214..314 exactly these six prices are divisible by 17. Event S0={214,215,216,217,218} is the only one of the five minimal event sets which avoids all six; every other event and all its intersections leave at most five unrestricted 17-multiples. Consequently its local finite polynomial determines the complete order-six pole:

\[
B_m^{17}(z)=\sum_{a_1,\ldots,a_5\ge0,\ \sum_i a_i<m}z^{214a_1+215a_2+216a_3+217a_4+218a_5}.
\]
\[
F_m^{(17)}(N)=\frac{N^5}{5!\,P17}\sum_{\operatorname{ord}(z)=17}
H17(z)\,B_m^{17}(z)\,z^{-N}+O_m(N^4),
\quad
H17(z)=\prod_{219\le p\le314,\ 17\nmid p}(1-z^p)^{-1}.
\]

The *all-threshold exact rational identity* is

\[
\boxed{\sum_{m\ge1}B_m^{17}(z)t^{m-1}=
\frac{\prod_{r\in\{1,2,3,4,5,6,7,8,9,15,16\}}(1-z^rt)}
{1-t^{17}}.}
\]

Proof: finite-m threshold tail summation gives 1/[(1-t)prod_{r=10}^{14}(1-z^r t)], and the 17th-root cyclotomic identity product_{r=0}^{16}(1-z^r t)=1-t^17 gives the displayed quotient. The numerator has degree 11; all its 12 coefficients are nonzero in Z[z]/Phi17(z). Exact nonzero basis witnesses (index,value) for coefficient j=0,...,11 in basis 1,z,...,z^15 are:

(0,1), (0,1), (0,1), (0,2), (1,-1), (0,-1), (0,1), (3,-1), (0,-1), (1,-1), (8,-1), (8,-1).

These are complete finite polynomial coefficients, not threshold samples. Thus

\[
\boxed{B_m^{17}(z)\ne0\iff m\bmod17\in\{1,\ldots,12\},\qquad B_m^{17}(z)=0\iff m\bmod17\in\{0,13,14,15,16\}.}
\]

The conclusion applies to each primitive 17th root by Galois conjugation. For m=1, B_1=1, so a nonzero degree-five 17-cycle definitely occurs.

## Primitive 16 at m=1: exact inclusion-exclusion coefficient

Let z be primitive of order 16, P16=224*240*256*272*288*304, and H16(z)=product over 222<=p<=314, 16 not dividing p, of (1-z^p)^(-1). Exactly seven inclusion-exclusion masks reach pole order six: all nonempty subsets of S0,S1,S2, because they avoid those six multiples; S3 and S4 constrain at least one multiple. At m=1 an event freezes all multiplicities on its set to zero. Factoring H16/P16 and combining these seven masks, the coefficient is

\[
A16(z)=\frac1{(1-z^{219})(1-z^{220})(1-z^{221})}
+\frac1{1-z^{215}}+\frac1{1-z^{214}}-2.
\]

Reducing exactly modulo Phi16(z)=z^8+1 yields

\[
\boxed{A16(z)=z^7-z^4+\frac12z^3+\frac12z-1\ne0.}
\]

The remaining 16th-root contribution therefore has a genuine degree-five term:

\[
F_1^{(16)}(N)=\frac{N^5}{5!\,P16}\sum_{\operatorname{ord}(z)=16}
H16(z)\,A16(z)\,z^{-N}+O(N^4).
\]

The identity is checked two ways: direct formula and the seven actual maximal-pole inclusion-exclusion masks in exact Q[z]/(z^8+1). Nonzero at all primitive roots follows from field automorphisms.

## Sharp new cost period at m=1 and remainder O(N^4)

The preceding theorem in this directory requires the factor 360360 at remainder O_1(N^5). The two independent nonzero harmonics here force a 16th-root factor (one extra factor two beyond the existing 2^3) and a new prime factor 17, giving

\[
\operatorname{lcm}(360360,16,17)=12\,252\,240.
\]

For every order d>=19, at most five prices in 214..314 are divisible by d, so such root contributions are O(N^4). For d=15,16,17,18 the pole order is at most six, and all d<=18 divide lcm(1,...,18)=12,252,240. Thus a quasipolynomial of this period exists through degree five and the Fourier lower bound is sharp:

\[
\boxed{M_1(\text{remainder }O(N^4))=12\,252\,240.}
\]

The full all-m classification at this accuracy remains open: the 16th-root order-six coefficient requires its own threshold analysis; in five 17-residue classes the order-six pole vanishes and the next Laurent order requires separate investigation.

## Verification and status

VERIFY_16_17.py uses only Python standard-library exact fractions, the degree-eight Phi16 ring and degree-sixteen Phi17 ring. It checks the seven inclusion-exclusion masks independently, validates the full twelve-term numerator and all basis witnesses, crosschecks threshold m=1..34 by independent local DP, verifies root pole counts for orders 16 and 17, and verifies all order d>=19 upper bounds. The local exact run returned PASS.

Independent scientific review: NOT_REVIEWED. Formal Task CLAIM/Result: not issued. Scalar cost-observer proof only, no unverified transport to P000 X6 dynamics.

Next: classify primitive 16th-root order-six contributions for all positive m and primitive 17th-root degree-four contributions in the five leading-order cancelling classes, then determine sharp universal or residue-dependent minimum moduli at O_m(N^4).
