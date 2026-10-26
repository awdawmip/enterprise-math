# D25/LIFT — Global Ward gluing, the rank-zero p-adic obstruction, and the p=733 resonant source certificate

Date: 2026-10-26. TASK_RESEARCH ordinary logical conversation \`chatgpt-research-hourly-enterprise-math-20260923\`, separate from CONTROL_PLANE_MAINTENANCE \`chatgpt-hourly-enterprise-math-20260921\`.
Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`; frozen scientific Source \`c47e13e4aba0e006366f989d6334d443f6333ae3\` unchanged.

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.**
This is corrected-Clausen auxiliary, finite-rank algebra. It is not an original-class CM/Frobenius experiment, native CLAIM/run/Source checkpoint, a new all-prime annihilating WZ syzygy, proof of D25/LIFT/JT2, or independent review.

## Inherited typed source and new question

Consume without recredit \`20261026_hourly_d25_negative_orientation_source_adjoint_r11.md\`, \`20261026_hourly_d25_positive_ward_infinity_telescope_r11.md\`, and \`20261026_hourly_d25_third_digit_dual_ward_resonant_face_r11.md\`. Their exact Hasse source equation is
\[
 (p-2n)Y_n^{ab}-(p-2n-1)Y_{n+1}^{ab}=S_n^{ab}=J_n^{ab}+E_n^{ab},
 \quad L=1-2m\le n\le N=2m-1,\quad Y_{N+1}=0,
\]
where \(p=6m+1\ge7\) is prime, \(M_n^{ab,s}=\sum_{\ell-j=n}j^s u_{a,j}u_{b,p-\ell}\) over ordered \(1\le j,\ell\le2m\), and \(Y_n=M_n^{ab,1}-(p-n)M_n^{ab,0}/2\). The indices, Hasse labels, two genuine finite faces, p-valuation, and orientation remain typed. The external Laurent rank coordinate is not a native P000 spatial axis or a complete three-dimensional slice.

Prior results treated lower (\(n\le0\)) and upper (\(n>0\)) Ward adjoints separately to avoid division by \(p\). The precise open algebraic problem here is whether a **single, left-face-free global source adjoint** is p-integral, and how this interacts with the previously observed p=733 resonance and third-digit face.

## Theorem 1 — exact global adjoint and a unique p-adic Fredholm obstruction

Let \(w_n=2^n\). Over \(\mathbb Q\), define the **left-zero gauge** \(a_{L-1}=0\), uniquely, by
\[
 \boxed{a_n=\frac{w_n+(p-2n+1)a_{n-1}}{p-2n}\quad(L\le n\le N).}\tag{1}
\]
Retain the prior lower adjoint
\[
\lambda_0=0,\quad
\lambda_{n-1}=\frac{(p-2n)\lambda_n-w_n}{p-2n+1}
\ (n=0,-1,\ldots,L+1),\quad
\delta=w_L-(p-2L)\lambda_L
\]
and the prior upper adjoint \(\mu_0=0\), \(\mu_n=[w_n+(p-2n+1)\mu_{n-1}]/(p-2n)\) for \(n\ge1\). Define
\[
 \boxed{\kappa_p=\frac{p+1}{p-2L}
          \prod_{n=L+1}^{-1}\frac{p-2n+1}{p-2n}.}\tag{2}
\]
Empty products equal one. Then
\[
 \boxed{a_0=\frac{\kappa_p\delta}{p},\qquad
 a_n=\mu_n+a_0\prod_{k=1}^{n}\frac{p-2k+1}{p-2k}\quad(1\le n\le N).}\tag{3}
\]
All factors of \(\kappa_p\) are p-units; indeed
\[
 \boxed{\kappa_p\bmod p=
 \frac1{4m-2}\prod_{j=1}^{2m-2}\frac{2j+1}{2j}
 =\frac{(4m-3)!}{(4m-2)\,2^{4m-4}((2m-2)!)^2}\not\equiv0\pmod p.}\tag{4}
\]
Consequently the **unique** left-zero global adjoint has p-integral coefficients precisely when \(\delta\equiv0\pmod p\). More generally \(v_p(a_0)=v_p(\delta)-1\) for \(\delta\ne0\), and the other coefficients can have no worse denominator. This is an obstruction for this source-independent gauge, not a theorem that no channel-specific syzygy or other supplemented observer exists.

For each real Hasse channel, the exact, finite, all-rank source identity is
\[
 \boxed{\sum_{n=L}^N2^nY_n^{ab}=\sum_{n=L}^N a_n\,[J_n^{ab}+E_n^{ab}].}\tag{5}
\]
The \(J/E\) distinction and cutoff faces **remain present in \(S\)**. The explicit lower face \(\delta Y_L\) has been transported to the rank-zero / neighboring genuine source coefficients; it has not been proved to vanish.

**Proof.** Equation (1) implies
\((p-2n)a_n-(p-2n+1)a_{n-1}=w_n\).
Multiply the Ward equation by \(a_n\), sum from \(L\) through \(N\), and shift the second sum. The coefficient of \(Y_L\) is \((p-2L)a_L=w_L\), each interior \(Y_n\) has coefficient \(w_n\), and the final \(Y_{N+1}\) is zero by the actual finite cutoff. This proves (5) over \(\mathbb Q\).

At \(n=L\), \(a_L-\lambda_L=\delta/(p-2L)\). Since \(a\) and \(\lambda\) satisfy the same inhomogeneous recurrence on \(L+1,\ldots,-1\), their difference propagates by \((p-2n+1)/(p-2n)\). Also the lower initialization gives \(\lambda_{-1}=-1/(p+1)\). Therefore
\[
p a_0=1+(p+1)a_{-1}
=(p+1)(a_{-1}-\lambda_{-1})=\kappa_p\delta.
\]
For \(n\ge1\), the difference between \(a\) and \(\mu\) solves the homogeneous recurrence with initial value \(a_0\), giving (3). Except \(n=0\), all denominators \(p-2n\) over this support are units modulo p. For the negative products, \(2j,2j+1< p\); (4) follows by factorial multiplication, establishing the equivalence. QED.

## Theorem 2 — one source-preserving third-digit Laurent endpoint

For six corrected Hasse channels \(ab\in\{02,12,03,22,13,04\}\) write
\[
 A_{ab}=\sum_{n=L}^N2^n M_n^{ab,0},\quad
 D_{ab}=\sum_{n=L}^N2^n M_n^{ab,1},\quad
 W_{ab}=\sum_{n=L}^N a_n(J_n^{ab}+E_n^{ab}),
\]
and \(X_{ab}=\sum_{n=L}^N(1-6n)2^nM_n^{ab,0}\). The exact identity
\[
 \boxed{X_{ab}=(1-6p)A_{ab}+12(D_{ab}-W_{ab})}\tag{6}
\]
comes from the definition of \(Y_n\) and (5). In terms of the inherited lower third-digit bracket \(\mathcal L_3\) and genuine upper/infinity bracket \(\mathcal I_3\), define the **full Laurent endpoint** \(\mathcal E_3=\mathcal L_3-\mathcal I_3\). For \(H=\{22,13,04\}\),
\[
\mathcal E_3=
X_{02}+p\left(6A_{02}-\frac{X_{12}+X_{03}}6\right)
+p^2\left(\frac{\sum_H X}{36}-A_{12}-A_{03}\right).
\]
Substitution of (6), canceling mass terms with matching Hasse labels, yields for all such primes
\[
\boxed{\begin{aligned}
\mathcal E_3\equiv{}&
 A_{02}+12(D_{02}-W_{02})
 -\frac p6(A_{12}+A_{03})\\
&-2p[(D_{12}-W_{12})+(D_{03}-W_{03})]
 +\frac{p^2}{36}\sum_H A
 +\frac{p^2}{3}\sum_H(D-W)\pmod{p^3}.
\end{aligned}}\tag{7}
\]
Equation (7) is algebraically valid over the p-local **result**; source coefficients \(a_n\) themselves are p-local at resonant primes, while the rational expression at nonresonant primes may require exact cancellation before reduction. This is a single cross-orientation Ward **source transport**, not proof that \(W\), the separate infinity \(\mathcal I_3\), or the ordered high-high sector \(H_p\) cancels. The inherited original scalar still uses \(\gamma(\mathcal E_3+\mathcal I_3)\) plus the disjoint p² high-high contribution, with \(\gamma=2^{-p}/18\).

## Theorem 3 — resonant face as the rank-zero gluing coefficient

The inherited genuine third-digit lower face is \(F_p=2pC_{12}-p^2(C_{22}+C_{13})/3\), where \(C_{ab}=\delta Y_L^{ab}\). If \(p\mid\delta\), (3) makes the upper-jet face \(0\bmod p^3\), and
\[
 \boxed{\frac{F_p}{p^2}\equiv
 2\,\frac{\delta}{p}Y_L^{12}
 \equiv 2\,\kappa_p^{-1}a_0Y_L^{12}\pmod p.}\tag{8}
\]
This proves the **source/observer bridge**: the third-digit face that reappears at a resonant prime is encoded by the integral rank-zero gluing coefficient of the global Ward telescope. It remains a true face, not a canceled source.

At \(p=733\), \(m=122\), exact finite-ring computation gives
\[
\delta\bmod p^2=176653=733(241),\quad \kappa_p\bmod p=20,\quad
a_0\bmod p=422,\quad Y_L^{12}\bmod p=610.
\]
Thus (8) gives \(F_p/p^2\equiv2\cdot422\cdot20^{-1}\cdot610\equiv87\bmod733\), recovering—not recrediting—the earlier observed \(F_{733}=733^2(87)\) and \(\gamma F_{733}=733^2(430)\bmod733^3\). This explains its mechanism. Conversely at \(p=13\),
\(\delta=4337/2016\), \(a_0=8674/62985\) with \(v_{13}(a_0)=-1\): a universally p-integral left-zero global coefficient vector is impossible there. Preserve the prior nonresonant face rather than extending the p733 regularity to all primes.

## Exact author checks and limits

The companion \`20261026_hourly_d25_global_ward_gluing_resonance_r11_check.py\` was executed in the available Python standard-library local runtime. It checked exact rational adjoint, lower/upper gluing and synthetic Ward telescope for p=7,13,19,31; enumerated all **80 primes** \(p\equiv1\bmod6\), \(7\le p\le997\), finding \(\delta\equiv0\bmod p\) only at p=733 in that finite range; and reconstructed all six corrected Hasse jet channels modulo \(733^3\), checking (5),(6),(7),(8). The p733 endpoint output is \(\mathcal E_3=217853993\bmod733^3\), \(\gamma\mathcal E_3=233027780\bmod733^3\), matching the earlier independently obtained endpoint. It computes Ward \(S\) from finite moments; separate identification of \(S=J+E\) is imported from the cited source proof, not independently rebuilt here. Finite checks do not prove the universal claims (the arguments above do), nor mathematical admission or native CM results.

**BRC — COMPOSE_APPLIED.** This proof preserves integer rank, source labels, upper/lower orientation, p-adic valuation, ordered Hasse population, observer precision and finite cutoff. Rank-zero gluing is an auxiliary coordinate operation, not a primitive native X6 operation or a P000 amendment.

**Next discriminating unit.** Determine whether any all-prime **source-independent p-unit** global telescoper can be obtained with one explicitly retained boundary/corner channel (rather than imposing the nonresonant impossible left-zero gauge), and test at both p13 and p733 with genuine J/E, \(\mathcal I_3\) and independent high-high \(H_p\). Look for a non-tautological cancellation certificate or precise impossibility result; (5)–(7) by themselves are source transport, not annihilation. Parent remains OPEN: real same-original-class \(H_0/B_0\), \([X]U\bmod p^2\), semilinear Frobenius direction/normalization \(\eta\), \(\kappa\), \(\Delta_p-R_p\), native CM experiment, and independent Driver review are missing.

**Control provenance.** Own Research-lane recovery \`r11-20261026-1422-recovery-01\` (#6530) and Source exact continuation \`r11-20261026-1425-continuation-01\` (#6531), full 36,479-character receipt via #6532/#6534, are successful **read-only**. The actual service session is \`MCP-22fdc1ed9a2d44d8bcf5fd6b5cf810dd\` / Researcher \`EM-ENTERPRISE-9C0A7C\`. Native persisted checkpoint remains \`SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED\` with two older completed units; historical latest CLAIM \`MCP-d0d70cd041b01e5db192870a\` differs from checkpoint predecessor \`MCP-87631b892b41fa18d799f2d8\`; no live claim, \`NEEDS_DISPATCH\`, authorization false. The earlier typed identity rejection is not replayed; no new native CLAIM, OPEN, checkpoint, freeze, or review is claimed. Control owner remains enterprise-math #1558, which must resolve the identity/previous-claim CAS conflict under current native authority.
