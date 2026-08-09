# P025 Supplement 15 — Unit-Relation Ideal Intersection and Blockwise Access

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner: `program/p025-abc-support-collapse`  
Depends on: P025 Supplements 13–14  
Hard block: `NONE`

## 1. A stronger decomposition for `1+b=c`

The relation

\[
\boxed{1+b=c}
\]

has a special simplification: the derivative of the unit is zero, so relation-adapted additivity is exactly

\[
\boxed{d_x(b)=d_x(c).}
\]

The Wronskian is also simply

\[
\boxed{W_x(1,b)=d_x(b).}
\]

Therefore both the arithmetic image problem and the floor-access problem can be decomposed **blockwise**, without first forming the global Wronskian-minor lattice.

## 2. P025-D05 — raw block derivative image generator

For `n>1`, define

\[
\boxed{
A(n)
=
\gcd_{p\mid n}
\frac{n v_p(n)}p.
}
\]

By P025-T37,

\[
\boxed{A(n)=m(n)h(n).}
\]

The raw derivative values of the block are exactly

\[
\boxed{
\{d_x(n):x\}
=A(n)\mathbb Z.
}
\]

So `A(n)` is the positive generator of the raw derivative image ideal.

## 3. P025-T42 — Wronskian image is an ideal intersection

Let

\[
A_b=A(b),
\qquad
A_c=A(c).
\]

In the unit relation, an additive witness must choose a derivative value lying in both image ideals:

\[
d_x(b)=d_x(c)
\in
A_b\mathbb Z\cap A_c\mathbb Z.
\]

For principal ideals in `Z`,

\[
A_b\mathbb Z\cap A_c\mathbb Z
=
\operatorname{lcm}(A_b,A_c)\mathbb Z.
\]

Hence the positive Wronskian image generator is

\[
\boxed{
D
=
\operatorname{lcm}(A_b,A_c).
}
\]

This gives an alternative exact derivation of the unit-relation absorption floor that never forms prime-pair minors.

## 4. P025-T43 — closed unit-relation floor formula

The residual product is

\[
M=m(b)m(c),
\]

so Pasten's residual divisibility implies `M|D`. Therefore

\[
\boxed{
\eta_{\min}(1,b,c)
=
\frac{\operatorname{lcm}(A(b),A(c))}
{m(b)m(c)}.
}
\]

Substituting `A(n)=m(n)h(n)` yields the equivalent form

\[
\boxed{
\eta_{\min}(1,b,c)
=
\frac{
\operatorname{lcm}(m_b h_b,m_c h_c)
}{m_bm_c}.
}
\]

This is the unit-block specialization of the general block formula from Supplement 13.

## 5. P025-D06 — block generator access radius

The image content `A(n)` answers **which values are attainable**, but not how large a prime-coordinate witness must be to attain one.

For any target

\[
T\in A(n)\mathbb Z,
\]

define

\[
\boxed{
\kappa_n(T)
=
\min\left\{
\|x\|_\infty:
\sum_{p\mid n}rac{n v_p(n)}p x_p=T
\right\}.
}
\]

This is the blockwise preimage-access cost of the raw derivative target.

For the image generator itself one may abbreviate

\[
\kappa(n)=\kappa_n(A(n)).
\]

The distinction

\[
A(n)
\quad\text{versus}\quad
\kappa_n(T)
\]

is the block-level analogue of the global distinction

\[
\eta_{\min}
\quad\text{versus}\quad
\nu.
\]

## 6. P025-T44 — exact blockwise decomposition of `nu`

Let

\[
D=\operatorname{lcm}(A_b,A_c).
\]

A positive-floor witness for `1+b=c` consists exactly of:

- a `b`-block coordinate vector realizing `d_x(b)=D`;
- a `c`-block coordinate vector realizing `d_x(c)=D`.

The coordinate blocks are disjoint, so the `L_infinity` norm of the combined witness is the maximum of the two block norms.

Therefore

\[
\boxed{
\nu(1,b,c)
=
\max\bigl(
\kappa_b(D),
\kappa_c(D)
\bigr).
}
\]

### Proof

Every absorption-floor witness must satisfy `d_x(b)=d_x(c)=±D`; changing the overall sign does not alter `L_infinity` norm. The two coordinate blocks are independent except for this common target. Thus the minimum maximum norm is obtained by minimizing each block preimage separately and taking the larger of the two minima. ∎

### Consequence

For unit relations, the global floor-access problem is not a generic high-dimensional CVP. It is the direct product of two independent block preimage problems.

This is substantially more structured than the general `omega(abc)>3` case.

## 7. `1+242=243` without a three-dimensional solver

For

\[
242=2\cdot11^2,
\]

the raw derivative coefficients are

\[
121,\ 44,
\]

so

\[
A(242)=11.
\]

For

\[
243=3^5,
\]

the raw derivative coefficient is

\[
405,
\]

so

\[
A(243)=405.
\]

Hence

\[
D=\operatorname{lcm}(11,405)=4455,
\]

and

\[
\eta_{\min}
=
\frac{4455}{11\cdot81}
=5.
\]

The two independent access problems are:

\[
121x_2+44x_{11}=4455
\]

