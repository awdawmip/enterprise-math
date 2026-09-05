# BRC rational rotation formal group and the primitive spectral division polynomials

Status: `FREE_RESEARCH / EXACT CROSS-LINE ALGEBRAIC SYNTHESIS / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Primary issue: `#1159`
Cross-line target: BRC coordinate-to-algebra program.

## 1. Oriented rational rotation law

In the declared quadratic rotation sector, use the affine BRC chart

\[
z=b/a
\]

with serial composition

\[
\boxed{
z\oplus w=\frac{z+w}{1-zw}.}
\tag{DP-1}
\]

The homogeneous pair `(a,b)` remains the global object; the affine pole `1-zw=0` is only a chart boundary.

---

## 2. Exact integer multiplication polynomials

Write

\[
(1+Jz)^n=A_n(z^2)+Jz\,B_n(z^2),
\qquad J^2=-1.
\]

Then

\[
\boxed{
A_n(y)=
\sum_{j\ge0}(-1)^j\binom{n}{2j}y^j,
}
\tag{DP-2}
\]

and

\[
\boxed{
B_n(y)=
\sum_{j\ge0}(-1)^j\binom{n}{2j+1}y^j.
}
\tag{DP-3}
\]

Only terms with admissible binomial indices occur.

The `n`-fold formal-group multiple is therefore

