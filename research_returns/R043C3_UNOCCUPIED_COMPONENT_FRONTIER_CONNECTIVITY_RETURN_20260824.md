# R043-C3 — Unoccupied-Component Frontier Connectivity Return

Status: `DONE / RETURNED / REDUCED_TO_LOCAL_LINK_SEPARATOR_LEMMA / NOT CANONICAL`

Researcher-ID: `EM-R043C3-9F21C6`  
Task: `RS-R043C3-UNOCCUPIED-COMPONENT-FRONTIER-CONNECTIVITY`  
Taskbook: `research_tasks/R043C3_UNOCCUPIED_COMPONENT_FRONTIER_CONNECTIVITY_20260824.md`  
Driver base: `main@19c71b41e96fd0e2186d3a074fb453591cbc52e3`

Primary verdict:

`REDUCED_TO_LOCAL_LINK_SEPARATOR_LEMMA`

No global frontier-connectivity theorem is claimed yet, and no native counterexample was found.

## 1. Exact question retained

For finite connected occupied `C`, let `Omega` be one connected component of the unoccupied graph `Lambda\C` and

`F_Omega = F(C) intersect Omega`.

The target remains:

> Is the induced native contact graph on `F_Omega` connected for every `C` and every `Omega` in frozen FCC and HCP?

C2 proves that a positive answer would make connected components of current `G0` coincide exactly with dynamically independent unoccupied components.

## 2. Exact finite pressure on the first nontrivial thick-void family

A counterexample requires a connected unoccupied region with at least one currently non-frontier interior cell. The minimal systematic pressure family used here is

`U = N[D] = D union all native neighbors of D`

for a finite connected core `D`.

Every `d in D` is interior to `U`. The current void frontier is

`Q(U) = {u in U : some native neighbor of u lies outside U}`.

The test asks whether the induced native graph on `Q(U)` is disconnected.

### FCC exact exhaustive core census

All frozen-symmetry connected FCC cores through `|D|<=8` were enumerated exactly:

| |D| | core classes | disconnected Q(U) |
|---:|---:|---:|
| 1 | 1 | 0 |
| 2 | 1 | 0 |
| 3 | 4 | 0 |
| 4 | 20 | 0 |
| 5 | 131 | 0 |
| 6 | 1,211 | 0 |
| 7 | 12,734 | 0 |
| 8 | 144,158 | 0 |

Total tested: `158,260` connected cores. Counterexamples: `0`.

### HCP exact exhaustive core census

All frozen-symmetry connected HCP cores through `|D|<=7` were enumerated exactly:

| |D| | core classes | disconnected Q(U) |
|---:|---:|---:|
| 1 | 1 | 0 |
| 2 | 2 | 0 |
| 3 | 9 | 0 |
| 4 | 57 | 0 |
| 5 | 460 | 0 |
| 6 | 4,641 | 0 |
| 7 | 50,353 | 0 |

Total tested: `55,523` connected cores. Counterexamples: `0`.

These are exact exhaustive statements only for the family `U=N[D]` at the stated core cutoffs. They are not a proof of the global C3 theorem. An attempted HCP `|D|=8` extension exceeded the bounded execution window and is not counted.

## 3. Why the obvious generic graph proof is insufficient

For an arbitrary graph, a connected complement component can have a disconnected vertex boundary. Therefore C3 cannot be discharged from graph connectivity alone.

The close-packed local geometry matters. In FCC/HCP each site has a highly connected native link, and finite connected occupied/unoccupied sets admit a natural three-dimensional close-packed cell thickening. The bounded `N[D]` census gives evidence that the local link structure is preventing the simplest separator patterns, but enumeration cannot establish the arbitrary-size result.

## 4. Topological reduction route

There is a clean proof architecture, but one discrete bridge lemma remains open.

Fix `Omega`. Thicken lattice sites into their native close-packed cells (equivalently use a sufficiently small compatible cell/star thickening) and form two regions:

