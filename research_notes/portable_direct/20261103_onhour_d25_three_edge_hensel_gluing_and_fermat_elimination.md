# D25 onhour — three edge Hensel gluing and boundary Fermat elimination

**2026-11-03 +08; TASK_RESEARCH, author-side portable mathematics.** Status: AUTHOR-DERIVED / EXACT SCOPED PROOF / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Logical research lane \`chatgpt-research-onhour-enterprise-math-20260923\` (no verified current native session/claim/run); maintenance lane \`chatgpt-hourly-enterprise-math-20260921\` is separate. Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`, immutable scientific pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`.

## Original coefficient and known dependencies

Let \(p=6r+1\ge7\) be prime, \(n=3r\), \(\chi=(6/p)\), and retain the original 216 coefficient and *unshifted ratio*:

\[
b_k=\frac{(2k)!(3k)!}{(k!)^5 216^k},\qquad
\frac{b_{k+1}}{b_k}=R_k=\frac{(2k+1)(3k+1)(3k+2)}{36(k+1)^3}.
\]

Reuse already proved middle boundary and dual Hensel formula (see \`20261103_onhour_d25_middle_h2_hensel_dual_defect.md\` and \`20261103_onhour_d25_complete_low_middle_h2_four_source_lift.md\`):

\[
b_n/p\equiv-2\chi(1+p\varepsilon)\pmod{p^2},
\quad \varepsilon=3+(q_p(2)-3q_p(3))/2\pmod p,
\]
\[
U_s=b_{n-s}/b_n\equiv u_s(1+pE_s)\pmod{p^2}\quad(0\le s<r),
\]
\[
u_s=\prod_{t=1}^s\frac{9(2t-1)^3}{t(36t^2-1)},\
E_s=\sum_{t=1}^s\left(\frac1{2t}+\frac3{6t-1}+\frac3{6t+1}-\frac3{2t-1}\right).
\]

## Theorem A: exact three p-valuation edge ratios

Substitute \(r=(p-1)/6\) directly in the original rational ratio. Every denominator below is a p-unit:

\[
\boxed{R_{2r}/p=\frac{(2p+1)(p+1)}{4(p+2)^3}
\equiv\frac1{32}(1+\frac32p)\pmod{p^2}}\tag{A1}
\]
\[
\boxed{R_{3r}/p=\frac{9p^2-1}{18(p+1)^3}
\equiv-\frac1{18}(1-3p)\pmod{p^2}}\tag{A2}
\]
\[
\boxed{R_{4r}/p=\frac{(4p-1)(2p-1)}{2(2p+1)^3}
\equiv\frac12(1-12p)\pmod{p^2}.}\tag{A3}
\]

**Proof:** the exact equalities are obtained by substituting \(2r=(p-1)/3,\ 3r=(p-1)/2,\ 4r=2(p-1)/3\). Expanding \((1+ap)^{-3}\) to first order proves the p² congruences. This is an exact rational calculation for all stated primes.

## Theorem B: repaired unit observer at the low–middle interface

\(U_{r-1}\) is a p-unit, but \(U_r=b_{2r}/b_{3r}\) has valuation -1. Use the correctly typed boundary observer \(\widehat U_r=pU_r\). Since \(U_r=U_{r-1}/R_{2r}\), A1 gives

\[
\boxed{pU_r\equiv32u_{r-1}[1+p(E_{r-1}-3/2)]\pmod{p^2}.}\tag{B1}
\]

Multiplying by \(b_n/p\) produces the **original** coefficient

\[
\boxed{b_{2r}\equiv-64\chi u_{r-1}
[1+p(\varepsilon+E_{r-1}-3/2)]\pmod{p^2}.}\tag{B2}
\]

The already proved low Hensel formula at this *same original index* is

\[
T_{2r}=\frac{\binom{3r}{2r}\binom{4r}{2r}}{2^{2r}},\quad
h_{2r}=\sum_{i=0}^{2r-1}\Big(\frac1{2(i-3r)}+\frac1{3(i-2r)}+\frac2{3(i-4r)}\Big),
\quad b_{2r}\equiv T_{2r}(1+ph_{2r})\pmod{p^2}.
\]

Matching both exactly valid readouts yields

\[
\boxed{T_{2r}(1+ph_{2r})\equiv-64\chi u_{r-1}
[1+p(\varepsilon+E_{r-1}-3/2)]\pmod{p^2}.}\tag{B3}
\]

In particular \(T_{2r}\equiv-64\chi u_{r-1}\pmod p\), so
\[
\delta_p=\frac{T_{2r}(-64\chi u_{r-1})^{-1}-1}{p}\pmod p
\]
is a well-defined p-integral **boundary jet**. Dividing the unit identity B3 and comparing first-order terms proves

\[
\boxed{\varepsilon\equiv h_{2r}-E_{r-1}+3/2+\delta_p\pmod p.}\tag{B4}
\]

This gives a finite low/middle interface representation of the established Fermat-quotient combination, using both valued carriers rather than discarding either source.

## Theorem C: high entry lifted to p^4 and first third-layer term

By A2 and the established \(b_n/p\) boundary,

\[
\boxed{b_{3r+1}/p^2\equiv(\chi/9)[1+p(\varepsilon-3)]\pmod{p^2}.}\tag{C1}
\]

By A3 and the established high-band \(b_{4r}/p^2\equiv(\chi/9)f_{r-1}\pmod p\),
where \(f_s=(1)_s(5/6)_s(7/6)_s/[2^s(3/2)_s^3]\),

\[
\boxed{b_{4r+1}/p^3\equiv\chi f_{r-1}/18\pmod p.}\tag{C2}
\]

These are exact interface consequences and preserve the distinct high/third-layer valuation ports.

## Consequence for the *frozen mother objective*

For \(p\equiv13,19\pmod{24}\), the previously proved scalar reduction
\[
\Delta_p-R_p\equiv D+C-2\chi(M_1+\varepsilon M_0)+(\chi/9)H\pmod p
\]
becomes, by B4,
\[
\boxed{\Delta_p-R_p\equiv D+C
-2\chi\left[M_1+(h_{2r}-E_{r-1}+3/2+\delta_p)M_0\right]
+(\chi/9)H\pmod p.}\tag{F4-glued}
\]
Here \(D,C,M_0,M_1,H\) are **unchanged** from the prior frozen-source four-port result. This removes the explicit Fermat quotient port from the finite Green/WZ-adjoint input. The right-hand cancellation for all target primes remains the active scientific problem.

## Exact executed evidence

The accompanying standard-library checker reads the original unshifted \(b_k\) independently, including mod \(p^4\) precision for C1 and C2, and verifies A1–A3, B1–B4 and C1–C2 for **all 148 primes \(7\le p\le2000,\ p\equiv1\pmod6\)**. At p=7,13,19,37,43,373 it independently cross-checks original integer binomial coefficients at the boundary positions. All checks passed.

| p | chi | epsilon | E_(r-1) | delta | pU_r mod p² | b_(3r+1)/p² mod p² | b_(4r+1)/p³ mod p |
|---:|---:|---:|---:|---:|---:|---:|---:|
|7|-1|2|0|2|39|17|5|
|13|-1|12|8|1|71|62|5|
|19|1|6|10|0|175|207|1|
|37|-1|32|10|8|375|337|2|
|373|-1|213|82|89|52118|99508|277|

At p=373, \(h_{124}=18\), and \(18-82+3/2+89\equiv213\pmod{373}\). The original \(b_{124}\equiv35604\pmod{139129}\) is recovered on both sides of B3. The portable local executed evidence package additionally retains the checker, full result JSON and continuation; these are not native same-class H0/B0 experiments.

## Durable handoff

**Completed:** exact A1–A3/B1–B4/C1–C2/F4-glued; 148-prime exact validation. **Next exact science action:** construct a signed terminating low/middle/high Green/WZ adjoint for F4-glued, preserving the normalized \(pU_r\) edge boundary and check p=13,19,373 before a universal theorem. **Unresolved:** universal second-digit cancellation; fixed373 native H0/B0 [X]U modulo 139129, module rank, actual semilinear Frobenius and independent verification (support #1559).

The native Source task remains open, without a verified own active session/claim/run. Historical request \`research-onhour-20261031-0205-dispatch-r15\` is not resent. Private adapter reads at 2026-11-03 21:02 +08: old result CONTROL_REQUEST_NOT_FOUND, continuation CONTROL_QUOTA; Sites reports research_authority_granted=false and write_relay_enabled=false. #1558 tracks control support. No Source checkpoint, Result or admission is claimed; this Git record is author-side scientific evidence only. No scheduler or notification change.
