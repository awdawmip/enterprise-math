# R5 — Exact coefficient period including the linear term at threshold m=1

Date: 2026-11-23 (Asia/Shanghai). Status: **AUTHOR_EXACT_CYCLOTOMIC_PROOF / VERIFIED_FINITE_FIELD_WITNESSES / NOT_REVIEWED**. This is an independent portable scientific result, not a canonical Task Result or a native X6 dynamics result.

Frozen scientific input (unchanged): `awdawmip/enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15`, the corrected genuine-intersection five-event scalar counting observer. Prior immutable scope comparison: `@c27732cc27700ab4e65268acdf4a285cbdf910f6:research_notes/portable_direct/r5_m1_o1_exact_period_20261122/RESEARCH.md` determined the degree-\(\ge2\) period (discarding an \(O(N)\) remainder). Here **we retain the coefficient of N**, obtaining a different, strictly larger period.

## Exact theorem

Let \(\mathbf a=(a_{214},\ldots,a_{314})\in\mathbb Z_{\ge0}^{101}\), with cost \(N=\sum_{p=214}^{314}p\,a_p\). At threshold \(m=1\), define five failure events \(\sum_{p\in S_i}a_p<1\), with supports
\[
\begin{aligned}
S_0&=\{214,215,216,217,218\},\\
S_1&=\{214,216,217,218,219,220,221\},\\
S_2&=\{215,216,217,218,219,220,221\},\\
S_3&=\{223,\ldots,290\},\quad S_4=\{296,\ldots,312\}.
\end{aligned}
\]
Let \(f_1(N)\) count configurations of cost \(N\) satisfying **at least one** failure event. It is a quasipolynomial; denote by \(M_1^{(\ge1)}\) the least common positive period of all coefficient functions of \(N^j\) with \(j\ge1\). The constant coefficient function is discarded (an \(O(1)\) remainder). Then
\[
\boxed{M_1^{(\ge1)}=814\,202\,665\,467\,037\,976\,682\,352\,800.}
\]
The value is attained, not merely an upper bound. Moreover, for **every** threshold \(m\ge1\) of this frozen model,
\[
 M_m^{(\ge1)}\mid \Lambda_1
 =814\,202\,665\,467\,037\,976\,682\,352\,800,
\]
where \(M_m^{(\ge1)}\) uses the same degree-\(\ge1\) observer; this universal upper bound needs no prior all-threshold cancellation theorem.

## Rational-function upper bound

Put \(D(q)=\prod_{p=214}^{314}(1-q^p)\). For \(m=1\), all multiplicities supported on any failed set must vanish, so genuine simultaneous intersections are encoded by the **union**, not the sum of separate prices:
\[
R_1(q)=\sum_{\emptyset\neq I\subseteq\{0,1,2,3,4\}}(-1)^{|I|+1}
  \prod_{p\in U_I}(1-q^p),\qquad
U_I=\bigcup_{i\in I}S_i,
\]
and \(F_1(q)=\sum_{N\ge0}f_1(N)q^N=R_1(q)/D(q)\).
For other \(m\), the numerator remains a polynomial since each simultaneous finite multiplicity cutoff leaves a finite sum over the corresponding union supports. Hence all \(F_m\) share the denominator \(D\).

For each \(d\ge1\), at any primitive \(d\)-th root, the denominator has vanishing order
\[
n_d=\#\{p:214\le p\le314,\ d\mid p\}
=\big\lfloor314/d\big\rfloor-\big\lfloor213/d\big\rfloor.
\]
A pole of order at most one contributes only a bounded root-of-unity wave, i.e. a degree-0 quasipolynomial term. Thus coefficient terms of degree \(\ge1\) can only involve orders \(d\) with \(n_d\ge2\). Exact finite integer enumeration (\(1\le d\le314\)) yields
\[
\Lambda_1=\operatorname{lcm}_{n_d\ge2}d
=814202665467037976682352800.
\]
Every coefficient-period \(M_m^{(\ge1)}\) therefore divides \(\Lambda_1\).

For comparison, the degree-\(\ge2\) denominator envelope is
\[
\Lambda_2=\operatorname{lcm}_{n_d\ge3}d
=229746052653717600,\qquad
\Lambda_1/\Lambda_2=3543924503=7\cdot41\cdot47\cdot59\cdot61\cdot73.
\]
The extra factor 7 arises from order 49, not order 7 alone.

## Matching lower bound by 18 exact independent finite-field witnesses

