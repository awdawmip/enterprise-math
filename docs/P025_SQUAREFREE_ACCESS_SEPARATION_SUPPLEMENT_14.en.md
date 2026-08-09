# P025 Supplement 14 — Squarefree Arithmetic Floor with Large Access Delay

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner: `program/p025-abc-support-collapse`  
Depends on: P025 Supplements 07, 13  
Hard block: `NONE`

## 1. Purpose

Supplement 13 shows that the arithmetic absorption floor can collapse all within-block prime-coordinate information into tiny block contents. The natural falsification question is whether this arithmetic compression also preserves the geometric cost of accessing that floor.

It does not.

A particularly clean conditional family has **no arithmetic absorption obstruction at all** while its floor-access radius can become much larger than the first witness radius.

## 2. Conditional Sophie Germain family

Let `q` be an odd prime such that

\[
\boxed{c=2q+1}
\]

is also prime. Then

\[
\boxed{1+2q=c}
\]

is a primitive abc triple with every non-unit term squarefree.

No infinitude of such primes is assumed or claimed. The theorem applies to each actual pair satisfying the displayed primality conditions.

Because the triple is squarefree, P025-T16 gives

\[
\boxed{\eta_{\min}=1.}
\]

The block derivative contents are also as small as possible:

\[
h(2q)=1,
\qquad
h(c)=1.
\]

Thus the arithmetic-floor language sees no nontrivial absorption obstruction.

## 3. P025-T39 — exact floor-access radius

For a unit-first relation `1+b=c`, the arithmetic Wronskian is simply

\[
W(1,b)=d_x(b).
\]

Here

\[
b=2q
\]

is squarefree, so on prime coordinates `(2,q)` one has

\[
\boxed{d_x(2q)=q x_2+2x_q.}
\]

Since `M=1` and `eta_min=1`, an absorption-floor witness must satisfy

\[
\boxed{q x_2+2x_q=\pm1.}
\]

The `c`-block is prime, so additivity forces its single coordinate to be the same sign `±1`; that coordinate does not increase the optimum beyond one.

For odd `q`, the minimum `L_infinity` solution of

\[
q u+2v=1
\]

is

\[
\boxed{u=1,
\qquad
v=\frac{1-q}{2}.}
\]

Hence

\[
\boxed{
\nu
=
\frac{q-1}{2}.
}
\]

### Proof of optimality

The equation modulo `2` forces `u` odd. The admissible values are therefore `u=...,-3,-1,1,3,...`. For `u=1`,

\[
v=(1-q)/2.
\]

For `u=-1`,

\[
v=(q+1)/2,
\]

which is already larger in absolute value. Moving `u` by any further multiple of `2` changes `v` by a multiple of `q`, increasing the maximum coordinate beyond the `u=1` solution. Thus the stated pair is `L_infinity`-minimal. ∎

## 4. P025-T40 — the first witness radius stays tiny

The full additive relation is

\[
q x_2+2x_q-x_c=0,
\]

and the Wronskian value is

\[
W=q x_2+2x_q=x_c.
\]

For `q>=5`, the vector

\[
\boxed{(x_2,x_q,x_c)=(0,1,2)}
\]

is a non-degenerate witness of radius `2`, so

\[
\mu\le2.
\]

Radius `1` is impossible:

- if `x_2=0`, then `W` is even, so a nonzero `W` has `|W|>=2` and cannot equal a coordinate bounded by one;
- if `x_2=±1`, then for `x_q in {-1,0,1}`,
  \[
  |W|=|\pm q+2x_q|\ge q-2\ge3.
  \]

Thus

\[
\boxed{\mu=2\qquad(q>=5).}
\]

For the exceptional smallest case `q=3`, `(1,-1,1)` has radius one and therefore `mu=1`.

## 5. P025-C02 — exact access delay

For every actual family member with `q>=5`,

\[
\boxed{
\delta_{\rm abs}
=
\nu-\mu
=
\frac{q-5}{2}.
}
\]

So arithmetic floor, first-certificate geometry, and floor-access geometry separate completely:

\[
\boxed{
\eta_{\min}=1,
\qquad
\mu=2,
\qquad
\nu=(q-1)/2.
}
\]

