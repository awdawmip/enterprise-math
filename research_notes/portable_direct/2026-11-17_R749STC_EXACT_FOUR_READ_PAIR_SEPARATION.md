# R749STC — Exactly four reads are necessary and sufficient for the cutoff pair (73,77)

**2026-11-17.** Evidence status: AUTHOR_EXACT_NOT_REVIEWED; companion scientific pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Independent portable research, within the same five-distinct-source auxiliary scalar observer as R749STA/R749STB.

## Main theorem

For the two distinct cutoffs \(q=73\) and \(p=77\), with **each** candidate using a fixed but arbitrary real error pair in \([-2,2]^2\) across its reads,
\[
\boxed{\mathcal O_{73}^{(4)}(e,d)\ne\mathcal O_{77}^{(4)}(E,D)
\quad \forall e,d,E,D\in[-2,2].}
\]
By the previously proven R749STA/R749STB exact three-read collision for these same two cutoffs, their **pairwise minimal exact observation horizon is exactly four.** This establishes the exact threshold for one pair, leaving the full unbounded all-cutoffs optimal horizon between four and eleven.

## Same frozen definitions and source counting

Five **separately labeled** sources have weights \((1,1,2,3,6)\). Let \(C_n\) count nonnegative five-tuples with weighted sum at most \(n-1\), and \(T_n\) sum their first coordinate. With \(S(n)=18n^4+54n^3-345n^2+2070n-16315\), use
\[
Y_n(e,d)=n^3(T_n+e)/(C_n+d)-S(n)/108.
\]
The four readouts are \(Y_{n+6j}(e,d)\) for \(j=0,\ldots,3\). The source counts independently reconstructed by the companion program include
\[
(C_{73},T_{73})=(707343,8931013),\quad
(C_{77},T_{77})=(906087,12046216),
\]
\[
(C_{91},T_{91})=(1978664,30933812),\quad
(C_{95},T_{95})=(2422568,39491884).
\]

## Elimination of arbitrary error parameters

Set \(a_j=73+6j,\ b_j=77+6j\) and
\[
x_j=(Y_{a_j}(e,d)+S(b_j)/108)/b_j^3,\quad
v_j=x_jC_{b_j}-T_{b_j}.
\]
The first two equalities impose \(E-x_jD=v_j\), hence
\[
D=\frac{v_0-v_1}{x_1-x_0},\qquad E=v_0+x_0D.
\]
The companion certificate shows \(x_1-x_0>0\) on the relevant exact bounded error rectangle; the previously established two-read conditioning result R749SSW also supplies positivity. In particular the rational map is well defined.

Matching the third read requires
\[
F(e,d):=(v_0-v_1)(x_2-x_0)-(v_0-v_2)(x_1-x_0)=0.
\]
Matching the fourth requires
\[
R_4(e,d):=Y_{95}(E(e,d),D(e,d))-Y_{91}(e,d)=0.
\]
Let \(P,Q\in\mathbb Z[e,d]\) be the primitive numerator polynomials of the reduced rational functions \(F,R_4\). Thus a four-read collision makes both \(P\) and \(Q\) vanish. Their exact Sylvester resultant \(\operatorname{Res}_d(P,Q)\) factors into **three linear factors and one quintic**, all with multiplicity one. The actual factor list is generated, reproduced and included in the machine certificate.

By exact Sturm real-root counts: the linear factors have **zero** real roots in \([-2,2]\); the quintic has **exactly one** real root there, confined to
\[
\boxed{3306/10000<e<3307/10000.}
\]
No other first-error value in the admissible square could participate in a four-read collision.

## Exclusion of the sole possible e interval

For every e in the exact rational bracket \([3306/10000,3307/10000]\), the following inequalities are proved exactly:

1. \(\partial F/\partial d>0\) for the full \(d\in[-2,2]\);
2. \(F(e,-1)>0\), hence any \(d\in[-2,2]\) satisfying \(F(e,d)=0\) must lie in \([-2,-1)\);
3. \(E(e,d)>2\) whenever \(d\in[-2,-1]\);
4. \(x_1-x_0>0\) on all \(d\in[-2,2]\).

These four claims follow from **50 strictly positive rational bivariate Bernstein coefficients in eight numerator/denominator polynomials** over the corresponding exact rectangles, as recorded in the companion JSON. Thus any possible four-read solution would demand \(E>2\), contradicting the admissible error square. This proves the theorem.

This proof uses full exact algebra, Sturm root counts and coefficientwise positivity over continuous parameter boxes. It is **not** a finite sample test or an inference from numerical optimization.

## Reproduction and scope

Run Python 3 with SymPy:
`python R749STC_FOUR_READ_PAIR_SEPARATION_CERT.py`
Expected status: PASS 50 strict Bernstein coefficients; resultant roots isolated; q73/p77 minimal exact horizon 4. The script writes R749STC_FOUR_READ_PAIR_SEPARATION_RESULTS.json, containing exact resultant factor polynomials, exact root counts and exact Bernstein minima.

The exact pairwise theorem is compatible with the analytic three-read collision sheet in R749STB: the first three reads are identical along a continuum of states, while the fourth always distinguishes these two fixed cutoff values. No cross-pair global separation claim follows solely from this pair. The model is auxiliary to P000's six-axis signed Cell ontology and typed time; native X6/BRC application requires a verified embedding preserving source labels, event order and future observer operations.

## Next

Test other cutoff pairs for four-read exact aliases and distinguish eventually sufficient four-read *residue* identification from full cutoff identification; seek an all-pairs bound improving eleven. Investigate computationally effective lower bounds on the four-read separation margin for bounded cutoffs, retaining the future-observer residual as an explicit BRC repair coordinate.

**Status:** AUTHOR_EXACT_NOT_REVIEWED; mathematical author certificate only. Independent portable artifact; no shared CLAIM, Result, Review or Foundation authority.
