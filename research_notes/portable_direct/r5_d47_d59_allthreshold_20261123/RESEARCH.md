# R5 — Exact all-threshold 47- and 59-primary linear coefficient periods

2026-11-23 (Asia/Shanghai). **AUTHOR_EXACT_PROOF / FINITE_FIELD_WITNESS / NOT_REVIEWED**. This is independent portable research, not a CLAIM, native Result/Review, or X6/BRC theorem.

Frozen science: awdawmip/enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15.
Predecessor: a225d60b94c73f12de03337a08492388f95cace2:research_notes/portable_direct/r5_d61_allthreshold_mod122_20261123/RESEARCH.md

## Input and theorem

Nonnegative item multiplicities occur at every integer price 214..314. The five failure supports are S0=214..218, S1={214,216,217,218,219,220,221}, S2={215,216,217,218,219,220,221}, S3=223..290, S4=296..312. Each failure means fewer than m items on that support, for m a positive integer. The union has generating function F_m(q)=R_m(q)/D(q), where D(q)=product over p=214..314 of (1-q^p), and R_m is an integer polynomial. M_m^(>=1) is the strictly least common period of the quasipolynomial **coefficient functions of degrees at least one**, not the period of F_m(N) itself.

**Theorem (all positive integer m).** For any primitive complex root ζ_d of the indicated order,

\[
R_m(\zeta_{47})=0\quad\Longleftrightarrow\quad m\bmod94\in\{0,90,91,92,93\},
\]

\[
R_m(\zeta_{59})=0\quad\Longleftrightarrow\quad m\bmod118\in\{0,114,115,116,117\}.
\]

Consequently the exact prime-primary period valuations are

\[
v_{47}(M_m^{(\ge1)})=\begin{cases}0&m\bmod94\in\{0,90,91,92,93\}\\1&\text{otherwise,}\end{cases}
\qquad
v_{59}(M_m^{(\ge1)})=\begin{cases}0&m\bmod118\in\{0,114,115,116,117\}\\1&\text{otherwise.}\end{cases}
\]

The characteristic-zero vanishing directions follow from rational-function pole degrees. The converse uses integer-exact finite-field **nonzero** witnesses, not finite-field zero tests.

## Joint-load preserving formula

Let A_m be the normalized union numerator of overlapping S0,S1,S2, and B_m,C_m the normalized singleton numerators of the disjoint S3,S4 blocks. Inclusion/exclusion across the three disjoint blocks gives

\[
R_m=A_m+B_m+C_m-A_mB_m-A_mC_m-B_mC_m+A_mB_mC_m.
\]

For d=47, S3 includes 235 and 282; for d=59, S3 includes 236. These prices are divisible by d. Since the correct singleton numerator is a product of (1-q^p) on its support multiplied by a finite complete-homogeneous prefix, B_m(ζ_d)=0 for every m. Thus at either primitive root R_m=A_m+C_m-A_mC_m.

Write a=n214, b=n215, c=n216+n217+n218, e=n219+n220+n221. Then the exact overlapping minimum load is

\[
\min(a+b+c,a+c+e,b+c+e)=c+a+b+e-\max(a,b,e).
\]

Set α=ζ^214, β=ζ^215, γ_j=ζ^j (j=219,220,221), K=∏_{p=214}^{221}(1−ζ^p), and H_c(t)=∏_{p=216}^{218}(1−tζ^p)^{-1}. Distinct γ_j permit exact partial fractions

\[
h_e(\gamma_{219},\gamma_{220},\gamma_{221})
=\sum_{j=219}^{221}\kappa_j\gamma_j^e,\quad
\kappa_j=\frac{\gamma_j^2}{\prod_{k\ne j}(\gamma_j-\gamma_k)}.
\]

Partition (a,b,e) into six integer gap cones, ordered from largest to smallest with fixed tie priority a,b,e. For permutation π=(top,middle,bottom), let e1=1 if top has lower tie priority than middle; e2=1 if middle has lower tie priority than bottom; otherwise each is zero. Arrange α,β,γ_j as u1,u2,u3 in that order. The exact cone series is

\[
\frac{u_1^{e_1}(u_1u_2t)^{e_2}}
{(1-u_1)(1-u_1u_2t)(1-u_1u_2u_3t^2)}.
\]

The threshold m > minimum load contributes the factor t/(1−t). Hence

\[
G_A(t):=\sum_{m\ge0}A_m(\zeta)t^m
=\frac{Kt}{1-t}H_c(t)\sum_{j=219}^{221}\kappa_j
\sum_{\pi\in S_3}
\frac{u_1^{e_1}(u_1u_2t)^{e_2}}
{(1-u_1)(1-u_1u_2t)(1-u_1u_2u_3t^2)}.
\]

No constant 1−u1 or γ_j−γ_k vanishes for primitive roots of either order. This formula counts the exact overlapping load; replacing S0,S1,S2 by independent events would be incorrect.

## Order 47: exact characteristic-zero 94-periodicity

