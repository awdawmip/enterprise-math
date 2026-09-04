# Exact physical-scale renormalization of the finite Dirichlet sine carrier

Status: `FREE_RESEARCH / EXACT FINITE RG + MODIFIED-EQUATION BRIDGE / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`

## 1. Physical spectral variable

Let

\[
\mathcal G_M(t)
:=
\frac1M
D_{M-1}\left(\frac{t}{M^2}\right).
\]

Then

\[
F_M(x)=\mathcal G_M(x^2).
\]

The exact spectral decimation law is

\[
D_{2q-1}(z)
=(2-z)D_{q-1}(z(4-z)).
\]

Set

\[
z=\frac{t}{4q^2}.
\]

Then

\[
2-z
=2\left(1-\frac{t}{8q^2}\right),
\]

and

\[
z(4-z)
=
\frac1{q^2}
\,t\left(1-\frac{t}{16q^2}\right).
\]

After dividing by `2q`, one obtains the exact finite renormalization equation

\[
\boxed{
\mathcal G_{2q}(t)
=
\left(1-\frac{t}{8q^2}\right)
\mathcal G_q\left(
 t\left(1-\frac{t}{16q^2}\right)
\right).
}
\tag{PSR-1}
\]

No analytic limit is used in (PSR-1).

## 2. Interpretation

The doubling refinement has two simultaneous finite effects:

1. an amplitude renormalization
   \[
   A_q(t)=1-\frac{t}{8q^2};
   \]
2. a nonlinear spectral-coordinate correction
   \[
   t\mapsto t\left(1-\frac{t}{16q^2}\right).
   \]

Thus the continuum sine carrier is approached by an exact discrete amplitude/coordinate RG, not merely coefficientwise convergence.

## 3. Formal correction hierarchy from the exact RG

Write a formal even inverse-scale expansion

\[
\mathcal G_q(t)
=
G(t)
+q^{-2}H_1(t)
+q^{-4}H_2(t)
+q^{-6}H_3(t)+\cdots.
\tag{PSR-2}
\]

Since `(2q)^(-2s)=4^(-s)q^(-2s)`, substitute (PSR-2) into (PSR-1) and compare powers of `q^-2`.

This recursively determines every `H_s` from the continuum profile `G` and the previous corrections.

## 4. First correction forced by RG

Let

\[
a(t):=\frac{t^2}{16}.
\]

At order `q^-2`, (PSR-1) gives

\[
\frac14H_1
=
H_1-aG'-\frac{t}{8}G.
\]

Therefore

\[
\boxed{
H_1(t)
=
\frac{t}{6}G(t)
+
\frac{t^2}{12}G'(t).
}
\tag{PSR-3}
\]

For the #1159 completion

\[
G(t)=F(\sqrt t)=\frac{S(\sqrt t)}{\sqrt t},
\]

this becomes, with `t=x^2`,

\[
\boxed{
H_1(x^2)
=
\frac{x^2C(x)+3xS(x)}{24}.
}
\tag{PSR-4}
\]

This is exactly the first central-factorial correction derived independently from the finite determinant coefficients.

## 5. Second correction forced by RG

At order `q^-4`, expanding the shifted arguments gives

\[
\frac1{16}H_2
=
H_2
-aH_1'
+\frac{a^2}{2}G''
-\frac{t}{8}H_1
+\frac{ta}{8}G'.
\]

Substituting (PSR-3) and simplifying yields

\[
\boxed{
H_2(t)
=
\frac{t^2}{30}G(t)
+
\frac{t^3}{40}G'(t)
+
\frac{t^4}{288}G''(t).
}
\tag{PSR-5}
\]

For `G=S(x)/x`, this is equivalent to the central-factorial expression

\[
\boxed{
H_2(x^2)
=
\frac{x^3[-5x^2S(x)+57xC(x)+135S(x)]}{5760}.
}
\tag{PSR-6}
\]

Thus two independent constructions produce the same correction hierarchy:

```text
finite central-factorial coefficient deformation
       \             /
        -> H_1,H_2,...
       /             \
exact finite spectral-decimation RG
```

## 6. All-order recursive structure

Let `epsilon=q^-2`.  Equation (PSR-1) can be written as

\[
\mathscr G(\epsilon/4,t)
=
\left(1-\frac{\epsilon t}{8}\right)
\mathscr G\left(
\epsilon,
 t-\frac{\epsilon t^2}{16}
\right).
\tag{PSR-7}
\]

For a formal series

\[
\mathscr G(\epsilon,t)=\sum_{s\ge0}\epsilon^sH_s(t),
\]

the coefficient of `epsilon^s` on the left is `4^-s H_s`; on the right it is a finite differential expression involving `H_0,...,H_s`.

Since

\[
1-4^{-s}\ne0
\qquad(s>=1),
\]

each correction `H_s` is uniquely determined recursively by `G=H_0`.

Thus the all-order modified equation is a formal consequence of exact finite decimation.

## 7. Relation to dyadic annihilation

The correction modes in (PSR-2) scale under `q->2q` by the exact eigenvalues

\[
4^{-s}.
\]

Therefore the dyadic annihilation filter

\[
\prod_{r=1}^{m}\frac{4^r\mathcal E-I}{4^r-1}
\]

is precisely the spectral projector that annihilates the first `m` RG correction eigendirections.

This gives a third equivalent interpretation of the same hierarchy:

1. central-factorial coefficient corrections;
2. formal eigendirections of the exact finite RG;
3. modes killed by the dyadic annihilation filter.

Freeze:

`EXACT_FINITE_DECIMATION -> PHYSICAL_SCALE_RG`.

`RG_CORRECTION_HIERARCHY = CENTRAL_FACTORIAL_MODIFIED_EQUATION`.

`DYADIC_ANNIHILATION = RG_ERROR_MODE_FILTER`.
