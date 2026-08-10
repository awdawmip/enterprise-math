# P025 Supplement 93 — Ferrers Precision Boundary and Dual Orbit Coordinates

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-orbit-normal-stage91`  
Depends on: P025 Supplement 92  
Hard block: `NONE`

## 1. The staircase has a dual coordinate system

Stage 92 represents the multi-threshold activation matrix by threshold-centric crossing depths

\[
0\le j_1\le\cdots\le j_s\le\infty.
\]

The same matrix also has a natural node-centric representation.

For each dyadic depth `j`, define

\[
\boxed{
r_j:=\#\{k:\rho_j\ge T_k\}.}
\]

Thus `r_j` is the number of declared threshold levels already reached at orbit node `j`.

## 2. P025-T216 — node ranks are monotone

Because

\[
\rho_j\le\rho_{j+1},
\]

every threshold reached at node `j` remains reached at node `j+1`. Therefore

\[
\boxed{
0\le r_0\le r_1\le\cdots\le r_h\le s.
}
\]

So the node-centric precision state is itself a monotone staircase.

## 3. P025-T217 — crossing/rank duality

A threshold `T_k` has been reached by node `j` exactly when its crossing depth is at most `j`. Hence

\[
\boxed{
r_j=\#\{k:j_k\le j\}.}
\]

Conversely, threshold `k` first becomes active at the first node whose rank has reached at least `k`:

\[
\boxed{
j_k=\min\{j:r_j\ge k\},}
\]

with `j_k=infinity` when no such node exists.

Therefore

\[
\boxed{
(j_1,\ldots,j_s)
\longleftrightarrow
(r_0,\ldots,r_h)
}
\]

is an exact bijection.

Neither coordinate is intrinsically more informative. They are dual views of the same finite semantic quotient.

## 4. P025-T218 — column-prefix form

Because the thresholds are ordered,

\[
T_1<\cdots<T_s,
\]

if node `j` reaches threshold `T_k`, it has reached every lower threshold as well.

Thus column `j` of the activation matrix is

\[
\boxed{
(\underbrace{1,\ldots,1}_{r_j},
\underbrace{0,\ldots,0}_{s-r_j})^\top.
}
\]

So Stage 92's row-suffix theorem and Stage 93's column-prefix theorem are exact dual descriptions of the same monotone matrix.

## 5. P025-D37 — Ferrers precision region

Regard the activation matrix as an `s x (h+1)` grid and mark a cell `(k,j)` when

\[
B_{k,j}=1.
\]

The marked cells form a monotone Ferrers-type region:

- each row is a suffix in the orbit direction;
- each column is a prefix in the threshold direction.

The entire finite precision state is therefore the boundary separating inactive from active cells.

## 6. P025-T219 — lattice-path encoding

Encode the boundary by a monotone lattice path with

\[
h+1
\]

horizontal steps `H` and

\[
s
\]

vertical steps `V`.

Given node ranks, start at height zero. Before horizontal step `j`, take enough vertical steps to reach height `r_j`; after the last orbit node, take the remaining vertical steps up to `s`.

This produces a word of length

\[
\boxed{h+s+1}
\]

containing exactly `h+1` symbols `H` and `s` symbols `V`.

Conversely the number of preceding vertical steps at each horizontal step recovers `r_j`.

Hence

\[
\boxed{
\text{crossing staircase}
\longleftrightarrow
\text{node-rank staircase}
\longleftrightarrow
\text{monotone lattice path}.
}
\]

The Stage-92 state count

\[
\binom{h+s+1}{s}
\]

is exactly the number of such lattice paths.

## 7. Exact working boundary

For the Stage-92 fixture

\[
(j_k)=(0,1,2,\infty),
\]

the dual node ranks are

\[
\boxed{(r_j)=(1,2,3,3).}
\]

The corresponding boundary word is

\[
\boxed{\texttt{VHVHVHHV}.}
\]

This one word encodes the full matrix

\[
\begin{pmatrix}
1&1&1&1\\
0&1&1&1\\
0&0&1&1\\
0&0&0&0
\end{pmatrix}.
\]

## 8. P025-D38 — activation area

Define the activation area

\[
\boxed{
A:=\sum_{k=1}^s\sum_{j=0}^hB_{k,j}.
}
\]

It is the number of reached threshold/node pairs in the declared finite future grid.

By column counting,

\[
\boxed{A=\sum_{j=0}^h r_j.}
\]

By row counting, threshold `k` contributes

\[
h+1-j_k
\]

active cells when `j_k` is finite and zero otherwise. Therefore

\[
\boxed{
A
=
\sum_{k:j_k<\infty}(h+1-j_k).
}
\]

Hence

\[
\boxed{
\sum_j r_j
=
\sum_{k:j_k<\infty}(h+1-j_k).
}
\]

This is the exact Ferrers area double-count identity.

## 9. Working area calibration

For

\[
(j_k)=(0,1,2,\infty),
\]

the row count gives

\[
A=4+3+2=9.
\]

The node ranks give

\[
A=1+2+3+3=9.
\]

The `4 x 4` grid therefore has active area `9` and inactive complement area `7`.

For the plateau staircase

\[
(1,2,2,\infty),
\]

the ranks are

\[
(0,1,3,3)
\]

and the active area is `7`.

## 10. Two coordinates serve different future operations

The crossing-depth representation is threshold-centric: it answers naturally

> when does threshold `T_k` first become true?

The node-rank representation is orbit-centric: it answers naturally

> how many declared precision levels have been reached at node `j`?

They are semantically equivalent but operationally different.

This distinction becomes important when the future query extends the threshold grid or extends the orbit horizon.

## 11. Precision-boundary interpretation

The finite state is no longer best viewed as a table. It is a boundary in a product of two ordered finite axes:

\[
\boxed{
\text{threshold precision}
\times
\text{orbit depth}.
}
\]

All cells on one side of the boundary are inactive, and all cells on the other side are active.

Thus the semantic information is geometrically localized to a monotone boundary rather than spread independently over the product grid.

This is an exact number-theoretic instance of a finite precision boundary geometry.

## 12. Prior-art / novelty discipline

Ferrers diagrams, conjugate partitions, monotone lattice paths and area double counting are classical/general mathematics.

P025 claims none of these concepts in isolation.

The project-side result is the exact dual boundary representation induced by the dyadic projective-pressure theorem and the corresponding finite precision interpretation. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 13. Executable assets

Added:

- `src/enterprise_math/abc_dyadic_ferrers_boundary.py`;
- `tests/test_abc_dyadic_ferrers_boundary.py`.

The executable layer verifies crossing/rank duality, path encode/decode, exact boundary words, plateau geometry and the area identity.

## 14. Next frontier

No hard block exists. Continue with:

1. compare incremental update cost when adding one threshold versus adding one orbit node;
2. prove which dual coordinate admits local append-only update for each extension direction;
3. define a representation-switch rule rather than one globally preferred coordinate;
4. investigate mixed extensions where both threshold precision and orbit horizon grow;
5. feed the resulting coordinate-choice law back to P023/A2 as a theorem-backed precision compiler pattern.
