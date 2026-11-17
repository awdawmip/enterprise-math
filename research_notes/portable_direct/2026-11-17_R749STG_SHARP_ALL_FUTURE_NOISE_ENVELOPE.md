# R749STG — Exact monotone all-future noise envelope for the 73/77 binary repair

**17 November 2026 · AUTHOR_EXACT_NOT_REVIEWED · Independent portable research.**

Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Exact predecessor: R749STF at eaca9aaec9f2b38d0e66f6283454e307e8704860. Load-bearing analytic collision theorem R749STB at d2a4436f4ed42aba25a54f9b7015e4c4a776c944 is reused without replaying its proof certificates. P000, ACTIVE worldview and the native X6 spatial/time distinction are unchanged.

## Theorem — more than 500-fold sharper all-horizon conditioning

Consider five *distinctly labeled* nonnegative integer sources with weights (1,1,2,3,6), marking the first unit-weight source. For each integer n>=6 define

\[
\Omega_n=\{k\in\mathbb Z_{\ge0}^5:k_1+k_2+2k_3+3k_4+6k_5\le n-1\},\quad
C_n=|\Omega_n|,\quad T_n=\sum_{k\in\Omega_n}k_1.
\]

Put \(S(n)=18n^4+54n^3-345n^2+2070n-16315\) and

\[
Y_n(e,d)=n^3\frac{T_n+e}{C_n+d}-\frac{S(n)}{108}.
\]

Each cutoff candidate uses the same error pair \((e,d)\in[-2,2]^2\) for all six-step future readouts. The correct one-bit label gives the known cutoff \(q\in\{73,77\}\). Observe \(z_0,z_1\) with \(|z_i-Y_{q+6i}(e,d)|\le\eta\), \(0\le\eta\le10^{-8}\). Invert the first two readings using R749STF's exact two-read inverse and clip both estimated error coordinates to \([-2,2]\), obtaining \((\hat e,\hat d)\). Then

\[
\boxed{\sup_{j\ge0}|Y_{q+6j}(\hat e,\hat d)-Y_{q+6j}(e,d)|\le131\eta.}
\]

For \(\eta>0\), the proved inequality is strict. For \(\eta=0\), inverse reconstruction is exact. The previous all-horizon envelope was \(66000\eta\), so the multiplicative improvement is \(66000/131>503\). The separately certified, sharper fourth-read bound \(103\eta\) remains valid.

## Exact proof

R749STF proved, putting \(\rho=\eta/q^3\),

\[
K_d=2(C_q+C_{q+6}+4),\qquad
M_n=\frac{T_n+2}{C_n-2},\qquad
K_e=C_q+2+(M_q+\tfrac14)K_d,
\]

that two-read inversion followed by clipping satisfies
\(|\hat d-d|\le K_d\rho\), \(|\hat e-e|\le K_e\rho\). Its exact rational-fraction difference law then gives

\[
|Y_n(\hat e,\hat d)-Y_n(e,d)|\le\eta A_q(n),\qquad
A_q(n)=\frac{n^3}{q^3}\frac{K_e(C_n-2)+K_d(T_n+2)}{(C_n-2)^2}
\]

for every \(n=q+6j\), \(j\ge0\). We therefore prove that this explicit envelope decreases at every six-step update.

**Rational quasipolynomials derived from generating functions.** Define \(F_C(z)=\sum_{n\ge1} C_n z^{n-1}\) and \(F_T(z)=\sum_{n\ge1}T_n z^{n-1}\). Marked-source coefficient extraction gives the formal identities

\[
F_C(z)=\frac1{(1-z)^3(1-z^2)(1-z^3)(1-z^6)}
      =\frac{Q_C(z)}{(1-z^6)^6},
\]

\[
F_T(z)=\frac{z}{(1-z)^4(1-z^2)(1-z^3)(1-z^6)}
      =\frac{Q_T(z)}{(1-z^6)^7},
\]

where

\[
Q_C(z)=(1+z+\cdots+z^5)^3(1+z^2+z^4)(1+z^3),
\quad
Q_T(z)=z(1+z+\cdots+z^5)^4(1+z^2+z^4)(1+z^3).
\]

Here \(\deg Q_C=22\) and \(\deg Q_T=28\). For every \(n\ge29\), these yield exact polynomials on residue \(r=n\bmod6\):

\[
C_r(n)=\sum_{u\equiv r-1\;(6)}[z^u]Q_C(z)
\binom{(n-1-u)/6+5}{5},
\quad
T_r(n)=\sum_{u\equiv r-1\;(6)}[z^u]Q_T(z)
\binom{(n-1-u)/6+6}{6}.
\]

The sums run over the actual finite polynomial support; these identities follow algebraically and are not extrapolations from finite samples. Their degrees are respectively 5 and 6.

For each \(q\in\{73,77\}\), use the residue polynomials \(C=C_{q\bmod6}\) and \(T=T_{q\bmod6}\). Let

\[
c(n)=C(n)-2,\qquad h(n)=n^3\left(K_e c(n)+K_d(T(n)+2)\right).
\]

Because \(C_n\) is increasing and \(C_q>2\), all denominators below are positive. Set

\[
\Delta_q(J)=h(q+6J)c(q+6J+6)^2-
            h(q+6J+6)c(q+6J)^2.
\]

Exact rational polynomial expansion establishes \(\deg\Delta_q=18\) and that **all 19 coefficients are strictly positive**, separately for \(q=73\) and \(q=77\). The 38 rational coefficients appear in the result JSON, ordered by increasing power; the Python certificate reconstructs and checks them directly from the generating functions. Hence \(\Delta_q(J)>0\) for every \(J\ge0\) and

\[
A_q(q+6(J+1))<A_q(q+6J).
\]

Therefore the maximum of the entire infinite sequence of error-envelope values occurs at \(j=0\), not merely within a finite checked prefix. Exact initial values are

\[
A_{73}(73)=\frac{62853114965490}{500331290281}
\approx125.6229945766,\qquad
A_{77}(77)=\frac{107417500758858}{820990027225}
\approx130.8389836621.
\]

Both are strictly below 131, proving the theorem.

## Reproducibility, scope and next question

Run the companion R749STG_ALL_FUTURE_MONOTONICITY_CERT.py with Python 3 and SymPy. The program regenerates the labeled-source integer counts; proves the genuine six-residue polynomial formulas by construction; checks four initial values against an independently formed integer recurrence; confirms both degree-18 polynomials have 19 positive rational coefficients; and prints/writes the full machine-checkable R749STG_ALL_FUTURE_MONOTONICITY_RESULTS.json. Arithmetic and comparisons are exact; decimals above are descriptive only. The author-side run returned PASS (38/38 strict positive coefficients). This theorem depends on R749STF's original inversion estimate. The R749STB collision-existence certificate and a typed native X6/BRC embedding remain separate obligations.

**Next scientific units:** search for a five-read exact collision to improve the global \(5\le m_*\le11\) horizon bound; compute an explicit robust five-read separation margin for the pair (602,604) using R749STE's exact elimination obstruction; or construct a source-preserving native BRC Port/Cell realization of the one-bit future repair under P000 with a specified future-operation interface.
