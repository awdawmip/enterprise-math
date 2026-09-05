# X6 六轴 directed gauge：任意点位移、三角不等式与 slice contraction

Status: `DERIVED / EXACT ON SIX-COORDINATE COMPLETION / NATIVE IF COORDINATE-COMPLETENESS GATE PROMOTED`
Date: `2026-09-05`

## 1. Directed displacement

Let P,Q be two states with six-axis coordinate lifts `p,q in Z^6` (or primitive candidate addresses in the min-zero section).

Define the derived six-axis directed displacement

`D6(P->Q)=can6(q-p)`.

This is independent of changing either affine coordinate description by the same admissible global diagonal gauge, and is the direct six-axis extension of the accepted R061 canonical displacement decoder.

Define

`ell6(P->Q)^2=sum_i D6_i(P->Q)^2`.

P000 pairwise Enterprise orthogonality supplies the sum-of-squares component readout; `can6` supplies the positive-axis directed decoder.

## 2. Exact gauge laws

For displacement classes x,y in `G6_D`:

1. positivity: `ell6(x)>=0`;
2. definiteness: `ell6(x)=0 iff x=0 in G6_D`;
3. nonnegative integer homogeneity: `ell6(kx)=k ell6(x)` for `k in N_0`;
4. triangle inequality:
   `ell6(x+y)<=ell6(x)+ell6(y)`.

### Triangle proof

Let `a=can6(x)`, `b=can6(y)`. Both are componentwise nonnegative.

`can6(x+y)=can6(a+b)`.

If `m=min_i(a_i+b_i)`, then `can6(a+b)=a+b-m*1`, which is componentwise between `0` and `a+b`; hence

`||can6(a+b)||_2 <= ||a+b||_2 <= ||a||_2+||b||_2`.

No continuum geometry is used as native input beyond the already frozen finite component quadratic readout; this is finite integer algebra followed by square-root readout if desired.

## 3. Reversal formula and asymmetry

Let `d=can6(x)` and `M=max_i d_i`. Then

`can6(-x)=M*1-d`.

Thus

`ell6(-x)^2 = sum_i (M-d_i)^2`

and

`ell6(-x)^2-ell6(x)^2 = 6M^2-2M sum_i d_i`.

Therefore the directed gauge is generally not symmetric.

This is not a defect: the already accepted three-axis directed gauge has the same positive-axis reversal phenomenon, while Packet/Path explicitly separates transition count from geometric length readout.

## 4. Unit-axis bidirectional spectrum

For one positive native axis generator `e_i`:

`can6(e_i)=e_i`, so `ell6(e_i)^2=1`.

For its path reversal:

`can6(-e_i)=(1,...,1)-e_i`,

which has five ones and one zero, so

`ell6(-e_i)^2=5`.

Hence the six-axis unit segment has directed squared pair

`(1,5)`

and unoriented bidirectional squared spectrum

`{1,5}`.

The reverse is one adjacency event at Packet/Path level even though the directed positive-axis component gauge reads `sqrt(5)`; `PATH_COUNT != LENGTH` remains intact.

## 5. Exact recovery of the old three-axis reversal law

Select any three-axis slice S containing i.

The local observation of the full reverse decoder restricts the tuple with five ones / one zero to the three visible components. After local min-zero canonicalization it is exactly a permutation of

`(0,1,1)`.

Therefore the local reverse squared gauge is

`2`,

while the forward local gauge is `1`.

This recovers the accepted three-axis axial asymmetry as the projection of the six-axis completion:

`FULL squared spectrum {1,5} -> selected 3-axis squared spectrum {1,2}`.

## 6. Slice projection is gauge-contractive

For any displacement x and selected slice S,

`ell_S(pi_S x) <= ell6(x)`.

Proof: let `d=can6(x)>=0`. The local canonical tuple is obtained from the three selected entries of d by subtracting their local minimum. This can only decrease the absolute value of each selected nonnegative component, and the omitted components contribute nonnegatively to `ell6^2`.

Thus a lower-dimensional slice cannot have larger coordinate-gauge magnitude than the full state.

Equality holds precisely when the omitted components contribute zero and no positive common local offset is removed (equivalently, in the canonical full representative the displacement is already supported in the visible slice with visible minimum zero).

## 7. Arbitrary-point directed distance on a coordinate-complete Cell torsor

If `CELL_IDENTITY_BY_FULL_SIX_AXIS_CENTER_ADDRESS` is promoted, define on the affine Cell torsor

`d6(P,Q)=ell6(D6(P->Q))`.

Then:

- `d6(P,Q)>=0`;
- `d6(P,Q)=0 iff P=Q`;
- `d6(P,R)<=d6(P,Q)+d6(Q,R)`;
- symmetry is not required and generally fails.

So the full coordinate-complete geometry naturally carries a directed metric/gauge, with the existing bidirectional-spectrum observer available when an unoriented endpoint pair is desired.

## 8. Boundary

This theorem does not identify path count with length, does not assign a continuum Euclidean norm to the FCC carrier, and does not declare every arbitrary six-tuple a primitive Cell address without the global min-zero/type gate.
