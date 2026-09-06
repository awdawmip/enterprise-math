# X6 native time V3: duration as a calibrated critical-path valuation on event dependency

Status: `FREE_RESEARCH / CONDITIONAL CALIBRATION THEOREM / NOT_FOUNDATION`
Date: `2026-09-06`
Task: `RS-X6-NATIVE-TIME-DYNAMICS`
Consumes:
- native event dependency/trace partial order V2;
- triadic atomic event synchrony;
- P000 finite-resolution-first and `TIME_ROLE=TRACE_AND_ORDER_OF_RELATIONAL_CHANGE`.

## 1. Order is native; duration needs calibration

The current native-time research has already separated:

- event dependency/order;
- local periodic phase;
- path/force occurrence count;
- precision/root lineage.

P000 does not yet assign a physical duration to one relation update. Therefore no number of seconds, or any continuum duration unit, is derived here without extra calibration data.

This note asks a narrower question:

> once local event durations are supplied as calibrated positive values, what scalar elapsed-time functional is forced by the dependency poset under ideal unlimited concurrency?

## 2. Weighted event poset

Let a finite physical event history be a dependency poset

`P=(E, <)`

from the V2 event-trace construction. Each event `e` receives a positive calibrated duration

`tau(e)>0`.

The calibration may depend on resolution, event type and physical context. It is not another spatial coordinate and need not be uniform.

A legal schedule assigns start times `s(e)>=0` such that

`e<f -> s(f)>=s(e)+tau(e)`.

The schedule makespan is

`T_sched=max_e [s(e)+tau(e)]`.

Assume no resource-capacity limit beyond the dependencies already represented in the poset: incomparable events may execute concurrently.

## 3. Critical-path theorem

Define the weighted height

`T_crit(P,tau)=max_{chains e_1<...<e_r} sum_j tau(e_j)`.

**Theorem.** The minimum possible makespan over all legal unlimited-concurrency schedules is exactly

`T_min=T_crit`.

### Lower bound

Along every dependency chain the events must execute sequentially, so every legal schedule has duration at least the sum of durations on that chain. Taking the maximum gives

`T_sched>=T_crit`.

### Achievability

Assign each event its earliest possible start time

`s(e)=max_{f<e immediate/predecessor path} [s(f)+tau(f)]`,

with zero for minimal events. Equivalently, the finish time of `e` is the maximum weighted-chain sum over chains ending at `e`.

This schedule respects every precedence relation and its global finish time is exactly the maximum weighted-chain sum. Thus

`T_sched=T_crit`.

No continuum geometry is used; only the finite dependency relation plus calibrated local durations.

## 4. Serial and parallel laws

The theorem gives the expected exact composition rules.

### Serial composition

If every event of history `A` precedes every event of history `B`, then

`T_crit(A;B)=T_crit(A)+T_crit(B)`.

### Independent parallel composition

If `A` and `B` have no dependency edges between them, then

`T_crit(A || B)=max(T_crit(A),T_crit(B))`.

Thus elapsed duration uses additive composition along causal/dependency chains and max composition across certified-independent parallel branches.

This is a max-plus/critical-path readout of the native event order. It is a standard scheduling construction reused here as a calibration interface, not claimed as a new algebraic invention.

## 5. Uniform event-duration specialization

If every elementary relation-update layer in the declared subsystem has one calibrated duration `tau_0`, then

`T_min=tau_0 * height(P)`,

where `height(P)` is the maximum number of events in a dependency chain.

For one deterministic INNER triadic C12 process the dependency poset is a 12-event chain, so one complete period has

`T_period=12 tau_0`.

For `k` mutually independent equal-duration atomic events in one layer, the history is a `k`-element antichain and

`T_min=tau_0`,

not `k tau_0`.

This is the precise reason total primitive transition occurrence count is not automatically elapsed time.

## 6. Atomic triadic event example

One shell-to-closure update contains three simultaneous incoming force-port transition occurrences meeting one Cell. They belong to one atomic relation layer.

If that atomic layer is assigned duration `tau_in`, the elapsed duration of the layer is `tau_in`; it is not the sum of three per-token path counts.

Likewise the outgoing closure-to-shell layer has its own duration `tau_out`.

One full triadic macrostep therefore has calibrated duration

`tau_macro=tau_in+tau_out`

when the two layers are sequential.

The six transition occurrences remain meaningful for work/traffic/BRC counts, but they do not become elapsed time by multiplication with a universal per-edge constant unless an additional theorem identifies those semantics.

## 7. Work/count versus duration

For a finite event history define several distinct quantities:

- number of relation events;
- number of primitive path/force occurrences;
- dependency height;
- calibrated critical-path duration.

They need not agree.

An antichain of many simultaneous events can have large event/occurrence count but small height and duration. A long causal chain can have the same count and much larger duration.

Therefore:

`EVENT_WORK_COUNT != ELAPSED_DURATION`.

Any effective rate, flux or force-like quantity formed as “calibrated action per elapsed duration” needs both numerator and duration calibration; it cannot be inferred from a raw event count alone.

## 8. Minimal calibration data

To turn the current order-only native time into a scalar duration readout for a declared finite subsystem, the minimum additional data in this model are:

1. a certified dependency poset/event trace;
2. a positive local duration map `tau` on event occurrences or event types/context;
3. an explicit concurrency assumption/resource model.

Under unlimited concurrency, the critical-path theorem gives the scalar duration uniquely from these data.

If extra resource constraints prevent nominally independent events from overlapping, those constraints must be added as dependencies or scheduling resources; the plain poset critical path is then only a lower bound.

## 9. Resolution and refinement

Under finite-resolution-first semantics, a duration calibration should be tagged by resolution/context, for example

`tau_delta(event_type,context)`.

Refining the Cell or event language does not force

`tau_fine = tau_coarse / r`

by native counting alone. A refinement compatibility law is separate physical evidence.

Likewise the Viète precision/root pro-state is not a duration refinement clock.

## 10. Optional effective action-rate bridge

If a later physical bridge calibrates one primitive action/impulse quantum by a value `q_delta`, then for a declared population of `N` such occurrences over a dependency history of duration `T_crit`, one may form an effective rate

`R_eff = q_delta * N / T_crit`.

Whether a particular external observable interprets this as force, flux, current or another rate is an external/bridge typing question. The formula is not promoted to a native force definition here.

## 11. Current time frontier

Closed conditionally in this stage:

- order/dependency to scalar-duration bridge once local durations are calibrated;
- exact serial-sum and independent-parallel-max laws;
- uniform-duration height formula;
- precise separation of event work/traffic count from elapsed duration.

Still open:

1. physical determination of `tau_delta` for native event types;
2. synchronization/calibration between different event classes and Cells;
3. resource limits or propagation constraints that add dependencies beyond relation support;
4. continuum-time recovery and comparison with external spacetime models;
5. whether duration is fundamental or only an effective readout of deeper event relations.

No P000/Foundation mutation is made.