and

\[
405x_3=4455.
\]

After dividing the first equation by `11`,

\[
11x_2+4x_{11}=405.
\]

Its exact minimum is attained by

\[
(x_2,x_{11})=(27,27),
\]

so

\[
\kappa_{242}(4455)=27.
\]

The second block requires

\[
x_3=11,
\]

so

\[
\kappa_{243}(4455)=11.
\]

Therefore

\[
\boxed{
u=\max(27,11)=27.}
\]

This recovers Supplement 09's exact result without using the global affine-line representation at all.

## 8. `1+512=513`: high quality, obstruction, and access all separated

For

\[
512=2^9,
\]

\[
A(512)=9\cdot2^8=2304.
\]

For

\[
513=3^3\cdot19,
\]

the raw derivative coefficients are

\[
513,\ 27,
\]

with image generator

\[
A(513)=27.
\]

Thus

\[
D=\operatorname{lcm}(2304,27)=6912,
\]

and with

\[
m(512)m(513)=256\cdot9=2304
\]

one gets

\[
\boxed{\eta_{\min}=3.}
\]

The `512` block needs coordinate `3`. The `513` block reduces to

\[
19x_3+x_{19}=256,
\]

whose minimum `L_infinity` solution has radius `13`, for example

\[
(x_3,x_{19})=(13,9).
\]

Hence

\[
\boxed{\nu=13.}
\]

This gives a compact exact profile for the earlier high-quality counterexample:

\[
\eta_{\min}=3,
\qquad
\nu=13,
\qquad
513^4>114^5.
\]

No implication among those three facts is asserted.

## 9. P025-T45 — Mersenne-prime unit family

Assume

\[
\boxed{
1+(2^m-1)=2^m
}
\]

and `2^m-1` is prime.

The prime block has

\[
A(2^m-1)=1.
\]

The prime-power block has one coordinate and

\[
A(2^m)=m2^{m-1}.
\]

Therefore

\[
D=m2^{m-1},
\qquad
M=2^{m-1},
\]

so

\[
\boxed{\eta_{\min}=m.}
\]

The prime block must realize derivative value `D` with its single coefficient `1`, hence its coordinate is exactly `D`. The power block uses coordinate `1`.

Consequently

\[
\boxed{
\nu=m2^{m-1}.
}
\]

There are only two prime coordinates in total, so P025-T22 also gives

\[
\boxed{\mu=\nu=m2^{m-1}.}
\]

Thus this family has no norm/absorption Pareto tradeoff, yet the arithmetic floor `m` and the very first witness radius `m2^(m-1)` can lie on radically different scales.

No infinitude of Mersenne primes is assumed.

### Examples

For `m=5`:

\[
1+31=32,
\qquad
\eta_{\min}=5,
\qquad
\mu=\nu=80.
\]

For `m=7`:

\[
1+127=128,
\qquad
\eta_{\min}=7,
\qquad
\mu=\nu=448.
\]

## 10. New architecture layer: image content versus generator access

The unit-relation decomposition makes one distinction unavoidable:

\[
\boxed{
\text{image content }A(n)
\neq
\text{access cost }\kappa_n(T).
}
\]

`A(n)` is enough to determine the block's attainable derivative ideal. It can therefore feed exact arithmetic-floor calculations.

But it does not determine the minimum coordinate radius needed to realize a selected target in that ideal. That requires additional coefficient geometry.

Thus even **inside one block**, P025 now sees the same architecture repeated:

\[
\text{generator/image state}
\to
\text{target selection}
\to
\text{minimum preimage precision}.
\]

This is the local form of the global `eta_min -> nu` distinction.

## 11. Prior-art discipline

Intersection of principal ideals, `lcm`, Bezout image generation, and minimum-norm preimages of integer linear forms are standard mathematics. P025 makes no priority claim for these tools.

The project-specific candidate is the repeated finite-precision pattern: an image generator can be a sufficient exact arithmetic state while access to a chosen generator value requires a strictly richer precision state.

## 12. Executable assets

Added:

- `src/enterprise_math/abc_unit_relation.py`
  - raw block derivative coefficients and image generator;
  - exact unit-relation Wronskian image as an `lcm` ideal intersection;
  - exact blockwise access decomposition for support size at most two;
  - Mersenne-prime closed family.
- `tests/test_abc_unit_relation.py`
  - ideal reconstruction for `1+242=243`;
  - blockwise recovery of `nu=27`;
  - `1+512=513` access radius `13`;
  - squarefree Sophie examples;
  - Mersenne examples `m=5,7`;
  - explicit refusal to hide a higher-rank block behind brute-force enumeration.

## 13. Next frontier

No hard block exists. Continue with:

1. study the block access function `kappa_n(T)` as a precision object in its own right;
2. determine its exact scaling/non-scaling laws under target multiplication;
3. characterize when `kappa_n(kA(n))=|k|kappa_n(A(n))` and produce counterexamples when this fails;
4. for squarefree multi-prime blocks, seek compact invariants of minimum Bezout coefficients below the full coefficient row;
5. test whether image-content/access-cost separation recurs in other Enterprise Math quotient/certificate systems.
