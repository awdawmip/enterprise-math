# D25 — Integral reciprocal anomaly and p² repair of the CM(−24) Hasse jet

Date: 2026-11-05. Role: TASK_RESEARCH author-side; Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific pin: c47e13e4aba0e006366f989d6334d443f6333ae3. **AUTHOR-DERIVED / EXACT GENERAL INTEGER IDENTITY / 168-PRIME FINITE CHECK / UNREVIEWED / NOT_ADMITTED.** Auxiliary CM/Legendre only, not native H0/B0.

## New exact integral theorem

For every integer m≥0, set p=2m+1 (primality not needed) and

$$H_m(t)=\sum_{j=0}^m\binom mj^2t^j,\quad C_m(t)=16t(1-t^2)H_m'(t)+(1+2t-7t^2)H_m(t).$$

The following identity holds **in Z[t,t⁻¹]**, not merely modulo p:

$$\boxed{t^{m+2}C_m(t^{-1})-C_m(t)=8p(t^2-1)H_m(t).}\tag{A}$$

Therefore the corrected observer \(\widehat C_m=C_m-8pH_m\) has **exact weighted reciprocal symmetry**

$$\boxed{t^{m+2}\widehat C_m(t^{-1})=\widehat C_m(t).}\tag{B}$$

Among corrections C_m+cpH_m with an integer constant c, this is the unique correction attaining that identity: c=−8.

**Proof.** Binomial symmetry gives H_m(t⁻¹)=t^(−m)H_m(t), and differentiation gives H_m'(t⁻¹)=m t^(1−m)H_m(t)−t^(2−m)H_m'(t). Substitute into C_m, cancel derivative terms and simplify the remaining coefficient to (16m+8)(t²−1)=8p(t²−1). A constant correction cpH_m changes the defect by cp(t²−1)H_m, forcing c=−8. QED.

## Split class and the forced second-digit source

Retain Q(t)=t⁴−140t³+294t²−140t+1. For primes p≡5 (mod24), the **previous author-side** 2-/3-isogeny theorem gives Q|C_m (mod p) and H_m(a)≠0 at all roots a of Q. Its proof has not been independently admitted; the following corollary depends on that result. Set A_p=F_p[t]/Q, and define the coefficientwise integral second digit

$$T_p=\frac{C_m\bmod Q}{p}\bmod p\in A_p.$$

The quotient is legitimate because the unique degree-<4 remainder over Z is divisible coefficientwise by p. As Q is reciprocal and monic, t is a unit and t⁻¹=140−294t+140t²−t³ modulo Q. Divide (A) in the free rank-4 (Z/p²)[t]/Q by p to obtain:

$$\boxed{t^{m+2}T_p(t^{-1})-T_p(t)=8(t^2-1)H_m(t)\pmod{p,Q}.}\tag{C}$$

The **source-preserving repaired observer** \(\widehat T_p=T_p-8H_m\) has zero weighted inversion defect and recovers T_p given H_m. The source 8(t²−1)H_m must be retained; a scalar norm/zero flag would erase it.

Since Q(±1)=(16,576), disc(Q)=2³²·3⁶ and H_m(a)≠0 at every CM root in the split class, the RHS of (C) is nonzero at each root. Thus **no reciprocal pair** (a,a⁻¹) can have both T_p values zero, and

$$\boxed{Q\nmid C_m\pmod{p^2}\quad\text{for every split prime }p\equiv5\pmod{24}}\tag{D}$$

**conditional only on the prior unreviewed general split-class theorem**. This is a sharp obstruction to the *uncorrected* lift, not to a corrected CM–Jacobi/Green cancellation or original native experiment.

## Exact computational certificate

The accompanying pure-stdlib Python file checks all 168 primes 5≤p≤5000, p≡5 (mod8): for each p, (A)/(B) coefficientwise modulo p²; for the 85 split primes it constructs T_p from full monic quartic remainder, verifies (C) and repaired inversion by explicit quotient-ring multiplication, and verifies T_p≠0. All assertions PASS. The other 83 are inert. Representative basis (1,t,t²,t³):

| p | T_p | H_m mod (p,Q) | T_p−8H_m |
|---|---|---|---|
|5|(3,2,0,0)|(1,4,1,0)|(0,0,2,0)|
|29|(17,8,16,17)|(27,16,27,7)|(4,25,3,19)|
|53|(49,21,2,24)|(5,32,3,5)|(9,30,31,37)|

p=5 also recovers the previous uncorrected witness C_5 mod (25,Q)=15+10t. This finite test corroborates the all-m proof and the conditional split corollary; it is not a native p373 H0/B0 calculation.

**BRC typed use:** retain the involution branch ports, exact integer coefficient vector, p-adic valuation, H_m source, raw T_p and invertible repaired T_hat. Inversion t→t⁻¹ is the allowed operation; source-erasing quotient is not valid for this next operation. CM Legendre is an explicitly auxiliary external algebraic observer, not an identification with P000 X6 native space.

## Next exact unit and evidence debt

Project the separated involution-odd source 8(t²−1)H_m and reciprocal-corrected T_hat through the existing period map x(t)=16t(1−t)²/(1+t)⁴, and test against the previously established short Jacobi Green–Wronskian port W(1) and Euler second digit. Establish an actual coordinate/source-preserving comparison before claiming the cancellation. Preserve original-class p373 H0/B0, [X]U mod p², eta, kappa, Delta_p−R_p, independent review and the canonical Source checkpoint as distinct obligations.

References (existing author-side): 20261105_hourly20_d25_cm24_second_digit_jet_counterexample.md; 20261105_hourly20_d25_cm24_23isogeny_firstjet_selection.md; 20261104_hourly20_d25_short_jacobi_green_wronskian.md. Native CLAIM/OPEN/checkpoint/Result/review are **not** asserted by this publication.
