# Free Research — C3 Cayley Prime-Balance Function V23

Status: `FREE_RESEARCH_FRONTIER / ABSOLUTELY CONVERGENT PRIME PRODUCT FOR s>1 / ABEL BOUNDARY VALUE FOUR / NATIVE TRACE LOCAL FACTORS / NOT WORKING TRUTH / NOT FOUNDATION / EXTERNAL NOVELTY NOT CLAIMED`
Date: `2026-09-05`
Project: `Enterprise Math / 进取数论`
Researcher-ID: `EM-FREE-PI-PRIME-20260905`
Parents:
- `FREE_RESEARCH_PI_PRIME_CRITICAL_CURRENT_C3_BALANCE_V23_20260905.md`;
- `FREE_RESEARCH_PI_PRIME_NATIVE_C3_CHIRAL_TRACE_20260904.md`;
- `FREE_RESEARCH_WALLIS_CAUCHY_INTERNAL_COMPLETION_20260904.md`.

## 1. Why regularize the weight-one prime product

The direct Euler product for `L(1,chi_3)` is a boundary/conditional object.  The geometric local factors are correct, but using the raw weight-one prime product as the primary global definition obscures the convergence type.

There is a cleaner one-parameter object.  For every real `s>1`, define

\[
\boxed{
\mathcal C_3(s)
:=\prod_{p\ne3}
\frac{p^s-\chi_3(p)}{p^s+\chi_3(p)}.}
\tag{1.1}
\]

Since

\[
\log\frac{1-x}{1+x}=-2x+O(x^3)
\]

and `sum_p p^{-s}<infinity` for `s>1`, the product is absolutely convergent for every `s>1`.

Thus `C_3(s)` is an ordinary positive prime product in the open stable half-line; no conditional rearrangement is involved.

---

## 2. Exact local factor identity

For `p!=3`, `chi_3(p)^2=1`.  Put `x=p^{-s}`. Then

\[
\frac{1-\chi_3(p)x}{1+\chi_3(p)x}
=\frac{(1-\chi_3(p)x)^2}{1-x^2}.
\tag{2.1}
\]

Therefore

\[
\boxed{
\frac{p^s-\chi_3(p)}{p^s+\chi_3(p)}
=\frac{(1-\chi_3(p)p^{-s})^2}{1-p^{-2s}}.}
\tag{2.2}
\]

This identity is purely local and algebraic.

---

## 3. Partition-ratio theorem

For `s>1`, absolute Euler products give

\[
L(s,\chi_3)^{-2}
=\prod_{p\ne3}(1-\chi_3(p)p^{-s})^2,
\]

while

\[
\prod_{p\ne3}(1-p^{-2s})^{-1}
=(1-3^{-2s})\,\zeta(2s).
\]

Combining with (2.2),

\[
\boxed{
\mathcal C_3(s)
=(1-3^{-2s})
\frac{\zeta(2s)}{L(s,\chi_3)^2}.}
\tag{3.1}
\]

In the internal prime-winding notation `Z(sigma)=prod_p(1-p^-sigma)^-1`,

\[
\boxed{
\mathcal C_3(s)
=(1-3^{-2s})
\frac{\mathcal Z(2s)}{L(s,\chi_3)^2}.}
\tag{3.2}
\]

This exhibits the balance function as a ratio of:

- an **untwisted magnitude partition** evaluated at double exponent `2s`;
- the square of the **C3 orientation partition** evaluated at exponent `s`;
- the single ramified local correction at `p=3`.

---

## 4. Abel boundary value at s=1

The internal quadratic birth completion gives

\[
\mathcal Z(2)=\tau^2/6.
\tag{4.1}
\]

The native projective/Wallis C3 completion gives

\[
L(1,\chi_3)=\mathcal O_3
=\tau R_{\rm cell}/3,
\qquad
R_{\rm cell}^2=1/3.
\tag{4.2}
\]

Both right-hand sides are finite and nonzero.  Therefore (3.2) has the boundary limit

