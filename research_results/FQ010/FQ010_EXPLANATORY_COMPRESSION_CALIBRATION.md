# FQ010 — Explanatory-Compression Calibration

Researcher-ID: `EM-FQ010-CA2555`

## Calibration rule

The current line/trace definition is used only after Interface K has been independently constructed from R065 relation evidence. No current `LENGTH`, `L_E^2`, sum-of-squares formula, or scalar output is used to define `R_type` or select its cardinality.

Allowed downstream source:

`definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md@9866e523b7e7f134497d8aca9ba2b6a093600257`.

## 1. Shuffle invariance at fixed component content

Current line identity is the component trace

`T_{a,b}^{(ij)}=[X_i^a X_j^b]`

modulo component-preserving commutation. All shuffle realizations have the same component multiplicities.

Interface K depends only on the type fibers, so every shuffle realization induces the same `R_type` up to token renaming and hence the same `Q_K`.

Classification: `EXACT_RECOVERY`.

This recovery is stronger than merely observing equal scalar values because the relation itself is invariant up to the admitted presentation changes.

## 2. Transition/word length versus native line scale

Occurrence-level observation has diagonal-cardinality readout

`Q_fine=a+b`,

which is the count of transition letters after the unique origin-incidence step is separated.

Component-kernel cardinality gives

`Q_K=a^2+b^2`.

Thus the two quantities arise from different observation relations on the same typed token content.

For the current `(3,4)` calibration witness:

- transition-letter count: `7`;
- component-kernel cardinality: `25`;
- current native length: `5`.

The equality `sqrt(Q_K)=5` is used only as downstream scalar calibration; the structural distinction between diagonal and component-kernel relations exists independently.

Classification: `EXACT_RECOVERY` of the distinction on the declared origin-based sector domain.

## 3. Axis scaling

For a one-component trace with multiplicity `n`,

`Q_K=n^2`.

Under the existing trace scaling law

`(T_{a,b})^k=T_{ka,kb}`,

component-fiber sizes multiply by `k`, so

`Q_K(ka,kb)=k^2 Q_K(a,b)`.

No metric is needed for this relation/cardinality statement.

Classification: `EXACT_RECOVERY` of quadratic squared-readout scaling.

Its interpretation as squared native line scale remains an N2 semantic assignment.

## 4. Two-component additivity / transverse independence

The component relation decomposes exactly as

`R_type=(U_i x U_i) disjoint_union (U_j x U_j)`.

Therefore

`Q_K(a,b)=|U_i|^2+|U_j|^2`.

No cross-component relation-pairs exist, so changing one component cannot alter the marginal pair contribution of the other. This is exactly the FQ008 zero mixed-second-difference property.

Classification: `EXACT_RECOVERY`.

## 5. Component provenance

`R_type` retains the partition into same-component blocks before scalarization. This is aligned with the current line identity, which preserves native component trace across shuffle-equivalent path representatives.

The scalar `Q_K` alone does not retain this provenance, as the explicit collisions at `25` and `65` show.

Classification:

- relation layer: `EXACT_RECOVERY` of component-provenance structure up to admitted relabeling;
- scalar layer alone: `NONRECOVERY` of provenance.

## 6. Current line-length formula

The current source states sector-local

`L_E^2=a^2+b^2`.

Interface K gives the same scalar exactly on the same origin-based sector domain:

`Q_K=a^2+b^2`.

Classification: `DOMAIN_RESTRICTED_RECOVERY`, because the current line definition itself leaves arbitrary point-to-point and cross-sector metric/trace gluing open.

The formula agreement is not used as the sole evidence for K. It comes after relation canonicity, maximality, observation-resolution classification and valuation analysis.

## 7. Compression verdict

Interface K explains multiple previously separated facts from one independently definable relation plus one readout choice:

- shuffle invariance;
- component provenance;
- separation from occurrence/word count;
- axis-square behavior;
- transverse independence;
- quadratic replication of the squared readout.

This is genuine explanatory compression beyond pointwise formula recovery.

However, the compression stops at the semantic boundary identified by R065 and FQ010:

- component-kernel cardinality is not uniquely forced among all intrinsic scalars;
- the squared-line-scale role still requires a separate N2 declaration or calibration.

Therefore the calibration evidence supports **hybrid structural admission**, not an N0 claim that cardinality is the uniquely forced scale.

`EXPLANATORY_COMPRESSION_TESTED_BEYOND_POINTWISE_FORMULA_RECOVERY = PASS`.
