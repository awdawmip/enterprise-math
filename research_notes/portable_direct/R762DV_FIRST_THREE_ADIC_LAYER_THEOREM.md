# R762DV — First three-adic layer of full three-area BRC at the nilpotence threshold

2026-11-18 (Asia/Shanghai). RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142; continuing original RESEARCHER EM-X6-3050F6 and SID MCP-4b2d70a97f594366a7c94a0f8b45df38. Status: symbolic author derivation, exhaustive modular author checks; independent review NOT_REVIEWED.

## Exact question and frozen science

Preserve frozen P000 V5 at awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 and taskbook at e3f42efac29a2da2d95be391f3231a664e2fade0. Use the exact six named positive BRC branch polynomial
\[
P=1+X+Z+XY+YZ+XYZ
\]
in the integer group ring R_Q=Z[C_Q^3]. For Q=3^a, a>=1, put d=Q/3 and H={(id,jd,kd): i,j,k in {0,1,2}}, the order-27 subgroup of C_Q^3. Let C_Q(n;u,v,w) denote the **integer path count** at the stated full three-coordinate endpoint. R762DU supplies the ternary pointwise kernel for counts modulo 3 below Q.

## Theorem: full coefficient law immediately beyond Q

For any a>=1, 0<=r<d, and all endpoints 0<=u,v,w<Q:

1. Every integer C_Q(Q+r;u,v,w) is divisible by 3.
2. Its first nonzero three-adic layer has the exact pointwise law
\[
\boxed{\frac{C_Q(Q+r;u,v,w)}{3}\equiv
-C_d(r;\,u\bmod d,\,v\bmod d,\,w\bmod d)
\pmod3.}
\]
Here C_d(r;*) is the *same six-branch count* in C_d^3, with d=1 interpreted as the trivial cyclic group.

Consequently the nonzero first-layer support comprises precisely 27 copies of the mod-3 endpoint support at modulus d:
\[
\boxed{S^{(1)}_Q(Q+r)=27\,6^{N_1(r)}18^{N_2(r)}.}
\]
If S^{(1),+} and S^{(1),-} count quotient residues 1 and 2 respectively, then
\[
S^{(1),+}_Q(Q+r)=27S_d^-(r),\qquad
S^{(1),-}_Q(Q+r)=27S_d^+(r)
\]
where S_d^± are those of R762DU, with the empty digit string when d=1. Across the entire first plateau r=0,...,d-1,
\[
\boxed{\sum_rS^{(1)}_Q(Q+r)=27\,25^{a-1}.}
\]

The identity-endpoint quotient is always 2 modulo 3. Thus the precise 3-adic valuation of the integer coefficient gcd of P^{Q+r} is 1. The full integer gcd is **exactly 3**: it divides 6^{Q+r}, while the mod-2 group algebra F_2[C_Q^3] is reduced because Q is odd and its defining polynomials X^Q-1 etc are separable; the six-term P is nonzero there and hence its powers are nonzero. The exact content statement recovers the first plateau in R762DN, now with every quotient coefficient explicitly determined modulo 3.

## Proof

Set A=P(X^d,Y^d,Z^d), supported on H. Frobenius in characteristic 3 implies an integral decomposition
\[
P^d=A+3B\qquad(B\in R_Q).
\]
Taking the third power and dividing coefficientwise yields
\[
P^Q/3=(A+3B)^3/3
=A^3/3+3A^2B+9AB^2+9B^3
\equiv A^3/3\pmod3.
\]
The quotient A^3/3 is integral. In the 27-element group H, direct enumeration of all 6^3=216 three-branch strings gives 21 coefficients equal to 6 and six coefficients equal to 15; hence every coefficient of A^3/3 is 2 modulo 3. Equivalently
\[
\boxed{P^Q/3\equiv 2\sum_{h\in H}h\pmod3.}
\]
This finite 27-entry identity is also contained in the q=3 character certificate of R762DN and is independently checked by the companion modular recurrence.

Multiply by P^r. As r<d and all six branch coordinate increments belong to {0,1}, each coordinate of every exponent in the ordinary polynomial P^r lies between 0 and r<d. Thus in each coset of H there is precisely one potential P^r exponent, namely the triple of endpoint residues modulo d. Translation by the full H-sum repeats its coefficient 27 times without interaction from other P^r exponents. Multiplying 2=-1 mod3 proves the boxed pointwise law.

Apply R762DU's complete digit-support/sign theorem to the right-hand side; multiplication by -1 swaps residue classes 1 and 2, while the H-sum contributes 27 distinct translations. This proves all support formulas and their digit-sum aggregate. The identity residue on the right is -1 because the constant coefficient of ordinary P^r equals 1 for r<d. Therefore at least one coefficient has 3-adic valuation exactly 1. The mod-2 reduced-algebra argument and divisibility of the gcd into total mass P(1,1,1)^{Q+r}=6^{Q+r} exclude all other prime factors. QED.

## Finite proof checks and boundaries

R762DV_VERIFY.js independently computes **all** cyclic endpoint coefficients modulo 9 and compares the quotient of P^{Q+r} by 3 to the -C_d(r) residue, for every 0<=r<d, Q=3,9,27,81 and every one of the Q^3 endpoints. That is 40 exponent cases and 14,528,268 first-layer coefficient comparisons, with PASS. The full script does not infer the quotient from an assumed digit theorem: it constructs P^{Q+r} by explicit six-shift cyclic integer recurrence modulo 9 and constructs the modulus-d comparison recurrence separately modulo 3. Evidence numbers and boundary samples are in R762DV_EVIDENCE.json. Generality in a and r rests on the algebraic proof, not on extrapolating these checks.

The theorem is about nonnegative counts, not signed phase cancellation, original Port data, complete native X6 events, or a future-event sufficient BRC state. The three-coordinate endpoint observation is retained; hidden event legality and V17/V29/V39 transport remain open.

## Next research

Lift the first-layer identity to modulo 9 of P^Q/3 (i.e. modulo 27 of P^Q), and propagate its H-coset structure to subsequent Q-sized windows. Test whether this supplies exact witnesses for the still-open R762DN valuation formula at arbitrary n, while preserving original signed provenance. Separately inspect the authentic permitted TRIADIC_CLOSURE_E event language and transport.

Dependencies: R762DN@4e9001fe28f8bc19ce93e5a1f87d842a241d7756; R762DT@2b00cadde50fa5528f4a6e87c0a027ec64767dba; R762DU on this branch.
