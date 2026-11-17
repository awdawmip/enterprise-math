# R749STB — Stable three-read collision sheet and quantified future-observer obstruction

Date: 2026-11-17. Evidence: AUTHOR_EXACT_NOT_REVIEWED. Mode: independent portable scalar research. Frozen scientific pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Predecessor: R749STA, PR #2613, commit f99411fb87774fdacf9dd4917ffa330bbeaf7d53. Previously established global upper bound: R749SST (11 reads).

## Model

Five **distinct labeled** sources with weights (1,1,2,3,6) define
\[
\Omega_q=\{k\in\mathbb Z_{\ge0}^5: k_1+k_2+2k_3+3k_4+6k_5\le q-1\},
\quad C_q=|\Omega_q|,\quad T_q=\sum_{k\in\Omega_q}k_1.
\]
Set \(S(q)=18q^4+54q^3-345q^2+2070q-16315\), and
\[
Y_q(e,d)=q^3(T_q+e)/(C_q+d)-S(q)/108,\qquad
\mathcal O_q^{(m)}(e,d)=(Y_{q+6j}(e,d))_{j=0}^{m-1}.
\]
Within one candidate the continuous errors (e,d) are shared across reads and lie in [-2,2]^2; different candidates may use different errors.

## New quantitative theorem

For **every** real e in [-151/100,-149/100], define
\[
c(e)=-183/200-(183/500)(e+3/2).
\]
There exists **exactly one** d(e) in (c(e)-1/1000,c(e)+1/1000) and uniquely determined E(e),D(e) such that
\[
\boxed{\mathcal O_{73}^{(3)}(e,d(e))=\mathcal O_{77}^{(3)}(E(e),D(e))}
\]
and all four error parameters are strictly inside (-2,2). The functions d(e), E(e), D(e) are analytic on a neighborhood of this closed interval. Moreover the fourth reads satisfy the uniform *strict* lower bound
\[
\boxed{Y_{95}(E(e),D(e))-Y_{91}(e,d(e))>1/100000.}
\]

**Forecasting corollary:** Any fourth-read predictor depending only on the first three scalar outputs incurs absolute error **strictly greater than 1/200000 on at least one** of the two states at each point on the collision curve. The first-three-read inputs are equal and their true future readouts differ by >1/100000; apply the triangle inequality. Thus the three-read observer merges a whole analytic family of future-inequivalent source states, with a quantitative positive residual.

## Construction and proof

For j=0,1,2,3 let a_j=73+6j, b_j=77+6j, and define
\[
 y_j=Y_{a_j}(e,d),\quad
 x_j=(y_j+S(b_j)/108)/b_j^3,\quad v_j=x_jC_{b_j}-T_{b_j}.
\]
Every desired equality has the form E-x_jD=v_j. Matching the first two reads yields rational functions
\[
D=(v_0-v_1)/(x_1-x_0),\quad E=v_0+x_0D.
\]
The third-read equality is F=0 for
\[
F=(v_0-v_1)(x_2-x_0)-(v_0-v_2)(x_1-x_0).
\]
After these first two matches, define the fourth-read residual
\[
R_4=Y_{95}(E,D)-Y_{91}(e,d).
\]

The companion certificate performs **exact rational arithmetic** over the whole slanted rectangle
\[
e=-151/100+u/50,\quad
d=c(e)+(2v-1)/1000,\quad (u,v)\in[0,1]^2.
\]
It verifies:

- F(e,c(e)-1/1000) < 0 < F(e,c(e)+1/1000);
- \(\partial F/\partial d>0\) throughout the rectangle;
- \(-2<E,D<2\) and every relevant denominator has the asserted sign;
- \(R_4>1/100000\) throughout the rectangle.

The intermediate value theorem gives a root d(e), derivative positivity gives uniqueness, and the analytic implicit-function theorem gives local analytic dependence. All constraints hold on the resulting branch.

For every polynomial P(u,v) of bidegree (m,n), let c_ab be its ordinary monomial coefficients. The exact Bernstein coefficients are
\[
\beta_{ij}=\sum_{a\le i,\ b\le j}c_{ab}
\frac{\binom ia}{\binom ma}\frac{\binom jb}{\binom nb}.
\]
The bivariate Bernstein basis is nonnegative on [0,1]^2 and sums to one. Thus positivity of all \(\beta_{ij}\) proves strict polynomial positivity throughout the square. The certificate proves positivity of **199 exact rational Bernstein coefficients in 16 numerator/denominator polynomials**: four for endpoint signs, eight for E/D guards, two for the fourth-gap inequality and two for derivative positivity. It independently confirms that the q=73 cubic from R749STA is square-free.

Run: python R749STB_STABLE_THREE_READ_COLLISION_CERT.py (Python 3 and SymPy). Expected console result: PASS 199 strict Bernstein coefficients unique analytic collision curve fourth gap > 1e-5. The companion JSON contains all 16 polynomial degrees, positive coefficient counts and exact minima. This is an all-real-parameter certificate, not a sampling experiment.

## Infinite qualitative corollary and scope

The R749STA exact all-q certificate proves strict opposite endpoint signs of the third defect and strict E/D guards at fixed e=-3/2 for every q>=73 with q=1 (mod 6), p=q+4. By continuity, **for each such q** some delta_q>0 exists so that every e satisfying |e+3/2|<delta_q admits at least one legal three-read collision. The present theorem adds an explicit interval, uniqueness and quantified future-read separation specifically at (73,77). It does not assert a uniform delta_q for all q.

The native P000 setting remains six-dimensional signed discrete Cell space with separately typed time and source/observer preservation. This labeled-source scalar observer is an auxiliary testbed. A BRC or X6 port theorem requires a typed embedding with source labels, ordering, branches and future-operation fidelity.

Next: Decide four-read separation for (73,77) on the entire admissible square; test whether four reads separate all sufficiently large cutoff residue classes; establish a lossless future-observer repair coordinate. No shared CLAIM/Result/Review/Foundation promotion is asserted.
