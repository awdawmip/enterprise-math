# R063 Stage 4 — Local-System / Groupoid Survivor

Status: `EXACT SURVIVOR CLASSIFIED`

## No global trivialization

Because the three-edge composite has nonzero odd holonomy, local absolute phases cannot be identified globally in a path-independent way.

Thus:

`GLOBAL_PATH_INDEPENDENT_C4_TRIVIALIZATION = NO_GO`.

As an ordinary strict descent datum on a cover, the cycle cocycle condition fails.

## Affine transport groupoid

A coherent survivor exists if route provenance is retained.

Use three objects `S12,S23,S31`. Each object carries a `C4` torsor. Each oriented overlap edge carries the affine translation `tau_k`, with inverse `tau_-k`.

Composition along a route is addition of edge shifts. Closed routes act by the corresponding holonomy translation.

This is an exact finite transport groupoid / sector-indexed affine local system on the sector adjacency cycle.

The local Stage 3 tensor remains defined fiberwise. Edge transport is affine-monoidal with the constant defect recorded in the overlap classification.

## Phase-orbit quotient survivor

Let a finite process object be a position poset `P` with a phase labelling `ell:P->C4`. Quotient by the uniform action

`ell ~ ell+a` for every `a in C4`.

Write the orbit as `[P,ell]`.

The Stage 3 Cartesian tensor descends exactly:

`[P,ell] bar_box [Q,m] := [P x Q, (p,q) -> ell(p)+m(q)]`.

Indeed, replacing `ell` by `ell+a` and `m` by `m+b` shifts every product label uniformly by `a+b`, which is the same orbit.

Every affine translation `tau_k` is trivial on these orbit classes. Hence loop holonomy disappears in the quotient and `bar_box` is route-independent and associative/commutative up to the inherited finite-poset isomorphisms.

## Information retained and lost

Retained:

- finite source-position/order structure;
- relative phase differences;
- opposition relation `x-y=2 mod 4` and therefore phase-relative cancellation incidence;
- separately stored native source-axis provenance tags.

Lost:

- absolute local phase origin;
- unit/orientation gauge;
- the map from phase `0/1` back to a particular ordered native-sector basis;
- direct ordered native path/trace readout without choosing a chart/gauge.

Therefore the quotient is a genuine global **process-orbit** multiplication, but not a global native path multiplication.

## Final survivor hierarchy

`strict global algebra` -> `NO_GO`

`affine sector transport groupoid` -> `EXACT WITH HOLONOMY`

`uniform-C4 phase-orbit process` -> `EXACT ROUTE-INDEPENDENT QUOTIENT PRODUCT`
