# R043-C4 — Native Interface Link-Separator Closure Return

Status: `FROZEN FINAL RETURN / LOCAL_SEPARATOR_FOUND_GLOBAL_REALIZABILITY_OPEN / NOT CANONICAL`
Date: `2026-08-26`
Task-ID: `RS-R043C4-NATIVE-INTERFACE-LINK-SEPARATOR-CLOSURE`
Publication-ID: `TP2-A63015C2EB99D00F2500`
Researcher-ID: `EM-R043C4-375FC7`
Claim-ID: `chatgpt-r043c4-20260826-1435`
Execution branch: `research/r043c4-link-separator-em-r043c4-375fc7`
Execution base: `a2ef31065884c9df0ba15ccc1f3fb7357013a263`

## Verdict

`LOCAL_SEPARATOR_FOUND_GLOBAL_REALIZABILITY_OPEN`.

Hard target:

`R043C4_NATIVE_INTERFACE_LINK_SEPARATOR_EXACTLY_CLOSED_OR_REDUCED_TO_FINITE_NATIVE_OBSTRUCTION = SATISFIED_BY_FINITE_NATIVE_OBSTRUCTION`.

No global FCC/HCP frontier-connectivity theorem and no global counterexample is claimed.

## Exact local theorem

Use the frozen R039 contact models:
- FCC: parity-even `Z^3` with the twelve permutations of `(±1,±1,0)`;
- HCP: exact ABAB integer coordinates with six same-layer and three contacts in each adjacent layer.

A cut contact is an occupied/unoccupied native contact. Two cut contacts are locally interface-adjacent when they lie in one native triangular face. If two such cut contacts have distinct unoccupied endpoints, those endpoints are themselves native-contact adjacent through that triangle. Thus triangle-connected cut contacts give a frontier-site contact lift.

The finite classification is exact:
- tetrahedron: `14` nonconstant two-colorings, `0` bad;
- octahedron: `62` nonconstant two-colorings, exactly `6` bad.

The six bad octahedral colorings are precisely those in which one color class is one of the three opposite vertex pairs, or equivalently the other color is the complementary four vertices. In that case the eight cut contacts split into two components of size `4+4`. The two same-side opposite vertices are not native-contact adjacent and no triangular face contains both.

Freeze:

`TETRAHEDRAL_INTERFACE_LIFT = PROVED`.

`OCTAHEDRAL_INTERFACE_LIFT = PROVED_EXCEPT_OPPOSITE_PAIR_POINT_PINCH`.

`UNIQUE_LOCAL_SEPARATOR = OCTAHEDRAL_OPPOSITE_PAIR_POINT_PINCH`.

This refutes an automatic pointwise local lift, not the global R043-C3 statement.

## FCC witness and control

One exact FCC octahedron is:
- opposite pair `u=(0,0,0)`, `v=(-2,0,0)`;
- equator `(-1,-1,0), (-1,0,-1), (-1,0,1), (-1,1,0)`.

The equator is a connected four-cycle; every equatorial site contacts both `u,v`; `u,v` do not contact each other.

With only the equator occupied, the local pinch is globally repaired by the frontier path

`(0,0,0) -> (0,-1,-1) -> (-1,-2,-1) -> (-2,-1,-1) -> (-2,0,0)`,

with occupied-neighbor counts `4,2,1,2,4`.

A targeted one-shell pressure fixes this equator-4 and tests every extension obtained by occupying at most four of its original 24 other frontier sites:
`1+24+276+2024+10626 = 12,951` connected extensions.
Frontier disconnects between the opposite pair: `0`.

## HCP witness and control

One exact HCP octahedron is:
- opposite pair `u=(0,0,0)`, `v=(-1,-1,-1)`;
- equator `(-1,0,-1), (-1,0,0), (0,-1,-1), (0,-1,0)`.

The same local separator occurs. With only the equator occupied, the external frontier repair is

`(0,0,0) -> (1,-1,0) -> (1,-2,0) -> (0,-2,-1) -> (-1,-1,-1)`,

again with occupied-neighbor counts `4,2,1,2,4`.

The identical targeted one-shell pressure tests `12,951` connected extensions and finds `0` frontier disconnects.

These one-shell checks are obstruction-specific pressure, not a generic animal census and not a proof of global impossibility.

## Consequences

R043-C3 remains `OPEN`. Its local bridge must be narrowed to:

> every tetrahedral interface passage and every non-opposite-pair octahedral passage lifts to native frontier contact; only the octahedral opposite-pair point pinch remains.

R043-C2 component factorization is unchanged. No harmful same-G0 collision is established.

The weakest remaining obstruction is:

`R043C4-O1 = GLOBAL REALIZABILITY OF OCTAHEDRAL OPPOSITE-PAIR PINCH`.

A genuine counterexample must construct finite connected occupied `C` and one connected unoccupied component `Omega` such that opposite-pair frontier sheets remain in the same `Omega`, every external frontier repair is blocked, yet a deeper unoccupied path still connects them. The minimal local realization and all tested one-shell extensions fail to do so.

## Certificates

- `scripts/check_r043c4_native_interface_link_separator.py`
- `research_artifacts/R043C4_link_separator/one_shell_pressure.py`
- `research_artifacts/R043C4_link_separator/RESULTS.json`

Primary classification:

`LOCAL_SEPARATOR_FOUND_GLOBAL_REALIZABILITY_OPEN`.

No Foundation promotion and no broader R043 successor is opened by this return.
