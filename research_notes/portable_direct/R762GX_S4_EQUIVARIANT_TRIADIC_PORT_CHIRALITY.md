# R762GX — S4-equivariant oriented Port repair for a typed K4-STAR triadic candidate

Date: 2026-11-20 (Asia/Shanghai). Author-side continuation of `RS-X6-TRIADIC-CLOSURE-DYNAMICS` / `TP2-8B7E13C5904A2D6F1142`.
Frozen scientific sources: taskbook at `awdawmip/enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8`; P000 V5 and native triad/Cell foundations at `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Method/rule context is read separately at current `main`. Starting finite signed STAR inventory results: R762GT/GU/GW. Independent review: `NOT_REVIEWED`.

## Precise question and result

The mother objective requires a signed `TRIADIC_CLOSURE_E` Cell/Link/Port event with six-axis spatial and separately typed time behavior. This note constructs an explicit **candidate realization**, without asserting that its chosen Link/Port law is the unique or canonically admitted native physical law.

The first result is a sharp obstruction: **a nontrivial deterministic update that turns an incident Port to a different edge at the selected STAR vertex cannot be fully equivariant under the already-established K4 carrier group S4 if the state remembers only the active vertex and the incoming Port.** There are two S4-covariant remedies: retain two positive BRC successor branches, or retain one extra orientation/chirality bit. One bit is both necessary and sufficient for deterministic full-S4 covariance of such a turn. Under A4 alone, a bit-free deterministic turn is possible.

A second result supplies a typed signed candidate transport and proves a conditional six-event first spatial-plus-Port return, with 20 ordered positive BRC source histories. All claims below are model-internal.

## Definitions: six native axes; four auxiliary STAR labels

Let `V={0,1,2,3}`, and identify the six edges `E(K4)={01,02,03,12,13,23}` with the six **native X6 axis labels**. The four vertex labels are auxiliary incidence indices, not additional physical dimensions. For each vertex `v`, let `H_v in Z^6` have a 1 on the three incident edges, zero elsewhere. The six-axis spatial Cell is a torsor over `Z^6`; a chosen chart writes its displacement as `x`. The four triples `{vw:w!=v}` have three distinct native axes, hence they are pairwise `PERP_E` with the P000 native 120-degree relation.

Define a **candidate STAR closure subfamily** `C_star(v,s)`, where `s in {+1,-1}`, consisting of three coattached equal-magnitude nonzero signed primitive force quanta `(sE_vw)_(w!=v)` with an explicit triadic Link witness. Each quantum is primitive on its own native axis; the triple and its possible transport are composite. The predicate `C_star` is a proposed sufficient realization of the arity/angle requirements, not an exhaustive interpretation or a proof of native permission for every candidate event. We do not define closure by Euclidean vector-sum-zero.

A Port is an unordered incident edge `e={u,v}` with the selected event vertex `v in e`; `u` is the partner. The two remaining vertices are `a,b`. A stored chirality `chi in {+1,-1}` is relative to the reference ordering `(0,1,2,3)`. Define the unique successor `a=T_chi(v,u)` by

```
a != u,v; b is the other remaining vertex;
sgn(v,u,a,b) = chi;
new Port e' = {v,a}.
```

The ordered triad-step witness is `W=(vu,va,vb;s)`; the ordered Link witness records `(e -> e';v,chi)`. A typed event at chosen chart Cell `x`, incoming Port `e`, chirality `chi` and event-order clock `t` is

```
F_(v,s): (x,e,chi,t) |--> (x+s H_v, {v,T_chi(v,u)}, chi, t+1),
         with stored W, Link, force-triplet and event source identity.
```

Here `x+s H_v` is a **declared three-primitive-step composite transport**, not an assertion that balanced forces necessarily produce physical movement. `t` is a separately typed model event ordinal, not a seventh spatial axis, absolute heartbeat interval, or a physical time-calibration law. Source/Link histories remain available; endpoint-only compression is not assumed safe.

An axis-label permutation `pi in S4` acts on X6 by its induced permutation of the six edge-axes and acts on the extended Port state by

```
pi : (v,u,chi) |--> (pi(v),pi(u),sgn(pi)*chi).
```

The sign change is the transformation of a pseudoscalar orientation reference; it does not change a primitive force sign `s`.

## Theorem GX1 — exact S4 obstruction and minimal repair

For any incident `(v,u)`, a deterministic function `f(v,u) in V\{v,u}` selecting a **different** edge `{v,f(v,u)}` cannot satisfy `f(pi(v),pi(u))=pi(f(v,u))` for every `pi in S4`.

**Proof.** Fix `(v,u)` and call the two unused vertices `a,b`. The transposition `pi=(a b)` fixes `v` and `u`, but exchanges the two permitted successors. Equivariance would require `f(v,u)=pi(f(v,u))`, impossible for a value in `{a,b}`. This proves impossibility without a residual branch/state. A two-way successor relation `{a,b}` is S4-equivariant with two distinguishable positive BRC branches. For a deterministic successor any residual-state fiber must have at least two states, since a one-state fiber is fixed by the transposition. The `chi` construction above has exactly two states and satisfies

```
T_(sgn(pi)*chi)(pi(v),pi(u)) = pi(T_chi(v,u))
```

because `sgn(pi(v),pi(u),pi(a),pi(b))=sgn(pi)sgn(v,u,a,b)`. Thus two states suffice. QED.

Under A4, the stabilizer of an ordered pair `(v,u)` is trivial; A4 of order 12 acts freely and transitively on the 12 ordered incident pairs. Therefore either of the two A4-equivariant cyclic-turn maps is possible without a `chi` variable. This is a symmetry-scope comparison, not a reason to identify A4 with the complete native rotation group.

## Theorem GX2 — 24-state oriented-Port torsor and covariance

The 24 triples `(v,u,chi)` with `v!=u` form a free and transitive `S4`-set under the action above. Moreover each signed `F_(v,s)` is equivariant under this action, provided the six-axis Cell, witness sequence and Port/Link axes are permuted accordingly and the event ordinal is held separately.

**Proof.** The stabilizer of `(v,u)` has size two: identity and transposition of the two unused vertices. The latter is odd and flips `chi`, so the stabilizer of `(v,u,chi)` is trivial. Since `|S4|=24` equals the number of triples, the action is also transitive. GX1 gives Port covariance; `pi H_v=H_pi(v)` gives X6 covariance; the ordered triad witness and Link are mapped entrywise; `t+1` is unchanged by spatial relabeling. QED.

A visible signed Cell update can therefore be the same for two states which have distinct next allowed Ports. For example at incoming `e=01`, active `v=0`, sign `s=+1`, the two `chi` states both add `H_0=(1,1,1,0,0,0)`, but successor Ports are `02` and `03`. A next event selecting active vertex 2 is eligible from the former and ineligible from the latter. This is a **one-step future-permission counterexample** to deleting chirality when the observer includes future Port gates, even if the current Cell increment and event time are retained.

## Theorem GX3 — exact fixed-vertex return counts

Fix a vertex `v`, initial incident partner `u`, chirality `chi`, and restrict every subsequent event to the same active vertex `v`. Permit independent signed event inputs `s_j in {+1,-1}`. The Port partner successor `u -> T_chi(v,u)` is a 3-cycle on the three neighbors of `v`. Thus for any length `m>=0`,

```
Port_m = Port_0  iff  3 | m,
Cell_m = Cell_0  iff  sum_(j=1)^m s_j = 0,
```

and the joint Cell+Port return count among signed ordered source words is

```
N_m = binom(m,m/2)  if 6 | m,
      0              otherwise,
```

with `N_0=1`. The shortest nonempty joint return has length **six**, and **N_6=20** distinct ordered source words. Under equal positive BRC weights for the two sign choices at each step, the conditional six-step return probability is `20/2^6=5/16`.

**Proof.** For fixed `v,chi`, `T_chi` chooses one of the two other neighbors in a consistent cyclic orientation. It is a fixed-point-free permutation of the three neighbors, hence a 3-cycle. The signed six-axis displacement is `(sum s_j)H_v`; because `H_v !=0`, return requires equally many positive and negative signs, possible exactly for even `m`, with `binom(m,m/2)` source words. Intersection of the divisibility conditions gives `6|m`. The clock increases by `m`, so a nonempty spatial+Port return is **not** a full spacetime-state return. QED.

At `m=6`, the conditional endpoint-and-Port fiber contains 20 histories; recovering its full ordered sign word requires at least `ceil(log2 20)=5` repair bits **within this declared fiber**. The count concerns this fixed-active-vertex, fixed-initial-`chi` experiment only.

## Exact validation and boundary

`R762GX_CHECK.js` exhaustively enumerates all 24 K4 label permutations, 12 incident `(v,u)` inputs, two chiralities and two signs: **1,152 covariant event cases** (including signed X6 increment and ordered Link witness). It also checks the 24 oriented states, 24 stabilizer-obstruction instances, all 24 three-turn cycles, the concrete observer-loss witness, and exact return counts for `m=0..10` by enumerating signed words. The test of the stored checker source was `PASS`. `R762GX_EVIDENCE.json` holds the exact output and scope.

Theorems GX1–GX3 are mathematically proved for the declared K4-STAR *candidate*; the finite checker audits all finite symmetry data and short source counts. Further mother-objective work: establish actual admissible `TRIADIC_CLOSURE_E` force/Cell/Link/Port events beyond the constructed sufficient candidate, compare to frozen signed native event permissions, and determine whether the chirality residual is intrinsic or is absorbed into a richer native Link/rotation carrier. Do not promote candidate transport, signed force closure or a model event ordinal into a new P000 axiom. Independent review `NOT_REVIEWED`.

## Source and control custody

This is author-side portable research. GitHub branch/PR publication and immutable file readback establish file custody, not an authenticated Task `PROGRESS`, Result freeze or peer acceptance. Existing contributor line: `EM-X6-3050F6` with original public session reference `MCP-4b2d70a97f594366a7c94a0f8b45df38`; this note grants no new claim or execution role. Keep existing completed source pointers and original request IDs; reconcile rather than replay unknown control writes.
