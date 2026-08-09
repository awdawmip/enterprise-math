# P025 Supplement 22 — One-Dimensional Floor Line for Arbitrary-Support Absorption Access

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-access-tail-stage18`  
Depends on: P025 Supplements 20–21 and finite block access from Supplements 16–18  
Hard block: `NONE`

## 1. `eta_min` is two-dimensional; floor access is only one-dimensional

Supplement 20 compresses the fine additive witness family to

\[
\Lambda_{abc}
=
\{(u,v):u\in A\mathbb Z,\ v\in B\mathbb Z,\ u+v\in C\mathbb Z\}
\subseteq\mathbb Z^2.
\]

Supplement 21 proves that the Wronskian image is

\[
W(\Lambda_{abc})=D\mathbb Z,
\qquad
W(u,v)=av-bu.
\]

The absorption floor is attained exactly on

\[
\boxed{
\mathcal F_D
=
\{(u,v)\in\Lambda_{abc}:W(u,v)=\pm D\}.
}
\]

For three non-unit blocks `Lambda_abc` has rank two, while `W=D` is one independent integer linear equation. Therefore each sign of the floor set is an affine rank-one lattice.

This reduces arbitrary-support `nu` to one integer parameter once the block access responses are available.

## 2. P025-T63 — explicit HNF-like basis of `Lambda_abc`

Assume `A,B,C>0` and set

\[
G=\gcd(A,B,C),
\qquad
d=\gcd(A,C).
\]

Put

\[
\boxed{y_0=d/G.}
\]

Since

\[
\gcd(A/d,C/d)=1,
\]

there is a unique residue

\[
0\le x_0<C/d
\]

satisfying

\[
\boxed{
\frac Ad x_0
\equiv
-\frac BG
\pmod{C/d}.
}
\]

Then

\[
\boxed{
g_1=(AC/d,0),
\qquad
g_2=(Ax_0,Bd/G)}
\]

is a basis of `Lambda_abc`.

### Proof

Both vectors satisfy `u in AZ`, `v in BZ`, and `u+v in CZ` by construction. Their determinant is

\[
\left|\det(g_1,g_2)\right|
=
\frac{AC}{d}\frac{Bd}{G}
=
\frac{ABC}{G},
\]

which equals the lattice index proved in Supplement 21. Therefore the two contained lattice vectors generate all of `Lambda_abc`. ∎

The chosen residue range makes this an HNF-like canonical basis relative to the coordinate order.

## 3. P025-T64 — explicit affine floor line

Let

\[
w_i=W(g_i).
\]

Supplement 21 implies

\[
\gcd(w_1,w_2)=D.
\]

Choose Bezout coefficients `r,s` with

\[
rw_1+sw_2=D.
\]

Define

\[
\boxed{p_0=r g_1+s g_2.}
\]

Then

\[
W(p_0)=D.
\]

Now define

\[
\boxed{
h
=
\frac{w_2}{D}g_1
-
\frac{w_1}{D}g_2.}
\]

Because `gcd(w_1/D,w_2/D)=1`, this is a primitive lattice direction in the kernel of `W` on `Lambda_abc`.

Hence

\[
\boxed{
\{(u,v)\in\Lambda_{abc}:W(u,v)=D\}
=
p_0+\mathbb Z h.
}
\]

The `W=-D` line is its negative and has the same access costs because block access is sign-symmetric.

## 4. P025-T65 — arbitrary-support `nu` is a one-parameter optimization

Recall

\[
K(u,v)
=
\max\bigl(
\kappa_a(u),
\kappa_b(v),
\kappa_c(u+v)
\bigr).
\]

Then

\[
\boxed{
\nu
=
\min_{k\in\mathbb Z}
K(p_0+k h).
}
\]

No assumption on the total number of prime coordinates is needed. All within-block high-dimensional geometry has already been compiled into the three exact access functions.

This strictly generalizes Supplement 09's affine-line solver, which required the whole fine witness ambient space to have only three prime coordinates.

## 5. P025-T66 — the one-dimensional search has an exact finite bound

Let

\[
R_0=K(p_0)
\]

be the cost of the constructed Bezout floor point.

For one block `n`, let its raw derivative coefficient row be `(c_{n,p})`. Any prime-coordinate vector of radius at most `R_0` satisfies

\[
|d_x(n)|
\le
R_0\sum_{p\mid n}|c_{n,p}|.
\]

Therefore any floor point that can improve on or tie `R_0` must satisfy three finite target inequalities:

\[
\begin{aligned}
|u_0+k h_u|&\le R_0 S_a,\\
|v_0+k h_v|&\le R_0 S_b,\\
|u_0+v_0+k(h_u+h_v)|&\le R_0 S_c,
\end{aligned}
\]

where

\[
S_n=\sum_{p\mid n}\frac{n v_p(n)}p
\]

and `S_1=0`.

Each inequality is an exact integer interval in `k`. Their intersection is finite in the rank-two case because the Wronskian-kernel direction is nonzero.

Thus an exact algorithm is:

1. construct `p_0` and `h`;
2. compute `R_0`;
3. intersect the three integer parameter intervals above;
4. evaluate `K` only on that finite interval;
5. take the minimum.

This enumerates floor-line parameter values, not prime-coordinate witness cubes.

## 6. Rank-one unit boundary

If `a=1`, then `u=0` and

\[
v\in B\mathbb Z\cap C\mathbb Z
=\operatorname{lcm}(B,C)\mathbb Z.
\]

The positive floor point is uniquely

\[
\boxed{(u,v)=(0,D)}
\]

with

\[
D=\operatorname{lcm}(B,C).
\]

Similarly, if `b=1`, the floor point is unique up to sign on the `u` axis.

So Supplement 15's unit-relation blockwise access is exactly the rank-one boundary of the same construction.

## 7. Exact examples

### `2+3=5`

The basis is

\[
((1,0),(0,1)),
\]

with Wronskian values `(-3,2)`, so `D=1`. One Bezout floor point is `(1,2)` and the kernel direction is `(2,3)`.

The exact floor-line optimization finds a cheaper equivalent point on the same line, for example `(-1,-1)`, and gives

\[
\boxed{\nu=2.}
\]

### `2+7=9`

Here

\[
(A,B,C)=(1,1,6)
\]

and an HNF-like basis is

\[
\boxed{((6,0),(5,1)).}
\]

The basis Wronskians are `(-42,-33)`, whose gcd is `D=3`. A positive floor point is

\[
(1,5),
\]

and the kernel direction is

\[
(4,14).
\]

The exact solver gives

\[
\boxed{\nu=5.}
\]

matching the earlier fine-lattice result.

### `5+7=12`

The basis is

\[
((4,0),(3,1)),
\]

with `D=4`, floor point `(-2,-2)`, and kernel direction `(5,7)`. The exact result is

\[
\boxed{\eta_{\min}=2,\qquad\nu=2.}
\]

### `25+704=729`

This example spans four fine prime coordinates across its blocks. The compressed exact solver finds

\[
\boxed{
(t_a,t_b,t_c)=(-20,8768,8748),
}
\]

with

\[
\boxed{
\eta_{\min}=6,
\qquad
\nu=6.
}
\]

The search occurs on the one-dimensional block-value floor line instead of a four-dimensional prime-coordinate cube.

## 8. Architecture consequence

The arbitrary-support floor-access chain is now

\[
\boxed{
\text{fine prime witness}
\to
\text{three block access functions}
+
\Lambda_{abc}
\to
\text{one affine floor line}
\to
\nu.
}
\]

So two different sources of complexity have been separated:

- within-block preimage geometry, compiled into `kappa_n`;
- cross-block relation geometry, reduced to a one-dimensional floor line.

This is stronger than simply saying “a short witness exists”: it gives an exact finite search domain for the minimum floor-access precision.

## 9. Prior-art boundary

HNF-style lattice bases, Bezout parameterization of a linear Diophantine level set, and affine-lattice one-parameter optimization are standard mathematics.

P025 does not claim those generic tools as new. The project-side result under test is the exact reduction of arbitrary-support arithmetic-derivative floor access through the previously established block-value quotient and finite block access responses.

Historical novelty of the integrated interface remains `NOVELTY_UNVERIFIED`.

## 10. Executable assets

Added:

- `src/enterprise_math/abc_block_floor_line.py`
  - HNF-like compressed-lattice basis;
  - Wronskian Bezout floor point;
  - primitive floor-line direction;
  - exact finite parameter bound;
  - arbitrary-support exact `nu` solver.
- `tests/test_abc_block_floor_line.py`
  - `2+3=5`, `2+7=9`, `5+7=12` line data;
  - rank-one unit relations;
  - `1+242=243`, `1+512=513` access;
  - four-coordinate `25+704=729` example;
  - additional small exact values.

## 11. Next frontier

No hard block exists. Continue with:

1. attack `mu`, which still minimizes over the full two-dimensional compressed lattice rather than one floor line;
2. exploit finite block capacity frontiers to derive exact/bounded sublevel sets of `K(u,v)`;
3. ask whether Wronskian-threshold queries admit finite two-dimensional antichain boundaries analogous to Stage 18;
4. compare the exact floor-line algorithm with Pasten's Geometry-of-Numbers sufficient norm bounds;
5. extend the block-value quotient to several simultaneous linear certificate forms.
