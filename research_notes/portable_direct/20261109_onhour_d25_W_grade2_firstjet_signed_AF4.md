# D25 — Exact first p-adic jet of the ORIGINAL signed 216 second valuation layer

Date: 2026-11-09. Research logical lane: chatgpt-research-onhour-enterprise-math-20260923 (not maintenance).
Parent Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Immutable publication TP2-B6F4FC938FF94941C1B7; scientific input pin c47e13e4aba0e006366f989d6334d443f6333ae3.
AUTHOR-SIDE PROVED EXACT ALGEBRAIC LEMMA / 80 PRIME REGRESSION / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.
Preceding same-turn theorem: research_notes/portable_direct/20261109_onhour_d25_W_grade2_finitefield_bridge.md, git 790aea0884feeb4658f5458cf0729ab729b58364.

## Theorem: signed second-layer first jet, p = 6m+1

For any prime p=6m+1, let n0=3m+1, r=n0+1=3m+2, N=m-1,
A_n=(2n)!(3n)!/((n!)^5 216^n),
W_{2,p}=sum_{n=n0}^{4m} (6n+1) A_n.
Each A_n in this sum has exact p-adic valuation 2.

Work in Z_(p) and modulo p^2. Define
B_p=A_n0/p^2 (mod p^2), a unit;
w_p=((p-1)!+1)/p (mod p), the Wilson quotient;
h_r=sum_{a=1}^r a^(-1) (mod p).
Then the EXACT first-jet formula for the leading unit is

B_p = [r / ((n0!)^4 216^n0)] * [1 + p(1+h_r-2w_p)] (mod p^2).

Define g_0=1 and S_0=0. For 0<=j<N set
g_(j+1)=g_j (j+1)(6j+5)(6j+7) / [9(2j+3)^3] (mod p^2),
S_(j+1)=S_j + 1/(2j+2) + 3/(6j+5) + 3/(6j+7) -3/(2j+3) (mod p).
All denominators in these recurrences are p-units in the stated range.

Define the signed first-jet polynomial readout
Sigma_p = sum_{j=0}^N g_j [(6j+4)+p(3+(6j+4)S_j)] (mod p^2).
Then

                         W_(2,p) / p^2 = B_p * Sigma_p (mod p^2).

Both the constant 3p in original weight and the term-dependent S_j are needed for the fourth digit.

## Proof

Original factorial recurrence:
A_(n+1)/A_n=(2n+1)(3n+1)(3n+2)/[36(n+1)^3].
Put n=n0+j. Its numerator factors equal
(p+2j+2)(3p+6j+5)(3p+6j+7), and denominator
36((p+2j+3)/2)^3.
Thus the ratio is the displayed recurrence for g multiplied by
1+p E_j modulo p^2, with
E_j=1/(2j+2)+3/(6j+5)+3/(6j+7)-3/(2j+3).
Induction gives A_(n0+j)/p^2=B_p g_j(1+p S_j) modulo p^2.

To evaluate B_p exactly, observe 2n0=p+1 and 3n0=p+r. Thus

((p+1)!/p)=(p-1)!(p+1),
((p+r)!/p)=(p-1)! r! product_(a=1)^r (1+p/a).

Multiply, divide by (n0!)^5*216^n0, and use
(p-1)!=-1+p w_p, and product(1+p/a)=1+p h_r modulo p^2.
This yields B_p= r/((n0!)^4 216^n0) times
[1+p(1+h_r-2w_p)] modulo p^2.

Finally, 6(n0+j)+1=3p+(6j+4). Multiply by the coefficient
jet and sum. Exact valuation and invertible denominators justify
division by p^2. QED.

## Original 216/2304 signed AF4 interface

Previous author-side Guo--Zudilin (2019) corollary
(20261109_onhour_d25_Cgrade2_GuoZudilin_uniform_zero_proof.md)
proved V_(2,p) divisible by p^3 for ALL primes p>3, for the original
2304 model. Retain Q_(2,p)=V_(2,p)/p^3 (mod p), generally nonzero.
The original signed second layer b_p is therefore EXACTLY

b_p = (W_(2,p)-2 V_(2,p))/p^2
    = B_p Sigma_p - 2p Q_(2,p) (mod p^2).

This is a direct formula for both relevant digits of the original
second-grade readout. In the known original cross-layer interface
ell_p+b_p+p t_p =0 (mod p^2), retain the actual carry
c_p=(ell_0+b_0)/p; substituting B_p Sigma_p does not erase it.
The full AF4 fourth-digit uniform cancellation is still an open
mathematical statement, and the frozen original Delta_p-R_p target
is separately open.

## Exact executed regression

Script: research_notes/portable_direct/d25_W_grade2_firstjet_signed_AF4_20261109.py.
For each of the 80 primes p=6m+1, 7<=p<=1000, computed:
(1) original signed W2 and V2 with integer binomial sums modulo p^4;
(2) B_p via Wilson quotient and root factorial;
(3) recurrence g_j, S_j and signed Sigma modulo p^2;
(4) independent original coefficient recurrence of W2 modulo p^3 from
    preceding first-bridge script.
Verified B_p equals original A_n0/p^2 modulo p^2,
W2/p^2 = B_p Sigma_p mod p^2, V2/p^3 integer, and modulo p
agreement with original coefficient recurrence. All 80 passed.
No floating arithmetic.

p | B_p | Sigma_p | W2/p² | Q2=V2/p³ (modp) | b_p modp²
13 | 62 | 53 | 75 | 3 | 166
19 | 207 | 81 | 161 | 6 | 294
37 | 337 | 1152 | 797 | 12 | 1278
43 | 970 | 1820 | 1454 | 17 | 1841
73 | 503 | 1301 | 4265 | 48 | 2586
373 | 99508 | 51691 | 68898 | 234 | 33463
997 | 284588 | 457380 | 374899 | 503 | 365926

For p373, 373^2=139129, signed second-layer certificate b_373=33463
matches prior independent low/high-carry and Abel results.

## BRC and observer preservation

Carrier = signed term-by-term original 216/2304 valuation layers,
each term labelled by original n, model A/C, valuation and signed
weight. The index bijection j=n-n0 and first-jet (B,g,S) preserve
the W2/p² observer modulo p². This is COMPOSE_APPLIED use of the
existing BRC residual/jet fidelity discipline. The lower-grade
ell_0,ell_1 and cross-grade carry are separate required coordinates,
as are the native H0/B0 Frobenius and kappa. Taking only modp would
erase the essential S_j, 3p and Q2 contributions.

## Next exact action and status

Seek an original-weight finite WZ/Fricke expression for the remaining
zero/first valuation layer ell_p to meet the exact signed b_p above
and known third-layer t_p, retaining c_p at p=13,19,373; then study
uniform target classes p=13,19 (mod24). Do not repeat 80-prime
first-jet regression without a changed hypothesis.

Native same-original-class p373 [X]U mod139129 divided-power
benchmark, actual module rank, semilinear Frobenius direction,
eta, signed odd kappa and Delta-R, independently reproducible
source, remain NOT_RUN; issue #1559 OPEN and PENDING_OWNER as read
2026-11-09. This author-side publication is not an authorized
Source native checkpoint/Result or project review/admission.
