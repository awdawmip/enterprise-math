# P025 Supplement 30 — Matrix-Preimage Access as a Word Norm on the Derivative Image

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-shared-access-stage30`  
Base: frozen Stage-18–29 generation  
Depends on: P025 Supplement 28; intrinsic discrete-geometry language  
Hard block: `NONE`

## 1. The shared-prime access problem

Supplement 28 replaces independent block preimages by one joint integer matrix problem. Let

\[
B\in\mathbb Z^{m\times s}
\]

be the block-by-prime derivative coefficient matrix. For a block-value target

\[
t\in\operatorname{im}_{\mathbb Z}B,
\]

define exact joint access

\[
\boxed{
\kappa_B(t)
=
\min\{\|x\|_\infty:Bx=t\}.
}
\]

A generic response might invoke Smith/Hermite normal form or closest-vector machinery immediately. Before doing that, the `L_infinity` cube itself gives a stronger structural simplification.

## 2. P025-D17 — radius image sets

For every integer radius `r>=0`, define

\[
\boxed{
Z_r(B)
=
B\bigl([-r,r]^s\cap\mathbb Z^s\bigr).
}
\]

Then

\[
\boxed{
\kappa_B(t)=\min\{r:t\in Z_r(B)\}.
}
\]

The one-step image

\[
\boxed{S_B=Z_1(B)}
\]

is finite, symmetric, contains zero, and contains every signed matrix column. Hence it generates the whole image group

\[
\Gamma_B=\operatorname{im}_{\mathbb Z}B.
\]

## 3. P025-T84 — exact Minkowski radius law

For all nonnegative integers `r,s`,

\[
\boxed{
Z_{r+s}(B)=Z_r(B)+Z_s(B),
}
\]

where the right side is the finite Minkowski sum.

### Proof

If `y` has coordinate radius at most `r` and `z` at most `s`, then `y+z` has radius at most `r+s`, proving

\[
Z_r+Z_s\subseteq Z_{r+s}.
\]

Conversely take any

\[
x\in[-r-s,r+s]^s\cap\mathbb Z^s.
\]

Split each coordinate independently as

\[
x_i=y_i+z_i
\]

with

\[
|y_i|\le r,
\qquad
|z_i|\le s.
\]

For example clamp `x_i` to `[-r,r]` for `y_i` and place the remaining integer amount in `z_i`; because `|x_i|<=r+s`, the remainder has size at most `s`.

Then

\[
Bx=By+Bz,
\]

so `Z_(r+s)` is contained in the Minkowski sum. ∎

## 4. P025-T85 — access is exactly a finite-generator word norm

Taking `s=1` repeatedly in P025-T84 gives

\[
\boxed{
Z_r(B)
=
\underbrace{S_B+\cdots+S_B}_{r\text{ copies}}.
}
\]

Because zero lies in `S_B`, this is also the set of elements representable by at most `r` one-step generators.

Therefore

\[
\boxed{
\kappa_B(t)
=
|t|_{S_B},
}
\]

where the right side is the ordinary word length of the abelian group element `t` with respect to the finite symmetric generating set `S_B`.

Consequently:

\[
\boxed{
\begin{aligned}
\kappa_B(0)&=0,\\
\kappa_B(-t)&=\kappa_B(t),\\
\kappa_B(t+u)&\le\kappa_B(t)+\kappa_B(u).
\end{aligned}}
\]

So matrix-preimage access is not merely a search cost; it is an intrinsic integer metric/word-norm structure on the derivative image lattice.

### Prior-art boundary

Word metrics on finitely generated abelian groups, images of cubes, zonotopes, and Minkowski sums are standard mathematics. P025 does not claim them as new. The project-side point is the exact identification of arithmetic-derivative `L_infinity` preimage precision with this structure.

## 5. Dynamic image computation without cube enumeration

The set `Z_r(B)` can be constructed column by column.

If `b_j` is column `j`, then its radius-`r` contribution is the finite segment

\[
\{-r b_j,\ldots,0,\ldots,r b_j\}.
\]

Repeated Minkowski addition of those column segments merges duplicate image states immediately. Thus the executable reference enumerates derivative-image values, not all

\[
(2r+1)^s
\]

fine coordinate vectors.

The benefit depends on the rank/geometry of `B`; no universal polynomial complexity claim is made.

## 6. Shared-prime example `(4,8)`

The derivative matrix is

\[
B=
\begin{pmatrix}4\\12\end{pmatrix}.
\]

Hence

\[
S_B
=
\{(-4,-12),(0,0),(4,12)\}.
\]

Therefore

\[
\kappa_B(4,12)=1,
\qquad
\kappa_B(8,24)=2.
\]

The image group is one-dimensional even though two block values are reported, matching Supplement 28.

## 7. Shared-prime example `2,4,6`

Here

\[
B=
\begin{pmatrix}
1&0\\
4&0\\
3&2
\end{pmatrix}.
\]

The state

\[
(1,4,5)=B(1,1)
\]

has

\[
\kappa_B=1.
\]

The false separate-ideal state

\[
(0,4,4)
\]

is not in the image group at all, so no finite access radius exists. The word-norm formulation automatically excludes it.

## 8. P025-N12 — restriction to a relation subgroup is not generally an intrinsic radius-one word norm

Now impose the valid block relation

\[
\boxed{4\cdot2+1\cdot4-2\cdot6=0.}
\]

Thus

\[
L=(4,1,-2).
\]

For the derivative matrix above,

\[
\boxed{LB=(2,-4).}
\]

Fine relation-adapted coordinates satisfy

\[
x_2=2x_3.
\]

At radius one, the only relation-compatible fine coordinate is zero, so

\[
\boxed{Z_1(B)\cap\ker L=\{0\}.}
\]

But at radius two,

\[
x=(2,1)
\]

is relation-adapted and gives

\[
\boxed{t=(2,8,8),
\qquad\kappa_B(t)=2.}
\]

Hence the relation subgroup contains nonzero finite-access elements even though its intersection with the ambient one-step generator is trivial.

Therefore

\[
\boxed{
\kappa_B|_{\Gamma_B\cap\ker L}
\text{ need not equal the intrinsic word norm generated by }
S_B\cap\ker L.
}
\]

The reason is that an optimal ambient word decomposition may pass through one-step image elements that individually leave the relation subgroup and only cancel back into it in the final sum.

This is a precise future/composition boundary: restricting a valid ambient metric to a relation state is not the same operation as regenerating a metric from relation-compatible primitive steps.

## 9. Architecture consequence

The shared-prime access hierarchy is now

\[
\boxed{
\text{fine coordinate cube}
\xrightarrow{B}
\text{finite one-step image }S_B
\to
\text{word norm }\kappa_B
\to
\text{relation subgroup restriction}.
}
\]

Two geometries must remain distinct:

1. **ambient derivative-image access:** exact word norm from `S_B`;
2. **intrinsic relation-step geometry:** word norm, when defined, from relation-compatible primitive generators.

They can disagree dramatically. P025 must not silently replace one with the other.

## 10. Executable assets

Added on the Stage-30 owner:

- `src/enterprise_math/matrix_access_word_norm.py`
  - exact radius image sets;
  - Minkowski addition;
  - one-step/repeated-step image identity;
  - exact matrix access radius;
  - triangle regression;
  - relation-subgroup one-step failure counterexample.
- `tests/test_matrix_access_word_norm.py`
  - `(4,8)` one-dimensional image;
  - exact `Z_(r+s)=Z_r+Z_s` checks;
  - `2,4,6` false-state exclusion;
  - triangle inequality;
  - relation-subgroup failure boundary;
  - pairwise-coprime calibration.

## 11. Next frontier

No hard block exists. Continue with:

1. define the minimum relation-generator radius needed for `Z_R(B) intersect ker L` to generate the relation subgroup;
2. classify when ambient access restriction equals intrinsic relation-step word norm;
3. connect this boundary to A5/P012 intrinsic graph geometry without conflating metrics;
4. use HNF/SNF only where it shortens exact generator/access calculations rather than as an automatic replacement for the word-norm state;
5. relay the ambient-vs-intrinsic metric distinction to P023/A3/A5.
