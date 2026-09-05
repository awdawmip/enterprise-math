# X6 原生六轴坐标完成候选：全局 min-zero section、slice 投影与隐藏三轴

Status: `DERIVED_RESEARCH_CANDIDATE / EXACT_COORDINATE_COMPLETION / NOT_YET_P000_NATIVE_CELL_PROMOTION`
Date: `2026-09-05`
Research lane: `X6 native Cell/address construction`

## 0. Why this route

A type audit killed the previous attempt to identify the two chart-local Cell trajectories belonging to one shared native line axis. Current R061 proves only:

- one physical axis line identity is shared/deduplicated at the **line/component-trace observer**;
- the two adjacent-sector physical Cell trajectories remain distinct;
- local same-terminal / reverse-third relations live at the **slice Cell endpoint observer**.

Therefore full X6 must sit *above* slice Cell observations. Slice-local endpoint equality may be the shadow of a nontrivial full-state displacement in omitted coordinates.

The present construction generalizes the already accepted three-positive-coordinate min-zero section without identifying carrier chart trajectories at full-state level.

## 1. Six-axis derived displacement carrier

Let

`L6 = Z^6`

with standard six labeled native-axis component generators `e_1,...,e_6`.

Let

`Delta6 = Z*(1,1,1,1,1,1)`

and define the **derived six-axis displacement group**

`G6_D := Z^6 / Delta6`.

This is a derived endpoint/component object, exactly analogous in type to the accepted three-axis derived displacement quotient `G_D=Z^3/Z(1,1,1)`. It is not by itself primitive native Cell identity, and its ordinary abelian rank must not be used to rewrite P000 dimension.

Define

`can6(z)=z-min_i(z_i)*(1,...,1)`.

Then every class in `G6_D` has one unique representative in

`A6_D={n in N_0^6 : min_i n_i=0}`.

Proof is identical to the accepted 3-axis canonical-section proof: diagonal shifts preserve `can6`; equal canonical representatives differ by a diagonal vector; subtracting the minimum makes every integer tuple nonnegative with minimum zero.

## 2. Primitive/native address candidate is separately typed

Define a **candidate** primitive address type

`A6_E^cand`

with underlying set equal to `A6_D`, but keep semantic separation

`A6_E^cand != A6_D`.

This mirrors the current 3-axis rule `underlying_set(A_E)=underlying_set(A_D)` while `A_E != A_D` as semantic types.

Candidate principle:

`FULL_SIX_POSITIVE_AXIS_ADDRESS = ONE_NONNEGATIVE_MIN_ZERO_SIX_TUPLE`.

This is a native-completion proposal, not a proof from Packet/Path alone. It is motivated by exact recovery of every current 3-axis min-zero chart and by the direct P000 statement that the full spatial Cell state is six-axis coordinate state.

A concrete full Cell space should be affine/torsor-typed rather than identify the geometric origin with a Cell: choose a Cell anchor `c_*` only to coordinatize a homogeneous component. `O_E` remains a non-Cell triple-intersection event in each established 3-axis slice.

## 3. Canonical six-axis translations

On `A6_D` (and conditionally on `A6_E^cand`) define for each positive native axis i

`T_i(n)=can6(n+e_i)`.

Define path reversal by

`T_i^{-1}(n)=can6(n-e_i)`.

The inverse uses the same adjacency backwards; it is not a primitive native negative axis.

At the derived coordinate level:

- all `T_i` are bijections;
- `T_i T_j = T_j T_i`;
- `T_1 T_2 ... T_6 = identity`;
- the six positive generators are distinct;
- their six inverses are distinct and disjoint from the positive set;
- hence every state has 12 distinct directed coordinate-neighbour actions.

Important strength boundary: promoting these 12 derived coordinate transitions to actual native Cell adjacencies requires the native coordinate-completeness/translation lift. Pairwise Enterprise orthogonality fixes angle/norm semantics but does not by logic alone prove Cell recoalescence for the three currently untested opposite K4 axis pairs.

## 4. Every 3-of-6 native coordinate slice

For any 3-element subset `S subset {1,...,6}`, define

`G_S = Z^S / Z*1_S`

and canonical min-zero section `A_S`.

Define the slice observation

`pi_S : G6_D -> G_S`

by coordinate restriction:

`pi_S([z])=[z|_S]`.

It is well-defined because a global diagonal shift restricts to a local diagonal shift.

In canonical addresses:

`Obs_S(n)=can3((n_i)_{i in S})`.

There are `C(6,3)=20` such native axis-selection slices. The current FCC/K4 atlas exposes four especially convenient close-packed carrier slices; it is not the definition of the full native set of three-axis selections.

## 5. Exact visible/hidden translation law

For every state n and every axis i:

- if `i in S`,
  `Obs_S(T_i n)=T_i^S(Obs_S(n))`;
- if `i notin S`,
  `Obs_S(T_i n)=Obs_S(n)`.

### Proof

A global canonicalization subtracts one common scalar from all six components. Restricting to S then performing local min-zero canonicalization removes that common scalar. If i is omitted, the restricted coordinates are unchanged before that removable common shift. If i is visible, exactly its local component increments by one before local canonicalization. QED.

Thus the three omitted native coordinates are not set to zero: their translations act nontrivially on the full candidate state but are **exactly invisible** in the selected 3-axis observation.

This is an explicit algebraic realization of P000:

`OMITTED_CELL_COORDINATE != ZERO_COORDINATE`

and

`SLICE_OBSERVATION != FULL_CELL_STATE`.

## 6. Slice kernel is exactly three-dimensional in the coordinate completion

At the group level,

`ker(pi_S) = { [z] : z_i is constant on S }`.

