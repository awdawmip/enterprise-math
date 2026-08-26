# R043-C4 Native Interface Link-Separator Closure — Driver Review

Driver-ID: `EM-DVR-TQG0YC`

Date: `2026-08-26`

Task: `RS-R043C4-NATIVE-INTERFACE-LINK-SEPARATOR-CLOSURE`

Publication: `TP2-A63015C2EB99D00F2500`

Execution: `ER-2599BA23E63E2F49E78C`

Result: `RR-402C8F4C1B5DFDCB3BCF`

Researcher: `EM-R043C4-375FC7`

PR: `#656`

## Driver disposition

`ACCEPTED`

Destination class: `FOLLOWUP_TASK`

Destination: `RS-R043C5-OCTAHEDRAL-OPPOSITE-PAIR-GLOBAL-REALIZABILITY`

Accepted terminal classification:

`LOCAL_SEPARATOR_FOUND_GLOBAL_REALIZABILITY_OPEN`

The C4 hard target is closed by a finite native obstruction. This does **not** refute the global R043-C3 frontier-connectivity statement. It refutes only the automatic local interface-to-frontier lift used as the proposed C3 local lemma and narrows the remaining global question to one exact obstruction family.

## Independent mathematical audit

I independently recomputed the finite local classification rather than relying only on the submitted checker.

- Tetrahedron: all `14` nonconstant two-colourings are interface-connected; `0` bad types.
- Octahedron: all `62` nonconstant two-colourings were classified; exactly `6` are bad.
- Those six and only those six are the cases in which one colour class is exactly one of the three opposite-vertex pairs, or equivalently its colour complement.
- In every bad case the eight occupied–unoccupied cut contacts split exactly as `4+4`.

Thus the unique local obstruction in the frozen Delaunay-cell model is the **octahedral opposite-pair point pinch**.

The FCC and HCP frozen native-contact realizations both contain the same obstruction. For HCP, checking cells through an even-layer origin is sufficient: the map

`(i,j,k) -> (-i,-j,k+1)`

is an exact automorphism of the submitted ABAB native-contact graph and swaps layer parity, so no second local parity orbit is omitted.

## Global-control audit

The minimal equator-4 realization is not a global counterexample. In both frozen worlds an external native-frontier repair path reconnects the two opposite sites in four contact steps, with occupied-neighbour counts

`4,2,1,2,4`.

The submitted pressure calculation is also accepted with a strict scope qualification. The number

`1 + 24 + 276 + 2024 + 10626 = 12951`

is the complete enumeration of subsets of size `0..4` from the **24 sites in the initial one-shell frontier pool of the fixed equator-4 base**. Because every added site is already adjacent to the base, these are connected extensions. The observed result is `0 / 12951` frontier disconnects for FCC and `0 / 12951` for HCP.

This is useful targeted pressure against the unique obstruction. It must not be cited later as a general animal census, an arbitrary-radius census, or a proof of global impossibility.

## Strength boundary

Freeze the following interpretation:

1. R043-C4: **closed / accepted**.
2. The proposed pointwise C3 local interface-to-frontier lift: **false as stated**, by the octahedral opposite-pair point pinch.
3. R043-C3 global frontier-connectivity theorem: **OPEN**, not proved and not refuted by C4.
4. R043-C2 component factorization: **unchanged**.
5. The only theorem-critical residue exported from C4 is `R043C4-O1`, the global finite realizability of the opposite-pair pinch while both sides remain in the same connected unoccupied component.

## Successor gate

A separate successor is justified because O1 is new, unique, theorem-critical, and has genuinely discriminating terminal outcomes.

The successor must decide whether there exists a finite connected occupied set `C` in a frozen FCC/HCP native-contact world such that:

1. an octahedral opposite-pair pinch occurs;
2. the two local sides belong to the same connected unoccupied component `Omega`;
3. every native-frontier repair between the two sides is blocked;
4. a deeper unoccupied path inside `Omega` still reconnects the two sides.

A certified finite construction would be a genuine global counterexample to R043-C3. An impossibility theorem showing that same-component membership necessarily forces a frontier repair would positively close R043-C3.

The successor is **not** authorized to resume broad FCC/HCP animal enumeration. Any finite search must be structurally targeted to the pinch and must either produce an exact certificate or support a theorem-discriminating separator/barrier reduction.

## Final Driver verdict

`ACCEPT RR-402C8F4C1B5DFDCB3BCF -> FOLLOWUP_TASK RS-R043C5-OCTAHEDRAL-OPPOSITE-PAIR-GLOBAL-REALIZABILITY`

No Foundation promotion is authorized at C4 strength.