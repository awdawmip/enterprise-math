# D25 — corrected Clausen p^4 harmonic channel reduction and endpoint-faithful rank transport

2026-10-26. Author-side portable TASK_RESEARCH; Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; publication \`TP2-B6F4FC938FF94941C1B7\`. **Frozen scientific Source pin unchanged:** \`c47e13e4aba0e006366f989d6334d443f6333ae3\`.

**Status:** AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. This is neither native CM evidence nor Source-native checkpoint, Result, independent review or a JT2 proof.

## Consumed immutable inputs, not re-credited

- \`research_notes/portable_direct/20261025_hourly_d25_clausen_operator_rank_boundary.md\`: corrected rank/Hasse recurrence.
- \`research_notes/portable_direct/20261026_hourly_d25_corrected_clausen_jet_reflection_p4_bridge.md\`: original ordered signed Q corner mod p^4.
- \`research_notes/portable_direct/20261026_hourly_d25_three_channel_clausen_p4_residue_polar_r11.md\` at EM commit \`a4483dc0fb56e7b29f8f85b131e28f08a65ba589\`: the distinct Hasse (0,2),(1,2),(0,3) residue channels and unimodular full rank-moment polar inverse.

The new smallest mathematical unit is to eliminate *independent* evaluation of the third high Hasse channel in the p^4 corner and transport the full shifted corrected rank operator through the existing quadratic moment carrier, including both endpoint fluxes.

## Theorem A — exact logarithmic high-jet elimination

Let p=6m+1≥7 be prime, d=2m, and define (as in the source)

\[
U_r(t)=\frac{(-m-t)_r(-2m-2t)_r}{(1-p/2-3t)_r r!},
\qquad u_{a,r}=[t^a]U_r(t),\quad 0\le r<p.
\]

Work in the p-local rationals; all denominator factors are p-units. Set H_n=Σ_{i=1}^n i^{-1}, D_n=Σ_{i=1}^n(i-p/2)^{-1}; H_0=D_0=0.

For 1≤j≤m,

\[
u_{0,j}=\frac{m!(2m)!}{(m-j)!(2m-j)!j!(1-p/2)_j},\qquad
u_{1,j}=\alpha_j u_{0,j},
\]
\[
\alpha_j=H_m-H_{m-j}+2(H_{2m}-H_{2m-j})+3D_j.
\tag{A1}
\]

For m<j≤2m, u_{0,j}=0 and the non-discardable middle source is

\[
u_{1,j}=\frac{(-1)^{m+j+1}m!(j-1-m)!(2m)!}{(2m-j)!j!(1-p/2)_j}.
\tag{A2}
\]

For every 2m<r<p, u_{0,r}=u_{1,r}=0 and

\[
u_{2,r}=\frac{2(-1)^m m!(2m)!(r-1-m)!(r-1-2m)!}
{r!(1-p/2)_r}\in\mathbb Z_{(p)}^\times,
\]
\[
\boxed{u_{3,r}=u_{2,r}\,h_r,\quad
h_r=H_m+2H_{2m}-H_{r-1-m}-2H_{r-1-2m}+3D_r.}
\tag{A3}
\]

In particular, with g_\ell=2^\ell u_{2,p-\ell} and h^*_\ell=h_{p-\ell}, r=p-\ell,

\[
\frac{g_{\ell+1}}{g_\ell}
=\frac{2r(r-p/2)}{(r-1-m)(r-1-2m)},\qquad
h^*_{\ell+1}-h^*_\ell
=\frac{3(r-1)-4m}{(r-1-m)(r-1-2m)}-\frac3{r-p/2}.
\tag{A4}
\]

All formulas are **exact rational identities**, not merely mod-p observations. Proof: the factors indexed m and 2m in the two numerator Pochhammers are -t and -2t, giving 2t²; factorial evaluation of all remaining nonzero factors proves u_2. Its logarithmic derivative proves h_r. For j≤m the ordinary logarithmic derivative gives α_j; in the middle band only -t survives, giving (A2). Ratios/differences yield (A4). Every inverse is a p-unit on the stated domain.

## Theorem B — original weighted corner from one base-high source plus a middle defect

Retain exactly the original ordered signed cutoff Q_p=Σ_{0≤j,k<p;j+k≥p}(6(j+k)+1)r_jr_k with r_n=(1/6)_n(1/3)_n/[2^n(n!)²]. Put f_j=2^{-j}u_{0,j} (j≤m), b_j=2^{-j}u_{1,j} (m<j≤2m). For 1≤j≤2m, form four source-labelled prefix ports

\[
P_j=\sum_{\ell=1}^j g_\ell,\quad
J_j=\sum_{\ell=1}^j \ell g_\ell,\quad
E_j=\sum_{\ell=1}^j h^*_\ell g_\ell,\quad
F_j=\sum_{\ell=1}^j \ell h^*_\ell g_\ell,
\]
\[
C_j=(6j+1)P_j-6J_j,\quad
C^h_j=(6j+1)E_j-6F_j.
\]

Then for every such prime

\[
\boxed{\begin{aligned}
\frac{Q_p}{p^2}\equiv\frac{2^{-p}}{18}\bigg[
&\sum_{j=1}^m f_j\Big\{C_j+
p\big(6P_j-(\alpha_j C_j+C_j^h)/6\big)\Big\}\\
&-\frac p6\sum_{j=m+1}^{2m}b_j C_j\bigg]\pmod{p^2}.
\end{aligned}}\tag{B1}
\]

Proof: in the already established corrected Clausen p^4 formula, the two next-digit contributions are u_{1,j}u_{2,p-ell} and u_{0,j}u_{3,p-ell}. For j≤m, (A1),(A3) combine them as u0*u2*(α_j+h^*_\ell); for m<j≤2m the u0 contribution vanishes but u1 is retained. The 6p change to the original signed weight gives the +6pP_j term. Reorganizing the exact triangle ell≤j through the four prefix ports proves (B1). It preserves the ordered factor of two, the exact original truncation and both rank populations. Evaluation from precomputed arrays takes O(m) ring operations, not a claimed O(m) bit-complexity theorem.

## Theorem C — full corrected shifted rank/Hasse operator transports to quadratic rank moments, with endpoints

Define f_{a,j}=2^{-j}u_{a,j} and L_a(x)=Σ_{j=1}^{2m} f_{a,j}x^j (L_a=0 for a<0), Θ=x∂_x. Define the **corrected** operators

\[
\mathscr D_0=\Theta(\Theta-p/2)-\tfrac x2(\Theta-m)(\Theta-2m),\qquad
\mathscr D_1=-3\Theta+\tfrac x2(3\Theta-4m).
\]

Summing the exact source rank recurrence gives the finite-polynomial identity

\[
\boxed{\mathscr D_0L_a+\mathscr D_1L_{a-1}-xL_{a-2}
=(m^2\delta_{a0}+2m\delta_{a1}+\delta_{a2})x+
(mf_{a-1,2m}-f_{a-2,2m})x^{2m+1}.}\tag{C1}
\]

The x term is the genuine omitted rank 0; the upper term is the genuine rank 2m+1 flux.

For g_{b,\ell}=2^\ell u_{b,p-\ell} let G_b(z)=Σ_{\ell=1}^{2m}g_{b,\ell}z^\ell and ϑ=z∂_z, with G_b=0 for b<0. The reverse recurrence is

\[
\begin{aligned}
\mathscr R_b={}&(p-\vartheta)(p/2-\vartheta)G_b
-\frac{(p-\vartheta-m)(p-\vartheta-2m)}{2z}G_b\\
&-3(p-\vartheta)G_{b-1}
+\frac{3(p-\vartheta)-4m}{2z}G_{b-1}-z^{-1}G_{b-2}\\
={}&(-10m^2g_{b,1}+7mg_{b-1,1}-g_{b-2,1})\\
&+(3m^2g_{b,2m+1}-4mg_{b-1,2m+1}+g_{b-2,2m+1})z^{2m},
\end{aligned}\tag{C2}
\]

where g_{b,2m+1}=2^{2m+1}u_{b,4m} is a *real outside-port source*, not zero. Derivation: set r=p-\ell in the exact corrected recurrence; the 1≤ell≤2m interior cancels and the truncated ell=1,2m+1 terms give the stated coefficients.

Define full oriented labelled-rank Laurent moments
\[
\mathcal H_{ab}^{(s)}(z)=\sum_{j,\ell=1}^{2m}j^s f_{a,j}g_{b,\ell}z^{\ell-j},
\quad s=0,1,2.
\]

For a=0,1 and b=2,3, substituting x=1/z into (C1) and multiplying **without differentiating G_b** gives

\[
\boxed{\begin{aligned}
&\mathcal H_{ab}^{(2)}-\tfrac p2\mathcal H_{ab}^{(1)}
-\tfrac1{2z}\big(\mathcal H_{ab}^{(2)}-3m\mathcal H_{ab}^{(1)}+2m^2\mathcal H_{ab}^{(0)}\big)\\
&-3\mathcal H_{a-1,b}^{(1)}
+\tfrac1{2z}\big(3\mathcal H_{a-1,b}^{(1)}-4m\mathcal H_{a-1,b}^{(0)}\big)
-\tfrac1z\mathcal H_{a-2,b}^{(0)}
=\tfrac{c_a}{z}G_b,\quad c_0=m^2,\;c_1=2m.
\end{aligned}}\tag{C3}
\]

Thus the shifted corrected source recurrence acts *exactly* through the existing s=0,1,2 full polar moment ports; (C2) shows why a naive endpoint-free adjoint/WZ cancellation is not yet justified. These are exact finite-polynomial identities, not an all-prime CM/JT2 proof.

## Actual arithmetic checks, provenance, and next executable unit

Author executed integer modular arithmetic independent of the source derivations: 80 primes p=6m+1 through 997 passed coefficientwise factorial/harmonic vs corrected Taylor-jet checks, (B1) vs original ordered r_n cutoff computed mod p^4 by both suffix mass/first moment and a literal double sum for p≤127, (C1),(C2) all coefficients, and (C3) bilinear full Laurent moments for a=0,1 and b=2,3. No floating point. Representative triples (p, Q/p² mod p², low, middle): (7,38,10,28), (13,104,78,26), (19,221,183,38), (31,225,907,279), (37,1084,973,111), (43,1563,1348,215), (211,19742,15311,4431). **Finite checks do not prove the whole original conjecture.**

**BRC COMPOSE_APPLIED:** ordered signed (j,ell) cell carrier with rank, corrected parameter Hasse source, valuation/precision, orientation and labelled quadratic moment. (B1) uses the exact smaller scalar observer; (C3) keeps rank degree two and explicit low/high fluxes, avoiding premature quotient. External Laurent z is not a P000 native two-dimensional plane or six-axis transfer.

**Next exact mathematical action:** combine (C3) with the existing signed n≤0 residue operator and the two high endpoint terms in (C2), and test for a genuine non-tautological source-adjoint telescoping identity. Preserve the upper infinity ports and middle defect. **Unfulfilled native obligations:** original-class CM H0/B0, [X]U mod p², Frobenius direction/η, κ mapping, original Δ_p-R_p observable, native benchmark and independent review. D25/LIFT/JT2 remains OPEN.

**Control:** observed service 0.6.11 with Site read-only/no Researcher execution authority; one exact continuation read in this turn returned CONTROL_QUOTA. GitHub issue #1558 preserves historic successful read recovery and the unresolved predecessor CAS mismatch; no current own winning claim/open/run or Source checkpoint was established here. User-prescribed \`chatgpt-research-onhour-enterprise-math-20260923\` and #1558's \`chatgpt-research-hourly-enterprise-math-20260923\` are **distinct strings and not silently coalesced**; the maintenance lane is also separate. Registration/Source-native checkpoint remain pending. No scheduler/configuration changes.

