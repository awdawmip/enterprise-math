# R061 Stage 0 — Three-Sector Covariance and Axis Gluing

## Formal cyclic covariance

The coordinate and free-word construction is exactly covariant under

`1 -> 2 -> 3 -> 1`.

The same `D_N` is used in every sector and the same theorem applies to:

- `S_12`: `(X1,X2)`;
- `S_23`: `(X2,X3)`;
- `S_31`: `(X3,X1)`.

Under cyclic relabeling, word lengths, binomial counts, formal endpoint maps,
and native sector squared-length values are unchanged.

Therefore:

`THREE_SECTOR_COVARIANCE_PASS_FORMAL = true`.

## Axis branch gluing

For `N=r^2`, axis-degenerate coordinate decompositions are `(r,0)` and
`(0,r)` in a local two-axis chart.

A physical positive axis belongs to the two adjacent sector charts. The
formal global coordinate fiber must identify chart duplicates by **physical
axis label plus radial coordinate**, not by raw ordered-pair position.

Exact coordinate gluing relations:

- `S_12:(r,0)` is the same `E1` axis branch as `S_31:(r,0)`;
- `S_12:(0,r)` is the same `E2` axis branch as `S_23:(r,0)`;
- `S_23:(0,r)` is the same `E3` axis branch as `S_31:(0,r)`.

For `r>0`, this leaves exactly three physical positive-axis coordinate
branches globally, one per `E_i`, rather than six chart copies. At `r=0`,
the unique coordinate vertex is the common origin and is not a cell.

Therefore:

`AXIS_GLUE_DEDUP_PASS_FORMAL = true`.

## Why the full native gates remain open

The current foundation does not yet specify:

- which incident start cell at `O_E` belongs to which sector trajectory;
- the affine map from those incident cells to absolute center addresses;
- the native chart-transition map for cross-sector cell trajectories.

The third-axis audit also proves that full carrier path realizations mix
direction families in a way not represented by a sector-local two-positive
shuffle.

Therefore the formal covariance/dedup theorem cannot be promoted to a full
native path-gluing theorem in this stage.

`THREE_SECTOR_COVARIANCE_PASS = false` for the complete candidate native
formula.

`AXIS_GLUE_DEDUP_PASS = false` for complete native trajectories, despite the
exact coordinate-level dedup rule above.
