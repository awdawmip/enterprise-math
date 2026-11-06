# PREFIX-528 — Generic minimal denominator for the full BRC–aAc joint distribution

Date: 2026-11-06 Asia/Shanghai.
Classification: AUTHOR_PROVED / EXACT_SYMBOLIC_AND_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.
Research line: RS-X6-NATIVE-ROTATION-DYNAMICS; independent author continuation, no formal CLAIM.
Frozen scientific input: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Dependencies: PREFIX-518 four-STAR candidate; PREFIX-522 aAc gate; PREFIX-525 endpoint pair BRC; PREFIX-526 first moment; PREFIX-527 full renewal and return-kernel denominator. P000/ACTIVE Heartbeat World and current portable protocol govern the interpretation.

## Population, target, and exact theorem

Four native STAR sets: A={L1,L3,L6}, B={L1,L4,L5}, C={L2,L3,L5}, D={L2,L4,L6}. Every signed directed phase (STAR, preceding direction, current direction) has three legal successors. There are 48 phases; each macro edge has two separately labeled native two-step paths INNER=(-old,current) and OUTER=(current,-old). For all starts and d macrosteps the population has 48*6^d histories, with all branch labels retained in its definition.

In the fixed chart +L1=a, -L1=A, +/-L3=c and other directions filler, H(w) counts literal occurrences of aAc. Let p1(w)=min(N1+(w),N1-(w)), the signed-pair BRC count. Define
P(t,q,z) = sum_(d>=0) t^d sum_(w of macro length d) q^p1(w) z^H(w).

Theorem. Over the rational-function field Q(q,z), P has a reduced rational representation whose denominator has EXACT degree 22 in t. Therefore the macro-depth coefficient sequence has minimal eventual constant-coefficient recurrence order exactly 22 over Q(q,z). This is the precise generic scalar-observer order, not a claim about a phase-automaton minimization.

Define
E(u,q) = 1-4u-(192+480q)u^2-(2304+8064q+2304q^2)u^3-(82944q+62208q^2)u^4-746496q^2 u^5,
D1(v,q)=1+2v-3q v^2,
D2(v,q)=1+(4+2q)v^2-(12q+4q^2)v^3+9q^2 v^4,
F(u,q)=D1(4u,q) D2(4u,q).

Let N0(t,q) be the following explicit polynomial, written by consecutive coefficients of t^0,...,t^9:
[48, 288, 288q+1248, 3456q+5760, 8832q+14208,
 13824q^2+69120q+55296, 4608q^2+152064q+64512,
 331776q^2+829440q+165888, 165888q^2+829440q,
 3981312q^2+1990656q].

Let K(u,q) have coefficients for u^0,...,u^11:
[0,0,20q,160q^2+368q,2560q^2+5120q,
 -27648q^3+16384q^2+27648q,
 -73728q^4-774144q^3-485376q^2+147456q,
 -1400832q^4-9732096q^3-3833856q^2,
 7077888q^5-8847360q^4-58392576q^3-31850496q^2,
 127401984q^5+445906944q^4-191102976q^3,
 573308928q^5+5733089280q^4,-20639121408q^5].

For J_N use the exact PREFIX-526 definitions:
A=1-2t-48(1+q)t^3-144qt^4-864qt^5,
B=1+2t+48(1+q)t^3-144qt^4+864qt^5,
U=(1+2t)(1+2t+12t^2)B,
Vm=8t^2(1+12t^2)^2,
Vp=8t^3(15552qt^6+1296qt^4+864t^4+48qt^2+84t^2+5),
J_N=9qt^2[(U+Vm+Vp)^2+(q-1)(Vm^2+Vp^2)].

Exact polynomial division in Z[q,t] proves that
H_*(t,q) = [J_N(t,q) F(t^2,q) - N0(t,q) K(t^2,q)] / E(t^2,q)
is a polynomial of degree 22 in t.

The complete rational function is
P(t,q,z) =
[N0(t,q) F(t^2,q) + (z-1) H_*(t,q)]
/
[E(t^2,q) F(t^2,q) - (z-1) K(t^2,q)].

In particular its generic minimal denominator is
DELTA(t,q,z)=E(t^2,q)F(t^2,q)-(z-1)K(t^2,q)
of degree 22 in t. The numerator is an exactly specified polynomial through the division identity above, not an uncomputed unknown function.

## Proof of P0 and the 12-orbit certificate

