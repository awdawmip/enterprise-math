# D25/LIFT SB-LOWHALF-D — the genuine R23 low-half observer has only a second-order pole after an authentic one-rank boundary shift

2026-10-27 (Asia/Hong_Kong). Portable TASK_RESEARCH author-side exact proof for logical Research lane \`chatgpt-research-hourly-enterprise-math-20260923\`. Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`; parent D25/LIFT/JT2 OPEN. Frozen scientific Source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\` unchanged. Status \`AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY\`.

## Prior input, disambiguated

Consume these **different, earlier** notes with original priority and credit:

- R23 \`20261027_hourly_d25_half_tail_r23.md\`: authentic low-half discrepancy \(L_p=L_W-L_S\), with \(L_W=\sum_{0\le k\le (p-1)/2}w_k\), \(L_S=\sum s_k\), and original-high W source \(U_p\). It proves \(W_p-S_p\equiv L_p+p^2U_p\pmod{p^3}\), but **not** \(L_p\equiv-p^2U_p\).
- R47/R50: original W/S one-step rational transitions and finite source-faithful Green adjoint.
- R51/R52: ordinary vs. \(\{139,199,277\}\) exceptional old two-endpoint determinant, original free source pair and its correlated jet.
- **Previously published canonical-labelled R53** \`20261027_hourly_d25_original_half_green_precision_r53.md\`: for the **genuine original R23 low-half vector**, the Green coefficients at old endpoints \((d_N,d_{N+1})\) have pole order at most three (exactly three at the three exceptional primes), rather than the four-order poles of an isolated \(d_1\) observer.
- **Previously published canonical-labelled R54/R55** \`20261027_hourly_d25_midpoint_high_chart_lift_r54_r55.md\`: midpoint/high joint chart and full-scalar lift precision. Do not recredit those results.
- Independently verified local-labelled **SB-SHIFT-A** \`20261027_hourly_d25_shifted_green_endpoints_r53_r54.md\`: at all primes \(p\equiv1\pmod6,\ p\ge13\), the adjacent transition difference \(D_{N+1}=a_{N+1}-b_{N+1}\) is a \(p\)-unit. **SB-TRANSFER-C** \`20261027_hourly_d25_green_boundary_relocation_r55.md\`: general exact two-endpoint Green boundary relocation and source correlation. The local R53/R54/R55 numbers in those filenames are not new global sequence IDs; use SB tags.

This note's new theorem composes the *actual* low-half R53 response with SB-SHIFT-A. It is not the earlier \(d_1\)-only shifted pole statement and does not change any original W/S input.

## Theorem — exact third-to-second-order improvement at all three exceptional primes

Let \(p\ge13\) be prime with \(p\equiv1\pmod6\), and let
\[
N=\left\lfloor\frac{3p-1}{4}\right\rfloor+1,\qquad j=N+1.
\]
As in R47, write \(d_k=W_k-S_k\), \(W_1=U\), \(S_1=V\), and let the free labelled source evolution be \(W_k=(w_k/w_1)U\), \(S_k=(s_k/s_1)V\). All original rational coefficients \(w_k,s_k\) are unchanged for the authentic trajectory \((U,V)=(w_1,s_1)\). The exact genuine R23 low-half observation of this free carrier is
\[
\mathcal L_p(U,V)=\frac{L_W}{w_1}U-\frac{L_S}{s_1}V.
\tag{D.1}
\]
Set \(A_j=w_j/w_1,\ B_j=s_j/s_1,\ D_j=a_j-b_j\). The unique shifted two-endpoint coefficients solving \(\mathcal L_p=Q_jd_j+Q_{j+1}d_{j+1}\) are
\[
\boxed{
Q_j=\frac{a_j L_S/s_j-b_j L_W/w_j}{D_j},\qquad
Q_{j+1}=\frac{L_W/w_j-L_S/s_j}{D_j}.
}
\tag{D.2}
\]

**Conclusion A, all target primes:**
\[
\boxed{v_p(Q_j),v_p(Q_{j+1})\ge-3.}
\tag{D.3}
\]
This is a source-preserving *shifted* R23 low-half Green identity, valid for all freely varying labelled inputs, with the original low-half coefficients and source provenance.

**Conclusion B, exact exceptional set \(E=\{139,199,277\}\):**
\[
\boxed{\min\{v_p(Q_j),v_p(Q_{j+1})\}=-2,\quad
v_p(Q_j),v_p(Q_{j+1})\ge-2\quad(p\in E).}
\tag{D.4}
\]
Thus the original R23 low-half readout requires a guaranteed **raw shifted endpoint precision of only \(p^{t+2}\)** to reconstruct it modulo \(p^t\) from independently supplied endpoint digits at each exceptional prime. This improves the old-endpoint \(p^{t+3}\) budget proved for the actual low-half observer in the *earlier* R53 note. This guarantee concerns the stated shifted endpoint pair and independent digit budgets; correlated joint jets may use different storage resources.

**Proof.** In the original labelled free input basis, \(\mathcal L_p\) is the row
\(\ell=(L_W/w_1,-L_S/s_1)\).
At the shifted authentic endpoints \((d_j,d_{j+1})\), their matrix is
\[
\mathsf E_j
=\begin{pmatrix} A_j&-B_j\\ a_jA_j&-b_jB_j\end{pmatrix}
=p^3\mathsf M_j,\qquad \mathsf M_j\in\mathrm{GL}_2(\mathbb Z_p)
\]
by the already established SB-SHIFT-A. Hence \((Q_j,Q_{j+1})=\ell \mathsf E_j^{-1}\), proving (D.2). All low-half original \(w_k,s_k\) are \(p\)-integral since \(k<p\) and all denominators \((k!)^5 216^k,(k!)^4 2304^k\) are \(p\)-units, so \(\ell\) is integral, establishing (D.3).

At each exceptional prime, the **complete finite exceptional-set original factorial certificate** from earlier R53 is now independently recomputed:
\[
\boxed{L_W\equiv L_S\equiv p\pmod{p^2},
\qquad p=139,199,277.}\tag{D.5}
\]
Since \(w_1=7/18,\ s_1=3/32\) are \(p\)-units, \(\ell/p\) is a primitive \(\mathbb Z_p^2\) row. Right multiplication by a unimodular matrix \(\mathsf M_j^{-1}\) preserves primitiveness:
\[
p^2(Q_j,Q_{j+1})=(\ell/p)\mathsf M_j^{-1}
\]
is integral with at least one unit coordinate. Therefore the minimum pole order is exactly two, proving (D.4) for the complete set \(E\). No universal statement is extrapolated from three numerical checks: R51 already proves \(E\) exhausts all exceptional primes, and the algebra handles all others. QED.

## Exact finite witnesses and reproducibility

The standalone Python standard-library author checker \`20261027_hourly_d25_sb4_genuine_lowhalf_movable_green_check.py\` **was actually executed**. It calculates the original factorial low-half sums directly modulo \(p^2\), not a proxy native Hasse computation, on **all 79 primes \(13\le p<1000,\ p\equiv1\pmod6\)**. For the *complete exceptional set* it independently computes the true normalized shifted factorial sources \(w_j/p^3,s_j/p^3\), unit \(D_j\), and exact \(p^2Q_j,p^2Q_{j+1}\) residues:

| p | N | j=N+1 | L_W mod p² | L_S mod p² | w_j/p³ mod p | s_j/p³ mod p | D_j mod p | p²Q_j mod p | p²Q_(j+1) mod p |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 139 | 105 | 106 | 139 | 139 | 84 | 121 | 134 | 130 | 29 |
| 199 | 150 | 151 | 199 | 199 | 179 | 143 | 94 | 20 | 195 |
| 277 | 208 | 209 | 277 | 277 | 175 | 133 | 94 | 175 | 218 |

The checker verified the first-order source updates at the shifted endpoints and the low-half reconstruction congruence in every exceptional row; the last two entries in each row are nonzero, so **both** shifted endpoint coefficients actually have valuation exactly \(-2\) there, a strengthening of (D.4). Exact executable Git blob \`98f0c4967d561e3bf9bf24f8b1286937180e93e3\` was read back from the GitHub connector and matches the actual executed local program.

## BRC, evidence tier, next action

BRC **COMPOSE_APPLIED** to the unchanged signed W/S source pair, real R23 low-half observer and two authentic high endpoints. Explicit shifting of the finite boundary gives a better *actual-observer* information budget: apparent special-prime exceptional poles reflect a chosen lossy pair of boundary readings, not an intrinsic W/S obstruction or a reason to erase finite source labels. This is a rational arithmetic representation, not a native six-dimensional geometry or native X6 three-dimensional-slice result. P000, ACTIVE worldview and frozen scientific Source are unaffected.

**Next precise unresolved scientific task:** Combine the **actual source-labelled** R23 identity \(W_p-S_p=L_p+p^2U_p\bmod p^3\), earlier R53 true half-observer finite boundary, new SB-LOWHALF-D shifted bound, and R36's *different* Picard–Fuchs integral Green inverse. Prove an exact carrier-preserving intertwiner before identifying R50's rank-two second-order residual with R36's polynomial PF source. Only then seek a genuine unchanged-input six-channel fixed-\(z=2\) Hasse J/E telescoping relation at \(p=13,19,139,181,199,277,373\). Original H0/B0, \([X]U\bmod p^2\), Frobenius rank / \(\eta,\kappa\), native \(p=373\) benchmark and independent Driver review remain separate open mother-target obligations.

No native Researcher CLAIM, authorized OPEN/run, \`publish_checkpoint\`, Result, review, or Research-Activity semantic checkpoint is asserted. Preserve old session, 16 prior contributions and neutral staging dispositions under existing control support Issue \`awdawmip/enterprise-math#1558\`; \`REGISTER_PENDING\` until a legitimately authorized registration/write and durable readback.
