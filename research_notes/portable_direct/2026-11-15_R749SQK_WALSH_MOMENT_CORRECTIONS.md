# R749SQK — Universal weighted-source moment correction and second-order Walsh bias

Date: 2026-11-15. Status: **AUTHOR_EXACT_NOT_REVIEWED**. Independent auxiliary-source research; no shared native X6 CLAIM, native dynamical equivalence, or review admission asserted.

**Frozen scientific input:** \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`, inherited unchanged from R749SQJ [PR #2499](https://github.com/awdawmip/enterprise-math/pull/2499), head \`3a9e77d610d27661f360bc927d6af348fe8dae81\`. P000 and the six-dimensional Cell worldview are preserved. The subject is the existing **auxiliary 16-atom Walsh source-fiber multiplicity** model.

## Definitions and exact identities

Let \(d\ge1\) and let \(s_1,\ldots,s_d\) be positive integer source weights, at least one equal to 1. Choose one *labeled optional source* of weight \(h=s_j\). For integer \(r\ge1\), sample uniformly from
\[
\Omega_r=\{n\in\mathbb Z_{\ge0}^{d}:\sum_i s_i n_i<r\}.
\]
Define \(C_r=|\Omega_r|\), \(C_t=0\) for \(t\le0\), \(K_r=n_j\), \(X_r=hK_r/r\), source excess \(D=\sum_i(s_i-1)\), and \(W=\prod_i s_i\).

Deleting \(k\) copies of the labeled optional source is an exact bijection:
\[
\Pr(K_r\ge k)=C_{r-hk}/C_r.
\]
The exact source-count generating function is
\[
F(z)=\sum_{r\ge1}C_rz^{r-1}=(1-z)^{-1}\prod_{i=1}^d(1-z^{s_i})^{-1}.
\]

**Theorem A (exact factorial-moment generator).** For a marking variable \(u\),
\[
\boxed{\sum_{r\ge1}C_r\mathbb E[u^{K_r}]z^{r-1}=F(z)\frac{1-z^h}{1-uz^h}},
\]
and for every integer \(p\ge0\),
\[
\boxed{\sum_{r\ge1}C_r\mathbb E[(K_r)_{\underline p}]z^{r-1}
=p!\left(\frac{z^h}{1-z^h}\right)^pF(z).}
\]
*Proof.* The marked optional coordinate contributes \((1-uz^h)^{-1}\) in place of \((1-z^h)^{-1}\). The cumulative-count factor is \((1-z)^{-1}\). Differentiate \(p\) times at \(u=1\). Coefficients are finite integers at every fixed \(r\). QED.

## Universal weighted-source moment theorem

**Theorem B.** For every *fixed integer* \(m\ge1\), along all positive integers \(r\to\infty\),
\[
\boxed{\mathbb E[X_r^m]
=\frac{m!}{(d+1)_m}
\left[1+\frac{m(d-1+D)-h(d+m)}{2r}\right]+O_{m,\mathbf s}(r^{-2})},
\]
where \((d+1)_m=(d+1)(d+2)\cdots(d+m)\).

*Proof.* At \(z=1\), put \(w=1-z\), \(T(z)=z^h/(1-z^h)\). Then
\[
F(1-w)=W^{-1}w^{-d-1}(1+D w/2+O(w^2)),\quad
T(1-w)=(hw)^{-1}-(h+1)/(2h)+O(w).
\]
The first two coefficient terms of the \(p\)th factorial-moment numerator are
\[
[z^{r-1}]p!T^pF=
\frac{p!}{h^pW}\frac{r^{d+p}}{(d+p)!}
\left[1+\frac{(d+p)(d-1+D-ph)}{2r}+O(r^{-2})\right].
\]
In particular
\[
C_r=\frac{r^d}{d!W}\left[1+\frac{d(d-1+D)}{2r}+O(r^{-2})\right].
\]
At any nontrivial root of unity, at least the unit-weight source factor is regular. The other source factors have pole order at most \(d-1\); even when \(T^p\) adds \(p\) more poles, the nontrivial-root coefficient is at most \(O(r^{d+p-2})\). Hence no omitted root affects these two leading powers. For \(d=1\) the identity reduces to the sole unit-weight case.

Use \(K^m=\sum_{p=0}^m {m\brace p}(K)_{\underline p}\). After scaling by \((h/r)^m\), only \(p=m,m-1\) contribute through \(r^{-1}\). The \(p=m-1\) term adds \(h(m-1)(d+m)/2\) to the relative coefficient of the \(p=m\) term, yielding exactly \([m(d-1+D)-h(d+m)]/2\). QED.

**Structural consequence.** The *entire collection* of first-order fixed-moment corrections depends only on \((d,D,h)\). Two labeled-source alphabets sharing those three statistics agree at this precision; a higher-order moment, tail, or full provenance record is needed to distinguish them.

## Frozen Walsh specialization and a sharper mean theorem

For the R749SQJ alphabet, weight multiplicities are
\[
(m_1,\ldots,m_7)=(3,4,6,4,3,2,1),\qquad
(d,D,h)=(23,56,3).
\]
For each fixed \(m\ge1\),
\[
\boxed{\mathbb E[X_r^m]=\frac{m!}{(24)_m}
\left[1+\frac{75m-69}{2r}\right]+O_m(r^{-2}).}
\]
In particular,
\[
\mathbb E[X_r]=\frac1{24}+\frac1{8r}+O(r^{-2}),\quad
\mathbb E[X_r^2]=\frac1{300}+\frac{27}{200r}+O(r^{-2}).
\]

**Theorem C (second-order mean and variance).** On the same frozen model,
\[
\boxed{\mathbb E[X_r]=\frac1{24}+\frac1{8r}-\frac{1357}{144r^2}+O(r^{-3})},
\quad
\boxed{\mathrm{Var}(X_r)=\frac{23}{14400}+\frac{299}{2400r}+O(r^{-2}).}
\]

*Proof.* The established source pole-one expansion is
\[
F(1-w)=W^{-1}w^{-24}(1+28w+(4717/12)w^2+O(w^3)).
\]
Since \(T(1-w)=1/(3w)-2/3+(2/9)w+O(w^2)\),
\[
T F=W^{-1}\big[(1/3)w^{-25}+(26/3)w^{-24}+(1351/12)w^{-23}+O(w^{-22})\big].
\]
Extract exact coefficients using
\([z^{r-1}](1-z)^{-j}=\binom{r+j-2}{j-1}\).
Divide the first-moment count by \(C_r\), multiply by \(3/r\), and expand the resulting rational polynomial quotient. Its first three terms are \(1/24,\ 1/(8r),\ -1357/(144r^2)\). The nontrivial-root pole order is at most 10 for \(F\) and at most 11 for \(TF\), far below these leading coefficients. For variance, subtract the squared mean from the \(m=2\) formula:
\(27/200-2(1/24)(1/8)=299/2400\). QED.

The leading moments coincide with \(\mathrm{Beta}(1,23)\), while the finite-resolution correction carries exact source-multiplicity information.

## Exact computational verification

Companions: \`R749SQK_WALSH_MOMENT_CERT.py\`, \`R749SQK_WALSH_MOMENT_RESULTS.json\`. The standard-library script independently counts each optional-source multiplicity (a) by removing one labeled weight-3 source from the generating function and (b) by subtracting successive cumulative counts \(C_{r-3k}-C_{r-3(k+1)}\). It compares all fibers and moments of order 0–4 at every integer \(1\le r\le2400\), **961,200 exact multiplicity comparisons**; result: **PASS**. Rational checks validate all displayed constants. In that finite window \(\mathbb E[X_r]-1/24\) changes from negative to positive at \(r=39\) and remains positive through 2400; Theorem C establishes eventual positivity, not the earliest global threshold.

**Research status:** AUTHOR_EXACT_NOT_REVIEWED. Exact arithmetic and proof are author-side; independent review and any native X6 observer/Port/Cell bridge remain distinct.

**Next problem:** prove or refute the *global* threshold \(r=39\) for the mean-bias sign by a cyclotomic coefficient inequality, and identify the first higher-order moment residual separating distinct weight alphabets with identical \((d,D,h)\).