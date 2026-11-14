# PREFIX-768 / R6 — Exact diagonal Gamma stationary isolation and sharper global mixed-phase bound

Date: 2026-11-14. Frozen scientific input: \`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d\`.
Status: AUTHOR_EXACT_INTEGER_COMPUTATION_WITH_ANALYTIC_REDUCTION / UNREVIEWED / NOT_ADMITTED.
Scope: the **external 189-layer stopped-BRC / independent Gamma-clock maximum auxiliary**, not native X6 dynamics or a completed 1/768 comparator exclusion.

## Statement 768.1 — a 1e-7 stationary-point existence bracket

Use PREFIX-760's rational 189-by-189 Erlang kernels
\[
K_{ij}={\binom{i+j}{i}\over 2^{i+j+1}},\qquad L_{ij}=(i+j+1)K_{ij},
\]
and PREFIX-767's diagonal notation \(s_i(u)=\Pr(T_u>i)\), \(d=s'\), \(e=s''\):
\[
m=2\mathbf1^\top s-s^\top Ks,\quad
v=\mathbf1^\top d-d^\top Ks,\quad
A=d^\top Kd,\quad B=d^\top Ld,\quad
D=B+2v^2-2mA.
\]
For \(D>0\), the local phase ratio \(Q(u)=A(u)/D(u)\) has derivative sign
\[
\operatorname{sgn}Q'(u)=\operatorname{sgn}(A'D-AD'),
\]
where
\[
A'=2e^\top Kd,\quad B'=2e^\top Ld,\quad
v'=\mathbf1^\top e-e^\top Ks-A,\quad
D'=B'+4vv'-4vA-2mA'.
\]

The checker performs a fully exact integer sign-bisection and finds
\[
\boxed{Q'(502971/10^7)<0,\quad Q'(502972/10^7)>0.}
\]
The earlier PREFIX-767 certificate establishes \(D(u)>27787>0\) throughout
\(u\in[251/5000,252/5000]\), which contains the new bracket. Hence
\[
\boxed{\exists u_*\in(502971/10^7,\ 502972/10^7):Q'(u_*)=0.}
\]
The width is \(10^{-7}\), 2,000 times smaller than PREFIX-767's \((0.0502,0.0504)\).
The existence claim does not assert uniqueness or global optimality.

Exact derivative signs were observed at the integer numerators over \(10^7\):
\[
(502900,-),\ (503000,+),\ (502950,-),\
(502975,+),\ (502962,-),\ (502968,-),\
(502971,-),\ (502973,+),\ (502972,+).
\]
Every sign comes from a direct integer comparison of \(A'D-AD'\), with \(D>0\) at all tested points. Continuity is supplied by the finite rational polynomial formulas and the previously proved full-interval denominator bound.

## Statement 768.2 — smaller mixed-curvature threshold witness

For the rational square \(R=[502971/10^7,502972/10^7]^2\), construct the frozen killed-Pascal survival polynomials exactly. Let
\(H=(10^7)^{188}\), \(T=2^{377}\), \(E=H^2T\), \(U(a)=Hs(a)\), \(U(b)=Hs(b)\), \(d=U(b)-U(a)\).
Use integer bilinear forms
\[
C(x,y)=\sum_{i,j} x_i y_j\,\binom{i+j}{i}2^{376-i-j},\qquad
L^*(x,y)=\sum_{i,j}(i+j+1)x_i y_j\,\binom{i+j}{i}2^{376-i-j}.
\]
The exact mixed mean increment is \(E\Delta_R\mu=-C(d,d)\), while
\[
E^2\Delta_R\operatorname{Var}Y=-E L^*(d,d)-
(M_{bb}^2-2M_{ab}^2+M_{aa}^2)
\]
where \(M_{aa}=2HT\sum U(a)-C(U(a),U(a))\),
\(M_{ab}=HT\sum(U(a)+U(b))-C(U(a),U(b))\),
\(M_{bb}=2HT\sum U(b)-C(U(b),U(b))\).

The exact integer checker establishes
\[
\Delta_R\mu<0,\qquad \Delta_R\operatorname{Var}Y<0,\qquad
q_R={\Delta_R\mu\over\Delta_R\operatorname{Var}Y}
<\boxed{\frac{28518591163}{10^{12}}=0.028518591163}.
\]
The displayed ratio is approximately \(0.02851859116286759365445722\); decimal display is **not** the certificate. The strict final inequality is tested by multiplying nonnegative integer numerators and denominators, without an approximate threshold comparison.

For \(V_q=q^2\operatorname{Var}Y-q\mu\),
\(\Delta_RV_q=q\,\Delta_R\operatorname{Var}Y(q-q_R)\).
Thus the global nonnegative mixed-curvature phase threshold from PREFIX-763 satisfies
\[
\boxed{0<q_c\le q_R<0.028518591163}.
\]
This improves the preceding strict upper bound \(0.0285186\). Together with the already verified positive mixed-difference witness from PREFIX-762, every \(q\ge0.028518591163\) has mixed rectangles with both signs.

## Computation, provenance and open issues

- Checker: \`research_notes/portable_direct/PREFIX768_R6_EXACT_PHASE_VERIFY.py\`; result: \`research_notes/portable_direct/PREFIX768_R6_EXACT_PHASE_RESULTS.json\`.
- The author-local exact calculation returned \`ALL_CHECKS_PASS PREFIX768\`. It checks the 189-layer killed-Pascal survivor recursion, 9,529 nonzero survivor positions, final zero row, every integer derivative sign, strict mixed differences, and rational ratio upper bound.
- Arithmetic semantics: Python unbounded integers throughout every proof-relevant comparison; \`Decimal\` is used only to format the final display.
- Scientific science pin and branch-width predicate are unchanged from PREFIX-767. PREFIX-767's whole-interval \(D>27787\) certificate is reused rather than re-proved.
- Not resolved: uniqueness of the stationary point, equality between a diagonal local minimum and the global \(q_c\), or a new genuine \(1/768\) cellwise comparator exclusion. No area/count is added.
- Next discriminating unit: prove or disprove uniqueness of the zero of \(A'D-AD'\) on the isolated rational interval by exact Bernstein/Sturm/interval polynomial sign certification; separately test a genuinely unresolved comparator cell with the finite K,L kernels. Maintain native model versus external auxiliary scope.
