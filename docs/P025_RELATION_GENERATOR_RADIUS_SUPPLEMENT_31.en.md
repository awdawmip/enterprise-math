# P025 Supplement 31 — Relation-Generator Radius Between First Witness and Primitive Direct Access

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-shared-access-stage30`  
Depends on: P025 Supplements 14–15, 23, 30  
Hard block: `NONE`

## 1. A third access scale

Supplement 30 distinguishes the ambient derivative-image word norm from an intrinsic relation-step geometry. This suggests asking when finite-radius relation-compatible states become sufficient to **generate the whole relation subgroup**.

For a unit relation

\[
\boxed{1+b=c,}
\]

the compressed additive relation state is one-dimensional. Let

\[
A_b=A(b),
\qquad
A_c=A(c),
\]

and define the primitive positive common derivative-value group step

\[
\boxed{D=\operatorname{lcm}(A_b,A_c).}
\]

Every relation state has common derivative value

\[
t=kD,
\qquad k\in\mathbb Z.
\]

## 2. P025-D18 — radius-`R` accessible scale factors

Define

\[
\boxed{
K_R
=
\{k\in\mathbb Z:
\kappa_b(kD)\le R,
\ \kappa_c(kD)\le R\}.
}
\]

This set is finite and symmetric for each finite `R`.

The relation states available at radius `R` are exactly

\[
\boxed{D K_R.}
\]

Their generated subgroup is

\[
\boxed{
D\,g_R\mathbb Z,
\qquad
g_R=\gcd\{|k|:k\in K_R\}.
}
\]

Use the convention `g_R=0` when only the zero scale is accessible.

## 3. P025-D19 — relation-generator radius

Define

\[
\boxed{
\rho_{\rm gen}
=
\min\{R:g_R=1\}.
}
\]

Thus `rho_gen` is the first witness radius at which the currently accessible relation-compatible derivative states generate the entire rank-one relation group, even if the primitive group step `D` itself is not yet directly accessible.

This differs from two previous coordinates:

- `mu`: first nonzero/nondegenerate relation state;
- `nu`: first direct access to the primitive absorption-floor step `D`.

## 4. P025-T86 — universal ordering in the unit relation

For a unit relation, any nonzero common derivative value gives a nonzero Wronskian, so `mu` is the first radius with a nonzero element of `K_R`.

At radius `nu`, the primitive scale `k=1` is directly accessible by definition. Hence `g_nu=1`.

Therefore

\[
\boxed{
\mu\le\rho_{\rm gen}\le\nu.
}
\]

Neither inequality must be equality.

## 5. Exact example `1+8=9`

Here

\[
D=12.
\]

No nonzero common derivative value is accessible at radius one. At radius two, `k=1` is already accessible.

Thus

\[
\boxed{
\mu=\rho_{\rm gen}=\nu=2.
}
\]

## 6. Exact example `1+22=23`

Here both blocks are squarefree/prime on the derivative-image level, so

\[
D=1.
\]

At radius two, the common target `2` is accessible:

\[
K_2=\{0,\pm2\},
\]

hence

\[
g_2=2.
\]

At radius three no odd common scale is yet accessible, so still

\[
g_3=2.
\]

At radius four, both scales `2` and `3` are accessible. Therefore

\[
\gcd(2,3)=1
\]

and the accessible relation states generate the entire group, despite the primitive state `k=1` still being inaccessible.

Direct primitive access occurs only at radius five.

Hence

\[
\boxed{
\mu=2
<
\rho_{\rm gen}=4
<
\nu=5.
}
\]

This is an exact separation of three finite precision notions.

## 7. P025-T87 — Sophie-type closed generator radius

Assume

\[
q\ge5,
\qquad q\text{ prime},
\qquad2q+1\text{ prime}.
\]

Consider

\[
\boxed{1+2q=2q+1.}
\]

Since `q>=5`, primality of `2q+1` forces

\[
\boxed{q\equiv5\pmod6.}
\]

The unit relation group step is

\[
D=1.
\]

Stage 14 gives

\[
\boxed{
\mu=2,
\qquad
\nu=\frac{q-1}{2}.
}
\]

The generator radius is

\[
\boxed{
\rho_{\rm gen}
=
\frac{q+1}{3}.
}
\]

### Proof

The even common target `2` is accessible at radius two: in the `2q` block use the coefficient-2 coordinate once, and in the prime block use coordinate value two.

To generate the full group `Z`, an odd common target must eventually become accessible.

Write a `2q`-block target as

\[
qx+2y=t.
\]

Suppose `t` is odd and all three magnitudes

\[
|x|,|y|,|t|
\]

are at most `R`.

For `R<q`, odd `x` with `|x|>=3` is impossible, because

\[
|qx+2y|
\ge3q-2R
>R.
\]

Thus the first odd target can use only `x=±1`. By symmetry take `x=1` and positive odd `t`; then

\[
y=\frac{t-q}{2}.
\]

The radius constraints require

\[
t\le R,
\qquad
\frac{q-t}{2}\le R.
\]

Therefore

\[
q\le3R,
\]

so

\[
R\ge\left\lceil\frac q3\right\rceil.
\]

Because `q=6k+5`, this lower bound is

\[
2k+2=\frac{q+1}{3}.
\]

At exactly this radius choose

\[
t=2k+1,
\qquad
x=1,
\qquad
y=-(2k+2).
\]

Then `t` is odd and all magnitudes are at most `(q+1)/3`. So the first odd common scale appears exactly there.

Since scale `2` was already available, the gcd of accessible scales becomes one immediately. ∎

## 8. Strict three-level separation

For `q=5`, all three values happen to equal two.

For every Sophie-type input in the stated scope with

\[
q\ge11,
\]

one has

\[
\boxed{
2
=\mu
<
\frac{q+1}{3}
=ho_{\rm gen}
<
\frac{q-1}{2}
=
u.
}
\]

Examples:

\[
\begin{array}{c|c|c|c}
q&\mu&\rho_{\rm gen}&\nu\\\hline
11&2&4&5\\
23&2&8&11\\
29&2&10&14\\
41&2&14&20
\end{array}
\]

No claim is made that infinitely many such `q` exist.

## 9. Architectural consequence

The unit-relation precision ladder now has three distinct access semantics:

\[
\boxed{
\text{first nonzero witness }\mu
\to
\text{group-generation radius }\rho_{\rm gen}
\to
\text{primitive direct access }\nu.
}
\]

The middle level says:

> the current finite set of relation-compatible states is collectively sufficient to generate every relation state under integer composition, even though the primitive generator itself is still outside the current direct-access ball.

So “directly observable at this precision” and “algebraically generatable from states observable at this precision” are different notions.

This distinction is closely analogous to other Enterprise Math boundaries between exact current state, generated closure, and future-language sufficiency.

## 10. Prior-art boundary

Subgroups of `Z`, gcd generation, word-generation radii, and the elementary modular/Bezout arguments above are standard mathematics.

P025 does not claim them generically. The project-side result is the explicit insertion of a generator-completeness precision layer between first witness access and primitive floor access in the arithmetic-derivative relation system.

## 11. Executable assets

Added:

- `src/enterprise_math/abc_relation_generator_radius.py`
  - unit relation group step;
  - radius-accessible scale factors;
  - generated scale gcd;
  - exact generator radius;
  - Sophie-family closed profile.
- `tests/test_abc_relation_generator_radius.py`
  - `1+8=9` collapse of all three scales;
  - `1+22=23` strict `2<4<5` separation;
  - Sophie examples `q=5,11,23,29,41`;
  - strict separation for `q>=11` examples.

## 12. Next frontier

No hard block exists. Continue with:

1. define `rho_gen` for higher-rank relation subgroups using HNF/index rather than scalar gcd;
2. compare intrinsic word metrics generated at radius `rho_gen` with the ambient restricted access norm;
3. determine whether generator completeness is the right state for future languages allowing arbitrary integer composition but not direct inverse witness recovery;
4. relay the new access/generation/direct-access distinction to P023/A5;
5. search for families where `rho_gen/mu` or `nu/rho_gen` is provably unbounded without assuming unresolved infinitude statements.
