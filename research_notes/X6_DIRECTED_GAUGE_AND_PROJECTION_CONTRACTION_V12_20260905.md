# X6 六轴 directed gauge：任意点位移、三角不等式与 slice contraction

Status: `RE-TYPED / EXACT RELATIVE-QUOTIENT DIRECTED GAUGE / NATIVE DEFINITENESS CLAIM SUPERSEDED`
Date: `2026-09-05`
Revision: `2026-11-13` (LP026 actual current-consumer correction against frozen P000 V5)

**Current native-versus-observer scope.** The construction `can6: Z^6 -> Z^6/Z(1,1,1,1,1,1)` is a lower-information observer. Its directed gauge is definite on this *relative quotient*, not on native signed Cell identity. The native Cell torsor has complete signed raw displacement `q-p in Z^6`; its component-square norm is `G(q-p)=sum_i(q_i-p_i)^2`. A common-depth shift is genuine native displacement even when invisible to the directed gauge.

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

## 7. Exact scope of the directed gauge on quotient and native Cells (2026-11-13 correction)

For native Cells `P,Q` with chosen-Cell raw signed coordinates `p,q in Z^6`, define

`d_rel(P,Q) = ||can6(q-p)||_2`.

This is a directed **pseudometric on native Cells**: it is nonnegative, satisfies the directed triangle inequality, and obeys

`d_rel(P,Q)=0 <=> q-p in Z*(1,1,1,1,1,1)`.

Consequently it is definite only after passing to the relative quotient `G6_D=Z^6/Z*(1,1,1,1,1,1)`, where it is a well-defined asymmetric directed metric. This quotient statement is the mathematically valid form of the historical §7 construction. Coordinate completeness of the native torsor **does not** make the relative observer injective.

**Exact signed-X6 counterexample:** `p=(0,0,0,0,0,0)` and `q=(1,1,1,1,1,1)` are distinct native Cells. The raw displacement has `G(q-p)=6` and precisely `6!=720` shortest signed native-axis paths, but `can6(q-p)=0` and `d_rel(P,Q)=0`. More generally `q-p=t*(1,1,1,1,1,1)` has native squared norm `6t^2`, whereas the relative directed gauge remains zero for every integer `t`. No native endpoint, BRC multiplicity, path order or provenance may be reconstructed solely from this observer without the scope-specific repair data.

For `d=e_i` and its signed reversal `-d`, the **native** component-square norm is `G(d)=G(-d)=1`, while the **relative observer** gives squared directed pair `(1,5)`. Likewise, §5's `{1,2}` is the selected three-axis *observer* spectrum, not native signed reversal asymmetry.

**Current consumer contract:** for native displacement/Cell equality/length consume the raw signed `q-p` with `G=sum_i(q_i-p_i)^2`; for relative quotient composition, one-way directed observation and its asymmetry consume `[q-p] in G6_D` or `can6(q-p)`, declaring lost common depth and future-operation limitations. For BRC and path-dependent work retain signed primitive steps and ordered witness/provenance until any observer quotient is justified. The earlier conditional assertion `d6(P,Q)=0 iff P=Q` on the *native* Cell torsor is superseded by the displayed exact kernel formula; the historical candidate claim remains attributable to the 2026-09-05 version.

## 8. Boundary

This theorem does not identify path count with length, does not assign a continuum Euclidean norm to the FCC carrier, and does not declare every arbitrary six-tuple a primitive Cell address without the global min-zero/type gate.
