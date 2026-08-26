# R043-C5 — Octahedral Opposite-Pair Global Realizability Return

Status: `FROZEN FINAL RETURN / GLOBAL_OPPOSITE_PAIR_PINCH_IMPOSSIBILITY_PROVED_FCC_AND_HCP / NOT CANONICAL`
Date: `2026-08-26`
Task-ID: `RS-R043C5-OCTAHEDRAL-OPPOSITE-PAIR-GLOBAL-REALIZABILITY`
Publication-ID: `TP2-3A4A96DB6B0E34DEB969`
Researcher-ID: `EM-R043C5-8F341F`
Claim-ID: `chatgpt-r043c5-20260826-1810`
Execution branch: `research/r043c5-global-pinch-em-r043c5-8f341f`
Execution base: `f781c458b1dc4f3ec1c5cab9cdfc244ce11220f7`

## 0. Primary verdict

`GLOBAL_OPPOSITE_PAIR_PINCH_IMPOSSIBILITY_PROVED_FCC_AND_HCP`.

`R043C5_OCTAHEDRAL_OPPOSITE_PAIR_GLOBAL_REALIZABILITY_DECIDED = SATISFIED`.

Stronger theorem proved:

> For every nonempty finite connected occupied set `C` in the frozen FCC or HCP native 12-contact world, and every connected component `Omega` of the unoccupied graph, the visible frontier slice
>
> `F_Omega = F(C) intersect Omega`
>
> is connected under native 12-contact.

Thus the unique R043-C4 octahedral opposite-pair point pinch can occur locally, but if its two sides remain in the same `Omega` they must reconnect elsewhere through the native frontier. No finite C5 counterexample exists.

## 1. Frozen predecessor boundary

Consume R043-C4 exactly at:

`LOCAL_SEPARATOR_FOUND_GLOBAL_REALIZABILITY_OPEN`.

Frozen regressions:
- tetrahedron: `14` nonconstant colorings, `0` bad;
- octahedron: `62` nonconstant colorings, `6` bad;
- bad type: exactly an opposite-vertex pair or color complement, with local cut split `4+4`;
- minimal FCC/HCP repair profile: `4,2,1,2,4`;
- fixed C4 one-shell pressure: `12,951` connected extensions per world, `0` disconnects.

The `12,951` result is regression only and is not used as global impossibility evidence.

## 2. Native interface complex

Fix `C` and `Omega`. Use the same native close-packed cell/star thickening admitted by R043-C3, where native 12-contact is shared native 2-face adjacency.

After one-point compactification, work in the induced cellulation of `S^3`.

Let:
- `B_Omega` be the union of native cells whose sites lie in `Omega`;
- `A_Omega` be the union of all remaining native cells;
- `K_Omega = A_Omega intersect B_Omega`.

`K_Omega` is finite and 2-dimensional. Its 2-cells are exactly the native interface faces `f_{c,x}` with `c in C`, `x in Omega`, `c~x`.

`B_Omega\K_Omega` is connected because `Omega` is native-contact connected.

`Lambda\Omega` is also native-contact connected: it is the connected set `C` plus every other unoccupied component, and every such component must contact `C`; otherwise the full native world would be disconnected. Hence `A_Omega\K_Omega` is connected.

Therefore:

`#pi_0(S^3\K_Omega)=2`.

Alexander duality over `F_2` gives:

`dim H^2(K_Omega;F_2)=dim reduced_H_0(S^3\K_Omega;F_2)=1`.

Since `K_Omega` is a finite cell complex over a field:

`dim H_2(K_Omega;F_2)=1`.

## 3. Each frontier component gives an independent 2-cycle

Let `Gamma_1,...,Gamma_r` be the native 12-contact connected components of `F_Omega`.

For each `Gamma`, define the mod-2 2-chain:

`z_Gamma = sum f_{c,x}`

over all interface faces whose `Omega`-side site `x` lies in `Gamma`.

The chain is nonzero. We prove `boundary z_Gamma=0`.

Every native interface 1-cell is dual to a Delaunay triangle of three pairwise native-contact sites. The task-local exact checker verifies in both FCC and HCP:
- `8` tetrahedra and `6` octahedra through a site;
- `24` native triangular 2-faces through a site;
- every such triangle is a face of exactly `2` local 3-cells;
- HCP layer parity is exchanged by `(i,j,k)->(-i,-j,k+1)`.

