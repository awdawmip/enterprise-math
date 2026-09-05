# Spectral formal phase, decimation linearization, and Jordan-totient diagonalization

Status: `FREE_RESEARCH / EXACT FORMAL-SPECTRAL THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`

## 0. Purpose

The finite Dirichlet spectral family developed in #1159 has three structures already established independently:

1. integer spectral decimation polynomials `R_n` with
   `R_(mn)=R_m o R_n` and `R_2(u)=u(4-u)`;
2. normalized finite determinants
   `H_M(u)=D_(M-1)(u)/M`, satisfying the scale cocycle
   `H_(mn)(u)=H_m(u) H_n(R_m(u))`;
3. primitive denominator factors obtained by divisor/Mobius decomposition of the finite spectrum.

This note shows that these are all shadows of one formal coordinate.  In that coordinate the nonlinear decimation semigroup becomes exactly linear, and primitive reciprocal spectral moments diagonalize into pure Jordan totients instead of mixtures of several Jordan orders.

No circle, Fourier basis, classical `pi`, or cyclotomic roots are needed for the formal theorem.

---

## 1. Integer decimation semigroup

Let the integer polynomial family `R_n in Z[u]` be the finite phase-multiplication maps, normalized by

`R_1(u)=u`,

and satisfying

`R_(mn)=R_m o R_n = R_n o R_m`.

The first cases are

`R_2(u)=u(4-u)`,

`R_3(u)=u(3-u)^2`,

`R_5(u)=u(u^2-5u+5)^2`.

At the fixed point `u=0`,

`R_n(0)=0`,

and direct recurrence differentiation gives

`R_n'(0)=n^2`.

Thus every `R_n` has the same fixed point but a different quadratic-scale multiplier `n^2`.

---

## 2. Unique common formal phase coordinate

Work in `Q[[u]]`.

There is a unique formal power series

\[
\boxed{\ell(u)=u+O(u^2)}
\]

satisfying

\[
\boxed{\ell(R_2(u))=4\ell(u).}
\tag{FP-1}
\]

### Existence and uniqueness

Write

\[
\ell(u)=u+\sum_{r\ge2} a_r u^r.
\]

Since

`R_2(u)=4u-u^2`,

the coefficient of `a_r` in degree `r` on the left of (FP-1) is `4^r a_r`, whereas the right contributes `4a_r`.  All remaining degree-`r` terms depend only on `a_2,...,a_(r-1)`.

Hence

\[
(4^r-4)a_r=(\text{known rational expression in lower coefficients}),
\]

and because `4^r-4 != 0` for `r>=2`, the coefficients exist and are unique recursively in `Q`.

The first terms are

\[
\boxed{
\ell(u)
=u+\frac{u^2}{12}+\frac{u^3}{90}+\frac{u^4}{560}
+\frac{u^5}{3150}+\frac{u^6}{16632}+\cdots .
}
\tag{FP-2}
\]

### Simultaneous linearization of every integer decimation

For any integer `n>=1`, define

\[
f_n(u):=\frac{\ell(R_n(u))}{n^2}.
\]

Using `R_n o R_2 = R_2 o R_n`,

\[
f_n(R_2(u))=4 f_n(u).
\]

Also

\[
f_n(u)=u+O(u^2)
\]

because `R_n'(0)=n^2` and `ell'(0)=1`.

By uniqueness of the normalized solution of (FP-1), `f_n=ell`.  Therefore

\[
\boxed{
\ell(R_n(u))=n^2\ell(u)
\qquad(n\ge1).
}
\tag{FP-3}
\]

This is the common Koenigs/formal-phase coordinate of the entire finite spectral renormalization semigroup.

Let `U(t)` be the compositional inverse of `ell`, so

\[
U(t)=t-\frac{t^2}{12}+\frac{t^3}{360}-\frac{t^4}{20160}+\cdots,
\]

and (FP-3) is equivalently

\[
\boxed{R_n(U(t))=U(n^2t).}
\tag{FP-4}
\]

Classification: `EXACT_FORMAL_ALGEBRA / COMMON_DECIMATION_LINEARIZATION`.

---

## 3. The determinant cocycle becomes a diagonal scale cocycle

Let

\[
H_M(u):=\frac{D_{M-1}(u)}{M},
\qquad H_M(0)=1.
\]

The finite scale cocycle is

\[
\boxed{
H_{mn}(u)=H_m(u)H_n(R_m(u)).
}
\tag{FP-5}
\]

Define its formal logarithm in the linearized coordinate:

\[
\mathcal L_M(t):=-\log H_M(U(t)).
\]

Then (FP-4) and (FP-5) give

