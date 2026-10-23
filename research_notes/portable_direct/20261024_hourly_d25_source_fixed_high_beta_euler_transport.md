# D25/LIFT — Source-fixed HIGH port basis and exact rank-transport in the cutoff m

2026-10-24 | TASK_RESEARCH, portable mathematical proof | **TWO ALL-m EXACT RATIONAL CERTIFICATES / EXACT AUTHOR CROSS-CHECKS / UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**.

Mother Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication: TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin **c47e13e4aba0e006366f989d6334d443f6333ae3** is unchanged. Research logical lane: chatgpt-research-hourly-enterprise-math-20260923, distinct from maintenance chatgpt-hourly-enterprise-math-20260921. The legitimate service Researcher EM-DIRECT-211CEB has no current winning claim/authorized run; this portable author proof does not turn a GitHub file into a Source checkpoint, Result, review, or native experiment.

Inherited, not new: the original two-seam Gosper forcing, LOW first jet, and HIGH two-sector mod-p transport from research_notes/portable_direct/20261024_onhour_d25_regular_low_jet_high_unit_two_sector_certificate.md, plus the separate auxiliary seam-pair exceptional-prime theorem at research_notes/portable_direct/20261024_hourly_d25_high_pair_modp_rank_exception_211.md. The new result below determines the *actual source-fixed HIGH K coefficients* as distinct rational Euler ports and supplies an exact m-contiguous generating-polynomial transport, including its new boundary terms. It is not a post-hoc adjustable cancellation of the auxiliary pair.

## 1. Exact source-fixed question and four ports

For an integer m>=1 and a target prime p=6m+1, retain the original regular forcing HIGH scalar

\[
\frac{\mathcal U_m^{hi}}p\equiv B_m Z_m^{hi}\pmod p,\qquad
B_m=\frac{(2m-1)!(2m)!}{(4m)!},
\]

with the **existing** two separately labeled intervals

\[
Z_m^{hi}=
\sum_{s=1}^{m-1}a_{m,s}\,k_s^A-
\frac1{24}\sum_{s=1}^{2m-1}c_{m,s}\,k_s^B,
\]

\[
a_{m,s}=2^{m-s}\frac{(2m)!(s-1)!}{(m+s)!(m-1)!},\qquad
c_{m,s}=2^{1-s}\frac{(2m+1)!(m+s-1)!}{m!(2m+s)!},
\]

\[
k_s^A=\frac{4(1-2s)(3s+1)}{(2s+1)(6s+1)},\qquad
k_s^B=\frac{(2-3s)(6s+1)}{3s(3s+1)}.
\]

These k values are fixed by the original Source K_{p,n} modulo p and are **not adjustable coefficients**. The new exact rational partial-fraction facts are

\[
\boxed{k_s^A=-2+\frac4{6s+1}+\frac2{2s+1},\qquad
k_s^B=-2+\frac3{3s+1}+\frac2{3s}.}\tag{PORT}
\]

All four rational poles are separately retained, along with the two base/mass terms, the -1/24 bridge and the physical n=2m seam exclusion. Pole uniqueness is only a statement about these rational functions of s; it does not claim the resulting *finite sums* are independent in every finite field.

Define finite generating polynomials

\[
X_m(z)=\sum_{s=1}^{m-1}a_{m,s}z^{s-1},\qquad
Y_m(z)=\sum_{s=1}^{2m-1}c_{m,s}z^{s-1},
\]

with X_1(z)=0 and Y_1(z)=1. For any polynomial f define the exact Euler-port operator

\[
(\mathcal T_{a,b}f)(z)=\int_0^1 y^{a-1}f(zy^b)\,dy,
\quad
\mathcal T_{a,b}(z^{s-1})=\frac{z^{s-1}}{a+b(s-1)}
\]

for the positive integer pairs used below. Since these are finite polynomial integrals, their coefficients are **exact rational numbers**; there is no analytic continuation or infinite-sum assumption. The source-fixed HIGH scalar has the exact all-m representation

\[
\boxed{
Z_m^{hi}=
\Bigl[\bigl(-2+4\mathcal T_{7,6}+2\mathcal T_{3,2}\bigr)X_m
-\frac1{24}\bigl(-2+3\mathcal T_{4,3}+2\mathcal T_{3,3}\bigr)Y_m
\Bigr]_{z=1}.
}\tag{HIGH-PORT}
\]

Here -2 means -2 times the identity operator. For example, \(\mathcal T_{7,6}\) divides coefficient a_{m,s} by 6s+1 and \(\mathcal T_{3,3}\) divides c_{m,s} by 3s. Equation (HIGH-PORT) follows termwise from (PORT), without deleting any branch or reindexing the original two seams.

## 2. New exact beta-polynomial realization

