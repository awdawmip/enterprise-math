# D25/LIFT — Source-fixed joint LOW/HIGH cutoff: exact Laurent split and full finite part modulo p²

2026-10-24 | TASK_RESEARCH | ALL-PRIME EXACT RATIONAL IDENTITY / TWO-DIGIT FINITE-PART COROLLARY / EXACT AUTHOR SELF-CHECK / UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT.

Mother RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin **c47e13e4aba0e006366f989d6334d443f6333ae3**, unchanged. Author Research lane chatgpt-research-hourly-enterprise-math-20260923 is neither the maintenance conversation nor the independently contributing onhour Research conversation. This note is a portable author proof, not a native CLAIM, run, Source checkpoint, Result or review.

## 1. Exact inputs and original coefficient scope

Inherited, not re-credited: the distinct onhour lane's 20261024_onhour_d25_regular_low_jet_high_unit_two_sector_certificate.md derives original LOW first jet, two source-fixed HIGH sectors and the finite LIFT obstruction; 20261024_onhour_d25_joint_low_high_cutoff_pole_one_port.md derives the fixed-p auxiliary joint cutoff's principal pole and one surviving LOW Cauchy port. This Research lane already proved LOW-jet m-shift with integral residual in 20261024_hourly_d25_low_jet_high_joint_m_seam_regularization.md; source-fixed HIGH pole −82 in 20261024_hourly_d25_fixed_high_cutoff_shift_universal_pole_82.md; and the new mod-p² HIGH *finite part* (including p³ eta boundary) in 20261024_hourly_d25_high_eta_third_digit_and_cutoff_finite_part.md, commit 1dec548ac8c5f5f00e59abb66717ee230c5e141e. The present unit composes these **as explicitly attributed, unreviewed mathematical inputs** to expose the *complete two-digit joint cutoff regular part*, beyond the other lane's leading residue.

Fix m≥2 and prime p=6m+1≥13. Let r denote a freely varied **auxiliary cutoff with the same fixed p**, not the original forcing at a different prime. Retain exactly the source-fixed rational functions
\[
b_{r,n}=(-1)^n2^{-n}\binom rn,\quad
k_n=\frac{(1-3n)(6n+3)}{(3n+1)(3n+2)},\quad
A_r=\sum_{n=0}^r b_{r,n}k_n,
\]
\[
J_r=\sum_{n=0}^rb_{r,n}k_n
\left[\frac2{1-3n}+\frac2{6n+3}-\frac1{3n+2}-\frac2{3n+1}
+\sum_{j=0}^{n-1}\left(\frac3{6j+1}-\frac1{3j+2}-\frac2{3j+1}\right)\right],
\]
\[
B_r=\frac{(2r-1)!(2r)!}{(4r)!},\quad
h_r=\frac{28}{9}+\frac13H_r+\frac29H_{2r},\quad
E_r=A_r+(1-2r)B_r.
\]
The inherited \(Z_r\) is the exact source-fixed HIGH rational sum, retaining the two separately labeled \(a_{r,s}k_s^A\) and signed \(-c_{r,s}k_s^B/24\) sectors. Define the other lane's joint fixed-p observer
\[
\Phi_p(r)=E_r/p+J_r+B_r(Z_r+h_r).
\]
The inherited original first-digit identity gives \(E_m/p\in\mathbb Z_{(p)}\), but there is no such assumption for \(E_{m+1}\).

The two existing **exact** cutoff decompositions are
\[
q_m=\frac{8(-1)^m}{7\,2^m},\qquad
J_{m+1}-J_m=q_m/p+V_m^J,\quad V_m^J\in\mathbb Z_{(p)},
\]
\[
Z_{m+1}-Z_m=-82/p+\Lambda_m,\quad\Lambda_m\in\mathbb Z_{(p)}.
\]
Here \(V_m^J\) is already an explicit finite rational six-port/harmonic operator expression in the cited LOW theorem; \(\Lambda_m\) is the full two-sector HIGH remainder with its precise new end terms from the cited HIGH theorem. Neither is an adjustable fitted cancellation.

## 2. Exact Laurent decomposition of the entire original-coefficient joint observer

**Theorem A.** Put
\[
\boxed{\widehat{\mathcal R}_m:=E_{m+1}-E_m+q_m-82B_{m+1}.}\tag{1}
\]
Then the following is an **exact equality of rational numbers**:
\[
\boxed{\begin{aligned}
\Phi_p(m+1)-\Phi_p(m)&=\widehat{\mathcal R}_m/p+\mathscr F_m,\\
\mathscr F_m&=V_m^J+(B_{m+1}-B_m)(Z_m+h_m)\\
&\quad+B_{m+1}\bigl(\Lambda_m+h_{m+1}-h_m\bigr)
\in\mathbb Z_{(p)}.
\end{aligned}}\tag{2}
\]
Its principal coefficient \(\widehat{\mathcal R}_m\bmod p\) is precisely the other lane's *already proved* three-boundary joint-cutoff residue; the **new object** here is the exact integral finite part \(\mathscr F_m\) and its second digit.

