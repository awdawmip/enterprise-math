# R059D — SIX-DIMENSION / 12-DIRECTION ALTERNATING-SIGN CLOSURE

Date: 2026-08-16
Driver: EM-DVR-9GP3M7 / CONTROL_PLANE
Status: DRIVER-VERIFIED COMBINATORIAL NOTE

## User definition being verified

- Enterprise plane: 3 axes / 6 directed directions.
- Adjacent 60-degree directions alternate sign.
- Enterprise solid-world carrier: 6 axes / 12 directed directions.
- The 6 axes restrict to 4 Enterprise planes, each containing 3 axes / 6 directions.
- Choose any one directed axis as `+u`; propagate sign by the rule `one 60-degree adjacency step flips sign`.

## Auxiliary indexing

Use four auxiliary labels `1,2,3,4` only to index the four 3-axis subplanes. The six actual axes are the unordered pairs

`12,13,14,23,24,34`.

The twelve directed directions are `ij` with `i != j`, with `ji` opposite to `ij`.

The four 3-axis subplanes are

- `P123={12,13,23}`;
- `P124={12,14,24}`;
- `P134={13,14,34}`;
- `P234={23,24,34}`.

## Global sign assignment

Fix `12` as positive. Define

- positive: `12,13,14,23,24,34`;
- negative: `21,31,41,32,42,43`.

Equivalently `sigma(ij)=+` iff `i<j`, and `sigma(ji)=-sigma(ij)`.

## 60-degree cyclic orders in the four planes

For `i<j<k`, use the local 60-degree order

`ij -> ki -> jk -> ji -> ik -> kj -> ij`.

Hence:

- `P123`: `12(+),31(-),23(+),21(-),13(+),32(-)`;
- `P124`: `12(+),41(-),24(+),21(-),14(+),42(-)`;
- `P134`: `13(+),41(-),34(+),31(-),14(+),43(-)`;
- `P234`: `23(+),42(-),34(+),32(-),24(+),43(-)`.

Every subplane therefore has exact `+,-,+,-,+,-` alternation.

## Closure

Every 60-degree adjacency edge joins opposite signs. Therefore the global 12-direction adjacency graph is bipartite.

The four plane cycles together connect all twelve directions. Hence once one directed axis is assigned `+`, every other direction is forced. The only other global assignment is simultaneous sign reversal.

Shared directions have the same sign in every subplane in which they occur. Therefore all four 3-axis subplanes inherit one compatible alternating-sign convention.

Equivalent loop statement: every closed walk made of 60-degree adjacency steps has even length, so sign returns to itself after any closed propagation loop.

## Verified disposition

`SIX_DIMENSION_12_DIRECTION_ALTERNATING_SIGN_SYSTEM_CLOSES_EXACTLY`

Scope: combinatorial closure of the declared 6-axis / 12-direction / 4-subplane incidence and 60-degree sign-flip rule. This note does not by itself assert an external physical-world dimensionality theorem.
