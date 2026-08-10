# P025 Supplement 65 — Derivative-Mass Triangle Law for Projective Orientation

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-paired-square-tail-stage61`  
Depends on: P025 Supplement 47  
Hard block: `NONE`

## 1. The projective maximum has an exact orientation selector

For a positive integer define the raw derivative mass

\[
\boxed{
U(n)=nS(n)
=
\sum_{p\mid n}v_p(n)\frac np.
}
\]

Set `U(1)=0`.

The three P025 projective terms are

\[
\rho_c=\frac{c}{R(S(a)+S(b))},
\quad
\rho_b=\frac{b}{R(S(a)+S(c))},
\quad
\rho_a=\frac{a}{R(S(b)+S(c))}.
\]

The value of `sigma_proj` requires the weighted-radical data, but the identity of its maximizing orientation is much cheaper.

## 2. P025-T131 — comparison with `c` is a triangle inequality in `U`

Cross-multiplying positive denominators and using `c=a+b` gives

\[
\rho_c\ge\rho_b
\iff
c(S(a)+S(c))\ge b(S(a)+S(b))
\]

\[
\iff
\boxed{U(a)+U(c)\ge U(b).}
\]

Similarly,

\[
\boxed{
\rho_c\ge\rho_a
\iff
U(b)+U(c)\ge U(a).
}
\]

Thus the two comparisons needed to decide whether `c` dominates are exactly two triangle inequalities among integer derivative masses.

## 3. P025-T132 — complete orientation classification

Define side triangle defects

\[
D_a=U(a)-U(b)-U(c),
\qquad
D_b=U(b)-U(a)-U(c).
\]

They cannot both be positive.

The complete projective orientation law is:

\[
\boxed{
D_a>0
\Longrightarrow
\rho_a>\rho_c\ge\rho_b,
}
\]

\[
\boxed{
D_b>0
\Longrightarrow
\rho_b>\rho_c\ge\rho_a,
}
\]

and otherwise

\[
\boxed{
\rho_c\ge\rho_a,\rho_b.
}
\]

Equality `D_a=0` or `D_b=0` gives the corresponding exact tie with the c-oriented term.

Therefore a side component can become the unique projective maximizer **only by becoming superdominant in raw derivative mass**.

## 4. Small exact examples

### `1+30=31`

Here

\[
U(1)=0,\qquad U(30)=31,\qquad U(31)=1.
\]

Thus

\[
U(30)>U(1)+U(31),
\]

and the `b` orientation is the unique projective maximum. This example also shows that side superdominance does not by itself imply repeated prime factors: `30` is squarefree.

### `1+2=3`

\[
(U(a),U(b),U(c))=(0,1,1).
\]

So `D_b=0` and the `b` and `c` projective terms tie exactly.

## 5. Classical high-quality calibration

For

\[
2+3^{10}\cdot109=23^5,
\]

one has

\[
U(2)=1,
\]

\[
U(3^{10}\cdot109)
=21\,513\,519,
\]

and

\[
U(23^5)=1\,399\,205.
\]

Hence

\[
U(b)>U(a)+U(c),
\]

so the `b`-oriented term must be the projective maximum before any witness computation is attempted.

This identifies the orientation of the hard classical example as a block-arithmetic mass phenomenon, not a fine-lattice search artefact.

## 6. Hard unit calibration

For

\[
1+239^2=2\cdot13^4,
\]

the side is not derivative-mass superdominant, and the c-oriented term wins. This matches the Stage-51 interpretation: projective pressure comes from the large residual of `c` divided by the very small prime-square capacity of its neighbor.

## 7. Precision interpretation

The full scalar `sigma_proj` is already a coarse quotient of the fine witness system. P025-T131–T132 expose an even coarser future state for the query

> which cyclic term attains the projective maximum?

That selector needs only the signs of two integer triangle defects

\[
(D_a,D_b).
\]

It does not need radicals, exact support loads, witnesses, or the projective value itself.

Thus even inside one explicit observable, different future queries induce further exact quotient layers.

## 8. Prior-art / novelty discipline

The proof is elementary cross-multiplication. No general triangle-inequality or selector mathematics is claimed as new.

The project-specific result is the exact identification of the P025 projective orientation with superdominance in the arithmetic-derivative mass `U(n)`. Historical novelty is `NOVELTY_UNVERIFIED`.

## 9. Executable assets

Added:

- `src/enterprise_math/abc_projective_orientation.py`;
- `tests/test_abc_projective_orientation.py`.

The implementation cross-checks the triangle-defect classifier against the independently computed exact cyclic projective values.

## 10. Next frontier

No hard block exists. Continue with:

1. separate the tail of c-oriented failures from side-superdominant failures;
2. test whether high-threshold side superdominance has an additional arithmetic sparsity mechanism;
3. express the derivative-mass selector in exponent-layer/anatomic coordinates used by classical exceptional-set work;
4. add this selector as another node in the P025 task-relative quotient poset rather than forcing all precision observables onto one scalar axis.