All poles in t belong to the 94th roots. With t=ζ47^r for positive roots, the poles are: threshold r={0}; c-group r={17,18,19}; pair r={34,35,36,37,41}; triple r={4,5,28}, plus their negative partners −ζ47^r. These sets are disjoint, and since 47 is odd negative partners cannot collide with positive ones. Thus all poles are simple.

At infinity H_c=O(t^{-3}), t/(1−t)=O(1), and each cone term is O(t^{e2−3}) with e2≤1. Therefore G_A=O(t^{-5}). It follows in the cyclotomic field that

\[
G_A(t)=Q_{47}(t)/(1-t^{94}),\qquad \deg Q_{47}\le89.
\]

Consequently A_{m+94}=A_m for all m≥1 and A_m=0 at residues m mod94 in {0,90,91,92,93} in characteristic zero.

## Order 59: cancellation of the apparent double pole

Positive t-pole exponents at order 59 are: threshold {0}, c-group {18,19,20}, pair {36,37,38,39,43}, triple {0,29,30}; the three negative triple poles are separate. The only coincidence is t=1: the threshold pole coincides with the j=220 triple pole since 214+215+220=649=11·59.

Inside the **sum of all six** sorting-cone terms for j=220 this collision cancels. Put a=α, b=β and γ220=1/(ab). After removing the common 1−t² denominator and evaluating the remaining numerator at t=1, the six rational terms sum to

\[
2\left[
\frac1{(a-1)(ab-1)}
+\frac b{(b-1)(ab-1)}
-\frac1{(a-1)(b-1)}
\right]=0.
\]

All displayed denominators are nonzero. Thus the j=220 cone sum has a factor 1−t, cancelling the t=1 part of its 1−t² denominator, leaving at most a pole at t=−1. The **outer threshold factor** still yields only one simple pole at t=1. Every remaining pole is distinct and among the 118th roots.

Using the same infinity estimate gives

\[
G_A(t)=Q_{59}(t)/(1-t^{118}),\qquad\deg Q_{59}\le113.
\]

Thus A_m is 118-periodic and vanishes in characteristic zero at m mod118 in {0,114,115,116,117}. The six-cone cancellation is an algebraic proof, not an inference from repeated finite-field observations.

## The correct S4 series and full R zeros

Because S4 supports precisely the 17 prices 296..312, its correct normalized threshold series is

\[
G_C(t)=\frac{t}{1-t}
\frac{\prod_{p=296}^{312}(1-\zeta^p)}
{\prod_{p=296}^{312}(1-t\zeta^p)}.
\]

For either d=47 or d=59 these 17 residues are distinct and nonzero modulo d; together with t=1, the poles are 18 distinct dth roots. Since G_C=O(t^{-17}) as t→∞,

\[
G_C(t)=Q_C(t)/(1-t^d),\qquad\deg Q_C\le d-17.
\]

Thus C_m is d-periodic and zero in characteristic zero when m mod d is any of d−16,...,d−1,0. It is therefore zero on the last five classes modulo 2d found for A_m. R_m=A_m+C_m−A_mC_m now proves all advertised vanishing directions for **every positive m**.

## Independent exact finite-field nonzero evidence

Run the included VERIFY_D47_D59.py. The program evaluates the same six-cone rational formula and the correct complete-homogeneous S4 prefix by modular polynomial series, with no floating arithmetic. It verifies primality and primitive-root order, the two cycles, the precise zero sets, and A_1 by independent seven-term inclusion/exclusion over the three original supports. Executed results:

| d | prime | primitive dth root | nonzero residues out of 2d−5 | R_1 mod prime |
|---|---:|---:|---:|---:|
| 47 | 283 | 163 | 89/89 | 5 |
| 47 | 659 | 568 | 89/89 | 229 |
| 59 | 827 | 671 | 113/113 | 472 |
| 59 | 1063 | 572 | 113/113 | 181 |

The only zeros in a complete cycle were respectively {90,91,92,93,94} and {114,115,116,117,118}, in both independent prime fields for each order. A nonzero evaluation of the integer polynomial R_m at a primitive dth root over one finite field precludes divisibility by the monic integer cyclotomic Φ_d(q); irreducibility over Q therefore proves R_m nonzero at **every** primitive complex dth root. Modular zeros by themselves are not treated as characteristic-zero zeros.

## Coefficient-period consequence and scope

Within prices 214..314 exactly two are divisible by 47 (235,282) and exactly two by 59 (236,295). Every larger multiple of either prime divides **at most one** price in this range, so can create at most a simple denominator zero and contributes no positive-degree coefficient oscillation. At primitive order 47 and 59 the denominator has exactly a double zero. Nonzero R_m yields a genuine double pole and an order-d oscillation in the linear coefficient; zero R_m removes that double pole. Together these prove the exact primary valuations above.

The result classifies two primary factors only; the full least coefficient period and remaining prime/composite-order factors are open. All calculations and proofs are author-checked, not independently reviewed. The overlapping support retains a relation/provenance-sensitive joint load, consistent with residual-fidelity; no native BRC/X6 transfer is claimed.

Next: combine the all-threshold 41,47,59,61,73 results with remaining composite-order observables and check any other colliding pole orders at exact algebraic multiplicity before using a simple-pole argument.
