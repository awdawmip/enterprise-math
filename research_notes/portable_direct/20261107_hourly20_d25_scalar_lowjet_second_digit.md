# D25 — scalar Gauss zero-jet representation of the A/B second digit

2026-11-07 · TASK_RESEARCH author-side · exact algebra in Z/p^3Z and bounded complete finite regression · UNREVIEWED / NOT_ADMITTED.

Parent task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. This follows the source-preserving compact A/B carry note committed at fb184c9049e174e985d861435ca92c2c5875bf4f. No native Researcher/session/CLAIM is asserted.

## Theorem: the remaining p-adic Gauss discrepancy is a zero-jet scalar

Let p be a prime with p==13 or 19 (mod 24), p>3. Put alpha=1/2, beta=1/9 in Z/p^3Z, where denominators are units. Let L_A(z)=sum_{n=0}^{2m} ((1/6)_n(1/3)_n/(n!)^2)z^n, p=6m+1. Put p=8k+3 (B3) or 8k+5 (B5). Let L_B(z)=sum_{n=0}^{3k+1} ((a)_n(b)_n/(n!)^2)z^n with (a,b)=(1/8,3/8) for B3 and (5/8,7/8) for B5. Every upper index is <p and coefficients are p-integral.

Set F_A=L_A(alpha), T_A=(z d/dz L_A)(alpha) and F_B=L_B(beta), T_B=(z d/dz L_B)(beta), all modulo p^3. The existing CM Gauss root results yield F_A==F_B==0 (mod p). Hence define u_A=F_A/p, u_B=F_B/p in Z/p^2Z. Let C=1 for B3 and C=1-beta=8/9 for B5, and delta=1 for B3, 0 for B5.

The low-jet weighted scalar observers from the preceding D25 source split satisfy exact congruences modulo p^3:
G_A=F_A^2+12 F_A T_A,
G_B=(F_B^2+16 F_B T_B) for B3,
G_B=16(1-beta)F_B T_B for B5.
For B5 this follows from the *exact* differential evaluation
(1+8D)((1-z)L_B^2)=[1-9z]L_B^2+16(1-z)L_B(D L_B),
since 1-9beta=0. All low-square polynomial degrees are <p so there is no hidden projection term in G_A or G_B.

Assume the already established weighted first-digit equality G_A==G_B (mod p^2); equivalently 12u_A T_A==16C u_B T_B (mod p). Define
Gamma=(G_A-G_B)/p^2 (mod p).
The explicit second-digit identity is
**Gamma == (12u_A T_A-16 C u_B T_B)/p + u_A^2-delta*u_B^2 (mod p).**
Division by p on the right is well defined because the numerator is divisible by p. Here u_A,u_B and T_A,T_B must retain enough p-adic digits before the quotient; reducing the inputs to F_p before division would lose the second digit. This formula is a scalar (O(p) coefficient recurrence) alternative to the full quadratic convolution defining the lower Gauss jets.

The B5 branch has delta=0: the entire square-amplitude term cancels at beta=1/9. The B3 branch has delta=1 and preserves its square-amplitude contribution. This is a structural distinction arising from the exact Euler factor and differential observer, not a numerical fit.

Combining the previous exact p^3 source split with the A and B short-carry/Cartier formulas reduces the remaining target to
 (12u_A T_A-16 C u_B T_B)/p +u_A^2-delta*u_B^2
 + E_A-E_B ==0 (mod p).
A universal Fricke/Dwork relation proving this scalar identity for every target prime remains the next unfinished unit.

## Executed exact finite regression

Companion source: d25_lowjet_second_digit_scalar_20261107.py, using a direct one-pass low Gauss coefficient recurrence modulo p^3, and independently comparing Gamma to the prior full polynomial-square and original weighted 3F2 coefficient computations from d25_compact_fricke_defect_20261107.py. PASS on **all 94 primes p<2500 with p==13 or 19 (mod 24)**.

Representative p:(Gamma,u_A mod p,u_B mod p,T_A mod p,T_B mod p):
13:(4,11,11,7,12); 19:(14,8,9,1,7); 43:(2,31,20,20,34); 67:(16,61,14,40,35); 373:(219,24,359,294,41); 997:(644,915,860,767,980).
The p=373 regression is portable finite ring arithmetic, not the native H0/B0 experiment.

## Frontier and routing

Required next result: derive a Fricke pullback identity for the *second-digit* difference of u_A T_A and C u_B T_B, including the scalar square term and exact A/B Cartier/carry corrections; start at p=13,19,43,67,373 with the listed witnesses. Preserve B5 Dixon diagonal, different source labels, and the original frozen mother target. No assumption of a single common Cartier constant.

Backend observed earlier in this run: CONFIGURED_NOT_LIVE_VERIFIED; em_status BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE / operation_sent=false. Original unresolved requests preserved, activity REGISTER_PENDING / SYNC_DEBT, no native checkpoint or acceptance. Support #1558.
