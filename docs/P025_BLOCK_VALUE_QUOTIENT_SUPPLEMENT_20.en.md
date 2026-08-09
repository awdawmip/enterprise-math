# P025 Supplement 20 — Exact Block Derivative-Value Quotient for Witness Cost Languages

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-access-tail-stage18`  
Depends on: P025 Supplements 13–19; P023 future-compatible quotient semantics  
Hard block: `NONE`

## 1. A second kind of compression

Supplement 19 shows that each individual arithmetic block can realize an arbitrary primitive positive coefficient row. Therefore one cannot simplify the **internal block access function** by assuming a hidden special row class.

But the abc relation does not inspect every prime coordinate directly. For the future language used in the current Wronskian certificate problem, it reads each block only through its arithmetic derivative value.

For a fine witness write

\[
\boxed{
t_a=d_x(a),
\qquad
t_b=d_x(b),
\qquad
t_c=d_x(c).}
\]

Additivity is exactly

\[
\boxed{t_a+t_b=t_c,}
\]

and the arithmetic Wronskian is exactly

\[
\boxed{W=a t_b-b t_a.}
\]

This suggests quotienting the high-dimensional prime-coordinate witness by its three block derivative values, while retaining the exact minimum access response of each block.

## 2. Block derivative image ideals and access functions

For `n>1`, let

\[
\boxed{A(n)=\gcd_{p\mid n}\frac{n v_p(n)}p}
\]

be the raw derivative image generator from Supplement 15. Then

\[
d_x(n)\in A(n)\mathbb Z.
\]

For the unit block set its image to `{0}`.

Define the exact block access function

\[
\boxed{
\kappa_n(t)
=
\min\{\|x^{(n)}\|_\infty:d_{x^{(n)}}(n)=t\}.
}
\]

It is finite exactly on the block derivative image. Supplements 16–18 provide finite exact representations of this response after dividing the raw coefficient row by its image generator.

## 3. P025-D12 — compressed derivative-value lattice

Define

\[
\boxed{
\Lambda_{abc}
=
\{(u,v)\in\mathbb Z^2:
 u\in A(a)\mathbb Z,
 v\in A(b)\mathbb Z,
 u+v\in A(c)\mathbb Z
\}.
}
\]

For a unit block, the corresponding condition means its derivative value is exactly zero.

Every additive fine witness maps to

\[
(u,v)=(t_a,t_b)\in\Lambda_{abc}.
\]

Conversely every point of `Lambda_abc` has independent prime-coordinate preimages inside the three blocks, and those preimages automatically satisfy additive relation compatibility because `t_c=u+v`.

Thus the fine additive witness family surjects onto this rank-at-most-two integer lattice.

## 4. P025-T57 — exact minimum fine norm over one block-value state

For `(u,v) in Lambda_abc`, define

\[
\boxed{
K(u,v)
=
\max\bigl(
\kappa_a(u),
\kappa_b(v),
\kappa_c(u+v)
\bigr).
}
\]

Then

\[
\boxed{
K(u,v)
=
\min\{\|x\|_\infty:
 x\text{ is an additive fine witness with }
(d_x(a),d_x(b))=(u,v)\}.
}
\]

### Proof

Any fine representative with these block derivative values restricts on each disjoint prime-support block to a preimage of the corresponding target. Hence its norm is at least each block minimum and therefore at least `K(u,v)`.

Conversely choose, independently inside each block, a prime-coordinate preimage attaining the block minimum. The blocks have disjoint coordinates. Their union is an additive fine witness because the derivative values satisfy `u+v=t_c`, and its global `L_infinity` norm is exactly the maximum of the three block norms. ∎

So the block-value state loses prime-coordinate identity but retains the exact optimal geometric cost for this future language.

## 5. P025-T58 — Wronskian and absorption descend exactly

For every compressed point `(u,v) in Lambda_abc`,

\[
\boxed{
W(u,v)=a v-b u.
}
\]

Let

\[
M=m(a)m(b)m(c).
\]

Pasten's residual divisibility implies that every nonzero additive compressed witness satisfies

\[
M\mid W(u,v).
\]

Therefore define

\[
\boxed{
\eta(u,v)=\frac{|a v-b u|}{M}
}
\]

for nondegenerate points.

Both Wronskian magnitude and absorption redundancy depend only on the block-value quotient; no within-block prime identity is read.

## 6. P025-T59 — fine and block-value Pareto frontiers are identical

Let the fine witness cost pair be

\[
C(x)=(\|x\|_\infty,\eta(x)).
\]

Then

\[
\boxed{
\operatorname{Min}
\{C(x):x\text{ nondegenerate additive fine witness}\}
=
\operatorname{Min}
\left\{
\left(K(u,v),\frac{|av-bu|}{M}\right):
(u,v)\in\Lambda_{abc},\ av-bu\ne0
\right\}.
}
\]

### Proof

Every fine witness maps to one compressed point with the same `eta` and norm at least `K(u,v)`, so it is dominated by a minimum-norm representative of the same compressed state.

Conversely P025-T57 constructs a fine representative attaining exactly `K(u,v)` for every compressed point. Thus the nondominated cost pairs agree in both directions. ∎

This is an exact quotient theorem for the declared norm/Wronskian certificate language.

## 7. Consequences for `mu`, `eta_min`, and `nu`

The scalar witness radius becomes

\[
\boxed{
\mu
=
\min_{(u,v)\in\Lambda_{abc},\ av-bu\ne0}
K(u,v).
}
\]

The arithmetic absorption floor becomes

\[
\boxed{
\eta_{\min}
=
\frac1M
\min_{(u,v)\in\Lambda_{abc},\ av-bu\ne0}
|av-bu|.
}
\]

And the first floor-access radius is

\[
\boxed{
\nu
=
\min_{(u,v)\in\Lambda_{abc},\ |av-bu|=M\eta_{\min}}
K(u,v).
}
\]

Thus all three current precision coordinates can be defined entirely on a two-dimensional derivative-value lattice equipped with block access responses.

This does **not** mean those optimization problems are automatically easy; Supplement 19 shows each block access response can already contain arbitrary primitive-row complexity.

## 8. Examples

### `2+3=5`

All three blocks are prime, so their derivative image generators are one and

\[
\kappa_n(t)=|t|.
\]

Hence

\[
K(u,v)=\max(|u|,|v|,|u+v|),
\qquad
W=2v-3u.
\]

The point `(0,1)` gives

\[
(K,\eta)=(1,2),
\]

while `(1,1)` gives

\[
(K,\eta)=(2,1).
\]

Therefore the compressed lattice immediately reproduces

\[
\boxed{
\mathcal P(2,3,5)=\{(1,2),(2,1)\}.
}
\]

### `1+8=9`

The unit block forces `t_a=0`. The derivative images are

\[
t_8\in12\mathbb Z,
\qquad
t_9\in6\mathbb Z,
\]

and additivity requires `t_8=t_9`. The smallest nonzero compressed state is therefore

\[
(0,12,12).
\]

Its block access radii are `(0,1,2)`, so

\[
\mu=2.
\]

Its Wronskian is `12`, exactly the residual product, so `eta=1`.

This recovers the earlier fine-lattice result without retaining the individual prime coordinates.

### `1+242=243`

The floor compressed state is

\[
(t_1,t_{242},t_{243})=(0,4455,4455).
\]

The exact block radii are

\[
(0,27,11),
\]

hence

\[
\boxed{\nu=27,
\qquad\eta=5.}
\]

This recovers Supplement 15's unit-relation decomposition as the rank-one boundary of the general block-value quotient.

## 9. What this quotient is not safe for

The map

\[
\text{fine prime-coordinate witness}
\mapsto
(t_a,t_b,t_c)
\]

is **not** asserted to preserve:

- which prime coordinates carry the certificate;
- witness multiplicity/counts;
- exact decomposition identities inside a block;
- later operations that act differently on two prime-coordinate representatives with the same derivative value.

If those observables enter the future language, P023 requires a finer state.

So this is a future-language-specific exact quotient, not an ontological claim that prime-factor coordinates are unreal or always disposable.

## 10. Architectural consequence

Supplements 13–20 now expose a nested decomposition:

\[
\boxed{
\text{fine prime coordinates}
\to
\text{block access response}
\to
\text{block derivative values }(t_a,t_b,t_c)
\to
\text{rank-two relation lattice }\Lambda_{abc}
\to
\text{norm/Wronskian certificate queries}.
}
\]

Internal block complexity can be universal, while relation coupling still collapses the **global certificate interaction** to two derivative-value coordinates.

This is precisely the kind of distinction P023 was designed to express: the minimum sufficient state is indexed by the future language.

## 11. Prior-art boundary

Images of integer linear forms, product decompositions over disjoint coordinate blocks, congruence lattices, and minimization over quotient fibers are standard mathematics. P025 does not claim those general facts as new.

The project-side candidate is the exact integration of:

- Pasten arithmetic derivative blocks;
- finite block access precision from Supplements 16–18;
- the derivative-value relation lattice;
- the norm/absorption Pareto certificate language.

Historical novelty of this packaged interface remains `NOVELTY_UNVERIFIED`.

## 12. Executable assets

Added:

- `src/enterprise_math/abc_block_value_quotient.py`
  - exact block target membership and access cost;
  - compressed derivative-value lattice membership;
  - Wronskian/absorption evaluation;
  - bounded block-value Pareto oracle;
  - fine-vs-block Pareto cross-checks.
- `tests/test_abc_block_value_quotient.py`
  - `2+3=5` frontier reconstruction;
  - `1+8=9` compressed witness;
  - `1+242=243` floor access;
  - fine/block frontier equality on current small reference examples.

## 13. Next frontier

No hard block exists. Continue with:

1. derive a compact basis / Smith description of `Lambda_abc` from the three block image generators;
2. recover the earlier `eta_min` block formula directly as the image generator of `W` on `Lambda_abc`;
3. test whether `mu` or `nu` admits stronger bounds from relation-lattice geometry plus finite block capacity frontiers;
4. extend from one Wronskian observable to several simultaneous certificate linear forms;
5. identify the P023-minimal state for each enriched block-value future language.
