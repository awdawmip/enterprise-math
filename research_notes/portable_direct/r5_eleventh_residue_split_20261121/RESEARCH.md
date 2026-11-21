# R5 — Primitive eleventh-root threshold switch: the first split in the least cost-period staircase

Date: 2026-11-21. Scope: frozen scalar nonadaptive R5. Evidence: AUTHOR_EXACT_DERIVATION / EXACT_FINITE_CHECKED / NOT_REVIEWED. Independent portable mathematical contribution; no authenticated formal TASK CLAIM/RUN, Result or Review.

## Frozen source and previously verified frontier

The R5 inputs are 256 labeled hypotheses, integer price types 214–314 and frozen 32,640-pair separation certificate (SHA256 \`50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b\`). Five minimal separation subsets are

\[
S_0=\{214,215,216,217,218\},\;
S_1=\{214,216,217,218,219,220,221\},\;
S_2=\{215,\ldots,221\},\;
S_3=\{223,\ldots,290\},\;
S_4=\{296,\ldots,312\}.
\]

For each fixed positive integer threshold m, F_m(N) counts nonnegative price-multiplicity vectors with total cost N for which at least one separation subset has multiplicity load less than m.

Pinned earlier results: [primitive seventh all m](https://github.com/awdawmip/enterprise-math/blob/1482e3a06ae5c2e6a8e18120d3aca48f95645c75/research_notes/portable_direct/r5_seventh_allm_20261121/RESEARCH.md) and [octic/nonic branch](https://github.com/awdawmip/enterprise-math/tree/025d3b5e2779f97670cb6adac4f9ba9fdda6689b/research_notes/portable_direct). The latter establishes a least cost quasipolynomial modulus of 2520 for every fixed m at remainder O_m(N^8).

## Theorem A — exact primitive-eleventh leading coefficient and zero classification

For any primitive eleventh root z, define

\[
P_{11}=\prod_{j=0}^{8}(220+11j),\qquad
H_{11}(z)=\prod_{\substack{219\le p\le314\\11\nmid p}}(1-z^p)^{-1}.
\]

Let

\[
B_m(z)=\sum_{\substack{a_5,\ldots,a_9\ge0\\a_5+\cdots+a_9<m}}
z^{5a_5+6a_6+7a_7+8a_8+9a_9}.
\]

For every fixed m, the order-nine Laurent coefficient at each primitive eleventh root is \(H_{11}(z)B_m(z)/P_{11}\), and the degree-eight Fourier contribution is

\[
\boxed{F_m^{(11)}(N)=\frac{N^8}{8!P_{11}}\sum_{\Phi_{11}(z)=0}
H_{11}(z)B_m(z)z^{-N}+O_m(N^7).}\tag{1}
\]

The coefficient has the exact threshold-generating function

\[
\begin{aligned}
\sum_{m\ge1}B_m(z)t^{m-1}
&=\frac1{(1-t)(1-z^5t)(1-z^6t)(1-z^7t)(1-z^8t)(1-z^9t)}\\
&=\boxed{\frac{(1-zt)(1-z^2t)(1-z^3t)(1-z^4t)(1-z^{10}t)}
{1-t^{11}}.}\tag{2}
\end{aligned}
\]

The second equality uses \(\prod_{r=0}^{10}(1-z^rt)=1-t^{11}\), without any approximation. The numerator has degree five, which implies the **exact universal classification**

\[
\boxed{B_m(z)\ne0\iff m\bmod11\in\{1,2,3,4,5,6\};\qquad
B_m(z)=0\iff m\bmod11\in\{7,8,9,10,0\}.}\tag{3}
\]

Indeed let \(Q_j(z)=[t^j]\prod_{r\in\{1,2,3,4,10\}}(1-z^rt)\). Then \(B_m(z)=Q_{(m-1)\bmod11}(z)\); \(Q_j=0\) for j=6,..,10. Each of the six remaining coefficients is nonzero in the canonical basis 1,z,...,z^9, with exact vectors

\[
\begin{array}{c|l}
j & Q_j \text{ in the }(1,z,\ldots,z^9)\text{ basis}\\\hline
0&(1,0,0,0,0,0,0,0,0,0)\\
1&(1,0,0,0,0,1,1,1,1,1)\\
2&(1,1,1,2,1,2,1,1,0,0)\\
3&(0,0,-1,-1,-2,-1,-2,-1,-1,-1)\\
4&(-1,-1,-1,-1,-1,0,0,0,0,-1)\\
5&(0,0,0,0,0,0,0,0,0,-1)
\end{array}
\]

Consequently \(B_{m+11}=B_m\) for every m>=1, and the least threshold coefficient period is exactly 11. In the five cancelling residue classes, the apparent order-nine pole is absent (primitive-eleventh contribution is at most order eight).

### Why no other failure event contributes to the order-nine pole

Exactly nine prices in 214–314 are divisible by 11: 220,231,242,253,264,275,286,297,308. None belongs to S_0, so S_0 alone contributes order nine. S_1 and S_2 both include 220; S_3 includes 231,..,286; S_4 includes 297 and 308. Thus every intersection containing any event other than S_0 constrains at least one of the nine multiples, and is of pole order at most eight. The S_0 load is the sum of five multiplicities with residues 5,6,7,8,9, yielding (1). The remaining free nonmultiples contribute the nonzero H_11 factor.

## Theorem B — split sharp modulus at the next precision

For fixed m>=1, retain all terms through degree N^8, i.e. permit only remainder \(O_m(N^7)\). At this precision, an order-d root with d>=12 cannot produce degree-eight terms: order d=12 has at most nine multiples in the price interval, but price 216 is constrained by each of the S_0,S_1,S_2 events, and the remaining events constrain several more, leaving at most eight free multiples. For d>=13 there are at most eight multiples in the entire price interval.

All roots of order at most ten are already represented by a cost period dividing 2520. Thus the only new possible prime factor at degree N^8 is 11, and Theorem A says exactly when it is present. We obtain the following exact piecewise least periods:

\[
\boxed{
\text{Least cost quasipolynomial period at }O_m(N^7)=
\begin{cases}
27720=\operatorname{lcm}(2520,11),&m\bmod11\in\{1,2,3,4,5,6\},\\
2520,&m\bmod11\in\{7,8,9,10,0\}.
\end{cases}}\tag{4}
\]

This is the first documented **threshold-residue bifurcation** of the R5 cost-period staircase: a genuine harmonic cancels in exactly five of eleven threshold classes. An example is m=7, where the eleventh-root N^8 coefficient vanishes; m=6 has a nonzero coefficient \(-z^9\). Both preserve the predecessor 2520 harmonic content. No claim is made that the complete exact counting function has either small period.

## Verification and continuation

\`python3 VERIFY_ELEVENTH.py\` uses only integer tuples in the exact field \(\mathbb Q[z]/(1+z+\cdots+z^{10})\). It calculates the 11 threshold residue classes, checks 33 periodic recurrence instances, and independently enumerates all five local multiplicities with total load below m for m=1..12. The program verifies six nonzero classes and five identically zero classes. The code and \`ELEVENTH_RESULT.json\` preserve exact basis vectors and test coverage. This is an exact mathematical derivation with author-side verification, independent scientific review NOT_REVIEWED.

The 11-periodic Fourier coefficient is a typed scalar combinatorial observer; transporting it to P000's native six-dimensional cell structure requires a separate proven observer-preserving bridge. No such X6 or BRC physical claim arises from the finite-period identity.

Next: classify the order-eight primitive-eleventh contribution in the five cancelling classes and the order-13 and higher roots at the following precision. Determine whether the least period 27720 becomes universal once the N^7 term is included.
