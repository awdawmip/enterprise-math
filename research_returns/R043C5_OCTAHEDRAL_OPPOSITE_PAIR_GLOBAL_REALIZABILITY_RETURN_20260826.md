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

Hard target:

`R043C5_OCTAHEDRAL_OPPOSITE_PAIR_GLOBAL_REALIZABILITY_DECIDED = SATISFIED`.

The unique R043-C4 local obstruction—the octahedral opposite-pair point pinch—cannot be promoted to a finite global R043-C3 counterexample in either frozen FCC or frozen HCP.

In fact the proof is stronger than the C5 target:

> **Global frontier-component theorem.**  Let `C` be any nonempty finite connected occupied set in the frozen FCC or HCP native 12-contact graph, and let `Omega` be any connected component of the unoccupied graph. Then
>
> `F_Omega := F(C) intersect Omega`
>
> is connected under the original native 12-contact relation.

Therefore the opposite-pair pinch is necessarily repaired somewhere else on the same native interface whenever its two local sides belong to the same `Omega`.

Consequently R043-C3 closes positively in both FCC and HCP.

No Foundation promotion is authorized by this task.

---

## 1. Frozen predecessor boundary

R043-C4 is consumed exactly at its Driver-accepted strength:

`LOCAL_SEPARATOR_FOUND_GLOBAL_REALIZABILITY_OPEN`.

The following are frozen:

- tetrahedron: `14` nonconstant two-colourings, `0` bad;
- octahedron: `62` nonconstant two-colourings, exactly `6` bad;
- the six bad colourings are exactly an opposite-vertex pair or its colour complement;
- each bad octahedral cut splits `4+4` at the local interface;
- the same local obstruction occurs in FCC and HCP;
- the minimal equator-4 realization repairs externally with occupied-neighbour profile `4,2,1,2,4`;
- the C4 fixed one-shell pressure checks `12,951` connected extensions per lattice and finds `0` opposite-pair frontier disconnects.

The last item remains regression evidence only. It is **not** used to infer global impossibility.

C5 does not repeat or enlarge the animal census.

---

## 2. Exact native interface object

Fix one frozen world `Lambda` (FCC or HCP), one finite connected occupied set `C`, and one connected unoccupied component `Omega` of `Lambda\\C`.

Use the same native close-packed cell/star thickening already admitted by the R043-C3 reduction. Native 12-contact means that the two corresponding site cells share a native 2-face.

After one-point compactification, the ambient close-packed cellulation is a cellulation of `S^3`.

Define the two site-cell unions:

- `B_Omega`: the union of native cells whose sites lie in `Omega`;
- `A_Omega`: the union of all remaining native cells, i.e. sites in `Lambda\\Omega`.

Include the point at infinity on the side containing the infinite site component.

Define the finite common interface

`K_Omega := A_Omega intersect B_Omega`.

Its 2-cells are exactly the native faces

`f_{c,x}`

with

`c in C`, `x in Omega`, and `c ~ x`

under native 12-contact. Lower-dimensional common incidences are retained as cells of `K_Omega`.

There are no 3-cells in `K_Omega`.

The visible frontier slice is exactly

`F_Omega = {x in Omega : exists c in C with c ~ x}`.

Thus every interface 2-face has one unique `Omega`-side frontier site.

---

## 3. Why `S^3 \\ K_Omega` has exactly two connected components

`B_Omega \\ K_Omega` is connected because `Omega` is connected in the native contact graph: a native site path gives a chain of native cells crossing shared 2-faces that are not part of the `Omega`/non-`Omega` interface.

Now consider the site set

`Lambda \\ Omega`.

It consists of:

- the connected occupied set `C`;
- every other connected component of the unoccupied graph.

Every other unoccupied component must have at least one native contact to `C`. Otherwise it has no contact to `Omega` (or it would be the same unoccupied component) and no contact to any other complement component, contradicting connectedness of the full FCC/HCP native graph.

Hence `Lambda\\Omega` is native-contact connected.

Therefore `A_Omega\\K_Omega` is also connected.

The interface `K_Omega` separates these two open sides and there is no third side. Thus

`# pi_0(S^3 \\ K_Omega) = 2`.

Since `K_Omega` is a finite cell subcomplex, it is compact and locally contractible, so Alexander duality over `F_2` applies:

`reduced H_0(S^3 \\ K_Omega; F_2) ~= reduced H^2(K_Omega; F_2)`.

The left side has dimension `1`. Therefore

`dim H^2(K_Omega; F_2) = 1`.

Because `K_Omega` is a finite cell complex and coefficients are a field,

`dim H_2(K_Omega; F_2) = dim H^2(K_Omega; F_2) = 1`.

