# X6 triadic INNER C12: relation-phase clock above one repeated action Cell

Status: `FREE_RESEARCH / EXACT DERIVATION / NOT_FOUNDATION`
Date: `2026-09-06`
Tasks: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, `RS-X6-NATIVE-TIME-DYNAMICS`
Depends on:
- `X6_TRIADIC_ATOMIC_SCATTER_AND_BRC_CORRELATION_V1_20260906.md`;
- `X6_TRIADIC_ROTATION_GENERATORS_V1_20260906.md`;
- existing Viète OUTER C12 / phase-vs-precision results.

## 1. Two different C12 lifts of one signed C6 frame

Fix a pivot Cell `c`, an oriented selected triad `S`, and the signed-C6 generator `Q=Q_S`.

Let an ordered equal-unit triad phase be

`Theta_r = Q^r Theta_0`, `r in C6`.

V1 gives two shortest microrealizations for each individual shell transition. Two typed C12 constructions now separate.

### OUTER spatial C12

For a single shell Cell trajectory, use the nonzero OUTER midpoint. This produces the already-derived 12-Cell spatial microcycle. On FCC STAR slices it carries the existing Viète gate/bisector interpretation.

### INNER interaction C12

For a triadic atomic event, V1 forces all three force occurrences through the common pivot `c`. Define the closure-event state

`Kappa_r := (c; Theta_r => Theta_{r+1}; token_matching)`.

The six `Kappa_r` share the same spatial Cell `c` but differ as relation/provenance states because their incoming/outgoing port matching differs.

Define a one-step successor on decorated states by

`F(Theta_r)=Kappa_r`,

`F(Kappa_r)=Theta_{r+1}`.

Then

`F^12=1`,

and the twelve decorated states

`Theta_0,Kappa_0,Theta_1,Kappa_1,...,Theta_5,Kappa_5`

are distinct when token/port correspondence is retained.

Thus the same signed-C6 macro frame has two different typed C12 lifts:

- OUTER: spatial-Cell refinement;
- INNER: atomic-interaction relation refinement.

They must not be identified.

## 2. Spatial state does not determine interaction phase

All six closure-event states `Kappa_r` project to the same native spatial Cell `c`.

Therefore the spatial projection

`pi_space(Kappa_r)=c`

has a six-element fiber on this cycle.

A future operation that asks which incoming port is matched to which outgoing port distinguishes the six states. Hence no quotient retaining only the pivot Cell is operation-safe for the triadic dynamics.

This gives an exact local theorem:

`SPATIAL_CELL_STATE != TRIADIC_INTERACTION_TIME_PHASE`.

Time/order information is genuinely relational state over the Cell, not another spatial coordinate.

## 3. Event-clock hierarchy

For a repeated deterministic triadic scatter trajectory, let `n in N_0` count the elementary relation update steps

`shell -> closure-event -> next shell`.

The finite phase readout is

`phase_12(n)=[n]_12`.

At even `n=2r`, the state is `Theta_r`; at odd `n=2r+1`, it is `Kappa_r`.

Two coarser readouts are:

- shell/closure parity: `[n]_2`;
- macro signed-C6 phase on shell instants: `[r]_6`.

If a reversible bi-infinite extension of the repeated process is later admitted, the event counter extends from `N_0` to `Z`; the present theorem does not assume such a global time reversal.

## 4. C3 matching repair inside the clock

For sign-coherent triads, forgetting token correspondence collapses the six shell phases to the two sign sheets. The exact repair fiber is `C3` as proved in V1.

At the closure Cell the loss is even more severe: forgetting the relation decoration collapses all six `Kappa_r` to one spatial state.

Therefore the minimal typed clock depends on the future observer:

- spatial pivot only: no phase retained;
- static sign sheet: `C2`;
- labeled shell triad: `C6`;
- full shell/closure decorated successor cycle: `C12`.

There is no observer-independent justification for replacing all of these by one scalar phase without a future-operation certificate.

## 5. Separation from precision/root refinement

The previously proved Viète precision pro-state records a compatible root lineage; for a fixed oriented half-turn chirality it is static under physical trajectory advancement.

The present `phase_12(n)` advances at every actual relation update.

Thus on this native triadic process:

`PHYSICAL_EVENT_PHASE != PRECISION_ROOT_LINEAGE`.

This supplies a second, independent native witness for the existing clock-separation result.

## 6. Consequence for the time task

A viable native time state cannot be reconstructed from spatial Cell coordinates alone, because six distinct ordered interaction events occur at the same pivot Cell in one period.

The smallest current positive model is therefore not a seventh spatial coordinate. It is an ordered event-history/index layer over decorated Cell relations, with finite phase quotients such as `C12` available only for periodic subsystems.

This does not yet define the global Enterprise time line. It gives a mandatory local contract any global time construction must satisfy.
