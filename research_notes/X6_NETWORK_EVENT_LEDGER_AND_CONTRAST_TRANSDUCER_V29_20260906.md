# X6 upper V29: conservative network event ledger and exact `(u,Omega)` contrast transducer

Status: `FREE_RESEARCH / EXACT INTEGER EVENT ALGEBRA + CONSERVATION THEOREM / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-CELL-CHANNEL-INTERNAL-STATE`, `RS-X6-NATIVE-TIME-DYNAMICS`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- `X6_PASSAGE_CONTINUITY_AND_NETWORK_BIAS_V28_20260906.md`;
- PF-10 ingress/egress/passage semantics;
- current dependency-event-time and BRC provenance discipline.
Checker: `experiments/x6_network_event_ledger_v29_20260906/check_network_event_ledger.py`.

## 1. Purpose

V28 gives a static/window identity

`u = (M-M^T)1 + R_in-R_out`.

The next question is dynamic:

> what primitive finite events update these nonnegative count objects, and which conservation laws follow before any continuum or field interpretation?

The answer is a small exact event algebra.

## 2. Network and local count ledger

Let `G=(V,E)` be a finite Cell interaction network. Each Cell x carries a declared finite internal port set; the current four-field application uses four typed source/port labels, while PF-10 itself may retain six channels.

For every Cell x retain only nonnegative integer counts

`M_x[a,b] in N_0`,

`Rin_x[a] in N_0`,

`Rout_x[a] in N_0`.

Define reconstructed PF-10 window counts

`I_x := M_x 1 + Rin_x`,

`O_x := M_x^T 1 + Rout_x`.

Thus the continuity inequalities are automatic rather than separately assumed.

Derived signed contrasts are

`Omega_x := M_x-M_x^T`,

`u_x := I_x-O_x = Omega_x 1 + Rin_x-Rout_x`.

The native stored ledger is nonnegative; signs occur only in derived exact differences.

## 3. Primitive event A: completed internal passage

For Cell x and two local ports a,b, define

`PASS(x;a->b)`

by

`M_x[a,b] += 1`.

All other M/Rin/Rout entries remain unchanged.

Consequently

`Delta Omega_x = E_ab-E_ba`,

`Delta u_x = e_a-e_b`.

The total scalar contrast at x is unchanged:

`1^T Delta u_x=0`.

The event records one completed ingress-a to egress-b occurrence. It is not a negative-flow update and never decrements a count.

## 4. Primitive event B: inter-Cell boundary transfer

For an allowed network connection from port a of Cell x to port b of Cell y, define

`TRANSFER(x:a -> y:b)`

by

`Rout_x[a] += 1`,

`Rin_y[b] += 1`.

No completed internal passage M is changed.

Hence

`Delta Omega_x=Delta Omega_y=0`,

`Delta u_x=-e_a`,

`Delta u_y=+e_b`.

The event is one relation crossing the declared Cell/window boundary. It is a single typed transfer occurrence, not two unrelated source/sink events.

## 5. Closed-network conservation theorem

Define the scalar network charge

`Q(L)=sum_x 1^T u_x`.

Every internal PASS event preserves Q because its local delta is `e_a-e_b`.

Every TRANSFER event preserves Q because its two endpoint deltas have scalar sums `-1` and `+1`.

Therefore any finite history generated only by PASS and matched TRANSFER events satisfies

`Q_after=Q_before`.

In particular, if Q is initialized at zero, it remains zero exactly.

This is finite counting conservation. It does not introduce a continuum divergence equation.

## 6. Exact event increments on the contrast observer

The projection

`pi_count : (M,Rin,Rout) -> (u,Omega)`

intertwines each primitive event with an exact additive increment:

- PASS(a->b): `(Delta u,Delta Omega)=(e_a-e_b, E_ab-E_ba)`;
- TRANSFER-out at a: `Delta u=-e_a`;
- TRANSFER-in at b: `Delta u=+e_b`;
- transfer leaves Omega unchanged.

Therefore the contrast state can be updated without recomputing the whole count ledger.

However this does **not** make `(u,Omega)` a globally operation-safe quotient. Futures asking absolute passage counts, residual totals, event multiplicity or provenance distinguish ledgers with the same contrasts.

For the specific V25/V28 active-triad score, `(u,Omega)` is sufficient only as long as all future update rules are themselves proved to factor through this contrast observer.

## 7. Cumulative count ledger is an additive history observer, not time

For a fixed collection of primitive event occurrences, final `M,Rin,Rout` is obtained by adding their incidence increments. Hence the final cumulative count ledger depends on the multiset of events, not on a serialization order.

This is useful compression for count-only futures.

But raw native time is the dependency/order of relation events. If an intermediate state is consumed by later dynamics, two different serializations of the same event multiset may produce different trajectories even though their final count ledger agrees.

V30 gives an exact two-event witness of this failure.

Thus

`CUMULATIVE COUNT LEDGER != NATIVE EVENT TIME`.

## 8. Batch independence versus dynamical independence

Two events that touch disjoint Cells/ports and whose declared future operations factor independently may be certified commuting and placed unordered in the native dependency trace.

By contrast, sharing an active Cell, frame, field context or downstream successor state creates a dependency even if their **final additive count increments commute**.

So event independence must be certified in the full future-operation language, not inferred from commutativity of a coarse count ledger.

This is an application of the existing Operation-Safe Quotient / BRC observer discipline, not a new top-level tool family.

## 9. Minimal autonomous network question after V29

V29 closes the count update grammar but does not choose which event occurs next.

A concrete autonomous network law still needs:

1. an event scheduler/relation selecting PASS or TRANSFER branches from current typed context;
2. active-triad/frame update after each dependent event;
3. possibly local inventory/legality semantics if one wishes to prohibit arbitrary cumulative transfers;
4. a rule for changing or resetting finite observation windows if M/Rin/Rout are not intended as lifetime cumulative counts.

Those choices are dynamical semantics, not consequences of nonnegative count arithmetic alone.