Write \(P_r(w)=\sum_{j=0}^{r-1}w^j\) for \(r\ge1\), and \(P_0(w)=0\). Then for every m>=1,

\[
\boxed{
X_m(z)=m\binom{2m}{m}2^{m-1}
\int_0^1 (1-t)^m P_{m-1}(zt/2)\,dt,
}\tag{XA}
\]

\[
\boxed{
Y_m(z)=(2m+1)\binom{2m}{m}
\int_0^1 t^m(1-t)^m P_{2m-1}(zt/2)\,dt.
}\tag{YB}
\]

**Proof, coefficient by coefficient.** In (XA), the coefficient of z^{s-1}, 1<=s<=m-1, is

\[
m\binom{2m}{m}2^{m-s}
\int_0^1 t^{s-1}(1-t)^m dt
=m\binom{2m}{m}2^{m-s}\frac{(s-1)!\,m!}{(m+s)!}
=a_{m,s}.
\]

In (YB), for 1<=s<=2m-1, the coefficient is

\[
(2m+1)\binom{2m}{m}2^{1-s}
\int_0^1 t^{m+s-1}(1-t)^m dt
=(2m+1)\binom{2m}{m}2^{1-s}
\frac{(m+s-1)!\,m!}{(2m+s)!}=c_{m,s}.
\]

Each integral is just the elementary integer-parameter beta factorial identity, itself obtainable by repeated integration by parts. Thus (XA)/(YB) are exact polynomial identities for all m, not sampled functional fits.

## 3. New exact m-contiguous rational-Euler transports

Let \(E=z\frac{d}{dz}\). All rational functions of E below act **diagonally on polynomials**, e.g.
\((E+m+2)^{-1}z^{s-1}=z^{s-1}/(m+s+1)\).
This is a finite coefficientwise map, not an infinite-dimensional spectral assertion.

The HIGH sector polynomials obey for **every integer m>=1**:

\[
\boxed{
X_{m+1}(z)=
\frac{4(2m+1)(m+1)}m
(E+m+2)^{-1}X_m(z)
+\frac{4(m+1)}m z^{m-1}.
}\tag{X-SHIFT}
\]

For the second sector define two explicit new boundary coefficients

\[
\eta_m=\frac{(2m+3)!(3m)!}{2^{2m-1}(m+1)!(4m+2)!},
\qquad
\theta_m=\frac{(2m+3)!(3m+1)!}{2^{2m}(m+1)!(4m+3)!}
=\frac{3m+1}{2(4m+3)}\eta_m.
\]

Then

\[
\boxed{
Y_{m+1}(z)=
2(2m+3)\frac{E+m+1}{(E+2m+2)(E+2m+3)}Y_m(z)
+\eta_m z^{2m-1}+\theta_m z^{2m}.
}\tag{Y-SHIFT}
\]

**Proof.** For each old surviving coefficient 1<=s<=m-1, direct factorial cancellation yields

\[
\frac{a_{m+1,s}}{a_{m,s}}
=\frac{4(2m+1)(m+1)}{m(m+s+1)},
\]

while the one new endpoint is \(a_{m+1,m}=4(m+1)/m\). These give (X-SHIFT). Likewise for 1<=s<=2m-1,

\[
\frac{c_{m+1,s}}{c_{m,s}}
=\frac{2(2m+3)(m+s)}{(2m+s+1)(2m+s+2)},
\]

and the only two additional coefficients are
\(c_{m+1,2m}=\eta_m\),
\(c_{m+1,2m+1}=\theta_m\).
Applying these equalities coefficientwise proves (Y-SHIFT). Every formula is in Q, with no prime hypothesis. Together with X_1=0/Y_1=1, this is a complete deterministic finite polynomial construction of the *actual source-fixed HIGH first-digit carrier* for every m.

**Sharp p-local seam at an auxiliary forward cutoff.** If p=6m+1 is prime, coefficients/inverse-E denominators in these transports are p-units at the **original old s ranges**. For m>=2, the new boundary factorials have top index 4m+3<p, hence the entire m->m+1 rational carrier is p-integral. For m=1,p=7, however,

\[
X_2(z)=8,\qquad Y_2(z)=1+\frac z4+\frac{z^2}{14};
\]

the newly introduced \(\theta_1=1/14\) is **not** 7-integral. This is an explicit, localized forward-cutoff exception, not a failure of the Q-identity or a contradiction in the *original m=1 problem*. A proof reducing Y-SHIFT modulo p for all target primes without isolating p=7 would be invalid.

## 4. Source-fixed exceptional-prime 211 comparison, not a fitted observer

For p=211,m=35 (a target prime in p=19 mod 24), use the **original fixed** finite obstruction