For the all-history unmarked series P0=P(t,q,1), construct the subgroup of S4 that preserves the unsigned axis L1=AB. Its four members act freely on the 48 signed directed phases. The 12 phase orbits give an EXACT orbit-constant 12x12 weighted transfer Q(x), with x marking unsigned L1 visits. Signed endpoint correction is x^(-|sigma1(c_end)-sigma1(c_start)|), giving q=x^2 after correction. This quotient is valid for the declared all-start/all-end observer.

Let v_{-1},v_0,v_1 denote the orbit-constant initial vectors by signed endpoint-L1 coordinate, and let E(t^2,x^2)=sum_j e_j(x^2)t^(2j). Direct exact integer polynomial multiplication proves, for each of these three vectors,
sum_(j=0..5) e_j(x^2) (2Q(x))^(10-2j) v=0.
The same identity at depth 11 follows by left multiplication by 2Q, as e_j has no odd coefficients. The formal transfer recurrence therefore proves E(t^2,x^2)(I-2tQ)^(-1)v is polynomial, with degree <=9. Explicit weighted end readout gives exactly N0 above, so P0(t,q)=N0(t,q)/E(t^2,q). This is an all-depth identity, not a fit to finite data.

## Proof of return kernel, cancellation, and minimality

PREFIX-527 establishes the exact return kernel S(t,q)=K(t^2,q)/[E(t^2,q)F(t^2,q)] by the 24-state parity-block matrix cofactor identity and its Q(q)[u] coprimality certificate. The present executable independently recomputes the first 16 two-step return coefficients; multiplying by E F gives K with no coefficients above u^11. PREFIX-526 supplies the exact first moment J(t,q)=J_N(t,q)/E(t^2,q)^2.

Apply the established rank-one marked-event renewal theorem:
P=P0+(z-1)J/[1-(z-1)S].
Substitution first gives a candidate denominator E(t^2)^2 [E(t^2)F(t^2)-(z-1)K(t^2)]. The exact polynomial identity
E(t^2) | [J_N F - N0 K]
cancels one ENTIRE degree-10 E factor and produces the displayed DELTA with numerator N0 F+(z-1)H_*.

To certify generically reduced form, specialize (q,z)=(2,3), (3,5), and (5,2). Exact polynomial Euclidean GCD is 1 for numerator and DELTA at each specialization, and their t-degrees equal the generic degrees (both degree 22). In particular, the nonzero specialized resultant at (2,3) proves that the generic resultant is nonzero, so gcd over Q(q,z)[t] is 1. Rational-series theory gives the sharp eventual recurrence order 22. At z=1, F cancels, yielding P0 with denominator E; the generic claim does not equate specialized minimal orders with the generic one.

## Actual execution and BRC scope

Run PREFIX528_compact_certificate.py for the exact divisibility, generic coprimality, and order certificate; an independent, longer local Python/SymPy certificate also constructed all 48 native phases, checked 12-orbit equitability, the depth-10 and depth-11 orbit-vector polynomial identities, the 24-state return kernel, and the branch-labeled literal-word joint dynamic program through macro depth d=11. It compared recurrence and raw path-weight sums at (q,z)=(1,2),(2,3),(3,5), with ALL_CHECKS_PASS. The displayed compact certificate separately executed with ALL_CHECKS_PASS. The expanded locally executed script and machine log are attached to the conversation artifact for this research turn; the GitHub files contain the complete algebraic reconstruction, compact certificate and numerical execution synopsis.

The scalar P observer sums paths. It does not replace the complete native signed-X6 Cell/path fiber, intermediate Cell/source provenance, the six-axis BRC vector, or time-labeled future operation history. The parent question remains arbitrary-triad native C6 generators, generated symmetry and rotation-selection dynamics.

## Next unit

Use the degree-22 denominator to extract coefficient-level recurrences in q,z and benchmark their true integer polynomial bit cost versus provenance-aware 96-state dynamic programming. Also test whether a concrete pair of native path histories with identical (p1,H) but different legal future behavior establishes a minimal continuation-state repair; preserve the original source/path distinction. Formal CLAIM, independent review and admission are separate canonical control actions.

## Parity refinement (new exact corollary)

Write P(t,q,z)=P_even(u,q,z)+t P_odd(u,q,z) with u=t^2. Because DELTA is even in t, both series have the same candidate denominator DELTA_u(u,q,z)=E(u,q)F(u,q)-(z-1)K(u,q), of degree 11 in u. Splitting the explicit numerator by even/odd t powers and taking exact polynomial GCD at (q,z)=(2,3) and (3,5) gives gcd=1 for BOTH parity numerators, with their generic degrees preserved. Hence each parity subsequence has exact minimal eventual recurrence order 11 over Q(q,z), rather than merely an upper bound. The attached executable certificate checks these four polynomial GCDs.
