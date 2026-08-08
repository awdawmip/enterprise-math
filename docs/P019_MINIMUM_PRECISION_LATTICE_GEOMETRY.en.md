# P019 — Minimum-Precision Lattice Geometry and Distance Carry

Status: `RESEARCH WIP`  
Scope: integer-only discrete geometry, collapse, finite-precision distance  
External prior art: being mapped in Issue #43; this branch makes no priority claim

## 1. Starting problem

If state `1` represents both a numerical unit and an indivisible minimum resolution, it cannot automatically be interpreted as a "small cube." Simple-cubic / hypercubic structure is only one possible gluing rule and privileges a small set of coordinate directions at the base layer.

The problem therefore separates into two layers:

1. **value layer**: `1` remains the same integer state `1` in every dimension;
2. **relation layer**: dimension and relative geometry are determined by the allowed discrete relations among unit states.

This branch does not assert that physical space is any particular lattice. The goal is to find integer-only tools that let minimum resolution, relative distance, directional richness, dimension lifting, and collapse be studied in one finite framework.

## 2. Working lattice: `A_p`

For integer `p>=1`, define

\[
A_p=\left\{x=(x_0,\ldots,x_p)\in\mathbb Z^{p+1}:\sum_{i=0}^p x_i=0\right\}.
\]

`A_p` uses `p+1` integer coordinates but one zero-sum constraint, so its intrinsic rank is `p`.

Define the primitive moves

\[
e_i-e_j,\qquad i\ne j.
\]

A primitive move transfers one integer unit from slot `j` to slot `i`.

The number of primitive moves is

\[
z_p=p(p+1),
\]

because there are `p+1` choices for the source slot and `p` distinct choices for the target slot.

The low-dimensional working models are:

- `A_1`: the integer chain;
- `A_2`: triangular adjacency;
- `A_3`: the FCC-type root lattice;
- higher dimensions continue the same zero-sum integer rule.

These identifications are working discrete structures, not theorems identifying physical space.

## 3. P019-T01 — Integer closed form for primitive graph distance

For `x,y in A_p`, let

\[
u=x-y.
\]

Define primitive graph distance as the minimum number of primitive moves required to go from `x` to `y`.

Because

\[
\sum_i u_i=0,
\]

the total positive coordinate mass equals the absolute total negative mass. Every primitive move transfers exactly one unit from a negative deficit to a positive surplus. Therefore

\[
\boxed{
 d_G(x,y)=\sum_{u_i>0}u_i
 =\frac12\sum_i|u_i|
 }
\]

holds.

The `/2` does not require hidden fractions: for a zero-sum integer vector, `sum |u_i|` is even, so the reference implementation uses integer division.

Thus `d_G` is an exact natural-valued metric: nonnegative, separating, symmetric, and triangle-subadditive.

## 4. P019-T02 — Integer quadratic separation

Define

\[
q_p(x,y)=\frac12\sum_i(x_i-y_i)^2.
\]

For every integer `m`,

\[
m^2\equiv m\pmod2.
\]

The coordinates of `x-y` sum to zero, hence the square sum is even. Therefore

\[
\boxed{q_p(x,y)\in\mathbb N_0}
\]

without floating point or true division.

Every primitive root `e_i-e_j` has

\[
q_p=1.
\]

`q_p` is not called a metric; squared separation generally fails the triangle inequality. It is an **integer radial separation observable**, complementary to the path/reachability metric `d_G`.

## 5. P019-T03 — Distance itself obeys square-root collapse

Reuse the existing exact integer root and define

\[
D_p(x,y)=R_2(q_p(x,y)).
\]

Then

\[
D_p(x,y)=k
\iff
k^2\le q_p(x,y)<(k+1)^2.
\]

Therefore, if `1` is the minimum distinguishable distance, **distance 1 is not only the shortest contact shell `q=1`**. It is the entire square-collapse basin

\[
1\le q_p<4.
\]

Thus directions with `q=1,2,3` are all observed as the same integer distance `1` at the present resolution.

This yields a core mechanism: **directional richness can arise automatically from distance collapse instead of being patched into the lattice afterward.**

## 6. P019-T04 — Exact size of the first precision-distance shell

Define

\[
U_p=\#\{v\in A_p\setminus\{0\}:D_p(0,v)=1\}.
\]

This is equivalent to counting `q=1,2,3`. Let `n=p+1`.

### `q=1`

The square sum is `2`; the only pattern is

\[
(+1,-1),
\]

so the count is

\[
p(p+1).
\]

### `q=2`

The square sum is `4` and the coordinate sum is zero. The only pattern is two `+1` entries and two `-1` entries, giving

\[
6\binom{p+1}{4}.
\]

### `q=3`

The square sum is `6` and the coordinate sum is zero. There are two pattern classes:

1. `(+2,-1,-1)` and its global negative: `6 binom(p+1,3)`;
2. three `+1` entries and three `-1` entries: `20 binom(p+1,6)`.

