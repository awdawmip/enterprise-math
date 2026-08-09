# P019 Supplement 13 — Legal Integer Sublattices and Indices of Contraction Charts

Status: `RESEARCH WIP / EXACT INTEGER INDEX THEOREM PROVED`

## 1. Problem

The local reassociation formulas in Supplement 12 contain exact divisions such as `//(m+n)`.

This needs a structural explanation:

- why are legal relation states always divisible as required?
- where do legal `z` coordinates sit inside ambient `Z^(N-1)`?
- why may a tree rotation have a rational determinant different from `±1` and still be a bijection between legal integer states?

This supplement unifies these questions in a chart-lattice index theorem.

## 2. Fixed-root-total chart map

Take a rooted ordered binary tree `T` with `N` labeled unit leaves and fix

\[
\sum_{i=1}^N x_i=c.
\]

The fine-state lattice therefore has `N-1` free integer coordinates.

At each internal node `v`, let left and right child sizes be `m_v,n_v`, totals `a_v,b_v`, and `|v|=m_v+n_v`. Define

\[
\boxed{z_v=n_v a_v-m_v b_v.}
\]

There are exactly `N-1` internal nodes, so this gives a chart map

\[
\Phi_T:\{x\in\mathbb Z^N:\sum x_i=c\}
\to\mathbb Z^{N-1}.
\]

## 3. One-step legality congruence

At one internal node, parent total is

\[
c_v=a_v+b_v.
\]

Since

\[
z_v=(m_v+n_v)a_v-m_vc_v,
\]

we have

\[
\boxed{z_v\equiv -m_vc_v\pmod{|v|}.}
\]

Conversely, if this congruence holds, the child totals are uniquely integral:

\[
a_v=(m_vc_v+z_v)//|v|,
\qquad
b_v=c_v-a_v.
\]

Thus whole-tree legality is a recursive triangular congruence system: start from the root total and check one modulus `|v|` at each node.

## 4. P019-X33 — Legal imbalance states form an affine sublattice

For fixed `T` and root total `c`, all legal tag tuples `z_T` form an affine lattice coset in `Z^(N-1)`, denoted

\[
L_T(c).
\]

Changing `c` may translate the coset but does not change its lattice index.

## 5. P019-X34 — Chart index equals the product of internal block sizes

Define

\[
\boxed{I(T)=[\mathbb Z^{N-1}:L_T(c)].}
\]

Then

\[
\boxed{
I(T)=
\prod_{v\in\operatorname{Internal}(T)}|v|.
}
\]

### Recursive proof

A one-leaf tree has no free coordinates and index one.

Let the root subtrees have sizes `m,n`, with `N=m+n`. At fixed root total `c`, changing the left subtree total `a` by one changes the root imbalance

\[
z=Na-mc
\]

by exactly `N`. Thus the root congruence contributes index `N` in the ambient root-tag coordinate.

After child totals are fixed, the internal charts contribute `I(T_L)` and `I(T_R)`. Hence

\[
I(T)=N I(T_L)I(T_R).
\]

Induction yields the product of all internal subtree sizes. ∎

## 6. Low-dimensional examples

For the four-slot chain

\[
T=(((1,1),1),1),
\]

internal sizes are `2,3,4`, so

\[
\boxed{I(T)=24.}
\]

For the balanced tree

\[
T=((1,1),(1,1)),
\]

internal sizes are `2,2,4`, so

\[
\boxed{I(T)=16.}
\]

Direct fixed-root-total imbalance chart matrices have determinant magnitudes `24` and `16`, respectively.

## 7. P019-X35 — Local rotation determinant matches the chart-index ratio

For the Supplement 12 rotation

\[
((A_m,B_n),C_k)
\longleftrightarrow
(A_m,(B_n,C_k)),
\]

the local tag transform is

\[
\begin{pmatrix}u'\\v'\end{pmatrix}
=
\frac1{m+n}
\begin{pmatrix}
-k & n\\
m+n+k & m
\end{pmatrix}
\begin{pmatrix}u\\v\end{pmatrix}.
\]

Its ambient rational determinant is

\[
\boxed{-\frac{n+k}{m+n}.}
\]

Before and after the rotation, the only changed internal block size is `m+n` versus `n+k`. Therefore

\[
\boxed{
|\det R|=\frac{I(T')}{I(T)}.
}
\]

The transform is therefore not expected to preserve all of ambient `Z^2`; it maps the legal lattice of index `I(T)` bijectively to the legal lattice of index `I(T')`.

This explains the automatic exact divisibility in the reassociation formulas.

## 8. Prior-art boundary: tree factorial

Products of rooted-subtree sizes are established in combinatorics/B-series under tree-factorial-style terminology.

Therefore the product

\[
\prod_v|v|
\]

itself is not an originality claim of P019.

The P019 research question is its role as the legal-sublattice index of fixed-root-total imbalance coordinates and its exact match to reassociation denominators/determinants.

Formal source and lineage registration is required before promotion.

## 9. P019-X36 — Chain-chart index is `N!`

A full chain/comb tree has internal sizes

\[
2,3,\ldots,N,
\]

so

\[
\boxed{I(T_{chain})=N!.}
\]

More generally, every `N`-leaf binary tree satisfies

\[
\boxed{I(T)\le N!.}
\]

Proof by induction. If the root split is `m+n=N`, then

\[
I(T)=N I(T_L)I(T_R)
\le N m!n!
\le N(N-1)!=N!.
\]

The chain split `1+(N-1)` reaches equality recursively. ∎

## 10. Balanced charts can have much smaller indices

For `N=2^h` and a perfectly balanced tree, blocks of size `2^j` occur `N/2^j` times. Thus

\[
I(T_{balanced})
=
\prod_{j=1}^h(2^j)^{N/2^j}.
\]

Since

\[
\sum_{j=1}^h\frac{jN}{2^j}=2N-h-2,
\]

we obtain

\[
\boxed{
I(T_{balanced})=2^{2N-h-2}.
}
\]

Examples:

- `N=4`: `16`;
- `N=8`: `2048`;
- `N=16`: `2^26`.

This can be dramatically smaller than the chain index `N!`.

This supplement does not yet claim that a perfectly balanced tree is the global minimizer for every `N`; chart-index minimization is left as a separate problem.

## 11. Computational meaning

If a tree is only a current-state representation chart rather than actual history, the atlas may choose a computationally favorable chart.

Candidate objectives include:

- smaller chart index;
- smaller imbalance-tag ranges;
- more local future operations;
- easier automorphism quotients.

Contraction Atlas may therefore support adaptive integer-coordinate selection, not merely theoretical equivalence.

## 12. Implementation and validation

Added:

- `src/enterprise_math/contraction_atlas.py`
  - `tree_leaves`
  - `tree_size`
  - `internal_block_sizes`
  - `chart_index_product`
  - `imbalance_tags`
  - `chart_matrix`
  - `chart_determinant`
  - `chart_index_identity`
- `tests/test_contraction_atlas.py`

All ordered binary tree shapes preserving leaf order were enumerated through `N=6`; direct exact integer determinants satisfy

\[
|\det(\Phi_T)|
=
\prod_{v\in Internal(T)}|v|.
\]

## 13. Next steps

1. rigorously classify the chart-index minimization problem instead of assuming balance;
2. test whether chart index correlates with actual `z` bit length and future-quotient complexity;
3. turn local rotation into an atlas-routing algorithm that selects lower-cost charts dynamically;
4. test whether dynamic chart changes significantly compress traces when process history is not queried;
5. complete the tree-factorial/B-series prior-art map and separate established invariants from the P019 chart-lattice application.
