# Heartbeat World: six native Enterprise spatial axes and one time dimension

Status: `ACTIVE / DIRECT_USER_NAMING_AND_COORDINATE_CONSTRAINT`
Effective: `2026-09-19`
Position updated: `2026-09-23`
Authority: Direct user naming on 2026-09-19 and residual-fidelity position update on 2026-09-23; existing P000 and native X6 foundations are retained, not replaced by experimental results.
Machine contract: `HEARTBEAT_WORLD_NATIVE_X6_TIME.json`
Chinese counterpart: [HEARTBEAT_WORLD_NATIVE_X6_TIME.md](HEARTBEAT_WORLD_NATIVE_X6_TIME.md)

## Formal definition

**Heartbeat World is the seven-dimensional world consisting of the six-dimensional discrete Cell space described by the six native Enterprise spatial coordinates, together with one time dimension.**

The stable machine identifier is `HEARTBEAT_WORLD`; the English name is `Heartbeat World`. The canonical Chinese name is recorded in the machine contract and Chinese counterpart.

The complete world is `6D_ENTERPRISE_NATIVE_SPACE + 1D_TIME`, not the six signed directions of ordinary three-dimensional space and not seven spatial axes. Two-dimensional diagrams, three-dimensional views, FCC carriers and three-axis sections serve only as sections or observations, not as the complete native world.

## Native spatial coordinates

The six spatial axes are `E_1,...,E_6`; native dimension counts axes. Each has a positive and negative primitive step direction, giving twelve signed primitive directions but six spatial dimensions. The axes are pairwise Enterprise-orthogonal under `PERP_E`, with native right angle `120 degrees`. This does not demand six Euclidean vectors in three-dimensional space with pairwise 120-degree angles.

Retain `X6 = AFFINE_TORSOR(Z^6)`. Once an actual Cell is chosen as reference, raw relative displacements have six signed integer components `z=(z_1,...,z_6)`. There is no distinguished global ontic origin. Primitive adjacency is `z -> z +/- e_i`. A multi-axis displacement is a composite path, not a new primitive direction.

The raw component-length readout is `L_E(z)^2=sum(z_i^2)`; the minimum primitive-step count is `sum(abs(z_i))`. These are different quantities. Common depth is part of a composite six-axis displacement, not a seventh spatial axis; removing it requires a suitable observer/future-operation preservation proof.

Signed raw coordinates are internal displacement charts, not final public Cell addresses. The final address remains six nonnegative integer fields under `coordinate_address_contract.json` and a registered lossless codec. This definition does not invent a general final-address codec for arbitrary full X6.

## Time and heartbeat

An event is written `(z,t)` or `(z_1,...,z_6;t)`, keeping space and time separately typed. Time records and orders changes in spatial, covering, rotation, scale and other relations. Spatial return need not be temporal return; repeating a heartbeat phase need not repeat the complete event.

Time organizes heartbeat evolution through scaling, rotation and interaction, but is not defined as one scale value. A periodic phase may be derived from time; whether it can replace complete time depends on the observation objective. Discrete `t in N_0` is a clock representation in current computational experiments, not a measured physical time law established by naming alone.

Six-step doubling, twelve-step round trips, radix 2 and particular step speeds are replaceable research programs, not conditions defining Heartbeat World. The finite S6 rotation skeleton is not the complete native rotation theory. Time metrics, complete spacetime transformations and actual memory benefits remain research questions.

## Residual-faithful discrete relational position

Heartbeat World adopts a **finite-resolution, residual-faithful discrete relational system**. The relevant complete state retains branches, joint relations, internal fields, loop records and provenance that affect the declared future operations and observations. Neither a spatial endpoint nor the current source distribution automatically determines these distinctions; a single scalar remainder need not represent them.

Exact removal requires preservation of observations under the allowed future compositions. Approximate removal requires a declared scope and propagated error bound. Genuine merging, proved zero residuals and minimally sufficient compression remain admissible; residuals need not be nonzero everywhere, and all history need not be retained forever. Cancellation must match complete joint states and algebraic types; nonnegative mass is not a signed amplitude.

Treat structural residuals, approximation errors, implementation/derivation errors and unclassified differences separately. A residual is not automatically energy, temperature, force or an extra spatial dimension. A discrete basis neither automatically discretizes its amplitudes nor supplies an infinitely precise real ontology. Study residual generation, evolution, repair, stability and resource cost rather than requiring universal elimination.

Detailed machine rules: [RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json](RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json). Project position: `PROJECT_DEFINITION.md` and its Chinese counterpart. This update changes neither the heartbeat-instant definition, candidate evidence status, existing task records nor review status.

## State and algebraic boundaries

The seven event coordinates are not a complete field state. Residues, weights, path provenance, resource budgets, heartbeat programs and observer contexts may be additional state over an event; they add no spatial dimensions. Do not hide all residues inside one global time value or interpret a fractional readout as dividing the native Cell.

Displacement addition within one scale and reference, number-ring multiplication induced by a particular heartbeat program, and serial composition of time-labelled operations are different types of operation. An algebraic instance such as `lambda^6=2`, a branch-elimination rule or a finite experiment is not automatically a world axiom.

New research and code should use the formal name and cite this contract. Historical records retain their original text and provenance rather than being bulk rewritten. External science is reported faithfully within its own models; project definitions are not presented as external scientific consensus.
