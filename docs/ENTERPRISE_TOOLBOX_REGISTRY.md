# Enterprise Math Toolbox Registry

Status: `ACTIVE / CURRENT TOOL ROUTER / NOT FOUNDATION AUTHORITY / V2`
Date: `2026-08-22`
Driver: `EM-DVR-ZX1UEJ`
Invocation protocol: `docs/ENTERPRISE_TOOL_INVOCATION_PROTOCOL.md`
Machine registry: `enterprise_toolbox_registry.json`
Method inventory: `research_method_inventory.json`
Executable router: `tools/enterprise_toolbox.py`

## Purpose

This registry routes reusable mathematical mechanisms across Enterprise Math.

A tool family is admitted only when it has a reusable input/output interface, structural law/certificate, explicit failure boundary and meaningful reuse. Exact theorem authority stays with the cited owner.

The central anti-duplication rule is:

`UNDERSTAND TASK -> LOOK UP EXISTING TOOL -> REUSE / COMPOSE / EXTEND -> NEW FAMILY ONLY AFTER GAP CONFIRMED`.

FREE Phase A is deliberately excluded from pre-freeze catalog lookup; Phase B uses this registry after candidate freeze for deduplication.

## T0 — BRC

Status: `PREEXISTING CANONICAL TOOL FAMILY`.

Use for support/result/provenance-valued composition, branching, multipath and recoalescence semantics. Current exact BRC definitions remain authoritative.

Hard boundary: Boolean support does not reconstruct provenance already erased.

## T1 — Enterprise Scale Enumeration / Valuation Calculus

Status: `ACCEPTED DERIVED TOOL`.

Use for integer-indexed finite scale families, shells, counts, finite differences, generating functions, valuations, inclusion-exclusion and local-to-global count decompositions.

Primary interface:

`DELTA / GEN / VAL / MOBIUS / LOCAL`.

Known recent specialization: mixed finite-difference separability from FQ008.

Hard boundary:

`NO_UNIVERSAL_NATIVE_EHRHART_POLYNOMIALITY`.

Growth degree is not automatically native geometric dimension.

## T2 — Enterprise Block Finite-Certificate Calculus

Status: `ACCEPTED DERIVED TOOL`.

Core law:

`INDEPENDENT BLOCKS -> GLOBAL CERTIFICATE NUMBER <= MAX LOCAL CERTIFICATE NUMBER`.

Use for local-to-global compatibility, finite gluing/constraint feasibility and bounded obstruction extraction.

Existing specialization:

`src/enterprise_math/box_collapse.py` already gives integer-box Helly number `2`, compact extremal facet witnesses and deletion-safe certificates.

Hard boundary: bounded local arity/domain or path/tree interaction topology does not guarantee bounded global obstruction size when relations propagate through arbitrarily long coupled chains.

## T3 — Typed Incidence Circuit Calculus

Status: `ACCEPTED DERIVED TOOL / SCOPE NARROWED`.

Use for finite typed incidence skeletons, path differences, cycles, provenance defects, rerouting and cut/separator certificates.

Interface:

`SIGN / CIRCUITS / ELIMINATE / SEPARATE / DUAL / REALIZATION_CHECK`.

Hard boundary:

`BARE THREE POSITIVE DIRECTIONS != NATIVE SIGNED CIRCUIT`.

Carrier linear relations may not be imported to manufacture native dependencies.

## T4 — Finite Fiber Capacity / Collision-Minima Calculus

Status: `ACCEPTED TOOL COMPOSITION / NOVELTY DOWNGRADED`.

Use after an observation/fiber map is already semantically justified. Provides raw capacity, occupied quotient capacity, collision defect/witnesses, representative packing/covering and successive collision minima.

Typical composition:

`T6/T8 constructs or certifies observation -> T4 counts/compresses its fibers`.

Hard boundary: T4 cannot invent `pi` simply to force a capacity theorem.

## T5 — Integer Precision / Refinement Calculus

Status: `HARVESTED PREEXISTING DERIVED TOOL FAMILY`.

This family consolidates mature older modules that had been scattered across P018/precision routes.

Main owners:

- `src/enterprise_math/precision.py`;
- `src/enterprise_math/graded_precision.py`;
- related precision-system/proof modules.

Use for:

- coarse/fine integer projections;
- exact bounded fiber details and recomposition;
- nested refinement identities;
- carry/borrow;
- mixed-radix precision chains;
- degree-aware transport;
- nonlinear homogeneous projection defects.

Hard boundary: finite integer precision semantics do not create a continuum or a limit theory.

## T6 — Operation-Safe Quotient / Predictive Refinement Calculus

Status: `HARVESTED PREEXISTING DERIVED TOOL FAMILY`.

This is one of the most important anti-duplication consolidations.

Existing modules:

- `predictive_quotient.py`;
- `composition_safe_collapse.py`;
- `operation_quotient.py`;
- `partial_operation_quotient.py`;
- `safe_operation_algebra.py`.

Shared mother operation:

