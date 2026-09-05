# P000 六轴两两进取正交与 120° 原生正角

Status: `ACTIVE / P000 DIRECT-USER DEFINITION / FOUNDATION`
Date: `2026-09-05`
Authority: direct current-user worldview correction.

## 1. Definition, not theorem

The following is a native Enterprise-geometry definition and has no proof obligation inside the project:

`FOR ALL i != j IN {1,...,6}: E_i PERP_E E_j`.

All six native positive spatial axes are pairwise Enterprise-orthogonal.

The native Enterprise right angle is

`ENTERPRISE_RIGHT_ANGLE = 120_DEGREES`.

Here `PERP_E` is the native Enterprise orthogonality relation. It is not classical Euclidean orthogonality.

Freeze:

`SIX_NATIVE_AXES_PAIRWISE_ENTERPRISE_ORTHOGONAL = TRUE`.

`ENTERPRISE_RIGHT_ANGLE = 120_DEGREES`.

`PAIRWISE_ORTHOGONALITY_IS_DEFINITION_NOT_PROOF_OBLIGATION`.

## 2. Classical 90° status

The classical Euclidean convention that a right angle is `90 degrees` is not the native right-angle definition of Enterprise geometry.

Within Enterprise Math native geometry:

`90_DEGREES != ENTERPRISE_RIGHT_ANGLE`.

For external Euclidean mathematics and engineering models, the classical `90 degree` right angle remains a valid effective-model definition and must be reported faithfully in that external model.

Freeze:

`CLASSICAL_90_DEGREE_RIGHT_ANGLE = EXTERNAL_EFFECTIVE_EUCLIDEAN_MODEL_ONLY`.

`DO_NOT_REIMPORT_90_DEGREES_AS_NATIVE_ENTERPRISE_ORTHOGONALITY`.

## 3. Relation to the existing three-axis slice

The previously established three-axis slice already declares each visible axis pair Enterprise-orthogonal and reads the native right angle as `120 degrees`.

The current definition upgrades that local fact to the full six-axis native relation:

`THREE_AXIS_PAIRWISE_PERP_E = RESTRICTION_OF_FULL_SIX_AXIS_PAIRWISE_PERP_E`.

The four FCC/K4 three-axis slice charts are observer/carrier slices. Their carrier Euclidean angles do not define the native full six-axis orthogonality relation.

In particular, the three K4 opposite-edge pairs

- `AB ⟂_E CD`,
- `AC ⟂_E BD`,
- `AD ⟂_E BC`

are now defined Enterprise-orthogonal as well.

## 4. Quadratic axis-component consequence

Whenever a typed state or displacement object has a declared six-axis component decomposition

`x = (x_1,...,x_6)`

whose components are measured on the six native axes and the existing native Pythagorean readout is applicable, pairwise Enterprise orthogonality forces zero mixed terms. Therefore the native axis-component quadratic readout is

`L_E(x)^2 = x_1^2 + x_2^2 + x_3^2 + x_4^2 + x_5^2 + x_6^2`.

This conclusion fixes the former one-parameter S4-invariant quadratic candidate family at `c=0`.

Important type boundary:

`SIX_AXIS_COMPONENT_NORM != DECLARATION_THAT_EVERY_N^6_TUPLE_IS_A_NATIVE_CELL_ADDRESS`.

The native `X6` Cell-state/admissibility problem remains separate. A tuple may be used in the norm only after an admissible typed six-axis component readout has been supplied.

## 5. Carrier guard

It is impossible and unnecessary to realize six pairwise Enterprise-orthogonal native axes as six pairwise classically Euclidean 120-degree vectors in one classical 3D carrier.

No contradiction follows, because:

`NATIVE_ENTERPRISE_ORTHOGONALITY != CARRIER_EUCLIDEAN_ANGLE_RELATION`.

The FCC carrier continues to provide a six-label rotational atlas and local chart orientations only.

Freeze:

`FCC_CARRIER_READOUT_IS_NOT_NATIVE_IDENTITY`.

`CARRIER_EUCLIDEAN_GRAM_MATRIX != NATIVE_6D_ORTHOGONALITY_MATRIX`.

## 6. Supersession

Any prior research note saying that the three K4 opposite-edge pairings were still undefined in native orthogonality, or that the S4-invariant quadratic family retained an unresolved parameter `c`, is superseded at the Foundation level by this direct-user definition.

The earlier classification theorem remains valid as a classification of all candidate S4-invariant quadratic extensions before the new definition; the current native choice is uniquely `c=0`.
