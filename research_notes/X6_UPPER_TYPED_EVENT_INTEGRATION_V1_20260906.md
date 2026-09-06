# X6 upper typed-event integration V1: state, event provenance, observer context, and law-specific memory

Status: `FREE_RESEARCH / SYNTHESIS + EXACT DERIVATIONS + NO-GO / NOT_FOUNDATION`
Date: `2026-09-06`
Task: `RS-X6-UPPER-STRUCTURE-INTEGRATION`

Consumes the current main-backed results:

- signed X6 spatial Cell torsor and centered slices;
- triadic signed-C6 frame group and concrete rotation paths;
- the correction `ROT_PATHCAT_X6`: raw concrete path category with reversal dagger, not a raw-concatenation groupoid;
- atomic triadic scatter and correlated `III` branch law;
- native event clock and dependency-trace time;
- 1920-state triadic Cell-internal fiber and PF-10 quotient hierarchy;
- all-20 slice native realization, FCC/no-Euclidean-carrier classification and `S3` chart holonomy;
- current noncommutative path tensor-jet results.

No P000/Foundation mutation is made.

## 1. First correction: upper structure is not one giant coordinate vector

The current results force three semantic layers.

### A. Dynamic/ontic state layer

A native spatial Cell is

`x in X6_NATIVE_SPATIAL`.

A subsystem may additionally carry an active relation/internal state `iota` over that Cell, for example the equal-unit triadic port state `(tau,mode)`.

These internal variables are not spatial coordinates.

### B. Event/morphism layer

Actual change is carried by typed events. An event may retain:

- a source and target decorated state;
- a concrete native Cell-path witness or a correlated family of path occurrences;
- a frame/rotation update;
- an internal-relation update;
- declared resource support used by the dependency-time test;
- exact event/path grades and BRC provenance required by the future observer.

Path history belongs primarily here, not as an extra coordinate on the spatial Cell.

### C. Observer/context layer

Carrier chart frame, selected three-axis observer, FCC projection, precision/root lineage and other readout parameters are context unless a separate physical law promotes them into subsystem state.

In particular:

- `J(6,3)` chart slot frame is observer atlas state;
- precision/root lineage is not automatically physical event time;
- an axis-channel bridge is extra relation/frame data, not spatial identity.

Thus the safe upper architecture is a typed fibration/category, not an untyped Cartesian product whose factors are all interpreted as equally ontic coordinates.

## 2. Universal event record

For a declared subsystem define a typed decorated state

`S=(x,iota)`

where `x` is spatial and `iota` is the internal/relation state required by that subsystem.

A provenance-preserving elementary upper event is a record

`E:S -> S'`

carrying, when applicable,

`(FRAME_UPDATE, PATH_FORMAL_WITNESSES, INTERNAL_UPDATE, RESOURCE_SUPPORT, GRADES)`.

The path field uses the current `PATHCAT_X6`/`ROT_PATHCAT_X6` typing: concrete reversal is a dagger involution, not a categorical inverse under literal concatenation.

Serial event composition is defined when target/source decorated states match. It composes frame/internal updates, concatenates concrete path provenance and adds the declared event grades.

No universal event inverse is assumed.

## 3. Dependency-time quotient

Let two upper events be certified independent only when:

1. their declared resources do not conflict;
2. their state updates commute on the relevant joint domain;
3. the future-operation language is insensitive to serialization order.

Then serial event words may be quotiented by swaps of adjacent certified-independent events. This is exactly the operation-safe dependency-trace construction already derived for native time.

Hence:

`FULL EVENT WORD -> DEPENDENCY TRACE/PARTIAL ORDER -> OPTIONAL LINEARIZATION/TIMESTAMP READOUT`.

The first arrow may preserve endpoint dynamics while discarding irrelevant scheduling order, but it is not safe for a future observer asking for the original serialization unless that observer has been excluded.

## 4. Rotation and triadic force fit the same event interface

### Generic rotation