\[
\boxed{
\mathcal L_{mn}(t)
=\mathcal L_m(t)+\mathcal L_n(m^2t).
}
\tag{FP-6}
\]

Write

\[
\mathcal L_M(t)=\sum_{s\ge1} a_s(M)t^s.
\]

Coefficient comparison in (FP-6) yields

\[
a_s(mn)=a_s(m)+m^{2s}a_s(n).
\tag{FP-7}
\]

Because multiplication is commutative, also

\[
a_s(mn)=a_s(n)+n^{2s}a_s(m).
\]

Hence for every `m,n>1`,

\[
(m^{2s}-1)a_s(n)=(n^{2s}-1)a_s(m).
\]

Therefore there is a universal rational constant `kappa_s`, independent of `M`, such that

\[
\boxed{
a_s(M)=\kappa_s(M^{2s}-1).
}
\tag{FP-8}
\]

Thus

\[
\boxed{
-\log H_M(U(t))
=\sum_{s\ge1}\kappa_s(M^{2s}-1)t^s.
}
\tag{FP-9}
\]

This is an exact formal diagonalization of the finite determinant scale cocycle.

The constants are themselves defined purely from finite algebra.  For example, using `M=2`,

\[
\boxed{
\kappa_s
=\frac{[t^s]\{-\log H_2(U(t))\}}{4^s-1}.
}
\tag{FP-10}
\]

Since `H_2(u)=1-u/2` and `U(t) in Q[[t]]`, every `kappa_s` is rational.

The first values are

\[
\boxed{
\kappa_1=\frac16,
\quad
\kappa_2=\frac1{180},
\quad
\kappa_3=\frac1{2835},
\quad
\kappa_4=\frac1{37800},
\quad
\kappa_5=\frac1{467775},\ldots
}
\tag{FP-11}
\]

---

## 4. Primitive spectral factors and a Witt-like ghost decomposition

Let `widehatPsi_d(u)` be the primitive denominator-`d` factor normalized by

\[
\widehat\Psi_d(0)=1.
\]

Equivalently, by spectral Mobius inversion,

\[
\boxed{
\widehat\Psi_d(u)
=\prod_{e\mid d} H_e(u)^{\mu(d/e)}
\qquad(d>1).
}
\tag{FP-12}
\]

Taking formal logarithms after the common phase change `u=U(t)`,

\[
-\log\widehat\Psi_d(U(t))
=\sum_{e\mid d}\mu(d/e)\mathcal L_e(t).
\]

Insert (FP-9):

\[
\begin{aligned}
-\log\widehat\Psi_d(U(t))
&=\sum_{s\ge1}\kappa_s
\left(\sum_{e\mid d}\mu(d/e)(e^{2s}-1)\right)t^s\\
&=\sum_{s\ge1}\kappa_s J_{2s}(d)t^s,
\end{aligned}
\]

because for `d>1`, `sum_(e|d) mu(d/e)=0`, while

\[
\sum_{e\mid d}\mu(d/e)e^{2s}=J_{2s}(d).
\]

Therefore

\[
\boxed{
-\log\widehat\Psi_d(U(t))
=\sum_{s\ge1}\kappa_s J_{2s}(d)t^s.
}
\tag{FP-13}
\]

This is the exact all-orders Jordan diagonalization.

Interpretation: the ordinary `u` coordinate mixes spectral moments of several Jordan orders, while the formal phase coordinate `t=ell(u)` diagonalizes the divisor arithmetic.  The quantities `J_(2s)(d)` are the ghost coordinates of the primitive spectral factorization.

Classification: `EXACT_SPECTRAL_DIVISOR_ARITHMETIC / WITT-LIKE_GHOST_DIAGONALIZATION`.

---

## 5. All ordinary primitive reciprocal moments at once

Let

\[
Z_s^{\rm prim}(d)
:=\sum_{\substack{1\le r<d\\(r,d)=1}}
 u_{r,d}^{-s}.
\]

By the normalized root product,

\[
\boxed{
-\log\widehat\Psi_d(u)
=\sum_{s\ge1}\frac{Z_s^{\rm prim}(d)}{s}u^s.
}
\tag{FP-14}
\]

Combining (FP-13) with `t=ell(u)` gives the all-orders transform

\[
\boxed{
Z_n^{\rm prim}(d)
=
 n\sum_{r=1}^{n}
 \kappa_r J_{2r}(d)
 [u^n]\ell(u)^r.
}
\tag{FP-15}
\]

Thus every ordinary primitive reciprocal moment is a universal lower-triangular rational combination