> Given declared observations/operations, find the coarsest quotient/refinement on which the required behavior descends, or produce a witness that it does not.

Use for predictive state, future-equivalence, operation congruence, quotient-safe collapse and minimal repair.

Hard boundary: the observation/operation language is input. T6 does not decide what information should be forgotten.

## T7 — Finite Symmetry / Orbit / Equivariance Calculus

Status: `HARVESTED AND TOOLIZED`.

Shared executable owner:

`src/enterprise_math/finite_symmetry.py`.

Harvested from the common method behind R064, FQ009 and the resolution-glue symmetry obstruction.

Interface:

- finite group-action validation;
- `orbit` / `orbit_partition`;
- `stabilizer`;
- global fixed points;
- canonical-choice obstruction;
- exact equivariant-map count/enumeration.

Use for relabeling/automorphism audits, orbit reduction, equivariant law classification, torsor/stabilizer calculations and canonical-choice impossibility.

Hard boundary: if the declared symmetry has no invariant datum, the tool diagnoses missing symmetry breaking; it does not invent one from carrier presentation.

## T8 — Relation Observable / Spectrum Calculus

Status: `HARVESTED PREEXISTING DERIVED TOOL FAMILY`.

Existing modules include:

- `relation_observable_signature.py`;
- `relational_spectrum.py`;
- `relation_observable_composition.py`;
- `relation_future_powerset.py`;
- `weighted_relation_field.py`;
- `relation_lattice.py`.

Use for multivalued relations/correspondences, powerset-valued future observations, common-target collision spectra, relation-safe quotients and capacity-weighted relation invariants.

Critical distinction:

`RAW RELATION BRANCHING != OBSERVABLE NONDETERMINISM != QUOTIENT SAFETY`.

## T9 — Holonomy / Cocycle / Gluing-Obstruction Calculus

Status: `HARVESTED PREEXISTING + RECENT DERIVED TOOL FAMILY`.

Existing/recent owners:

- `precision_holonomy.py`;
- `precision_signed_holonomy.py`;
- `p023_borrow_cocycle.py`;
- `material_loop_identity.py`;
- R063 Stage-4 C4 globalization result.

Use for local transports, chart/process gluing, staged-vs-direct transport, loop defects, cocycles, route dependence, torsors and strict-globalization obstructions.

Core pattern:

`LOCAL TRANSPORT -> LOOP COMPOSITION -> HOLONOMY/DEFECT -> STRICT GLUING VERDICT`.

Hard boundary: nonzero holonomy proves failure of strict trivialization but does not select a unique repaired global object.

## Domain facade D1 — Prime Toolkit

Status: `PREEXISTING DOMAIN TOOL LIBRARY`.

Sources:

- `src/enterprise_math/prime_toolkit.py`;
- `src/enterprise_math/prime_method_inventory.json`.

Prime Toolkit already preserves mathematical/toolization/provenance status next to returned values. Keep using it for prime-specific dispatch, but route generic mechanisms such as precision or quotient refinement through T5/T6 rather than duplicating them in prime-only code.

## Tool-family and method layers

The family registry answers:

> Which mathematical mechanism owns this problem shape?

`research_method_inventory.json` answers:

> Which exact callable method, recent result interface, specialization or domain operator already exists?

The executable router searches both and then scans all current Python source by AST/docstring/public API.

Therefore a method does not need to be manually remembered to be discoverable.

## Current selection guide

- support/result/provenance algebra -> T0;
- scale/shell/count/growth -> T1;
- local-to-global compatibility/certificates -> T2;
- incidence cycles/path differences/cuts -> T3;
- declared fibers/capacity/compression -> T4;
- coarse/fine precision/carry/detail -> T5;
- future-preserving quotient/descent -> T6;
- symmetry/orbits/equivariance/canonical choice -> T7;
- relation-valued observations/collision spectra -> T8;
- loop transport/cocycle/holonomy/gluing obstruction -> T9.

Tools may compose, but semantic input contracts remain binding.

## Recent-route harvest

Priority research from 20–22 August 2026 is indexed in:

`docs/RESEARCH_METHOD_HARVEST_20260820_20260822.md`.

Key decisions:

- R061 line/gauge/segment results are domain operators, not new generic families;
- R062 multipath bridge is a T0 subtool;
- R063 path-root is a domain operator while Stage-4 holonomy is T9;
- R064 orbit/equivariant-map method is T7;
- FQ008 mixed differences route to T1;
- FQ009 torsor/stabilizer route to T7;
- LSR-N2 remains a candidate, not a tool family; generic fiber/kernel machinery already belongs to T4/T6.

## Invocation and promotion rule

For TASK/Driver/Steward work:

`UNDERSTAND TASK -> TOOL COVERAGE LOOKUP -> REUSE/COMPOSE/EXTEND/GAP`.

For FREE Phase A the catalog remains hidden until candidate freeze; Phase B then performs the same dedup lookup.

Tool acceptance never promotes a Foundation premise. The exact owner/source controls theorem status.
