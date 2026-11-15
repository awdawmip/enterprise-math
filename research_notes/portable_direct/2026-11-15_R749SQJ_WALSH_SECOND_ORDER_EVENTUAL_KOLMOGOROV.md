# R749SQJ — Second-order Walsh provenance tails and eventual exact Kolmogorov maximizer

Date: 2026-11-15. Status: **AUTHOR_EXACT_NOT_REVIEWED**.
Independent auxiliary Walsh continuation of R749SQI, [Draft PR #2497](https://github.com/awdawmip/enterprise-math/pull/2497), head \`9c6b5145e20c652b6dfe9c3a954965230b30e009\`.
Frozen scientific input: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Parameters \((t,s)=(1/10,1/2)\). No native X6 signed-Port/Cell/Link correspondence, shared CLAIM or theorem acceptance is asserted.

## Definitions

There are 23 *labeled* positive-slack source variables with weight multiplicities
\((m_1,\ldots,m_7)=(3,4,6,4,3,2,1)\).
For integer \(r\ge1\), define
\[
 C_r=\#\{(n_1,\ldots,n_{23})\in\mathbb Z_{\ge0}^{23}:\sum_i s_i n_i<r\},\qquad C_t=0\quad(t\le0).
\]
As previously proved, \(\Pr(K_r\ge k)=C_{r-3k}/C_r\), where the optional source contributes weight 3; \(X_r=3K_r/r\). Put \(W=\prod_i s_i=94,058,496,000\).

## Theorem A — Three pole-one coefficients and uniform second-order tail

For \(r\to\infty\),
\[
\boxed{C_r=\frac{r^{23}}{23!W}\left(1+\frac{897}{r}+\frac{2266627}{6r^2}+O(r^{-3})\right).}
\]
Uniformly for all integers \(0\le t\le r\), with \(\alpha=t/r\),
\[
\boxed{\frac{C_t}{C_r}=\alpha^{23}+\frac{897}{r}\alpha^{22}(1-\alpha)
+\frac{\alpha^{21}(1-\alpha)}{r^2}
\left[\frac{2266627}{6}(1+\alpha)-897^2\alpha\right]+O(r^{-3}).}
\]
Here at \(t=0\) the powers vanish and \(C_0=0\). In particular the atom at zero has the sharper third-order expansion
\[
\boxed{\Pr(K_r=0)=1-\frac{C_{r-3}}{C_r}
=\frac{69}{r}-\frac{4968}{r^2}+\frac{372623}{r^3}+O(r^{-4}).}
\]

**Proof.** Put \(w=1-z\). The cumulative weight generating function is
\[
F(z)=\sum_{r\ge1}C_r z^{r-1}=(1-z)^{-1}\prod_{s=1}^7(1-z^s)^{-m_s}.
\]
Writing \(F(1-w)=w^{-24}W^{-1}\prod_s[(1-(1-w)^s)/(sw)]^{-m_s}\) and expanding logarithms,
\[
\log\big(Ww^{24}F(1-w)\big)
=A\,w+L_2w^2+O(w^3),
\quad A=\tfrac12\sum_s m_s(s-1)=28,
\quad L_2=\tfrac1{24}\sum_s m_s(s-1)(5-s)=13/12.
\]
Therefore \(Ww^{24}F(1-w)=1+28w+(4717/12)w^2+O(w^3)\). Extracting the \(z^{r-1}\) coefficient produces the first three terms
\[
\frac1W\left[\binom{r+22}{23}+28\binom{r+21}{22}
+\frac{4717}{12}\binom{r+20}{21}\right].
\]
The \(r^{21}\) coefficient relative to \(r^{23}/(23!W)\) is
\(30107+23\cdot231\cdot28+23\cdot22(4717/12)=2266627/6\).
At any other root of unity, the pole order is at most ten (at \(-1\)), so all remaining contributions have degree at most nine; the omitted terms at 1 have degree at most twenty. This proves the first asymptotic expansion with a genuine integer-uniform quasipolynomial remainder. Substitution \(t=r\alpha\) and algebraic division gives the second formula with error \(O(r^{-3})\) uniform on \(0\le t\le r\): the discarded absolute numerator is \(O((t+1)^{20})\), divided by \(C_r\asymp r^{23}\). Substitute \(t=r-3\) and expand through \(r^{-3}\) to obtain the zero-atom coefficients. \(\square\)

## Theorem B — Eventual exact Kolmogorov maximizer

There exists a finite integer \(R_0\) (not yet made effective) such that, **for every integer \(r\ge R_0\)**,
\[
\boxed{d_K(\mathcal L(X_r),\operatorname{Beta}(1,23))
=\Pr(K_r=0)=1-\frac{C_{r-3}}{C_r}.}
\]
The entire unbounded tail is therefore rigorously settled, while the exact assertion for all \(r\ge1\) still requires an effective \(R_0\) or a separate finite-to-infinite certificate.

**Proof.** First, let \(q_j\) be the number of source multisets of *exact* weight \(j\). Since there are three weight-one types, incrementing the count of any fixed weight-one type injects weight \(j\) objects into weight \(j+1\) objects; therefore \(q_j\) is nondecreasing. Consequently
\[
p_k:=\Pr(K_r=k)=\frac{C_{r-3k}-C_{r-3(k+1)}}{C_r}
\quad\text{is nonincreasing in }k,\quad p_k\le p_0.
\]

Second define \(A_t=C_t/t^{23}\) for positive integers. By Theorem A,
\(A_t=a(1+897/t+(2266627/6)t^{-2}+O(t^{-3}))\),
where \(a=(23!W)^{-1}\). Hence \(A_t-A_{t+1}=a(897/t^2+O(t^{-3}))>0\) for all sufficiently large \(t\). For *each* positive integer \(t\), \(A_t>a\): the continuous open weighted simplex \(\{x_i\ge0:\sum_i s_ix_i<t\}\), of volume \(a t^{23}\), is contained in the union of \(C_t\) unit cubes based at admissible integer vectors by coordinatewise flooring. This inclusion is proper in positive measure (the admissible vector with a weight-one coordinate \(t-1\), and all other coordinates 0, has a unit cube crossing the simplex boundary). Thus \(A_t>a\). Since \(A_r\to a\), each finitely many exceptional small values \(A_t\) eventually exceeds \(A_r\), while the tail is eventually decreasing. It follows that for all sufficiently large \(r\) and every \(0\le t\le r\),
\[
 C_t/C_r\ge(t/r)^{23}.
\]

At every post-jump point \(x=3k/r\), setting \(t=r-3k\) gives
\[
 F_{X_r}(x)-F_\beta(x)=(t/r)^{23}-C_{t-3}/C_r
\le(C_t-C_{t-3})/C_r=p_k\le p_0.
\]
For the pre-jump points, the signed discrepancy is
\((t/r)^{23}-C_t/C_r\le0\). Its absolute value is uniformly at most
\[
\frac{897}{r}\max_{0\le\alpha\le1}\alpha^{22}(1-\alpha)+O(r^{-2})
=\frac{39(22/23)^{22}}{r}+O(r^{-2}),
\]
which is strictly less than \(p_0=69/r+O(r^{-2})\) for sufficiently large \(r\). Between jumps the beta CDF increases continuously and the discrete CDF is fixed, so the absolute extremum is attained at one of these endpoints or limits. At \(x=0\) the discrepancy is exactly \(p_0\). Thus the stated equality holds for all \(r\ge R_0\). \(\square\)

## Exact computational verification

A Python 3 standard-library-only companion \`R749SQJ_WALSH_KOLMOGOROV_SECOND_ORDER_CERT.py\` implements independent 420-step Newton interpolation of the highest three quasipolynomial coefficients, integer DP on the 23 labeled sources, rational coefficients, and exact endpoint checks without float comparisons.

Local execution gave **PASS**: \(C_t/t^{23}\) is nonincreasing for \(t=1,\ldots,10000\); the three leading coefficients agree with the independent 24-sample, period-420 finite-difference extraction; the zero atom equals the full Kolmogorov supremum at \(r=120,420,840,1680,2940,3360,5000,10000\), across **16,234** exact endpoint comparisons. These are finite checks. Theorem B is proved by the argument above, without requiring the checks as its premise.

## Scope and next problem

Theorem B has an existence-only cutoff; the original all-positive-integer conjecture remains open below that unknown cutoff. The strongest next action is to obtain an explicit upper bound on \(R_0\) by bounding the degree-20 pole-one remainder and the lower-order cyclotomic terms, then combine it with an exact finite certificate (or find a global monotonicity theorem for \(C_t/t^{23}\)). This is a provenance-sensitive BRC count statement about an auxiliary Walsh source fiber, not a native dynamical or Foundation theorem.


## New exhaustive finite theorem certificate (all 1 ≤ r ≤ 10,000)

A second standard-library certificate, \`R749SQJ_FULL_GRID_10000_CERT.py\`, checks normalized ratio monotonicity
\(\ C_{t+1}t^{23}\le C_t(t+1)^{23}\ \) for every \(1\le t<10000\) (9,999 exact inequalities), and all negative pre-jump Kolmogorov errors for **every** \(1\le r\le10000\), **16,661,667** exact integer comparisons. All pass. The monotone exact-weight-count injection in Theorem B implies \(p_k\le p_0\); these 9,999 normalized-ratio inequalities imply the full positive post-jump discrepancy bound for every r in that finite range. Therefore
\[
\boxed{\forall r\in\{1,\dots,10000\},\quad d_K(\mathcal L(3K_r/r),\mathrm{Beta}(1,23))=1-C_{r-3}/C_r.}
\]
The second checker was executed and produced PASS; its output is recorded as \`R749SQJ_FULL_GRID_10000_RESULTS.json\`. This finite theorem plus the independent eventual theorem covers a finite initial interval and an unspecified infinite terminal interval. Their possible middle gap remains the precise all-r closure question.
