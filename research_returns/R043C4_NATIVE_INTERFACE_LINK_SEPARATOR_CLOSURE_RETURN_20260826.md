# R043-C4 — Native Interface Link-Separator Closure Return

Status: `FROZEN FINAL RETURN / LOCAL_SEPARATOR_FOUND_GLOBAL_REALIZABILITY_OPEN / NOT CANONICAL`
Date: `2026-08-26`
Task-ID: `RS-R043C4-NATIVE-INTERFACE-LINK-SEPARATOR-CLOSURE`
Publication-ID: `TP2-A63015C2EB99D00F2500`
Researcher-ID: `EM-R043C4-375FC7`
Claim-ID: `chatgpt-r043c4-20260826-1435`
Execution branch: `research/r043c4-link-separator-em-r043c4-375fc7`
Execution base: `a2ef31065884c9df0ba15ccc1f3fb7357013a263`

## 0. Primary verdict

`LOCAL_SEPARATOR_FOUND_GLOBAL_REALIZABILITY_OPEN`.

Hard target:

`R043C4_NATIVE_INTERFACE_LINK_SEPARATOR_EXACTLY_CLOSED_OR_REDUCED_TO_FINITE_NATIVE_OBSTRUCTION = SATISFIED_BY_FINITE_NATIVE_OBSTRUCTION`.

The exact local interface-to-frontier lift is **not** universally valid at a single close-packed lower-dimensional incidence. In both FCC and HCP there is one and only one local obstruction type: an octahedral hole whose two opposite vertices lie on one side of the interface while the four equatorial vertices lie on the other side (or the color-complement version).

At that octahedral incidence the eight cross-color native contacts split into two four-edge interface families. The two corresponding same-side opposite sites are not 12-contact adjacent, and no triangular face of the octahedron contains both. Thus a connected interface may pass through the dual Voronoi vertex while the two local frontier-site labels fail to connect through native contact **at that incidence**.

This does **not** yet refute the global R043-C3 frontier-connectivity statement. The finite realizability gate remains open: a global counterexample would have to realize one or more such octahedral pinches inside a finite connected occupied set while keeping the two local sheets in the same connected unoccupied component and simultaneously suppressing every external frontier repair path. The smallest exact realization does not do this; it repairs outside the octahedron in four native contacts in both FCC and HCP.

No Foundation promotion is requested.

---

## 1. Frozen sources

Current-policy task publication:

- `research_tasks/R043C4_NATIVE_INTERFACE_LINK_SEPARATOR_CLOSURE_REISSUE_20260826.md@blob:4d0e5c5853b4d39a53fec714027e434d29cc59c1`;
- immutable publication `TP2-A63015C2EB99D00F2500`.

Frozen predecessors:

- R043-C3 return `research_returns/R043C3_UNOCCUPIED_COMPONENT_FRONTIER_CONNECTIVITY_RETURN_20260824.md@49877b834c4f15e7f30cb54f03ba5f106dba0342`;
- R043-C2 result/owner head `a2aaaece1fcdea23f799b73728bb628b7d72bfa5`;
- R039 exact metric-free close-packed reference `research_artifacts/R039_native_rough_surface/reference.py@research/R039-native-rough-surface-EM-R039-9F3C27`, blob `4b86693c9bc7eb79563df859d45ecb88a9065e1b`.

R039 supplies exactly:

- FCC: parity-even `Z^3` with the twelve contact steps obtained by permutations of `(±1,±1,0)`;
- HCP: exact ABAB integer coordinates with six same-layer contacts and three contacts in each adjacent layer.

No Euclidean distance threshold, floating point, or continuum metric was used in the finite certificate.

---

## 2. Interface-face encoding

Use the standard close-packed local dual incidence already implicit in the C3 thickening route.

A native occupied/unoccupied contact is dual to one local interface 2-face. If two such cut contacts lie in one native triangular face, their interface faces meet along the corresponding dual edge.

Label every cut contact by its unoccupied endpoint. For two cut contacts in one triangle:

- if they have the same unoccupied endpoint, the frontier label is unchanged;
- if they have distinct unoccupied endpoints, those endpoints themselves are joined by the third edge of the native triangle and are therefore 12-contact adjacent.

Hence triangle-connectedness of all cut contacts incident to a local Delaunay cell is sufficient for a native frontier-site lift through that local incidence.

The theorem-critical finite question is therefore:

> For every nonconstant two-coloring of the vertices of a tetrahedral or octahedral close-packed hole, are all cross-color edges connected under the relation “two cut edges lie in a common triangular face”? 

This is an exact finite combinatorial problem.

---

## 3. Tetrahedral disposition — positive

A tetrahedron has four vertices, six edges and four triangular faces.

All `2^4-2 = 14` nonconstant two-colorings were enumerated exactly.

Result:

`TETRA_BAD_INTERFACE_COLORINGS = 0 / 14`.

Equivalently, for every split `1+3`, `2+2` or `3+1`, the cut-edge set is connected under shared-triangle adjacency.

