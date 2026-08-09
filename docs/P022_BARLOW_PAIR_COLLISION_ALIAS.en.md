# P022 — Pair-Collision Aliasing of Barlow Checkpoint Geometry

Status: `ACTIVE RESEARCH NOTE / EXACT COUNTEREXAMPLE / PRIOR-ART SENSITIVE`  
Owner: `program/p022-geometry-v2`  
Depends on: P011 `J_2`; P022 checkpoint fiber convolution

## 1. Question

For a final-observing schedule with segment lengths `ell_1,...,ell_m`, let

\[
B_n=\binom{2n}{n}.
\]

The ordered equal-observation pair moment is

\[
M_2=\prod_jB_{\ell_j},
\]

and, since the microscopic domain has size `2^N`,

\[
\boxed{J_2=\frac{M_2-2^N}{2}.}
\]

Does fixed total length `N`, fixed checkpoint count `m`, and exact `J_2` determine the segment-length multiset?

No.

## 2. P022-PA01 — first finite alias by total length

A complete finite search over positive segment multisets with fixed `(N,m)` finds no `M_2` alias for

\[
N\le20.
\]

At

\[
N=21,\qquad m=4,
\]

the two distinct multisets

\[
\boxed{(1,5,5,10)}
\]

and

\[
\boxed{(2,2,6,11)}
\]

satisfy

\[
\boxed{
B_1B_5^2B_{10}=B_2^2B_6B_{11}=23465490048.
}
\]

Hence both have

\[
\boxed{J_2=11731696448.}
\]

The bounded `N<=20` statement is an exhaustive finite result for this segment-multiset class; it is not a claim about unrelated observation systems.

## 3. Exact proof of the product identity

Use

\[
\frac{B_n}{B_{n-1}}=4-\frac2n.
\]

Then

\[
\frac{B_6}{B_5}=\frac{11}{3},
\qquad
\frac{B_{11}}{B_{10}}=\frac{42}{11}.
\]

Therefore

\[
\frac{B_2^2B_6B_{11}}{B_1B_5^2B_{10}}
=
\frac{36}{2\cdot252}
\cdot\frac{11}{3}
\cdot\frac{42}{11}
=1.
\]

No approximation is involved.

## 4. Higher information separates the two schedules

The complete fiber profiles differ.  In particular:

- image sizes are
  \[
  792\quad\text{and}\quad756;
  \]
- third collision counts are
  \[
  \boxed{64506690871040}
  \]
  and
  \[
  \boxed{70446056775360}.
  \]

So

\[
\boxed{
(N,m,J_2)\not\Rightarrow\text{segment multiset}.
}
\]

The failure is repaired already by additional higher-order information in this example.

## 5. Cleaner three-segment alias

A slightly later but algebraically compact example is

\[
(1,4,17)
\]

versus

\[
(2,2,18),
\]

with `N=22,m=3`.

They satisfy

\[
B_1B_4B_{17}=B_2^2B_{18}=326704870800,
\]

because

\[
\frac{B_{18}}{B_{17}}=\frac{35}{9}
\]

and

\[
\frac{B_2^2}{B_1B_4}\frac{B_{18}}{B_{17}}
=
\frac{36}{140}\frac{35}{9}=1.
\]

They have identical

\[
J_2=163350338248,
\]

but different image sizes `180` and `171` and different `J_3` values.

## 6. Precision consequence

Pair collision is a legitimate ambiguity statistic, but it is only one projection of the complete fiber geometry.

This exact alias proves:

> minimizing or matching `J_2` is not the same problem as identifying the quotient geometry.

That distinction is essential when a later future language can react to higher collision blocks, worst fibers, or the exact observation image.

The complete P011 collision polynomial avoids this alias in the Barlow specialization because the fiber-convolution theorem recovers the segment multiset and hidden tail from the full profile.

## 7. Executable assets

- `src/enterprise_math/p022_barlow_pair_collision_alias.py`;
- `tests/test_p022_barlow_pair_collision_alias.py`.

The tests preserve the exact identities, verify the different higher statistics, and exhaust all positive segment multisets with total length below 21 to establish the stated finite first-alias boundary.
