# Driver Review — P000 background S4 equivariance gate V17

Status: `ACCEPTED / CHARGED BACKGROUND TRANSPARENCY CLASSIFIED / NONTRIVIAL EQUIVARIANT MODULI OPEN`

Result: `RR-985AEE277DE45AFCC9D8`  
Task: `RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE`  
Publication: `TP2-A7D3C18E5B904F621476`  
Researcher: `EM-P000FCC17-9419D1`  
Driver: `EM-DVR-7C31A8`

## Verdict

`ACCEPTED` at charged-downstream-background-equivariance strength.

Accepted terminal class:

`MULTIPLE_INDEPENDENT_BACKGROUND_LEAK_SOURCES_AND_PARETO_GATES_CLASSIFIED`.

This does not retroactively accept Gen16's unconditional `{K4_ADJ}` frontier and does not promote the complete native P000 rotation group to `S4`.

## Decisive audit

1. For the structural carrier-compatible group `G0` and retained background components `B`, the actual enriched group is `G=intersection_B G_B`; therefore `im(q)=q0(intersection_B G_B) <= intersection_B q0(G_B)`.
2. Componentwise full readout compatibility is not jointly sufficient. The exact `C2 x S4` graph-section witness has two subgroups each projecting onto `S4` while their intersection projects only to `A4`.
3. PF-10 is a genuine independent symmetry-leak source: `I=O=e1, M=I6` reduces the six-edge carrier action to `Stab(E1)` of order 4.
4. An independently retained connection is a second leak source even with PF-10 fully symmetric: a unique marked K4 edge with nonidentity transport leaves compatibility order 4.
5. Frames are gauge presentation, frame-induced transport is automatically natural, and retained transported star/gluing data at the already accepted scope need no extra charged gate.
6. The composable condition is structural transparency `G_B=G0`, not merely `Compat_B=S4`. This avoids incompatible kernel/lift choices across independent backgrounds.
7. The atomic charged grammar is well-typed and non-tautological: `PF10_STRUCTURAL_AUT_EQ` and, only for independently stored connections, `CONNECTION_STRUCTURAL_AUT_EQ`; each costs one global-constraint unit. Synthetic conjunction packing is forbidden.
8. Under those gates, the K4 positive theorem is conditional and exact: frame-induced/no-independent-connection frontier `{K4_ADJ, PF10_STRUCTURAL_AUT_EQ}`; independent-connection frontier adds `CONNECTION_STRUCTURAL_AUT_EQ`. P4, PF-10-e1, and marked-edge-connection deletion witnesses make each condition essential at the declared separable grammar strength.

## Boundary

Freeze:

`GEN17_BACKGROUND_EQUIVARIANCE_GATES = ACCEPTED`.

`PF10_STRUCTURAL_AUT_EQ_NOT_DERIVED_FROM_PRIOR_ACCEPTED_STRUCTURE = TRUE`.

`INDEPENDENT_CONNECTION_STRUCTURAL_AUT_EQ_NOT_DERIVED_FROM_PRIOR_ACCEPTED_STRUCTURE = TRUE`.

`FRAME_INDUCED_CONNECTION_NEEDS_NO_CHARGED_GATE = TRUE`.

`COMPONENTWISE_COMPAT_S4_DOES_NOT_IMPLY_JOINT_LIFT = TRUE`.

`GEN16_UNCONDITIONAL_K4_FRONTIER_REMAINS_REJECTED = TRUE`.

`UNIQUE_SECTION_NOT_GRANTED = TRUE`.

No P000 mutation, kernel quotient, carrier/native identity collapse, or time rotation is authorized.

## Method harvest

Reusable method: separate a structural automorphism group from independently stored content, classify each content family by its symmetry stabilizer, use intersection/projection rather than independent image tests, and charge only the content families whose transparency is not derivable. For connection data, distinguish equivariance from flatness and treat source-target fibers as groupoid/coset objects rather than subgroups.

## Routing consequence

The next P0 stage should test whether these accepted transparency gates support rich, non-degenerate native content. It should give a finite/local presentation of the PF-10 and connection gates, classify the moduli of nonconstant `S4`-equivariant PF-10 profiles and independent connections on the K4/tetra structural model, and either construct a nonidentity/nonflat but fully equivariant connection witness or prove the exact obstruction. A positive theorem that only survives for constant PF-10 and identity connection is not sufficient closure of the parent rotation objective.

Final disposition: `ACCEPTED / FOLLOWUP_TASK`.
