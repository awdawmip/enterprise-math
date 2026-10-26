# D25/LIFT — Two-chart Hasse source reduction at the terminating rank

Date: 2026-10-26. TASK_RESEARCH portable evidence for RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin **c47e13e4aba0e006366f989d6334d443f6333ae3** unchanged.

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** This is an exact p-local hypergeometric result, not a native CM experiment, authorized research checkpoint, WZ cancellation, independent review or proof of the D25/LIFT/JT2 mother objective.

## Prior work and new question

Consume, without counting it as new: the corrected Clausen rank/Hasse recurrence in 20261025_hourly_d25_clausen_operator_rank_boundary.md; the three-channel p^4 signed reflection and infinity port in 20261026_hourly_d25_three_channel_clausen_p4_residue_polar_r11.md; full-cell unimodular tomography in 20261026_hourly_d25_unimodular_binomial_fibre_tomography_r11.md; and oriented rank flux in 20261026_hourly_d25_binomial_rank_flux_operator_r11.md.

For arbitrary signed labelled cells the preceding exact observer needs M² coordinates. Here we establish a smaller *honest chart for the constrained three-channel corrected-Clausen source*, retaining the seam where the zeroth jet vanishes but the first jet does not.

For m>=1, target prime p=6m+1, M=2m, define
\[
u_{k,r}=[t^k]\frac{(-m-t)_r(-2m-2t)_r}{(1-p/2-3t)_r r!},\quad 0\le r<p,
\]
and
\[
A(r)=r(r-p/2),\quad B(r)=(r-1-m)(r-1-2m),\quad C(r)=3(r-1)-4m,\quad
\delta(r)=3r/A(r)-C(r)/B(r).
\]
The delta denominators below are p-units: r=1,...,m or r=4m+1,...,p-1. Let c_j=u_{0,j}, d_j=u_{1,j}, h_l=u_{2,p-l}, k_l=u_{3,p-l}. We use j=0,...,M and l=1,...,M+1.

## Theorem A — first-jet passage across the terminating seam

For 0<=j<=m, c_j is a p-unit; setting alpha_j=d_j/c_j gives
\[
\boxed{c_0=1,\quad c_j=\frac{B(j)}{A(j)}c_{j-1},\quad
\alpha_0=0,\quad\alpha_j-\alpha_{j-1}=\delta(j)\quad(1\le j\le m).}\tag{A1}
\]
On the upper strip,
\[
\boxed{c_j=0\quad(m+1\le j\le M),\qquad
d_{m+1}=\frac{m c_m}{A(m+1)},\qquad
d_j=\frac{B(j)}{A(j)}d_{j-1}\quad(m+2\le j\le M).}\tag{A2}
\]
Every upper d_j is a p-unit. More specifically
\[
\boxed{c_m\equiv\binom{2m}{m},\qquad
d_{m+1}\equiv\frac{m}{(m+1)^2}\binom{2m}{m}\not\equiv0\pmod p.}\tag{A3}
\]

**Proof.** The corrected rank/Hasse recurrence, valid coefficientwise, is
\[
A(r)u_{k,r}-B(r)u_{k,r-1}-3r u_{k-1,r}
+C(r)u_{k-1,r-1}-2u_{k-2,r-1}=0.
\]
For j<=m its k=0 equation and the k=1 equation yield A1 by division by nonzero c_j and c_{j-1}. For m<j<=2m the factor (-m-t)_j has precisely one simple zero and c_j=0. At j=m+1 we have B=0 and C=-m; k=1 gives A(m+1)d_{m+1}=m c_m. For higher j both adjacent c's vanish, giving A2. All relevant factors are p-units, A(j)≡j² mod p, and the terminating products give c_m≡binom(2m,m). QED.

## Theorem B — reflected second/third-jet unit chart

For every 1<=l<=M+1, h_l is a p-unit. Set beta_l=k_l/h_l. Then for 1<=l<=M,
\[
\boxed{h_l=\frac{B(p-l)}{A(p-l)}h_{l+1},\qquad
\beta_l-\beta_{l+1}=\delta(p-l).}\tag{B1}
\]
The terminal seed is an exact factorial quotient:
\[
\boxed{h_{M+1}=
\frac{2(-1)^m m!(2m)!(3m-1)!(2m-1)!}
{(1-p/2)_{4m}(4m)!}.}\tag{B2}
\]
For any 4m<=r<p, also
\[
\boxed{\frac{u_{3,r}}{u_{2,r}}=
-\sum_{\substack{0\le i<r\\i\ne m}}\frac1{i-m}
-2\sum_{\substack{0\le i<r\\i\ne2m}}\frac1{i-2m}
+3\sum_{0\le i<r}\frac1{i+1-p/2}.}\tag{B3}
\]
Thus B3 at r=4m supplies beta_{M+1}, and B1 computes every high reflected jet without computing separate Taylor polynomials.

