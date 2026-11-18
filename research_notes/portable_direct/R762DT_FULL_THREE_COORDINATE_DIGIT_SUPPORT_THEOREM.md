# R762DT — Full three-coordinate BRC ternary digit-support theorem

Date: 2026-11-18 Asia/Shanghai. Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, publication TP2-8B7E13C5904A2D6F1142. Author lineage EM-X6-3050F6, SID MCP-4b2d70a97f594366a7c94a0f8b45df38. Evidence status: symbolic author proof; finite independent author-side checker PASS; review NOT_REVIEWED.

## Frozen science and typed claim

Taskbook: awdawmip/enterprise-math@e3f42efac29a2da2d95be391f3231a664e2fade0:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md. P000 science pin: a72226e2430ffa4786321ac86e7f0c599d5f0389.

The candidate six-branch positive BRC polynomial from R762DI–DS is

\[
P(X,Y,Z)=1+X+Z+XY+YZ+XYZ.
\]

It encodes three area-residual observer variables of an explicitly selected X6 slice, NOT a replacement of native signed X6 Cell coordinates. All three observed components are retained. It is a candidate BRC observer, without a native TRIADIC_CLOSURE_E event license. Field coefficients +1/-1 modulo 3 in this note are not physical signed force amplitudes or Port provenance.

For every a>=1 let Q=3^a, and let

\[
R_a=\mathbf F_3[X,Y,Z]/(X^Q-1,Y^Q-1,Z^Q-1).
\]

Writing x=X-1, y=Y-1, z=Z-1 gives the exact isomorphism R_a = F_3[x,y,z]/(x^Q,y^Q,z^Q). Define S_a(n) to be the number of nonzero *augmentation-basis* coefficients of P^n in this algebra, with S_a^+(n) and S_a^-(n) counting coefficients equal to 1 and 2 in F_3, respectively. These counts are basis-specific: no claim about monomial-basis endpoint support follows merely from their values.

## Theorem (all powers a, exact finite-horizon support)

For any 0<=n<Q, write n in its a base-3 digits n_j in {0,1,2}, and denote by N1 and N2 the counts of digits 1 and 2. Then

\[
S_a(n)=4^{N1}10^{N2},
\quad
S_a^+(n)-S_a^-(n)=
\begin{cases}
0,&N1>0,\\
6^{N2},&N1=0.
\end{cases}
\]

Consequently S_a^±(n) are the half-sum and half-difference. For n=0, S^+(0)=1 and S^-(0)=0.

The coefficient of x^n y^0 z^n is exactly 1 for every n<Q, so P^n is nonzero in R_a. Conversely P^Q=0 and all further powers vanish. Thus the nilpotence index of the complete three-coordinate polynomial P over the characteristic-three group algebra is EXACTLY Q. In the integral group ring Z[C_Q^3], the gcd of the monomial-basis coefficients of P^n is divisible by 3 if and only if n>=Q. This establishes the first 3-divisibility threshold, not the subsequent 3-adic valuations.

## Proof

Expansion at the augmentation origin gives

\[
P(1+x,1+y,1+z)\equiv f=xz-xy-yz+xyz\pmod3.
\]

The one-digit polynomial f contains four nonzero terms: two coefficients +1 and two -1. Direct expansion of f^2 in F_3[x,y,z] has the following complete list of supported exponent triples:

+1: (2,2,2), (2,2,1), (2,2,0), (2,1,1), (2,0,2), (1,2,1), (1,1,2), (0,2,2).
-1: (2,1,2), (1,2,2).

Thus f^0, f^1, f^2 have support counts 1, 4, 10 and coefficient sign sums 1, 0, 6 respectively.

Frobenius yields the exact identity

\[
f^n=\prod_{j=0}^{a-1}f(x^{3^j},y^{3^j},z^{3^j})^{n_j}.
\]

For each digit factor, the exponent of each of x,y,z is 0, 1 or 2. The exponents of a product across different positions have UNIQUE base-3 representations: no cross-digit carry or monomial collision is possible. Hence the support cardinalities multiply to 4^N1 10^N2, and the sum of coefficient signs multiplies to 0 when a digit 1 occurs, otherwise 6^N2.

Every monomial of f^n has each exponent <=n<Q, so the quotient by (x^Q,y^Q,z^Q) removes nothing. In particular the coefficient of x^n y^0 z^n is 1: to achieve y-exponent zero in a product of n copies of f, one must choose xz from every factor. For n=Q, Frobenius gives f^Q=(xz)^Q-(xy)^Q-(yz)^Q+(xyz)^Q=0 in the truncated ring, and hence all larger powers also vanish. The reduction of the integral group-ring monomial basis modulo 3 is the monomial basis of R_a, proving the integral divisibility statement. QED.

## Executed exact verification and numerical frontier

Companion R762DT_VERIFY.py checks the theorem independently by direct sparse multiplication in the truncated augmentation algebra for Q=3,9,27,81, checking EVERY n=0,...,Q-1: 120 exponent cases, supports, positive/negative coefficient counts, x^n z^n witness and zero at n=Q. All passed.

An independent cyclic monomial-basis six-branch integer recurrence additionally computes P^n modulo 3^12 and checks mass conservation at each step, for Q=9 and n=1..30, Q=27 and n=1..85, and Q=81 and n=1..147. No disagreement was observed with the R762DN conjectural general formula for a>=2:

\[
v_3(c_{3^a}(n))\stackrel{?}{=}\max(0,\lfloor n/3^{a-1}\rfloor-2).
\]

At Q=81, n=81,108,135 the respective exact valuations are 1,2,3; this extends author-side computation to a=4, including the previously unproved third threshold. Each observed valuation is less than 12, so modular witness precision is sufficient. The 3-adic formula remains open in general. No formal Result or mathematical acceptance is implied by GitHub storage.

## Scientific continuation

Use the digit-factor identity and integral lift of P^Q to seek a general proof or counterexample for the higher 3-adic content of full P at all Q=3^a (a>=2). Preserve full signed Port provenance and distinguish the complete three-area endpoint observer from the XZ terminal marginal of R762DS. Separately obtain a licensed native TRIADIC_CLOSURE_E Cell/Link/Port rule and exact V17/V29/V39 transport to test future-operation safety.

Source chain: R762DN@4e9001fe28f8bc19ce93e5a1f87d842a241d7756; R762DS@04366d0180f233ed68bb54243a532e2130f527ab. Current behavior follows docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context without changing frozen science pins.
