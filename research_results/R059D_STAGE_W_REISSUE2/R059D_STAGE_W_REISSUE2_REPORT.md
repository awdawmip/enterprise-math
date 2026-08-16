# R059D Stage W REISSUE2 — Nonhomogeneous Triaxial Cell-Count Root-Collapse Atlas

Researcher-ID: `EM-R059D-9C6B2A`  
Taskbook: `R059D_STAGE_W_REISSUE2_NONHOMOGENEOUS_TRIAXIAL_CELL_COUNT_ROOT_COLLAPSE_20260816.md`  
Taskbook Git blob: `7ddaa1422786a39e5baa9fc2498298db6a28fa06`  
Frozen parent: `a9929a5bd666e621cb1bd77adb464df0d35db399`

## Executive result

This reissue corrects the first Stage-W execution by removing `TRANSLATION_HOMOGENEITY` from stored cell coordinates.

The cell-ID scaffold is the independent A2/C6 combinatorial sheet `C[a,b]`. Stored triaxial coordinates are a separate unknown map into `Z^3`.

The required semantic freeze holds:

`CELL_COORDINATES_ARE_INTEGER_ONLY`.

Radicals such as `sqrt(2)` and `sqrt(5)` occur only as `PRECOLLAPSE_ALGEBRAIC_VALUE`; they are never stored crystal-cell coordinates.

Only two observations are hard in the minimal control:

- `O=C[0,0] -> (0,0,0)`;
- one `+u` step `C[1,0] -> (1,-1,-1)`.

The cyclic first-neighbor values and their sign-inverted negatives are retained only in an explicitly declared first-shell symmetric subcase; they are not reclassified as observations. Global inversion covariance beyond the first shell is audited separately and is not assumed.

## Independent cell identity scaffold

The six cell-ID transitions are exactly the taskbook A2 moves:

- `+u:(a,b)->(a+1,b)`;
- `-w:(a,b)->(a+1,b-1)`;
- `+v:(a,b)->(a,b-1)`;
- `-u:(a,b)->(a-1,b)`;
- `+w:(a,b)->(a-1,b+1)`;
- `-v:(a,b)->(a,b+1)`.

This scaffold contains 61 cells through radius 4, with shell counts `1,6,12,18,24`. Pure rays in all six orientations are frozen through `n=36`.

Cell equality is equality of `(a,b)` IDs. Stored coordinates never determine whether two paths recoalesce.

Important cell-ID identities include

`+u,+v = -w`,

`+v,+w = -u`,

`+w,+u = -v`,

and the zero loop `+u,+v,+w`.

These relations are the central path-independence stress tests.

## Count ledgers

For each path, event counts are recorded before any coordinate proposal:

`D_i = #(+i)-#(-i)`.

For the other two axes relative to axis `i`:

`Q_i_plus = # negative moves`,

`Q_i_minus = # positive moves`,

`Q_i = Q_i_plus-Q_i_minus`.

These are event counts only.

For the pure `+u^n` ray,

`D_u=n`, `D_v=D_w=0`, while the transverse negative-event magnitude is `n`. Hence a candidate transverse root `-n^(1/p)` can arise without any assumption that stored coordinates have fixed increments.

For the A2 scaffold, two net-D triples describe the same cell iff they differ by a common shift

`D' = D + k(1,1,1)`.

This quotient relation is the key to constructing genuinely cell-state-valued count models.

## Predeclared model registry

The registry was frozen before formal scoring and no later formulas were added.

Mandatory models:

- `N`: `R_i=D_i+sgn(Q_i)|Q_i|^(1/p)`;
- `S`: `R_i=D_i+(Q_i_plus)^(1/p)-(Q_i_minus)^(1/p)`;
- `H`: first-round homogeneous/path-sum linear control.

Two allowed additions were used:

### Q — quotient range root

Let

`m=min(D_u,D_v,D_w)`, `M=max(...)`, `rho=M-m`, `N_i=D_i-m`.

