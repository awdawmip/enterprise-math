# X6 triadic network V3: local two-triad switch connectivity of every fixed-degree decomposition fiber

Status: `FREE_RESEARCH / EXACT COMBINATORIAL DYNAMICS / NOT_FOUNDATION`
Date: `2026-09-06`
Task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`
Depends on:
- equal-unit triadic decomposition criterion;
- triadic decomposition BRC polynomial `H^m`;
- integer force-quantum multiplicity lift V2.

## 1. From existence to reconfiguration

For a fixed equal-unit force-quantum degree vector

`d=(d_1,...,d_6)`

with

`sum_i d_i=3m`, `max_i d_i<=m`,

V1 proves that at least one decomposition into `m` distinct-axis triads exists.

A decomposition is a list/multiset

`D=(S_1,...,S_m)`,

where each `S_j` is a 3-subset of the six underlying native axes and each axis `i` occurs in exactly `d_i` triads.

The next question is whether different decompositions with the same aggregate degree vector are dynamically isolated or can be related by local degree-preserving changes.

They are all connected by two-triad switches.

## 2. Elementary two-triad symmetric exchange

Choose two triad occurrences `A,B` in a decomposition and choose

`a in A\B`, `b in B\A`.

Replace

`A -> A'=(A-{a}) union {b}`,

`B -> B'=(B-{b}) union {a}`.

Because `a` and `b` were not already present in the opposite triad, both `A'` and `B'` are again 3-subsets.

The total underlying-axis degree vector is unchanged exactly: one occurrence of `a` and one occurrence of `b` merely exchange triad membership.

Call this an **elementary triadic switch**.

It acts on only two primitive triadic closures at a time and introduces no vector-sum or continuum premise.

## 3. Incidence-matrix representation

Label the `m` triad occurrences temporarily. Associate to `D` the binary incidence matrix

`M_D in {0,1}^{6 x m}`

with

`(M_D)_{ij}=1 iff axis i belongs to triad occurrence j`.

Every column sum is 3 and the row sums are exactly `d_i`.

An elementary triadic switch is precisely the standard `2x2` binary interchange

`[[1,0],[0,1]] <-> [[0,1],[1,0]]`

on two axis rows and two triad-occurrence columns.

Thus the decomposition fiber is the fixed-margin binary-matrix fiber with six row margins `d_i` and all column margins 3.

## 4. Connectivity theorem

**Theorem.** Any two labeled equal-unit triadic decompositions with the same degree vector `d` are connected by a finite sequence of elementary triadic switches.

### Proof

Let `M,N` be their incidence matrices. They are binary matrices with identical row sums and identical column sums.

Color every entry where `M=1,N=0` red and every entry where `M=0,N=1` blue. View these entries as colored edges in the bipartite graph

`axis rows -- triad columns`.

At every row vertex, the red and blue degrees agree because `M,N` have the same row sum. At every column vertex they also agree because both matrices have column sum 3.

Therefore the symmetric-difference graph decomposes into alternating even cycles.

On one alternating cycle, replacing one red/blue crossing pair by the opposite crossing is a legal binary `2x2` interchange whenever the relevant chord is empty. If a candidate chord is already occupied, it splits the discrepancy into shorter alternating cycles. Induction on the alternating-cycle length therefore expresses the full cycle toggle as a sequence of legal `2x2` interchanges.

Applying this to every alternating cycle transforms `M` into `N` while preserving all row and column margins after every step.

Each interchange is exactly one elementary triadic switch. QED.

This is the standard fixed-margin binary-matrix switch argument, retyped here as native triadic-decomposition dynamics; no novelty is claimed for the matrix lemma itself.

## 5. Unlabeled/multiset decompositions are connected as well

Physical/BRC decompositions need not privilege an ordering of the `m` triad occurrences.

Choose arbitrary labels for the occurrences in two multiset decompositions. Their labeled incidence matrices have the same row margins and all columns have margin 3. The theorem connects them after some target column ordering.

Forgetting the temporary occurrence labels maps that switch sequence to a path between the original multiset decompositions.

Hence every nonempty fixed-degree decomposition fiber is connected under local two-triad switches.

## 6. BRC consequence: one support component, many provenance states

Let

`F(d)`

be the set of all triadic decompositions of `d`.

The theorem gives a connected switch graph on `F(d)` whenever `F(d)` is nonempty.

Therefore a Boolean observer asking only

“is some decomposition reachable by local degree-preserving reconfiguration?”

sees one connected support component.

But Path-formal/N-BRC can still distinguish:

- which decomposition state was used;
- which sequence of switches connected two states;
- switch multiplicity;
- event order/time;
- signed occurrence assignment and other internal provenance.

Connectivity is not permission to collapse the fiber for arbitrary future operations.

## 7. Six-force witness becomes a complete local reconfiguration graph

For

`d=(1,1,1,1,1,1)`, `m=2`,

an unlabeled decomposition is a partition of the six axes into two complementary triples. There are 10 such states.

Given one partition `A | A^c`, choose one axis from each triple and exchange them. Every other complementary partition is obtained by one such elementary switch after possibly exchanging the names of the two triad occurrences.

Therefore the unlabeled switch graph is the complete graph

`K_10`.

So the earlier 10-fold BRC decomposition ambiguity is not a set of ten isolated alternatives: every state is one local two-triad switch away from every other state.

## 8. Conditional stochastic dynamics

For fixed `d`, choose any strictly positive symmetric transition rate on every elementary switch edge.

Because the finite switch graph is connected, the resulting continuous- or discrete-time Markov chain is irreducible on `F(d)`.

If the rates are symmetric, the uniform distribution on labeled switch states (or the appropriately quotient-corrected distribution on unlabeled states) is stationary.

This is an optional dynamical model, not a P000 law. The theorem supplies only the exact connected state graph on which such laws may be placed.

## 9. Compatibility with event time

A two-triad switch is a local relation update involving exactly two triadic closure occurrences. Its event duration is not determined by the combinatorial switch theorem.

If two switches have disjoint declared force-token/internal resources and their updates commute, the native event-trace rule may leave them incomparable/parallel. If they share a triad occurrence or other resources, dependency order must be retained.

Thus triadic switch dynamics plugs directly into the current dependency-time architecture.

## 10. Completion-lift fibers

For an initially nondecomposable apparent force population, V2 supplies a family of minimal augmented populations `d'` with `DEFECT_3(d)` added quanta.

For each chosen completed degree vector `d'`, the present theorem says all its triadic decompositions lie in one local-switch component.

Different minimal augmented **degree vectors** need not be connected without changing which hidden quanta were added; that higher lift provenance remains a separate BRC layer.

Thus the exact hierarchy is

`apparent population`

`-> family of minimal augmented degree vectors`

`-> connected triadic-decomposition fiber for each degree vector`

`-> local switch histories`.

## 11. Current triadic-network frontier

Closed:

- existence criterion for a fixed equal-unit degree vector;
- minimal integer completion defect for nondecomposable populations;
- connectedness of every fixed-degree decomposition fiber under local two-triad switches;
- explicit K10 six-force witness;
- reusable finite state graph for stochastic/deterministic local reconfiguration laws.

Still open:

1. which switch transitions are physically admitted or weighted;
2. signed/token/internal-state constraints on switches;
3. unequal primitive quantum species or continuous effective calibration;
4. spatial coupling when the two triads act at different Cells;
5. interaction between switch dynamics and frame/channel holonomy.

No Foundation promotion is made.
