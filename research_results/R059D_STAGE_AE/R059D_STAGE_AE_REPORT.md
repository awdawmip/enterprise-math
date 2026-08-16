# R059D Stage AE — Count-First Outward-Convexity Threshold and Inverse Law

Researcher-ID: `EM-R059D-AE-5C91D4`
Task-ID: `RS-R059D-STAGE-AE-COUNT-FIRST-OUTWARD-CONVEXITY-INVERSE-LAW`
Taskbook source: `b2be905b4a809ad5af86cd82c7ade53ad60c115a`
Frozen base: `c5f3c2668ceda46dc1094b2349fb4fe7ad3891b3`
Accepted AD source head: `d5270439d41ab2a421195d7387d6c819eba4bf56`

## Primary disposition

`NO_OUTWARD_CONVEXITY_THRESHOLD_THROUGH_AUDIT_RANGE`

The accepted AD N/C resolvers were replayed from exact generator semantics for `r=1..64`. Resolver C uses frozen sampling `s=64`; an exact full-range replay at `s=128` gives identical C occupancy for every radius 1..64.

## 1. Count semantics calibration

The AE first gate was not allowed to identify the user's D/C/V labels by formula fitting. Natural counts from the AD binary triangular disks were enumerated at r=1,2,3.

The one typed carrier that reproduces all controls for both N and C is the `EDGE_SUPPORTED_DUAL_CELL_CARRIER`:

- a triangular-lattice vertex is a dual-cell state iff it is the endpoint of at least one edge shared by two occupied AD triangles;
- `V` = total number of selected dual cells;
- `D` = selected dual cells on one full opposite-axis diameter (`b=0`), endpoints included;
- `C` = selected dual cells with at least one of their six dual neighbors absent.

This gives exactly:

| r | D | C | V |
|---:|---:|---:|---:|
| 1 | 3 | 6 | 7 |
| 2 | 5 | 12 | 19 |
| 3 | 7 | 18 | 37 |

for both N and C.

Rejected as the common D/C/V carrier include raw occupied-triangle count, triangle shell increment, interface-edge count, one-or-more-incidence vertex count, full-star interior count, and axis transition count.

## 2. Zero-bulge baseline

In the canonical 60-degree sector the predeclared zero-bulge path is

`P0(r) = [(r-k,k): k=0..r]`

with constant internal step `(-1,+1)`. Its D6 completion is the combinatorial baseline dual disk

`H_r = {(a,b): max(|a|,|b|,|a+b|)<=r}`.

No Euclidean chord, area, curvature, distance, sqrt, or pi enters this definition.

For both N and C and every audited `r=1..64`:

- `H_r` is a subset of the resolved dual disk `S_X(r)`;
- no extra selected cell lies on a native axis;
- extra cells occur in free D6 orbits of size six;
- the dual boundary is a single D6-symmetric closed cycle;
- `D=2r+1`.

Define the official open-sector bulge count

`B_X(r) = #(S_X(r) \ H_r, a>0,b>0) - #(H_r \ S_X(r), a>0,b>0)`.

In the census the second term is identically zero, but it remains part of the signed definition.

## 3. Critical-radius result

Both N and C satisfy `B(r)=0` for `r=1,2,3,4`, and both first satisfy `B(r)>0` at `r=5`.

Therefore:

- `LAST_ZERO_BULGE_RADIUS_N = 4`
- `LAST_ZERO_BULGE_RADIUS_C = 4`
- `FIRST_POSITIVE_BULGE_RADIUS_N = 5`
- `FIRST_POSITIVE_BULGE_RADIUS_C = 5`.

However Stage AE explicitly required a stable strict outward-convex regime of at least eight consecutive radii, not merely positive bulge.

With the frozen internal turn convention:

- N is strictly outward convex only on `r=5..10` (length 6);
- C is strictly outward convex only on `r=5..11` (length 7);
- no later qualifying run occurs through `r=64`.

Thus neither family reaches the required 8-radius stability window:

- `FIRST_STABLE_OUTWARD_BULGE_RADIUS_N = null`
- `FIRST_STABLE_OUTWARD_BULGE_RADIUS_C = null`.

The shared `r=5` event is therefore frozen only as a resolver-independent first positive-bulge onset, not as the stable outward-convexity threshold requested by the taskbook.

## 4. Exact count and inverse identities

The D6 decomposition yields, on every audited N/C row,

`V = 1 + 3r(r+1) + 6B`.