- the thickened chosen unoccupied component `B(Omega)`;
- the thickening of its complement, including occupied `C`, all other unoccupied components, and the point at infinity, `A(Omega)`.

The intended construction has:

1. `A(Omega)` connected because `C` is connected and all other complementary pieces attach through their interface with `C`;
2. `B(Omega)` connected because `Omega` is graph-connected;
3. after one-point compactification, `A(Omega) union B(Omega)` covers the ambient 3-sphere.

For connected sufficiently regular neighborhoods covering `S^3`, the reduced Mayer-Vietoris `H_0` segment and `H_1(S^3)=0` force the common topological interface to be connected.

This does **not yet** prove C3, because C3 asks for connectivity in the induced **frontier-site native contact graph**, not merely connectivity of a continuous face/edge/vertex interface.

## 5. Exact remaining local lemma

### R043C3-L1 — native interface-to-frontier connectivity

For the frozen FCC and HCP close-packed cell structures, prove that if one connected occupied-side thickening and one connected unoccupied-side thickening share a connected interface, then the set of unoccupied lattice sites whose native cells meet that interface is connected under the original 12-contact relation.

Equivalently, rule out a local interface passage that transfers connectedness only through lower-dimensional cell incidences while jumping between frontier sites that are not linked by a chain of frontier-frontier native contacts.

This is now a finite local incidence / link-separator question. It should be attacked separately in FCC and HCP using the actual native link and cell incidence tables, not by generic digital-topology analogy.

A proof of R043C3-L1 plus a fully explicit thickening construction closes C3 positively. A counterexample to R043C3-L1 gives the exact local pattern from which to build a native C3 counterexample.

## 6. Alternative direct discrete route

A second valid route avoids topological thickening entirely:

1. assume a minimal `C,Omega` whose `F_Omega` is disconnected;
2. take a shortest unoccupied path in `Omega` joining two frontier components;
3. use minimality to constrain every interior path vertex to have no occupied neighbor;
4. classify the resulting native link separator around the first/last departure from the frontier;
5. prove the separator impossible from the FCC/HCP link incidence, or freeze it as a local obstruction.

This discrete route reaches the same R043C3-L1-type object: a local link pattern must isolate visible frontier pieces while preserving a deeper unoccupied connection.

## 7. Consequence for the G0 mother problem

C3 has not yet eliminated component-grouping ambiguity globally. It has reduced it from an arbitrary-size surface problem to one native local-interface lemma.

Current exact hierarchy:

```text
C1: raw K_partial -> G0 injectivity false
    but shielded cavity relocation future-safe

C2: addition-only dynamics factorizes over true unoccupied components
    relative placement of distinct components future-safe

C3: whether G0 connected components identify those true components
    reduced to native interface/link separator lemma

then: single-component rooted successor-extension rigidity
```

A positive C3-L1 would make the last line the only remaining stationary-G0 obstruction.

## 8. Regression / evidence matrix

| surface | test | disposition |
|---|---|---|
| FCC | `U=N[D]`, all connected cores `|D|<=8` | 158,260 / 158,260 boundary-connected |
| HCP | `U=N[D]`, all connected cores `|D|<=7` | 55,523 / 55,523 boundary-connected |
| HCP | `|D|=8` extension | NOT COMPLETED / no inference |
| C1 singleton cavity | one frontier component per one finite void component | PASS |
| C2 component factorization | distinct true void components never merge under additions | PROVED |
| global C3 | every `F_Omega` connected | OPEN |

## 9. Weakest supported statement

> No frontier-connectivity counterexample exists in the exact thick-void family `U=N[D]` for all frozen-symmetry FCC connected cores through size 8 or HCP connected cores through size 7. Structurally, the global C3 question can be reduced to a close-packed native interface/link separator lemma that converts connected topological interface incidence into connected frontier-site 12-contact incidence. That local lemma is not yet proved or refuted.

No Foundation or canonical theorem promotion is requested.
