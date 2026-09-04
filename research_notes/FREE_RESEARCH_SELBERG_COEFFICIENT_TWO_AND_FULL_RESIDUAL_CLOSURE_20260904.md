# Free Research — Selberg Coefficient Two and Full Residual Closure

Status: `FREE_RESEARCH_FRONTIER / SELBERG_COEFFICIENT_TWO_DERIVED_FROM_FIRST_MASS / FULL_SIGNLESS_RESIDUAL_UNIFORMLY_BOUNDED / DEEP_RESIDUAL_FORCING_SUMMABLE / NO_PNT_INPUT / END_TO_END_MULTICHANNEL_CASCADE_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_RECTANGULAR_TAIL_RETURN_INTERTWINER_20260904.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`
Reuse-Resolution: `COMPOSE_APPLIED` from the established first prime-power mass law, exact factorial return, relation-field return lift, and classical finite Möbius convolution. No new general-purpose tool family is claimed.

## 1. Executive result

The same-scale adaptive residual isolated by the rectangular tail-return bridge can be removed from the list of open density obstructions.

The key observation is an elementary Möbius--harmonic factorization. Let

\[
u_q:=\frac{\Lambda(q)}q,
\qquad
A(x):=\sum_{q\le x}u_q,
\]

and use the already established first-mass estimate

\[
\boxed{A(x)=\log x+O(1).}
\tag{1.1}
\]

Then two exact finite convolutions with harmonic sums imply

\[
\sum_{d\le x}\frac{\mu(d)}d\log^2\frac xd
=2A(x)+O(1)
=2\log x+O(1).
\tag{1.2}
\]

Inserted into the Möbius form of Selberg's identity, this gives

\[
\boxed{
\sum_{q\le x}\Lambda(q)\log q
+
\sum_{ab\le x}\Lambda(a)\Lambda(b)
=2x\log x+O(x).
}
\tag{1.3}
\]

No prime number theorem is used in this derivation.

For

\[
R(n):=\psi(n)-n,
\qquad
r(n):=R(n)/n,
\]

(1.3), Chebyshev's bound, and the exact factorial return imply that the full signless residual

\[
\boxed{
\rho_n(r;n)
:=A(n)r(n)
+
\sum_{q\le n}\frac{\Lambda(q)}q
r\!\left(\left\lfloor\frac nq\right\rfloor\right)
=O(1)
}
\tag{1.4}
\]

uniformly in `n`.

Consequently the high/low adaptive residual relation energies from the V14 bridge contribute only

\[
\boxed{O((\log Y)^{-2})}
\tag{1.5}
\]

to the full degree-three packet. They are summable along the cube-root hierarchy.

The remaining obstruction is therefore no longer density matching, coefficient two, or same-scale scalar residual growth. It is the finite composition of the common-suffix transport and lower-scale tail channels with the two-channel energy envelope.

---

## 2. Arithmetic functions and exact convolution identity

Let

\[
L(n):=\log n,
\]

and let `*` denote Dirichlet convolution. Since

\[
L=\mathbf1*\Lambda,
\]

one has the pointwise divisor identity

\[
L(n)^2
=
\sum_{d\mid n}\Lambda(d)L(d)
+
\sum_{ab\mid n}\Lambda(a)\Lambda(b).
\tag{2.1}
\]

Equivalently,

\[
L^2
=
\mathbf1*(\Lambda L+\Lambda*\Lambda).
\]

Möbius inversion gives the exact Selberg primitive

\[
\boxed{
\mu*L^2
=\Lambda L+\Lambda*\Lambda.
}
\tag{2.2}
\]

Thus, with

\[
\mathcal S(x)
:=
\sum_{q\le x}\Lambda(q)\log q
+
\sum_{ab\le x}\Lambda(a)\Lambda(b),
\]

and

\[
F(y):=\sum_{m\le y}\log^2m,
\]

we have the exact summatory formula

\[
\boxed{
\mathcal S(x)
=
\sum_{d\le x}\mu(d)F(x/d).
}
\tag{2.3}
\]

---

