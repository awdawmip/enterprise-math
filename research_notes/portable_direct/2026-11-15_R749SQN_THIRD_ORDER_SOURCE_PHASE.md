# R749SQN — Third-order weighted-source signature and cyclotomic phase residue

Date: 2026-11-15. Status: **AUTHOR_EXACT_NOT_REVIEWED**. Research type: independent auxiliary 16-atom Walsh source-fiber line. Frozen underlying scientific input: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Exact predecessor: R749SQM, \`8429bdaa546e19df05d95ccfb3e55542fb807644\`, \`research_notes/portable_direct/2026-11-15_R749SQM_SECOND_ORDER_WALSH_SOURCE_SIGNATURE.md\`. This note advances the positive integer source-count/moment observer, preserving multiplicity and marked source provenance; it does not assert a native X6 equivalence or change shared task ownership.

## Model, notation and target

Take a finite labeled alphabet of \`d >= 2\` positive integer weights \`s_1,...,s_d\`, of which at least two equal 1. Fix a marked index \`j\`, put \`h=s_j\`, and sample uniformly among nonnegative integer multiplicity vectors \`n\` with \`sum_i s_i n_i <= r-1\` (\`r >= 1\`). Set \`K_r=n_j\`, \`X_r=h K_r/r\`, and \`C_r=#Omega_r\`. Labeled equal-weight source types remain distinct. Define

\[
D=\sum_i(s_i-1),\quad Q=\sum_i(s_i^2-1),\quad W=\prod_i s_i,\quad u=\#\{i:s_i=1\}.
\]

The new question is whether the entire third inverse-resolution mean coefficient is a function of \`(d,D,Q,h)\`, and precisely when an extra integer residue survives the source observer.

## Theorem 1 — smooth third-order universality

Define exact rationals

\[
\begin{split}
A_0&=\frac1{d+1},\\
A_1&=\frac{D+d-1-h(d+1)}{2(d+1)},\\
A_2&=\frac{d((d+1)(h^2-1)-Q)}{12(d+1)},\\
A_3&=-\frac{D+d-1}{2}\,A_2.
\end{split}
\]

If \`u >= 3\`, or if \`u=2\` and the gcd of all \`d-2\` nonunit weights is 1, then along all positive integer \`r\`:

\[
\boxed{\mathbb E[X_r]=A_0+A_1/r+A_2/r^2+A_3/r^3+O_{\bf s}(r^{-4}).}
\]

If \`d=u=2\` (all weights 1), the same formula is exact, with \`A_2=A_3=0\`. The third smooth coefficient introduces **no additional alphabet statistic beyond \`(d,D,Q,h)\`**. In particular, the third correction is \`-(D+d-1)/2\` times the second smooth coefficient.

## Theorem 2 — exact classification of the third-order cyclotomic residue for two unit weights

Suppose \`u=2\`, \`d>=3\`, and \`g=gcd{s_i:s_i>1}>1\`. Define the real rational, period-\`g\` function

\[
S_g^{(3)}(r)=\sum_{\substack{\zeta^g=1\\\zeta\ne1}}\frac{\zeta^{-(r-1)}}{(1-\zeta)^3}.
\]

Then for every fixed such alphabet as integer \`r -> infinity\`,

\[
\boxed{\mathbb E[X_r]=A_0+\frac{A_1}{r}+\frac{A_2}{r^2}+\frac{A_3+\beta S_g^{(3)}(r)}{r^3}+O_{\bf s}(r^{-4})},
\quad
\beta=\begin{cases}
3d(d-1)/(d+1),&h>1,\\
-d(d-1)(d-2)/(d+1),&h=1.
\end{cases}
\]

The periodic function is nonconstant for \`g>1\`; its nonzero Fourier components cannot cancel because their coefficients \`(1-zeta)^(-3)\` are nonzero. Thus the first periodic obstruction for \`u=2\` enters at order \`r^-3\`, whereas for \`u>=3\` none enters through that order. This classification is exact for the stated \`u>=2\` domain; the one-unit second-order sector was treated in R749SQM and is outside this theorem.

## Proof of Theorems 1–2

**Exact generating functions and source-moment bridge.** With \`w=1-z\` and \`T(z)=z^h/(1-z^h)\`, use the deletion of \`k\` marked sources to obtain

\[
F(z)=\sum_{r\ge1}C_r z^{r-1}=\frac1{1-z}\prod_i\frac1{1-z^{s_i}},\qquad
\sum_{r\ge1}C_r\mathbb E[K_r]z^{r-1}=F(z)T(z).
\]

The formula keeps the full labeled positive-weight multiplicity count. In particular, distinct equal-weight sources remain independently sampled; a collapsed weight histogram would change the population.

**Pole at 1.** Direct Taylor expansion of the individual factors \`s w/(1-(1-w)^s)\` gives

\[
F(1-w)=\frac{w^{-d-1}}W(1+a w+b w^2+c w^3+O(w^4)),
\]

\[
a=D/2,\qquad b=D(D+2)/8-Q/24,\qquad
c=(D+2)(D(D+4)-Q)/48.
\]

The absence of a cubic power-sum is substantive: the third logarithmic coefficient of an individual factor is \`(-s^2+4s-3)/24\`, so sums through \`w^3\` use only \`D,Q\`. For the marked source,

\[
h w T(1-w)=1-(h+1)w/2+(h^2-1)w^2/12+(h^2-1)w^3/24+O(w^4).
\]

Put \`P_k(r)=binom(r+k-1,k)\` and expand \`P_k(r)=r^k/k!\` times

\[
1+\frac{k(k-1)}{2r}+\frac{k(k-1)(3k^2-7k+2)}{24r^2}
+\frac{k^2(k-1)^2(k-2)(k-3)}{48r^3}+O(r^{-4}).
\]

The \`z=1\` contributions to \`C_r\` and \`h[z^{r-1}]FT/r\` are respectively

\[
W^{-1}\sum_{j=0}^3 a_j P_{d-j}(r)+O(r^{d-4}),\qquad
(Wr)^{-1}\sum_{j=0}^3 b_j P_{d+1-j}(r)+O(r^{d-4}),
\]

where \`(a_0,a_1,a_2,a_3)=(1,a,b,c)\` and \`b_j=[w^j](1+a w+b w^2+c w^3)(h w T(1-w))\`. Polynomial division gives the four \`A_i\` displayed above, with the identity \`A_3=-(D+d-1)A_2/2\`. (The finite coefficient polynomial for small \`d\` is interpreted with its natural terminating binomial terms.)

**Other roots and uniform error.** At a root of unity \`zeta !=1\`, let \`m_zeta=#{i:zeta^(s_i)=1}\`. The pole order of \`F\` is \`m_zeta\`; for \`FT\` it is at most \`m_zeta+1\`. Their contribution after the ratio and the extra marked \`/r\` is \`O(r^{-(d-m_zeta+1)})\`. If \`m_zeta<=d-3\` for every nontrivial root, the overall ratio remainder is \`O(r^-4)\`. With at least three unit weights this is automatic. With exactly two, it is equivalent to gcd of all nonunit weights being 1.

If exactly two unit weights have nonunit gcd \`g>1\`, the maximal order \`m_zeta=d-2\` occurs precisely for nontrivial \`g\`-th roots. Write \`v=1-z/zeta\`. At those roots,

\[
F(z)=\frac{v^{-(d-2)}}{W(1-\zeta)^3}+O(v^{-(d-3)}).
\]

Consequently, their leading aggregate correction to \`C_r/[r^d/(d!W)]\` is \`d(d-1)(d-2) S_g^(3)(r)/r^3\`. When \`h>1\`, every such root also divides \`h\`, so \`T(z)=1/(h v)+O(1)\`; their leading correction to \`(h/r)[z^{r-1}]FT/[r^d/(d!W)]\` is \`d(d-1) S_g^(3)(r)/r^3\`. When \`h=1\`, \`T\` is analytic there and its numerator contribution begins one order later. Taking the quotient and using \`A_0=1/(d+1)\` yields the stated two values of \`beta\`. Every other root contributes \`O(r^-4)\`. Finitely many roots give a uniform remainder across residue classes. QED.

## A matched-signature provenance pair (new discriminating construction)

Choose labeled alphabets \`A=(1,1,3,3,6)\`, \`B=(1,1,2,5,5)\` and mark the first weight-1 coordinate in each. Both have \`(d,D,Q,h)=(5,9,51,1)\`, hence identical smooth \`A_0=1/6, A_1=7/12, A_2=-85/24, A_3=1105/48\`. But their nonunit gcds are respectively 3 and 1. An exact root-of-unity reduction gives

\[
S_3^{(3)}(r)=\begin{cases}0,&r\equiv1\pmod3,\\1/3,&r\equiv2\pmod3,\\-1/3,&r\equiv0\pmod3.\end{cases}
\]

It follows rigorously that

\[
\boxed{\lim_{\substack{r\to\infty\\r\equiv a\ (3)}}r^3(\mathbb E_A[X_r]-\mathbb E_B[X_r])=
\begin{cases}10/3,&a=0,\\0,&a=1,\\-10/3,&a=2.\end{cases}}
\]

The pair is indistinguishable by \`(d,D,Q,h)\` and by every smooth mean term through order 3, yet it retains a detectable source-period class at precisely that order. The correct reduced observer for these asymptotics must therefore also retain whether the nonunit alphabet has a common periodic divisor, and its residue phase. The construction is an auxiliary positive-count provenance example, not a claim of native X6 dynamical equivalence.

For \`(1,1,2)\` with marked \`h=2\` the smooth third coefficient is \`-27/32\` and the periodic third component is \`(+9/16)(-1)^(r-1)\`. Marking one of the unit weights instead gives smooth \`9/32\` and periodic component \`(-3/16)(-1)^(r-1)\`. Both give independent low-dimensional tests of the root calculation.

## Reproducibility, evidence scope and next problem

\`R749SQN_THIRD_ORDER_SOURCE_CERT.py\` is dependency-free Python using exact integers and \`fractions.Fraction\`. It performs \`2,048\` source-deletion first-moment equalities over eight marked source alphabets (\`r=1..256\`), \`272\` independent recursively enumerated equality checks (\`r=1..34\`), verifies all displayed signatures and produces exact finite mean comparisons through \`r=6002\`. The saved result JSON was produced by executing that code. The source-moment identities and bounded tests are finite checks; the infinite expansions and the three subsequential limits follow from the rational-function/pole argument here. No independent review or Lean check is claimed.

**Next:** classify the one-unit case's order-\`r^-3\` secondary root sectors and determine the first *smooth* order that sees an alphabet statistic beyond \`D,Q\`; analyze how much finite source residual information suffices for preserving the corresponding family of observers. Existing X6 task claims, current native ownership and Source Activity checkpoint are separate control matters.