This is the global rank bound.

---

## 4. Every native frontier component creates an independent 2-cycle

Let

`Gamma_1, ..., Gamma_r`

be the connected components of the induced native 12-contact graph on `F_Omega`.

For each component `Gamma`, define the mod-2 interface face chain

`z_Gamma := sum f_{c,x}`

over all interface faces with `x in Gamma`.

The chain is nonzero because every frontier component contains a site adjacent to `C`.

We prove

`boundary z_Gamma = 0`.

### 4.1 Exact codimension-two native incidence

In both frozen FCC and HCP cellulations, every native interface 1-cell is dual to a Delaunay triangle of three pairwise native-contact sites.

The task-local exact checker independently verifies the local incidence surface:

- `8` tetrahedra through a site;
- `6` octahedra through a site;
- `24` native triangle faces through a site;
- every such triangle is a face of exactly `2` local 3-cells;
- HCP even/odd layers are related by the exact native automorphism
  `(i,j,k) -> (-i,-j,k+1)`.

Thus it is enough to inspect one binary colouring of a native triangle by

`Omega` versus `Lambda\\Omega`.

A binary triangle has either:

- `0` cut edges, or
- exactly `2` cut edges.

Those cut edges are dual to exactly the interface 2-faces incident to the corresponding interface 1-cell.

If the two cut edges have the same `Omega` endpoint, both interface faces belong to the same `z_Gamma`.

If they have two distinct `Omega` endpoints `x,y`, then `x,y` are joined by the third edge of the Delaunay triangle. Therefore

`x ~ y`

under native 12-contact. Since both lie in `F_Omega`, they belong to the same frontier component `Gamma`.

Hence, at every interface 1-cell, the number of incident faces belonging to any fixed `z_Gamma` is even—either `0` or `2`.

Over `F_2` they cancel.

Therefore

`boundary z_Gamma = 0`.

### 4.2 Nonzero and independent homology classes

`K_Omega` has dimension `2`, so its cellular chain complex has no 3-cell boundary group:

`B_2(K_Omega; F_2) = 0`.

Thus every nonzero 2-cycle `z_Gamma` represents a nonzero class in

`H_2(K_Omega; F_2)`.

Distinct frontier components have disjoint sets of `Omega`-side interface faces. Therefore the chains

`z_{Gamma_1}, ..., z_{Gamma_r}`

have disjoint 2-cell support and are linearly independent.

Consequently

`r <= dim H_2(K_Omega; F_2)`.

Using the global rank bound from Section 3,

`r <= 1`.

The frontier slice is nonempty because every connected component of `Lambda\\C` contacts the nonempty finite set `C` in the connected native world.

Hence

`r = 1`.

Therefore

`F(C) intersect Omega`

is native 12-contact connected.

This proves the theorem.

---

## 5. Exact disposition of the C4 opposite-pair pinch

The C4 octahedral opposite-pair colouring remains a genuine **local** failure of the pointwise interface-to-frontier lift.

At its dual octahedral vertex the local interface contains two sheet germs meeting only at that point, while the two opposite unoccupied sites are not native 12-contact neighbors.

But if those two sheet germs belonged to different global frontier components `Gamma_1,Gamma_2` of the same `Omega`, Section 4 would produce two independent nonzero classes

`[z_{Gamma_1}], [z_{Gamma_2}] in H_2(K_Omega;F_2)`.

That would force

`dim H_2(K_Omega;F_2) >= 2`,

contradicting Alexander duality, which forces the dimension to equal `1` because the two sides of the interface are connected.

Therefore every local opposite-pair pinch whose two sides remain in the same `Omega` must reconnect elsewhere through native frontier 12-contact.

Equivalently:

`SAME_OMEGA + LOCAL_OCTAHEDRAL_OPPOSITE_PAIR_PINCH -> GLOBAL_NATIVE_FRONTIER_REPAIR`.

So the C5 witness requested by the counterexample route does not exist in FCC or HCP.

---

## 6. FCC disposition

`GLOBAL_OPPOSITE_PAIR_PINCH_IMPOSSIBILITY_PROVED_FCC`.

More strongly:

`FOR_ALL_FINITE_CONNECTED_C_FOR_ALL_UNOCCUPIED_COMPONENTS_OMEGA_F_OMEGA_CONNECTED_FCC`.

No finite FCC occupied-set certificate can satisfy the four C5 counterexample conditions.

The local incidence assumptions used by the proof are checked exactly from the frozen FCC contact model; no Euclidean threshold or floating point is used.

---

## 7. HCP disposition

`GLOBAL_OPPOSITE_PAIR_PINCH_IMPOSSIBILITY_PROVED_HCP`.

More strongly:

