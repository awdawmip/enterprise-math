# D25/LIFT — exact Hesse finite-polynomial reflection defect and the first-digit invariant derivative

2026-10-24 · **portable TASK_RESEARCH author derivation** · UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT.

Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, immutable publication \`TP2-B6F4FC938FF94941C1B7\`; frozen scientific pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\` unchanged. Research lane \`chatgpt-research-hourly-enterprise-math-20260923\`. No current native CLAIM, authorized run or native CM benchmark is asserted.

This note **consumes rather than re-credits** the frozen parent \`CM0/SIMPLE\` Legendre/Hesse polynomial relation and the [new same-class Hesse lambda coefficient normalization](https://github.com/awdawmip/enterprise-math/blob/d921541fdc3bb38201d72ba302922769fc837143/research_notes/portable_direct/20261024_hourly_d25_inert_hesse_norm2_frobenius_branch_collision_p2.md). Its new content is a uniform polynomial-level **second-digit reflection-defect certificate**, not the missing divided-power CM \`[X]U\` or original \`Delta_p-R_p\` certificate.

## 1. Exact frozen primitives and first-digit composition

For every target prime \`p=6m+1 >=13\`, set \`n=(p-1)/3=2m\` (even) and define the finite source Hesse-invariant polynomial lift over \`Z_(p)\` by
\[
A_p(X)=\sum_{k=0}^{n}c_kX^k,\qquad
c_k=\frac{(3k)!}{27^k(k!)^3},\qquad
\frac{c_{k+1}}{c_k}=\frac{(3k+1)(3k+2)(3k+3)}{27(k+1)^3}.
\tag{1}
\]
These coefficients are \`p\`-integral because \`k<=n<p\`. The frozen parent identifies, **as polynomials modulo p**,
\[
A_p(X)\equiv P_n(1-2X)\pmod p.
\tag{2}
\]
Indeed the \`k\`-th coefficient of \`P_n(1-2X)={}_2F_1(-n,n+1;1;X)\` is
\(({-n})_k(n+1)_k/(k!)^2\), with \(-n\equiv1/3\), \(n+1\equiv2/3\pmod p\), giving \((1/3)_k(2/3)_k/(k!)^2=c_k\).

Choose the declared quadratic coefficient ring \`R_2=(Z/p²Z)[T]/(T²-2)\` and normalized Hesse parameter from the cited first note:
\[
u=\frac{2-T}{4},\quad \sigma(u)=1-u,\quad
\lambda^3=u^{-1}=4+2T,\quad
\lambda\sigma(\lambda)=2.
\tag{3}
\]
This \(\sigma(T)=-T\) is a **coefficient Frobenius lift**, not a Gauss-Manin or crystalline Frobenius operator. In the mod-\(p\) field put \(t=1-2u=T/2\), so \(t^2=1/2\). The frozen Legendre polynomial is even:
\(P_n(t)=Q_m(t^2)\).
Differentiate the polynomial identity (2) and evaluate at \((3)\):
\[
\boxed{A'_p(u)\equiv-2P'_n(T/2)
=-2T Q'_m(1/2)\pmod p.}
\tag{4}
\]
The frozen parent supplies **the original scalar unit**
\(h\equiv -6Q'_m(1/2)\pmod p\).
Consequently the exact first-digit typed interface is
\[
\boxed{h\equiv\frac3T A'_p(u)
\equiv-\frac{\lambda^4}{T}
\frac{d}{d\lambda}A_p(\lambda^{-3})\pmod p.}
\tag{5}
\]
By the accepted \`SIMPLE\` theorem, both \(h\) and \(A'_p(u)\) are units. The coefficient field conjugation of \(A'_p(u)\) changes its sign modulo p. Equation (5) is a faithful **ordinary first-digit Hesse polynomial** observer; it does not identify the original source-specific \(\partial_\lambda\omega\), \(\kappa\), \(c_p\), H0/B0 basis or the desired product second digit. Those retain their separate operation types and obligations.

## 2. New all-target theorem: divisible polynomial reflection defect

Because \(n=2m\) is even, \(P_n(-t)=P_n(t)\) in characteristic zero. Applying (2) to \(1-X\), one has
\[
A_p(X)-A_p(1-X)\equiv
P_n(1-2X)-P_n(2X-1)=0\pmod p
\tag{6}
\]
**coefficientwise**, not merely at the chosen CM point. Therefore
\[
\boxed{\mathscr D_p(X)=
\frac{A_p(X)-A_p(1-X)}p\ \in\ \mathbf Z_{(p)}[X]}
\tag{7}
\]
is well defined for the exact declared polynomial lift. The completely explicit finite rational polynomial (7) is a source-specific \`p\`-adic reflection **defect**, and by construction obeys the exact antisymmetry
\[
\mathscr D_p(1-X)=-\mathscr D_p(X),\qquad
\mathscr D'_p(1-X)=\mathscr D'_p(X).
\tag{8}
\]
Differentiate (7), use \(\sigma(u)=1-u\), and define the **new, separately typed second-digit even derivative**
\[
\boxed{
E_p=\frac{A'_p(u)+\sigma(A'_p(u))}{2p}
=\frac12\,\mathscr D'_p(u)\pmod p.
}
\tag{9}
\]
The numerator has coefficients divisible by p before evaluating at u, so no nonunit denominator is illegally inverted. By (8), \(\mathscr D'_p(u)\pmod p\) is fixed under \(\sigma\), thus \(E_p\in\mathbf F_p\), not merely \(\mathbf F_{p^2}\). The same source polynomial has the canonical coefficient decomposition
\[
\boxed{
A'_p(u)=pE_p+T B_p\pmod{p^2},\quad
B_p=(A'_p(u)-\sigma(A'_p(u)))/(2T)\in \mathbf Z/p^2\mathbf Z,
\quad h\equiv3B_p\pmod p.
}
\tag{10}
\]
Here \(\mathscr D_p,E_p,B_p\) are **relative to the displayed coefficient polynomial A_p**, whereas a crystalline/CM companion would require an authenticated differential, basis, divided-power lift and semilinear map. Equation (10) does not assert \(h=3B_p\pmod{p^2}\), precisely the missing normalization information.

This is a rigorous *all-target source-polynomial information-loss theorem*: reduction of \(A'_p(u)\) modulo p eliminates the invariant-even layer \(pE_p\), while (7)-(9) reconstruct it exactly in a declared finite polynomial. The coefficient Frobenius/even-odd scalar decomposition preserves provenance and distinguishes the original Hesse lift from unrelated WZ or Cauchy observers.

## 3. Exact independent finite arithmetic witnesses

The author independently reconstructed the rational coefficients using recurrence (1) in \`R_2\`; evaluation of \`A_p(u)\` and \`A'_p(u)\` used multiplication
\((a,b)(c,d)=(ac+2bd,ad+bc)\pmod{p^2}\), and the original source unit \`h mod p\` was separately computed using
\[
B_0=1,\quad B_{k+1}/B_k=(6k+1)(3k+1)/(36(k+1)^2),\quad
h=\sum_{k=0}^{p-1}(12k+1)B_k.
\]
The original \`B_k\` symbol is local to the parent source scalar, not the new odd coefficient \(B_p\) of (10).

| p | A_p(u) mod p² as a+bT | A'_p(u) mod p² as a+bT | original h mod p | E_p=a/p mod p |
|---:|:---:|:---:|---:|---:|
| 13 | (91,78) | (130,119) | 6 | **10** |
| 19 | (152,209) | (304,42) | 12 | **16** |
| 37 | (555,1332) | (962,947) | 29 | 26 |
| 43 | (344,1763) | (43,1456) | 25 | 1 |
| 61 | (2196,2135) | (2989,2734) | 28 | 49 |
| 67 | (402,670) | (2412,2103) | 11 | 36 |
| 211 | (32494,44099) | (42200,16204) | 82 | 200 |

All seven checks give \(A_p(u)=0\pmod p\), \(\operatorname{scalar}(A'_p(u))=0\pmod p\), \(3B_p=h\pmod p\), \(E_p\) as reported, and \(A'_p(u)\) a unit. The nonzero \(E_{13},E_{19}\) are *exact counterexamples to automatically lifting first-digit anti-invariance of this chosen polynomial to mod p²*; **they are not counterexamples to original LIFT/JT2**. Independent mathematical review NOT_RUN, formal checking NOT_RUN, native CM divided-power benchmark NOT_RUN.

## 4. BRC composition, mathematical scope and next exact unit

BRC resolution: \`COMPOSE_APPLIED\` to the source-labelled quadratic carrier \((p,T,\sigma,\lambda,u,A_p,\mathscr D_p,A'_p,E_p,B_p;h)\) with valuations and scalar/parity ports preserved. Allowed operations are finite polynomial differentiation, \(\sigma\), evaluation, mod p² arithmetic, quotient by p **only after exact coefficientwise divisibility** and the first-digit comparison (5). Project P000/X6 is not modified; this is external finite-field/CM auxiliary algebra, not a new native spatial model or physical dynamics. Port collapse to \`h mod p\` is valid for first-digit UR but demonstrably insufficient to recover the even-derivative defect. No arbitrary cohomology-gauge replacement is licensed.

**Last new author frontier:** (7) universal reflection-defect polynomial, (9) guaranteed \(\mathbf F_p\)-valued second-digit scalar, (10) source-resolved p² Hesse derivative split and first-digit \(h\) interface; exact nonzero p=13/19 witnesses. This is a reusable, authenticated-parameter **input candidate**, not a native Source checkpoint or a full equivalent LIFT certificate.

**Exact remaining action:** determine whether the actual Source-bound CM \([X]U\bmod p^2\) with fixed H0/B0 basis and c_p normalization has an explicitly proved transport to this \((B_p,E_p)\) carrier, including the correct semilinearity, Gauss-Manin representative, quartic twist and endpoint \(R_p\). Use the frozen accepted parent and existing actual CM companion records, not a self-imposed \(c_p\) chosen to force the target congruence. Absent that verified map, \(\Delta_p-R_p\) and the mother task remain OPEN. Retain the separate norm-2 Hesse j-branch witness from the first note without equating it to \(E_p\).