## SCT-T01 — Three weighted Möbius moments

For integers `x>=1`, define

\[
M_j(x)
:=
\sum_{d\le x}\frac{\mu(d)}d
\log^j\frac xd
\qquad(j=0,1,2).
\tag{3.1}
\]

### Zeroth moment

The exact floor inversion

\[
\sum_{d\le x}\mu(d)\left\lfloor\frac xd\right\rfloor=1
\tag{3.2}
\]

implies

\[
\boxed{M_0(x)=O(1).}
\tag{3.3}
\]

Indeed, replacing the floor by `x/d` leaves at most `x` fractional parts.

### First moment

Let

\[
H(y):=\sum_{m\le y}\frac1m.
\]

The exact double convolution is

\[
\begin{aligned}
\sum_{d\le x}\frac{\mu(d)}dH(x/d)
&=
\sum_{dm\le x}\frac{\mu(d)}{dm}\\
&=
\sum_{n\le x}\frac1n\sum_{d\mid n}\mu(d)\\
&=1.
\end{aligned}
\tag{3.4}
\]

Using

\[
H(y)=\log y+\gamma+O(1/y),
\]

(3.3) and (3.4) give

\[
\boxed{M_1(x)=O(1).}
\tag{3.5}
\]

### Second moment

Let

\[
J(y):=\sum_{m\le y}\frac{\log m}{m}.
\]

There is an absolute constant `c_J` such that

\[
J(y)
=
\frac12\log^2y+c_J
+O\!\left(\frac{1+\log y}{y}\right).
\tag{3.6}
\]

The corresponding exact double convolution is

\[
\begin{aligned}
\sum_{d\le x}\frac{\mu(d)}dJ(x/d)
&=
\sum_{dm\le x}\frac{\mu(d)\log m}{dm}\\
&=
\sum_{n\le x}\frac1n
\sum_{d\mid n}\mu(d)\log(n/d)\\
&=
\sum_{n\le x}\frac{\Lambda(n)}n\\
&=A(x).
\end{aligned}
\tag{3.7}
\]

The total error in substituting (3.6) is bounded because

\[
\frac1x
\sum_{d\le x}
\left(1+\log\frac xd\right)=O(1).
\]

Therefore

\[
\boxed{
M_2(x)=2A(x)+O(1)
=2\log x+O(1).
}
\tag{3.8}
\]

This is the source of the coefficient `2`.

---

## SCT-T02 — Selberg coefficient two

Elementary summation gives, uniformly for `y>=1`,

\[
F(y)
=
y\bigl(\log^2y-2\log y+2\bigr)
+O(\log^2(2y)).
\tag{4.1}
\]

Insert (4.1) into (2.3):

\[
\mathcal S(x)
=
x\bigl(M_2(x)-2M_1(x)+2M_0(x)\bigr)
+O\!\left(
\sum_{d\le x}\log^2\frac{2x}{d}
\right).
\tag{4.2}
\]

A dyadic decomposition gives

\[
\sum_{d\le x}\log^2\frac{2x}{d}=O(x).
\tag{4.3}
\]

Using SCT-T01,

\[
\boxed{
\mathcal S(x)=2x\log x+O(x).
}
\tag{4.4}
\]

Equivalently, for the ordered prime-power square

\[
\Psi_2(x):=
\sum_{ab\le x}\Lambda(a)\Lambda(b),
\]

\[
\boxed{
\sum_{q\le x}\Lambda(q)\log q
+
\Psi_2(x)
=2x\log x+O(x).
}
\tag{4.5}
\]

This closes the coefficient-two analytic target left open in the earlier Selberg return-operator note, conditional only on the established first-mass law (1.1).

---

## 5. Ideal remainder return

Let

\[
\psi(n):=\sum_{q\le n}\Lambda(q),
\qquad
R(n):=\psi(n)-n.
\]

Write

\[
B(n):=\sum_{q\le n}\Lambda(q)\log q,
\qquad
D(n):=\sum_{q\le n}\Lambda(q)\left\lfloor\frac nq\right\rfloor.
\]

