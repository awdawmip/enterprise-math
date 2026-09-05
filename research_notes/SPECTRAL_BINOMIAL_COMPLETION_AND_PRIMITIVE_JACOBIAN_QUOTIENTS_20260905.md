# Spectral binomial completion and primitive Jacobian quotients

Status: `FREE_RESEARCH / EXACT INTERNAL COMPLETION THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- formal phase `ell` and inverse `U`;
- `ell(u_(k,M))=k^2 tau^2/M^2`;
- Jacobian identity `H_M(U(t))=U'(M^2t)/U'(t)`;
- primitive Mobius factorization.

## 1. Central-binomial expansion of the formal phase

The formal phase coefficients are

\[
\boxed{
\ell(u)
=2\sum_{n\ge1}
\frac{u^n}{n^2\binom{2n}{n}}.
}
\tag{BC-1}
\]

All coefficients are positive and the consecutive-term ratio is strictly below `u/4` for `0<u<4`.

---

## 2. Every finite mode gives a completion series for `tau^2`

For every finite Dirichlet mode

\[
1\le k<M,
\]

internal phase quantization gives

\[
\boxed{
\ell(u_{k,M})
=\frac{k^2\tau^2}{M^2}.
}
\tag{BC-2}
\]

Insert (BC-1):

\[
\boxed{
\tau^2
=\frac{2M^2}{k^2}
\sum_{n\ge1}
\frac{u_{k,M}^n}{n^2\binom{2n}{n}}.
}
\tag{BC-3}
\]

Thus every algebraic finite spectral root supplies an exact central-binomial completion series for the same internal constant.

This is an infinite family of identities indexed by finite mode data rather than by a preselected transcendental argument.

---

## 3. Rational special case from the three-step chain

For `M=3`,

\[
D_2(u)=(2-u)^2-1=(u-1)(u-3),
\]

so the first root is exactly

\[
u_{1,3}=1.
\]

Taking `(M,k)=(3,1)` in (BC-3) gives the purely rational series

\[
\boxed{
\tau^2
=18\sum_{n\ge1}
\frac{1}{n^2\binom{2n}{n}}.
}
\tag{BC-4}
\]

Since the finite-spectral moment route independently gives

\[
\zeta(2)=\tau^2/6,
\]

we obtain

\[
\boxed{
\zeta(2)
=3\sum_{n\ge1}
\frac{1}{n^2\binom{2n}{n}}.
}
\tag{BC-5}
\]

This is obtained internally from finite spectral phase plus the formal-phase coefficient recurrence.  The later naming `tau=pi` is not used in the derivation.

---

## 4. Other algebraic spectral series

For the one-edge interior chain `M=2`, `u_(1,2)=2`, so

\[
\boxed{
\tau^2
=8\sum_{n\ge1}
\frac{2^n}{n^2\binom{2n}{n}}.
}
\tag{BC-6}
\]

For `M=4`, the first mode is the nested-radical root

\[
u_{1,4}=2-\sqrt2,
\]

and

\[
\boxed{
\tau^2
=32\sum_{n\ge1}
\frac{(2-\sqrt2)^n}{n^2\binom{2n}{n}}.
}
\tag{BC-7}
\]

More generally, dyadic first modes give a tower of increasingly small algebraic arguments and therefore rapidly convergent completion series.

---

## 5. Explicit finite tail certificate

Let

\[
S_N(u):=2\sum_{n=1}^{N}
\frac{u^n}{n^2\binom{2n}{n}}.
\]

For `0<u<4`, positivity and the coefficient ratio give

\[
\boxed{
0<\ell(u)-S_N(u)
\le
\frac{2u^{N+1}}
{(N+1)^2\binom{2N+2}{N+1}(1-u/4)}.
}
\tag{BC-8}
\]

Therefore every finite spectral mode gives the target-free algebraic bracket

\[
\boxed{
\frac{M^2}{k^2}S_N(u_{k,M})
<\tau^2
\le
\frac{M^2}{k^2}
\left(
S_N(u_{k,M})+
\frac{2u_{k,M}^{N+1}}
{(N+1)^2\binom{2N+2}{N+1}(1-u_{k,M}/4)}
\right).
}
\tag{BC-9}
\]

This is a square-free variant of the single-scale completion certificate: no final square root is required if the target observable is `tau^2` or `zeta(2)`.

---

## 6. Primitive factors as Mobius quotients of the completion Jacobian

Recall

\[
H_M(U(t))
=\frac{U'(M^2t)}{U'(t)}.
\]

For `d>1`, the normalized primitive factor is

\[
\widehat\Psi_d(u)
=\prod_{e\mid d}H_e(u)^{\mu(d/e)}.
\]

Substitute `u=U(t)`:

\[
\widehat\Psi_d(U(t))
=
\prod_{e\mid d}
\left(\frac{U'(e^2t)}{U'(t)}\right)^{\mu(d/e)}.
\]

Because

\[
\sum_{e\mid d}\mu(d/e)=0,
\]

the common denominator cancels exactly, leaving

\[
\boxed{
\widehat\Psi_d(U(t))
=
\prod_{e\mid d}
U'(e^2t)^{\mu(d/e)}.
}
\tag{BC-10}
\]

This is an exact formal-unit identity.

---

## 7. Primitive internal sine quotient

Set

\[
t=x^2.
\]

Since

\[
U'(x^2)=F(x)=S(x)/x,
\]

(BC-10) becomes

\[
\boxed{
\widehat\Psi_d(U(x^2))
=
\prod_{e\mid d}
F(ex)^{\mu(d/e)}
=
\prod_{e\mid d}
\left(\frac{S(ex)}{ex}\right)^{\mu(d/e)}.
}
\tag{BC-11}
\]

The normalizing powers of `x` and integer `e` cancel globally through the Mobius exponent sum in the formal-unit interpretation.

Thus each primitive finite spectral factor is exactly a divisor-Mobius quotient of the internally reconstructed completion Jacobian.

This identity precedes the later classical interpretation as a cyclotomic/trigonometric quotient.

---

## 8. Jordan diagonalization follows immediately

Take logarithms of (BC-10):

\[
-\log\widehat\Psi_d(U(t))
=
\sum_{e\mid d}\mu(d/e)\mathcal K(e^2t),
\]

where

\[
\mathcal K(t)=-\log U'(t)=\sum_{r\ge1}\kappa_rt^r.
\]

Therefore

\[
\begin{aligned}
-\log\widehat\Psi_d(U(t))
&=
\sum_{r\ge1}\kappa_rt^r
\sum_{e\mid d}\mu(d/e)e^{2r}\\
&=
\boxed{
\sum_{r\ge1}\kappa_rJ_{2r}(d)t^r.
}
\end{aligned}
\tag{BC-12}
\]

So the primitive Jacobian quotient (BC-10) is the multiplicative master identity whose logarithm is the Jordan ghost expansion.

---

## 9. Structural synthesis

The same inverse formal phase `U` now yields both a completion series and primitive factor arithmetic:

```text
finite spectral mode u_(k,M)
  -> ell(u_(k,M)) = k^2 tau^2/M^2
  -> central-binomial series for tau^2

finite determinant H_M
  -> H_M(U(t)) = U'(M^2t)/U'(t)
  -> divisor Mobius inversion
  -> primitive factor = Mobius quotient of U'
  -> logarithm = Jordan-totient ghost series
```

Freeze at free-research strength:

`EVERY_FINITE_MODE -> EXACT_CENTRAL_BINOMIAL_COMPLETION_SERIES`.

`PRIMITIVE_SPECTRAL_FACTOR = MOBIUS_JACOBIAN_QUOTIENT`.

`JORDAN_GHOST_SERIES = LOGARITHM_OF_PRIMITIVE_COMPLETION_QUOTIENT`.
