# Free Research — Stopped Signed Return Operator

Status: `FREE_RESEARCH_FRONTIER / EXACT FINITE OPERATOR / PARITY FOLD AS SECOND ITERATE / CONTINUUM TOP-SCALE TWO-STEP ANNIHILATION / DISCRETIZATION-REGULARITY GATE EXPOSED / NOT WORKING TRUTH / NOT FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_PARITY_FOLDED_SQUARE_SCALAR_READOUT_V15_20260904.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`

## 1. Exact finite operator

Fix a top cutoff `N`, a finite positive action family `S_N`, weights `u_a>=0`, and

\[
A:=A_N=\sum_{a\in S_N}u_a>0,
\qquad
A_n:=\sum_{\substack{a\in S_N\\a\le n}}u_a.
\]

Define the adaptive full residual

\[
G_f(n)
:=A_nf(n)+
\sum_{\substack{a\in S_N\\a\le n}}
 u_af(q_a(n)).
\]

Define the stopped signed return operator on states `1<=n<=N` by

\[
\boxed{
(\mathcal T_Nf)(n)
:=\frac{A-A_n}{A}f(n)
-
\frac1A
\sum_{\substack{a\in S_N\\a\le n}}
 u_af(q_a(n)).}
\tag{1.1}
\]

The first term selects an action that exceeds the current state, keeps the state fixed and assigns sign `+1`. The second selects a valid action, descends to the quotient and assigns sign `-1`.

By construction,

\[
\boxed{
f(n)=\frac{G_f(n)}A+(\mathcal T_Nf)(n).}
\tag{1.2}
\]

This is an exact finite resolvent, not an asymptotic equation.

---

## 2. Probabilistic history realization

Let actions be sampled independently from

\[
p_N(a)=u_a/A.
\]

At current state `n`, one action produces

\[
(n,\sigma)
\mapsto
\begin{cases}
(q_a(n),-\sigma),&a\le n,\\
(n,+\sigma),&a>n.
\end{cases}
\]

Then

\[
(\mathcal T_N^rf)(n)
=
\mathbb E_n
\left[(-1)^{V_r}f(X_r)\right],
\tag{2.1}
\]

where `V_r` is the number of valid quotient moves during the first `r` sampled actions and `X_r` is the retained state.

Iterating (1.2) gives the exact Duhamel expansion

\[
\boxed{
f(N)
=
\sum_{j=0}^{r-1}
\mathcal T_N^j\left(\frac{G_f}{A}\right)(N)
+
(\mathcal T_N^rf)(N).}
\tag{2.2}
\]

Thus every provenance depth is an iterate of one finite signed stopped-history primitive.

---

## SSR-T01 — The parity fold is the second iterate

At the top state `N`, every action in `S_N` is valid, so

\[
(\mathcal T_Nf)(N)
=-\frac1A\sum_au_af(q_a(N)).
\]

At the second step, `b` is valid precisely when

\[
b\le q_a(N)
\iff ab\le N.
\]

Therefore

\[
\boxed{
(\mathcal T_N^2f)(N)
=
\frac1{A^2}
\left[
\sum_{ab\le N}u_au_bf(q_{ab}(N))
-
\sum_{ab>N}u_au_bf(q_a(N))
\right].}
\tag{3.1}
\]

This is the negative of the signed folded term in the parity-resolvent note.

Taking `r=2` in (2.2) gives

\[
\boxed{
f(N)
=
\frac{G_f(N)}A
-
\frac1{A^2}\sum_au_aG_f(q_a(N))
+
(\mathcal T_N^2f)(N),}
\tag{3.2}
\]

which is exactly the parity-fold scalar resolvent.

---

## 3. Constant-mode defect

For the constant field `1`,

\[
\boxed{
(\mathcal T_N^2\mathbf1)(N)
=
\frac{2C_2(N)}{A^2}-1,}
\tag{4.1}
\]

where

\[
C_2(N)=\sum_{ab\le N}u_au_b.
\]

For prime-winding weights,