Since `D=2r+1`, this gives the exact audited inverse bulge identity

`B = (4V - 3D^2 - 1)/24`.

Let the per-sector boundary excess be `J = (C-6r)/6`. Then

`C = 6r + 6J`

and

`J = (C - 3(D-1))/6`.

The shell-difference identity is

`DeltaV = 6r + 6 DeltaB`,

hence

`DeltaV - C = 6(DeltaB - J)`.

Therefore `DeltaV=C` is not a universal law. It holds exactly when the current bulge increment equals the current boundary-excess count.

## 5. Exact zero-bulge laws

For the certified zero-bulge regime `r=1..4`, `B=J=0`, so the baseline gives exact formulas

`D = 2r+1`,

`C = 6r`,

`V = 1 + 3r(r+1)`.

Eliminating r gives

`C = 3(D-1)`,

`V = (3D^2+1)/4`,

`V = C^2/12 + C/2 + 1`.

These are proved from the D6 constant-step baseline and are not extrapolated from the three user controls.

## 6. Transient post-bulge candidate and holdout failure

After `r=5`, both resolvers temporarily satisfy

`B=r-2`,

`C=6(r+1)`,

`V=3r^2+9r-11`

for `r=5..10`.

This apparent law is not promoted:

- N fails it at `r=11`;
- C still matches at `r=11` but fails at `r=12`.

Thus the first post-bulge pattern is a transient candidate, not a stable inverse law.

The original candidate `C=6r` and centered-hex `V=1+3r(r+1)` both first fail at `r=5`; `D=2r+1` survives the entire audited range for both families.

## 7. Resolver comparison

N and C agree on the first positive-bulge onset and on the zero-bulge regime, but their count ledgers diverge at 17 radii through 64. First differing radii are

`11,15,21,24,28,31,34,38,39,44,45,49,52,53,54,57,58`.

They re-agree by `r=64` (`D=129, C=444, V=15043, B=427`), but no single stable post-transition polynomial/rational law is promoted from this coincidence.

## 8. Precision audit

N is sampling-independent by definition.

For C, `s=64` was frozen before scoring. Exact replay at `s=128` gives identical binary C occupancy for every mandatory radius `r=1..64`.

Earlier `s=32` controls differ from `s=64` at difficult radii 24 and 53, so the higher frozen precision is materially necessary. No threshold was retuned.

## 9. Semantic firewalls

No classical pi, Euclidean curvature, Euclidean area, Euclidean equal-distance, classical square root, or radius-specific threshold/scan tuning was used to generate or select the AE laws. Candidate formulas were evaluated only after raw rows were generated.

AD remains immutable. Resolver R is not promoted. No AF or later result is consumed.

## 10. Status vector

- `COUNT_SEMANTICS_STATUS = EDGE_SUPPORTED_DUAL_CELL_CARRIER_CALIBRATED`
- `LAST_ZERO_BULGE_RADIUS_N = 4`
- `LAST_ZERO_BULGE_RADIUS_C = 4`
- `FIRST_POSITIVE_BULGE_RADIUS_N = 5`
- `FIRST_POSITIVE_BULGE_RADIUS_C = 5`
- `FIRST_STABLE_OUTWARD_BULGE_RADIUS_N = null`
- `FIRST_STABLE_OUTWARD_BULGE_RADIUS_C = null`
- `RESOLVER_INDEPENDENT_FIRST_POSITIVE_BULGE = true`
- `RESOLVER_INDEPENDENT_THRESHOLD_CANDIDATE = false`
- `ZERO_BULGE_INVERSE_LAWS = PROVED_ON_CERTIFIED_REGIME`
- `GLOBAL_BULGE_INVERSE_IDENTITY = PROVED_ON_AUDIT_RANGE`
- `POST_BULGE_CLOSED_FORM = UNDERDETERMINED / TRANSIENT_CANDIDATE_ONLY`
- `PRIMARY_DISPOSITION = NO_OUTWARD_CONVEXITY_THRESHOLD_THROUGH_AUDIT_RANGE`

## 11. Checker

The deterministic checker regenerates N and C for every `r=1..64`, reconstructs the edge-supported dual carrier, D6 baseline, bulge and turn words, verifies the exact inverse identities, and checks C `s=64` against `s=128` over all mandatory radii.

Final mathematical/semantic replay before the external Git-history gate:

`2692/2692 PASS`

Digest:

`5eaf3b8821001ac7451556d4022815e95f99f37b6e45e50af2ad91b21a3802f2`.
