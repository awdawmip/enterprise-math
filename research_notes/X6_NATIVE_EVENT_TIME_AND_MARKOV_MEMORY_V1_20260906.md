# X6 native event time: ordered relation updates, phase quotients, and Markov-memory lower bounds

Status: `FREE_RESEARCH / EXACT RESTRICTED DERIVATION + NO-GO / NOT_FOUNDATION`
Date: `2026-09-06`
Task: `RS-X6-NATIVE-TIME-DYNAMICS`
Consumes:
- P000 `TIME_ROLE = TRACE_AND_ORDER_OF_RELATIONAL_CHANGE`;
- `X6_TRIADIC_INNER_C12_RELATION_CLOCK_V2_20260906.md`;
- `X6_ROTATION_PATH_GROUPOID_V2_20260906.md`;
- current Viète phase/refinement clock-separation theorems.

## 1. Minimal time base for an ordered trajectory

For one forward native process, let

`T_ev = N_0`

index successive **relation-update layers**. A time-indexed native trajectory is a sequence

`S_0 -> S_1 -> S_2 -> ...`

of typed decorated states over X6.

`T_ev` is not a seventh spatial coordinate. It orders change events. If a particular process is later proved reversible in both temporal directions, its event index may extend to `Z`; this note does not assume a global time-reversal axiom.

The decorated state may contain spatial Cell data, rotation frame, force/closure relation, internal/channel state and the amount of BRC/path provenance required by the declared future-operation horizon.

## 2. Event-layer count is not summed spatial path count

In the atomic triadic scatter from V1, one shell-to-closure update contains three simultaneous primitive force-port transitions into the common action Cell. The closure-to-shell update contains three simultaneous outgoing transitions.

Therefore one triadic macrostep has:

- `2` ordered relation-update layers;
- `6` primitive force transition occurrences in total.

So even in this smallest exact native example,

`RELATION_EVENT_TICK != SUMMED_PRIMITIVE_PATH_TRANSITION_COUNT`.

Path count remains a valid event count on each path/branch, but it is not automatically physical elapsed time when several transitions belong to one atomic relation update.

## 3. Periodic phase is a quotient of event order, not full time

For the deterministic INNER triadic C12 subsystem, define the physical phase observer

`phi_12(n)=[n]_12`.

This is a periodic quotient of the unbounded event index. It forgets how many complete periods have elapsed.

The shell/closure parity is the homomorphic quotient

`phi_2(n)=[n]_2`.

The signed-C6 shell phase is naturally observed only on even event times:

`psi_6(2r)=[r]_6`.

It satisfies the two-step semiconjugacy

`psi_6(n+2)=psi_6(n)+1`

on the shell subtrajectory. Treating one C12 microstep as one C6 macrostep would therefore be a clock-typing error.

## 4. Spatial-only Markov no-go

The six decorated closure states

`Kappa_0,...,Kappa_5`

all have the same spatial projection: the pivot Cell `c`.

But their deterministic successors are the six distinct labeled shell states

`Theta_1,...,Theta_0`.

Suppose a deterministic Markov update were defined on spatial Cell state alone. At the input `c` it would need to choose one unique next state, contradicting the six distinct correct successors.

Therefore

`SPATIAL_X6_CELL_ALONE_IS_NOT_A_MARKOV_STATE_FOR_TRIADIC_ROTATION`.

Any exact deterministic repair that preserves the next labeled shell relation must distinguish all six members of the pivot fiber. Hence its relation-memory cardinality at `c` is at least `6`.

A `C6` closure-phase label is sufficient at the pivot; the full alternating decorated cycle can be represented by a 12-state phase token `C12` when that periodic subsystem is the declared observer horizon.

## 5. Observer-dependent minimality

There is no single smallest memory independent of future operations.

Examples on the same process:

- observer asks only shell/closure parity -> `C2` is sufficient;
- observer asks static sign sheet -> `C2` on shell states is sufficient;
- observer asks labeled triad matching -> exact repair needs the `C3` matching coordinate above the sign sheet;
- observer asks deterministic full C12 successor -> 12 decorated phase states are sufficient;
- observer asks full Path-formal history -> no finite phase quotient is sufficient.

Thus `MINIMAL_TIME_STATE` is always scope-typed to the declared future-operation language.

## 6. No finite globally provenance-complete Markov memory

Let `L_i` be the two-step spatial loop at a Cell

`x -> x+e_i -> x`.

For every `k>=0`, the history `L_i^k` has the same spatial endpoint and identity frame but exact path length `2k` and distinct Path-formal word/provenance.

If the future-operation language includes exact path length, exact loop count or exact Path-formal history, any finite memory quotient must identify two different powers `L_i^k` and `L_i^m` by the pigeonhole principle. A future exact-history query then separates them.

Therefore no finite-state Markov summary can be globally operation-safe for unrestricted Path-formal/BRC provenance.

This does not prevent finite Markov states for restricted law/observer horizons such as the deterministic triadic C12 subsystem.

## 7. Precision/root lineage is not event time

In the existing Viète half-turn root bundle, fixed sweep chirality selects a precision/root lineage that remains unchanged as the physical trajectory start advances.

By contrast the event index `n` and `phi_12(n)` advance under actual relation updates.

Hence

`PRECISION_ROOT_LINEAGE != PHYSICAL_EVENT_CLOCK`.

The natural typed picture is a base/fiber separation:

- base: ordered physical relation events / trajectory phase;
- fiber/parameter: compatible precision or root lineage when such a structure is present.

A synchronous identification requires a separate theorem and is already known to fail in the current Viète setting.

## 8. Reusable state contract

The smallest currently safe general template is

`STATE_t = (SPATIAL_t, RELATION_t, FRAME_t, MEMORY_t; PRECISION_PARAMETER)`.

`TIME` is the order on updates of this decorated state, not one component of `SPATIAL_t`.

`MEMORY_t` may be finite for a restricted deterministic law or unbounded when full path provenance is in scope.

The precision parameter is separately typed and does not advance merely because `t` advances.

## 9. Current frontier

Closed in this stage:

- exact event-order base for one-sided native trajectories;
- explicit divergence between relation-update count and summed primitive path count;
- physical C12 phase as a quotient of event order;
- exact two-step C6 shell semiconjugacy;
- spatial-only Markov no-go and six-state pivot-memory lower bound;
- no-finite-memory theorem under unrestricted exact path-history observers;
- explicit separation of physical event time from precision/root lineage.

Still open:

1. global inter-system synchronization between distinct local event clocks;
2. causal/partial-order semantics when independent Cell events are not totally ordered;
3. calibration from relation-update order to physical duration units;
4. coupling time to channel/internal state and non-periodic force networks;
5. whether P000 time is globally best represented by one total order, a partial order of events, or a richer directed event category.
