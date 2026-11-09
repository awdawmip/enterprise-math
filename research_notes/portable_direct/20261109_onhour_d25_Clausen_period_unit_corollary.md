# D25 — Exact two-period unit dichotomy for the frozen inert-plus residue classes

Date: 2026-11-09. TASK_RESEARCH; author-side corollary / local exact regression; UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.
Lane: chatgpt-research-onhour-enterprise-math-20260923. Parent: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3.

## Proposition (exact p-adic units from native original signed W/V)

Define the rational p-integral half-period coefficients
f_k=(1/6)_k(1/3)_k/((k!)² 2^k) and
g_k=(1/8)_k(3/8)_k/((k!)² 9^k), for 0<=k<p.
Let
S_A=sum f_k, D_A=sum k f_k, S_C=sum g_k, D_C=sum k g_k.
All congruences are in Z_(p).

**Theorem A.** For every prime p congruent to 13 or 19 modulo 24,
S_A*(S_A+12D_A) == p (mod p²).
In particular v_p(S_A)+v_p(S_A+12D_A)=1, where v_p is the integer p-adic valuation; the factors are p-integral, so exactly one is a unit and the other has valuation exactly one.

**Theorem C (p==19 branch).** For every prime p congruent to 19 modulo 24,
S_C*(S_C+16D_C) == p (mod p²).
Consequently exactly one of S_C and S_C+16D_C has valuation one, and the other is a p-unit.

**Proof.** The prior all-prime original signed Clausen triangular-boundary theorem, at research_notes/portable_direct/20261109_onhour_d25_Clausen_triangle_native_boundary.md, proves exact identities
W_p=S_A(S_A+12D_A)-T_A, V_p=S_C(S_C+16D_C)-T_C,
with T_A in p²Z_(p) when p==1 mod6 and T_C in p²Z_(p) when p==1 or3 mod8.
The frozen accepted D24 task specifically treats the original W_p == p mod p² for p==13 or19 mod24 as closed input (see research_tasks/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT_610cb297.md, section 1).
Published Guo–Zudilin 2019 gives original V_p == p*(-3/p) mod p³ for all p>3 (research_notes/portable_direct/20261109_onhour_d25_Cgrade2_GuoZudilin_uniform_zero_proof.md). In the two target classes (-3/p)=+1. Theorem A follows for both target classes; Theorem C follows for p==19 mod24, which is 3 modulo 8.
If a product of two p-integral numbers is p modulo p², its valuation is exactly 1, proving the dichotomies.

The theorem does not choose which factor is the unit. In the tested target primes both period sums S_A, and the p==19 class S_C, are divisible by p, so the *empirically observed branch* gives
(S_A/p)*(S_A+12D_A) == 1 (mod p);
(S_C/p)*(S_C+16D_C) == 1 (mod p) in the p==19 branch.
A uniform proof of the branch orientation requires a Hasse/Jacobi or other independent argument; the valuation-sum theorem is already unconditional relative to the previously accepted/published original signed W/V results.

## Exact local tests at all target primes <=373

Used the same rational-modular half-period recurrence as d25_Clausen_triangle_boundary_exact_20261109.py. Independently checked products modulo p² at all 19 primes p==13 or19 mod24 with 5<=p<=373, and at all 9 of those with p==19 mod24 for C. Each product was **exactly p mod p²**.

Representative p | S_A modp² | S_A+12D_A modp² | S_C modp² | S_C+16D_C modp²
13 | 143 | 149 | not part of Theorem C | —
19 | 152 | 50 | 171 | 131
37 | 851 | 547 | not part of Theorem C | —
43 | 1333 | 1659 | 860 | 286
373 | 8952 | 62835 | not part of Theorem C | —

Thus p19 gives (S_A/p)*(S_A+12D_A)=8*12=1 (mod19) and (S_C/p)*(S_C+16D_C)=9*17=1 (mod19). At p373, (S_A/p)*(S_A+12D_A)=24*171=1 (mod373). These finite calculations verify the branch on the stated finite set, not for all p.

## Mathematical use and pending original native input

This supplies a precise invertible period/derivative coordinate for finite Fricke/WZ attacks on the original signed second p-adic digit, and a class-specific split of the 2304 observation. The next discriminating action is to prove or refute the period-orientation claim S_A==0 (mod p), and for p==19 branch S_C==0 (mod p), via an explicit Jacobi-polynomial/Hasse transformation. Preserve source/observer coupling and full triangle corrections.

The original fixed-class p373 H0/B0 divided-power [X]U mod 139129, rank, Frobenius direction/eta, signed odd kappa and original Delta-R require the native benchmark #1559; they are not supplied by the Clausen periods. Source session and claim verification remain distinct.
