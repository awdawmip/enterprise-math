# R063 Stage 4 — Strict Global Product No-Go

Status: `PROVED`

## Theorem

`STRICT_SINGLE_GLOBAL_STAGE3_PRODUCT = NO_GO`.

There is no single typed product on the three native positive axes whose restriction to every sector equals the frozen Stage 3 local table, for any of the eight local orientation assignments.

## Proof by shared-axis squares

In a local chart, the phase-0 axis squares to itself, while the phase-1 axis squares to the negative process state of the chart's phase-0 companion axis.

For the global square of `E2` to agree between `S12` and `S23`, `E2` must be phase `0` in both charts. This forces

`epsilon_12=1` and `epsilon_23=0`.

For the global square of `E3` to agree between `S23` and `S31`, `E3` must be phase `0` in both charts. This forces

`epsilon_23=1` and `epsilon_31=0`.

The two requirements already contradict each other at `epsilon_23`.

Therefore no orientation assignment can make all shared-axis squares chart-independent.

## Mandatory G2 witness

For cyclic orientation `(0,0,0)`:

- in `S12`, `E1` is phase `0`, so `E1 box E1 -> +E1`;
- in `S31`, `E1` is phase `1`, so `E1 box E1 -> -E3`.

The outputs have different signed native-axis tags. A single global typed product cannot equal both.

## Boundary

The contradiction is at the **absolute phase / ordered native-axis readout** level. It does not forbid:

- sector-indexed local products;
- affine phase transport with explicit route provenance;
- a phase-orbit quotient product that forgets the absolute `C4` origin.

Thus the no-go is exact and scoped, not an assertion that all globalization is impossible.
