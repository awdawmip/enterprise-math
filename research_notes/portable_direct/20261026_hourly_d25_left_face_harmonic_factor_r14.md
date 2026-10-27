# D25/LIFT — Exact harmonic factorization of the third-digit left Hasse face

Date: 2026-10-26. Scope: auxiliary corrected-Clausen source algebra, not original-class CM/Frobenius. Requested TASK_RESEARCH logical lane: `chatgpt-research-hourly-enterprise-math-20260923`, separate from maintenance `chatgpt-hourly-enterprise-math-20260921`. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`; scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` **unchanged**.

**Status:** AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. No current Source winning CLAIM, authorized OPEN, native checkpoint, original-class experiment or independent mathematical review is established by this note.

## Consumed results and exact new question

Reuse (do not recredit) the two-parameter generating Ward source `20261026_hourly_d25_bivariate_master_ward_r13.md`, the actual one-cell left boundary `20261026_hourly_d25_ward_factorial_boundary_r11.md`, and the six-channel third-digit boundary port `20261026_hourly_d25_third_digit_dual_ward_resonant_face_r11.md`. These give, for p=6m+1 prime, L=1-2m, Hasse jets u[a,r], and the existing negative Ward adjoint face C_ab=delta*Y_L^{ab},

```
Y_L^{ab} = -2m u[a,2m]u[b,p-1],
F_p = 2p C_12 - (p^2/3)(C_22+C_13)       (mod p^3).
```

The unresolved *subunit* is whether the higher-jet boundary C_22+C_13 is independent information or is exactly recoverable from C_12 with a computable p-unit coefficient. We retain genuine ordered (j,ell), Hasse labels, negative Ward source J+E, two finite cutoff origins, separately oriented infinity, and the ordered high-high sector.

## Theorem — exact rank-one Hasse boundary and harmonic multipliers

Let H_n=sum_{k=1}^n 1/k, H_0=0. Define the rational germs (all coefficients regular at zero)

```
f_r(z) = (-m-z)_r (-2m-2z)_r / ((1/2-3m-3z)_r r!),
a_j = [z^j]f_{2m}(z),  b_j=[z^j]f_{p-1}(z).
```

The factor `(-m-z)_{2m}` has exactly one zero factor at z=0 and `(-2m-2z)_{2m}` has none. In `f_{p-1}`, the two numerator factors have exactly one zero each. Thus `f_{2m}(z)=a_1 z(1+A_m z+O(z^2))` and `f_{p-1}(z)=b_2 z^2(1+B_m z+O(z^2))`, where a_1 and b_2 are p-local units and

```
A_m = 1/m + 2H_{2m} - 6 sum_{u=m+1}^{3m} 1/(2u-1),
B_m = H_m-H_{5m-1} + 2H_{2m}-2H_{4m-1}.
```

These are **exact rational identities for every integer m>=1**. For target primes p=6m+1, every denominator displayed is a p-unit.

**Proof.** Extract the forced zero factor(s), then take the logarithmic derivative at z=0 of each remaining nonvanishing product. For a_2/a_1, the first Pochhammer contributes `H_m-H_{m-1}=1/m`; the second contributes `2H_{2m}`; the denominator contributes `3 sum_{k=0}^{2m-1}(1/2-3m+k)^{-1} = -6 sum_{u=m+1}^{3m}(2u-1)^{-1}`. For b_3/b_2, the first and second numerator products contribute respectively `H_m-H_{5m-1}` and `2H_{2m}-2H_{4m-1}`. The denominator log derivative vanishes **exactly** because its 6m terms are paired by k -> 6m-1-k with opposite reciprocal signs. Thus A_m=a_2/a_1 and B_m=b_3/b_2. No expansion, division or congruence by p is used in the proof. QED.

The actual leftmost ordered cell then yields exact equalities

```
Y_L^{02}=Y_L^{03}=Y_L^{04}=0,
Y_L^{22}=A_m Y_L^{12},       Y_L^{13}=B_m Y_L^{12}.
```

In particular the six-channel third-digit face satisfies the **one-coordinate reduction**

```
F_p = delta Y_L^{12} (2p - (p^2/3)(A_m+B_m))  (mod p^3).   (*)
```

This is an exact compression of the *declared left-face observer* at this precision. It is NOT a compression of the positive infinity, all J/E interior sources, the signed six-channel Clausen scalar, or the independent high-high population. Nor does it prove a cross-source WZ cancellation. BRC **COMPOSE_APPLIED**: the ordered labelled carrier has a rank-one *finite-face port* under this observer; the separately sourced operations remain explicit.

## New discrimination: two distinct mechanisms at p=13 and p=733

- At p=13 (m=2), **exactly** `A_2+B_2=-26351/27720`; its numerator is divisible by 13 while its denominator is a 13-unit. Consequently `Y_L^{22}+Y_L^{13}=0 (mod 13)`, though `delta=8 (mod 13)` and the first Hasse face survives. The high-jet contribution `-(p^2/3)(C_22+C_13)` vanishes (mod p^3) because of a **Hasse-jet multiplier cancellation**, not a Ward resonance. Direct independent modular recurrence gives `F_13=1872 (mod 2197)`.
- At p=733 (m=122), `A_m+B_m=527 (mod 733)`, and `Y_L^{22}+Y_L^{13}=416 (mod 733)` is **nonzero**, but `delta=0 (mod 733)` (indeed `delta=176653 (mod 733^2)`). Here the same high-jet correction vanishes at precision p^3 for the **different reason** that delta is p-divisible. Direct recurrence gives `F_733=46744143=733^2*87 (mod 733^3)`, agreeing with, but not recrediting, the existing third-digit result.

The secondary congruence `A_m+B_m=0 (mod p)` was checked for all **80** primes p=1 (mod 6) in [7,997]; only p=13 occurred **within that finite range**. No assertion is made about all primes.

## Exact reproducibility and status

Companion file: `20261026_hourly_d25_left_face_harmonic_factor_r14_check.py`. The Python standard-library checker was **actually executed** on all 80 primes, at q=p^3, constructing the jets independently via the original product recurrence rather than the harmonic formulas. Result: **PASS, 400 exact modular assertions** (5 per prime), including both p=13 and p=733 certificates. Arithmetic is integer modular arithmetic with proved p-unit divisions; no floating-point error. These checks are author replication of this auxiliary statement, not independent Driver review nor an original native CM experiment.

Next smallest science unit: substitute (*) into the genuine bivariate J/E six-channel Ward reduction at fixed original z=2. Preserve the p=13 surviving first-jet boundary, p=733 resonant but later-reappearing boundary, both finite cutoff sources, positive infinity Z+ and separate ordered high-high H_p. Seek a **new** cross-source cancellation identity or an explicitly tagged nonzero remainder, not a relabelling of (*) as WZ closure. Original same-class H_0/B_0, [X]U mod p^2, Frobenius eta, kappa and Delta_p-R_p, native experiment and independent review remain unresolved. D25/LIFT/JT2 parent **OPEN**.

Control recovery: the directly accessible Sites gateway reports v0.6.11 and research_authority_granted=false, so the existing Research-lane session/CLAIM is not treated as owned by this transport. The established support tracker is `enterprise-math#1558`; no previously rejected prepare or ambiguous write is replayed. This portable publication is **not** a Source-native research checkpoint.
