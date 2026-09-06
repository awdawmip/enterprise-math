# X6 branch selection V3: no endpoint-only universal law, and event-context irreducibility

Status: `FREE_RESEARCH / EXACT NO-GO + MINIMAL REPAIR / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-NATIVE-ROTATION-DYNAMICS`, `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- atomic triadic scatter: common-Cell closure selects joint `III`;
- `VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md`: nonzero intermediate phase selects OUTER;
- `X6_UPPER_RELATIONAL_BUNDLE_INTEGRATION_V2_20260906.md`.
Checker: `experiments/x6_branch_selector_context_v3_20260906/check_branch_selector_context.py`.

## 1. The same spatial macro arrow supports two different valid laws

Fix one established FCC/K4 STAR triad `S` and its signed C6 generator `Q_S`. Let `a` be one signed unit-shell phase and

`b=Q_S a`.

Then `a,b` lie on two distinct native axes and the displacement `b-a` has exactly two shortest primitive Cell realizations:

`INNER: a -> 0 -> b`,

`OUTER: a -> a+b -> b`.

Both have the same:

- source Cell `a`;
- target Cell `b`;
- selected STAR `S`;
- macro frame update `Q_S`;
- primitive path count 2;
- shortest-path multiplicity 2.

So none of these data alone distinguishes the branches.

## 2. Atomic triadic closure requires INNER

For the equal-unit atomic triad, take the three signed force tokens on the active axes and evolve all three by the same `Q_S` macro update.

Each token independently has INNER and OUTER shortest branches, so the joint shortest branch population has `2^3=8` members.

The P000 atomic event is attached to one common action Cell. Exact enumeration shows that among the eight joint choices, precisely

`INNER x INNER x INNER`

has one common intermediate Cell for all three tokens, namely the pivot Cell.

Hence on the atomic-force interface:

`TRIADIC_CLOSURE_E -> SELECT INNER`.

This is a correlated three-path law, not three unrelated marginal preferences.

## 3. Nonzero phase refinement requires OUTER on the same macro arrow

On the established STAR C6/C12 phase interface, the same shell arrow `a->b` has:

- INNER midpoint `0`, where the radial phase direction is undefined;
- OUTER midpoint `a+b!=0`, whose carrier ray is the proved C12 half-angle/bisector ray.

The already-derived law

`REQUIRE_DEFINED_NONZERO_INTERMEDIATE_PHASE`

therefore selects exactly OUTER.

Hence on this rotation/phase interface:

`NONZERO_PHASE_REFINEMENT -> SELECT OUTER`.

## 4. Endpoint/frame-only selector no-go

Suppose a deterministic selector were a function only of any combination of the following macro data:

`(source Cell, target Cell, selected triad, frame element Q_S, shortest-path fiber)`.

For the same `a->b` these inputs are identical in the atomic-force and nonzero-phase events.

But the required outputs are different:

`force context -> INNER`,

`phase context -> OUTER`.

Therefore no such context-free selector exists.

The checker verifies this conflict on all six macro arrows of each of the four established STAR charts, giving 24 exact same-input/different-required-output witnesses.

This is stronger than saying “BRC has two branches”: it proves that **law selection itself is relation-context dependent**.

## 5. Minimal repair on the restricted two-law interface

On the restricted interface containing only these two event semantics, one additional two-valued event kind is sufficient:

`EVENT_KIND in {TRIADIC_ATOMIC_CLOSURE, NONZERO_PHASE_REFINEMENT}`.

Define

`selector(TRIADIC_ATOMIC_CLOSURE)=INNER`,

`selector(NONZERO_PHASE_REFINEMENT)=OUTER`.

Since one endpoint-only state must map to two different outputs, at least two context classes are also necessary.

Thus the minimal context cardinality on this restricted interface is exactly 2.

This does **not** say that one binary flag is sufficient for all native rotation/force laws. Generic rotation fibers remain richer.

## 6. Event kind belongs to the morphism/context layer

The new repair is not an eighth spatial coordinate and need not become a permanent subsystem state.

The correct typing is:

- the spatial Cell knows where the event occurs;
- the internal state records persistent relation variables needed by future updates;
- the event/morphism type declares which law is being applied;
- the law selects or weights its BRC path fiber.

If the next law invocation is externally/declaratively known, `EVENT_KIND` can remain part of the operation signature rather than stored state.

If the subsystem itself can switch autonomously between event kinds and future prediction must infer which comes next, a corresponding control/internal state becomes necessary.

## 7. Consequence for universal rotation law searches

There is no single “shortest native rotation path” rule valid across the current upper program.

The two exact sections already derived are:

- atomic triadic closure section: correlated INNER;
- nonzero phase/Viete section: OUTER.

Therefore future generic rotation research must ask

`WHICH EVENT LAW / OBSERVER REQUIREMENT?`

before collapsing a BRC fiber.

A candidate law that chooses INNER or OUTER solely from geometry of the macro endpoint pair is already refuted by the coexistence of these two interfaces.

## 8. Broader observer lesson

The no-go is an exact example of Joint Relation Observer Preservation:

`same spatial/frame observation != same admissible future operation`.

The missing distinction is not reconstructible from the coarse endpoint because it is the **role of the event in the relational process**.

This also explains why the upper architecture in V1/V2 separates:

`STATE`, `EVENT`, and `OBSERVER/CONTEXT`

instead of concatenating every distinction into one ontic coordinate vector.

## 9. Current law-selection frontier

Closed:

- exact same-arrow INNER/OUTER conflict;
- no endpoint/frame/shortest-fiber-only universal selector;
- exact two-class context lower bound and sufficient repair for the current force-vs-phase interface.

Still open:

1. classification of additional event semantics and their path-fiber sections/weights;
2. whether a more general physical principle predicts the event kind itself;
3. stochastic/signed-amplitude branch laws when no deterministic section exists;
4. coupling to unequal force quanta and multi-Cell interaction networks.

No Foundation promotion or external novelty claim is made.
