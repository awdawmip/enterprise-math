# 进取最短路径族：固定端点后的反向 realization fiber

Status: `RETAINED / REVERSE_GEODESIC_REALIZATION_ONLY / SUPERSEDED_AS_SEGMENT_LENGTH_ONTOLOGY`
Date: `2026-08-17`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Current foundational route:
`definitions/ENTERPRISE_VECTOR_NORM_ENDPOINT_REVERSE_GEODESIC_SEGMENT_20260817.md`

## 1. Retained theorem

For a fixed native endpoint cell `P`, define

`GEO_REV_E(P)`

as the complete family of paths from `VOID_E` to `P` using the minimum possible primitive jump count. Equivalently, delete the unique first edge `VOID_E->O_E` and retain all minimum-jump spatial tails from `O_E` to `P`.

Freeze:

`ALL_REVERSE_SHORTEST_REALIZATIONS_ARE_RETAINED`.

No minimizer is privileged or deleted merely to fit a desired perimeter/circle.

## 2. Foundational correction

The old identification

`segment length = minimum jump count`

is superseded.

The current logic is:

`native cumulative vector length -> endpoint cell P -> GEO_REV_E(P)`.

Therefore shortest paths do not select the radius level. They realize an endpoint already selected by vector norm.

Freeze:

`SHORTEST_PATH_LENGTH_IS_NOT_FOUNDATIONAL_SEGMENT_LENGTH`.

## 3. Spatial footprint remains derived

For fixed `P`, the reverse geodesic footprint may still be defined as unions over all minimizers:

- `VERT_GEO_REV(P)`;
- `EDGE_GEO_REV(P)`;
- induced triangle/cell incidence as secondary structure.

A chosen chain, strip, packet, or representative geodesic is not canonical unless proved equivalent to the whole reverse fiber.

## 4. Local geodesic moves

Equal-endpoint local deformations among minimum-jump paths remain a valid realization-level question. Triangle `1->2` detours, `2<->2` exchanges, and related moves are typed only inside the reverse realization fiber.

They do not determine the vector radius.

## 5. Current route

Read first:

`definitions/ENTERPRISE_VECTOR_NORM_ENDPOINT_REVERSE_GEODESIC_SEGMENT_20260817.md`.
