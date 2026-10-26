# D25/LIFT — Full three-channel p=733 second-digit Ward/Clausen certificate

2026-10-26; TASK_RESEARCH logical lane chatgpt-research-hourly-enterprise-math-20260923, separate from CONTROL_PLANE_MAINTENANCE. Parent Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 **unchanged**.

**Classification:** AUTHOR-EXACT-CHECKED FINITE CERTIFICATE / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. This is an original-*corrected-Clausen auxiliary* Hasse/Green source calculation in Z/(733^2), not original-class H0/B0/[X]U, not native semilinear Frobenius, not the frozen LIFT theorem or a native Source checkpoint.

## Exact input and independent construction

Consume, without recredit, the existing three-channel corrected-Clausen Hasse rank relation from 20261026_hourly_d25_negative_orientation_source_adjoint_r11.md and the new general second-digit adjoint tangent from 20261026_hourly_d25_ward_adjoint_two_digit_tangent_r11.md.

Put p=733,m=122,L=1-2m=-243, q=p^2=537289 and channels (0,2),(1,2),(0,3). Independently compute the exact 4-level corrected-Clausen jet coefficient arrays u[a][r], 0<=a<=3, 0<=r<p, by the p-local recurrence

\[
r(r-p/2)u_{a,r}=(r-1-m)(r-1-2m)u_{a,r-1}
+3r u_{a-1,r}-[3(r-1)-4m]u_{a-1,r-1}
+2u_{a-2,r-1},
\]

with u[0][0]=1, all other boundary terms zero. Every r(r-p/2) for 1<=r<p is a unit mod p^2. Construct explicitly labelled moments

\[
M_n^{ab,s}=\sum_{1\le j,\ell\le 2m,\ \ell-j=n}j^s u_{a,j}u_{b,p-\ell}\pmod {p^2},
\quad
Y_n=M_n^{ab,1}-(p-n)M_n^{ab,0}/2,
\]

and the previously proved genuine separate J_n and E_n source terms, retaining both finite faces. Check each original exact Ward cell

\[
(p-2n)Y_n-(p-2n-1)Y_{n+1}=J_n+E_n.
\]

Compute negative adjoint lambda_n by its *original* p-local backward recurrence, not by imposing the new tangent answer. Compute U=Σ_{n=L}^0 2^n M_n^0, T=Σ 2^n(1-6n)M_n^0, K=Σ 2^n M_n^1, R=Σ 2^n Y_n. Independent source observer is B=Σ_{n=L}^{-1} lambda_n(J_n+E_n), left-face observer C=delta Y_L. Verify R=B+C and T=(1-6p)U+12K-12R. All sums are signed and the rank orientation n=ell-j is retained.

## New exact p=733 source-port certificate

Every entry is a residue modulo q=537289 from the separate source constructions, not a decimal approximation:

| Channel (a,b) | U | T | K | R | B = genuine J+E adjoint | C = delta Y_L | raw Y_L |
|---|---:|---:|---:|---:|---:|---:|---:|
| (0,2) | 194980 | 14284 | 492593 | 506918 | 506918 | 0 | 0 |
| (1,2) | 225095 | 108012 | 109186 | 140261 | 377020 | 300530 | 268155 |
| (0,3) | 400749 | 526050 | 300290 | 229559 | 229559 | 0 | 0 |

The unexpanded recurrence and new tangent both give delta=176653=733*241 (mod 733^2). In the (1,2) channel, Y_L=268155 gives Y_L mod733=610, and

\[
\boxed{C_{12}=\delta Y_L^{12}=300530=733\cdot410\pmod{733^2}.}
\]

The full channel verifies
\[
\boxed{140261=377020+300530\pmod{537289},}
\]
whereas removing the left face would yield 377020 rather than 140261. The difference is invisible modulo 733, but it changes the second p-adic digit. Channels (0,2) and (0,3) have zero raw left face in this exact construction; they do not justify zeroing the (1,2) face. At p=13 the same independent modular implementation reproduces all 18 published U/T/K/R/B/C port values from the earlier exact Fraction source checker, providing a small-rank regression.

## Validation boundary and next exact step

The companion Python standard-library checker ran all 1461 channel-specific Ward cells at p=733 (plus 21 cells at p=13), then all three signed adjoint identities and all three T decompositions at each prime: **PASS**. The jet recurrence, direct J+E source definitions, literal signed moments and the original lambda recurrence are evaluated independently; the p=733 tangent is crosschecked against the separate formula. This is a bounded exact finite-ring certificate and not a universal proof or independent mathematical review. It does not calculate the original same-class CM module, Frobenius direction/normalization eta or kappa, and cannot replace those native experiments.

BRC **COMPOSE_APPLIED**: the requisite carrier includes signed orientation, Hasse channel, boundary label, prime valuation and the separate observer B/C; scalar mod-p output alone would lose the p=733 (1,2) face. The auxiliary formal/rank coordinates are not P000 physical native axes or a complete three-dimensional slice.

The *next* mathematical unit is an explicit signed and source-labelled combination of all three channel T/U/K observers with the independent Laurent-infinity port and the original cutoff Q/R for p=733, checking whether a candidate coupled WZ telescoper leaves a nonzero residual. Native original-class benchmark H0/B0/[X]U mod p^2, semilinear Frobenius eta, kappa, original Delta_p-R_p, Source execution CLAIM/OPEN/checkpoint and independent review remain outstanding. Mother objective D25/LIFT/JT2 OPEN.