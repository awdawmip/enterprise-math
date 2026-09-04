# Dyadic algebraic upper certificates and two-sided completion brackets

Status: `FREE_RESEARCH / TWO-SIDED FINITE CERTIFICATE STRENGTHENING / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on the internal completion law `(S,C,tau)` and dyadic first-mode algebra.

## 1. Lower carrier

Let

\[
y=\frac{\tau}{2q},
\qquad
T_q=2qS(y)=q\sqrt{a_q}.
\]

On the first half-phase, `0<C(y)<1`, hence `S(y)<y`, so

\[
T_q<\tau.
\]

The level-one dyadic annihilation lower bound is

\[
L_q:=\frac{4T_{2q}-T_q}{3}<\tau.
\]

For dyadic `q`, all `T` values are nested-radical algebraic data.

## 2. A same-mode tangent upper carrier

Define

\[
V_q:=2q\frac{S(y)}{C(y)}.
\]

Because the first-mode identity gives

\[
a_q=4S(y)^2,
\qquad
C(y)=\sqrt{1-S(y)^2}=\frac{\sqrt{4-a_q}}2,
\]

we have the entirely algebraic formula

\[
\boxed{
V_q
=
\frac{2q\sqrt{a_q}}{\sqrt{4-a_q}}.
}
\tag{AUC-1}
\]

Let

\[
g(y):=S(y)-yC(y).
\]

Using `S'=C` and `C'=-S`,

\[
g'(y)=yS(y)>0
\]

for `0<y<tau/2`, while `g(0)=0`. Therefore

\[
S(y)>yC(y),
\]

and since `C(y)>0`,

\[
\boxed{V_q>\tau.}
\tag{AUC-2}
\]

Thus a single finite first mode already gives both a chord lower carrier `T_q` and a tangent upper carrier `V_q`.

## 3. Unique single-scale quartic upper combination

Consider a normalized linear combination

\[
U_q=\alpha T_q+(1-\alpha)V_q.
\]

The local expansions

\[
\frac{T_q}{\tau}
=1-\frac{y^2}{6}+\frac{y^4}{120}+O(y^6),
\]

\[
\frac{V_q}{\tau}
=\frac{S(y)}{yC(y)}
=1+\frac{y^2}{3}+\frac{2y^4}{15}+O(y^6)
\]

show that cancellation of the `y^2` mode requires uniquely

\[
-\frac\alpha6+\frac{1-\alpha}{3}=0,
\]

hence

\[
\alpha=\frac23.
\]

Therefore the unique same-scale second-order-cancelling combination is

\[
\boxed{
U_q
:=
\frac{2T_q+V_q}{3}.
}
\tag{AUC-3}
\]

## 4. Huygens-type derivative proof of the strict upper sign

Define

\[
h(y)
:=
\frac{2S(y)+S(y)/C(y)}3-y.
\]

Since `S^2+C^2=1`,

\[
\begin{aligned}
3h'(y)
&=2C(y)+\frac{1}{C(y)^2}-3\\
&=\frac{2C(y)^3-3C(y)^2+1}{C(y)^2}\\
&=\frac{(1-C(y))^2(2C(y)+1)}{C(y)^2}.
\end{aligned}
\]

Thus

\[
\boxed{
h'(y)>0\qquad(0<y<\tau/2),}
\]

and `h(0)=0`, so

\[
\boxed{U_q>\tau.}
\tag{AUC-4}
\]

The cancellation in Section 3 also shows

\[
U_q-\tau=O(q^{-4}).
\]

The leading normalized error is

\[
\frac{U_q-\tau}{\tau}
=\frac{y^4}{20}+O(y^6).
\]

## 5. Fully algebraic quartic two-sided interval

Combining the old quartic lower endpoint with (AUC-4),

\[
\boxed{
\frac{4T_{2q}-T_q}{3}
<\tau<
\frac{2T_q+V_q}{3}.
}
\tag{AUC-5}
\]

Using (AUC-1), the upper endpoint is

\[
\boxed{
\frac13
\left(
2q\sqrt{a_q}
+
\frac{2q\sqrt{a_q}}{\sqrt{4-a_q}}
\right)
}
\]

with the first term doubled appropriately through `2T_q`; explicitly

\[
U_q
=
\frac{2q\sqrt{a_q}
+2q\sqrt{a_q}/\sqrt{4-a_q}}3
\]

only after remembering `2T_q=2q\sqrt{a_q}`.

For dyadic `q`, both interval endpoints are constructed using only integers, rational arithmetic, and nested square roots. No value of `tau`, `pi`, `sin`, or `cos` is an input.

This is an exact finite two-sided certificate; its computable interval width `U_q-L_q` itself is a valid error certificate, so no unknown target-dependent remainder constant is needed operationally.

## 6. Explicit upper-error bound if desired

The already used inequality

\[
1-C(t)\le\frac{t^2}{2}
\]

implies

\[
C(t)\ge1-\frac{t^2}{2}.
\]

For `0<=t<=y<1`,

\[
h'(t)
=
\frac{(1-C)^2(2C+1)}{3C^2}
\le
\frac{t^4}{4(1-y^2/2)^2}.
\]

Integrating,

\[
0<U_q-\tau
\le
\boxed{
\frac{\tau^5}
{320q^4\left(1-\tau^2/(8q^2)\right)^2}.
}
\tag{AUC-6}
\]

This may be made fully rational by replacing `tau` with either `4` or the sharper internal rational upper bound `355/113`.

## 7. Tangent-series positivity

Let

\[
t(y):=\frac{S(y)}{C(y)}.
\]

Direct differentiation gives

\[
\boxed{t'(y)=1+t(y)^2,\qquad t(0)=0.}
\tag{AUC-7}
\]

Write

\[
t(y)=\sum_{n\ge0}b_ny^{2n+1}.
\]

Then

\[
b_0=1,
\]

and coefficient comparison in (AUC-7) gives

\[
\boxed{
(2n+1)b_n
=
\sum_{r=0}^{n-1}b_rb_{n-1-r}
\qquad(n\ge1).
}
\tag{AUC-8}
\]

Hence

\[
\boxed{b_n>0\quad\text{for all }n.}
\tag{AUC-9}
\]

Thus

\[
\frac{V_q}{\tau}
=
\frac{t(y)}y
=
\sum_{n\ge0}b_ny^{2n}
\]

has strictly positive correction coefficients.

## 8. High-order tangent-filter sign hierarchy

Apply the same dyadic annihilation filter

\[
\mathcal A_m
=
\prod_{r=1}^{m}\frac{4^r\mathcal E-I}{4^r-1}
\]

to the finite tangent carrier `V_q`.

The exact response on `y^(2n)` is

\[
\lambda_{m,n}
=
\prod_{r=1}^{m}\frac{4^{r-n}-1}{4^r-1}.
\]

The modes `n=1,...,m` vanish, while for every `n>=m+1`,

\[
\operatorname{sgn}(\lambda_{m,n})=(-1)^m.
\]

Since every tangent coefficient `b_n` is positive,

\[
\boxed{
\operatorname{sgn}\left((\mathcal A_mV)(q)-\tau\right)
=(-1)^m.
}
\tag{AUC-10}
\]

Therefore:

- even `m`: `A_m V` is a strict upper certificate of order `q^(-2m-2)`;
- odd `m`: `A_m V` is a strict lower certificate of the same order.

In particular, at `m=2`,

\[
\boxed{
\frac{V_q-20V_{2q}+64V_{4q}}{45}
>\tau,
}
\tag{AUC-11}
\]

and its error is sextic.

Pairing this with the sine-carrier lower certificate

\[
E_2(q)<\tau
\]

gives an exact dyadic sextic two-sided algebraic interval.

More generally, every even annihilation level gives matching-order nested-radical lower/upper endpoints:

\[
\boxed{
E_{2r}(q)<\tau<(\mathcal A_{2r}V)(q).
}
\tag{AUC-12}
\]

All values involved are rational combinations of the dyadic nested-radical first-mode data.

## 9. Research consequence

The completion constant now has two finite first-mode geometries:

```text
chord carrier   T_q = 2q S(y)          -> lower
 tangent carrier V_q = 2q S(y)/C(y)    -> upper
```

The quartic Huygens combination is the unique one-scale cancellation of their quadratic errors, while the generic dyadic annihilation filter yields arbitrarily high even-level algebraic two-sided certificates.

Freeze:

`SAME_MODE_CHORD/TANGENT -> FINITE TWO_SIDED_COMPLETION`.

`HUYGENS_COMBINATION -> UNIQUE_SINGLE_SCALE_QUARTIC_UPPER`.

`EVEN_TANGENT_ANNIHILATION_LEVEL -> HIGH_ORDER_UPPER`.
