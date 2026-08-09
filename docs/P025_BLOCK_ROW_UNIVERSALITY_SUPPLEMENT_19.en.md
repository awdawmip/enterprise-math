# P025 Supplement 19 — Universality of Primitive Positive Arithmetic Block Rows

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-access-tail-stage18`  
Depends on: P025 Supplements 13, 16–18  
Hard block: `NONE`

## 1. The apparent escape route

Supplements 16–18 study signed access for an arbitrary primitive positive coefficient row

\[
b=(b_1,\ldots,b_d).
\]

One could hope that actual arithmetic-derivative blocks form a much smaller special subclass, making the generic numerical-semigroup / capacity-frontier complexity irrelevant to P025.

That hope is false.

The normalized coefficient rows produced by integer arithmetic derivatives are **exactly all primitive positive integer rows**.

## 2. Actual arithmetic block row

Let

\[
n=\prod_{i=1}^d p_i^{e_i}
\]

with distinct primes `p_i` and positive exponents `e_i`.

Write

\[
R=\operatorname{rad}(n)=\prod_i p_i.
\]

Supplement 13 showed that the normalized derivative

\[
\frac{d_x(n)}{m(n)}
\]

has coefficient at prime `p_i`

\[
\boxed{
c_i=e_i\frac{R}{p_i}.}
\]

Let

\[
h(n)=\gcd_i c_i.
\]

The corresponding primitive positive block row is

\[
\boxed{
b_i(n)=\frac{c_i}{h(n)}.}
\]

By construction

\[
\gcd_i b_i(n)=1.
\]

So every actual block row lies in the class of primitive positive integer rows.

## 3. P025-T56 — every primitive positive row is realized by an integer block

Conversely let

\[
\boxed{
b=(b_1,\ldots,b_d)\in\mathbb N_{>0}^d,
\qquad
\gcd(b_1,\ldots,b_d)=1.}
\]

Choose any distinct primes

\[
p_1<\cdots<p_d
\]

and define exponents

\[
\boxed{e_i=p_i b_i.}
\]

Set

\[
\boxed{
n_b=\prod_i p_i^{p_i b_i}.}
\]

Then the normalized derivative coefficient at `p_i` is

\[
e_i\frac{R}{p_i}
=
(p_i b_i)\frac{R}{p_i}
=
R b_i.
\]

Therefore the content of the whole coefficient row is

\[
\gcd_i(Rb_i)
=R\gcd_i b_i
=R.
\]

Dividing by the content gives exactly

\[
\boxed{
\left(
\frac{Rb_1}{R},\ldots,
\frac{Rb_d}{R}
\right)
=b.
}
\]

Hence every primitive positive integer row is the primitive arithmetic-derivative row of an explicit positive integer block. ∎

## 4. Exact row-class classification

Combining both directions:

\[
\boxed{
\{\text{primitive arithmetic block rows}\}
=
\{b\in\mathbb N_{>0}^d:\gcd(b_i)=1\}.
}
\]

This holds in every finite dimension `d>=1`.

The construction is intentionally existence-oriented; it does not claim the resulting integer `n_b` is smallest among realizations of the same row.

## 5. Concrete realizations of current pressure-test rows

### `(5,2)`

Choose prime labels `(2,3)`. Then

\[
e=(10,6),
\qquad
n=2^{10}3^6.
\]

The normalized derivative coefficients are

\[
(30,12)=6(5,2),
\]

so the primitive row is exactly `(5,2)`.

### `(15,10,6)`

Choose labels `(2,3,5)`. Then

\[
e=(30,30,30),
\]

and the primitive row is exactly `(15,10,6)`.

### Stage-17 equal-Apéry counterexample rows

Each of

\[
(2,4,5,11),
\quad
(2,5,7,8),
\quad
(2,5,6,9)
\]

is therefore an actual arithmetic block row, for example using prime labels `(2,3,5,7)` and exponents `p_i b_i`.

So the Stage-17 distinction between semigroup membership, labelled factorization geometry, and access precision is not an artifact of leaving the arithmetic-derivative domain.

## 6. P025-N08 — no hidden row-class simplification

A theorem that fails for some primitive positive row can be transported to an actual arithmetic block by the construction above.

Therefore no universal P025 argument may assume, merely because coefficients originate from prime valuations, that the primitive row satisfies an extra combinatorial property beyond positivity and gcd one.

In particular, one cannot hope to eliminate the following phenomena by saying “real arithmetic rows are more special”:

- nonminimal/redundant coefficient coordinates;
- equal generated semigroups with different labelled factorization geometry;
- nontrivial Apéry preperiods;
- multi-level capacity frontiers;
- arbitrary finite-dimensional positive-row access problems.

Any stronger simplification must use additional hypotheses about the **particular abc relation**, exponent pattern, support size, or declared future language.

## 7. Architectural consequence

This result sharpens the ownership boundary of Supplements 16–18.

The numerical-semigroup and `L_infinity` factorization mathematics remains prior art, but the generic positive-row access layer is not merely an external calibration universe. It is exactly the coefficient-row universe already embedded in arithmetic-derivative blocks.

Thus the pressure-test chain becomes

\[
\boxed{
\text{integer prime/exponent block}
\twoheadrightarrow
\text{arbitrary primitive positive row}
\to
\text{signed access / Apéry / capacity frontier}.
}
\]

The first map is surjective at the level of primitive coefficient rows.

## 8. Prior-art discipline

The construction `e_i=p_i b_i` and the gcd calculation are elementary arithmetic. P025 does not claim historical priority for the bare realization trick.

The project value is a negative-boundary conclusion for the research architecture: generic primitive-row access complexity genuinely belongs inside the arithmetic-derivative search space and cannot be dismissed as an over-generalization.

Historical novelty of that architectural use remains `NOVELTY_UNVERIFIED`.

## 9. Executable assets

Added:

- `src/enterprise_math/abc_block_row_universality.py`
  - primitive block-row extraction;
  - explicit realization `n_b=product p_i^(p_i b_i)`;
  - exact row reconstruction checks.
- `tests/test_abc_block_row_universality.py`
  - two-variable `(5,2)` realization;
  - Stage-17 four-coordinate rows;
  - three-coordinate `(15,10,6)` realization;
  - one-dimensional boundary;
  - rejection of nonprimitive or invalid prime-labelled inputs.

## 10. Next frontier

No hard block exists. Continue with:

1. use universality to transfer generic lower bounds/counterexamples directly into arithmetic blocks;
2. characterize the smallest exponent size needed to realize a given row, without confusing that separate optimization with access precision;
3. identify special abc relation constraints that genuinely reduce row-access complexity after this universality barrier;
4. test multi-block simultaneous certificate targets, where each block row is individually universal but relation coupling may impose new structure;
5. keep generic factorization theory as prior art while studying the project-specific future-language compression interfaces.
