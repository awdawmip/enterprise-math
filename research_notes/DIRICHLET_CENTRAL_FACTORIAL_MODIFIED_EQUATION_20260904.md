# Central-factorial modified-equation hierarchy for the finite Dirichlet sine carrier

Status: `FREE_RESEARCH / ALL-ORDER COEFFICIENT STRUCTURE / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`

## 1. Exact coefficient deformation

The exact finite carrier is

\[
F_M(x)=
\sum_{j=0}^{M-1}
\frac{(-1)^jx^{2j}}{(2j+1)!}
\prod_{r=1}^{j}
\left(1-\frac{r^2}{M^2}\right).
\]

Let

\[
e_s^{(j)}:=e_s(1^2,2^2,\ldots,j^2)
\]

be the `s`-th elementary symmetric polynomial of the first `j` squares, with

\[
e_0^{(j)}=1,
\qquad
e_s^{(j)}=0\quad(s>j).
\]

Then exactly

\[
\boxed{
\prod_{r=1}^{j}
\left(1-\frac{r^2}{M^2}\right)
=
\sum_{s=0}^{j}
\frac{(-1)^s e_s^{(j)}}{M^{2s}}.
}
\tag{CFM-1}
\]

Thus the finite carrier has an exact all-order even inverse-scale decomposition.

## 2. Universal central-factorial polynomials

For fixed `s`, the integer-valued function

\[
j\mapsto e_s^{(j)}
\]

extends to a polynomial `P_s(j)` of degree `3s`.

The recurrence is

\[
\boxed{
P_s(j)=P_s(j-1)+j^2P_{s-1}(j-1),
}
\tag{CFM-2}
\]

with `P_0=1` and `P_s(j)=0` for the integer nodes `j=0,...,s-1`.

The leading coefficient is

\[
\boxed{
P_s(j)
=
\frac{j^{3s}}{3^s s!}+O(j^{3s-1}).
}
\tag{CFM-3}
\]

The first polynomials are

\[
\boxed{
P_1(j)
=\frac{j(j+1)(2j+1)}6,
}
\tag{CFM-4}
\]

\[
\boxed{
P_2(j)
=\frac{
 j(j-1)(j+1)(2j-1)(2j+1)(5j+6)
}{360},
}
\tag{CFM-5}
\]

and

\[
\boxed{
P_3(j)
=
\frac{
 j(j-1)(j-2)(j+1)
 (2j-1)(2j-3)(2j+1)
 (35j^2+91j+60)
}{45360}.
}
\tag{CFM-6}
\]

These are the square-elementary central-factorial deformation polynomials underlying the finite determinant coefficients.

## 3. Diagonal differential operator

Define the Euler half-degree operator

\[
\boxed{
\Theta:=\frac{x}{2}\frac{d}{dx}.
}
\]

On even monomials,

\[
\Theta x^{2j}=j x^{2j}.
\]

Let the internal completion truncation be

\[
F_{<M}(x)
:=
\sum_{j=0}^{M-1}
\frac{(-1)^jx^{2j}}{(2j+1)!}.
\]

Because `P_s(j)=0` for `j<s`, equation (CFM-1) may be rearranged exactly as

\[
\boxed{
F_M(x)
=
\sum_{s=0}^{M-1}
\frac{(-1)^s}{M^{2s}}
P_s(\Theta)F_{<M}(x).
}
\tag{CFM-7}
\]

This is an exact finite modified-equation decomposition, not merely an asymptotic statement.

## 4. Completion-level asymptotic operator hierarchy

Let

\[
F(x)=\frac{S(x)}x
=
\sum_{j\ge0}\frac{(-1)^jx^{2j}}{(2j+1)!},
\qquad F(0):=1.
\]

For each fixed order `N` and compact radius `R`, factorial domination permits replacement of `F_<M` by `F` in the first `N` operator terms, while the remaining coefficient deformation starts at `M^(-2N-2)`.

Thus

\[
\boxed{
F_M(x)
\sim
\sum_{s=0}^{\infty}
\frac{(-1)^s}{M^{2s}}
P_s(\Theta)F(x)
}
\tag{CFM-8}
\]

locally uniformly in the asymptotic sense: after truncating at `s=N`, the remainder is `O_R(M^(-2N-2))` plus a factorially small finite-series cutoff term.

This is the all-order structural refinement of WSR-T02.

## 5. First true correction function

From (CFM-4),

\[
P_1(\Theta)
=\frac{\Theta(\Theta+1)(2\Theta+1)}6.
\]

Using

\[
F=S/x,
\qquad S'=C,
\]

a direct calculation gives

\[
\boxed{
-P_1(\Theta)F(x)
=
\frac{x^2C(x)+3xS(x)}{24}.
}
\tag{CFM-9}
\]

Therefore

\[
\boxed{
M^2(F_M(x)-F(x))
\longrightarrow
\frac{x^2C(x)+3xS(x)}{24}
}
\tag{CFM-10}
\]

locally uniformly.

This identifies the sign and shape of the actual leading discretization error, not just a majorant.

## 6. Why WSR-T02 has cosh/sinh

Taking absolute values termwise in the first correction replaces the alternating weights by positive ones.  The resulting exponential generating sum is

\[
\sum_{j\ge0}
\frac{j(j+1)(2j+1)R^{2j}}{(2j+1)!}
=
\frac{R^2\cosh R+3R\sinh R}{4}.
\]

After the factor `1/6` from `P_1`, this is exactly the WSR-T02 main majorant

\[
\boxed{
\frac{R^2\cosh R+3R\sinh R}{24M^2}.
}
\]

Thus the T02 hyperbolic expression is the absolute-coefficient envelope of the true internal correction (CFM-9).

## 7. Second correction function

From (CFM-5),

\[
P_2(\Theta)F
\]

simplifies under `S'=C`, `C'=-S` to

\[
\boxed{
P_2(\Theta)F(x)
=
\frac{x^3
\left[-5x^2S(x)+57xC(x)+135S(x)\right]}
{5760}.
}
\tag{CFM-11}
\]

Hence the first two completion corrections are

\[
F_M-F
=
\frac{x^2C+3xS}{24M^2}
+
\frac{x^3[-5x^2S+57xC+135S]}{5760M^4}
+O_R(M^{-6}).
\tag{CFM-12}
\]

The signs here are determined by the differential correction functions and need not be globally constant in `x`; the coefficient-level structure is exact regardless.

## 8. Why dyadic annihilation works

Under dyadic refinement `M->2M`, every universal correction mode scales as

\[
M^{-2s}\mapsto4^{-s}M^{-2s}.
\]

Therefore the annihilation filter

\[
\mathcal A_m
=
\prod_{r=1}^{m}\frac{4^r\mathcal E-I}{4^r-1}
\]

kills the first `m` operator corrections in (CFM-8) exactly:

\[
P_1(\Theta)F,
\ldots,
P_m(\Theta)F.
\]

So the arbitrary-order dyadic hierarchy is not an empirical Richardson trick. It is the exact spectral filter associated with the central-factorial modified-equation modes of the finite determinant.

Freeze:

`CENTRAL_FACTORIAL_COEFFICIENTS -> UNIVERSAL_M^-2s_CORRECTION_OPERATORS`.

`WSR_T02_MAJORANT = ABSOLUTE_ENVELOPE_OF_FIRST_TRUE_CORRECTION`.

`DYADIC_ANNIHILATION = EXACT_FILTER_OF_MODIFIED_EQUATION_MODES`.
