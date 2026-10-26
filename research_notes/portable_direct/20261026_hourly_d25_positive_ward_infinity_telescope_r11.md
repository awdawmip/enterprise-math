# D25/LIFT — Genuine positive Ward adjoint as an infinity-source telescoper

Date 2026-10-26. TASK_RESEARCH logical lane chatgpt-research-hourly-enterprise-math-20260923 (distinct from maintenance). Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen science Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** Corrected-Clausen auxiliary finite-rank source, not native original-class CM/Frobenius, canonical CLAIM/run/checkpoint, all-prime D25 proof or independent review.

## Exact inherited input and new question

From 20261026_hourly_d25_diagonal_one_digit_resonance_r11.md, consume (do not recredit) the exact **genuine source** recurrence with Hasse k-1,k-2 coupling and the actual two finite cutoff faces:
\[
(p-2n)Y_n^{ab}-(p-2n-1)Y_{n+1}^{ab}=S_n^{ab}=J_n^{ab}+E_n^{ab},
\quad Y_n=M_n^{ab,1}-\frac{p-n}{2}M_n^{ab,0}.
\]
For prime p=6m+1>=7 the signed difference n=ell-j has support 1-2m<=n<=2m-1; Y_{2m}=0. For channels ab=(0,2),(1,2),(0,3), define the **positive, upper/infinity-oriented** observations
\[
I^0_{ab}=\sum_{n=1}^{2m-1}2^nM_n^{ab,0},\quad
I^1_{ab}=\sum_{n=1}^{2m-1}2^n(6n-1)M_n^{ab,0},\quad
K^+_{ab}=\sum_{n=1}^{2m-1}2^nM_n^{ab,1}.
\]
The inherited residue paper supplies the Laurent interpretation of I^0,I^1. The new issue is to **express the independent infinity port through authentic positive-rank Ward source terms**, not a tautological endpoint-versus-infinity restatement and not the old negative-oriented adjoint.

## Theorem A — positive-orientation p-unit Ward Green adjoint

Put N=2m-1. Define, over the p-local rationals,
\[
\boxed{\mu_1=\frac{2}{p-2},\qquad
\mu_n=\frac{2^n+(p-2n+1)\mu_{n-1}}{p-2n}\quad(2\le n\le N).}\tag{1}
\]
Every denominator p-2n lies in [2m+3,p-2], hence is a p-unit. Define the **authentic positive source observable**
\[
Z^+_{ab}=\sum_{n=1}^{N}\mu_n\big(J_n^{ab}+E_n^{ab}\big).
\]
Then the finite **exact rational** identity is
\[
\boxed{\sum_{n=1}^{N}2^nY_n^{ab}=Z^+_{ab},\qquad
I^1_{ab}=(6p-1)I^0_{ab}-12K^+_{ab}+12Z^+_{ab}.}\tag{2}
\]

**Proof.** Multiply the inherited Ward equation at n by mu_n and sum n=1..N. At Y_1 the coefficient is (p-2)mu_1=2. For n>=2, the coefficient of Y_n after reindexing is (p-2n)mu_n-(p-2n+1)mu_{n-1}=2^n by (1). The only other boundary is -(p-2N-1)mu_N Y_{N+1}, which is zero **because the actual finite carrier has Y_{2m}=0**; no artificial infinite extension is made. This proves the first identity, with every genuine J and E source intact.

Next, from the definition of Y, one gets sum_n n2^n M_n^0 = pI^0-2(K^+-sum_n2^nY_n). Multiply by six and subtract I^0 to obtain the second identity. QED.

This is different from the predecessor's negative-origin adjoint, whose leftmost face is C12=delta Y_L. The positive one has no separate left correction because its first weight mu_1 is fixed by Y_1 and its actual right terminal moment is zero. **The genuine E_n faces are still present inside Z+**; their vanishing was never asserted.

## Theorem B — exact source-labelled infinity compensator for all three Hasse channels