\[
\boxed{
Z_n^{\rm prim}(d)
=\sum_{r=1}^{n} A_{n,r}J_{2r}(d),
\qquad A_{n,r}\in\mathbf Q,
}
\tag{FP-16}
\]

and the coefficients are explicitly

\[
A_{n,r}=n\kappa_r[u^n]\ell(u)^r.
\]

The first rows are

\[
\boxed{Z_1^{\rm prim}(d)=\frac{J_2(d)}6,}
\]

\[
\boxed{
Z_2^{\rm prim}(d)=\frac{5J_2(d)+2J_4(d)}{180},
}
\]

\[
\boxed{
Z_3^{\rm prim}(d)
=\frac{42J_2(d)+21J_4(d)+8J_6(d)}{7560},
}
\]

\[
\boxed{
Z_4^{\rm prim}(d)
=\frac{270J_2(d)+147J_4(d)+80J_6(d)+24J_8(d)}{226800}.
}
\tag{FP-17}

The previously observed Jordan mixtures are therefore not separate coincidences; they are exactly the coordinate-change matrix from the nonlinear spectral coordinate `u` to the common formal phase `ell(u)`.

---

## 6. Full spectral moments and even-zeta constants

Let

\[
Z_s(M)=\sum_{k=1}^{M-1}u_{k,M}^{-s}.
\]

From (FP-9) with `t=ell(u)`, the coefficient of the highest power `M^(2s)` in `Z_s(M)` can only come from the `r=s` term, because `ell(u)^s=u^s+O(u^(s+1))`.

Hence

\[
\boxed{
Z_s(M)=s\kappa_s M^{2s}+O(M^{2s-2})
}
\tag{FP-18}
\]

as a polynomial identity in `M^2` at leading degree.

Internal phase quantization and the bound `rho_(k,M)>=2k` give the independent limit

\[
\frac{Z_s(M)}{M^{2s}}
\longrightarrow
\frac1{\tau^{2s}}\sum_{k\ge1}\frac1{k^{2s}}.
\]

Therefore

\[
\boxed{
\zeta(2s)=s\kappa_s\tau^{2s}.
}
\tag{FP-19}
\]

This identifies every even-zeta coefficient with one of the rational diagonal coefficients of the finite spectral renormalization cocycle.

In the later classical compatibility layer,

\[
\kappa_s
=(-1)^{s+1}
\frac{2^{2s-1}B_{2s}}{s(2s)!},
\]

so (FP-19) becomes the usual Bernoulli formula.  But the rational constants `kappa_s` are already defined and computable before Bernoulli numbers or classical `pi` are named.

Freeze:

`EVEN_ZETA_RATIONAL_COEFFICIENTS = FINITE_SPECTRAL_RG_DIAGONAL_COEFFICIENTS`.

---

## 7. Later analytic compatibility, not proof input

After the formal theorem is established, the internal analytic phase identifies

\[
\boxed{
\ell(u)=4\arcsin^2(\sqrt u/2)
}
\]

as a classical readout, with inverse

\[
\boxed{
U(t)=4\sin^2(\sqrt t/2).
}
\]

This explains the name “formal phase”: if `u=4 sin^2(theta/2)`, then `ell(u)=theta^2`, and `R_n` is simply `theta -> n theta` after squaring the phase coordinate.

But neither arcsine nor sine is required to construct `ell`, prove uniqueness, prove simultaneous linearization, or derive (FP-13).

---

## 8. Structural consequence

The #1159 finite spectrum now has the following algebraic hierarchy:

```text
integer Dirichlet recurrence
  -> commuting integer decimation maps R_n
  -> unique rational formal phase ell
  -> exact linear action t -> n^2 t
  -> determinant scale cocycle diagonalizes
  -> universal rational coefficients kappa_s
  -> divisor Mobius transform
  -> pure Jordan ghost coordinates J_(2s)
  -> ordinary moments recovered by one universal triangular coordinate change
  -> even-zeta values from the same kappa_s after analytic completion
```

This is stronger than separately observing Jordan-totient moment formulas or Bernoulli/even-zeta limits.

Freeze at free-research strength:

`COMMON_FORMAL_PHASE_LINEARIZES_ALL_INTEGER_SPECTRAL_DECIMATIONS`.

`PRIMITIVE_SPECTRAL_LOG_IN_FORMAL_PHASE = PURE_JORDAN_GHOST_SERIES`.

`ORDINARY_PRIMITIVE_MOMENTS = UNIVERSAL_TRIANGULAR_PULLBACK_OF_JORDAN_GHOSTS`.

`EVEN_ZETA_COEFFICIENTS = FINITE_RG_DIAGONAL_COEFFICIENTS`.
