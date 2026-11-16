# Unit 68 — native signed-X6 BRC mass is not determined by min-zero observation, quadratic grade and event count

Date: 2026-11-17. Mother Task: `RS-X6-LEGACY-PLANE-RECONCILIATION`; LP019/LP023/LP026. Author-side status: **EXACT PROOF / LOCAL CHECK EXECUTED / UNREVIEWED / NOT_ADMITTED**. Native Source semantic publication: **pending genuine current CLAIM/RUN**.

## Immutable input and precise type

Use the **frozen** scientific source `59538f585d037d09ef687b28715c4bc1a3f9fe03`, `p000_reality_foundation.json`, `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`, and `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` (actual observed blob `300a96e3dc24bf6fff73743037a0347a8bc83176`). Work in the actual three-axis signed sub-torsor of `Z^6`, with the other three coordinates identically zero. Define `can3(x)=x-min(x)(1,1,1)`, native component square `G(x)=sum_i x_i²`, shortest native event count `T(x)=sum_i |x_i|`, and nonnegative natural BRC path multiplicity `N(x)=T(x)!/prod_i |x_i|!`.

## All-positive-integer obstruction family

For **each** `m>=1`, take the distinct signed native endpoint displacements (six coordinates)

```
x_m=(0,-3m,-3m,0,0,0)
y_m=(4m, m, m,0,0,0).
```

Their selected three-axis min-zero observations are **identical**:
`can3(x_m[:3])=can3(y_m[:3])=(3m,0,0)`, taking the first three signed coordinates of each six-axis vector. Moreover

```
G(x_m)=G(y_m)=18m²,    T(x_m)=T(y_m)=6m,
N(x_m)=(6m)!/((3m)!)²,
N(y_m)=(6m)!/((4m)!(m!)²).
```

For every positive integer `m` the ratio is

```
N(y_m)/N(x_m) = product_{j=1}^m (m+j)(2m+j) / [j(3m+j)] > 1,
```

since **each** numerator minus its corresponding denominator is `2m²>0`. This is a complete universal integer proof. At `m=1`, the two endpoints have the same `(can3,G,T)=((3,0,0),18,6)`, but shortest positive natural BRC counts are **20** and **30**. Both use length 6, so the inequality persists at the **same fixed native path length** `endpoint_multiplicity(6,z)`.

Consequently there is no function `F` with `N(z)=F(can3(z_S),G(z),T(z))` on the whole selected signed native slice. The lossless observer pair `(can3(x_S),h=min(x_S))` repairs the raw three-axis coordinates; if BRC path provenance is needed, retain native step data or the exact multiplicity. The result does not assert a discovered historical consumer bug; the outstanding LP019 historical erroneous *positive-count subtraction* caller remains unlocated.

## Actual finite verification

A standalone independent Python integer checker was **executed** in normal, `-O`, `-OO` modes: all 128 values `m=1,...,128` passed exact factorial and independently assembled binomial counts; for `1<=m<=5`, an additional memoized native shortest-word recurrence verifies both endpoint counts. The script checks equal `can3`, `G`, `T`, strict multiplicity separation, and the all-m factor-product identity. Independent BigInt factorial verification reproduced the reported samples.

Frozen `signed_brc.py` bytes were **read and matched by exact formulas**, but the original frozen Python module was not imported or executed in this unit. The original R063/Helly native benchmark remains unchanged.

## Source-level consumer consequence

Production `src/enterprise_math/diagonal_quotient.py` (observed main Git blob `a527e347e33d0a0039258a9b25f48b1f1466d149`) correctly labels `canonical_min_zero` a representation operator; `src/enterprise_math/p022_geodesic_multiplicity.py` (blob `46373050168d2430b6cb3952aa763f3081284632`) exposes endpoint-based positive path count. Neither source is accused of conflating the layers. For an adapter combining these APIs, the exact `(can3,G,T)` fiber collision above is a regression witness: **observer equivalence + squared native grade + length are insufficient to supply BRC endpoint weights**.

## Continuation / provenance

- Parent objective: source-attested 28-LP typed ledger, full active-current consumer dependency closure, independent Driver `REQUEST_REVISION`.
- Invariant science pins: current `59538f585d037d09ef687b28715c4bc1a3f9fe03`; old `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.
- Do not repeat: original R063/Helly, Unit66 three-sector exact count, Unit67 Viète signed-reversal proof.
- Existing Researcher/SID: `EM-X6-FB6990` / `MCP-082892eb480e45dea6d4b9fcc0491034` (Research lane only).
- Pending original control reads: `onhour-20261117-0004-x6-continuation-read-v1`; original new CLAIM request `onhour-20261117-0011-x6-own-claim-after-typed-prepare-v1`; **do not resubmit**. Fresh original CLAIM/RUN and Native semantic PROGRESS require Source-winning readback.
- Next exact action: reconcile both original requests; if own CLAIM/RUN becomes genuinely authorized, Source-checkpoint already saved Unit66–68; then locate active downstream callers requiring `N_BRC` from min-zero grade and complete historical LP011/LP019 exact file:line source attribution without inventing a culprit.

Scientific review: **UNREVIEWED / NOT_ADMITTED**. Publication of this note is author evidence, not native Task/Review acceptance.