Define

`R_i = N_i - (rho-N_i)^(1/p)`.

This is invariant under `D -> D+k(1,1,1)`, so it is a cell-state candidate rather than a preferred-path rule.

On `+u^n` it gives exactly

`(n,-n^(1/p),-n^(1/p))`,

retaining the hard direct primary count `U=n`.

### O — inversion-odd quotient root control

Using the same quotient counts,

`R_i = N_i^(1/p) - (rho-N_i)^(1/p)`.

This is exactly odd under inversion of the net count class, but for `p>1` it cannot maintain the hard primary count `U=n` beyond the smallest rays.

## Precollapse path-independence gate

The taskbook requires this gate before integer completion.

### N fails

The same cell `C[1,-1]` can be reached by `-w` or `+u,+v`.

For N these give

`(1,1,-1)`

versus

`(0,0,-root_p(2))`.

Thus N is history/path-representation dependent for every `p=1..6`.

### S fails

S has the same A2 relation failure. For `p>1` it is even sensitive to an inserted exact reversal: `+u` and `+u,+v,-v` reach the same cell but change the split-root precollapse state.

### H fails

The first-round path-sum control gives `(1,1,-1)` on `-w` but `(0,0,-2)` on `+u,+v` for the same cell. It therefore is not a valid cell-state coordinate model on the REISSUE2 scaffold.

### Q and O pass

Q and O depend only on `rho` and the common-shift-invariant normalized counts `N_i`. Every tested shortest path, A2 relation alternative, reversal insertion and triangle loop therefore recoalesces to one exact precollapse state.

## First-round trivialization is not reproduced

At `p=1`, Q simplifies to an exact integer quotient-range map. Along the pure `+u` ray it indeed gives `(n,-n,-n)`, but this does **not** come from a fixed stored increment.

For example:

- `O -> C[1,0]` under `+u` changes stored Q,p1 coordinates by `(1,-1,-1)`;
- `C[0,-1] -> C[1,-1]` under the same `+u` cell-ID move changes them by `(2,0,0)`.

So Q,p1 is explicitly nonhomogeneous. Its survival is due to A2 quotient invariance, not the first-round assumption `C(cell+d)-C(cell)=C(d)`.

## Mixed-cell completion atlas

Formal completion scoring is restricted to path-independent models.

Model O with `p>1` is rejected by the hard pure-axis primary count: at `n=3`, the only adjacent completions of `3^(1/p)` are 1 and 2, so the primary component cannot equal the directly counted value 3.

Model Q survives for every tested `p=1..6` in the minimal/cyclic subcase.

For each `p`, an exact cyclic-covariant and injective integer-coordinate assignment exists for all 61 radius-4 cells.

Mandatory mixed cells include:

- `+u,+v`, which recoalesces exactly to the one-step `-w` cell and has exact Q state `(1,1,-1)`;
- `+u,-v`, whose Q,p2 precollapse state is `(2,-sqrt(2),0)` and for which both `(2,-2,0)` and `(2,-1,0)` extend to complete radius-4 atlases;
- `+u,+w`, exact `(1,-1,1)`;
- `+u,+u,+v`, Q,p2 `(2,0,-sqrt(2))`, where both `(2,0,-2)` and `(2,0,-1)` extend globally.

The same lower/upper ambiguity persists for the corresponding p=3..6 cases.

On the pure `+u` ray:

- at `n=2`, both transverse magnitudes 1 and 2 extend to complete atlases for every p=2..6;
- at `n=3`, both 1 and 2 also extend;
- at `n=4`, p=2 is exact at magnitude 2, while p=3..6 retain both 1 and 2.

Thus mixed-cell consistency through radius 4 does **not** force a unique collapse sequence.

Freeze:

`COLLAPSE_SEQUENCE_REMAINS_MULTIBRANCH_AT_RADIUS4`.

## Root-order result

The formal result is not a unique square-root law.

