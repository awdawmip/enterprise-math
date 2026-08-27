# Driver Review — R043-C5 Octahedral Opposite-Pair Global Realizability

Status: `DRIVER_FINAL / ACCEPTED / GLOBAL_PINCH_IMPOSSIBILITY_PROVED_FCC_AND_HCP / R043C3_POSITIVELY_CLOSED / RESULT_ONLY`

Date: `2026-08-27`

Driver-ID: `EM-DVR-K7Q4N8 / CONTROL_PLANE`

Task: `RS-R043C5-OCTAHEDRAL-OPPOSITE-PAIR-GLOBAL-REALIZABILITY`

Publication: `TP2-3A4A96DB6B0E34DEB969`

Execution: `ER-392110949F52CE665B5C`

Researcher-ID: `EM-R043C5-8F341F`

Result: `RR-D4B443215DC78E8ACFF3`

Source PR: `#659`

Reviewed PR head: `b41861b30899ec6fbbb9eadd62b84520a642fa6e`

Evidence materialization on current main: `e56a13b91716b4e7953cfafe5e0651a2f60e415e`.

## 1. Final disposition

`DRIVER_DISPOSITION = ACCEPTED`.

`HARD_TARGET = SATISFIED`.

`RESULT_CLASS = GLOBAL_NATIVE_FRONTIER_CONNECTIVITY_THEOREM / R043_C5_CLOSURE`.

`GLOBAL_OPPOSITE_PAIR_PINCH_IMPOSSIBILITY_FCC = PROVED`.

`GLOBAL_OPPOSITE_PAIR_PINCH_IMPOSSIBILITY_HCP = PROVED`.

`R043C3_GLOBAL_FRONTIER_CONNECTIVITY = POSITIVELY_CLOSED_FCC_AND_HCP`.

`R043C2 = UNCHANGED`.

`G0_COMPONENT_GROUPING_AMBIGUITY = REMOVED_FOR_FCC_AND_HCP`.

`FOUNDATION_MUTATION = NONE`.

`SUCCESSOR_TASK = NONE_FROM_C5`.

The Driver accepts the global impossibility proof. The bounded one-shell computation remains regression only and is not load-bearing.

## 2. Accepted theorem

For every nonempty finite connected occupied set `C` in either frozen FCC or frozen HCP native 12-contact world, and every connected component `Omega` of the unoccupied graph,

`F(C) intersect Omega`

is connected under native 12-contact.

Consequently, the unique C4 octahedral opposite-pair local point pinch may exist locally, but if both local sides lie in the same unoccupied component they necessarily reconnect through the native frontier elsewhere. No finite C5 counterexample exists in either frozen world.

## 3. Driver audit of the topology bridge

Fix `C` and `Omega`. Let `K_Omega` be the finite native interface 2-complex consisting of shared native 2-faces between `Omega` cells and complement cells.

The following points were checked as load-bearing rather than inferred from continuum intuition:

1. **Finiteness.** Since `Omega` is a component of the unoccupied graph, no native edge joins it to another unoccupied component. Every site across its interface therefore lies in finite `C`; finite degree then makes `K_Omega` finite.
2. **Two complementary sides.** `Omega` is native-contact connected, hence its cell union minus the interface is connected. The complement-site set is connected: it contains connected `C`, and every other unoccupied component has a native contact to `C` because the full native graph is connected. Thus the complement of `K_Omega` in the one-point compactification has exactly two connected components.
3. **Alexander-duality rank.** Applied only to the finite native polyhedral complex `K_Omega` embedded in `S^3`, Alexander duality over `F_2` yields `dim H^2(K_Omega;F_2)=1`; finite-dimensional field duality gives `dim H_2(K_Omega;F_2)=1`.
4. **No hidden 3-boundaries.** `K_Omega` is an interface complex of dimension at most two, so `B_2=0`.
5. **Component cycles.** For each native frontier component `Gamma`, summing interface 2-faces whose `Omega`-side site lies in `Gamma` gives a nonzero mod-2 2-chain `z_Gamma`.
6. **Boundary cancellation is native.** Each interface 1-cell is dual to a native Delaunay triangle. A binary `Omega/complement` coloring of a triangle has zero or two cut edges. If the two cut edges expose two distinct `Omega` sites, those sites share the third native triangle edge and therefore belong to the same frontier component. Hence every fixed `z_Gamma` has zero mod-2 boundary.
7. **Independence.** Distinct frontier components give disjoint interface-face supports. Because there are no 3-boundaries, the corresponding nonzero `H_2` classes are linearly independent.

Therefore if there are `r` frontier components,

`r <= dim H_2(K_Omega;F_2)=1`.

The slice is nonempty, so `r=1`.

This is a native-cell-complex theorem. Alexander duality is used as an exact theorem on the finite interface carrier; Euclidean-distance surrogate adjacency or an untyped continuum surface argument is not used.

## 4. FCC/HCP local incidence audit

The task-local exact checker separately verifies the finite incidence hypotheses in both frozen worlds:

- 12-contact neighbor models;
- `8` tetrahedra and `6` octahedra through a site;
- `24` native triangular faces through a site;
- each such triangle is incident to exactly two local Delaunay 3-cells;
- codimension-two binary cut parity is `0_OR_2`;
- the HCP parity-changing automorphism;
- C4 tetrahedron `14/0` and octahedron `62/6` classification;
- local `4+4` pinch split;
- minimal repair profile `4,2,1,2,4`;
- `12,951 / 0` one-shell pressure regression in each world.

The finite checker supports the native-incidence hypotheses but does not certify the Alexander-duality theorem by enumeration.

## 5. CI status boundary

PR #659 remained Draft at reviewed head, so its three GitHub checks are `skipped`, not `success`. This Driver review does not relabel skipped CI as passed.

Acceptance rests on the exact frozen proof and the task-local deterministic incidence checker/source artifacts. The result/evidence files have been materialized on current main before this review.

## 6. Consequence boundary

Accepted consequence:

`R043C3 = POSITIVELY_CLOSED_FCC_AND_HCP`.

Together with the already-frozen R043-C2 component factorization, the specific hidden **component-grouping** ambiguity in stationary G0 is removed for FCC/HCP.

This does **not** by itself prove the full stationary-G0 program. Any single-component rooted successor-extension rigidity question remains a separate layer and must be opened only by an explicit Driver decision.

No Foundation promotion follows from this theorem.

## 7. Final freeze

`RS-R043C5-OCTAHEDRAL-OPPOSITE-PAIR-GLOBAL-REALIZABILITY = TERMINAL / ACCEPTED`.

`RR-D4B443215DC78E8ACFF3 = ACCEPTED`.

`DESTINATION = RESULT_ONLY / R043C3_CLOSURE`.

`UNRESOLVED_RESIDUE_WITHIN_C5 = NONE`.

`SUCCESSOR_FROM_C5 = NONE`.
