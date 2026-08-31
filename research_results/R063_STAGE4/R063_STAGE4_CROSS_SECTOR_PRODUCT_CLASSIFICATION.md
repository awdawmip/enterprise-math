# R063 Stage 4 — Cross-Sector Product Classification

Status: `CLASSIFIED`

## 1. Shared-axis input

A path on a shared native axis has two adjacent chart presentations. The strict square conflict from Stage 4 shows that absolute-phase object multiplication can depend on which chart is used.

Therefore overlap representation alone does not define one chart-independent ordered product.

## 2. Interior `S12` x interior `S23`

No frozen Stage 3 chart contains all three native positive-axis tags `E1,E2,E3`. Hence an interior path from `S12` and an interior path from `S23` cannot be fed into one local Stage 3 product without first choosing process transport/retyping into a common process fiber.

Define a route-indexed process product by choosing a target sector `T` and routes `gamma,delta`:

`P box_T^(gamma,delta) Q = Transport_gamma(P) box_T Transport_delta(Q)`.

This is well typed at the N1 process level when the routes and target fiber are retained.

Changing a transport route by one sector loop changes the absolute output phase by the nonzero holonomy (plus the exact affine tensor defect when both operands are transported). Hence the object-level result is route dependent.

## 3. Direct-versus-long route witness

For `S12 -> S23`, the direct phase shift is `k_12,23`.

The alternate route `S12 -> S31 -> S23` has shift `-k_31,12-k_23,31`.

Their difference is exactly

`H = k_12,23+k_23,31+k_31,12`.

Since `H` is odd, the two faithful absolute-phase results differ for every orientation assignment.

## 4. Cyclic triples

For three inputs, one from each sector, a faithful result exists only as a route/provenance-labelled groupoid process. Different choices of common sector and transport route are related by explicit holonomy morphisms, not by equality.

The uncancelled Cartesian position tensor remains coherent once route morphisms are retained. Destructive ordered path readout remains downstream and chart dependent.

## 5. Quotient-level product

After quotienting each process object by uniform `C4` phase shift, transport-route differences vanish and the Cartesian tensor descends to a route-independent global process-orbit product.

This quotient can still retain position/order and source native-axis provenance. It cannot reconstruct an absolute ordered native trace/path without selecting a local phase origin.

## Verdict

`ROUTE_INDEPENDENT_CROSS_SECTOR_ABSOLUTE_PROCESS_PRODUCT = NO_GO`.

`ROUTE_LABELLED_GROUPOID_PROCESS_PRODUCT = EXACT`.

`PHASE_ORBIT_CROSS_SECTOR_PROCESS_PRODUCT = EXACT`.

`GLOBAL_ORDERED_NATIVE_PATH_MULTIPLICATION = NOT_OBTAINED`.
