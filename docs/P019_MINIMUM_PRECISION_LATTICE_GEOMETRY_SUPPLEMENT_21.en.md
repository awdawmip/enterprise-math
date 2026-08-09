# P019 Supplement 21 — Graph and Radial Ball Observables on the Relation Field

Status: `RESEARCH WIP / EXACT INTEGER IDENTITIES PROVED`

## 1. Goal

Graph and radial/collision-power balls already share the same weighted relation contraction. This supplement removes another coordinate dependence: the principal `s=1` and `s=2` ball observables can be read directly from the same weighted relation state.

## 2. P019-X71 — Graph radius is the maximum directed relation cut

For zero grand total, total capacity `M`, and any subset `S`, the weighted directed cut satisfies

\[
Z(S,S^c)=M C_S.
\]

The maximum occurs at the set of positive-total blocks, so

\[
\boxed{
M E_{\mathbf m}^{(1)}=2\max_S Z(S,S^c).
}
\]

For unit `A_p` states, `E^(1)=2d_G` and `M=N=p+1`, giving

\[
\boxed{N d_G(0,x)=\max_S Z(S,S^c).}
\]

Thus primitive graph radius is a max-cut observation of the relation field rather than an externally imposed axis geometry.

## 3. P019-X72 — Unit radial `q` is a squared relation-field observation

For unit blocks `Z_ij=d_ij=x_i-x_j`. Define

\[
P=\sum_{i<j}d_{ij}^2.
\]

On zero-sum `A_{N-1}` states,

\[
\boxed{P=2Nq,}
\qquad
\boxed{q=P//(2N).}
\]

The same relation field therefore supports graph radius through a maximum cut and radial `q` through an all-pair square sum.

## 4. Internal minimum pair dispersion of one coarse block

For capacity `m`, total `c`, and square-balanced internal unit slots,

\[
P_{internal}^{min}
=m\Psi_{m,2}(c)-c^2
=\varepsilon_m(c)
=r(m-r),
\]

where `r=|c| mod m`.

## 5. P019-X73 — Minimum cross-pair dispersion between two coarse blocks

For blocks `(m,a)` and `(n,b)` with weighted relation `Z=na-mb`, let `C_AB^min` be the sum of squared differences across all unit pairs after each block is internally balanced. Then

\[
\boxed{
mnC_{AB}^{min}
=n^2\varepsilon_m(a)
+m^2\varepsilon_n(b)
+Z^2.
}
\]

This follows by expanding the cross-pair square sum and substituting each block's internal pair dispersion.

## 6. P019-X74 — Tagged square energy is fully reconstructible from weighted relation geometry

Let

\[
P_{min}
=
\sum_i\varepsilon_{m_i}(c_i)
+
\sum_{i<j}C_{ij}^{min}.
\]

For zero grand total and total capacity `M`, the balanced expanded unit state satisfies

\[
\boxed{P_{min}=M E_{\mathbf m}^{(2)}.}
\]

Hence

\[
\boxed{E_{\mathbf m}^{(2)}=P_{min}//M.}
\]

All cross terms are reconstructed from capacities, bounded residues, and weighted relations. No hidden fine allocation has to be retained.

## 7. Unified relation-level picture

At `s=1`, ball membership is a max-directed-cut observation. At `s=2`, it is a minimum pair-dispersion observation reconstructed from squared weighted relations plus bounded block residues. The underlying weighted relation state is the same; graph/radial geometry is better understood as different integer observation channels on that state.

## 8. Implementation

Added `src/enterprise_math/relation_geometry.py`, `src/enterprise_math/weighted_relation_geometry.py`, and corresponding tests. The tests verify the max-cut identity, `P=2Nq`, the exact two-block cross formula, explicit balanced expansion, and relation-based reconstruction of square energy.

## 9. Prior-art boundary

Maximum cuts, graph-Laplacian quadratic forms, and pairwise-square/variance identities are established mathematics. P019 makes no priority claim for those tools. The research interface is their use on a finite-precision capacity-weighted relation state together with the same directional quotient theorem.
