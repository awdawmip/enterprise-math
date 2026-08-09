# P025 Supplement 23 — Exact `mu` as First Escape from the Block Scaling Line

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-access-tail-stage18`  
Depends on: P025 Supplements 20–22  
Hard block: `NONE`

## 1. `nu` became one-dimensional; `mu` still reads a two-dimensional sublevel set

Supplement 22 reduces the absorption-floor access radius `nu` to one affine line because the floor condition fixes the Wronskian value `W=±D`.

The first nondegenerate witness radius

\[
\mu
\]

is different: it asks only for `W!=0`, so it ranges over the whole compressed additive lattice.

The block-value quotient nevertheless removes the fine prime-coordinate cube. At each radius, only finitely many **scalar derivative values per block** need to be retained.

## 2. P025-D13 — reachable block derivative values

For a block `n` and radius `r>=0`, define

\[
\boxed{
V_n(r)
=
\{d_x(n):\|x\|_\infty\le r\}.
}
\]

For a unit block,

\[
V_1(r)=\{0\}.
\]

For `n>1`, write the raw derivative row as

\[
A(n)b,
\]

where `b` is primitive positive and

\[
P_n=\sum_i b_i.
\]

Then every reduced derivative value lies in

\[
[-rP_n,rP_n]\cap\mathbb Z,
\]

so

\[
\boxed{|V_n(r)|\le2rP_n+1.}
\]

The exact set can be built by repeated Minkowski/set addition of the scalar coordinate ranges

\[
[-rb_i,rb_i]_{b_i\mathbb Z}
\]

without enumerating the Cartesian prime-coordinate cube.

Thus the compression changes a potential `(2r+1)^omega(n)` state enumeration into a one-dimensional reachable-value calculation inside each block.

## 3. P025-D14 — compressed additive reachable set

Define

\[
\boxed{
\mathcal R_r
=
\{(u,v,u+v):
 u\in V_a(r),
 v\in V_b(r),
 u+v\in V_c(r)\}.
}
\]

This is exactly the set of block derivative-value states induced by fine additive witnesses of radius at most `r`.

The sets are nested:

\[
\mathcal R_r\subseteq\mathcal R_{r+1}.
\]

## 4. P025-T67 — Wronskian degeneracy is exactly the integer scaling line

For a compressed additive state `(u,v,u+v)`,

\[
W=av-bu.
\]

Because

\[
\gcd(a,b)=1,
\]

one has

\[
\boxed{
W=0
\iff
(u,v,u+v)=t(a,b,c)
\text{ for some }t\in\mathbb Z.
}
\]

### Proof

If `W=0`, then

\[
av=bu.
\]

Since `gcd(a,b)=1`, `a|u` and `b|v`. Write

\[
u=at,
\qquad
v=bs.
\]

Substitution gives `ab s=ab t`, hence `s=t`. Additivity then gives

\[
u+v=(a+b)t=ct.
\]

The converse is immediate. ∎

Define the **degenerate scaling line**

\[
\boxed{
\Delta_{abc}
=
\{t(a,b,c):t\in\mathbb Z\}.
}
\]

## 5. P025-T68 — exact first-escape characterization of `mu`

The first nondegenerate witness radius is exactly

\[
\boxed{
\mu
=
\min\{r\ge1:
\mathcal R_r\not\subseteq\Delta_{abc}\}.
}
\]

### Proof

By construction, `R_r` is exactly the compressed image of all fine additive witnesses with norm at most `r`. By P025-T67, a compressed state is Wronskian-degenerate exactly when it lies on `Delta_abc`. Therefore a nondegenerate fine witness exists at radius `r` exactly when `R_r` contains a point outside the scaling line. Taking the first such radius gives `mu`. ∎

This is an exact relation-state escape problem, not a heuristic witness search.

## 6. P025-T69 — exact arbitrary-support finite solver

Supplement 22 supplies an exact floor witness at radius `nu`, so

\[
\mu\le\nu
\]

is a finite upper bound.

An exact algorithm is therefore:

1. compute `nu` by the block floor-line solver;
2. for `r=1,...,nu`, build `V_a(r),V_b(r),V_c(r)` as scalar reachable sets;
3. form only additive pairs `(u,v)` with `u+v in V_c(r)`;
4. stop at the first point with `av-bu != 0`.

This is exact for arbitrary support size and never enumerates fine prime-coordinate witness cubes.

## 7. Examples

### `2+3=5`

At radius one, all prime blocks can already realize `-1,0,1`. The compressed additive set contains, for example,

\[
(-1,0,-1),
\]

which does not lie on the scaling line. Therefore

\[
\boxed{\mu=1.}
\]

The floor access remains `nu=2`, yielding the known Pareto tradeoff.

### `1+8=9`

At radius one,

\[
V_8(1)=\{-12,0,12\},
\qquad
V_9(1)=\{-6,0,6\},
\]

but additivity `t_8=t_9` leaves only zero. Thus

\[
\mathcal R_1=\{(0,0,0)\}
\]

and no nondegenerate witness exists.

At radius two, the common value `12` appears and gives

\[
\boxed{\mu=2.}
\]

### `1+22=23`

The absorption floor has `D=1`, but solving the floor target inside block `22` requires radius

\[
\nu=5.
\]

However the common derivative value `2` is already reachable at global radius `2`. Its Wronskian has absorption redundancy `2`, so

\[
\boxed{\mu=2<\nu=5.}
\]

This recovers the squarefree access-delay/Pareto phenomenon using only block-value reachability.

### `25+704=729`

The relation spans four fine prime coordinates. The compressed solver gives

\[
\boxed{\mu=6=\nu,}
\]

with no prime-coordinate cube enumeration in the `mu` computation.

## 8. Architecture consequence

The two principal access coordinates now have complementary compressed forms:

\[
\boxed{
\begin{array}{ll}
\mu &: \text{first escape of }\mathcal R_r\text{ from }\Delta_{abc},\\
\nu &: \text{minimum of }K\text{ on the one-dimensional floor line }W=D.
\end{array}
}
\]

So the former is a growing two-dimensional reachable-set problem, while the latter is a one-dimensional level-set problem.

Both share the same three finite block access systems.

## 9. What remains hard

Stage 23 gives an exact finite solver but not yet a closed formula for `mu`.

Supplement 19 explains why a universal trivial formula should not be expected from block coefficients alone: arbitrary primitive positive rows occur as actual arithmetic blocks. Radius-one reachability already contains bounded signed subset-sum/factorization structure.

The useful next target is therefore not to guess a universal scalar formula, but to identify relation classes where the scaling-line escape can be certified by smaller summaries of the three block reachable sets.

## 10. Prior-art boundary

Linear image sets, dynamic set addition, integer proportionality under coprimality, and first-exit formulations are elementary/standard mathematics.

P025 does not claim these generic tools as new. The project-side result is the exact block-value compression of Pasten-style nondegeneracy and its integration with the finite precision/access architecture.

Historical novelty remains `NOVELTY_UNVERIFIED`.

## 11. Executable assets

Added:

- `src/enterprise_math/abc_block_mu.py`
  - exact block reachable derivative values;
  - compressed additive reachable sets;
  - exact scaling-line degeneracy test;
  - arbitrary-support exact `mu` solver using `nu` as finite upper bound.
- `tests/test_abc_block_mu.py`
  - scaling-line characterization;
  - `2+3=5`, `1+8=9`, tradeoff examples;
  - `1+22=23` strict `mu<nu`;
  - four-coordinate `25+704=729`;
  - comparison with the prior fine exact oracle on selected small cases.

## 12. Next frontier

No hard block exists. Continue with:

1. find task-minimal summaries of `V_n(r)` sufficient only for scaling-line escape;
2. derive exact `mu=1` and low-radius criteria for structured block families;
3. test whether reachable-value MAY/MUST or interval/hole summaries can replace full sets for selected relation classes;
4. combine `mu` escape and `nu` floor-line data into a compressed exact Pareto-frontier solver;
5. generalize from one Wronskian nondegeneracy condition to several simultaneous certificate forms.
