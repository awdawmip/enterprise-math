# Enterprise Math Toolbox Registry

Status: `ACTIVE / CURRENT TOOL ROUTER / NOT FOUNDATION AUTHORITY / V4`
Date: `2026-08-23`
Driver: `EM-DVR-ZX1UEJ`
Invocation protocol: `docs/ENTERPRISE_TOOL_INVOCATION_PROTOCOL.md`
Machine registry: `enterprise_toolbox_registry.json`
Base method inventory: `research_method_inventory.json`
Method addenda: `research_method_inventory_addenda/*.json`
Executable router: `tools/enterprise_toolbox.py`
Logic-closure checker: `tools/check_toolbox_logic_closure.py`

## Purpose

This registry routes reusable mathematical mechanisms across Enterprise Math.

A tool family is admitted only when it has a reusable input/output contract,
structural law or certificate, explicit failure boundary and meaningful reuse.
Exact theorem authority remains with the cited owner.

Central rule:

`UNDERSTAND TASK -> LOOK UP EXISTING TOOL -> REUSE / COMPOSE / EXTEND -> NEW FAMILY ONLY AFTER GAP CONFIRMED`.

FREE Phase A is excluded from pre-freeze catalog lookup; Phase B performs
deduplication after candidate freeze.

## Repository-tool ownership

`research_common_surface.json` remains the owner of universal
theorem/formal/operational infrastructure. Toolbox is a separate mathematical
routing surface.

Toolbox-owned repository tools are:

- `tools/enterprise_toolbox.py`;
- `tools/check_toolbox_logic_closure.py`;
- `tools/tool_discovery_native_valuation_ehrhart_brion_calculus_check.py`.

`tools/check_research_common_surface.py` enforces disjoint ownership of
`tools/*.py`. `tools/check_toolbox_logic_closure.py` separately enforces the
end-to-end tool loop: registry, inventories/addenda, executable source, role
timing, taskbook inheritance, router discoverability and regression.

## T0 — BRC

Use for support/result/provenance-valued composition, branching, multipath and
recoalescence.

Hard boundary: Boolean support cannot reconstruct erased provenance.

## T1 — Scale Enumeration / Valuation

Use for integer-indexed scales, shells, counts, finite differences, generating
functions, valuations, inclusion-exclusion and local-to-global counting.

Interface:

`DELTA / GEN / VAL / MOBIUS / LOCAL`.

Hard boundary:

`NO_UNIVERSAL_NATIVE_EHRHART_POLYNOMIALITY`.

## T2 — Block Finite-Certificate

Use for supported local-to-global compatibility, finite constraint feasibility
and bounded obstruction extraction.

Core law:

`INDEPENDENT BLOCKS -> GLOBAL CERTIFICATE NUMBER <= MAX LOCAL CERTIFICATE NUMBER`.

Hard boundary: propagating coupling can force unbounded minimal obstruction
size.

## T3 — Typed Incidence Circuit

Use for typed incidence skeletons, cycles/cocircuits, cuts, path differences,
provenance defects and rerouting certificates.

Interface:

`SIGN / CIRCUITS / ELIMINATE / SEPARATE / DUAL / REALIZATION_CHECK`.

Hard boundary:

`BARE THREE POSITIVE DIRECTIONS != NATIVE SIGNED CIRCUIT`.

## T4 — Finite Fiber Capacity / Collision-Minima

Use only after an observation/fiber map is semantically justified. Provides
capacity, collision witnesses, representative compression and collision minima.

Typical composition:

`T6/T8 constructs observation -> T4 counts/compresses fibers`.

Hard boundary: T4 cannot invent the observation map.

## T5 — Integer Precision / Refinement

Use for exact coarse/fine projection, detail/recomposition, carry/borrow,
mixed-radix chains and graded transport.

Primary sources include:

- `src/enterprise_math/precision.py`;
- `src/enterprise_math/graded_precision.py`.

Hard boundary: finite precision does not create continuum or limit semantics.

## T6 — Operation-Safe Quotient / Predictive Refinement

Use for coarsest partitions/quotients on which declared future observations or
operations descend, or an exact obstruction.

Primary sources include:

- `src/enterprise_math/predictive_quotient.py`;
- `src/enterprise_math/composition_safe_collapse.py`;
- `src/enterprise_math/operation_quotient.py`;
- `src/enterprise_math/partial_operation_quotient.py`;
- `src/enterprise_math/safe_operation_algebra.py`.

Hard boundary: the observation/operation language is input.

## T7 — Finite Symmetry / Orbit / Equivariance

Use for orbit/stabilizer computation, relabeling audits, equivariant-map
classification, torsors and canonical-choice obstruction.

Executable owner:

`src/enterprise_math/finite_symmetry.py`.

Hard boundary: the tool diagnoses missing symmetry breaking; it does not invent
one.

## T8 — Relation Observable / Spectrum

Use for multivalued relations, powerset-valued future signatures, relation
collision spectra, relation-safe quotients and capacity-weighted relation
invariants.

Freeze:

`RAW RELATION BRANCHING != OBSERVABLE NONDETERMINISM != QUOTIENT SAFETY`.

## T9 — Holonomy / Cocycle / Gluing-Obstruction

Use for local transports, loop defects, route dependence, cocycles, torsors and
strict-globalization obstruction.

Core pattern:

`LOCAL TRANSPORT -> LOOP COMPOSITION -> HOLONOMY/DEFECT -> STRICT GLUING VERDICT`.

Hard boundary: nonzero holonomy does not select a unique repair.

