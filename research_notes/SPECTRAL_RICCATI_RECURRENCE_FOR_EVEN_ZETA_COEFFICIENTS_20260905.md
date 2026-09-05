# Spectral Riccati recurrence for all even-zeta rational coefficients

Status: `FREE_RESEARCH / EXACT FORMAL-ARITHMETIC THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`

## 1. The inverse formal phase obeys a linear ODE

The inverse common formal phase is

\[
U(t)=2\sum_{n\ge1}\frac{(-1)^{n+1}t^n}{(2n)!}.
\]

The coefficient recurrence forced by dyadic decimation is equivalent to

\[
\boxed{
4tU''(t)+2U'(t)+U(t)=2.
}
\tag{ZR-1}
\]

Differentiate once and set

\[
F(t):=U'(t).
\]

Then

\[
\boxed{
4tF''(t)+6F'(t)+F(t)=0,
\qquad F(0)=1.
}
\tag{ZR-2}
\]

The internal completion satisfies

\[
F(x^2)=S(x)/x.
\]

---

## 2. Logarithmic Jacobian potential

Define

\[
\mathcal K(t):=-\log F(t)
=\sum_{n\ge1}\kappa_nt^n.
\]

Then

\[
F'/F=-\mathcal K',
\qquad
F''/F=(\mathcal K')^2-\mathcal K''.
\]

Divide (ZR-2) by `F`:

\[
\boxed{
4t\big((\mathcal K')^2-\mathcal K''\big)
-6\mathcal K'+1=0.
}
\tag{ZR-3}
\]

Equivalently,

\[
\boxed{
4t\mathcal K''+6\mathcal K'
=4t(\mathcal K')^2+1.
}
\tag{ZR-4}
\]

---

## 3. Universal rational recursion

Coefficient comparison gives

\[
\kappa_1=1/6,
\]

and for `n>=2`,

\[
\boxed{
\kappa_n
=
\frac{2}{n(2n+1)}
\sum_{j=1}^{n-1}
 j(n-j)\kappa_j\kappa_{n-j}.
}
\tag{ZR-5}
\]

Define the more natural diagonal coefficients

\[
\boxed{\beta_n:=n\kappa_n.}
\]

Then

\[
\boxed{
\beta_1=\frac16,
\qquad
\beta_n
=
\frac{2}{2n+1}
\sum_{j=1}^{n-1}
\beta_j\beta_{n-j}
\quad(n\ge2).
}
\tag{ZR-6}
\]

Thus all rational completion coefficients are generated internally from the single seed `1/6` by a quadratic convolution.

---

## 4. One generating-function equation

Let

\[
B(t):=t\mathcal K'(t)
=\sum_{n\ge1}\beta_nt^n.
\]

Then (ZR-4) is exactly

\[
\boxed{
4tB'(t)+2B(t)=4B(t)^2+t.
}
\tag{ZR-7}
\]

This is the master Riccati equation for the finite-spectral RG coefficients.

---

## 5. First coefficients

The recursion gives

\[
\boxed{
\beta_1=\frac16,
\quad
\beta_2=\frac1{90},
\quad
\beta_3=\frac1{945},
\quad
\beta_4=\frac1{9450},
\quad
\beta_5=\frac1{93555},
}
\]

and

\[
\boxed{
\beta_6=\frac{691}{638512875}.
}
\tag{ZR-8}
\]

The numerator `691` therefore appears directly as a sixth-order coefficient of the finite spectral logarithmic-Jacobian recursion; it need not be imported from a Bernoulli-number table.

---

## 6. Even zeta values

The finite spectral moment limit already gives

\[
\boxed{
\zeta(2n)=\beta_n\tau^{2n}.
}
\tag{ZR-9}
\]

Therefore (ZR-6) induces the normalized Euler convolution

\[
\boxed{
\frac{\zeta(2n)}{\tau^{2n}}
=
\frac{2}{2n+1}
\sum_{j=1}^{n-1}
\frac{\zeta(2j)}{\tau^{2j}}
\frac{\zeta(2n-2j)}{\tau^{2n-2j}}.
}
\tag{ZR-10}
\]

Equivalently, after canceling the common power of `tau`,

\[
\boxed{
(2n+1)\zeta(2n)
=2\sum_{j=1}^{n-1}
\zeta(2j)\zeta(2n-2j)
}
\tag{ZR-11}
\]

for `n>=2`.

This classical-looking identity is here obtained from the finite decimation/Jacobian ODE.

---

## 7. Later Bernoulli compatibility

Only after the native recursion is established, one may identify

\[
\boxed{
\beta_n
=(-1)^{n+1}
\frac{2^{2n-1}B_{2n}}{(2n)!}.
}
\tag{ZR-12}
\]

Then (ZR-9) becomes the usual Bernoulli formula for even zeta values after the later classical naming `tau=pi`.

But the project can instead regard `(beta_n)` as a finite-spectral sequence defined by (ZR-6).  Bernoulli numbers are a compatibility image, not required input.

---

## 8. Arithmetic research direction

The numerators of `beta_n` contain the same irregular-prime information that later appears in Bernoulli numerators.  The spectral formulation therefore gives a new internal question:

> Can the `p`-adic valuation pattern of `beta_n` be read directly from finite primitive spectral factors, denominator Frobenius, or BRC transfer arithmetic, without first importing Bernoulli theory?

No answer is claimed yet.  This is a genuine next research direction suggested by the finite RG formulation.

Freeze:

`EVEN_ZETA_COEFFICIENT_SEQUENCE = UNIQUE_SPECTRAL_RICCATI_SEQUENCE`.

`BERNOULLI_COMPATIBILITY = LATER IDENTIFICATION`.