Use the diagonal gauge to set that common visible value to zero. The three omitted coordinates are then arbitrary integers.

Therefore

`ker(pi_S) ~= Z^3`.

More concretely it is generated freely by the three omitted axis translations.

Hence there is an exact sequence

`0 -> Z^3_hidden(S) -> G6_D -> G_S -> 0`.

This is classical group rank bookkeeping only; P000 native dimension is still six axis dimensions. The result says exactly what one 3-axis observation forgets in this coordinate candidate: three independent relative translation coordinates.

## 7. One-slice coordinate chart for the full candidate

Fix a slice S and choose the gauge in which the minimum of the three visible lifted coordinates is zero.

Then every class of `G6_D` has a unique representation

`(a_S, h_1,h_2,h_3)`

where

- `a_S in A_S` is the existing nonnegative min-zero local triple;
- `(h_1,h_2,h_3) in Z^3` are the omitted coordinates relative to the visible chart gauge.

So, as a **set/chart**,

`G6_D ~= A_S x Z^3`.

The signed hidden integers are derived chart differences, not primitive native negative axes.

Unlike the superseded `one min-zero triple + one Z/2 bit` over-quotient, the correct no-extra-identification coordinate completion retains a full `Z^3` hidden fibre per selected slice.

## 8. Local 3-axis triangle return becomes full-state holonomy

Let `S={i,j,k}`. In the local 3-axis observation,

`T_i^S T_j^S T_k^S = identity`,

which is the established triangular three-positive-axis Cell return in that slice.

In the full coordinate completion, the same sequence has displacement

`H_S = [e_i+e_j+e_k] in G6_D`.

It lies in `ker(pi_S)` but is nonzero.

Since

`sum_{r=1}^6 e_r = 0 in G6_D`,

one has the exact complement law

`H_S = - H_{S^c}`.

Therefore a path that closes in a selected 3-axis Cell observation can carry a genuine translation in the three omitted coordinates. This is a typed hidden-coordinate holonomy, not a violation of the local slice theorem.

The reverse-third shortcut relation is reinterpreted correctly:

`pi_S(T_i T_j)=pi_S(T_k^{-1})`,

while globally

`T_i T_j T_k = H_S != identity`.

Thus the current R061 same-slice terminal equality need not be promoted to equality of full 6D Cell states.

## 9. All-slice reconstruction

The map to all 20 slice displacement observations

`Pi = product_{|S|=3} pi_S`

is injective.

Proof: if `[z]` maps to zero in every three-axis quotient, then for any pair i,j choose a third k. In the slice `{i,j,k}`, zero means `z_i=z_j=z_k`; hence every pair of global coordinates is equal. Thus z is diagonal and `[z]=0`.

Hence the full six-axis coordinate state has **no additional fibre invisible to every possible 3-axis coordinate observation**.

A smaller connected family of slices also suffices; the previously built four FCC/K4 star charts admit an exact integer gluing/reconstruction algorithm through their canonical min-zero sections.

## 10. Full six-axis min-zero section closes the old common-depth ambiguity

The derived six-axis atlas V2 proved that compatible local K4 min-zero charts reconstruct a unique min-zero six-count residual `n0`, while every nonnegative raw lift is

`n0 + h*(1,...,1)`, `h>=0`.

If the primitive full address rule is chosen as `A6_E^cand` with global minimum zero, only `h=0` is an admissible primitive address. Thus the common-depth ambiguity is not a hidden spatial dimension; it is absent from the primitive min-zero section exactly as in the established 3-axis address type.

This uses the V2 gluing theorem rather than replacing it.

## 11. Six-axis directed Pythagorean gauge consequence

P000 now defines all six native axes pairwise Enterprise-orthogonal and the typed six-axis component quadratic readout as sum of six squares.

For a derived displacement class g define

`ell_6(g)^2 = sum_i can6(g)_i^2`.

This generalizes the accepted 3-axis directed gauge and is translation invariant as a displacement readout.

It is not reversal-symmetric. If `d=can6(g)`, `M=max_i d_i`, then

`can6(-g)=M*1-d`,

and

`ell_6(-g)^2-ell_6(g)^2 = 6 M^2 - 2 M sum_i d_i`.

For one positive-axis unit:

- forward canonical component tuple has squared gauge `1`;
- reversed displacement has canonical tuple with five `1`s and one `0`, squared gauge `5`.

Projecting that reversed tuple to any three-axis slice containing the original axis gives `(0,1,1)` up to order, exactly recovering the accepted local reverse-axis squared gauge `2`.

Thus the six-axis construction explains rather than erases the older 3-axis reversal asymmetry.

## 12. What is proved versus what remains a Foundation choice

### Exact derived mathematics

- `G6_D=Z^6/Z1` and its unique min-zero section;
- all 20 restriction maps;
- omitted-axis invisibility under canonical coordinate translations;
- slice kernel `Z^3`;
- local triangle hidden holonomy `H_S` and complement law;
- all-slice injective reconstruction;
- six-axis directed sum-of-squares gauge on already-typed displacement components.

### Native Cell promotion still requires

A single semantic bridge remains:

`NATIVE_CELL_COORDINATE_COMPLETENESS`:

> the full spatial Cell identity/admissibility is exactly the six-axis min-zero coordinate state (affinely based at a Cell anchor), and unit six-axis coordinate translations are the actual native Cell adjacency actions; no additional path-history/internal state belongs to Cell identity itself.

Path history, BRC multiplicity, line identity and signed/readout holonomy remain separate richer observer layers even if endpoint Cell identity is coordinate-complete.

This bridge is strongly aligned with the current P000 statement `CELL_SPATIAL_STATE := (E_1,...,E_6)` but is recorded explicitly rather than silently inferred.