## T10 — Local Redistribution / Toppling / Potential

Status: `DRIVER ACCEPTED / PRODUCTION CALLABLE`.

Executable owner:

`src/enterprise_math/discrete_laplacian_chip_firing.py`.

Use for:

- legal finite integer local redistribution;
- strict termination witnesses;
- order-independent stabilization in the proved regime;
- odometers;
- least-action certificates;
- conservation/sink dissipation;
- reduced-Laplacian/cokernel invariants.

The graph Laplacian is one constructor, not the whole family. Mixed-radix carry
is another demonstrated specialization.

Hard boundaries:

- `L=D-A` alone is not T10;
- sinkless/inaccessible systems may not terminate;
- semantic edge reversal is not orientation gauge;
- stabilization is not a canonical representative of each cokernel class;
- potential is not automatically geometry or energy.

### T10 weighted variational subtool

Positive weighted Dirichlet/flow energy, Thomson/Dirichlet minimization,
gradient/circulation orthogonality, effective resistance and Kron reduction are
retained as a T10 specialization, optionally composed with T3.

Permanent freeze:

`BARE_INCIDENCE != ENERGY`.

## T11 — Discrete Morse / Acyclic-Matching Chain Reduction

Status: `DRIVER ACCEPTED / PRODUCTION CALLABLE`.

Executable owner:

`src/enterprise_math/discrete_morse_collapse.py`.

Use only for explicit finite free chain complexes. Capabilities include:

- exact `d^2=0` validation;
- adjacent-grade matching legality;
- closed-gradient-path obstruction;
- coefficient-aware cancellation;
- critical generators and reduced boundary;
- projection/lift/homotopy maps;
- replayable strong-deformation-retract certificate.

Hard boundaries:

- graph node deletion is not Discrete Morse;
- over `Z`, only unit pivots `+1/-1` cancel in this interface;
- field-only reduction is not an integral result;
- homology equivalence is not T6 operation safety;
- greedy matching is not canonical or optimal by default.

## T12 — Idempotent Path Closure / Bellman Fixed-Point

Status: `DRIVER ACCEPTED / PRODUCTION CALLABLE`.

Executable owner:

`src/enterprise_math/idempotent_path_closure.py`.

Use only when the caller explicitly supplies weighted transition semantics and
an idempotent semiring/order contract.

Capabilities:

- min-plus/max-plus matrix composition;
- fixed-length path envelopes;
- finite Kleene closure after exact improving-cycle checks;
- exact path witnesses;
- finite semiring validation;
- left/right matrix residuals when a greatest residual exists;
- Bellman least/greatest fixed points on finite complete carriers;
- explicit improving-cycle and non-residuation obstructions.

Critical ownership boundary:

`RESIDUATION / GALOIS ADJUNCTION ALONE REMAINS P008-OWNED`.

Hard boundaries:

- weights are explicit input;
- improving cycles or incomplete carriers may obstruct finite closure;
- unweighted quotient safety does not imply weights descend;
- a path envelope is not automatically a native metric.

Frozen discovery checker:

`scripts/tool_discovery_tropical_residuation_idempotent_closure_check.py`.

## Non-promoted 23 August discoveries

### Weighted incidence energy

Classification: `DOMAIN_SPECIALIZATION_ONLY`.

Route to the T10 weighted variational layer. No separate energy family.

### Carrier Voronoi / Delaunay

Classification: `CURRENT_CENTER_CARRIER_SPECIALIZATION_ONLY`.

It remains discoverable as a domain operator with exact ties, dual adjacency,
empty-ball certificates and degeneracy handling.

Freeze:

`CARRIER_NEAREST_SITE_TOOL != NATIVE_ENTERPRISE_METRIC`.

### Discrete conformal / circle pattern

Classification: `CURRENT_FOUNDATION_EXTRA_STRUCTURE_REQUIRED`.

Freeze:

`CURRENT_ENTERPRISE_CIRCLE_CELLS != CIRCLE_PACKING`.

`CARRIER_EUCLIDEAN_CONFORMAL_DATA != NATIVE_ENTERPRISE_CONFORMAL_DATA`.

Weighted/cotangent derivative layers route to T10; no global conformal family
was accepted.

## Domain facade D1 — Prime Toolkit

Sources:

- `src/enterprise_math/prime_toolkit.py`;
- `src/enterprise_math/prime_method_inventory.json`.

Use it for prime-specific dispatch, while routing generic precision/quotient/
certificate mechanisms to T0–T12.

## Method inventory architecture

`research_method_inventory.json` is the backward-compatible base.

New harvests use:

`research_method_inventory_addenda/*.json`.

The router loads both, rejects duplicate `method_id` values, then scans all
current source modules without importing them.

Current six-return shard:

`research_method_inventory_addenda/20260823_tool_discovery_six_return.json`.

## Current selection guide

- support/result/provenance -> T0;
- scale/shell/count -> T1;
- compatibility/certificate -> T2;
- cycles/cuts/path differences -> T3;
- declared fibers/collision compression -> T4;
- precision/carry/refinement -> T5;
- future/operation-safe quotient -> T6;
- symmetry/orbits/canonical choice -> T7;
- multivalued relation/spectrum -> T8;
- loop transport/holonomy/gluing -> T9;
- local redistribution/stabilization/odometer -> T10;
- graded chain-complex cancellation -> T11;
- weighted idempotent path closure/Bellman -> T12.

Tool acceptance changes routing, not theorem ownership or Foundation ontology.
