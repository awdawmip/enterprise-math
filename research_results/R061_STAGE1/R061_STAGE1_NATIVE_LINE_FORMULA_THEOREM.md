# R061 Stage 1 — Corrected Native Line Formula Theorem

Task-ID: `RS-R061-STAGE1-NATIVE-LINE-TRACE-FIBER-ORIGIN-AFFINE-REALIZATION`  
Researcher-ID: `EM-R061S1-4183C1`

## Final formula

For a fixed native right sector `S_ij`, define

`D_N={(a,b) in N_0^2 : a^2+b^2=N}`,

and

`T_{a,b}^{(ij)}=[X_i^a X_j^b]`

under `X_i X_j ~ X_j X_i`.

Let `Sigma_O^(ij)` be the unique origin-to-sector-anchor incidence, and define the affine cell chart

`C_ij(a,b)=C_ij(0,0)+a t_i+b t_j`.

Then

`Realize_E(T_{a,b}^{(ij)})`

is the set of all single-cell trajectories

`Sigma_O^(ij) ; w`,

where

`w in Lin(T_{a,b}^{(ij)})=Sh_{a,b}(X_i,X_j)`.

The typed endpoint is

`END_E^(ij)(a,b)=(V_ij(a,b),C_ij(a,b))`.

The corrected sector-local native line formula is

`LINE_E^(ij)(N)`

`= disjoint_union_{(a,b) in D_N} Realize_E(T_{a,b}^{(ij)})`.

## Why this is not Pi_cell = identity

At the free-word level no positive-axis shuffle word is rejected after the sector start cell is fixed.

But the native realization map is not the identity because it performs required type-changing structure:

1. `Sigma_O^(ij)` selects the unique sector-local incident cell;
2. formal prefix counts are interpreted in the affine center chart;
3. the terminal object is typed as `(coordinate vertex, terminal cell)`;
4. line identity is the component trace, not merely the carrier endpoint.

Thus the correct statement is:

`Pi_cell` is identity **on the already typed positive-axis word body**, while `Realize_E` is a nontrivial typed realization functor/operator.

## Fiber cardinality

For one coordinate branch:

`|Realize_E(T_{a,b}^{(ij)})|=binom(a+b,a)`.

The start incidence does not multiply the count in a fixed sector because the sector anchor is unique.

For a physical axis identity, two adjacent sector charts yield two distinct chart-local trajectories; the identity is deduplicated under global axis gluing while both trajectories are retained.

## N=25 exact answer

The coordinate fiber is

`D_25={(0,5),(3,4),(4,3),(5,0)}`.

The nondegenerate `3-4-5` branch is

`(3,4)` with

`L_E^2=3^2+4^2=25`, `L_E=5`.

Its native line identity is

`T_{3,4}^{(ij)}`.

Its exact native line-path count is

`binom(7,3)=35`.

An exact path ID is the set of positions occupied by `X_i` in a seven-letter word:

`ID(S)=S_ij-T3-4-XPOS-S`, `S subset {1,...,7}`, `|S|=3`.

The 35 IDs are therefore represented exactly by the 35 three-element subsets of `{1,...,7}`. The machine-readable exact-example file lists them explicitly for `S_12`.

The swapped branch `(4,3)` also has `35` representatives. Each axis branch has one sector-local representative. Hence one fixed sector has

`1+35+35+1=72`

native line-path representatives at `N=25` across all four coordinate branches.

Same-endpoint routes containing reverse-third-family carrier moves are omitted because they are not linearizations of the native `ij` component trace, not because their jump count is different.

## N=0

`D_0={(0,0)}`.

`T_{0,0}` has one empty linearization.

The realization is the typed origin incidence with zero center transitions. The line identity has native length zero at `O_E`; no cell is identified with `O_E`.

## Nonrepresentable N

If `D_N=empty`, then

`LINE_E^(ij)(N)=empty`

at the integer-center/vertex endpoint level. No path is invented.

## Three-sector covariance

The same formula holds under cyclic relabeling for `S_12,S_23,S_31`.

Global gluing deduplicates physical axis line identities by `(axis label, radial component)` while retaining distinct chart-local trajectory realizations from the two adjacent sector anchors.

## Acceptance

`NATIVE_LINE_PATH_FIBER_IS_EXACTLY_TYPED_AND_ALGEBRAICALLY_GENERABLE = true`.

`NATIVE_LINE_PATH_FIBER_DERIVABLE_FROM_CURRENT_FOUNDATION = true`.

This result preserves the Stage 0 exact coordinate and shuffle theorems and supplies the previously missing native realization layer.