Hence

\[
\boxed{
U_p=
 p(p+1)
 +6\binom{p+1}{4}
 +6\binom{p+1}{3}
 +20\binom{p+1}{6}
}
\]

and the first five intrinsic dimensions give

\[
\boxed{2,\ 12,\ 42,\ 110,\ 260}.
\]

In particular:

- `A_2` has `6` primitive nearest neighbors but `12` states in its minimum-precision distance shell;
- `A_3/FCC` has `12` primitive nearest neighbors but `42` states in its minimum-precision distance shell.

Thus the statement "FCC has 12 nearest neighbors" is not the full distance-1 information in a finite-precision theory.

## 7. Simple cubic is not logically eliminated at the first step

The same result weakens the overly strong claim that minimum resolution by itself forces FCC/HCP.

On `Z^p`, take the integer square separation

\[
q_{SC}(x,y)=\sum_i(x_i-y_i)^2
\]

and apply the same `R_2`. Again `q=1,2,3` all collapse to distance `1`.

The first precision-shell count is

\[
U_p^{SC}
=2p+4\binom p2+8\binom p3.
\]

In three dimensions,

\[
U_3^{SC}=26.
\]

So the traditional six-neighbor simple-cubic graph automatically expands to a 26-neighbor distance-1 shell after finite-precision distance collapse.

The conclusion is not that SC is correct. It is that **lattices must be compared after distance collapse, not rejected solely from their uncollapsed traditional nearest-neighbor counts.**

## 8. P019-T05 — Every fixed-`q` shell has exact second-order directional balance

Let

\[
X_{p,m}=\{v\in A_p:q_p(0,v)=m\}.
\]

Whenever nonempty, this shell is closed under coordinate permutations and global negation.

For

\[
M=\sum_{v\in X_{p,m}} vv^T,
\]

permutation symmetry forces all diagonal entries to agree and all off-diagonal entries to agree. Since every `v` is orthogonal to the all-ones vector, `M` acts as a scalar multiple of the identity on the zero-sum subspace.

For every zero-sum integer vector `x`, this can be written as the integer identity

\[
\boxed{
 p\sum_{v\in X_{p,m}}(v\cdot x)^2
 =2m\,|X_{p,m}|\sum_i x_i^2
 }
\]

Therefore every complete `q` shell has **no preferred direction at second-moment order**.

The `D=1` shell is the union of the complete `q=1,2,3` shells, so it inherits the same second-order balance.

This does not imply full rotational symmetry; fourth and higher directional moments may still retain lattice anisotropy. It does show that precision-distance collapse enriches directions on a strictly symmetric integer shell structure rather than by an arbitrary neighborhood patch.

## 9. P019-T06 — Collapsed radial distance has at most one unit of triangle defect

`D_p` is not a traditional metric, but failure of its triangle inequality is bounded by exactly **one minimum-resolution unit**.

Let

\[
u=x-y,\qquad v=y-z,
\]

and write

\[
r=D_p(x,y),\qquad s=D_p(y,z).
\]

From the integer-root basins,

\[
q(u)<(r+1)^2,\qquad q(v)<(s+1)^2.
\]

Use the integer Lagrange identity

\[
\left(\sum_i u_i^2\right)
\left(\sum_i v_i^2\right)
-
\left(\sum_i u_i v_i\right)^2
=
\sum_{i<j}(u_iv_j-u_jv_i)^2
\ge0.
\]

Because `sum u_i^2=2q(u)` and `sum v_i^2=2q(v)`, this gives

\[
\left(\sum_i u_iv_i\right)^2\le4q(u)q(v).
\]

Together with

\[
q(u+v)=q(u)+q(v)+\sum_i u_iv_i,
\]

pure integer inequalities imply

\[
q(u+v)<(r+s+2)^2.
\]

Hence

\[
\boxed{
D_p(x,z)\le D_p(x,y)+D_p(y,z)+1.
}
\]

## 10. P019-T07 — The `+1` defect is sharp and is an exact distance carry

In `A_2`, take

\[
a=(-2,0,2),\quad
b=(-1,1,0),\quad
c=(0,2,-2).
\]

Then

\[
q(a,b)=q(b,c)=3,
\]

so

\[
D(a,b)=D(b,c)=1.
\]

But

\[
q(a,c)=12,
\]

and therefore

\[
D(a,c)=3.
\]

Thus

\[
3=1+1+1.
\]

The traditional triangle inequality misses by exactly one minimum-resolution unit, so the previous `+1` cannot generally be removed.

Define the positive defect

\[
\kappa(x,y,z)=
\max\{0,D(x,z)-D(x,y)-D(y,z)\}.
\]

Then

\[
\boxed{\kappa\in\{0,1\}}.
\]

Further let

\[
b=\sum_i(x_i-y_i)(y_i-z_i).
\]

Since

\[
q(x,z)=q(x,y)+q(y,z)+b,
\]