The exact factorial identity is

\[
\boxed{D(n)=\log(n!).}
\tag{5.1}
\]

Also put

\[
C(n):=\sum_{q\le n}\Lambda(q)\log(n/q).
\]

Then the following decomposition is exact:

\[
\boxed{
\begin{aligned}
&\log n\,R(n)
+
\sum_{q\le n}\Lambda(q)
R\!\left(\left\lfloor\frac nq\right\rfloor\right)\\
={}&
\bigl(B(n)+\Psi_2(n)-2n\log n\bigr)
+C(n)
+\bigl(n\log n-D(n)\bigr).
\end{aligned}
}
\tag{5.2}
\]

By (4.5), the first term is `O(n)`. Stirling gives the third term `O(n)`. Chebyshev's upper bound `psi(t)=O(t)` and partial summation give

\[
C(n)
=
\int_{1^-}^{n}\log(n/t)\,d\psi(t)
=O(n).
\tag{5.3}
\]

Consequently,

\[
\boxed{
\log n\,R(n)
+
\sum_{q\le n}\Lambda(q)R(\lfloor n/q\rfloor)
=O(n).
}
\tag{5.4}
\]

Since `A(n)-log n=O(1)` and Chebyshev gives `R(n)=O(n)`, (5.4) also yields

\[
\boxed{
A(n)R(n)
+
\sum_{q\le n}\Lambda(q)R(\lfloor n/q\rfloor)
=O(n).
}
\tag{5.5}
\]

---

## SCT-T03 — Exact floor-deformation formula

Let

\[
m_q:=\left\lfloor\frac nq\right\rfloor,
\qquad
\lambda_q(n):=\frac{n}{qm_q}.
\]

For `r(n)=R(n)/n`, the full prime-winding residual is

\[
\rho_n(r;n)
=A(n)r(n)+\sum_{q\le n}\frac{\Lambda(q)}q r(m_q).
\]

The exact decomposition is

\[
\boxed{
\rho_n(r;n)
=
\frac1n\left[
A(n)R(n)+\sum_{q\le n}\Lambda(q)R(m_q)
\right]
+\varepsilon(n),
}
\tag{6.1}
\]

where

\[
\boxed{
\varepsilon(n)
=
\frac1n\sum_{q\le n}
\Lambda(q)(\lambda_q(n)-1)R(m_q).
}
\tag{6.2}
\]

Writing `n=qm_q+s_q` with `0<=s_q<q`, we have

\[
\lambda_q(n)-1=\frac{s_q}{qm_q}.
\]

If `|R(m)|<=C_Rm` and `psi(n)<=C_psi n`, then

\[
\begin{aligned}
|\varepsilon(n)|
&\le
\frac{C_R}{n}
\sum_{q\le n}\Lambda(q)\frac{s_q}{q}\\
&\le
C_RC_\psi.
\end{aligned}
\tag{6.3}
\]

Combining (5.5) and (6.3),

\[
\boxed{\rho_n(r;n)=O(1)}
\tag{6.4}
\]

uniformly in `n`.

---

## SCT-T04 — Full-cutoff completion of both deep branches

Let

\[
U_0:=A(Y),
\qquad
U_1:=A(Y^2)-A(Y).
\]

For any intermediate vertex `n>Y`, define the full tail coefficient

\[
\boxed{V_Y(n):=A(n)-A(Y).}
\tag{7.1}
\]

and the lower-scale tail channel

\[
\boxed{
E_Y(f;n)
:=\sum_{Y<q\le n}\frac{\Lambda(q)}q
f(\lfloor n/q\rfloor).
}
\tag{7.2}
\]

Then the exact full return equation is

\[
\boxed{
(U_0+V_Y(n))f(n)
+
\sum_{q\le Y}\frac{\Lambda(q)}q
f(\lfloor n/q\rfloor)
=
\rho_n(f;n)-E_Y(f;n).
}
\tag{7.3}
\]

### High branch

For

\[
h_a=\lfloor Y^3/a\rfloor,
\qquad a\le Y,
\]

the original pair coefficient

