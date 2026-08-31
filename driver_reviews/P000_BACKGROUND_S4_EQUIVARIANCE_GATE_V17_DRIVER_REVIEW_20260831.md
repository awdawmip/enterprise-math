# Driver Review — P000 background S4 equivariance gate V17

Status: `ACCEPTED / MULTIPLE INDEPENDENT BACKGROUND LEAKS CLASSIFIED / G17 ATOMIC TRANSPARENCY FRONTIERS ACCEPTED`

Result: `RR-985AEE277DE45AFCC9D8`  
Task: `RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE`  
Publication: `TP2-A7D3C18E5B904F621476`  
Researcher: `EM-P000FCC17-9419D1`  
Driver: `EM-DVR-7C31A8`

## Verdict

`ACCEPTED` at charged-background / atomic-separable-transparency strength.

Accepted terminal class:

`MULTIPLE_INDEPENDENT_BACKGROUND_LEAK_SOURCES_AND_PARETO_GATES_CLASSIFIED`.

The acceptance does not reinstate the rejected Gen16 unconditional `{K4_ADJ}` frontier, does not promote carrier `S4` to the complete native P000 rotation group, and does not claim global optimality over every possible coupled multi-background condition.

## Decisive audit

1. For the frozen structural reduct `M0(P)`, with `G0=Aut_car(M0(P))`, every retained contentful background `B` defines `G_B={u in G0:u preserves B}` and the actual enriched group is `G=intersection_B G_B`. Therefore `im(q)=q0(intersection_B G_B) <= intersection_B q0(G_B)`.
2. Componentwise full projection is not jointly sufficient: the exact `C2 x S4` graph-section witness has two background-preserving subgroups each projecting onto all `S4`, while their intersection projects only to `A4`. Hence `Compat_B=S4` per component is too weak.
3. PF-10 is an independent leak source. `I=O=e1, M=I6` leaves only the order-4 stabilizer of `E1`; full symmetric PF-10 leaves all 24 carrier actions.
4. An independent retained connection is a second independent leak source. With symmetric PF-10, a single marked K4 edge carrying `T_AB=(E1 E6)` leaves only an order-4 edge stabilizer.
5. Per-Cell frames are gauge presentation and frame-induced transport is automatically natural/equivariant; neither requires a charged gate. Nontrivial holonomy is not itself an obstruction; failure of equivariance is the obstruction.
6. The atomic charged templates `PF10_STRUCTURAL_AUT_EQ` and `CONNECTION_STRUCTURAL_AUT_EQ` are non-tautological preservation laws on existing background fields. Each contributes one global-constraint cost and has an exact deletion countermodel.
7. Within the frozen separable-transparency grammar, `G_B=G0` is composable and prevents incompatible-lift intersections. It is accepted only at this declared grammar strength; weaker coupled conditions are not ruled out globally.

## Accepted conditional frontiers

Frame-induced/no independent connection subclass:

`{K4_ADJ, PF10_STRUCTURAL_AUT_EQ}`

with cost `(0,0,0,0,0,0,2,0)`.

Independent-connection subclass:

`{K4_ADJ, PF10_STRUCTURAL_AUT_EQ, CONNECTION_STRUCTURAL_AUT_EQ}`

with cost `(0,0,0,0,0,0,3,0)`.

The corresponding TETRA packages are targeted positive but Pareto-dominated by the K4 packages in the frozen cost coordinates. `UNIQUE_SECTION` is not granted.

## Boundary

Freeze:

`GEN17_MULTIPLE_BACKGROUND_LEAK_SOURCES = ACCEPTED`.

`PF10_STRUCTURAL_AUT_EQ = CHARGED_DOWNSTREAM_CONSTRAINT_NOT_P000_ROOT`.

`CONNECTION_STRUCTURAL_AUT_EQ = CHARGED_DOWNSTREAM_CONSTRAINT_NOT_P000_ROOT_WHEN_INDEPENDENT_CONNECTION_DECLARED`.

`G17_ATOMIC_TRANSPARENCY_GLOBAL_OPTIMALITY = NOT_GRANTED`.

`GEN16_UNCONDITIONAL_K4_FRONTIER = REJECTED`.

`BARE_P000_UNIVERSAL_S4_LIFT_DERIVABLE = FALSE`.

`NO_KERNEL_QUOTIENT`; `TIME_FIXED`; carrier/native identity remains separated.

## Routing consequence

The next P0 stage should keep G15 and the G17 atomic charged grammar immutable and perform the full 90-package Pareto recomputation separately for (i) frame-induced/no independent connection and (ii) independent-connection model subclasses. It must prove universal sufficiency or produce same-package countermodels, compute definitional quotients and frontiers, and retain the Gen17 background-leak deletion certificates. Only after this finite atomic grammar is fully closed should a later stage ask whether a genuinely coupled non-tautological background condition can Pareto-improve the atomic transparency gates.

Final disposition: `ACCEPTED / FOLLOWUP_TASK`.