Thus every tetrahedral lower-dimensional interface passage lifts locally to a chain of frontier-site native contacts.

Freeze:

`TETRAHEDRAL_INTERFACE_TO_FRONTIER_LIFT = PROVED_EXACTLY`.

---

## 4. Octahedral disposition — unique exact separator

Model the octahedron by three opposite pairs

`{0,1}`, `{2,3}`, `{4,5}`.

Its contact graph is `K_{2,2,2}`: twelve edges, with the three opposite pairs omitted. Its eight triangular faces contain one vertex from each opposite pair.

All `2^6-2 = 62` nonconstant two-colorings were enumerated exactly.

Result:

- `56 / 62` colorings: cut edges triangle-connected;
- `6 / 62` colorings: cut edges split into two components of size `4+4`.

The six bad colorings are **exactly**:

> one color class is one entire opposite pair, or equivalently the other color class is the complementary four vertices.

There are three opposite pairs and two choices of which color owns the pair, hence exactly six bad colorings.

For the bad type, if the same-side opposite vertices are `u,v`, then every one of the four equatorial vertices is adjacent to both `u` and `v`, but `u` and `v` are not adjacent. The eight cut contacts are

`{u-e_i : i=1..4} union {v-e_i : i=1..4}`.

No native triangular face contains both `u` and `v`; therefore no shared-triangle sequence joins the two four-edge families at that octahedral incidence.

Freeze:

`OCTAHEDRAL_OPPOSITE_PAIR_POINT_PINCH = UNIQUE_LOCAL_SEPARATOR_TYPE`.

`POINTWISE_INTERFACE_TO_FRONTIER_LIFT_WITHOUT_OCTAHEDRAL_CASE_SPLIT = REFUTED`.

This is a refutation of the **local automatic lift step**, not a global R043-C3 counterexample.

---

## 5. FCC exact native witness

The frozen R039 FCC contact graph contains six octahedral cells through the origin. One exact cell is:

- opposite unoccupied candidates:
  - `u=(0,0,0)`;
  - `v=(-2,0,0)`;
- connected equatorial four-cycle:
  - `(-1,-1,0)`;
  - `(-1,0,-1)`;
  - `(-1,0,1)`;
  - `(-1,1,0)`.

Every equatorial site contacts both `u` and `v`; `u` and `v` do not contact each other. The equatorial induced degree sequence is exactly `[2,2,2,2]`, so the occupied local side is itself connected.

Thus the octahedral separator is natively realizable as a local FCC occupancy pattern.

### Minimal global-control check

Take **only** the equatorial four sites as the occupied set `C`.

Then `u,v` are both frontier sites and belong to the same outer unoccupied component. Nevertheless they are still frontier-connected by the exact four-contact path

`(0,0,0)`
`-> (0,-1,-1)`
`-> (-1,-2,-1)`
`-> (-2,-1,-1)`
`-> (-2,0,0)`.

The occupied-neighbor counts along that frontier path are exactly

`4,2,1,2,4`.

Therefore the local point pinch does not by itself produce a global FCC frontier counterexample.

Targeted one-shell pressure: starting from this equator-4 base, the initial outer frontier excluding `u,v` has exactly `24` sites. Every connected extension obtained by additionally occupying at most four of those original 24 sites was tested:

`1 + 24 + 276 + 2024 + 10626 = 12,951` exact extensions.

Frontier disconnects between `u,v`: `0 / 12,951`.

This is obstruction-specific pressure only, not a general animal census and not a proof of global impossibility.

FCC disposition:

`LOCAL_OCTAHEDRAL_SEPARATOR_EXISTS / GLOBAL_FINITE_REALIZABILITY_OPEN`.

---

## 6. HCP exact native witness

The frozen R039 ABAB contact graph also contains six octahedral cells through the phase-0 origin (and the same local counts occur in the other AB phase).

One exact cell is:

- opposite unoccupied candidates:
  - `u=(0,0,0)`;
  - `v=(-1,-1,-1)`;
- connected equatorial four-cycle:
  - `(-1,0,-1)`;
  - `(-1,0,0)`;
  - `(0,-1,-1)`;
  - `(0,-1,0)`.

Again every equatorial site contacts both opposite sites, the opposite pair is not a native contact, and the equator has induced degree sequence `[2,2,2,2]`.

### Minimal global-control check

With only the equator occupied, the opposite pair is frontier-connected outside the octahedron by

`(0,0,0)`
`-> (1,-1,0)`
`-> (1,-2,0)`
`-> (0,-2,-1)`
`-> (-1,-1,-1)`.

Occupied-neighbor counts are again

`4,2,1,2,4`.

Targeted one-shell pressure is identical in size:

- original external pool: `24`;
- connected extensions with at most four additional sites: `12,951`;
- frontier disconnects: `0`.

HCP disposition:

`LOCAL_OCTAHEDRAL_SEPARATOR_EXISTS / GLOBAL_FINITE_REALIZABILITY_OPEN`.

---

## 7. Exact finite certificate

Primary checker:

`scripts/check_r043c4_native_interface_link_separator.py`.