`FOR_ALL_FINITE_CONNECTED_C_FOR_ALL_UNOCCUPIED_COMPONENTS_OMEGA_F_OMEGA_CONNECTED_HCP`.

No finite HCP occupied-set certificate can satisfy the four C5 counterexample conditions.

The exact phase-swap automorphism

`(i,j,k) -> (-i,-j,k+1)`

interchanges HCP layer parity, so the local triangular codimension-two incidence check covers both layer orbits.

---

## 8. C4 regression audit

The task-local checker replays only the theorem-relevant frozen C4 controls:

- tetrahedron nonconstant colourings: `14`, bad `0`;
- octahedron nonconstant colourings: `62`, bad `6`;
- every bad octahedral cut has component sizes `4+4`;
- minimal FCC repair profile: `4,2,1,2,4`;
- minimal HCP repair profile: `4,2,1,2,4`;
- fixed one-shell pool: `24` sites;
- subsets of size `0..4`: `12,951` connected extensions per world;
- frontier disconnects: `0` in FCC and `0` in HCP.

The checker reports PASS.

These computations are regression guards only. The global theorem is proved by the interface-cycle/Alexander-duality argument, not by bounded search.

---

## 9. Consequence for R043-C3

R043-C3 asked whether, for every finite connected occupied `C` and every connected unoccupied component `Omega`, the induced native contact graph on

`F(C) intersect Omega`

is connected.

C5 proves exactly that statement in both frozen worlds.

Therefore freeze:

`R043C3_GLOBAL_FRONTIER_CONNECTIVITY_FCC = PROVED`.

`R043C3_GLOBAL_FRONTIER_CONNECTIVITY_HCP = PROVED`.

`R043C3_GLOBAL_FRONTIER_CONNECTIVITY = POSITIVELY_CLOSED_FCC_AND_HCP`.

The local C4 point-pinch remains an important warning: topological interface connectivity does **not** imply a pointwise local frontier-site lift. The correct global proof uses independent interface 2-cycles and the rank-one duality constraint.

---

## 10. Consequence for R043-C2 and the G0 grouping ambiguity

R043-C2 is unchanged: addition-only future dynamics factorizes over true connected unoccupied components.

With C3 now proved, the connected components visible in current `G0` identify those true unoccupied components. The remaining hidden-state mechanism based on grouping multiple disconnected frontier pieces inside one true `Omega` is eliminated.

Freeze:

`G0_COMPONENT_GROUPING_AMBIGUITY = REMOVED_FOR_FCC_AND_HCP`.

Under the hierarchy already frozen in the C3 return, the next unresolved stationary-G0 obstruction is therefore the **single-component rooted successor-extension rigidity** problem.

This task does not open that successor.

---

## 11. Exact checker / durable certificate

Task-local checker:

`scripts/check_r043c5_global_pinch.py`

Durable result certificate:

`research_artifacts/R043C5_global_pinch/RESULTS.json`

The checker is intentionally finite and local. It certifies the exact FCC/HCP codimension-two incidence hypotheses and the frozen C4 regressions. It does not pretend to replace the global homological proof with computation.

Primary certificate facts:

- FCC: `8` tetrahedra, `6` octahedra, `24` native triangles through origin, every triangle in exactly `2` local 3-cells;
- HCP: same counts, with parity orbit checked by exact phase swap;
- every binary native triangle contributes `0` or `2` interface faces;
- two distinct `Omega` endpoints in that case are native adjacent;
- all C4 local and one-shell regression guards pass.

---

## 12. Weakest supported statement

The strongest supported statement is already global and exact:

> In the frozen FCC and HCP native close-packed 12-contact cellulations, for every nonempty finite connected occupied set `C` and every connected component `Omega` of the unoccupied graph, the visible frontier slice `F(C) intersect Omega` is connected under native 12-contact. Hence the unique octahedral opposite-pair local pinch of R043-C4 is globally unrealizable as a same-component frontier disconnection: whenever both local sides remain in the same `Omega`, a native frontier repair exists elsewhere.

There is no smaller unresolved separator remainder inside C5.

## 13. Final classification

`GLOBAL_OPPOSITE_PAIR_PINCH_IMPOSSIBILITY_PROVED_FCC_AND_HCP`.

`R043C5_OCTAHEDRAL_OPPOSITE_PAIR_GLOBAL_REALIZABILITY_DECIDED = YES`.

`R043C3 = POSITIVELY_CLOSED_FCC_AND_HCP`.

`R043C2 = UNCHANGED`.

`G0_COMPONENT_GROUPING_AMBIGUITY = REMOVED`.

`FOUNDATION_PROMOTION = NOT_AUTHORIZED_BY_THIS_TASK`.
