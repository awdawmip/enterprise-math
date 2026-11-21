# CFD address transport: exact 2×3 Neumann pressure-block witness (2026-11-21)

Task: RS-COORD-CFD-OPERATOR-TRANSPORT-20260916. Author: EM-X6-C7A253. Status: NOT_REVIEWED / finite exact model; not a CFD speedup or a general X6 codec theorem.

## Fixed input and prior evidence
The registered `three_region_slice_v1` maps the fixed signed integer plane into a lossless nonnegative six-field address subset. Source pin: `awdawmip/enterprise-math@d2984d1a0c5c8221ee103084dd3da68dd039dfaa:coordinate_address_contract.json` and `research_notes/CELL_SLICE_LEAN_VALIDATION_20260913_A8D47F21.md`. The existing Lean result covers encoding/decoding and native steps on that slice; it does not already prove this explicit finite pressure-operator comparison.

Choose the 2-by-3 unit Cartesian cell grid, ordered in the raw chart as
`v=[(0,0),(1,0),(2,0),(0,1),(1,1),(2,1)]`.
Keep seven actual undirected face adjacencies, oriented from lower raw-list index to higher:
`e=[(0,1),(0,3),(1,2),(1,4),(2,5),(3,4),(4,5)]`.
Cell-centered scalar pressure is a signed field, not an address coordinate. All boundary faces are impermeable, giving the standard unweighted finite-volume graph/Neumann pressure Laplacian. Let the incidence matrix D have -1 at each edge tail, +1 at its head. Then A=DᵀD.

## Exact native operator
```
A =
[ 2 -1  0 -1  0  0]
[-1  3 -1  0 -1  0]
[ 0 -1  2  0  0 -1]
[-1  0  0  2 -1  0]
[ 0 -1  0 -1  3 -1]
[ 0  0 -1  0 -1  2]
```
Its exact eigenvalues are `0,1,2,3,3,5`; rank 5. `A·1=0`, preserving the Neumann gauge. The gauge-fixed example `p=(0,1,2,-2,-1,0)` has zero sum, `f=A p=(1,2,3,-3,-2,-1)`, and energy `pᵀ A p=16`.

For the registered three-region codec, the six raw vertices become
```
(0,0) ↦ (0,1,1,0,0,0)
(1,0) ↦ (1,0,1,0,0,0)
(2,0) ↦ (2,0,1,0,0,0)
(0,1) ↦ (0,2,1,0,0,0)
(1,1) ↦ (1,1,0,0,0,0)
(2,1) ↦ (2,1,0,0,0,0)
```
All are legal, distinct addresses in this slice, including the former raw zero cell. Lexicographic address order corresponds to old indices `[0,3,1,4,2,5]`. Define P by `(Pz)_j=z_{order[j]}`. The transported matrix is `Aaddr=P A Pᵀ`, exactly:
```
Aaddr =
[ 2 -1 -1  0  0  0]
[-1  2  0 -1  0  0]
[-1  0  3 -1 -1  0]
[ 0 -1 -1  3  0 -1]
[ 0  0 -1  0  2 -1]
[ 0  0  0 -1 -1  2]
```
`Pp=(0,-2,1,-1,2,0)`, `Pf=(1,-3,2,-2,3,-1)`, and `Aaddr(Pp)=Pf` exactly. `P1=1`, `rank(Aaddr)=5`, the spectrum and energy 16 are preserved. Face orientation is an independent edge record: `Daddr=D Pᵀ`, retaining seven distinct face identities. Thus `DaddrᵀDaddr=Aaddr`. Signed flux and pressure values remain signed; no address field is subtracted as a physical vector.

## Decision and limitations
This is an exact small *representation-invariance* pressure witness, not evidence of numerical speedup or of a 3D/AMR operator migration. It closes a baseline check on cell, face and DOF transport with Neumann gauge and flux identity for the declared 2×3 grid. The hard target still requires pinning an existing CFD host's real mesh/operator, carrying boundary/AMR/rounding and timing its full implementation; no new pressure solver, native CFD execution, general six-axis codec, independent review or P000 promotion is claimed.