For each table row, \(p\) is verified prime, \(d\mid p-1\), and \(z\in\mathbb F_p^\times\) has **exact multiplicative order \(d\)**. The entry \(v\) is the **nonzero** exact residue \(R_1(z)\bmod p\), computed both by all 31 literal inclusion/exclusion masks and independently by the disjoint-block factorization \(R_1=1-(1-A)(1-B)(1-C)\), where \(A\) is the union of the first three overlapping events and \(B,C\) are the disjoint long-block events.

| d | n_d | p | z | R1(z) mod p |
|---:|---:|---:|---:|---:|
| 32 | 3 | 97 | 28 | 59 |
| 54 | 2 | 109 | 36 | 95 |
| 25 | 4 | 101 | 16 | 84 |
| 49 | 2 | 197 | 16 | 31 |
| 11 | 9 | 23 | 4 | 14 |
| 13 | 8 | 53 | 16 | 41 |
| 17 | 6 | 103 | 64 | 71 |
| 19 | 5 | 191 | 69 | 103 |
| 23 | 4 | 47 | 4 | 20 |
| 29 | 3 | 59 | 4 | 58 |
| 62 | 2 | 311 | 264 | 231 |
| 37 | 3 | 149 | 16 | 106 |
| 41 | 2 | 83 | 4 | 31 |
| 43 | 3 | 173 | 16 | 35 |
| 47 | 2 | 283 | 64 | 196 |
| 59 | 2 | 709 | 551 | 360 |
| 61 | 2 | 367 | 64 | 238 |
| 73 | 2 | 293 | 16 | 117 |

Why this certifies characteristic-zero nonvanishing: \(R_1(q)\in\mathbb Z[q]\). If it vanished at a complex primitive \(d\)-th root, the monic cyclotomic polynomial \(\Phi_d(q)\in\mathbb Z[q]\) would divide \(R_1(q)\) in \(\mathbb Z[q]\). Reduction mod \(p\) would then force \(R_1(z)=0\) at **every** primitive order-\(d\) root in \(\mathbb F_p\), contradicting the table. Thus \(R_1\) is nonzero at all complex primitive \(d\)-th roots of each selected order.

Since \(n_d\ge2\), the poles of \(F_1\) at these primitive roots have order \(\ge2\). A nonzero degree-\(\ge1\) exponential-polynomial term of frequency a primitive \(d\)-th root forces \(d\) to divide any period of the coefficient functions of degrees \(\ge1\); distinct roots cannot cancel each other's exponential-polynomial contributions. The selected orders have
\[
\operatorname{lcm}(32,54,25,49,11,13,17,19,23,29,62,37,41,43,47,59,61,73)=\Lambda_1.
\]
Hence \(\Lambda_1\mid M_1^{(\ge1)}\), completing equality with the upper bound.

This proof uses finite fields to **disprove cyclotomic divisibility**, not to infer that characteristic-zero vanishing follows from finite-modular zeroes. Exact data plus the root-of-unity partial-fraction theorem supply the infinite-in-\(N\) conclusion.

## Verification and boundaries

The companion `VERIFY_M1_LINEAR_PERIOD.py` reconstructs every table value with two distinct exact modular expressions, checks all moduli are prime and roots of exact prescribed order, enumerates every denominator root order up to 314, and validates both least common multiples. Executed in a local Python 3 standard-library environment:
```text
PASS: 18/18 primitive nonzero finite-field witnesses, double independent event formulas
Lambda_1 = 814202665467037976682352800; Lambda_2 = 229746052653717600; ratio=3543924503
```
No floating-point approximation is used.

The proof is for the frozen **scalar partition-cost observer**; it does not assert an unproved native X6 embedding, BRC phase-cancellation representation, a heartbeat dynamical law, a formally accepted Result or an independent Review. Native X6/P000 and the ACTIVE worldview are unchanged; signed cyclotomic phases must be retained for this observer, since a positive-mass-only reduction could lose cancellation information.

## New research question

For all \(m\ge1\), classify \(M_m^{(\ge1)}\) by identifying threshold-dependent vanishing and nonvanishing for the new order-\(\ge2\) frequencies, notably orders 49,41,47,59,61,73 as well as order 54 and 62. Reuse the 43-adic first-jet all-\(m\) conclusion at immutable `enterprise-math@d2545049efd91c126fb928ad2f0187f7e9ebd390` within its exact seven cancellation classes. A subsequent task is to give an observer-preserving bridge from scalar frequency/jet data to typed BRC or X6 native states, if such a map is constructible.

Contribution: independent author-side calculation on an informed frozen scientific input. Historical R5 author/activity IDs remain provenance and do not certify this Sites runtime's identity. No formal CLAIM/RUN has been invoked in this contribution.
