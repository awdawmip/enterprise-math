# R749SOX–SOY — Exact zero-gap Walsh onset line and a positive-area zero chamber

Date: 2026-11-14. Research class: **AUTHOR_EXACT_NOT_REVIEWED**.

Frozen scientific pin: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. This research concerns the **auxiliary 16-atom Walsh observer**, not a native two-dimensional plane or a proved X6/V29/V39 correspondence.

Immediate frontiers: R749SOS–SOT ([PR #2399](https://github.com/awdawmip/enterprise-math/pull/2399), \`5f2830988e31eae99d9ef11882e626b56b022552\`); R749SOU–SOV ([PR #2404](https://github.com/awdawmip/enterprise-math/pull/2404), \`986aa94c2ca6323207796b031deff0d7f1283e36\`); R749SOW ([PR #2408](https://github.com/awdawmip/enterprise-math/pull/2408), \`00117309c64e9b1fedb2b920b7b99a22e191a89a\`). Source scientific definitions stay pinned.

## 1. Model

Let \`K=F_2^4\`, with \`chi_m(k)=(-1)^popcount(k&m)\`; use \`A=chi_3\`, \`B=chi_12\`, \`C=chi_15=AB\`. The complete compatible source fiber \`F_(t,s)\` consists of all normalized nonnegative 16-atom laws

\[
p_{t,s,h,u,v,w,z}(k)=\frac{1+t A(k)+s B(k)+h C(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16}.
\]

The free minimax total-variation radius is \(\rho(t,s)=\inf_{q\in\Delta_{16}}\sup_{p\in F_{t,s}}\mathrm{TV}(p,q)\). The calibrated radius is \(\rho^{\rm cal}(t,s)=\inf_{q\in F_{t,s}}\sup_{p\in F_{t,s}}\mathrm{TV}(p,q)\). Put \(g=\rho^{\rm cal}-\rho\).

## 2. R749SOX — full zero-gap onset line to the upper-triangle transition

**Theorem (all real parameters):** For the *entire closed segment*

\[
\frac12\le s\le\frac57,\qquad t=\frac{1+3s}{11},
\]

the exact minimax radii coincide:

\[
\boxed{\rho(t,s)=\rho^{\rm cal}(t,s)=\frac{3-t+s}{8}=\frac{4+s}{11},\qquad g(t,s)=0.}
\]

A minimizing **calibrated** center is \(q_s=p_{t,s,H(s),0,0,0,0}\), with the explicit continuous piecewise-affine coefficient

\[
H(s)=
\begin{cases}
(4-10s)/11,&1/2\le s\le11/20,\\
45(s-7/12)/11,&11/20\le s\le7/12,\\
0,&7/12\le s\le5/7.
\end{cases}
\]

The formulas agree at \(s=11/20\) (\(-3/22\)) and \(s=7/12\) (\(0\)). The former R749SOW zero segment ended at \(s=103/200\); this extends its proven zero line through every \(s\) up to \(5/7\), where \(t+s=1\) and the existing upper-triangle phase is encountered.

### Exact lower certificate

For every \((t,s)\) on this line, the pair

\[
P_+=p(t,s,0,t,t,1-t,s),\qquad
P_-=p(t,s,0,-t,-t,t-1,-s)
\]

lies in the fiber. Each source atom is affine in \(s\) after substituting \(t=(1+3s)/11\). Explicit endpoint checks at \(s=1/2,5/7\) establish nonnegativity and normalization for both sources, with consistent weak signs for each atomwise difference across the endpoints. Their exact total variation is

\[
\mathrm{TV}(P_+,P_-)=\frac{3-t+s}{4}=\frac{2(4+s)}{11}.
\]

The triangle inequality gives \(\rho\ge\mathrm{TV}(P_+,P_-)/2=(4+s)/11\).

### Exact calibrated upper certificate

For each of the three subsegments, consider the **6-dimensional** bounded joint polytope in coordinates \((s,h,u,v,w,z)\) with sixteen source-atom inequalities and two bounds on \(s\). After multiplying by 11, the sixteen inequalities have integer coefficient rows

\[
(3A(k)+11B(k),\,11C(k),\,11\chi_1(k),\,11\chi_2(k),\,11\chi_4(k),\,11\chi_8(k))
\]

and right-hand side \(-11-A(k)\). Each joint polytope has nonempty interior, and every vertex is obtained from six independent active inequalities. The companion Python program exhaustively enumerates all \(\binom{18}{6}=18,564\) possible active bases **per subsegment** using integer Bareiss elimination and exact \`Fraction\` back-substitution.

| Subsegment | Independent bases | Feasible bases | Different vertices | Maximum risk excess |
|---|---:|---:|---:|---:|
| [1/2,11/20] | 11,520 | 436 | 96 | 0 |
| [11/20,7/12] | 11,520 | 432 | 88 | 0 |
| [7/12,5/7] | 11,520 | 844 | 60 | 0 |

Here the exact risk excess is \(\mathrm{TV}(p,q_s)-(4+s)/11\). All tested vertices satisfy the source and center probability constraints; the maximum excess is **exactly zero**. Because both source and chosen center are affine in the six joint variables, and TV minus the claimed radius is convex, the vertex bound extends to the whole polytope, proving the upper inequality for **every real** parameter and all compatible sources. With the lower certificate it proves the theorem.

## 3. R749SOY — a two-parameter positive-area zero-gap chamber

**Theorem (all real parameters):** On the full closed auxiliary-parameter rectangle

\[
\boxed{\frac14\le t\le\frac3{10},\qquad\frac35\le s\le\frac7{10}},
\]

the calibrated center with *zero additional Walsh coefficients*,

\[
q_{t,s}=p_{t,s,0,0,0,0,0},
\]

is minimax among **all** probability centers. In particular,

\[
\boxed{\rho(t,s)=\rho^{\rm cal}(t,s)=\frac{3-t+s}{8},\qquad g(t,s)=0.}
\]

The proven zero-gap rectangle has exact area \(1/200\).

### Lower certificate

Use the same explicit \(P_\pm\) from Section 2, now affine in \((t,s)\). Their atomwise nonnegativity, normalization, fixed-sign TV identity and \(\mathrm{TV}(P_+,P_-)=(3-t+s)/4\) all hold at the four rectangle corners. Affine interpolation and the fixed-sign identity extend these properties to every real point of the rectangle. This proves \(\rho\ge(3-t+s)/8\).

### Upper certificate

In the seven variables \((t,s,h,u,v,w,z)\), intersect the sixteen nonnegative-source-atom inequalities with the four rectangle facets. The resulting joint polytope is bounded and full-dimensional. The companion exact checker examines all \(\binom{20}{7}=77,520\) active seven-facet bases via integer Bareiss elimination. Results:

| Measure | Exact result |
|---|---:|
| Nonsingular bases | 30,208 |
| Feasible bases, with multiplicity | 1,464 |
| Distinct rational vertices | 144 |
| Tight risk-bound vertices | 40 |
| Maximum \(\mathrm{TV}(p,q_{t,s})-(3-t+s)/8\) | **0** |

Every source and center is a valid normalized nonnegative law at each vertex. The upper excess is convex in all seven joint variables; thus the verified vertex bound proves the inequality on the **whole real rectangle**, matching the lower certificate.

For the concrete point \((t,s)=(7/25,3/5)\), the exact common minimax radius equals \(83/200\). Yet \(11t-3s-1=7/25>0\). This is an explicit counterexample to **extrapolating** the R749SOW positive-gap linear formula beyond that earlier theorem's stated parameter trapezoid: at this point \(g=0\). The earlier R749SOW theorem remains valid on its own stated domain.

## 4. Reusable four-orbit / BRC reduction

Write \(a=A(k),b=B(k),i=\chi_1(k),j=\chi_4(k)\), so \(\chi_2=ai\), \(\chi_8=bj\). Each of the four \((a,b)\)-branches contains four atoms, and

\[
16p_{abij}=M_{ab}+iU_a+jV_b,
\quad M_{ab}=1+ta+sb+hab,\quad U_a=u+av,\quad V_b=w+bz.
\]

Therefore the sixteen atomwise source inequalities are **equivalent** to four typed branch inequalities

\[
\boxed{M_{ab}\ge |U_a|+|V_b|\quad(a,b=\pm1).}
\]

The translation group \(G=\{0,3,12,15\}\) preserves the source fiber and TV. Averaging any free minimax center over this group does not raise its maximum source distance. Hence a free minimax center always exists with the three surviving Walsh coefficients \(A,B,C\), i.e. \(q_{\alpha,\beta,\gamma}\) with \(1+\alpha a+\beta b+\gamma ab\ge0\) for all \((a,b)\). A calibrated center is the special case \(\alpha=t,\beta=s\).

For a calibrated center \(q_{h_0}\) and any source \(p\), the exact total-variation expression reduces to four branches:

\[
\boxed{\mathrm{TV}(p,q_{h_0})=
\frac1{16}\sum_{a,b=\pm1}
\left[
\max(|h-h_0|,|U_a+V_b|)+
\max(|h-h_0|,|U_a-V_b|)
\right].}
\]

This follows from \(|x+y|+|x-y|=2\max(|x|,|y|)\) applied to paired branch atoms, and retains the distinct signed source coefficients. It is an exact BRC-style branch-carrier reduction of this *auxiliary* observer, not a native X6 transfer.

## 5. Reproduction, evidence, current limits, next problem

Companion files under \`research_notes/portable_direct/\`:

- \`R749SOX_ZERO_ONSET_SEGMENT_CERT.py\` and \`R749SOX_ZERO_ONSET_SEGMENT_RESULTS.json\`.
- \`R749SOY_ZERO_RECTANGLE_CERT.py\` and \`R749SOY_ZERO_RECTANGLE_RESULTS.json\`.

Run each script with Python 3 standard library only; compare reported segment endpoints, exact integer counts, zero maximum excess and source-pair evidence. All active-basis enumerations use exact arithmetic and certify universal statements by their separately stated polyhedral/convexity argument, rather than treating finite samples as a continuum proof.

**Evidence level:** author-side exact proof with fully reproducible exhaustive finite certificates, awaiting independent mathematical review. Frozen observer and scientific input unchanged. Typed, future-operation-preserving correspondence to native X6/V29/V39 remains open. No shared-task CLAIM or mathematical acceptance is asserted.

**Next:** classify the precise zero-gap polygon adjacent to R749SOY, using the four-orbit formulas to derive a shorter purely analytic upper bound; then locate an actual positive-gap boundary beyond the \((5/22,1/2)\) onset, since the R749SOW line can enter the interior of a zero-gap chamber. Seek independent adversarial review of the certificates and any native bridge separately.
