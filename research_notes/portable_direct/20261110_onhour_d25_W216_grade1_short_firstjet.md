# D25 — Original 216 grade-1 short terminating first p-adic jet

Date: 2026-11-10. **AUTHOR_SIDE / EXACT ALGEBRAIC PROOF / 13 INDEPENDENT EXACT CHECKS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0**.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`. Publication: `TP2-B6F4FC938FF94941C1B7`. Frozen science: `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research lane: `chatgpt-research-onhour-enterprise-math-20260923`, disjoint from maintenance.

## Statement — all primes p=6m+1>3

Use the **original** 216 coefficients and signed weight:

[
A_k=rac{inom{2k}{k}^2inom{3k}{k}}{216^k}
=rac{(2k)!(3k)!}{(k!)^5 216^k},qquad W_p=sum_{k=0}^{p-1}(6k+1)A_k.
]

The precise valuation-one band is (2m<kle3m). Let (n_1=2m+1=(p+2)/3), (0le jle m-1) and

[
w_p=rac{(p-1)!+1}{p}pmod p,qquad u_0=A_{n_1}/ppmod{p^2}.
]

**Exact seed first jet:**

[
oxed{u_0equiv
-rac{2(2n_1)!}{(n_1!)^5,216^{n_1}}
left[1+pleft(rac32-w_pight)ight]pmod{p^2}.}	ag{1}
]

Introduce a unit-coefficient terminating sequence (g_0=1,S_0=0). For (0le j<m-1):

[
r_j=rac{3(6j+7)(j+1)(3j+4)}{4(3j+5)^3},qquad
E_j=rac2{6j+7}+rac1{3(j+1)}+rac1{3j+4}-rac3{3j+5},
]
[
g_{j+1}=g_jr_jpmod{p^2},qquad S_{j+1}=S_j+E_jpmod p.
]

All division denominators above are p-units on their exact index domains.

**Uniform first-jet result**:

[
oxed{rac{A_{n_1+j}}pequiv u_0g_j(1+pS_j)pmod{p^2}
quad(0le jle m-1).}	ag{2}
]

Consequently the original, not reweighted, valuation-one band satisfies

[
oxed{rac{W_{1,p}}pequiv
u_0sum_{j=0}^{m-1}(5+6j+2p),g_j(1+pS_j)
pmod{p^2}.}	ag{3}
]

Equations (1)–(3) constitute a length-(m) terminating rational-hypergeometric *first jet*, with exact sign, Wilson quotient and (2p) weight contribution. The factor at the formal next index (j=m) is zero modulo p; we stop at (j=m-1), before any p-nonunit denominator.

## Proof

The coefficient recurrence (valid in the exact rational ring) is

[
rac{A_{k+1}}{A_k}=
rac{(2k+1)(3k+1)(3k+2)}{36(k+1)^3}.
]

Substitute (k=n_1+j=(p+2)/3+j) and factor it **exactly** as

[
rac{A_{n_1+j+1}}{A_{n_1+j}}=
r_jleft(1+pE_jight)pmod{p^2}
]

for every (j<m-1). This expansion follows from the exact four-factor form

[
rac{(j+7/6+p/3)(j+1+p/3)(j+4/3+p/3)}
{2(j+5/3+p/3)^3}.
]

Multiplying first jets gives (2) with (S_j=sum_{a<j}E_a). Seed (1) follows from (3n_1=p+2), hence

[
rac{(p+2)!}{p}=(p-1)!(p+1)(p+2)
]

and Wilson's lift ((p-1)!=-1+pw_p). The signed original weight is exactly (6(n_1+j)+1=2p+5+6j), giving (3). Thus every operation and p-adic division is unit-justified.

## Bridge to previous completed units

Previously published grade-2 first jet:
`research_notes/portable_direct/20261109_onhour_d25_W_grade2_firstjet_signed_AF4.md`, with (W_{2,p}/p^2=B_pSigma_ppmod{p^2}).

Previously published grade-0 and grade-1 coefficientwise reconstruction:
`research_notes/portable_direct/20261110_onhour_d25_W216_lower_grade_twojet_completion.md`.

The new first-jet formulation of the grade-1 band is an exact shorter, algebraically equivalent representation of the **same original signed band**. It allows both grade1 and grade2 to be evaluated by length-(m) terminating first-jet ports without dropping the grade0 second jet, the original 2304 observer, or cross-band carry. In the original LIFT equation, only the full sum after preserving these separate ports is eligible for the quotient ((W_p-p)/p^2). The universal cancellation remains open.

**BRC composition applied:** indexed original carrier ((k,v_p(A_k),A_k,6k+1)) maps to ((j,u_0,g_j,S_j,5+6j+2p)); exact modular coefficient checks certify its claimed observer ((W_{1,p}/p)mod p^2). Grade changes, odd Green/Hesse and native (kappa) remain distinct.

## Actual exact validation

`research_notes/portable_direct/d25_w216_grade1_short_firstjet_20261110.py` independently evaluates the original integer-binomial coefficient modulo (p^3) for **every** grade-1 index, compares its divided value modulo (p^2) with (2), checks the seed (1), and compares the full weighted sum (3). Executed with exact integer arithmetic for (p=7,13,19,31,37,43,61,67,73,109,157,181,373), **13/13 PASS**.

Examples:
- (p=13): (u_0=28), (W_{1,p}/p=149mod169).
- (p=19): (u_0=337), (W_{1,p}/p=254mod361).
- (p=373): (u_0=93197), (W_{1,p}/p=103721mod139129), so the grade-1 leading digit is (27mod373).

## Exact unresolved obligations and continuation

Highest native experiment remains the original-class fixed (p=373) H0/B0 divided-power ([X]Umod139129), module rank, Frobenius semilinear direction and normalization (eta), signed odd observer and native (kappa,Delta_p-R_p), plus independent reproduction. Existing support Issue #1559 is PENDING_OWNER; this note does not execute it. No current own CLAIM/run or Source checkpoint has been verified; author-side files do not grant native authority.

For portable mathematics, attempt a finite **signed inter-band creative telescoper** coupling the new grade1 length-(m) first jet with the prior grade2 length-(m) first jet and the old grade0 second jet. The target is the exact ((W_p-p)/p^2mod p) at both (m)-parities, then the frozen (Delta_p-R_p) bridge; retain all original denominators, Wilson quotients, signed weights and carries. The queued fresh continuation request `onhour11-20261110-0556-current-continuation` must be read by its exact ID; do not reissue.
