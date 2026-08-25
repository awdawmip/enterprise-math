# Driver Review — QRF-R2 Independent Foundation Verification

Status: `DRIVER_ACCEPTED_WITH_PRODUCT_STRUCTURE_SCOPE / EQUIVALENT_BUT_FOUNDATION_USEFUL / NOT_FOUNDATION_ADMITTED`

Date: `2026-08-25`

Driver-ID: `EM-DVR-R63A21 / CONTROL_PLANE`

Task:
`RS-QRF-R2-INDEPENDENT-FOUNDATION-VERIFICATION`

Taskbook source:
`41a1bbdf23831f9ad2af160df4a6bd5603f22547`

Owner branch/head:
`research/qrf-r2-independent-foundation-verification@28d3942dfc4e85ba85d6db83365eaaba399388d0`

Researcher-ID:
`EM-QRF2-BD143C`

Primary report:
`research_outputs/QRF_R2_INDEPENDENT_FOUNDATION_VERIFICATION_20260822.md`

## 1. Driver verdict

The returned leading verdict

`VERIFY_R2_EQUIVALENT_BUT_FOUNDATION_USEFUL`

is accepted with an explicit scope condition:

QRF-R2 is intrinsic only relative to a primitive two-channel product decomposition whose admissible relabelings preserve the two channel foliations, up to axis swap.

It is not invariant under arbitrary channel-mixing changes of chart.

## 2. Exact discrete theorem

Let `Q:I x J -> A`, where `I,J` are nonempty connected integer intervals and `A` is an abelian group.

If every elementary plaquette has zero mixed difference,

`Q(i+1,j+1)-Q(i+1,j)-Q(i,j+1)+Q(i,j)=0`,

then for any basepoint `(i0,j0)`:

`Q(i,j)=Q(i,j0)+Q(i0,j)-Q(i0,j0)`.

Conversely every such additively separated field has zero mixed difference.

The report's telescoping proof is complete. No positivity, symmetry, homogeneity, continuity, multiplication, norm, Euclidean geometry, or Gaussian structure is required.

With frozen axis data

`Q(a,0)=a^2`,
`Q(0,b)=b^2`,

this yields exactly

`Q(a,b)=a^2+b^2`.

Hence:

`AXIS_SQUARE_LAWS + ZERO_MIXED_DIFFERENCE <=> SUM_OF_SQUARES_SECTOR_LAW`.

The full package is theorem-equivalent to the current two-variable law; it is not logically weaker once the axes are fixed.

## 3. Nonredundancy and operational content

The condition is nevertheless mathematically nonempty relative to the axis data.

For

`Q_tau(a,b)=a^2+tau ab+b^2`,

all `tau` have the same frozen axis restrictions, while

`Delta_a Delta_b Q_tau = tau`.

Thus `tau=-1` and `tau=1` are genuinely excluded while `tau=0` survives.

The target-free operational interpretation is also accepted:

`Q(a+1,b)-Q(a,b)`

must be independent of the transverse background `b`; equivalently the elementary interaction observable

`I_Q(a,b)=Q(a+1,b+1)+Q(a,b)-Q(a+1,b)-Q(a,b+1)`

vanishes.

This is a local four-value comparison rule that can be tested without first naming the global sum-of-squares formula.

Therefore QRF-R2 has explanatory/local value even though the completed model class is unchanged.

## 4. Invariance boundary

The report correctly distinguishes product-structure covariance from arbitrary chart invariance.

Because zero mixed difference is equivalent to additive separation, it is preserved under independent relabelings of the two factors and under axis swap, provided boundary data are transported with the relabeling.

It is not preserved under maps that mix the two foliations.

For the shear

`(a,b)=(u,u+v)`,

pulling back `a^2+b^2` gives

`2u^2+2uv+v^2`,

whose mixed defect is exactly `2`.

A finite channel-mixing relabeling likewise produces nonzero plaquette defect.

Therefore:

`QRF_R2_FOUNDATION_USEFUL` is conditional on the native ontology treating the two channel factors as primitive structure rather than quotienting by arbitrary shears/mixed charts.

If a future admissibility contract enlarges chart equivalence to channel-mixing transformations, R2 must be reclassified as an invariance failure without changing the discrete theorem.

## 5. Executable pressure evidence

The executable witnesses correctly verify:

- `tau=-1,0,1` mixed defects are exactly `-1,0,1`;
- separable non-target functions satisfy zero defect;
- the frozen axis reconstruction agrees with `a^2+b^2` on the regression grid;
- the shear has constant mixed defect `2`;
- an explicit finite channel-mixing relabeling creates defect `-3` at the origin.

These are regression/pressure witnesses; the general theorem is supplied by the telescoping proof.

## 6. Scope / Foundation boundary

Accepted:

`QRF_R2_DISCRETE_SEPARATION_THEOREM = VERIFIED`

`QRF_R2_OPERATIONAL_NO_INTERACTION_READING = VERIFIED`

`QRF_R2_COMPLETED_STRENGTH = THEOREM_EQUIVALENT_TO_TARGET_WITH_FROZEN_AXES`

`QRF_R2_PRODUCT_STRUCTURE_SCOPE = REQUIRED`

Not accepted:

- strict logical weakening of the sum-of-squares law after the axes are fixed;
- coordinate-free invariance under arbitrary channel-mixing charts;
- automatic Foundation promotion;
- Euclidean/Pythagorean/norm interpretation from this result alone.

## 7. Closure

`DRIVER_REVIEW = ACCEPT_WITH_SCOPE`

`VERIFY_R2_EQUIVALENT_BUT_FOUNDATION_USEFUL = ACCEPTED`

`FOUNDATION_ADMITTED = false`

`SUCCESSOR_AUTOMATICALLY_OPENED = false`

This closes independent verification of QRF-R2 at the frozen two-channel product scope.