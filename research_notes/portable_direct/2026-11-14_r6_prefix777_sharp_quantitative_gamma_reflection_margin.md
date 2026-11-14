# PREFIX-777 / R6 — Sharp quantitative four-cell Gamma reflection margin

Date: 2026-11-14 (Asia/Shanghai)
Researcher: EM-DIRECT-E77192; Session: MCP-d9aca4ec6e00440eba66035326ea5a4e
Scientific input pinned to: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d
Direct predecessor: PREFIX-776, \`2026-11-14_r6_prefix776_exact_reflection_all_q_grid_nonmodularity.md\`.
Status: AUTHOR_EXACT_INTEGER_AND_ALGEBRAIC_THEOREM / UNREVIEWED / NOT_ADMITTED.

## Domain and statement

Only the **external** 189-layer killed-Pascal first-stop model with two independent unit-rate Gamma clocks is studied. Put
\[
Y(p,z)=\max(C_p,C_z),\quad \mu=\mathbb EY,\quad W=\operatorname{Var}Y,\quad V_q=q^2W-q\mu.
\]
The grid is \(G=\{k/768:0\le k\le768\}\). Let the four fixed cells be
\[
R_{38}=[38,39]^2/768,\quad R_{39}=[39,40]^2/768,
\]
\[
R_{38}^\#=[38,39]\times[729,730]/768,\quad
R_{39}^\#=[39,40]\times[728,729]/768.
\]
For a cell \(R=[a,b]\times[c,d]\), the rectangular mixed difference is
\(\Delta_RF=F(b,d)-F(b,c)-F(a,d)+F(a,c)\).

**Theorem (quantitative all-\(q\) obstruction).** There is an explicitly computed **sharp** positive constant \(C_{\rm four}\), independent of \(q\), with
\[
\frac{27}{10^8}<C_{\rm four}<\frac{271}{10^9},
\quad C_{\rm four}\simeq2.7096259882035419423\times10^{-7},
\]
such that, for *every real* \(q>0\), among the four fixed cells there is a mixed difference \(\ge q C_{\rm four}\) and another \(\le-q C_{\rm four}\).

Here "sharp" means optimal for these four fixed witness cells, not for all cells of \(G^2\) and not for the original native comparator.

## Exact algebraic proof

For \(k\in\{38,39\}\), set \(A_k=-\Delta_{R_k}\mu>0\), \(B_k=-\Delta_{R_k}W>0\), and \(r_k=A_k/B_k\). The inherited exact integer calculation from PREFIX-776 verifies
\[
0<r_{38}<r_{39},\qquad
B_{38}>\frac16,\quad B_{39}>\frac16.
\]
Then
\[
\Delta_{R_k}V_q=qB_k(r_k-q).
\]
PREFIX-776 proves the exact involution \(\Delta_{R_k^\#}V_q=-\Delta_{R_k}V_q\).
Consequently the largest positive difference among the four cells and the magnitude of the most negative one are *both exactly*
\[
q\,E(q),\qquad
E(q)=\max\{B_{38}|q-r_{38}|,\ B_{39}|q-r_{39}|\}.
\]
For \(q\in[r_{38},r_{39}]\), the first term increases and the second decreases, so their maximum attains its unique minimum at
\[
q_0=\frac{B_{38}r_{38}+B_{39}r_{39}}{B_{38}+B_{39}}
=\frac{A_{38}+A_{39}}{B_{38}+B_{39}}.
\]
For \(q<r_{38}\) or \(q>r_{39}\), \(E(q)\) is strictly larger than its minimum inside the interval. Thus
\[
\boxed{C_{\rm four}=\inf_{q>0}E(q)
=\frac{B_{38}B_{39}}{B_{38}+B_{39}}(r_{39}-r_{38})}.
\]
Equality \(E(q_0)=C_{\rm four}\) shows sharpness. Note that \(q_0>0\), so equality occurs within the stated parameter domain.

Use the same integer scalings as PREFIX-776: \(E_0=768^{188}\), \(H=E_0^2\,2^{377}\). If its integer corner differences are \(d\mu_k=H\Delta\mu\), \(dw_k=H^2\Delta W\), put \(a_k=-d\mu_k>0\), \(b_k=-dw_k>0\). Then the **exact rational** constant is
\[
\boxed{
C_{\rm four}=
\frac{a_{39}b_{38}-a_{38}b_{39}}
{H(b_{38}+b_{39})}
}
\]
and the exact minimizer is
\[
q_0=\frac{H(a_{38}+a_{39})}{b_{38}+b_{39}}.
\]
The executable checker reconstructs the frozen 189 killed-Pascal rows, tests 9,529 nonzero survivor positions, reflects the actual grid cells, and verifies the integer inequalities
\[
10^8(a_{39}b_{38}-a_{38}b_{39})
>27H(b_{38}+b_{39}),
\]
\[
10^9(a_{39}b_{38}-a_{38}b_{39})
<271H(b_{38}+b_{39}).
\]
It also checks \(r_{38}<q_0<r_{39}\), \(B_k>1/6\), and the strict ratio ordering. The result is
\[
q_0\simeq 0.0285219091833044830313156.
\]

## Certified stability under pointwise perturbations

For any proposed scalar readout \(\widehat V_q\), suppose that at *every corner* of the four cells,
\[
|\widehat V_q(p,z)-V_q(p,z)|\le\varepsilon.
\]
Each rectangular difference changes by at most \(4\varepsilon\). Hence
\[
4\varepsilon<qC_{\rm four}
\quad\Longrightarrow\quad
\max_R\Delta_R\widehat V_q>0
\quad\text{and}\quad
\min_R\Delta_R\widehat V_q<0.
\]
A completely explicit sufficient bound is
\[
\boxed{\varepsilon\le \frac{27q}{4\cdot10^8}}.
\]
The strict lower bound on \(C_{\rm four}\) makes the non-strict endpoint of this sufficient error condition safe.

This transfer theorem is conditional on an actual pointwise observer error certificate. It does **not** assert that a native X6/BRC comparator satisfies such a bound or that reflection preserves native source, branch, signed-port or event-time provenance.

## Reproducibility, scope and next problem

Source: \`PREFIX777_R6_QUANTITATIVE_REFLECTION_MARGIN_CHECK.py\`.
Result: \`PREFIX777_R6_QUANTITATIVE_REFLECTION_MARGIN_RESULTS.json\`.
Command: \`python3 research_notes/portable_direct/PREFIX777_R6_QUANTITATIVE_REFLECTION_MARGIN_CHECK.py\`.
All decisions use Python arbitrary-precision integers and cross products; decimals are only display. Local result: \`ALL_CHECKS_PASS PREFIX777 SHARP_MARGIN\`. Reuses the exactly defined width predicate and two-Gamma maximum moment kernels of PREFIX-776; no additional 1/768 original comparator exclusion is claimed.

**Next discriminating unit:** on the frozen original comparator, identify whether a *typed* reflected observer can preserve branch/port/provenance; alternatively establish a pointwise \(q\)-dependent scalar discrepancy bound on the 14 distinct corners of the fixed four cells. Either route would determine whether this quantitative certificate transfers beyond the auxiliary Gamma model. P000's six-axis spatial model and three-dimensional slice remain unchanged.