**Proof.** Subtract the two definitions of \(\Phi_p\) and separate the change in \(B\):
\[
\Delta\Phi_p=(E_{m+1}-E_m)/p+\Delta J+
(B_{m+1}-B_m)(Z_m+h_m)+B_{m+1}(\Delta Z+\Delta h).
\]
Insert the two **exact** inherited decompositions, collect pole numerators, and obtain (1)–(2) with no congruence or fitted coefficients. For m≥2, both \(B_m,B_{m+1}\) are p-units (top factorial \(4m+4<p\)), as are \(Z_m,h_m\) and
\[
\Delta h=\frac1{3(m+1)}+\frac29
\left(\frac1{2m+1}+\frac1{2m+2}\right).\tag{3}
\]
The p-integrality of \(V_m^J\) and \(\Lambda_m\) has been proved in the separately cited, exact predecessor identities. Therefore \(\mathscr F_m\) is p-integral. QED.

## 3. New complete second-digit formula for the joint finite part

In the fixed HIGH source, let the exact old-coefficient and true final-endpoint remainder be
\[
\begin{aligned}
W_m={}&\sum_{s=1}^{m-1}(\rho^A_{m,s}-1)a_{m,s}k_s^A
-\frac1{24}\sum_{s=1}^{2m-1}(\rho^B_{m,s}-1)c_{m,s}k_s^B
-\frac{\theta_m}{24}k_{2m+1}^B,\\
\rho^A_{m,s}&=\frac{4(2m+1)(m+1)}{m(m+s+1)},\quad
\rho^B_{m,s}=\frac{2(2m+3)(m+s)}{(2m+s+1)(2m+s+2)},\\
\theta_m&=c_{m+1,2m+1},
\end{aligned}\tag{4}
\]
with all \(a,c,k\) unchanged from the Source-fixed HIGH definition. Define
\[
S_m=H_{3m}-H_m/2,\quad T_m=H_{3m}^{(2)}-H_m^{(2)}/4,\quad
C_m=-S_m^2-T_m+\tfrac{77}{12}S_m-\tfrac{607}{6}.
\]
The immediately preceding new HIGH theorem proved
\(\Lambda_m\equiv W_m-1315/12-2S_m+pC_m\pmod {p^2}\).

**Theorem B (every p=6m+1≥13):**
\[
\boxed{\begin{aligned}
\mathscr F_m\equiv{}&
V_m^J+(B_{m+1}-B_m)(Z_m+h_m)\\
&+B_{m+1}\Big[
W_m-\frac{1315}{12}-2S_m
+\frac1{3(m+1)}+\frac29\left(\frac1{2m+1}+\frac1{2m+2}\right)
+pC_m\Big]\pmod {p^2}.
\end{aligned}}\tag{5}
\]
**Proof:** use the exact joint Laurent split (2), the source-fixed HIGH p² expansion, and the exact \(\Delta h\) identity (3). Each term is in \(\mathbb Z_{(p)}\) for p≥13; reducing modulo p² is lawful. No source branch, LOW first-jet, \(n=2m\) seam or original \(n=4m\) merged terminal was dropped. In contrast, directly reducing \(\Delta\Phi_p\) before extracting its actual Laurent principal part is generally invalid. QED.

## 4. Executed exact checks, inference and next dependency

Author-side code (Python standard-library Fraction, arbitrary-size factorial integers) independently rebuilt \(A,J,B,Z,h,W\) from original rational sums, evaluated exact (1)–(2), and checked the new congruence (5) modulo p² for **all nine instances** p=13,19,31,37,43,61,67,73,211. Every check passed. Triples \((p;\widehat{\mathcal R}_m\bmod p;\mathscr F_m\bmod p^2)\):
\[
13:(6,123),\quad19:(7,184),\quad31:(26,531),\quad
37:(24,719),\quad43:(18,511),\quad61:(22,97),\quad
67:(41,1583),\quad73:(37,608),\quad211:(142,4966).
\]
The rational identity is exact, and the p² result follows algebraically from the cited, **unreviewed** earlier author proofs; nine tests are regression only. The special p=7 is excluded: \(B_{m+1}\) has a nonunit denominator and the LOW forward jet has a second pole. No p=7 second-digit statement is being inferred here.

**BRC: REUSE_APPLIED / COMPOSE_APPLIED.** Carrier tracks signed LOW first-jet, original HIGH-A and HIGH-B branches, valuation labels, exact \(m,m+1\) indices and two seam boundaries. Observer is the first two **integral p-adic digits** after extraction of the actual rational Laurent numerator. Neither positive mass nor scalar-only cancellation is substituted for the signed branch data; no native X6 computation is claimed.

The next smallest unproved task is a terminating WZ/Gosper or valid finite-difference antidifference for the explicit p-integral multiport (5), keeping the other lane's surviving LOW Cauchy \(I_1(m)\) coordinate, with original fixed-rank seam and endpoint conditions. This auxiliary cutoff theorem is NOT the target proof of \(\mathcal D_m^{finite}\equiv0\bmod p\). The real native D25 still requires a Source-specific divided-power/CM primitive class, semilinear map direction, ordinary \(\omega+6\nabla_\lambda\omega\) comparison, exact leading normalization, and same-class kappa bridge. No native Result, independent review, claim or Source checkpoint was made; original Source pin and scheduler/notifications are untouched.
