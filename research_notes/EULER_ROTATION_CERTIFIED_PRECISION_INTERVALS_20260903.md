# Self-certified nested precision intervals from the Euler rotation-root tower

Status: `FREE_RESEARCH / EXACT FINITE CERTIFICATE / NOT FOUNDATION`  
Date: `2026-09-03`  
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`  
Author/program signature: `YUAN X / Enterprise Math`

## 1. Motivation

The finite Viète/rotation readout

\[
L_m:=\Pi_m^{\rm rot}
=
\frac{2}{\prod_{n=2}^{m}c_n}
\]

is defined without inserting the numerical value of classical pi. It is strictly
increasing and converges to an internally defined rotation constant

\[
\pi_{\rm rot}:=\lim_m L_m.
\]

For finite-resolution mathematics, convergence alone is not enough. A finite state
should carry an exact certificate of how much unresolved refinement remains.

This note derives, from the same half-trace recursion, a computable upper endpoint
`U_m` such that

\[
\boxed{
L_m<\pi_{\rm rot}<U_m
}
\]

and the intervals are strictly nested:

\[
\boxed{
L_m<L_{m+1}<\pi_{\rm rot}<U_{m+1}<U_m.
}
\]

Every endpoint uses only finitely many nested radicals and does not use a target
value of pi.

## 2. Half-trace defect recursion

Recall

\[
c_{n+1}^2=\frac{1+c_n}{2},
\qquad
c_1=0,
\qquad
0<c_n<1\quad(n\ge2).
\]

Put

\[
d_n=1-c_n.
\]

Rationalizing the square root gives the exact recursion

\[
\begin{aligned}
d_{n+1}
&=1-c_{n+1}\\
&=\frac{1-c_{n+1}^2}{1+c_{n+1}}\\
&=\frac{1-c_n}{2(1+c_{n+1})}.
\end{aligned}
\]

Hence

\[
\boxed{
d_{n+1}=\frac{d_n}{2(1+c_{n+1})}.}
\]

Fix a visible level `m` and define

\[
q_m=\frac1{2(1+c_{m+1})}.
\]

Since the half-traces increase, for all `n>=m+1`,

\[
d_{n+1}\le q_m d_n.
\]

Therefore the unresolved total half-trace defect satisfies

\[
\sum_{n=m+1}^{\infty}d_n
\le
\frac{d_{m+1}}{1-q_m}.
\]

Define the finite tail certificate

\[
\boxed{
S_m
=
\frac{1-c_{m+1}}
{1-\dfrac1{2(1+c_{m+1})}}.
}
\]

It simplifies to

\[
\boxed{
S_m
=
\frac{2(1-c_{m+1}^2)}{1+2c_{m+1}}.
}
\]

Because `c_(m+1)>=c_2=1/sqrt(2)`, one has

\[
0<S_m\le\sqrt2-1<1.
\]

## 3. Product tail lemma

For any finite family `0<=x_j<=1`, induction gives

\[
\prod_j(1-x_j)
\ge
1-\sum_jx_j.
\]

Apply this to `x_j=d_j`. Passing to the decreasing infinite product,

\[
\prod_{n=m+1}^{\infty}c_n
=
\prod_{n=m+1}^{\infty}(1-d_n)
\ge
1-S_m>0.
\]

But

\[
\pi_{\rm rot}
=
\frac{L_m}{\prod_{n=m+1}^{\infty}c_n}.
\]

Therefore

\[
L_m<\pi_{\rm rot}
\le
\frac{L_m}{1-S_m}.
\]

Define

\[
\boxed{
U_m:=\frac{L_m}{1-S_m}.
}
\]

The explicit finite error certificate is

\[
\boxed{
0<\pi_{\rm rot}-L_m
\le
\frac{L_mS_m}{1-S_m}.
}
\]

No unknown limiting constant appears on the right-hand side.

## 4. Strict nesting of the upper endpoints

It remains to prove that `U_m` decreases.

Write

\[
a=c_{m+1},
\qquad
b=c_{m+2},
\qquad
a=2b^2-1.
\]

Since

\[
L_{m+1}=\frac{L_m}{a},
\]

we have `U_(m+1)<U_m` exactly when

\[
a(1-S_{m+1})>1-S_m.
\]

Substitute

\[
S(x)=\frac{2(1-x^2)}{1+2x}.
\]

A direct factorization gives

\[
\boxed{
a(1-S(b))-(1-S(a))
=
\frac{4b(b-1)^2(b+1)}{2b-1}.}
\]

For every finite level,

\[
\frac12<b<1,
\]

so the right-hand side is strictly positive. Hence

\[
\boxed{U_{m+1}<U_m.}
\]

Together with the already proved strict increase of `L_m`, this gives the nested
interval theorem.

## 5. Certified precision state

Define the finite Enterprise rotation-pi state

\[
\boxed{
\widehat\pi_m^{\rm rot}
=
[L_m,U_m].
}
\]

Then

\[
\widehat\pi_{m+1}^{\rm rot}
\subsetneq
\widehat\pi_m^{\rm rot},
\]

and

\[
\bigcap_{m\ge1}
\widehat\pi_m^{\rm rot}
=
\{\pi_{\rm rot}\}.
\]

This is a concrete realization of the principle

\[
\text{precision is part of the number state}.
\]

At depth `m`, the mathematical object is not an infinitely precise point plus an
external error bar. It is a certified interval produced by the unresolved dyadic
rotation phases themselves.

## 6. Sample intervals

The endpoints below are computed entirely from the nested-radical recurrence:

\[
\begin{array}{c|c|c}
m&L_m&U_m\\\hline
4&3.121445152258052\ldots&3.141631813240761\ldots\\
6&3.140331156954753\ldots&3.141592805651393\ldots\\
8&3.141513801144301\ldots&3.141592654183564\ldots\\
10&3.141587725277160\ldots&3.141592653592113\ldots\\
12&3.141592345570118\ldots&3.141592653589802\ldots
\end{array}
\]

The classical value is used only after the construction to identify the unique
limit point with the usual pi.

## 7. Downstream Archimedean asymptotics

Under the standard complex character completion,

\[
L_m=2^m\sin\frac{\pi}{2^m}.
\]

The lower endpoint has the familiar leading error of order `4^-m`.
The new upper certificate cancels that leading defect; expansion gives

\[
\frac{U_m}{\pi}
=
1+\frac{2}{15}
\left(\frac{\pi}{2^{m+1}}\right)^4
+O(64^{-m}).
\]

Thus the certified upper endpoint approaches the limit at fourth order in the local
phase step, even though it was derived without using that Archimedean expansion.

This asymptotic is a downstream interpretation. The finite nested interval theorem
does not depend on it.

## 8. Candidate statement

`AC-EM-FREE-F6D046-EULER-CERTIFIED-PRECISION-INTERVAL-V1`:

> The pi-free dyadic rotation-root tower determines explicit finite lower and upper
> endpoints `L_m` and `U_m`. The lower endpoints strictly increase, the upper
> endpoints strictly decrease, every interval contains the internally completed
> rotation constant, and the intervals shrink to a singleton. Hence the rotation
> value of pi can be represented at every finite depth by a certified nested
> precision state rather than by an infinite real number with an externally added
> error annotation.

Status:

`FINITE_INTERVAL_CERTIFICATE_EXACT`.

`NESTING_EXACT`.

`CLASSICAL_PI_IDENTIFICATION_ARCHIMEDEAN_COMPLETION`.
