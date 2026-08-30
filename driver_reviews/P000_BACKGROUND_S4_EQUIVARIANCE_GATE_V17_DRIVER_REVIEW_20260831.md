# Driver Review — P000 background S4 equivariance gate V17

Status: `ACCEPTED / CHARGED-BACKGROUND-GATE STRENGTH / FOLLOWUP_TASK`

Result: `RR-985AEE277DE45AFCC9D8`  
Publication: `TP2-A7D3C18E5B904F621476`  
Researcher: `EM-P000FCC17-9419D1`  
Driver: `EM-DVR-7C31A8`

## Verdict

`ACCEPTED` at the declared downstream charged-background-grammar strength.

Accepted terminal class:

`MULTIPLE_INDEPENDENT_BACKGROUND_LEAK_SOURCES_AND_PARETO_GATES_CLASSIFIED`.

## Decisive findings

1. For structural reduct group `G0` and retained background families `B`, the actual enriched group is `G=intersection_B G_B`, hence `im(q)=q0(intersection_B G_B) subseteq intersection_B q0(G_B)`.
2. Componentwise full projected compatibility `q0(G_B)=S4` is not jointly sufficient. The exact `C2 x S4` graph-section witness gives two individually surjective preserving subgroups whose intersection projects only to `A4`.
3. PF-10 is an independent contentful symmetry leak. `I=O=e1, M=I6` reduces compatibility to the order-4 edge stabilizer.
4. An independently retained connection is a second independent leak even with fully symmetric PF-10. A single marked K4 edge with nonidentity channel transport again leaves only an order-4 stabilizer.
5. Per-Cell frames and frame-induced transport are gauge/derived; transported star/gluing data at accepted scope need no separate charge.
6. Therefore the composable atomic gates are structural transparency conditions `G_B=G0`, not merely `Compat_B=S4`.

## Accepted conditional frontiers

Frame-induced/no independent connection subclass:

`{K4_ADJ, PF10_STRUCTURAL_AUT_EQ}` with cost `(0,0,0,0,0,0,2,0)`.

Independent-connection-declared subclass:

`{K4_ADJ, PF10_STRUCTURAL_AUT_EQ, CONNECTION_STRUCTURAL_AUT_EQ}` with cost `(0,0,0,0,0,0,3,0)`.

At the returned semantics these force faithful splitting and an `Aut_prim`-fixed section. The corresponding TETRA packages are strictly Pareto-dominated. Each displayed condition has an exact deletion countermodel.

## Boundary

- Gen15 remains immutable.
- Gen16 bare `{K4_ADJ}` frontier remains rejected.
- These charged templates are downstream sufficient conditions, not P000 root axioms.
- `CARRIER_S4 != COMPLETE_NATIVE_P000_ROTATION_GROUP` remains frozen.
- `BARE_P000_UNIVERSAL_S4_LIFT_DERIVABLE=FALSE` remains frozen.
- `UNIQUE_SECTION` is not granted.
- no kernel quotient; time fixed.

## Routing

The next P0 task should stop adding symmetry conditions and test whether the accepted charged gates can be *derived from intrinsic local regularity/transport laws* rather than postulated. It must seek the weakest local-to-global criterion implying `PF10_STRUCTURAL_AUT_EQ` and, when an independent connection exists, `CONNECTION_STRUCTURAL_AUT_EQ`, with exact countermodels separating local orbit regularity, generator equivariance, path consistency, and full structural transparency. If no non-tautological derivation exists in the current language, classify the irreducible information cost of the gates.

Final disposition: `ACCEPTED / FOLLOWUP_TASK`.
