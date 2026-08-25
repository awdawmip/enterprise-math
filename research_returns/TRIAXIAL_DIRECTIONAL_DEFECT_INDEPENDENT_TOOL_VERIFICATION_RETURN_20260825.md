# Return — Triaxial Directional Defect Independent Tool Verification

Researcher-ID: `EM-TDDEF-79114C`

Task: `RS-TRIAXIAL-DIRECTIONAL-DEFECT-INDEPENDENT-TOOL-VERIFICATION`

Hard target: `TRIAXIAL_DIRECTIONAL_DEFECT_CALCULUS_T1_SUBTOOL_INDEPENDENTLY_RECONSTRUCTED_AND_CROSS_DOMAIN_VERIFIED_OR_NARROWED_OR_REJECTED`

## Final verdict

**`NEEDS_NARROWER_TOOL_INTERFACE`**

## Control-plane result

- Required pre-math stamp: PASS.
- Stamp commit: `0f6e3d558411c282af1ffd1cdeae7f045c5722c7`.
- Remote owner branch was confirmed at that commit before Phase A.
- Phase-A independent freeze: `9ff6b64bee6431be0a44bf876254875c47a6e588`.
- Withheld/source/inventory boundary was respected until that freeze.
- Shared toolbox registry was not modified.

## Independently reconstructed mathematics

Accepted:

1. `Delta_i=tau_i-I`.
2. `H_ij=Delta_i Delta_j`.
3. `G=Delta_1 Delta_2 Delta_3`.
4. Cyclic frame covariance and reversal law `G_{-F}=-G_F`.
5. Second-to-third bridge `Delta_1H_23=Delta_2H_31=Delta_3H_12=G`.
6. Frame width `w(S)=max(S)-min(S)`.
7. Primitive exact-width census: `phi(w)` unoriented tomography frames and `2phi(w)` oriented/chiral frames.
8. Eight formal trace states are distinct from the six-point endpoint stencil; endpoint coalescence is not trace-identity coalescence.
9. For a pairwise distinct family of primitive unoriented frame orbits and `W=sum w(S)`, exact finite tomography kernel:
   `ker X_F(B_R)=P_F K^{B_{R-W}}`.
10. Hence `dim ker=|B_{R-W}|` and X-ray uniqueness holds exactly when `W>R`.
11. Exposed-vertex augmentation gives one scalar measurement per ghost-amplitude degree with triangular determinant `+/-1`; field-scalar count is minimal.
12. `G^*G=L_1L_2L_3`, where `L_i=2I-tau_i-tau_i^{-1}`.
13. Full adjoint-field augmentation is finite-support injective over every field.
14. Compressed square-Gram augmentation is not characteristic-uniform; independently reproduced failures occur in characteristics `2,3,5,7` on small boxes.
15. Characteristic `2` destroys reversal-sign chirality.
16. No finite-support translation-invariant Laurent-convolution left inverse of `G` exists.
17. Hive/rhombus reuse: PASS with the exact same `RHOMBUS2` / `TRIPLE_DEFECT` implementation.
18. Y–Delta: HARD NEGATIVE BOUNDARY; the general star/triangle response map is rational/nonadditive and is not this linear defect interface.

## Phase-B dedup result

Current shared assets already contain generic/classical neighboring machinery:

- exact state difference/response logic in `src/enterprise_math/difference_response.py`;
- order-theoretic adjoint boundary pullback in `src/enterprise_math/adjoint_boundary_precision.py`;
- graph Laplacian / chip-firing T1 machinery in `src/enterprise_math/discrete_laplacian_chip_firing.py` and the registry.

These do not replace the reconstructed closed-frame Laurent defect + finite X-ray kernel + exposed reconstruction capability, but they prevent `DIFF1`, a bare adjoint name, or “a Laplacian factorization exists” from being claimed as standalone new T1 value.

## Required narrower interface

Any future integration should at minimum split the candidate surface as follows:

Core typed closed-frame algebra:

- `DECLARE_FRAME`
- `DIFF1`
- `RHOMBUS2`
- `TRIPLE_DEFECT`
- `FRAME_WIDTH`

Finite tomography specialization:

- `XRAY_KERNEL_CERT`
- `MULTIFRAME_UNIQUENESS`
- `EXPOSED_AUGMENT`

Adjoint/chirality specialization:

- `CHIRALITY_AUGMENT_FULL`
- `COMPRESSED_GRAM_AUGMENT(characteristic, invertibility_certificate)`
- `GRAM_FACTOR`

Load-bearing preconditions must be typed: closed three-direction frame, orientation, primitive ray identifiers, duplicate-unoriented-ray control, coefficient domain/characteristic where relevant.

Explicitly excluded from the interface:

- finite-support translation-invariant deghosting;
- native trace quotient inferred from endpoint closure;
- characteristic-uniform compressed-Gram recovery;
- Y–Delta / arbitrary Schur-complement response equivalence.

## Why this verdict

`ACCEPT_T1_TRIAXIAL_DIRECTIONAL_DEFECT_GLOBAL_SUBTOOL` is too strong because the present proposed interface conflates distinct adjoint/Gram semantics and omits load-bearing type/precondition boundaries.

`ACCEPT_AS_DOMAIN_OPERATOR_ONLY` is too narrow because the same exact operator implementation passes the independent Hive/rhombus reuse test.

`REJECT_TOOL_UPGRADE` is too strong because, after Phase-B dedup, the finite-X-ray kernel/exposed-reconstruction capability remains a real shared-tool gap.

Therefore the only supported disposition is:

**`NEEDS_NARROWER_TOOL_INTERFACE`**

## Evidence

- implementation: `src/enterprise_math/triaxial_directional_defect.py`;
- unit regressions: `tests/test_triaxial_directional_defect.py` — `11/11 PASS` in independent local execution;
- checker: `research_output/evidence/triaxial_directional_defect_independent_checker.py`;
- Phase-A frozen return: `research_returns/TRIAXIAL_DIRECTIONAL_DEFECT_INDEPENDENT_TOOL_VERIFICATION_PHASE_A_RETURN_20260825.md`;
- full report: `research_outputs/TRIAXIAL_DIRECTIONAL_DEFECT_INDEPENDENT_TOOL_VERIFICATION_20260825.md`.