\[
\boxed{
[n]z
=z\frac{B_n(z^2)}{A_n(z^2)}.
}
\tag{DP-4}

Everything here lies in `Z[z]` before the final rational quotient.

---

## 3. Norm identity

The quadratic norm gives

\[
(1+Jz)^n(1-Jz)^n=(1+z^2)^n.
\]

Hence

\[
\boxed{
A_n(y)^2+yB_n(y)^2=(1+y)^n.
}
\tag{DP-5}

This is the homogeneous identity controlling the two projective coordinate charts.

---

## 4. Projective spectral quotient recovers `R_n`

Set

\[
\boxed{
u=\frac{4y}{1+y},
\qquad y=z^2.}
\tag{DP-6}

The projective coordinate of `[n]z` is

\[
\frac{4([n]z)^2}{1+([n]z)^2}.
\]

Using (DP-4)-(DP-5),

\[
\boxed{
R_n\!\left(\frac{4y}{1+y}\right)
=
\frac{4yB_n(y)^2}{(1+y)^n}.
}
\tag{DP-7}

Likewise

\[
\boxed{
4-R_n\!\left(\frac{4y}{1+y}\right)
=
\frac{4A_n(y)^2}{(1+y)^n}.
}
\tag{DP-8}

Thus the two critical-value square factorizations of the spectral decimation map are the projective images of the two homogeneous coordinates of the BRC rotation multiple.

This is an exact rational semiconjugacy, not a trigonometric readout.

---

## 5. Division points

A finite affine point satisfies

\[
[n]z=0
\]

iff

\[
z=0
\quad\text{or}\quad
B_n(z^2)=0.
\]

Therefore `B_n(y)` is the nonzero affine `n`-division polynomial in the squared oriented coordinate.

Its degree is

\[
\deg B_n=\left\lfloor\frac{n-1}{2}\right\rfloor.
\]

For even `n`, one additional projective `n`-division point lies at the affine point at infinity; the homogeneous formulation retains it automatically.

---

## 6. Primitive projective division factors

For `d>2`, let

\[
h_d=\varphi(d)/2.
\]

Define the projective primitive division polynomial in the squared oriented coordinate by the Möbius transform

\[
\boxed{
\Theta_d(y)
:=(1+y)^{h_d}
\Omega_d\!\left(\frac{4y}{1+y}\right).
}
\tag{DP-9}

Because `Omega_d` has degree `h_d`, the denominator cancels and

\[
\Theta_d(y)\in\mathbf Z[y].
\]

The map `y -> 4y/(1+y)` is birational, so irreducibility of `Omega_d` implies

\[
\boxed{
\Theta_d\text{ is irreducible over }\mathbf Q.
}
\tag{DP-10}

The roots of `Theta_d` are exactly the primitive projective `d`-division points in the `y=z^2` chart.

Examples:

```text
Theta_3 = y - 3
Theta_4 = 2(y - 1)
Theta_5 = y^2 - 10y + 5
Theta_6 = 3y - 1
Theta_7 = y^3 - 21y^2 + 35y - 7
Theta_8 = 2(y^2 - 6y + 1)
Theta_9 = y^3 - 33y^2 + 27y - 3
```

Scalar content is retained here because `Theta_d` is a division polynomial, not normalized to be monic.

---

## 7. Exact division-polynomial factorization

The nonzero division points of level `n` split uniquely by their primitive denominator.  Therefore, up to the leading sign,

\[
\boxed{
B_n(y)
=
\epsilon_n c_n
\prod_{\substack{d\mid n\\d>2}}
\Theta_d(y),
\qquad \epsilon_n\in\{\pm1\},
}
\tag{DP-11}

where the scalar magnitude is

\[
\boxed{
c_n=
\begin{cases}
1,&n\text{ odd},\\
2,&n\text{ even}.
\end{cases}}
\tag{DP-12}

The degree check is exact:

- for odd `n`,
  `sum_(d|n,d>1) phi(d)/2=(n-1)/2`;
- for even `n`, excluding `d=1,2` gives
  `sum_(d|n,d>2) phi(d)/2=(n-2)/2=deg B_n`.

The constant-term magnitude also matches:

\[
B_n(0)=n,
\]

while the product of primitive projective masses over `d|n,d>2` is `n` for odd `n` and `n/2` for even `n`.

Thus (DP-11) is fixed up to the easily computable global leading sign.

---

## 8. Prime division polynomial and Eisenstein

For an odd prime `p`, there is only one primitive denominator above the nonzero affine `p`-division set, so

\[
B_p(y)=\pm\Theta_p(y).
\]

From the binomial formula (DP-3), all nonleading coefficients are divisible by `p`, while the constant coefficient is `p` and the leading coefficient is `±1`.

Thus `Theta_p`, equivalently `Omega_p`, is `p`-Eisenstein directly from the BRC division polynomial.

This recovers the prime case of the spectral Eisenstein theorem without any spectral discriminant calculation.

---

## 9. Primitive spectral factors are formal-group division polynomials

Combining (DP-6) and (DP-9), one obtains the exact dictionary:

```text
oriented homogeneous BRC rotation state [a:b]
  -> affine z=b/a
  -> squared oriented coordinate y=z^2
  -> primitive division polynomial Theta_d(y)
  -> projective trace coordinate u=4y/(1+y)
  -> primitive spectral factor Omega_d(u)
```

Hence `Omega_d` is not merely cyclotomic-like after classical identification.  It is natively the primitive projective division polynomial of the rational BRC rotation formal group.

The later root-of-unity/cyclotomic description is a compatibility image of this algebraic division structure.

---

## 10. Root-block compiler consequence

For a BRC Schur-reduced module known to lie in the rational rotation sector, primitive repetition singularities can be compiled in either coordinate:

- `Theta_d(y)` if the squared oriented chart is retained;
- `Omega_d(u)` if only the projective trace defect is observable.

Both are exact irreducible primitive root blocks, related by the birational substitution (DP-9).

This gives a root-block construction based only on:

- integer binomial coefficients;
- divisor/Möbius splitting;
- a rational change of coordinate.

No numerical root finding is required.

Freeze at free-research strength:

`OMEGA_d = PRIMITIVE_PROJECTIVE_DIVISION_POLYNOMIAL_OF_THE_BRC_ROTATION_FORMAL_GROUP`.

`R_n = PROJECTIVE_IMAGE_OF_THE_INTEGER_MULTIPLICATION_MAP_[n]`.

`BRC_BINOMIAL_DIVISION_POLYNOMIALS -> SPECTRAL_PRIMITIVE_ROOT_BLOCKS`.