**Proof.** For r>=2m+1, the two indexed numerator zeros contribute (-t)(-2t)=2t². Remove those factors. The remaining product evaluated at t=0 gives B2; its logarithmic derivative gives B3. For r=p-l>=4m+1, both k=0 and k=1 coefficients vanish at r and r-1. The corrected k=2 recurrence is A(r)u2_r=B(r)u2_{r-1}. Subtract its multiple from the k=3 recurrence to obtain beta_l-beta_{l+1}=3r/A(r)-C(r)/B(r). QED.

## Theorem C — exact three-channel reduction, and a true obstruction to the naive quotient

The actual labelled cells are
\[
w^{02}_{j,l}=c_jh_l,\quad w^{12}_{j,l}=d_jh_l,\quad
w^{03}_{j,l}=c_jk_l.
\]
For j<=m, the two logarithmic charts give the exact relation
\[
\boxed{w^{12}_{j,l}+w^{03}_{j,l}=(\alpha_j+\beta_l)w^{02}_{j,l}.}\tag{C1}
\]
For m<j<=M the correct relation is instead
\[
\boxed{w^{02}_{j,l}=w^{03}_{j,l}=0,\qquad w^{12}_{j,l}=d_jh_l\in\mathbb Z_{(p)}^\times.}\tag{C2}
\]
Using the prior *ordered signed* reflection observer
\[
T_{ab}=\sum_{1\le l\le j\le2m}2^{l-j}(1+6(j-l))w^{ab}_{j,l},
\]
we therefore obtain
\[
\boxed{\begin{aligned}
T_{12}+T_{03}={}&
\sum_{j=1}^m\sum_{l=1}^j
2^{l-j}(1+6(j-l))c_jh_l(\alpha_j+\beta_l)\\
&+\sum_{j=m+1}^{2m}\sum_{l=1}^j
2^{l-j}(1+6(j-l))d_jh_l.
\end{aligned}}\tag{C3}
\]
All three identities are exact in Z_(p), hence modulo p². They retain the lower-triangle orientation and independently retain the complementary upper-triangle infinity residue from the previous three-channel theorem.

**Sharp in-family counterexample:** at the actual source cell (j,l)=(m+1,1), w02=w03=0 while w12=d_{m+1}h_1 is a p-unit. Therefore no global p-local scalar multiplier can absorb w12+w03 into w02 on the entire rectangle. Erasing the upper strip loses *genuine constrained hypergeometric Hasse information* already mod p, not merely a synthetic perturbation of arbitrary signed cells.

**Information budget:** A1-A2 and B1-B3 specify the entire three-channel family using O(m) p-local vector entries and two genuine unit charts, versus M² independent coordinates needed for arbitrary signed arrays. O(m) signed-prefix evaluation of T and the distinct infinity port is inherited from the prior theorem. This is a representation and source-faithfulness theorem, not a new cancellation, proof of original Delta_p-R_p=0, or permission to discard rank labels before future quadratic operators.

## Verification, source scope and next action

The adjacent stdlib checker independently generates exact Pochhammer Taylor coefficients and checks the corrected rank recurrence, both charts, terminal factorial and harmonic seeds, seam nonzero mod p, all labelled cells, ordered signed T and complementary infinity orientation. Actual author run: **4189 exact assertions PASS**, m=1,...,12 (not all 6m+1 prime; the rational identities cover composite values too), independent Pochhammer coefficient path for m<=5, and p-unit checks only for listed target primes. Finite checks supplement the proofs, not independent mathematical review.

**BRC COMPOSE_APPLIED:** typed carrier (j,l,oriented difference,Hasse channel,p-adic precision) and signed operations. The low observer has a real seam kernel detected by the first jet, so the two-chart representation is necessary. Auxiliary Laurent/Hasse variables are external arithmetic, not native P000 six-dimensional geometry. P000 remains ACTIVE_LOCKED.

**Next exact science:** using C1-C3, find or rule out a genuinely coupled corrected-Clausen WZ/adjoint cancellation, including the upper-strip injection, both finite boundaries and independent infinity port. Native original-class H0/B0, [X]U mod p², Frobenius direction/eta, kappa/Delta correspondence and independent review remain missing. Parent D25/LIFT/JT2 is OPEN. This portable evidence is not a Source checkpoint or Result.