It independently freezes:

- native FCC/HCP contact generators;
- `8` tetrahedral and `6` octahedral local hole cells through the origin in each world;
- all tetra/octa two-colorings;
- exact `14/0` tetra and `62/6` octa coloring counts;
- exact opposite-pair characterization of every bad octa coloring;
- explicit FCC/HCP local witnesses;
- exact four-step external frontier repair controls.

Targeted realizability pressure:

`research_artifacts/R043C4_link_separator/one_shell_pressure.py`.

Machine-readable certificate:

`research_artifacts/R043C4_link_separator/RESULTS.json`.

No result in this task depends on enlarging the C3 `U=N[D]` census.

---

## 8. Consequence for R043-C3

The C3 proposed proof architecture had two layers:

1. prove the occupied/unoccupied topological interface connected;
2. lift interface connectivity to connectivity of frontier sites under native 12-contact.

C4 shows that step 2 is **not automatic at every local incidence**. Tetrahedral incidences and 56/62 octahedral colorings are safe, but an octahedral opposite-pair pinch can transfer topological interface connectivity through a dual Voronoi vertex without a local frontier-frontier contact lift.

Therefore the original generic C3-L1 statement must be narrowed:

> all interface passages lift except the unique octahedral opposite-pair pinch; a global proof must additionally show that such pinches are globally repairable, globally paired in a way that reconnects frontier labels, or incompatible with a finite connected same-`Omega` counterexample.

C3 remains `OPEN`.

However it is no longer an unconstrained FCC/HCP incidence problem. Any global counterexample or positive proof must pass through this one exact obstruction family.

---

## 9. Consequence for R043-C2 / G0 component grouping

R043-C2 remains unchanged:

`DISTINCT_TRUE_UNOCCUPIED_COMPONENTS_FACTORIZE_AND_NEVER_MERGE_UNDER_ADDITIONS`.

C4 does not create a harmful same-G0 collision.

The only still-possible component-grouping ambiguity is now much narrower:

> one connected unoccupied component would have to contain two or more visible frontier pieces whose only interface-level communication is mediated by globally realized octahedral opposite-pair pinches, while all ordinary triangle/tetrahedron/good-octahedron interface transitions fail to furnish a frontier contact path.

If future work proves every finite occurrence of that pinch has an external frontier repair whenever the opposite sites remain in the same unoccupied component, then C3 closes positively and the component-grouping ambiguity disappears entirely.

If a finite connected `C,Omega` suppressing every such repair is constructed, it is the first valid C3 global counterexample and should then be routed back to C2 for successor-future comparison.

---

## 10. Why no stronger negative claim is frozen

A local separator is not sufficient to refute global frontier connectivity. The taskbook explicitly requires native global realizability for that upgrade.

The minimal equator-4 realization is a negative control against overclaiming: it contains the exact bad octahedral coloring, yet its frontier is connected outside the octahedron in both FCC and HCP.

The targeted 12,951-extension pressure in each world likewise finds no immediate local-shell global lift.

Therefore the strongest exact current classification is not

`LOCAL_SEPARATOR_LIFTED_TO_GLOBAL_FRONTIER_COUNTEREXAMPLE`,

but exactly

`LOCAL_SEPARATOR_FOUND_GLOBAL_REALIZABILITY_OPEN`.

---

## 11. Weakest remaining obstruction

One problem remains:

`R043C4-O1 — GLOBAL REALIZABILITY OF OCTAHEDRAL OPPOSITE-PAIR PINCH`.

Decide whether there exists a finite connected occupied set `C` and one connected unoccupied component `Omega` such that:

1. the interface contains at least one octahedral opposite-pair pinch of the exact certified type;
2. the opposite local frontier sheets belong to the same `Omega`;
3. every external native frontier repair between those sheets is blocked;
4. nevertheless `Omega` retains a deeper unoccupied path connecting them.

This is no longer a generic surface census problem. It is a single typed realizability/repair question centered on the exact octahedral pinch certificate.

No broader R043 successor is opened by this return.

---

## 12. Final freeze

Primary classification:

`LOCAL_SEPARATOR_FOUND_GLOBAL_REALIZABILITY_OPEN`.

Exact local conclusions:

`TETRAHEDRAL_INTERFACE_LIFT = PROVED`.

`OCTAHEDRAL_INTERFACE_LIFT = PROVED_EXCEPT_OPPOSITE_PAIR_POINT_PINCH`.

`UNIQUE_LOCAL_SEPARATOR = OCTAHEDRAL_OPPOSITE_PAIR_POINT_PINCH`.

Global conclusions:

`FCC_GLOBAL_FRONTIER_CONNECTIVITY = OPEN`.

`HCP_GLOBAL_FRONTIER_CONNECTIVITY = OPEN`.

`GLOBAL_COUNTEREXAMPLE = NOT_ESTABLISHED`.

`R043C2_COMPONENT_FACTORIZATION = UNCHANGED`.

Hard target is satisfied at the permitted finite-obstruction terminal class.