Binary coloring of a triangle by `Omega` versus `Lambda\Omega` has either `0` or `2` cut edges.

If the two cut edges have one common `Omega` endpoint, both interface faces belong to the same `z_Gamma`.

If they have two distinct `Omega` endpoints `x,y`, then `x,y` are joined by the third triangle edge, hence are native 12-contact neighbors and lie in the same frontier component `Gamma`.

Thus every interface 1-cell occurs `0` or `2` times in the boundary of each fixed `z_Gamma`, so it cancels over `F_2`:

`boundary z_Gamma=0`.

Because `K_Omega` has no 3-cells, `B_2(K_Omega;F_2)=0`. Therefore every nonzero `z_Gamma` gives a nonzero class in `H_2`.

Distinct frontier components have disjoint interface-face support, so the classes `[z_Gamma]` are linearly independent.

Hence:

`r <= dim H_2(K_Omega;F_2)=1`.

The frontier slice is nonempty, so `r=1`.

Therefore `F(C) intersect Omega` is connected.

## 4. Exact C5 disposition

FCC:

`GLOBAL_OPPOSITE_PAIR_PINCH_IMPOSSIBILITY_PROVED_FCC`.

HCP:

`GLOBAL_OPPOSITE_PAIR_PINCH_IMPOSSIBILITY_PROVED_HCP`.

Combined:

`GLOBAL_OPPOSITE_PAIR_PINCH_IMPOSSIBILITY_PROVED_FCC_AND_HCP`.

The C4 local point-pinch is real, but it cannot be the global separation of two frontier components of one `Omega`: two such components would create two independent nonzero interface 2-cycles, contradicting the rank-one Alexander-duality bound.

Freeze:

`SAME_OMEGA + LOCAL_OCTAHEDRAL_OPPOSITE_PAIR_PINCH -> GLOBAL_NATIVE_FRONTIER_REPAIR`.

## 5. Consequence for R043-C3 and G0

R043-C3 is positively closed in both frozen worlds:

`R043C3_GLOBAL_FRONTIER_CONNECTIVITY_FCC = PROVED`.

`R043C3_GLOBAL_FRONTIER_CONNECTIVITY_HCP = PROVED`.

`R043C3_GLOBAL_FRONTIER_CONNECTIVITY = POSITIVELY_CLOSED_FCC_AND_HCP`.

R043-C2 remains unchanged.

Combining C2 and C3 removes the hidden component-grouping mechanism:

`G0_COMPONENT_GROUPING_AMBIGUITY = REMOVED_FOR_FCC_AND_HCP`.

Under the hierarchy already frozen in the C3 return, the next stationary-G0 obstruction is the single-component rooted successor-extension rigidity problem. This task does not open that successor.

## 6. Exact checker and certificate

Checker:

`scripts/check_r043c5_global_pinch.py`

Certificate:

`research_artifacts/R043C5_global_pinch/RESULTS.json`

The checker independently verifies:
- FCC/HCP local Delaunay incidence counts;
- triangular codimension-two incidence and `0_OR_2` cut parity;
- HCP parity automorphism;
- C4 `14/0`, `62/6`, `4+4` local classification;
- minimal `4,2,1,2,4` repair;
- exact `12,951 / 0` one-shell regression in each world.

It does not replace the global homological proof with bounded computation.

## 7. Final classification

`GLOBAL_OPPOSITE_PAIR_PINCH_IMPOSSIBILITY_PROVED_FCC_AND_HCP`.

`R043C5_OCTAHEDRAL_OPPOSITE_PAIR_GLOBAL_REALIZABILITY_DECIDED = YES`.

`R043C3 = POSITIVELY_CLOSED_FCC_AND_HCP`.

`R043C2 = UNCHANGED`.

`G0_COMPONENT_GROUPING_AMBIGUITY = REMOVED`.

`UNRESOLVED_RESIDUE_WITHIN_C5 = NONE`.

`FOUNDATION_PROMOTION = NOT_AUTHORIZED_BY_THIS_TASK`.
