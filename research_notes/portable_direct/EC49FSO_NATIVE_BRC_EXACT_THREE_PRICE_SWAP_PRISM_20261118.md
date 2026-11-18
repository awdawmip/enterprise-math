# EC49FSO — Exact three-parameter native BRC price prism and sharp swap boundary

Date: 2026-11-18. Independent portable scientific continuation of EC49FSN PR #2706 at immutable commit `0842017a6bfdc83e7af59c6d2be0493dd53d58da`. Frozen original scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. The original finite BRC16943 system retains 310 configurations, 141 distinct fully named joint-response profiles, 228 original physically named observations, the uniform prior over profiles, and unrestricted deterministic adaptive decision trees.

Define `F(a,b,z)=141 V(a,b,z)/t`, where the price of q32, q34, q140 is `(1-a)t, (1-b)t, (1-z)t` respectively; other observations cost `t>0`.

## Exact continuum theorem (a full three-dimensional prism)

For **every real** `a in [31/64,33/64]`, `b in [27/64,29/64]`, `z in [0,51/448]`,

```text
F(a,b,z) = 306 - 141a - 41b - 4z
F(b,a,z) = 306 - 141a - 41b - 10z
F(a,b,z) - F(b,a,z) = 6z.
```

The strict swap penalty therefore extends to an open-volume three-parameter family for all `z>0`, rather than a single fixed (a,b) price line. No q32/q34 sensor-automorphism assumption is used.

## Complete exact Bellman vertex evidence

Each row reports `F(a,b,0)=F(b,a,0)`, `F(a,b,51/448)`, `F(b,a,51/448)` respectively.

| a | b | z=0, both | z=51/448, direct | z=51/448, swapped |
|---|---|---|---|---|
|31/64|27/64|7053/32|49269/224|12279/56|
|31/64|29/64|1753/8|24491/112|48829/224|
|33/64|27/64|216|24141/112|48129/224|
|33/64|29/64|6871/32|47995/224|23921/112|

All 16 orientation-specific vertex values were checked by the **unrestricted exact Bellman recurrence** over the original 228 observation partitions:

```text
T(singleton)=0
T(S)=min_{q strictly splits S} (|S| p_q + sum_r T(S∩C(q,r))).
```

The independently redecoded original-family solver confirmed both top-corner orientations at `(31/64,27/64,51/448)` (respectively `49269/224` and `12279/56`); another independent corner replay at z=0 was also completed. Each cost calculation used integer-denominator exact rational arithmetic. The inherited source modules check the frozen data hashes and reproduce all named response partitions.

Full admissible 141-state decision tree witnesses have `(U,N32,N34,N140)` vectors:

* Direct `(306,141,41,4)`: canonical JSON SHA256 `ad7047debd6d04d3c076eef6d593b7de4d50879a671a439760d4d436210cc767`.
* Swapped `(306,41,141,10)`: canonical JSON SHA256 `db669e0116a1816bbf53fed6cb1bc07a4549ef9665637433e05c059936ff9742`.

Both witnesses are retained in the immutable EC49FSN native tree bundle. The local self-contained EC49FSO evidence archive additionally carries their exact original JSON, the raw data, source modules, machine-readable certificate, validation runner and execution results. All three witnesses (including the sharpness challenger below) passed complete native-response leaf replay.

## Proof for every real point

For each fixed complete original-native tree `T`, its cost `U_T - a N32_T - b N34_T - z N140_T` is affine in three prices. Consequently `F = min_T cost_T` is **jointly concave** over `[0,1]^3`. The two feasible trees above give affine upper bounds for their respective orientations. The 8 prism vertices per orientation exactly attain these bounds by the global 228-observer Bellman recurrence. Every prism point is a convex combination of those vertices; concavity gives the affine lower bound at every such point. These lower and upper bounds coincide, proving the displayed identities on the complete continuous prism.

## Exact sharpness of the z ceiling for this rectangle

At the swapped corner `a=31/64, b=27/64`, an additional feasible full 141-profile tree has counts `(303,32,141,17)` and exact canonical JSON SHA256 `c43c37dfca7f748b0e4acadcd69c8be5e8c5bdeb3a0515c6c7e8c796250042e2`. Its cost minus the asserted swapped prism plane is

```text
[303-32b-141a-17z] - [306-41b-141a-10z]
= -3 + 9b - 7z = 51/64 - 7z.
```

The crossing occurs **exactly** at `z=51/448`. For any larger z the challenger strictly beats the swapped prism plane. The direct optimum remains on its original affine plane up to at least z=1/8 at this corner: the endpoint z=1/8 was checked by exact unrestricted Bellman and has the same direct tree; concavity closes the intervening segment. Hence `F(a,b,z)-F(b,a,z)>6z` at this fixed corner throughout `51/448<z<=1/8`. At z=1/8 the swapped challenger has global cost `14021/64`, while the old plane would be `7013/32`, an exact improvement of `5/64`. Therefore **51/448 is the sharp largest uniform prism height for the 6z identity** over the stated (a,b) rectangle.

## Reproducibility and classification

Evidence scope: original 141-profile, all-228 physically named BRC16943 finite model; both exact native-tree response decoders; three fully replayed lossless trees; 16 exact Bellman vertices and at least 3 independent decoder crosschecks. All validation is deterministic rational/integer arithmetic. A Git repository path/hash locates evidence but is not mathematical acceptance.

Status: `AUTHOR_PROVED / EXACT_PRIMARY_FINITE_EXHAUSTIVE / INDEPENDENT_PARTIAL / NOT_REVIEWED`.

Next research: classify how the certified `6z` phase extends in (a,b), find the earliest additional 3D Pareto facets, and examine the zero set near `a=b` without presupposing a named-observer exchange symmetry. Independent portable source material only; current formal Task CLAIM/Result/Review/Activity linkage remains separately governed. Historical author identity: `EM-DIRECT-8454C6`; historical Activity `RA-ED136F89271FD89288F3E58D`.
