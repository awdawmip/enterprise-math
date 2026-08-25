# Phase-A Return — Triaxial Directional Defect Independent Tool Verification

Researcher-ID: `EM-TDDEF-79114C`

Task: `RS-TRIAXIAL-DIRECTIONAL-DEFECT-INDEPENDENT-TOOL-VERIFICATION`

Phase-A status: `FROZEN_INDEPENDENT_RECONSTRUCTION_PENDING_PHASE_B_DEDUP`

## Independence attestation

The execution stamp was committed and remotely confirmed before mathematical source reading. Before this freeze, no originating triaxial-tomography journal, conversation, Driver handoff, source proof, source checker, downstream integration, current toolbox inventory, or candidate implementation was read.

Phase-A inputs were restricted to the taskbook, the two whitelisted native-plane definitions, standard mathematics, and independently written standard-library code.

## Reconstructed operator

For a declared cyclic 120-degree endpoint frame:

`Delta_i=tau_i-I`

`H_ij=Delta_i Delta_j`

`G=Delta_1 Delta_2 Delta_3`.

`G` is cyclically covariant and changes sign under simultaneous frame reversal. It is an oriented frame defect, not a coordinate-free scalar.

## Exact Phase-A results

1. **Tomography kernel.** For any field `K` and pairwise distinct unoriented primitive frame orbits,

   `ker X_mathcalF(B_R)=P_mathcalF K^{B_{R-W}}`,

   where `P_mathcalF` is the product of the frame triple-defect operators and `W=sum w(S)` over frame orbits.

2. **Frame width.** `w(S)=max(S)-min(S)`; on canonical min-zero seeds this is `max(S)`.

3. **Kernel dimension / uniqueness.** `dim ker X_mathcalF(B_R)=|B_{R-W}|`; injectivity holds exactly when `W>R`. At `W=R`, one ghost amplitude remains.

4. **Primitive census.** Exact width `w` has `phi(w)` unoriented tomography frames and `2phi(w)` oriented/chiral frame orbits.

5. **Eight traces vs six endpoints.** The formal expansion has eight signed trace states. Endpoint carrier closure coalesces only endpoints and yields the six-point stencil

   `G=tau_1+tau_2+tau_3-tau_1^{-1}-tau_2^{-1}-tau_3^{-1}`.

   `ENDPOINT_COALESCENCE != TRACE_IDENTITY_COALESCENCE` is preserved.

6. **Second-to-third bridge.** `Delta_1 H_23=Delta_2 H_31=Delta_3 H_12=G` exactly.

7. **Exposed augmentation.** One exposed-vertex point sample per ghost-amplitude degree produces a triangular matrix with determinant `+/-1`. It is injective over every commutative coefficient ring with `1` and scalar-count minimal over fields.

8. **Adjoint / Laplacian.** `G^*G=L_1L_2L_3`, with `L_i=2I-tau_i-tau_i^{-1}`. Full `G^*` output is injective on finite-support ghost space over every field. Compressed square-Gram output is not finite-characteristic-uniform: base-frame failures occur in characteristics `2,3,5,7` on small boxes. Characteristic `2` also collapses reversal-sign chirality.

9. **No local deghosting.** `G` has no finite-support translation-invariant convolutional left inverse in the Laurent group-ring model.

10. **Hive/rhombus reuse.** `PASS`; the regression uses the exact same `RHOMBUS2` and `TRIPLE_DEFECT` implementations and verifies complementary-direction rhombus-defect variation.

11. **Y-Delta discriminator.** `OUTSIDE_INTERFACE / HARD NEGATIVE BOUNDARY`; general star/triangle response equivalence is a rational Schur-complement family, not the fixed linear directional-defect interface.

## Machine verification

Independent unit suite: `11/11 PASS`.

Independent checker covers:

- 14 exact tomography cases, including mixed frames;
- rational and characteristics `2,3,5,7` rank checks;
- Euler-phi census through width `32`;
- exposed-vertex unimodularity in one- and two-frame cases;
- compressed-Gram characteristic failure witnesses;
- same-operator Hive/rhombus regression;
- Y-Delta negative discriminator;
- no finite-support Laurent left inverse.

## Phase-A interface narrowing already forced

Any accepted interface must distinguish:

- `ORIENTED_FRAME` from `UNORIENTED_XRAY_FRAME`;
- `EIGHT_STATE_TRACE_CUBE` from `SIX_POINT_ENDPOINT_STENCIL`;
- `CHIRALITY_AUGMENT_FULL` from `COMPRESSED_GRAM_AUGMENT`;
- exact finite-domain reconstruction from nonexistent finite-support convolutional deghosting.

## Phase-A disposition

`MATHEMATICS_RECONSTRUCTED / CROSS_DOMAIN_REUSE_PASS / INTERFACE_NARROWING_REQUIRED_BEFORE_GLOBAL_TOOL_VERDICT`

No final four-way task verdict is issued before Phase-B dedup.
