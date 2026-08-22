# Enterprise Math Toolbox Registry

Status: `ACTIVE / CURRENT TOOL ROUTER / NOT FOUNDATION AUTHORITY`
Date: `2026-08-22`
Driver: `EM-DVR-ZX1UEJ`

## Purpose

This registry lists reusable mathematical tools that have cleared the project threshold

`NEW THEOREM != NEW TOOL`.

A registry entry must have a callable input/output interface, structural laws or certificates, an explicit failure boundary, and demonstrated reuse across more than one problem family. Exact theorem authority remains in the cited source/report or canonical definition; this file is a routing surface.

## T0 — BRC

Status: `PREEXISTING CANONICAL TOOL FAMILY`

Current BRC routing remains controlled by the exact current BRC definitions. The toolbox does not redefine BRC.

Use when the problem is naturally support/result/provenance-valued and requires composition across multiple path or branch realizations.

## T1 — Enterprise Scale Enumeration / Valuation Calculus

Status: `ACCEPTED_DERIVED_TOOL`

Core object: integer-indexed finite admissible family `S(s)` with enumerator `F(s)=|S(s)|`.

Primary operations:

- `DELTA` — finite-difference shell and degree detection;
- `GEN` — exact generating-function construction when recurrence/difference structure justifies it;
- `VAL` — finite valuation / inclusion-exclusion;
- `MOBIUS` — inversion of cumulative finite-poset data;
- `LOCAL` — semantics-preserving local decomposition.

Use for scale growth, shell counts, precision-state counts, path/shuffle counts, basin widths, BRC state counts, and other finite scale families.

Hard boundary: `NO_UNIVERSAL_NATIVE_EHRHART_POLYNOMIALITY`.

Driver review: `driver_reviews/TOOL_DISCOVERY_NATIVE_VALUATION_EHRHART_BRION_DRIVER_REVIEW_20260822.md`.

## T2 — Enterprise Block Finite-Certificate Calculus

Status: `ACCEPTED_DERIVED_TOOL`

Core mechanism:

`INDEPENDENT_BLOCK_COMPOSITION -> GLOBAL_CERTIFICATE_NUMBER <= MAX_LOCAL_CERTIFICATE_NUMBER`.

When local bounds are sharp and realized, equality follows.

Primary operations:

- factor compatibility constraints into certified independent blocks;
- compute local certificate numbers;
- extract a bounded obstruction witness;
- assemble a global success witness;
- reject application when coupling destroys block independence.

Use for local-to-global feasibility, gluing, chart consistency, support assertions, finite constraint systems, and other compatibility questions.

Hard boundary: bounded local arity, finite domain size, or path/tree interaction topology alone do not force bounded obstruction size under propagating coupling.

Existing integer-box Helly number `2` is a specialization, not a new discovery of this task.

Driver review: `driver_reviews/TOOL_DISCOVERY_ENTERPRISE_HELLY_RADON_DRIVER_REVIEW_20260822.md`.

## T3 — Typed Incidence Circuit Calculus

Status: `ACCEPTED_DERIVED_TOOL / SCOPE_NARROWED`

Input: finite component-typed incidence skeleton `Gamma=(V,E,s,t,tau)`.

Primary operations:

- `SIGN`;
- `CIRCUITS`;
- `ELIMINATE`;
- `SEPARATE`;
- `DUAL`;
- `REALIZATION_CHECK`;
- same-endpoint path-defect decomposition into circuits.

Use for path/shuffle provenance, cycle defects, recoalescence diamonds, incidence obstructions, and dual cut/cocircuit certificates without metric coordinates.

Hard boundary: the bare three positive direction types do not currently determine a signed circuit/chirotope. Carrier linear relations may not be imported as native circuit dependencies.

Driver review: `driver_reviews/TOOL_DISCOVERY_NATIVE_ORIENTED_MATROID_DRIVER_REVIEW_20260822.md`.

## T4 — Finite Fiber Capacity / Collision-Minima Calculus

Status: `ACCEPTED_TOOL_COMPOSITION / NOVELTY_DOWNGRADED`

Input: finite or locally finite state data with an already declared/derived semantic observation `pi:X->Q` and admissible finite bodies/filtration.

Primary operations:

- `nu(A)=|A|` raw capacity;
- `kappa(A)=|pi(A)|` quotient capacity;
- fiber-free/injective test;
- `delta(A)=|A|-|pi(A)|` collision defect;
- same-fiber witness extraction;
- representative packing/covering compression;
- successive collision minima `lambda_k` along a declared filtration.

Use when a problem already has meaningful quotient/fiber semantics and asks existence, compression, packing/covering, or first-collision-scale questions.

Hard boundary: the quotient/observation is an input, not something this tool may invent. Much of its quotient/collision mathematics predates this discovery; the accepted contribution is a reusable geometry-of-numbers-style composition layer.

Driver review: `driver_reviews/TOOL_DISCOVERY_NATIVE_GEOMETRY_OF_NUMBERS_DRIVER_REVIEW_20260822.md`.

## Tool-selection rule

Prefer the narrowest tool matching the actual information structure:

- scale family / shell growth -> `T1`;
- finite local-to-global compatibility -> `T2`;
- incidence cycles / path differences / cuts -> `T3`;
- declared quotient fibers / capacity / first collision -> `T4`;
- support/provenance algebra already modeled by BRC -> `T0`.

Tools may compose, but composition must preserve semantic typing. A result obtained only after inventing a target observation, metric, orientation, convexity, or carrier relation is conditional on that extra datum.

## Promotion rule

Tool acceptance is not Foundation canonicalization. This registry does not create native primitives. A tool may be used by later research immediately at its accepted derived semantic scope; any attempt to promote one of its assumptions or readouts into Foundation follows the separate Foundation route.
