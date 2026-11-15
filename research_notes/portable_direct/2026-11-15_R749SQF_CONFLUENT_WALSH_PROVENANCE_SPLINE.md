# R749SQF — Exact Walsh provenance tails, independent Dirichlet residual and confluent spline

Date: 2026-11-15. Research status: **AUTHOR_EXACT_NOT_REVIEWED**.

**Scope and pins.** This is an independent portable continuation of R749SQE, whose exact source is [research artifact at immutable commit 087166f4](https://github.com/awdawmip/enterprise-math/blob/087166f458cef7c564d4e4df1de7c58846075861/research_notes/portable_direct/2026-11-15_R749SQE_WALSH_BOUNDARY_DIRICHLET_LIMIT.md). Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. The object is the **auxiliary 16-atom signed Walsh source model** at $(t,s)=(1/10,1/2)$, not an identified native X6/Port observer. The preceding 33 first-grid points, 25 forced source letters and R749SQB/SQD boundary classification remain inherited author-level hypotheses pending independent review.

## 1. Exact finite source-residual law

In the R749SQE model there are 23 positive-slack source letters with positive integer slacks $s_i$. One distinguished optional letter, indexed $*$, has $(s_*,b_{0,*},b_{1,*})=(3,2,1)$. All other 22 letters have $b_{0,i}=b_{1,i}$. For each integer $r\ge1$, let

\[
L_r=\{m\in\mathbb Z_{\ge0}^{23}:\sum_i s_im_i\le r-1\},\quad
C_r=|L_r|\quad(r\ge1),\quad C_r=0\quad(r\le0).
\]

Sample $m$ uniformly from $L_r$, and define $K_r=m_*$ and $Y_{j,r}=\sum_i b_{j,i}m_i$.

**Theorem A (all-depth tail and disintegration).** For all $r\ge1$ and integers $k\ge0$,

\[
\boxed{\Pr(K_r\ge k)=\frac{C_{r-3k}}{C_r}},\qquad
\boxed{\mathbb EK_r=\frac{1}{C_r}\sum_{k=1}^{\lfloor(r-1)/3\rfloor}C_{r-3k}}.
\]

Conditional on $K_r=k$ with positive probability, the other 22 multiplicities are uniform over $\sum_{i\ne *}s_im_i\le r-1-3k$. Moreover $Y_{0,r}-Y_{1,r}=K_r$ pointwise. The ordinary generating function is

\[
\sum_{r\ge1}C_rz^{r-1}
=\frac{1}{(1-z)\prod_{i=1}^{23}(1-z^{s_i})}.
\]

The optimal formal missing-pattern source transport formula from R749SQE therefore becomes the directly computable exact sequence identity

\[
\boxed{W_1(r,n)=
\frac{\sum_{k=1}^{\lfloor(r-1)/3\rfloor} C_{r-3k}}{20nC_r}}
\quad(n,r\ge1).
\]

**Proof.** Subtract $k$ copies of the optional letter to biject $\{m\in L_r:m_*\ge k\}$ with $L_{r-3k}$. Fixing the optional multiplicity gives the conditional distribution; summing the integer survival probabilities yields the expectation. Product geometric series give the generating function. The established source-pairing has nonnegative readout shift $K_r$, so its cost equals the mean-difference dual lower bound, proving the transport formula. The convention $C_s=0$ for $s\le0$ includes all boundary cases.

## 2. An independent two-variable representation of the entire joint limit

R749SQE established a 24-coordinate Dirichlet$(1,\ldots,1)$ limit. Denote the optional barycentric coordinate by $Z_*$ and define

\[
K=Z_*/3,\qquad W_i=Z_i/(1-Z_*)\quad(i\ne *),
\]

where the remaining 23 indices include the zero-slack barycentric coordinate. The gamma construction implies that $K$ and $W$ are independent, $Z_*\sim\operatorname{Beta}(1,23)$ and $W\sim\operatorname{Dirichlet}(1^{23})$. Set $a_0=0$ and, for the 22 compulsory positive-slack letters, $a_i=b_i/s_i$. Let $S=\sum_{i\ne *}a_iW_i$.

**Theorem B (independence, joint law and residual density).** The R749SQE joint limit has the exact representation

\[
\boxed{(Y_0,Y_1,K)=
\bigl(2K+(1-3K)S,\ K+(1-3K)S,\ K\bigr),\qquad S\perp K.}
\]

Its residual marginal has **explicit density**

\[
\boxed{f_K(k)=69(1-3k)^{22}\mathbf1_{(0,1/3)}(k)},\qquad
\Pr(K\ge k)=(1-3k)^{23}\quad(0\le k\le1/3).
\]

Thus $\mathbb EK=1/72$ and $\operatorname{Var}K=23/129600$. The joint support of $(Y_1,K)$ is the triangle $0\le k\le1/3$, $k\le y\le2-5k$, with $Y_0=Y_1+k$. If $f_S$ is given by Theorem C below, its explicit joint density in the interior is

\[
\boxed{f_{Y_1,K}(y,k)=
69(1-3k)^{21}f_S\!\left(\frac{y-k}{1-3k}\right).}
\]

**Proof.** Normalize independent unit-shape gamma variables to obtain the Dirichlet vector. The distinguished gamma ratio is Beta$(1,23)$, independent of the normalized 23 other gamma variables. The optional readout coefficients are exactly $2/3$ and $1/3$; all other coefficients coincide. Substitute $Z_*=3K$. The density follows from $z=3k$, and the support and joint density follow by the one-dimensional affine change of variables conditioned on $K$.

## 3. Complete rational knot list and explicit confluent B-spline

The exact 23 conditional knots have 12 distinct rational values:

| Knot $a$ | 0 | $1/4$ | $1/3$ | $1/2$ | $4/7$ | $3/5$ | $2/3$ | $3/4$ | $4/5$ | 1 | $4/3$ | 2 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Multiplicity $m_a$ | 6 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 2 | 4 | 1 | 1 |

Define

\[
R(z)=\prod_a(z-a)^{-m_a},\qquad
P_a(z)=\prod_{b\ne a}(z-b)^{-m_b},\qquad
c_{a,j}=\frac{P_a^{(m_a-j)}(a)}{(m_a-j)!}.
\]

Then $R(z)=\sum_a\sum_{j=1}^{m_a}c_{a,j}(z-a)^{-j}$.

**Theorem C (fully specified rational spline).** For every real $x$,

\[
\boxed{
F_S(x)=\sum_a\sum_{j=1}^{m_a}
(-1)^{j-1}{22\choose j-1}\,
c_{a,j}\,(x-a)_+^{23-j}.}
\]

This is an **explicit finite 23-term formula** with rational coefficients determined by the displayed 12-knot table; its derivative $f_S$ is a continuous piecewise polynomial density of degree at most 21 on $[0,2]$. The 12 knots are the complete possible change points and split the support into 11 rational intervals. No numerical interpolation is required.

**Proof.** For 23 pairwise distinct knots, the uniform-simplex linear-image CDF is the Hermite–Genocchi divided difference of the truncated-power function:

\[
F(x)=\sum_i \frac{(x-a_i)_+^{22}}{\prod_{j\ne i}(a_j-a_i)}.
\]

Equivalently it is the $(-1)^{22}$ residue sum of $(x-z)_+^{22}/\prod_i(z-a_i)$. When knots coalesce, the simplex pushforward converges and the repeated-pole partial fractions give the $j$th residue term via the $(j-1)$st derivative of the truncated power. That derivative is $(-1)^{j-1}22!/(23-j)!\,(x-a)_+^{23-j}$; dividing by $(j-1)!$ yields the binomial coefficient in the formula. Every $m_a<23$, so the law has no atom and differentiation yields the claimed density.

Exact rational moment consequences, verified both by integrating the above piecewise polynomial and by independent Dirichlet symmetric-polynomial identities, are

\[
\begin{aligned}
\mathbb ES&=\frac{482}{805},&
\mathbb ES^2&=\frac{17950601}{48686400},\\
\mathbb ES^3&=\frac{3312362413}{14200200000},&
\mathbb ES^4&=\frac{23494607999719}{155066184000000},\\
\operatorname{Var}S&=\frac{11407951}{1119787200}.
\end{aligned}
\]

Substitution recovers the R749SQE limit means $(379/630,1481/2520,1/72)$ and covariances $\operatorname{Cov}(Y_0,K)=41/1134000$ and $\operatorname{Cov}(Y_1,K)=-641/4536000$.

## 4. Quantitative lattice-to-Dirichlet convergence

**Theorem D (uniform $O(r^{-1})$ marginal bound).** For the integer-depth source residual,

\[
\boxed{\sup_{0\le t\le1/3}
\left|\Pr(K_r/r\ge t)-(1-3t)^{23}\right|=O(r^{-1})}.
\]

The constant depends only on the 23 fixed integer slacks. The Kolmogorov discrepancy, with the usual discrete endpoint convention, is also $O(r^{-1})$.

**Proof.** The weighted integer lattice count is an Ehrhart quasipolynomial for a fixed 23-dimensional rational simplex and satisfies $C_s=A s^{23}+O(s^{22})$ for positive integers $s$, where $A=(23!\prod_i s_i)^{-1}>0$. Uniformly for $0\le v\le r$, the error is $O(r^{22})$. By Theorem A the finite tail at $t>0$ equals $C_{r-3\lceil rt\rceil}/C_r$; replacing $(r-3\lceil rt\rceil)/r$ by $1-3t$ changes its 23rd power by $O(r^{-1})$. At $t=0$ the tail is exactly one. The total error after dividing by $C_r\asymp r^{23}$ is uniformly $O(r^{-1})$.

## 5. Reproduction, limitations and next step

The standard-library Python verifier **R749SQF_DIRICHLET_SPLINE_CERT.py** reconstructs all 33 first-grid points, 25 forced letters and 23 positive-slack letters from the frozen eight facets, derives all 12 knots and 23 repeated-pole coefficients, integrates the rational spline on its 11 intervals, and independently recomputes the first four moments via Dirichlet homogeneous symmetric polynomials. For **every $r=1,\ldots,120$**, it checks the finite tail against a second 22-letter integer partition DP; all arithmetic uses exact integers and Fraction objects, with no floating tolerance. The corresponding JSON result is **R749SQF_DIRICHLET_SPLINE_RESULTS.json**, status PASS.

The universal conclusions are supported by the bijection, gamma/Dirichlet disintegration, confluent divided difference and rational Ehrhart arguments; finite tests are consistency checks. They remain author-level within the frozen auxiliary Walsh source model.

**Open problem:** determine the first quasipolynomial correction to $C_r$, sharp residue-class Kolmogorov constants modulo the lcm of weights (420), and an independently verified native signed-Port observation bridge before transferring these auxiliary source statistics to X6.
