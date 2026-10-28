# D25/LIFT GH-83 — Uniform first-order Laurent pole cancellation on the entire p ≡ 3 (mod 4) prime family

2026-10-29 Asia/Hong_Kong. **AUTHOR-DERIVED / SOURCE-COROLLARY / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**. Mother objective \`ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION\` remains OPEN; Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`; scientific pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\` unchanged. This note depends on the *still-unreviewed* GH-74/75 and GH-80/81/82 CM author proofs and does not constitute independent mathematical acceptance.

## Theorem: every real Laurent rank loses its double pole, but only transversely

For any prime \(p=4d+3\ge7\), work over \(\mathbb F_p\), with the **original** GH-13/GH-15 rational cyclic resolvent
\[
R_z(x)=\frac{\sum_{j=0}^{p-1}(8(x+j)+1)t_j(x)}{z-1},\quad
t_j(x)=\prod_{i=0}^{j-1}\frac{z(4(x+i)+1)^3}{(4(x+i)+2)(4(x+i)+3)(4(x+i)+4)}.
\]
At its actual integer ranks \(0\le r\le d\), write
\(R_z(r+\varepsilon)=A_r(z)\varepsilon^{-2}+B_r(z)\varepsilon^{-1}+H_r(z)+O(\varepsilon)\). At the successor rank \(d+1\), write
\(R_z(d+1+\varepsilon)=V_{-1}(z)\varepsilon^{-1}+V_0(z)+\cdots\). All coefficients are rational functions in \(z\) regular near \(z=9\), since \(9\notin\{0,1\}\) in the stated characteristics.

Set \(C_0(z)=1\) and \(C_{r+1}(z)=a_z(r)C_r(z)\). GH-15 proves \(C_r(z)A_r(z)=A_0(z)\) and \(A_0(z)=2zC_d(z)V_{-1}(z)\), all \(C_r(9)\) being field units. GH-16 proves the **full rational parameter identity**
\[
A_0(z)=Q_p(z)\mathcal H_d(z),\qquad
Q_p(z)=\frac{\alpha_pz^{2d+2}}{z-1},
\quad\alpha_p\in\mathbb F_p^\times,
\]
with \(\mathcal H_d=(8\theta+5)U_d\) the original coefficient polynomial, not the elliptic Hasse invariant. Both \(Q_p(9)\) and every \(C_r(9)\) are nonzero. GH-77 (for \(p\equiv3\bmod8\)) and GH-82 (for \(p\equiv7\bmod8\)) together establish, as author mathematics,
\[
\mathcal H_d(9)=0,\qquad\mathcal H'_d(9)\ne0
\quad\text{for all }p=4d+3\ge7.
\]

**Exact new full-rank synthesis:**
\[
\boxed{A_r(9)=0,\qquad
A'_r(9)=\frac{\alpha_p\,9^{2d+2}}{8\,C_r(9)}\,
\mathcal H_d'(9)\ne0
\quad(0\le r\le d).}\tag{83.1}
\]
The successor pole is also eliminated at the precise \(z=9\) fiber, but has nonzero parameter response:
\[
\boxed{V_{-1}(9)=0,\qquad
V'_{-1}(9)=\frac{\alpha_p\,9^{2d+2}}{144\,C_d(9)}
\mathcal H_d'(9)\ne0.}\tag{83.2}
\]
**Proof.** Differentiate \(C_r(z)A_r(z)=Q_p(z)\mathcal H_d(z)\) with respect to \(z\) and set \(z=9\); the terms containing \(A_r(9)\) or \(\mathcal H_d(9)\) disappear, leaving (83.1). Apply the same differentiation to \(2zC_d(z)V_{-1}(z)=A_0(z)\) to obtain (83.2). Every asserted nonzero divisor is a unit. Thus each rational coefficient \(A_r(z)\), and the successor residue \(V_{-1}(z)\), has **a simple zero at the target parameter** \(z=9\). QED.

The original finite-window GH-15 identity consequently simplifies on the *entire* \(p\equiv3\bmod4\) family:
\[
\boxed{
T_{p,9}=C_d(9)\bigl(H_d(9)+8d+1\bigr)
-H_0(9)+B_0(9)L\pmod p,
\qquad L=\sum_{r=0}^{d-1}\ell_r.}\tag{83.3}
\]
Here \(H_0,H_d\) are genuine **Laurent constant terms** (not \(\mathcal H_d\) or elliptic \(H_p\)), and \(B_0L\) is the untouched true first-order polar correction. GH-76 previously established the \(p\equiv3\bmod8\) special case. Equations (83.1)–(83.3) extend it to every prime \(p\equiv7\bmod8\) using the new asymmetric odd factorization and CM classification.

The simple-zero statement is an exact \(\mathbb F_p[\delta]/(\delta^2)\) parameter-jet statement. **It is not a congruence mod \(p^2\)** and does not remove \(B_0\), any finite endpoint, or certify the full GH-3 truncation \(T_{p,9}=0\).

## Source-fidelity and verification

The observer order is original \((p,z,r,j,\varepsilon)\), with \(C_r(z)\), \(A_r,B_r,H_r\), \(\alpha_p,\mathcal H_d,\mathcal H_d'\) and successor \(V_{-1}\) kept distinct. This is a BRC **COMPOSE_APPLIED** scalar arithmetic carrier; a scalar Laurent port is not an X6 native Cell, original W/S, six Hasse ports, or a proven three-dimensional native transfer. P000 ACTIVE remains frozen.

The companion exact Python standard-library verifier computes GH-16 coefficients and \(\mathcal H'_d(9)\), the original \(\alpha_p\) valuation-normalized product and all genuine \(C_r(9)\). It checks \(\mathcal H_d(9)=0\), \(\mathcal H'_d(9)\ne0\), each (83.1) jet and (83.2) successor relation for **all 86 primes \(7\le p<1000\), \(p\equiv3\bmod4\)**, totaling **9,895 distinct real rank jets**. All PASS. Examples, in columns \((p,d,\mathcal H'_d(9),A'_0(9),A'_d(9),V'_{-1}(9))\):
\[
(7,1,1,2,3,6),\
(11,2,4,1,9,6),\
(19,4,4,9,11,8),\
(23,5,17,11,3,4),\
(43,10,11,6,38,26).
\]
These finite tests are **author exact checks**; the proof of the all-prime corollary is algebraic and explicitly inherits the GH-75 and GH-81 CM authorship/review boundary. Original GH-15 verifier independently checked the actual Laurent transfer for specific primes and two parameters; no native \(p=373\) experiment was performed here.

Immutable project parents: \`20261028_hourly_d25_gh15_gh16_finite_laurent_counterterm.md\` (blob \`fcfad3c663bf917cac691deea4b5585738eb69e5\`), GH-76 \`20261029_hourly_d25_gh76_uniform_laurent_double_pole.md\`, GH-77 \`20261029_hourly_d25_gh77_gh78_transverse_odd_chart.md\`, GH-81/82 \`20261029_hourly_d25_gh81_gh82_odd_cm_cartier_dichotomy.md\` (blob \`dcd7d3db85e993f58951e7ffcb8843a23109acd9\`).

**Next precise action:** obtain a source-independent finite-field/CM/WZ certificate for cancellation of the three terms in (83.3), with actual \(B_0L\) retained, or falsify GH-3; independently audit the GH-74 CM model and the odd Hasse parity sign. Do not consume dual-number jets as the second \(p\)-adic digit. Original W/S, GH-20/21, native six Hasse ports, Green R23/R36 and the \(p=373\) native H0/B0 experiment remain open.

Source gateway last observed: version 0.6.11, research authority false, executor binding false, control CODE_REVIEW_REQUIRED, active jobs 5/5. No new native claim/run/checkpoint, research-activity registration or independent Driver review in this run. Control support remains \`awdawmip/enterprise-math#1558\`. Unverified old session and staging are preserved; existing scheduling and notification settings unchanged.