A rotation event may carry frame label `g` plus one concrete path witness `gamma:x->gx`, or a Path-formal/BRC family of alternatives.

### Atomic triadic force event

A canonical equal-unit atomic triad carries three correlated force-port path occurrences. Before imposing the law, each token has INNER/OUTER alternatives and the joint shortest population has eight members.

The common-Cell atomic closure law selects exactly `III`.

Therefore a triadic event is not three independent branch variables. Its branch state is a joint relation constrained by one atomic incidence law.

This is a concrete example where an untyped product of marginals creates spurious states.

## 5. Law-specific witness sections

Suppose a deterministic law on decorated states is

`L:S -> S`

and for every state `s` it supplies a unique concrete event witness

`w(s):s -> L(s)`.

Then for forward prediction of the same law, the current state `s` is Markov-complete: the next event witness is reconstructed as `w(s)` rather than stored as an independent branch coordinate.

Given an initial state `s_0` and event count `N`, the full law-generated history is also reconstructible by concatenating

`w(s_0), w(L s_0), ..., w(L^{N-1}s_0)`.

But the **current periodic state alone** does not reconstruct how many prior periods occurred. Exact historical queries therefore still require event count/history information.

### Current exact examples

- atomic equal-unit triadic law: the section is joint `III`;
- current faithful Viète phase/root law on its declared interface: the section is OUTER;
- generic rotation before law selection: no unique section exists, so branch provenance must remain.

Therefore “keep every branch bit forever” and “erase every branch immediately” are both wrong. The correct rule is law/observer typed.

## 6. Tensor path jets are compositional summaries, not path identity

The current path-jet theorem defines

`PJ_K(gamma)=(M,S_1,...,S_K)`

with exact concatenation law in truncated tensor algebra, signed-frame covariance and dagger action.

For one shortest six-macrostep triadic frame cycle:

- degree 1 gives 1 class on the 64 branch histories;
- degree 2 gives 27 classes;
- degree 3 is injective on all 64 histories.

The parallel two-cycle calculation shows first lossless order 5 on that ordered 4096-history population.

These are exact **population-scoped** compression theorems.

## 7. Strong no-go: even the all-order tensor jet is not raw path identity

Take one native axis `e_i` and two length-two concrete paths

`gamma=(+e_i,-e_i)`,

`eta=(-e_i,+e_i)`.

They are different Path-formal witnesses because their first transition is different.

But

`S_1(gamma)=S_1(eta)=0`,

and

`S_2(gamma)=S_2(eta)=-e_i tensor e_i`.

There are no higher nonzero subsequence tensors for a length-two word. Thus

`PJ_K(gamma)=PJ_K(eta)`

for every `K>=2`, even with exact length included.

Therefore no tensor-jet order, including the full finite jet of these paths, equals raw Path-formal identity on the unrestricted signed path category.

The path jet is a powerful relation-sensitive observer, not a replacement ontology for concrete path history.

## 8. No fixed finite jet order is globally provenance-complete

There is also a general counting obstruction.

Fix `K`. For paths of length `M` over the twelve signed primitive steps, each tensor coordinate of `S_k` is an integer between

`-C(M,k)` and `+C(M,k)`.

There are `6^k` tensor coordinates at degree `k`. Hence the number of possible order-`K` jets at fixed length is at most

`prod_{k=1}^K (2*C(M,k)+1)^(6^k)`,

which grows polynomially in `M` for fixed `K`.

The number of raw signed step words is `12^M`, exponential in `M`.

Therefore for every fixed `K`, sufficiently long distinct concrete paths collide under `PJ_K`.

Adding any fixed finite frame/internal/phase decoration, or the spatial endpoint whose number of possibilities at length `M` is only polynomial in `M`, does not remove this asymptotic collision.

So globally exact path provenance requires either the raw Path-formal carrier or a memory family whose expressive order grows with the declared path population/horizon.

## 9. Irreducibility witnesses for the current upper factors