\[
A=\log N+O(1),
\qquad
C_2(N)=\frac12\log^2N+O(\log N),
\]

so

\[
\boxed{
(\mathcal T_N^2\mathbf1)(N)
=O(1/\log N).}
\tag{4.2}
\]

The finite arithmetic square is therefore an asymptotic annihilator of constants at the top scale.

---

## 4. Ideal logarithmic continuum operator

Replace the normalized prime-winding action measure by Lebesgue measure on the logarithmic interval. Let the current logarithmic scale be

\[
t\in[0,1].
\]

An action coordinate `s` is uniform on `[0,1]`. It is valid when `s<=t`; if valid the new state is `t-s`, and otherwise the state is retained.

The limiting stopped signed operator is

\[
\boxed{
(\mathcal Tf)(t)
=(1-t)f(t)-\int_0^tf(t-s)ds
=(1-t)f(t)-\int_0^tf(u)du.}
\tag{5.1}
\]

This is the exact continuum counterpart of (1.1).

---

## SSR-T02 — Top-scale two-step annihilation

Let

\[
F(t)=\int_0^tf(u)du.
\]

Then

\[
(\mathcal Tf)(t)=(1-t)f(t)-F(t).
\]

At the top state,

\[
(\mathcal T^2f)(1)
=-\int_0^1(\mathcal Tf)(u)du.
\]

But

\[
\begin{aligned}
\int_0^1(\mathcal Tf)(u)du
&=\int_0^1(1-u)f(u)du
-
\int_0^1F(u)du\\
&=\int_0^1(1-u)f(u)du
-
\int_0^1(1-u)f(u)du\\
&=0.
\end{aligned}
\]

Therefore

\[
\boxed{
(\mathcal T^2f)(1)=0
\qquad\text{for every integrable }f.}
\tag{6.1}
\]

This is much stronger than a spectral contraction. The ideal two-history fold annihilates every top-scale readout exactly.

---

## 5. Pointwise formula away from the top

A direct calculation gives

\[
\boxed{
(\mathcal T^2f)(t)
=(1-t)\left[(1-t)f(t)-2F(t)\right].}
\tag{7.1}
\]

The factor `1-t` explains why exact annihilation occurs only at the top state. It also shows that descendants near the top retain a boundary mode, in agreement with the actual-additive-intertwiner no-go.

---

## 6. Discrete arithmetic defect

Equation (6.1) identifies the source of the arithmetic remainder precisely.

The finite prime-winding operator differs from the continuum operator through:

1. CDF discrepancy of the normalized logarithmic action measure;
2. floor quantization in the quotient endpoint;
3. lack of a priori smoothness of the field being integrated.

The first two are small against regular test functions. The third is the decisive gate: bounded discrepancy alone does not control integration against an arbitrary bounded field whose energy concentrates at the small-action boundary.

The V15 variance and Dirichlet carriers are positive ways to measure exactly this missing regularity.

---

## 7. Relation to classical smoothing

The continuum identity says that two integrations cancel the full leading signed history measure. An elementary quantitative remainder proof must show that the arithmetic field is regular enough for the discrete two-step operator to inherit a rate from this cancellation.

There are two possible implementations:

- **native energy route:** control the parity-fold variance or its shared-first `S_3` Dirichlet lift;
- **slow-oscillation route:** establish a modulus of continuity and apply bounded-discrepancy quadrature, as in classical iterated smoothing methods.

The current project has closed the first route's state, positivity and scalar readout, but not yet its final decay estimate.

---

## 8. Updated boundary

Closed:

1. exact finite stopped signed return operator;
2. exact provenance-depth Duhamel expansion;
3. parity fold as the second iterate;
4. prime-winding constant-mode defect;
5. exact continuum operator;
6. universal top-scale identity `T^2 f(1)=0`;
7. precise separation of discretization and regularity defects.

Open:

1. a quantitative bound for `(T_N^2-T^2)f` on the actual prime-error field without importing PNT;
2. variable-depth or energy-based suppression of the small-action boundary mode;
3. a native remainder rate.
