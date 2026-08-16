# R059D Stage AE — Driver Review

Date: `2026-08-17`
Driver-ID: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Reviewed owner branch: `research/r059d-stage-ae-count-first-outward-convexity`
Reviewed owner head: `f8b56c910150ecd04d7e30ac03ea5bf0083b9429`
Task: `RS-R059D-STAGE-AE-COUNT-FIRST-OUTWARD-CONVEXITY-INVERSE-LAW`

## Driver disposition

`DRIVER_ACCEPTED__FIRST_BULGE_ZERO_BOUNDARY_ESTABLISHED_AT_R4_TO_R5__STABLE_POST_BULGE_LAW_OPEN`

Stage AE is accepted.

The taskbook-level primary disposition `NO_OUTWARD_CONVEXITY_THRESHOLD_THROUGH_AUDIT_RANGE` is preserved as an exact statement about the *additional eight-consecutive-radius strict-convexity gate* introduced by the taskbook, but it is not the Driver-level answer to the user's original question.

The user's requested target was the first zero-boundary where the counted path leaves the zero-bulge baseline. On that target AE succeeds exactly and resolver-independently:

- `LAST_ZERO_BULGE_RADIUS_N = 4`
- `LAST_ZERO_BULGE_RADIUS_C = 4`
- `FIRST_POSITIVE_BULGE_RADIUS_N = 5`
- `FIRST_POSITIVE_BULGE_RADIUS_C = 5`

Therefore freeze:

`FIRST_BULGE_ZERO_BOUNDARY = 4 -> 5`

and

`RESOLVER_INDEPENDENT_FIRST_BULGE_ONSET = true`.

## Count semantics accepted

The common user controls

- `r=1: D=3, C=6, V=7`
- `r=2: D=5, C=12, V=19`
- `r=3: D=7, C=18, V=37`

are not treated as formula-fit labels. AE identifies a common typed carrier:

`EDGE_SUPPORTED_DUAL_CELL_CARRIER`.

Accepted meanings:

- `V`: total selected dual-cell states;
- `D`: selected dual cells on a full opposite-axis diameter, endpoints included;
- `C`: selected dual cells having at least one absent dual neighbor.

This carrier reproduces all three user controls for both AD resolvers N and C.

## Exact zero-bulge regime

For `r=1..4`, both N and C exactly equal the D6 baseline dual disk and satisfy:

`D = 2r+1`

`C = 6r`

`V = 1 + 3r(r+1)`.

Equivalent inverse identities:

`C = 3(D-1)`

`V = (3D^2+1)/4`

`V = C^2/12 + C/2 + 1`.

These formulas are accepted as the exact certified zero-bulge law, not as global circle laws.

## Global bulge identities accepted on audited range

For both N and C over `r=1..64`:

`D = 2r+1`.

Let `B` be the signed open-sector bulge-cell count relative to the D6 zero-bulge baseline. Then:

`V = 1 + 3r(r+1) + 6B`.

Hence:

`B = (4V - 3D^2 - 1)/24`.

This is the strongest AE inverse identity and is accepted on the audited range.

Let `J=(C-6r)/6` be the per-sector boundary excess. Then:

`C = 6r + 6J`

and

`DeltaV - C = 6(DeltaB-J)`.

Therefore the early identity `DeltaV=C` is not universal. It holds exactly only when `DeltaB=J`.

## Post-bulge law status

At `r=5` both accepted AD resolvers leave the baseline for the first time.

Both temporarily satisfy for `r=5..10`:

`B=r-2`

`C=6(r+1)`

`V=3r^2+9r-11`.

This is explicitly rejected as a global law:

- resolver N fails at `r=11`;
- resolver C fails at `r=12`.

N and C differ at 17 audited radii through 64, even though they agree again at `r=64`.

Thus the post-bulge structure is not a single currently established low-degree polynomial/rational law. The correct next object is the integer correction process carried by `B`, `J`, and their jump structure.

## Stable strict convexity gate

The taskbook required eight consecutive radii of a stronger strict-turn convexity property.

Observed:

- N strict run: `r=5..10` (length 6);
- C strict run: `r=5..11` (length 7);
- no qualifying 8-radius run through `r=64`.

Freeze separately:

`STABLE_STRICT_OUTWARD_CONVEX_REGIME_NOT_ESTABLISHED_THROUGH_R64`.

This does not negate the already-proved first bulge zero-boundary at `4 -> 5`.

## Precision and verification

- C frozen sampling `s=64` equals `s=128` for every `r=1..64`;
- checker: `2692/2692 PASS`;
- checker digest: `5eaf3b8821001ac7451556d4022815e95f99f37b6e45e50af2ad91b21a3802f2`;
- prior AD results remain immutable.

## Driver interpretation

Stage AE changes the frontier.

The primary open problem is no longer whether the counted circle ever leaves the centered D6 baseline. It does, first at `r=5`, with resolver-independent onset.

The open problem is now to characterize the post-onset integer correction law:

`baseline hex growth + 6 * bulge correction`.

The next investigation should study the jump sequence of `B(r)` and `J(r)`, their finite differences, motif/period structure, and any resolver-independent invariant before fitting a closed form.

No new resolver is selected here.

`STOP_FOR_NEXT_DRIVER_DECISION`