The current program now has explicit witnesses for why several factors cannot be silently identified.

### Spatial Cell versus internal relation

Six closure phases `Kappa_r` share one pivot Cell but have six different deterministic successors. Spatial state alone is not Markov.

### Frame transform versus spatial Cell

At a chosen coordinate anchor `0`, all frame transformations fix the spatial point. Yet a future labeled-axis operation distinguishes identity from a nontrivial `Q_S`. Frame action is therefore not encoded by the anchor coordinate.

### Internal signed triad versus PF-10 channel passage

A directed unsigned PF-10 3-cycle has 24 full signed/token frames above it. Passage counts do not determine the active triadic relation.

### Path provenance versus frame/endpoint

A complete `Q_S^6=1` cycle has 64 shortest concrete path lifts with the same frame closure and endpoint.

### Event order versus current state

Certified-independent events may have multiple serializations with one dependency trace; conversely dependent events with identical endpoint can remain distinguishable by future history queries. Time/order is neither simply endpoint state nor arbitrary total order.

### Native chart versus carrier frame

All 20 native three-axis selections exist, but only four are current-FCC 120-degree charts. The all-20 triangular atlas has `S3` frame holonomy, so no path-independent global three-slot carrier frame exists.

### Physical event phase versus precision lineage

The former advances under relation updates; the latter can remain static along a fixed-chirality Viète trajectory.

These witnesses justify semantic separation without claiming ontic independence of every convenient implementation field.

## 10. Current minimal deterministic triadic subsystem

For the current restricted equal-unit atomic law, a practical exact Markov state over one action node can be represented as

`(c, tau, mode)`

where

- `c` is the pivot spatial Cell;
- `tau` is one of 960 ordered signed triadic port frames;
- `mode in {SHELL,CLOSURE}`.

The local internal fiber has 1920 states and deterministic C12 update. The atomic branch choice `III` is derived by the law and need not be stored as an independent next-step bit for this Markov horizon.

A separate event index/dependency trace is required when the future language asks elapsed order/history rather than only next-state prediction.

Carrier chart and precision/root parameters remain observer/context data unless a particular physical subsystem couples them explicitly.

## 11. Current minimal generic-rotation subsystem

Before a rotation-path law selects one witness, the state/event carrier must remain richer:

- spatial source/target;
- frame transform;
- concrete Path-formal/BRC path population or a proved scope-sufficient summary such as `PJ_K`;
- resource support/dependency order when composing with other events.

No universal finite Markov quotient of this generic carrier has been proved.

## 12. Operation-safe quotient lattice

The current reusable direction is:

`PATH-FORMAL EVENT`

`-> optional law section / scope-sufficient path jet`

`-> frame + internal relation + event grade`

`-> spatial endpoint / PF-10 / carrier chart / Boolean support`

with every downward arrow governed by T6/Joint Relation Observer Preservation.

Different downstream observers induce different safe quotients; there is no single universally preferred collapse.

## 13. Integration status

The five upstream programs now fit one typed architecture:

1. **spatial** — X6 Cell torsor;
2. **rotation** — signed frame algebra plus concrete path dagger category;
3. **triadic force** — correlated multi-path atomic event and law-specific `III` section;
4. **internal/channel** — finite relation fiber over Cells, with PF-10 as coarser positive traffic observers;
5. **time** — dependency/order of relation events, with local finite phase quotients;
6. **carrier/chart** — observer atlas with `S3` transition holonomy;
7. **precision** — separately typed refinement/root parameter.

The remaining upper-level questions are no longer basic typing problems. They are law/calibration questions:

- unequal force quanta and multi-Cell interaction rules;
- physical duration/energy calibration of event layers;
- channel exchange between neighboring Cells;
- which generic rotation path laws nature admits;
- physical interpretation, if any, of carrier/chart and path holonomies;
- application-specific safe quotient interfaces for number theory and PDE programs.

No Foundation promotion or external novelty claim is made.
