# R749SQI — Cubic-root subleading Walsh residual and sharp Kolmogorov asymptotic

Date: 2026-11-15. Research status: **AUTHOR_EXACT_NOT_REVIEWED**.

This is a portable independent continuation of R749SQG–SQH, [Draft PR #2495](https://github.com/awdawmip/enterprise-math/pull/2495), exact head ac55516617614ad044999145b520f191a28312e9. The scientific input remains frozen at **awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389**. It concerns the auxiliary 16-atom signed Walsh source model at (t,s)=(1/10,1/2); no native X6 signed-Port/Cell/Link transfer is asserted.

## Definitions and inherited exact inputs

The 23 labeled positive-slack source types have the multiplicity vector

\[
(m_1,\dots,m_7)=(3,4,6,4,3,2,1).
\]

For positive integers r, put

\[
C_r=\#\{(n_i)_{i=1}^{23}\in\mathbf Z_{\ge0}^{23}:\sum_i s_i n_i\le r-1\},\qquad C_r=0\ (r\le0).
\]

The exact generating function is

\[
F(z)=\sum_{r\ge1}C_rz^{r-1}=(1-z)^{-1}\prod_{s=1}^{7}(1-z^s)^{-m_s}.
\]

R749SQG proved that C_r=P_{23}(r)+(-1)^{r-1}Q_9(r)+R_{420}(r), with a degree-23 polynomial P, a degree-9 polynomial Q, and a period-420 rational quasipolynomial R whose constituent degrees are at most 7. R749SQH calculated its degree-7 coefficient.

## Theorem 1 — Exact cubic-root degree-six coefficient

For all positive integers r, uniformly as r tends to infinity,

\[
\boxed{R_{420}(r)=A_7(r\bmod3)r^7+A_6(r\bmod3)r^6+O(r^5).}
\]

The coefficient functions are exactly

\[
A_7(0)=-\frac2{4\cdot3^{16}\cdot7!},\qquad
A_7(1)=A_7(2)=\frac1{4\cdot3^{16}\cdot7!},
\]

\[
\boxed{
A_6(0)=-\frac{39}{2\cdot3^{16}\cdot6!},\
A_6(1)=\frac{41}{4\cdot3^{16}\cdot6!},\
A_6(2)=\frac{37}{4\cdot3^{16}\cdot6!}.
}
\]

Equivalently, for every integer r>=1 and h=420, the following identity is **exact**:

\[
\boxed{
\Delta_h^6 R_{420}(r)=h^6\left[
7!A_7(r\bmod3)(r+3h)+6!A_6(r\bmod3)\right].
}
\]

**Proof.** Let \(\rho^3=1,\ \rho\ne1\) and \(w=1-z/\rho\). The six weight-3 factors and two weight-6 factors give a pole of order 8. Write \(A_\rho(w)=w^8F(\rho(1-w))\). The preceding theorem gives

\[
B_\rho=A_\rho(0)=-\frac{\rho^2}{4\cdot3^{16}}.
\]

The logarithmic derivative at w=0 from the singular factors is \(6(3-1)/2+2(6-1)/2=11\). The nonsingular factors with weights congruent to 1 modulo 3 (including the cumulative factor) have weighted multiplicity \(4\cdot1+4\cdot4+1\cdot7=27\), while those congruent to 2 have \(4\cdot2+3\cdot5=23\). Hence

\[
\frac{A_\rho'(0)}{A_\rho(0)}
=11-\frac{27\rho}{1-\rho}-\frac{23\rho^2}{1-\rho^2}
=\frac{106-4\rho}{3}.
\]

The two highest Laurent terms at \(\rho\) are thus

\[
B_\rho(1-z/\rho)^{-8}
+B_\rho\frac{106-4\rho}{3}(1-z/\rho)^{-7}.
\]

For the coefficient of \(z^{r-1}\), this yields

\[
\rho^{-(r-1)}B_\rho
\left[\binom{r+6}{7}
+\frac{106-4\rho}{3}\binom{r+5}{6}\right].
\]

Using \([r^6]\binom{r+6}{7}=3/6!\) and \([r^6]\binom{r+5}{6}=1/6!\), adding the conjugate \(\rho^2\) pole gives

\[
A_6(r)=-\frac{(115-4\rho)\rho^{-r}+
(115-4\rho^2)\rho^{-2r}}{12\cdot3^{16}\cdot6!}.
\]

Evaluating the three residue classes yields the theorem. All other primitive-root orders have pole order at most 4, hence degree at most 3. The remaining cubic-root terms have degree at most 5. Each residue class modulo 420 is an exact degree-at-most-7 polynomial. Apply \(\Delta_h^6r^7=7!h^6(r+3h)\), \(\Delta_h^6r^6=6!h^6\), and annihilation of degrees at most 5 to conclude the exact identity. \(\square\)

## Theorem 2 — A sharp finite-resolution convergence constant

Let \(K_r\) count use of the optional source, sampled uniformly among the \(C_r\) eligible source multisets, and define \(X_r=3K_r/r\). The inherited exact tail formula is

\[
\Pr(K_r\ge k)=\frac{C_{r-3k}}{C_r}.
\]

For every integer \(r\to\infty\), **uniformly over all integers \(k\ge0\) with \(3k\le r\)**,

\[
\boxed{
\frac{C_{r-3k}}{C_r}=
(1-3k/r)^{23}
+\frac{897}{r}(1-3k/r)^{22}(3k/r)+O(r^{-2}).
}
\]

Consequently \(X_r\) converges weakly to \(\operatorname{Beta}(1,23)\) and, with the standard Kolmogorov distance between real CDFs,

\[
\boxed{\lim_{r\to\infty}r\,
d_K(\mathcal L(X_r),\operatorname{Beta}(1,23))=69.}
\]

The sharp first-order discrepancy is the atom at zero:

\[
\Pr(K_r=0)=1-C_{r-3}/C_r=69/r+O(r^{-2}).
\]

**Proof.** The pole-1 polynomial calculated in SQG has the first two powers

\[
C_t=\frac{t^{23}}{23!\,W}
+\frac{39t^{22}}{22!\,W}+O((t+1)^{21}),\qquad
W=94,058,496,000.
\]

This remainder estimate is uniform over positive integers because F has a finite root-of-unity partial-fraction expansion. Defining \(C_0=0\), division by the expression for \(C_r\) gives, uniformly over integers \(0\le t\le r\),

\[
C_t/C_r=(t/r)^{23}
+(897/r)(t/r)^{22}(1-t/r)+O(r^{-2}).
\]

Insert \(t=r-3k\) to obtain the uniform tail formula.

To compute the full CDF distance, for \(x\in[0,1)\) let \(k=\lfloor rx/3\rfloor\), \(\alpha=1-x\), and \(h=3-r(x-3k/r)\), so \(0<h\le3\). Except in the final interval where the discrete CDF is already 1 (the error there is \(O(r^{-23})\)), put \(t=r-3(k+1)=r\alpha-h\ge0\). As the beta CDF equals \(1-(1-x)^{23}\), its difference from the discrete CDF is uniformly

\[
F_{X_r}(x)-F_{\mathrm{Beta}}(x)
=\frac{\alpha^{22}}r[23h-897(1-\alpha)]+O(r^{-2}).
\]

The positive leading coefficient never exceeds 69. The magnitude of the negative leading coefficient is at most

\[
897\max_{0\le\alpha\le1}\alpha^{22}(1-\alpha)
=39(22/23)^{22}<69.
\]

Thus \(\limsup r\,d_K\le69\). At \(x=0\), the continuous beta CDF is zero while the discrete CDF equals the atom \(1-C_{r-3}/C_r=69/r+O(r^{-2})\), proving the matching lower bound. \(\square\)

## Reproducible exact verification

Run the sibling Python-3 standard-library certificate:

    python3 research_notes/portable_direct/R749SQI_WALSH_CUBIC_SUBLEADING_CERT.py > research_notes/portable_direct/R749SQI_WALSH_CUBIC_SUBLEADING_RESULTS.json

The script independently builds cumulative integer partition counts for 23 labeled source types; uses exact Fraction Taylor recurrences for the full pole-1 and pole-minus-1 principal parts; checks all 420 residue classes of the sixth step-420 difference (using counts to r=2940); and enumerates both sides of every support jump to compute the exact Kolmogorov supremum for r=30,60,120,420,840,1680,2940. The observed result was PASS; all seven finite suprema equal their zero atoms. These finite cases are consistency checks, not the proof of the general theorem. The full proof above supplies the infinite-domain result.

All statements are internal to the frozen auxiliary Walsh source model, without an asserted native P000/X6 observer identification. The BRC-relevant output is explicit, provenance-aware source counting with a sharp error coefficient; this research remains pending independent review.

## Open next question

Determine whether for **every** positive integer r the exact Kolmogorov supremum is attained at the zero atom, rather than merely to first asymptotic order and in the seven tested cases. Independently derive an explicit nonasymptotic constant B in the bound \(d_K\le69/r+B/r^2\), or compute the next (degree-5) cubic-root coefficient. Preserve the unchanged scientific pin and contributor/provenance distinction.
