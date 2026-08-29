# P000 First Native Layer Polyhedron Classification — Driver Review

Status: `ACCEPTED / HARD_TARGET_CLOSED_AT_TYPED_IDEAL_BARLOW_CARRIER_STRENGTH / RESULT_ONLY`

Driver-ID: `EM-DVR-P8H4Q2`
Driver authority: `DA-FADB5B44A384B8C3F3F5`
Source authority comment: `5458931979`

Task: `RS-P000-FIRST-SHELL-POLYHEDRON-CLASSIFICATION`
Publication: `TP2-8BAE9A40F7D298D7AD01`
Result: `RR-73C4AC1CB16F08C64FC4`
Execution: `ER-8EFD143E5946F2E46BB2`
Researcher: `EM-P000SHELL-44B349`
Source PR: `#820`

## 1. Verdict

`ACCEPTED`.

The hard target is closed at the exact strength claimed by the frozen return:

`P000_FIRST_NATIVE_LAYER_POLYHEDRON_AND_READOUTS_EXACTLY_CLASSIFIED`

only under the declared typed ideal equal-sphere Barlow carrier. This review does not identify any classical carrier polyhedron with native P000 ontology.

## 2. Result-envelope audit

The current taskbook blob is exactly

`be8dbfeb55b594fc11b35fd15d354f37ea1d1100`.

At the Result-declared `owner_head=60750b2466bd3bad68bd6165be999a87f178fb4e`, every manifest Git blob resolves exactly:

- return: `ebdba3056bbd7cd7e0391577b7426b9f0733d2e8`;
- exact certificate: `2b6f1dd99e4b628877efb006003b353089c8509b`;
- checker: `e58b287ae65eaadd8a805b5ebac84535b2cb5211`;
- execution record: `5bf7eafec4dc641e2a0534c7719894a589614ff3`.

No provenance drift analogous to the rejected RR-D082 envelope was found.

## 3. Independent mathematical audit

The submitted coordinate map

`Phi(X,Y,Z)=(X/2,Y/(2 sqrt(3)),Z sqrt(6)/3)`

gives exactly

`12 ||Phi(p)-Phi(q)||^2 = 3 dX^2 + dY^2 + 8 dZ^2`.

I independently recomputed the finite hull incidences from the frozen point sets.

For the cubic/FCC local environment:

- `V=12, E=24, F=14`;
- face multiset `8 triangles + 6 squares`;
- edge-face signature `(TT,TS,SS)=(0,24,0)`;
- the shell is centrally symmetric.

For the hexagonal/HCP local environment:

- `V=12, E=24, F=14`;
- the same face multiset `8 triangles + 6 squares`;
- edge-face signature `(TT,TS,SS)=(3,18,3)`;
- the shell is not centrally symmetric.

Hence equal f-vectors and equal face-size multisets do not imply the same coordination polyhedron. The cubic type is the cuboctahedron; the hexagonal type is the triangular orthobicupola / anticuboctahedron.

The Barlow local classification is exact at this carrier scope: for a middle layer, the two adjacent layer labels are either equal (`ABA`-like, hexagonal type) or the two distinct alternatives (`ABC`-like, cubic type). Thus there are exactly two local kissing-shell hull types.

The polar/Dirichlet calculation also reproduces:

- FCC: `V=14,E=24,F=12`, all 12 faces rhombi;
- HCP: `V=14,E=24,F=12`, 6 rhombi + 6 isosceles trapezoids.

The exact checker reproduces these counts and metrics with integer/rational arithmetic. Independent literature cross-checks agree that close-packed sphere environments have cuboctahedral/anticuboctahedral coordination and the corresponding rhombic/trapezo-rhombic Dirichlet domains.

## 4. P000 typing boundary

The strongest accepted native statement is:

`DEFAULT_FIRST_LAYER = L1_NATIVE = NATIVE_ADJACENCY_DISTANCE_1`.

`KISS1`, `HULL1`, and `VOR` remain carrier/readout objects requiring an explicit bridge.

The accepted carrier-level universal statements are limited to the declared ideal Barlow carrier:

- `KISS1` has 12 contacts;
- `HULL1` has 14 faces but two local polyhedral types;
- `VOR` has 12 faces but two local Dirichlet types.

The HCP shell is not centrally symmetric. Therefore the inference

`12 carrier contacts -> 6 opposite pairs -> 6 native P000 axes`

is rejected. The six native P000 axes remain fixed by P000, not derived from this carrier.

No Working Truth, Foundation admission, canonical promotion, or classical-geometry override is granted by this review.

## 5. Routing consequence

The classification task itself is terminal and accepted. The parent P000 rotation/tomography objective remains open because the exact residue

`CARRIER_TO_NATIVE_ADJACENCY_AND_AXIS_BRIDGE_NOT_YET_DEFINED`

is a real model-interface gap.

A mathematical continuation is therefore justified only as an explicit bridge task: define or obstruct a typed map between `L1_NATIVE` and carrier contacts/direction relations in one declared six-dimensional P000 model, with FCC and HCP retained as mandatory regressions and HCP non-central-symmetry retained as a no-overclaim guard.

Driver disposition:

`ACCEPTED / FOLLOWUP_TASK`.