For the already-established three-channel corrected-Clausen reflection define
\[
\mathcal I_p=I^1_{02}+p\left(-6I^0_{02}-\frac{I^1_{12}+I^1_{03}}6\right).
\]
Substituting (2), and **without invoking any residue-theorem cancellation**, gives the exact p-local identity
\[
\boxed{\begin{aligned}
\mathcal I_p={}&-I^0_{02}-12(K^+_{02}-Z^+_{02})
+\frac p6(I^0_{12}+I^0_{03})\\
&+2p(K^+_{12}+K^+_{03}-Z^+_{12}-Z^+_{03})
-p^2(I^0_{12}+I^0_{03}).
\end{aligned}}\tag{3}
\]
In particular, modulo p² the last p² mass drops, but the first two-digit channel and the other channels' first-digit **genuine source terms** remain.

**Proof.** Apply (2) to channel 02 and cancel +6pI^0_02 with the original -6pI^0_02. Substitute (2) in the remaining two I^1 terms:
\[
-\frac p6(6p-1)(I^0_{12}+I^0_{03})
=\frac p6(I^0_{12}+I^0_{03})-p^2(I^0_{12}+I^0_{03}),
\]
while the K^+/Z^+ parts contribute +2p(K^+_{12}+K^+_{03}-Z^+_{12}-Z^+_{03}). This is precisely (3); every step is over Q with p-local denominators. QED.

Compare (3) with the separate lower-orientation scalar Ward formula proved in 20261026_hourly_d25_ward_scalar_port_filtration_infinity_r11.md: its U/K/S signs are dual to the upper I^0/K^+/Z^+ signs, **but the lower left finite face 2pC12 has no automatically identified upper counterpart**. This gives a source-faithful dual-port interface, not an all-prime vanishing theorem.

## Independent exact source certification

The companion standard-library checker builds all Hasse jets, every required *genuine* positive J_n and E_n from their separate rank expressions, independently computes labelled moments and the original I^0/I^1 by positive Laurent ranks. It checks each true Ward cell, the p-unit mu recurrence, (2) and (3), and compares I^0/I^1 with an independent signed rank/prefix construction.

**PASS: 23 primes**, all p=6m+1 in [7,211] plus p=733, modulo p². The exact channel source readouts are:

| p | Channel | I0 | I1 | K+ | Z+=sum mu*(J+E) |
|---|---|---:|---:|---:|---:|
| 13 | (0,2) | 71 | 140 | 102 | 151 |
| 13 | (1,2) | 143 | 96 | 71 | 105 |
| 13 | (0,3) | 14 | 66 | 121 | 93 |
| 733 | (0,2) | 412429 | 133234 | 270708 | 452579 |
| 733 | (1,2) | 43506 | 152058 | 311692 | 501710 |
| 733 | (0,3) | 219766 | 424333 | 35027 | 182587 |

From **actual J+E source sums** via (3), the combined independent infinity port is **166 mod169** at p=13 and **216796 mod537289** at p=733, matching the direct Laurent upper-rank computation. These are exact finite-ring observations, not universal evidence that some further WZ cancellation holds.

## BRC scope and next unresolved unit

**BRC COMPOSE_APPLIED.** Ordered signed (j,ell) carrier; Hasse channels; positive-versus-negative rank orientation; typed p-adic precision; genuine J/E source tags, finite cutoff faces and independent infinity port. The new mu adjoint is a p-local **source-preserving linear operator** on this carrier. Compressing to a scalar endpoint alone would discard the source information required for the original Q; this auxiliary Laurent operator is not a native X6 spatial axis or P000 dynamics.

**Next concrete unit:** combine (3) with the lower scalar Source formula, retaining the 2pC12 face, and seek a further nontrivial relation among their separate J/E terms. A putative all-prime telescoper must account for the p=13 (nonresonant face) and p=733 (resonant face, nonzero infinity) witnesses without silently identifying the two orientations. The mother goal still needs same-class original CM H0/B0, [X]U mod p², Frobenius eta/kappa/Delta-R, real native experiment and independent Driver review; D25/LIFT/JT2 remains OPEN.

Native control reads this turn returned INVALID_ARGUMENT / CONTROL_QUOTA; the exact original request IDs then returned CONTROL_REQUEST_NOT_FOUND, not NO_DISPATCH. No new service Researcher, CLAIM, OPEN, Source checkpoint, freeze or review is asserted.