\[
\begin{aligned}
\lim_{s\downarrow1}\mathcal C_3(s)
&=(1-3^{-2})
\frac{\tau^2/6}{(\tau R_{\rm cell}/3)^2}\\
&=\frac89\cdot\frac{9}{6R_{\rm cell}^2}\\
&=\frac89\cdot\frac92\\
&=4.
\end{aligned}
\]

Hence

\[
\boxed{
\lim_{s\downarrow1}
\prod_{p\ne3}
\frac{p^s-\chi_3(p)}{p^s+\chi_3(p)}
=4.}
\tag{4.3}
\]

This is an Abel-regularized version of the weight-one chiral prime balance. It avoids any need to treat the conditional `s=1` product as the primary object.

---

## 5. Native trace form

The current three-sector orientation theorem gives

\[
\chi_3(p)=\frac13\operatorname{Tr}(JP^p).
\]

Therefore, for every `s>1`,

\[
\boxed{
\mathcal C_3(s)
=\prod_{p\ne3}
\frac{3p^s-\operatorname{Tr}(JP^p)}
     {3p^s+\operatorname{Tr}(JP^p)}.}
\tag{5.1}
\]

and

\[
\boxed{
\lim_{s\downarrow1}
\prod_{p\ne3}
\frac{3p^s-\operatorname{Tr}(JP^p)}
     {3p^s+\operatorname{Tr}(JP^p)}
=4.}
\tag{5.2}
\]

Every local factor is now an explicit Cayley transform of the finite native chiral trace.

---

## 6. Why the exponent doubling is structural

The magnitude factor enters at `2s` because eliminating the sign of a C3 orientation factor uses

\[
(1-\chi x)(1+\chi x)=1-x^2
\qquad(\chi^2=1).
\]

Thus squaring the orientation response naturally produces the orientation-blind quadratic magnitude factor.  The appearance of exponents `s` and `2s` is not inserted to fit the known value of `tau`; it is already present in the local algebra (2.2).

At the boundary `s=1`, the two observers land exactly on the two project completion orders already discovered independently:

\[
\boxed{
\text{C3 orientation at order }1
\quad\leftrightarrow\quad
\text{universal magnitude at order }2.}
\tag{6.1}
\]

This explains more sharply why the same `tau` appears in both channels.

---

## 7. Relation to the projective radius

The value `L(1,chi_3)=tau R_cell/3` is not being imported from a classical circle formula.  The existing projective-radius and Wallis--Cauchy notes derive it through:

1. the native radius equation `3 R_cell^2=1`;
2. the radius-selected projective order-three orbit;
3. three equal invariant Cauchy/Wallis completion cells;
4. the target-free Wallis squeeze identifying the Cauchy completion with the internal `wallisLimit`.

The only remaining standard multiplicative input in (3.1) is the absolutely convergent Euler product for `s>1`; the boundary value is then taken after the exact partition ratio is formed.

---

## 8. Geometric reading

The function `C_3(s)` compares, prime by prime, the two orientations of the native order-three phase while dividing out the corresponding orientation-blind quadratic magnitude.

Thus the boundary constant `4` is best typed as

\[
\boxed{
\text{C3 Cayley polarization balance of prime births at the critical boundary}.}
\]

No native meaning of the number `4` beyond this exact balance is asserted yet.  In particular, it is not identified with a spatial axis count, a dimension, or a cell multiplicity without a separate theorem.

---

## 9. Classification

Proved exactly for `s>1`:

- absolute convergence of `C_3(s)`;
- local Cayley factor identity;
- partition ratio `(3.1)--(3.2)`;
- native trace form `(5.1)`.

Closed at existing internal completion strength:

- Abel boundary value `lim_(s downarrow 1) C_3(s)=4`.

Not required for the theorem:

- ordinary convergence of the unregularized prime product at `s=1`;
- PNT in arithmetic progressions;
- any zero-free-region estimate.

Open:

- a direct finite-cell/provenance interpretation of the resulting constant `4`;
- full P000 six-dimensional lift of the C3 polarization observer;
- external novelty classification.
