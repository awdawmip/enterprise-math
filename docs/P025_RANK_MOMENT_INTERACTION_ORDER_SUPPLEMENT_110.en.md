# P025 Supplement 110 — Exact Interaction Order for Arbitrary Rank Moments

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-nonlinear-observable-stage107`  
Depends on: P025 Supplements 108–109  
Hard block: `NONE`

## 1. Keep the operation algebra fixed

The primitive actions remain exactly the same:

- select candidate threshold rows;
- select/append future node columns.

The common labelled merged-rank path from Stage109 also remains unchanged.

Only the observable varies.

For integer degree

\[
d\ge1,
\]

define the rank moment

\[
\boxed{
M_d:=\sum_jr_j^d.
}
\]

Stage110 determines its exact worst-case action-interaction order.

## 2. P025-T251 — upper bound `d+1`

For an old node `c`, its selected rank has the form

\[
r_c+\sum_i x_i a_{ic},
\]

so its contribution

\[
\left(r_c+\sum_i x_i a_{ic}\right)^d
\]

is a Boolean polynomial of degree at most `d` in the candidate-threshold variables.

For a future node `j`, the contribution is gated by its future-column selection bit:

\[
y_j\left(R_j+\sum_i x_iC_{ij}\right)^d.
\]

The inner rank polynomial has degree at most `d`, so multiplication by `y_j` raises total degree by at most one.

Summing over nodes gives

\[
\boxed{
\deg M_d(x,y)\le d+1.
}
\]

Therefore every irreducible Boolean finite difference of order `d+2` or higher vanishes.

## 3. P025-CE44 — one arithmetic edge realizes every finite degree

Use the exact P025 dyadic edge

\[
\rho_0=\frac1{22},
\qquad
\rho_1=\frac{13}{22}
\]

from `(q,p,m)=(3,41,2)`.

For any fixed `d>=1`, choose `d` distinct rational thresholds

\[
\rho_0<U_1<\cdots<U_d<\rho_1.
\]

No old thresholds are needed.

The old node lies below every candidate threshold, while the future node lies above all of them. Hence, on the selected variables `x_1,...,x_d,y`, the entire nonzero moment response is

\[
\boxed{
M_d(x_1,\ldots,x_d,y)
=
y(x_1+\cdots+x_d)^d.
}
\]

## 4. P025-T252 — top coefficient is `d!`

Take the mixed Boolean finite difference in all `d` threshold variables and the future selector `y`.

The `y` difference removes the outer gate and leaves the `d`-fold difference of

\[
(x_1+\cdots+x_d)^d.
\]

The coefficient of the squarefree monomial

\[
x_1x_2\cdots x_d
\]

is the number of permutations assigning the `d` factors to all `d` distinct variables, namely

\[
\boxed{d!}.
\]

Therefore

\[
\boxed{
\Delta_{x_1}\cdots\Delta_{x_d}\Delta_yM_d=d!\ne0.
}
\]

So interaction order `d+1` is actually attained.

## 5. P025-T253 — exact worst-case order

Combining P025-T251 and P025-T252:

\[
\boxed{
\operatorname{ord}(M_d)=d+1
}
\]

in the worst case.

The first two cases recover earlier stages:

- `d=1`: activation area, exact order `2`;
- `d=2`: quadratic rank energy, exact order `3`.

The executable layer verifies the top coefficient for `d=1,...,5` and verifies vanishing one order above the bound.

## 6. Unbounded response order under a fixed operation algebra

The operation language and common incidence generator are fixed while `d` varies.

Since

\[
\operatorname{ord}(M_d)=d+1,
\]

we obtain

\[
\boxed{
\sup_d\operatorname{ord}(M_d)=\infty.
}
\]

Thus there is no universal finite response-jet order determined by this operation algebra alone.

Any architecture that hard-codes a fixed finite interaction order independently of the declared observable family will eventually lose future distinctions.

## 7. Generator complexity remains fixed in kind

Despite arbitrarily high response order, the Stage109 primitive incidence state remains one monotone merged-rank path.

The same path reconstructs every selected rank `r_j`, after which any declared moment `r_j^d` is evaluated locally.

Hence

\[
\boxed{
\text{unbounded derived response order}
\not\Rightarrow
\text{unbounded primitive generator order}.
}
\]

The generator grows only with the declared threshold/node geometry, not with the algebraic degree of the observable.

## 8. Architectural consequence

Stage110 identifies three independent precision axes:

1. **generator geometry** — the common merged-rank path;
2. **observable algebra** — here the moment degree `d`;
3. **operation/trace semantics** — which action words and observations are declared.

The required response jet is a derived consequence of all three, not a primitive state type.

## 9. Prior-art / novelty boundary

Finite differences of powers, the coefficient `d!`, and polynomial-degree bounds are classical algebra/combinatorics. P025 claims none individually.

The project-side result is the exact arithmetic pressure-test family showing unbounded response-jet order under one fixed operation algebra and one fixed kind of incidence generator. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 10. Executable assets

Added:

- `src/enterprise_math/abc_rank_moment_closure.py`;
- `tests/test_abc_rank_moment_closure.py`.

## 11. Next frontier

Stage111 should replace monomials `r^d` by an arbitrary polynomial observable `P(r)` and determine whether the exact interaction order is `deg(P)+1` whenever the leading coefficient is nonzero and the geometry supplies enough unresolved candidate thresholds.