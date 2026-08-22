# R063 Stage 4 — Cyclic Relabeling Equivariance

Status: `CLASSIFIED`

Let

`rho:E1->E2->E3->E1`

and simultaneously

`S12->S23->S31->S12`.

The action is defined discretely from the atlas; no classical carrier rotation is used.

## Action on data

Under one application of `rho`:

- sector tags cycle;
- native axis tags cycle;
- source-position posets are relabelled but not reordered;
- local phase labels are transported by the corresponding overlap affine map;
- tensor positions are carried functorially;
- cancellation incidence based on phase opposition is preserved because uniform translations preserve phase differences.

## Threefold action

After `rho^3`:

- sector tag returns exactly;
- native axis tag returns exactly;
- source-position poset and path order return exactly;
- absolute `C4` phase is translated by the loop holonomy `H`.

Since `H` is `1` or `3`,

`rho^3 != identity`

on the faithful absolute-phase process local system.

After quotienting by uniform global `C4` phase shift,

`rho^3 = identity`

on process-orbit classes.

## Mandatory G5 witness

For the Stage 3 witness `iij x iji`, the nine interaction positions and their native/source provenance return after `rho^3`, while every process label is shifted uniformly by `H`. The checker verifies strict inequality before quotient and exact orbit equality after quotient for all eight orientation assignments.

## Boundary

Cyclic relabeling covariance therefore survives globally only as:

- a groupoid action with holonomy on the faithful process; or
- a strict action on the phase-orbit quotient.

It is not a proof of a global N0 multiplication.