- N/S/H are killed before completion by cell-state/path-independence gates.
- O,p>1 is killed by direct primary count at `+u^3`.
- Q,p=1 survives structurally through A2 quotient invariance.
- Q,p=2,3,4,5,6 all survive the radius-4 minimal/cyclic mixed-cell atlas.

Therefore:

`MULTIPLE_ROOT_ORDERS_SURVIVE`.

`ROOT_ORDER_NOT_IDENTIFIED`.

And, importantly:

`SQUARE_ROOT_SURVIVES_NONHOMOGENEOUS_ATLAS_IN_MINIMAL_CYCLIC_SUBCASE`.

This is the scientific correction to first-round Stage W: square root is **not** rejected once stored-coordinate homogeneity is removed.

It is also not singled out.

## Inversion audit

First-shell sign inversion is an explicit subcase hypothesis and passes at shell 1.

Extending inversion covariance globally is a stronger requirement. Q,p>1 fails that extension by ray `n=3`: the positive ray can have primary `+3`, while the negative-ray Q precollapse state cannot complete its corresponding component to `-3`.

Thus:

`GLOBAL_INVERSION_EXTENSION_REJECTS_Q_P_GT_1_BY_RAY3`.

Q,p1 does satisfy global inversion.

Accordingly, the nontrivial root survival claim is scoped to the minimal/cyclic subcase and is not an inversion-covariant universal law.

## Anti-triviality controls

No default rounding rule is selected.

Within Q,p=2..6, all of the following fixed completion policies can produce cyclic/injective radius-4 atlases:

- floor-root magnitude;
- ceiling-root magnitude;
- nearest-root magnitude;
- midpoint-in-power-interval choice.

Their survival means the atlas does **not** distinguish them at this radius. It is not evidence that any is native.

A simple parity rule survives at p=2 but at p=3..6 causes explicit distinct-cell coordinate collisions, including a collision at `(-1,-1,4)` among several shell-4 cells.

Axis-name preference, old zero-sum raw coordinates, old `(1,-1,0)` raw cell coordinates, and the first-step path-sum rule are all rejected as positive premises.

## 5 -> 4 / 9 control

Because Q,p=2 square root survives the preceding minimal/cyclic gates, `n=5` is admissible to inspect.

`sqrt(5)` has adjacent integer root levels 2 and 3, yielding candidate stored ray coordinates

`(5,-2,-2)`

or

`(5,-3,-3)`.

The mixed atlas is frozen through radius 4, so it provides no shell-5 constraint capable of eliminating either value.

Therefore:

`FIVE_TO_FOUR_OR_NINE_STILL_UNRESOLVED_AT_TEST_RADIUS`.

On the squared-count readout these correspond to `5->4` and `5->9` respectively. Neither is promoted.

In the stronger global-inversion subcase the Q square-root model has already failed at n=3, so the 5-control is inapplicable there.

## What remains underdetermined

- the root order: Q,p=2..6 all survive the tested minimal/cyclic atlas;
- the integer collapse sequence: multiple lower/upper choices remain globally self-consistent through radius 4;
- `5->4` versus `5->9`;
- whether a nontrivial root model can coexist with a globally inversion-covariant stored-coordinate ontology;
- stored coordinates outside the hard +u observation if even the explicit first-shell cyclic/inversion subcase is withheld;
- any universal BRC or physical interpretation.

The first Stage-W conclusions `P1_IDENTITY_UNIQUE...`, `SQUARE_ROOT_PRECOLLAPSE_REJECTED...`, and its linear stored-coordinate formula remain preserved only as conclusions of the superseded homogeneous model, not as answers to this experiment.

## Checker

Deterministic checker: `799 / 799 PASS`.

Checks digest:

`f6593f207d852783a411a441761f3a0dc903f376582f92f220f2765226199103`

The checker explicitly verifies the frozen-parent immutability gate and rejects accidental reintroduction of fixed stored increments/path-sum homogeneity.

`STOP_FOR_DRIVER_REVIEW`
