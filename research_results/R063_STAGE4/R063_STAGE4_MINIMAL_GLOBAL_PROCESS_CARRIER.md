# R063 Stage 4 — Minimal Faithful Global Process Carrier

Status: `PROVED RELATIVE TO DECLARED FAITHFULNESS REQUIREMENTS`

## Requirements

A faithful finite carrier for the Stage 4 local-system survivor must simultaneously retain:

1. which of the three sector process charts owns the current local phase state;
2. all four distinct Stage 3 `C4` phase states in each sector;
3. invertible overlap transport without identifying distinct sector/phase pairs;
4. enough information to recover each local Stage 3 process fiber before any quotient.

## Lower bound

There are exactly

`3 x 4 = 12`

distinct `(sector,local_phase)` pairs.

Under the faithfulness requirements each pair must have a distinct carrier state. By injectivity/pigeonhole,

`|Carrier| >= 12`.

## Attainment

The bundle

`C3 x C4 = {(S12,x),(S23,x),(S31,x): x in C4}`

has exactly 12 states and attains the lower bound.

Fiberwise tensor is partial/local:

`(S,x) box (S,y) = (S,x+y)`.

Overlap arrows are the affine transports

`(S,x) -> (T,x+k_ST)`.

Cross-sector tensor is therefore route-indexed unless one first passes to the phase-orbit quotient.

## Important non-identifications

This 12-state object is **not** a cyclic `C12` native direction system.

It is a three-object family of four-state process fibers.

Freeze:

`12_PROCESS_STATES != 12_NATIVE_DIRECTIONS`.

No native negative axes are restored.

## Quotient boundary

A smaller global quotient exists only by losing faithfulness: quotienting uniform `C4` phase removes absolute phase and holonomy and supports a route-independent process-orbit product. That quotient cannot reconstruct the full local absolute-phase process or ordered native readout.

Thus `12` is minimal for the faithful local-system carrier, not for every possible information-losing quotient.
