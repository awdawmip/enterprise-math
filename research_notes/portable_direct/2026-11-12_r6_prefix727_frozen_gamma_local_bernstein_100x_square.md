# PREFIX-727-R6 — A 100× larger exact frozen-Gamma witness square via local Bernstein variation

Date: 2026-11-12 (Asia/Shanghai). Mother objective: PREFIX-675. Predecessor: PREFIX-726-R6.
Scientific input pin (unchanged): `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Mathematical status: AUTHOR_EXACT_INTEGER_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Main theorem

In the same auxiliary BRC stopping-count model with two independent conditional unit-rate Gamma completion clocks as PREFIX-726, put
\[
Y(p,z)=\max(T_p,T_z),\quad \mu=E[Y],\quad M_2=E[Y^2],
\quad f_t(p,z)=M_2-\mu^2-t\mu,\quad V_q=q^2f_{1/q}.
\]
The domain is \(D=[0,1/2]^2\), with all real \(q\ge2\), equivalently \(t\in[0,1/2]\).
Let \(c=(11/96,11/96)\) and the fixed feasible witness \(e=(0,73/500)\).
Then every point of the *closed continuous rational square*
\[
R_{727}=\{(p,z): |p-11/96|\le1/2000,\ |z-11/96|\le1/2000\}
\]
satisfies
\[
\boxed{V_q(e)-V_q(p,z)>\frac{957}{125}\,q^2=7.656q^2.}
\]
This excludes every point of \(R_{727}\) from being a global maximizer of the auxiliary frozen-Gamma objective. The certified half-width is exactly 100 times PREFIX-726's \(1/200000\), increasing certified square area by a factor of 10,000.

## Exact meaning of the 189-row Bernstein controls — correction to PREFIX-726 wording

The frozen recurrence carries **surviving path counts** \(w_{n,k}\), not binary indicators. Its Bernstein control is
\[
b_{n,k}=\frac{w_{n,k}}{\binom nk}\in[0,1],
\quad s_n(p)=\sum_{k=0}^n b_{n,k}\binom nk p^k(1-p)^{n-k}.
\]
The previous PREFIX-726 phrase saying controls are in \(\{0,1\}\) was imprecise: 8,904 control entries in the 189-row actual recurrence are strictly between zero and one. The global derivative bound \(|s'_n|\le n\) used there remains valid, because all controls lie in \([0,1]\) and \(|b_{n,k+1}-b_{n,k}|\le1\). This correction changes the **new local** derivative analysis: simply counting the two nonzero support boundaries would omit interior fractional transitions.

The checker recomputes rows 0 through 189 from the exact integer width predicate, verifies row 189 is empty and the preceding rows contain exactly 9,529 nonzero cells. It checks, via cross-multiplied integer inequalities for all 189 rows,
\[
b_{n,k}=b_{n,n-k},\qquad
b_{n,k+1}\ge b_{n,k}\quad (0\le k<\lfloor n/2\rfloor).
\]
For \(0\le p\le1/2\), pair the symmetric terms in the derivative
\[
s_n'(p)=n\sum_{k=0}^{n-1}\Delta b_{n,k}B_{n-1,k}(p),
\qquad \Delta b_{n,k}=b_{n,k+1}-b_{n,k}.
\]
The lower-half differences are nonnegative, their reflected differences are their negatives, and \(B_{n-1,k}(p)\ge B_{n-1,n-1-k}(p)\) for lower-half indices. Therefore \(s'_n(p)\ge0\) on \([0,1/2]\).

## Local derivative certificate

Set \(a=11/96-1/2000\), \(b=11/96+1/2000\). For each nonzero normalized difference, define
\[
P^*_{n,k}=\max_{x\in[a,b]} \binom{n-1}{k}x^k(1-x)^{n-1-k}.
\]
The maximum is attained at the rational argument
\[
x^*_{n,k}=\min\{b,\max\{a,k/(n-1)\}\}.
\]
The standalone checker computes each \(n|\Delta b_{n,k}|P^*_{n,k}\) using exact `Fraction` arithmetic, rounds it **upward** to an integer multiple of \(10^{-6}\), and sums the rounded upper contributions, including their respective \(2(n+1)\) weights. The exact integer totals are
\[
T_1=543771784,\quad T_2=80388454400,
\]
at denominator \(10^6\), hence throughout \([a,b]\)
\[
\sum_{n=0}^{188}|s_n'(x)|<544,\qquad
\sum_{n=0}^{188}2(n+1)|s_n'(x)|<80400.
\]
Exact evaluation of the single-clock tail sum at \(b\) gives \(\sum_{n<189}s_n(b)<72\). By the checked symmetry/unimodality, the same tail sum at every \(p\in[a,b]\) is smaller than 72. Thus
\[
0\le\mu(p,z)=E[\max(T_p,T_z)]\le E[T_p+T_z]<144
\quad ((p,z)\in R_{727}).
\]
The independent-Gamma maximum formulas from PREFIX-726 give
\[
\mu_p=\sum_n a_n(z)s_n'(p),\qquad
(M_2)_p=\sum_n h_n(z)s_n'(p),
\]
with \(0\le a_n(z)\le1\), \(0\le h_n(z)\le2(n+1)\), by the exact negative-binomial kernel sums; similarly for the \(z\) derivatives. Consequently, for every \(t\in[0,1/2]\),
\[
|\partial_p f_t|,|\partial_z f_t|
<80400+(2\cdot144+1/2)544
=\boxed{237344}=:L_{727}
\]
throughout the square.

## Complete gap proof for continuous q

PREFIX-726 has independently calculated the frozen integer/Gamma moments at \(c\) and \(e\) and proved the exact rational endpoint statements
\[
f_0(e)-f_0(c)>245,\qquad
f_{1/2}(e)-f_{1/2}(c)>245.
\]
Their difference is affine in \(t\), so \(f_t(e)-f_t(c)>245\) for **all real** \(t\in[0,1/2]\). Within the convex square,
\[
|f_t(p,z)-f_t(c)|\le L_{727}(|p-c_1|+|z-c_2|)
\le 2L_{727}/2000=237.344.
\]
Subtracting gives
\[
f_t(e)-f_t(p,z)>245-237.344=\frac{957}{125}>0.
\]
Multiplying by \(q^2\) proves the theorem for all real \(q\ge2\).

## Reproduction, evidence and next problem

The companion standard-library checker is `PREFIX727_R6_ACTUAL_BERNSTEIN_LOCAL_SQUARE.py`; it regenerates the actual frozen 189 rows with integer predicates, checks all monotonicity inequalities, performs exact local binomial-maximizer calculations with outward rational rounding, and writes `PREFIX727_R6_RESULTS.json`. Local execution returned `ALL_CHECKS_PASS PREFIX727-R6`. It inherits only the explicitly cited, already exact-checked center/witness Gamma moment gap of PREFIX-726. Both checks must be run when independently reproducing the entire chain.

The previously certified whole-cell 384×384 exclusion fraction remains \(139018/147456\). This new square is centered at the grid vertex \(44/384\) and spans only parts of adjacent fine cells, so no new whole-cell coverage is claimed.

Next discriminating unit: use the now explicit actual fractional Bernstein controls to compute tighter local bounds of the **full variance derivative**, rather than separately bounding the first and second moments; test whether a complete adjacent 384×384 cell can be certified by the fixed witness or a switched witness. Preserve the frozen Gamma pin and explicitly check disjointness before changing aggregate coverage.
