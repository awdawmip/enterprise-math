# R061 Stage 1 — Origin Incidence / Affine Anchor Theorem

Task-ID: `RS-R061-STAGE1-NATIVE-LINE-TRACE-FIBER-ORIGIN-AFFINE-REALIZATION`  
Researcher-ID: `EM-R061S1-4183C1`

## Status

`ORIGIN_INCIDENCE_EXACT = true`.

`AFFINE_ADDRESS_ANCHOR_EXACT = true`.

The correct origin correction is **not** a guessed `+1`, `-1`, or half step. It is a type-changing incidence followed by a constant affine center-versus-vertex offset.

## 1. Exactly three cells incident to the origin

The frozen carrier has nearest center spacing `1` and cell radius

`R_CELL=1/sqrt(3)`.

At this critical covering radius every elementary triangle of three mutually neighboring centers has one common triple boundary-intersection point. `O_E` is one such point.

Therefore exactly the three cells whose centers are the vertices of that elementary center triangle are incident to `O_E`.

No fourth cell is incident: the next nonzero center separation is too large for its circle boundary to pass through the same triple point under the frozen carrier theorem.

Thus:

`|IncCells(O_E)|=3`.

## 2. Exact carrier normalization, used only for incidence

Choose carrier direction vectors `t_1,t_2,t_3` with pairwise carrier angle `120°` and carrier presentation relation

`t_1+t_2+t_3=0`.

This relation is used only to name carrier positions and adjacency. It is not a native Enterprise vector identity and never enters the native length formula.

Use `(t_1,t_2)` as a carrier presentation basis. In one mirror gauge, the three incident center offsets from `O_E`, multiplied by `3`, are

`(-2,-1), (1,-1), (1,2)`.

Hence the offsets themselves are

`s_A=(-2 t_1-t_2)/3`,

`s_B=(t_1-t_2)/3`,

`s_C=(t_1+2 t_2)/3`.

With the carrier quadratic form for this presentation only,

`q_car(x,y)=x^2+y^2-xy`,

we obtain

`q_car(s_A)=q_car(s_B)=q_car(s_C)=1/3=R_CELL^2`,

and every pair of centers has carrier separation squared `1`.

The mirror gauge uses `-s_A,-s_B,-s_C` and yields the same incidence theorem.

## 3. One canonical anchor per fixed sector

The three incident centers are separated around `O_E` by `120°`, and no center lies on a native number axis because the foundation freezes

`NATIVE_NUMBER_AXIS_NEVER_PASSES_THROUGH_CELL_CENTER`.

The three open native right sectors are also the three `120°` regions between successive positive axes.

Therefore each open sector contains **exactly one** of the three incident centers.

Define that unique cell in sector `S_ij` as

`C_ij(0,0)`.

This is canonical from incidence plus the sector label; no tie-break is used.

Hence:

`Sigma_O^(ij): O_E -> C_ij(0,0)`

is a unique type-changing start incidence for every fixed sector.

It is not a nearest-center jump.

Consequences:

- fixed sector origin branch count: `1`;
- global origin incident-cell count: `3`;
- a global axis line has two adjacent sector presentations and therefore two distinct chart-local start-cell trajectories, while its line identity is glued once.

## 4. Exact affine vertex chart

For `a,b>=0`, define the coordinate vertex

`V_ij(a,b)=O_E+a t_i+b t_j`.

These are the translated triple-intersection vertices. In particular the native axis ticks are vertex events.

## 5. Exact affine center chart

Let

`s_ij := ctr(C_ij(0,0))-O_E`.

Define

`ctr(C_ij(a,b)) = ctr(C_ij(0,0))+a t_i+b t_j`.

Equivalently:

`ctr(C_ij(a,b)) = V_ij(a,b)+s_ij`.

Therefore the exact affine equation is

`ctr(C_ij(a,b)) - V_ij(a,b) = s_ij`,

independent of `(a,b)`.

Translation invariance of the triangular circle-cell carrier implies that `C_ij(a,b)` is incident to `V_ij(a,b)` for every integer address.

## 6. No off-by-one

Formal component counts give a **relative integer translation**:

`End_formal(w)=(#X_i(w),#X_j(w))=(a,b)`.

After the exact start anchor is typed,

`ctr(C_end)=ctr(C_ij(0,0))+a t_i+b t_j`.

There is no scalar correction to `(a,b)`.

The apparent Stage 0 off-by-one problem arose only if one silently set

`ctr(C_ij(0,0))=O_E`.

Stage 1 does not do that. The correction is the fixed affine vector `s_ij` together with a type tag.

Therefore:

`FORMAL_COMPONENT_COUNT -> CENTER_AFFINE_ADDRESS`

is exact with the same integer pair `(a,b)` after `Sigma_O^(ij)`.

## 7. 3-4-5 consequence

For `(a,b)=(3,4)`:

- `Sigma_O^(ij)` selects the first cell state;
- every trace word has exactly seven center-transition letters;
- after those seven transitions the terminal cell is `C_ij(3,4)`;
- that cell is incident to `V_ij(3,4)`;
- the native endpoint length is `sqrt(3^2+4^2)=5`.

Thus the seven letters are now exactly the center-to-center transitions **after** the origin incidence. They are not the native length and `Sigma_O` is not an eighth center jump.

## 8. Covariance

Cyclic relabeling

`(1,2,3)->(2,3,1)->(3,1,2)`

permutes the three sectors and their unique anchors.

The affine equation is unchanged in form, proving cyclic covariance.

Mirror reversal of the carrier drawing changes the representative offsets but not the incidence theorem or branch counts.

## 9. Verdict

The origin/cell gap is resolved by

`O_E --Sigma_O^(ij)--> C_ij(0,0)`

and

`C_ij(a,b)=C_ij(0,0)+a t_i+b t_j`,

with terminal incidence to

`V_ij(a,b)=O_E+a t_i+b t_j`.

Freeze for Stage 1:

`ORIGIN_INCIDENCE_EXACT = true`.

`AFFINE_ADDRESS_ANCHOR_EXACT = true`.

`NO_NUMERIC_OFF_BY_ONE_PATCH_REQUIRED = true`.
