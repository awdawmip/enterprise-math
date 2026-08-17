# Driver Review — Signed Origin-One Coordinate Correction and Square/Root Restoration

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Date: `2026-08-17`
Disposition: `DRIVER_ACCEPTED__SIGNED_ORIGIN_ONE__ZERO_ABSENT__SQUARE_ROOT_RESTORED`

## User supersession

The user supplied the decisive native-coordinate correction:

- the Enterprise origin is the single glued state represented by `+1` and `-1` simultaneously;
- `+1 ≡ -1 ≡ O_E`;
- `0` does not occur in the Enterprise coordinate system;
- one negative primitive step from the origin lands at `-2`, not `-1`;
- one positive primitive step lands at `+2`;
- in three-axis notation the origin may be represented by `(±1,±1,±1)`.

This supersedes the previous one-sided origin-one interpretation that retained only positive native coordinate values.

## Exact counterexample to the shifted square rebuild

The user supplied the native quadrilateral

`Q=((±1,±1,±1),(2,1,1),(1,-2,1),(1,1,2))`.

Freeze:

`PERIMETER_E(Q)=4`

`AREA_E(Q)=4`.

The recently proposed shifted law

`ENTERPRISE_SQUARE(n)=1+(n-1)^2`

would give `ENTERPRISE_SQUARE(2)=2`, contradicting this exact native calibration.

Therefore that rebuild is rejected.

## Correct square/root status

Restore:

`ENTERPRISE_SQUARE(n)=n^2`, `n>=1`

`ENTERPRISE_ROOT(n^2)=n`, `n>=1`.

No `0` square-state is included in the native coordinate domain.

The quantity `n-1` remains only the external primitive-adjacency distance from the glued origin to `±n`; it does not redefine the native coordinate magnitude `n`.

## Signed-axis topology

Canonical one-axis state space:

`A_E={O_E}∪{+n,-n:n>=2}`

with `O_E=[+1]=[-1]` and adjacency

`...,-4~-3~-2~O_E~+2~+3~+4,...`.

## Auxiliary chart consequence

The legacy signed integer chart has a canonical no-zero reencoding:

`ENC_SIGNED(0)=O_E`

`ENC_SIGNED(k)=sign(k)(|k|+1)` for `k!=0`.

Thus R059D combinatorial results remain preserved. Full native status should be restored only after an explicit conjugacy audit of the turn/rotation/canonicality machinery under this encoding.

## Canonical files

- `definitions/ENTERPRISE_SIGNED_ORIGIN_ONE_COORDINATE_20260817.md`
- `definitions/ENTERPRISE_SQUARE_AND_ROOT_SIGNED_ORIGIN_ONE_20260817.md`
- `definitions/ENTERPRISE_COORDINATE_SYSTEM_AND_BRC_BRIDGE_20260816.md`

The immediately preceding files based on one-sided origin-one or shifted square/root are superseded.