and `D(x,z)` is already known to be at most `r+s+1`, the exact criterion is

\[
\boxed{
\kappa=1
\iff
q(x,y)+q(y,z)+b\ge(r+s+1)^2.
}
\]

This naturally connects to the project's basin-carry theme: finite precision does not repair triangle relations with hidden fractions; crossing the next distance basin is retained as an explicit integer carry.

## 11. Primitive graph metric and collapsed radial distance should not replace each other

The current proposal keeps two observables together:

\[
\rho_p(x,y)=\bigl(d_G(x,y),D_p(x,y)\bigr).
\]

- `d_G`: a strict metric measuring minimum relation steps;
- `D_p`: radial finite-precision distance obeying square-root collapse and an exact `0/1` triangle carry.

Keeping only `d_G` risks treating the polyhedral norm induced by a fixed finite direction set as the whole distance structure. Keeping only `D_p` loses the strict traditional triangle law.

The pair is more faithful to the current research goal than selecting a continuous Euclidean distance first and rounding it afterward.

## 12. P019-T08 — Integer counts for primitive `A_p` shells and balls

Define

\[
S_p(r)=\#\{x\in A_p:d_G(0,x)=r\},
\qquad S_p(0)=1.
\]

The working formula is

\[
H_p(t)=\sum_{j=0}^p\binom pj^2t^j,
\]

with coefficient form

\[
\boxed{
S_p(r)=
\sum_{j=0}^{\min(p,r)}
\binom pj^2
\binom{r-j+p-1}{p-1}.
}
\]

For `r>=1`, the low-dimensional forms are

\[
S_1(r)=2,
\]

\[
S_2(r)=6r,
\]

\[
S_3(r)=10r^2+2.
\]

Thus the primitive `A_3/FCC` graph shells are

\[
1,12,42,92,162,252,\ldots
\]

Define the closed ball

\[
V_p(r)=\sum_{s=0}^rS_p(s).
\]

It has the finite integer formula

\[
\boxed{
V_p(r)=
\sum_{j=0}^{\min(p,r)}
\binom pj^2
\binom{r-j+p}{p}.
}
\]

In particular

\[
V_p(0)=1
\]

for every `p`: a centered minimum-precision state still counts as exactly `1` in every dimension.

## 13. P019-T09 — Geometric growth laws plug directly into the existing collapse skeleton

Abstract the current perfect-power growth law

\[
V(k)=k^p
\]

to any strictly increasing integer function

\[
V:\mathbb N_0\to\mathbb N_0.
\]

Define

\[
R_V(n)=\max\{r:V(r)\le n\},
\]

\[
C_V(n)=V(R_V(n)).
\]

By definition,

\[
V(r)\le n\iff r\le R_V(n).
\]

This is the same order-adjoint pattern as P008, so `C_V` is automatically:

- reductive;
- monotone;
- idempotent.

For the primitive `A_p` graph ball, use the preceding `V_p(r)` and define

\[
R_p^A(n)=\max\{r:V_p(r)\le n\},
\]

\[
C_p^A(n)=V_p(R_p^A(n)).
\]

Its basin width is exactly the next primitive shell:

\[
\boxed{
\Delta_p^A(r)=V_p(r+1)-V_p(r)=S_p(r+1).
}
\]

Thus this research line **does not require a second collapse algebra**. Geometry only supplies an integer growth embedding; the existing P008 skeleton remains reusable.

## 14. Open risks

1. It is not proved that `A_p` is preferable to SC, `A_p^*`, HCP-type multi-basis structures, or another discrete family as the minimum-precision relation geometry.
2. FCC and HCP have rich first contact neighborhoods but differ in higher shells, periodic structure, and dimensional recursion; they must be pressure-tested separately.
3. A fixed finite direction set can have exact second-order balance without having all higher-order directional symmetries.
4. Whether the additive-one triangle carry of `D_p` should become a basic axiom of finite-precision distance requires more closure and counterexample work.
5. It is not yet settled which of `d_G`, `D_p`, and `q_p` belong to the mathematical ontology and which should remain tool observables.
6. Root-lattice growth formulas have mature prior art. Source-registry / lineage mapping must be completed before merge; this branch makes no originality claim.

## 15. Current conclusion

The main result is not "space is FCC."

The more robust conclusion is:

> **If `1` is minimum resolution, relative distance itself must also undergo collapse. A lattice's traditional nearest-neighbor shell is only fine structure; the actual distance-1 class is determined by the distance-collapse basin.**

In the `A_p` working model, this expands the `A_3/FCC` primitive neighborhood from 12 states to 42 finite-precision unit-distance states and produces an exact, sharp triangle carry bounded by one unit.

This gives Enterprise Math a new tool interface:

\[
\text{integer relation lattice}
\to q
\to R_2(q)
\to \text{finite-precision distance basin}
\to \text{explicit distance carry}.
\]

Every step uses only integers, finite sums, squaring, comparison, and integer roots.