\[
V_H(a)=A(\lfloor h_a/Y\rfloor)-A(Y)
\]

satisfies

\[
V_H(a)\le V_Y(h_a).
\]

Therefore

\[
Q_H(a)\le U_1V_H(a)\le U_1V_Y(h_a),
\tag{7.4}
\]

so the larger full-cutoff coefficient still absorbs the complete high suffix-pair density.

Every tail descendant in (7.2) satisfies

\[
\left\lfloor\frac{h_a}{q}\right\rfloor
<\frac{h_a}{Y}<Y^2
\qquad(q>Y),
\tag{7.5}
\]

because every nonzero prime-power action has `a>=2`.

### Low branch

For

\[
\ell_b=\lfloor Y^3/b\rfloor,
\qquad b>Y,
\]

the earlier low coefficient is already

\[
S_L(b)=A(\ell_b)-A(Y)=V_Y(\ell_b).
\]

Every tail descendant satisfies

\[
\left\lfloor\frac{\ell_b}{q}\right\rfloor<Y
\qquad(q>Y),
\tag{7.6}
\]

because `ell_b<Y^2`.

Thus both branches use the same full-cutoff return residual (6.4), while all `q>Y` terms descend to a strict lower scale.

---

## SCT-T05 — Residual relation energy is summable

Let `w_i>=0` have total mass `W`, and suppose

\[
|\rho_i|\le C_\rho.
\]

Then

\[
\boxed{
\mathcal E_w(\rho)
:=\sum_{i,j}w_iw_j(\rho_i-\rho_j)^2
\le4C_\rho^2W^2.
}
\tag{8.1}
\]

Insert this into the normalized rectangular high/low estimate. The high first-label mass is `U_0`; the low first-label mass is `U_1`. For all three colors, the residual contribution is at most

\[
\boxed{
\frac{54C_\rho^2U_1}{T_Y},
}
\tag{8.2}
\]

where the full ordered degree-three packet mass satisfies

\[
T_Y=\frac92(\log Y)^3+O((\log Y)^2),
\qquad
U_1=\log Y+O(1).
\]

Consequently,

\[
\boxed{
\mathcal E_{\rm residual}^{\rm deep}(Y)
=O((\log Y)^{-2}).
}
\tag{8.3}
\]

Along `log Y_k=3^k log Y_0`, this forcing is geometrically summable.

---

## 9. What has now been closed

The chain of the formerly missing bridge is now:

\[
\boxed{
\begin{aligned}
&\text{endpoint-conditioned history variance}\\
&\quad\le\text{aggregate high/low marginal variance}\\
&\quad\le\text{positive one-body tail-potential defects}\\
&\quad\le\text{full return residual energy}
+\text{common-suffix transport}
+\text{strict lower-scale tail}\\
&\quad=O((\log Y)^{-2})
+\text{transport}
+\text{strict lower-scale tail}.
\end{aligned}
}
\tag{9.1}
\]

The following are no longer open:

1. the shape of the induced high/low density;
2. endpoint disintegration;
3. control for unbounded readouts;
4. conversion of two-body density to a positive relation defect;
5. the rectangular adaptive return equation;
6. the Selberg coefficient `2`;
7. uniform control of the full signless scalar residual;
8. summability of its deepest relation-energy contribution.

---

## 10. Remaining frontier

The remaining problem is a finite multichannel cascade composition:

1. combine the common-suffix nonexpansion with the exact `S_3` standard-sector coefficient `1/9`;
2. route the full tail channel `E_Y` through the top/middle/bottom logarithmic scale bands without double counting;
3. prove one block-energy recurrence for the history mean and standard sectors together;
4. identify that recurrence with the complete odd-simplex energy `mathfrak E_N`;
5. only then promote a native logarithmic remainder for `psi(N)/N-1`.

No RH-scale estimate is claimed. No quantitative prime remainder is promoted in this checkpoint. The decisive scalar arithmetic bridge, however, is closed at research-note theorem strength using only first-mass Mertens input, Chebyshev, finite convolution, and Stirling.
