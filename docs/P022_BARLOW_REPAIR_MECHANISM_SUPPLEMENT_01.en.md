# P022 — Both Repair Mechanisms Survive at Leading Square-Root Order

Status: `ACTIVE RESEARCH NOTE / ASYMPTOTIC TYPED REPAIR`  
Owner: `program/p022-geometry-v2`  
Depends on: bivariate repair-mechanism polynomial; microscopic-average repair complexity

## 1. Typed microscopic averages

Write

\[
\overline E_N
=
\frac1{4^N}\sum_{w\in\Omega_N}E(O(w))
\]

for the microscopic-weighted mean number of excursion-orientation bits, and

\[
\overline B_N
=
\frac1{4^N}\sum_{w\in\Omega_N}B(O(w))
\]

for the microscopic-weighted mean number of diagonal side-label bits.

The bivariate mechanism polynomial gives

\[
\boxed{
\overline E_N
=
\frac{2\partial_x\mathcal R_N(2,2)}{4^N},
\qquad
\overline B_N
=
\frac{2\partial_y\mathcal R_N(2,2)}{4^N}.
}
\]

The scalar mean repair is

\[
\overline r_N=\overline E_N+\overline B_N.
\]

---

## 2. P022-RM06 — orientation contribution

The one-sided excursion calculation gives

\[
A_N
=(2m+1)\frac{\binom{2m}{m}}{4^m},
\qquad
m=\left\lfloor\frac{N-1}{2}\right\rfloor.
\]

There are two labelled sides, so

\[
\overline E_N=2A_N.
\]

Using the standard central-binomial asymptotic,

\[
\boxed{
\overline E_N
=
2\sqrt{\frac{2N}{\pi}}
+O(N^{-1/2}).
}
\]

Thus zero-boundary orientation repair contributes a genuine square-root main term.

---

## 3. P022-RM07 — diagonal-split contribution

The exact split average is

\[
\overline B_N
=
\sum_{t=1}^{N-1}
\frac{
\binom{2t}{t}
-
\mathbf1_{2\mid t}\binom{t}{t/2}^2
}{4^t}.
\]

The uncorrected central-binomial partial sum contributes

\[
2\sqrt{\frac N\pi}+O(N^{-1/2}),
\]

while the simultaneous-zero correction satisfies

\[
\sum_{j\le(N-1)/2}
\frac{\binom{2j}{j}^2}{16^j}
=
\frac1\pi\log N+O(1).
\]

Therefore

\[
\boxed{
\overline B_N
=
2\sqrt{\frac N\pi}
-
\frac1\pi\log N
+O(1).
}
\]

The logarithmic correction belongs only to the side-split mechanism because simultaneous visits to zero remove would-be diagonal splits.

---

## 4. P022-RM08 — neither repair type is asymptotically negligible

The leading square-root coefficients satisfy

\[
\frac{\overline E_N}{\overline B_N}
\longrightarrow
\sqrt2.
\]

Equivalently, relative to the total square-root main term,

\[
\boxed{
\frac{\overline E_N}{\overline r_N}
\longrightarrow
\frac{\sqrt2}{\sqrt2+1}
=2-\sqrt2,
}
\]

and

\[
\boxed{
\frac{\overline B_N}{\overline r_N}
\longrightarrow
\frac1{\sqrt2+1}
=\sqrt2-1.
}
\]

So both repair mechanisms survive at leading order.  Scalarizing them into

\[
r=E+B
\]

cannot be justified by claiming that one mechanism becomes asymptotically negligible.

This strengthens the horizon-three mechanism-alias counterexample: the semantic distinction persists not only at small finite scale but in the leading microscopic-average repair budget.

---

## 5. Precision consequence

A future operation that needs only orientation repair and one that needs only side identity have asymptotically different but comparable state costs.

Therefore a generic precision layer should carry **typed repair coordinates** whenever the future language distinguishes them.  A scalar repair magnitude remains appropriate only for future tasks that genuinely factor through the sum `E+B`.

No universal two-type ratio is claimed outside the Barlow two-channel transition law.