Again, no asymptotic/unbounded conclusion is inferred without an infinitude result for the prime family. The formula itself is exact for every actual member.

## 6. P025-T41 — exact two-point Pareto frontier for `q>=11`

For `q>=11`, `nu>2`.

At radius `2`, the witness `(0,1,2)` gives

\[
\eta=|W|=2,
\]

so `(2,2)` is attainable.

By definition of `nu`, no witness of radius less than `nu` can have `eta=1`. Since `eta` is a positive integer, every cost point with radius at least `2` and `eta>=2` is dominated by `(2,2)`, while every point with `eta=1` is dominated by the first one at radius `nu`.

Therefore

\[
\boxed{
\mathcal P
=
\{(2,2),(\nu,1)\}
\qquad(q>=11).
}
\]

The small cases collapse as expected:

- `q=3`: `P={(1,1)}`;
- `q=5`: `P={(2,1)}`.

## 7. Exact working examples

### `q=5`

\[
1+10=11,
\qquad
\eta_{\min}=1,
\qquad
\mu=\nu=2.
\]

### `q=11`

\[
1+22=23,
\qquad
\mu=2,
\qquad
\nu=5,
\qquad
\delta_{\rm abs}=3.
\]

### `q=23`

\[
1+46=47,
\qquad
\mu=2,
\qquad
\nu=11,
\qquad
\delta_{\rm abs}=9.
\]

### `q=41`

\[
1+82=83,
\qquad
\mu=2,
\qquad
\nu=20,
\qquad
\delta_{\rm abs}=18.
\]

In all these examples the arithmetic floor remains exactly one.

## 8. Direct no-go for content-only geometric precision

For every squarefree unit-first member of this family,

\[
h(2q)=h(2q+1)=1
\]

and

\[
\eta_{\min}=1.
\]

Yet `nu` varies with `q`.

Thus the block derivative contents that are complete for the absorption-floor observable are not complete for the access-radius observable.

This gives the explicit future-language boundary promised after Supplement 13:

\[
\boxed{
\text{same minimal block-content type for }\eta_{\min}
\not\Rightarrow
\text{same access precision }\nu.
}
\]

More strongly, even **perfect absorption** plus squarefree multiplicity data do not imply a nearby floor certificate.

## 9. Relation to P023

This is a particularly transparent task-relative precision example.

For the arithmetic-floor language, the state may collapse to

\[
(h_b,h_c,g)=(1,1,1)
\]

and the answer `eta_min=1` is exact.

For the geometric-access language, that same compression is illegal: the coefficient geometry `(q,2)` must remain visible at least through the Bezout access class needed to distinguish `(q-1)/2`.

So one representation can be exact for one future query and radically insufficient for another, even though both queries concern the same witness system.

## 10. Prior-art discipline

Sophie Germain primes, the linear equation `qu+2v=1`, parity, and minimum-size Bezout coefficients are classical arithmetic. P025 claims no priority for them.

The family is used solely as a precise pressure test demonstrating that arithmetic image content and geometric preimage access are different finite-precision objects.

## 11. Executable assets

Added:

- `src/enterprise_math/abc_absorption_sophie.py`
  - domain validation;
  - exact `eta_min`, `mu`, `nu`, access delay and Pareto frontier;
  - exact floor witness.
- `tests/test_abc_absorption_sophie.py`
  - calibration at `q=3,5`;
  - growing delays for exact working examples `q=11,23,29,41`;
  - exact floor-witness equation;
  - rejection of non-family input.

## 12. Next frontier

No hard block exists. Continue with:

1. formulate the minimal extra state beyond block content needed to recover `nu` in squarefree blocks;
2. compare that state with the full primitive additive normal and seek a coarser Bezout-access signature;
3. generalize from one two-prime squarefree block to arbitrary squarefree blocks, where the floor-access problem becomes shortest Bezout coefficients for the reciprocal-product coefficient row;
4. test whether known lattice invariants provide a compact access signature without reintroducing the full witness generator;
5. keep any infinity/unboundedness statement conditional unless the relevant prime-family infinitude is independently proved.
