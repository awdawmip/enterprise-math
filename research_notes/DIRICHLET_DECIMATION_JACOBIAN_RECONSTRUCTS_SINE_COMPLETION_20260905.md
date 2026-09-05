# Dirichlet determinant as decimation Jacobian and reconstruction of the internal sine completion

Status: `FREE_RESEARCH / EXACT FINITE+FORMAL SYNTHESIS / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`

## 0. Main statement

The finite Dirichlet determinant and the integer spectral-decimation family are not merely compatible objects.  They are differential aspects of the same polynomial map.

Let

\[
D_0(u)=1,
\quad D_1(u)=2-u,
\quad D_{m+2}(u)=(2-u)D_{m+1}(u)-D_m(u),
\]

and

\[
H_M(u):=\frac{D_{M-1}(u)}{M}.
\]

Let the integer decimation polynomial be

\[
R_M(u)=2-C_M(2-u),
\]

where

\[
C_0(x)=2,
\quad C_1(x)=x,
\quad C_{m+1}(x)=xC_m(x)-C_{m-1}(x).
\]

Then

\[
\boxed{R_M'(u)=M D_{M-1}(u)=M^2H_M(u).}
\tag{DJ-1}
\]

Consequently the genuine finite Dirichlet eigenvalues are exactly the critical points of the finite decimation map `R_M`.

---

## 1. Pure polynomial proof kernel

The rescaled first/second-kind recurrence identities give

\[
\boxed{C_M'(x)=M U_{M-1}(x),}
\tag{DJ-2}
\]

where `U_(M-1)(2-u)=D_(M-1)(u)` in the current normalization.

Because

\[
R_M(u)=2-C_M(2-u),
\]

chain differentiation gives

\[
R_M'(u)=C_M'(2-u)=M D_{M-1}(u),
\]

which is (DJ-1).

This is finite polynomial algebra.  No eigenvalue formula or trigonometric function is required.

---

## 2. The companion Pell/Shabat identity

The same recurrences give

\[
C_M(x)^2-4=(x^2-4)U_{M-1}(x)^2.
\]

Substituting `x=2-u` yields

\[
\boxed{
R_M(u)(4-R_M(u))
=u(4-u)D_{M-1}(u)^2.
}
\tag{DJ-3}
\]

Combining (DJ-1) and (DJ-3):

\[
\boxed{
 u(4-u)R_M'(u)^2
 =M^2R_M(u)(4-R_M(u)).
}
\tag{DJ-4}
\]

Thus the rational quadratic differential

\[
\boxed{
q(u):=\frac{du^2}{u(4-u)}
}
\]

satisfies the exact pullback law

\[
\boxed{R_M^*q=M^2q.}
\tag{DJ-5}
\]

Every finite critical point therefore maps to one of the two finite critical values `0` or `4`.  After normalization by four, `R_M/4` is a polynomial with finite critical values in `{0,1}`; this is the algebraic Shabat/Belyi compatibility of the decimation family.

The Belyi terminology is a later algebraic-geometry readout; the identities (DJ-3)-(DJ-5) are the native content.

---

## 3. Parity is the two critical-value fibers

Let

\[
E_M(u)=\prod_{\substack{1\le k<M\\ k\;\mathrm{even}}}(u-u_{k,M}),
\]

\[
O_M(u)=\prod_{\substack{1\le k<M\\ k\;\mathrm{odd}}}(u-u_{k,M}),
\]

with both products monic.

Internal phase quantization identifies the critical value of `u_(k,M)`:

\[
R_M(u_{k,M})=
\begin{cases}
0,&k\text{ even},\\
4,&k\text{ odd}.
\end{cases}
\]

Since all finite critical points are simple, degree and leading-coefficient comparison give exact square factorizations.

For `M=2q`:

\[
\boxed{
R_{2q}(u)=u(4-u)E_{2q}(u)^2,
}
\tag{DJ-6}
\]

\[
\boxed{
4-R_{2q}(u)=O_{2q}(u)^2.
}
\tag{DJ-7}
\]

For `M=2q+1`:

\[
\boxed{
R_{2q+1}(u)=uE_{2q+1}(u)^2,
}
\tag{DJ-8}
\]

\[
\boxed{
4-R_{2q+1}(u)=(4-u)O_{2q+1}(u)^2.
}
\tag{DJ-9}
\]

Thus the even/odd spectral split is exactly the split between the two finite critical-value fibers of the decimation polynomial.

---

## 4. Parity root products from one derivative evaluation

Because

\[
R_M'(0)=M^2,
\]

the factorizations above immediately give the parity products.

For `M=2q`:

\[
4E_{2q}(0)^2=(2q)^2,
\]

so

\[
\boxed{
\prod_{r=1}^{q-1}u_{2r,2q}=q.
}
\tag{DJ-10}
\]

Also

\[
O_{2q}(0)^2=4,
\]

so

\[
\boxed{
\prod_{r=1}^{q}u_{2r-1,2q}=2.
}
\tag{DJ-11}
\]

This recovers the two key factors behind the #1159 parity-curvature collapse from the critical-value geometry alone.

For odd length `M=2q+1`, the same argument gives the useful extension

\[
\boxed{
\prod_{r=1}^{q}u_{2r,2q+1}=2q+1,
}
\tag{DJ-12}
\]

\[
\boxed{
\prod_{r=0}^{q-1}u_{2r+1,2q+1}=1.
}
\tag{DJ-13}
\]

The familiar even-length values `q` and `2` are therefore one parity of a more general critical-fiber product law.

---

## 5. Common formal phase and its inverse

Let

\[
\ell(u)=u+O(u^2)
\]

be the unique common formal phase satisfying

\[
\ell(R_M(u))=M^2\ell(u).
\]

Let

\[
U(t):=\ell^{-1}(t).
\]

Then

\[
\boxed{
R_M(U(t))=U(M^2t).
}
\tag{DJ-14}
\]

Differentiate (DJ-14):

\[
R_M'(U(t))U'(t)
=M^2U'(M^2t).
\]

Using (DJ-1):

\[
\boxed{
H_M(U(t))
=\frac{U'(M^2t)}{U'(t)}.
}
\tag{DJ-15}
\]

This is an exact formal Jacobian cocycle for every finite `M`.

It implies the finite determinant scale cocycle automatically.

---

## 6. The completion series is forced by the dyadic finite algebra

For `M=2`, (DJ-14) gives

\[
\boxed{
U(4t)=U(t)(4-U(t)).
}
\tag{DJ-16}
\]

Normalize

\[
U(t)=t+O(t^2).
\]

Write

\[
U(t)=\sum_{n\ge1}a_nt^n,
\qquad a_1=1.
\]

Coefficient comparison in (DJ-16) gives, for `n>=2`,

\[
\boxed{
(4^n-4)a_n
=-\sum_{j=1}^{n-1}a_ja_{n-j}.
}
\tag{DJ-17}
\]

Since `4^n-4 != 0`, the coefficients are uniquely forced in `Q`.

The closed solution is

\[
\boxed{
a_n=\frac{2(-1)^{n+1}}{(2n)!}.}
\tag{DJ-18}
\]

Indeed substitution into (DJ-17) reduces exactly to the even-binomial identity

\[
\sum_{j=1}^{n-1}\binom{2n}{2j}
=2^{2n-1}-2
=\frac{4^n-4}{2}.
\]

Therefore

\[
\boxed{
U(t)
=2\sum_{n\ge1}
\frac{(-1)^{n+1}t^n}{(2n)!}.
}
\tag{DJ-19}
\]

and differentiation gives

\[
\boxed{
U'(t)
=\sum_{j\ge0}
\frac{(-1)^jt^j}{(2j+1)!}.
}
\tag{DJ-20}
\]

Thus the internal completion coefficients are not an external sine ansatz: they are uniquely reconstructed from the finite dyadic decimation law plus the identity-near normalization.

Classification: `FINITE_DECIMATION_ALGEBRA -> UNIQUE_FORMAL_COMPLETION`.

---

## 7. Reconstructing the internal S/C pair

Define purely from `U`:

\[
\boxed{
S(x):=xU'(x^2),
}
\tag{DJ-21}
\]

\[
\boxed{
C(x):=1-\frac{U(x^2)}{2}.
}
\tag{DJ-22}
\]

Then (DJ-19)-(DJ-20) give

\[
\boxed{
S(x)=\sum_{j\ge0}\frac{(-1)^jx^{2j+1}}{(2j+1)!},
}
\tag{DJ-23}
\]

\[
\boxed{
C(x)=\sum_{j\ge0}\frac{(-1)^jx^{2j}}{(2j)!}.
}
\tag{DJ-24}
\]

Termwise differentiation yields

\[
\boxed{S'=C,\qquad C'=-S.}
\tag{DJ-25}
\]

With the initial data `S(0)=0`, `C(0)=1`,

\[
(S^2+C^2)'=0,
\]

hence

\[
\boxed{S^2+C^2=1.}
\tag{DJ-26}
\]

So the entire internal rotation-law pair is recovered from the finite decimation algebra.

---

## 8. The finite determinant is the finite Jacobian approximation to the completion

Equation (DJ-20) implies

\[
\boxed{
F(x):=\frac{S(x)}x=U'(x^2)
}
\tag{DJ-27}
\]

with the normalized value `F(0)=1`.

For the finite carrier,

\[
F_M(x)=H_M(x^2/M^2).
\]

Using (DJ-1),

\[
\boxed{
F_M(x)
=\frac1{M^2}
R_M'\!\left(\frac{x^2}{M^2}\right).
}
\tag{DJ-28}
\]

Thus WSR-T02 is literally a convergence theorem for normalized Jacobians of finite decimation maps.

A phase-corrected exact identity is even stronger:

\[
\boxed{
H_M\!\left(U\!\left(\frac{t}{M^2}\right)\right)
=\frac{U'(t)}{U'(t/M^2)}.
}
\tag{DJ-29}
\]

As `M -> infinity`, the denominator tends to one, leaving `U'(t)`.

---

## 9. Exact phase quantization becomes a uniform lattice

Because

\[
H_M(U(t))=\frac{U'(M^2t)}{U'(t)},
\]

finite spectral roots are pulled back from zeros of `U'` by the linear scale `t -> M^2t`.

After defining `tau` as the first positive zero of `S`, the zeros of `U'` occur at

\[
t=k^2\tau^2.
\]

Hence the finite Dirichlet roots satisfy

\[
\boxed{
\ell(u_{k,M})
=\frac{k^2\tau^2}{M^2}.
}
\tag{DJ-30}
\]

So in the native nonlinear spectral coordinate `u` the roots look curved, while in the formal phase coordinate they lie on an exact quadratic lattice.

An oriented square-root lift `eta=sqrt(ell)` would put them on the uniform linear lattice

\[
\eta(u_{k,M})=\frac{k\tau}{M},
\]

but that lift requires a branch/sheet choice; this matches the BRC warning that projective scalar coordinates do not replace retained frame/orientation data.

---

## 10. Master logarithmic potential

Define

\[
\boxed{
\mathcal K(t):=-\log U'(t)
=\sum_{s\ge1}\kappa_st^s.
}
\tag{DJ-31}
\]

From (DJ-15):

\[
\boxed{
-\log H_M(U(t))
=\mathcal K(M^2t)-\mathcal K(t).
}
\tag{DJ-32}
\]

Thus the universal rational coefficients `kappa_s` of the formal-phase/Jordan theory are simply the coefficients of the logarithmic Jacobian potential of the inverse formal phase.

This compresses the previous diagonalization theorem into one exact identity.

---

## 11. Structural synthesis

The new hierarchy is

```text
finite integer recurrence
  -> integer decimation polynomial R_M
  -> derivative R_M' = M^2 H_M
  -> Dirichlet spectrum = critical set of R_M
  -> parity = critical-value split {0,4}
  -> common formal phase ell
  -> inverse U with exact self-similarity U(M^2 t)=R_M(U(t))
  -> finite determinant = Jacobian ratio U'(M^2t)/U'(t)
  -> dyadic equation uniquely forces factorial completion coefficients
  -> internal S,C reconstructed from U
  -> tau and Euler/Wallis completion arise later from the same reconstructed function
```

Freeze at free-research strength:

`DIRICHLET_FINITE_DETERMINANT = NORMALIZED_DECIMATION_JACOBIAN`.

`DIRICHLET_SPECTRUM = DECIMATION_CRITICAL_SET`.

`PARITY_SECTORS = TWO_CRITICAL_VALUE_FIBERS`.

`INTERNAL_SINE_COMPLETION = UNIQUE_FORMAL_DYADIC_DECIMATION_COMPLETION`.

`FORMAL_PHASE_INVERSE_JACOBIAN = MASTER_SPECTRAL_COMPLETION_FUNCTION`.