\[
\mathcal D_m^{finite}=
\frac{A_m-G_m+B_m}{p}
+J_m^{lo}
+B_mZ_m^{hi}
+\frac{B_m}{9}\bigl(28-6H_{2m}-12q_p(6)\bigr),
\]

where \(A_m=\sum_{n=0}^m(-1)^n2^{-n}\binom mn k_n\),
\(k_n=(1-3n)(6n+3)/((3n+1)(3n+2))\);
\(J_m^{lo}\) is the **inherited** exact LOW first jet,
\(G_m=(-1)^m((2m)!)^3/((3m)!)^2\), and
\(q_p(6)=(6^{p-1}-1)/p\).
The scalar components **in their true Source-fixed order** reduce modulo 211 to

\[
\boxed{
\left(
\overline{(A-G+B)/p},
\overline{J^{lo}},
\overline{B Z^{hi}},
\overline{B(28-6H_{70}-12q_{211}(6))/9}
\right)=(160,62,126,74).
}\tag{211-FIXED}
\]

The total is \(422=2\cdot211\), hence zero mod 211. Additional exact checks:
\[
(\bar A,\bar G,\bar B,\bar Z^{hi})=(162,146,195,124),
\quad
\overline{H_{70}}=184,\quad
q_{211}(6)\equiv127\pmod{211}.
\]

**Independent route for the nonzero HIGH digit:** recursing the **original** R_n from R_0=1 with its exact rational adjacent ratio, and summing \(K_{211,n}R_n/211\) only over 36<=n<140 with n != 70, gives \(126\bmod211\), equal to \(B_{35}Z_{35}^{hi}\) from (HIGH-PORT). The LOW A value was also obtained independently from the two earlier exact Cauchy-port recurrences. All operations used arbitrary-size integers and exact rational reduction with p-unit denominators, not a floating-point fit.

Thus the previously observed **auxiliary** seam-pair degeneration \(H_{35}^{pair}=0\bmod211\) does **not** imply that the original fixed high contribution vanishes: \(B_{35}Z_{35}^{hi}=126\ne0\bmod211\). Moreover the original cancellation uses all four fixed contributions; the freely calibrated auxiliary coefficient s=136 is neither derived from nor substituted into the Source's forcing. The 211 calculation is a finite target-specific cross-check and a useful method-selection witness, **not** a full all-prime LIFT proof.

## 5. Verification / BRC typing / next live mathematical unit

Actual author checks, distinct from the proofs: exact rational coefficientwise verification of (PORT), (X-SHIFT), (Y-SHIFT) and the new-tail formulas for every m=1,...,16; independent factorial/beta formula matching on those coefficient ranges; original-R recurrence comparison of the high sum at p=211; low A computed from both original binomial sum and the inherited two-port recurrence; exact modular computation of (211-FIXED). All passed. The universal statements (PORT), (XA)/(YB), (X-SHIFT)/(Y-SHIFT) are proved by the displayed algebra, not extrapolated from the checks. There was no native-X6 benchmark, independent Driver audit, official Source claim/open, publish_checkpoint, freeze or Result.

Typed BRC use: REUSE_APPLIED and COMPOSE_APPLIED, not a BRC executable run. Carrier retains separately the 1<=s<=m-1 A sector and 1<=s<=2m-1 B sector, signed rational weights, each port, the -1/24 combination, original p-valuation/units and the distinguished n=2m/n=4m seams. Observer is the original regular HIGH mod-p scalar after the lawful division of R_n by p; future operations include shifting m and taking the next p-adic digit. The two polynomial port maps are exact for this observer and do not erase coefficients needed by that cutoff transport; a total-only scalar does not automatically suffice for a future m-shift or higher-digit computation. No promotion to the 6D native model follows.

**Smallest next unfinished unit:** apply the *source-fixed*, exact (X-SHIFT)/(Y-SHIFT) and four Euler ports to derive a closed first p-adic digit for the actual m-contiguous \(B_m Z_m^{hi}\) (including the two new B tails and the p=7 boundary). Combine it with the inherited LOW first-jet transport and the exact (A-G+B)/p/seam and Fermat-quotient terms; seek a terminating finite difference/WZ identity for \(\mathcal D_m^{finite}=0\bmod p\) for all required target primes. Do not replace these fixed coefficients by the adjustable auxiliary seam pair. The native D25 Source still separately lacks the class/map/semilinearity, \(\omega+6\nabla_\lambda\omega\) comparison, leading normalization and same-class divided-power/CM bridge; this author-side paper does not supply them.

Status remains **UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**, parent LIFT OPEN. No frozen scientific Source pin, activity/owner, maintenance conversation, scheduler or notification setting was modified. The existing control-support path is Enterprise Math Issue #1558.
