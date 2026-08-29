# P000 axis-refined mixed-support `BMix_b` V8 — Research Return

Status: `FROZEN RESEARCH RETURN / DRIVER REVIEW REQUIRED`

Researcher-ID: `EM-P000NATFCC8-5D31C7`

Task-ID: `RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE`

Publication-ID: `TP2-0CFF11F0F26D16A513B2`

Execution branch: `research/p000-native-axis-refined-bmix-v8-em-p000natfcc8-5d31c7`

Execution base: `d8e3cda3b322f177f6692f76f22a0d3a43eb4aca`

Hard target:

`P000_AXIS_REFINED_MIXED_SUPPORT_BMix_b_RELATION_AND_JB_NATIVE_SLICE_EXACTLY_CONSTRUCTED_OR_OBSTRUCTED`

Terminal class:

`MINIMAL_DERIVED_BMix_b_CONSISTENT_PARTIAL_LIFT_CONSTRUCTED`

## 1. Result

Gen8 finds no already-authorized current P000 primitive whose composition produces the missing mixed-support Cell relation. The Gen7 block-pure obstruction therefore survives the deeper inventory.

A deeper project foundation does expose a useful relation shape: `PACKET_PATH_FOUNDATION.md` permits optional local six-channel state with ingress/egress data and passage counts `M_x[a,b]`. This is the first inventoried relation schema fine enough to carry six separately addressable local relation payload slots. But PF-10 does not identify those channels with geometry, and the current P000 registry has no authorized bridge from them to native axes `E_1,...,E_6`. Hence it does not itself derive `BMix_b`.

The smallest consistent extension found is a derived axis-handle/contact interface over opaque full P000 Cell identity. It adds no root axiom, no metric, no negative axes and no carrier quotient.

## 2. Primitive inventory

- `definitions/00_CURRENT_NATIVE_FOUNDATION.md`: exact full six-axis Cell typing and native adjacency, but native six-axis address/global metric/native 6D rotation remain research targets. `OMITTED_CELL_COORDINATE!=ZERO_COORDINATE`.
- `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`: exact axis-refined geometry on `J_A={E_1,E_2,E_3}` only; Cell identity, adjacency, 120-degree native right sectors, min-zero sector addresses, no primitive diagonal-shift quotient.
- `definitions/P000_FCC_PRIMARY_COORDINATE_CARRIER_20260829.md`: six carrier line families and four carrier windows, but `FCC_CARRIER_READOUT_IS_NOT_NATIVE_IDENTITY` and the exact native axis bridge remains open.
- `PACKET_PATH_FOUNDATION.md`: packet/adjacency/path plus optional local channel relation `M_x[a,b]`; relation-fine enough, but no P000 axis attachment.
- `admissible_support.py`, `relation_observable_composition.py`, `partial_operation_quotient.py`, `state_pair.py`: operation-safe generic relation calculus only.
- `material_lifted_state.py` and `native_trisector_coupled_closure.py`: unrelated E001/finite-field semantics.
- `p022_barlow_stacking.py`: classical Barlow stacking state, not a hidden P000 mixed handle.

Inventory subfinding:

`NO_DEEPER_MIXED_PRIMITIVE_FOUND`.

The first strictly missing interface is:

`FULL_CELL_IDENTITY + SIX_AXIS_HANDLE_ATTACHMENT + ONE_MIXED_CONTACT_RELATION`.

## 3. Derived axis-refined state

Define a downstream sort `AxisHandledCell(x)`, where `x` is an opaque `FULL_6D_NATIVE_CELL_STATE`. The derived envelope has six total local handles `H_x(E_i)` and opaque payload `P_x(E_i)`.

Native identity is unchanged:

`native_id(AxisHandledCell(x))=x`.

A slice observation exposes only selected handles; every other handle is marked `OMITTED/UNOBSERVED`, never numeric zero. Thus `J_A` is not a six-tuple padded by three zeros, and neither is `J_B`.

Carrier readout remains an observable. Equal readout of distinct native ids does not imply native equality.

## 4. Minimal mixed relation

Add one explicit derived relation instance:

`CONTACT_MATCH_b={{H(E_2),H(E_4)},{H(E_3),H(E_5)}}`.

It carries symmetric passage payload:

- `E_2 -> E_4 : m24`;
- `E_4 -> E_2 : m24`;
- `E_3 -> E_5 : m35`;
- `E_5 -> E_3 : m35`.

This is relation semantics, not equality and not an FCC permutation. Its shape is compatible with PF-10 passage data after — and only after — an axis-handle attachment is supplied.

## 5. Genuine derived `J_B`

The accepted `J_A` cyclic right-sector relation is

`E_1 -> E_2 -> E_3 -> E_1`.

Shared `E_1` plus `CONTACT_MATCH_b` uniquely determines the ordered role transport

`tau_b(E_1)=E_1`,
`tau_b(E_2)=E_4`,
`tau_b(E_3)=E_5`.

Hence

`tau_b(J_A)=J_B={E_1,E_4,E_5}`

and the transported right-sector cycle is

`E_1 -> E_4 -> E_5 -> E_1`.

Define `J_B` Cells as a disjoint tagged copy of the accepted `J_A` Cell set and transport adjacency exactly:

`Adj_B(Tc,Td) <=> Adj_A(c,d)`.

Transport the local address sort as a separately typed chart

`A_E^B={[a_1,a_4,a_5]_B : min(a_1,a_4,a_5)=0}`.

No omitted coordinate is set to zero. No diagonal quotient is introduced. The accepted 120-degree native-right relation and sector-local Pythagorean strength pass to `J_B` by structural transport, not by FCC Euclidean inference.

Because the current native number axis does not pass through Cell centers, the `J_A/J_B` overlap is the common `E_1` coordinate/incidence interface, not a quotient-identification of Cell-center identities.

## 6. Typed partial/groupoid `R~_b`

On handled states carrying the required mixed passage payload define payload transport by

`P'(b(i))=P(i)`

for

`b=(E_2 E_4)(E_3 E_5)`

with `E_1,E_6` fixed. Relation payload is transported by the same typed relabeling. Time is not permuted.

The domain is explicit: if either mixed passage pair is absent, `R~_b` is undefined rather than silently identity.

On its domain,

`R~_b^2=id`.

It transports `J_A` to `J_B`, preserves the finite transported Cell adjacency relation, preserves full Cell native-id tagging, and has an exact inverse/converse.

The forgetful map to the opaque full P000 Cell state is deliberately not used to claim a new base-Cell automorphism. Therefore:

`TYPED_PARTIAL_R~_b_EXISTS_IN_DERIVED_INTERFACE`

but

`FULL_P000_NATIVE_BASE_ROTATION_b_NOT_PROVED`.

## 7. Independence certificate

Use the six-axis relation skeleton containing:

- distinguished shared anchor `E_1`;
- distinguished full-state spectator `E_6`;
- source cycle `E_1->E_2->E_3->E_1`;
- transported target cycle `E_1->E_4->E_5->E_1`;
- contact matching `{{E_2,E_4},{E_3,E_5}}`.

Exhaustive enumeration of all `6!=720` axis permutations gives exactly two automorphisms:

1. `id`;
2. `b=(E_2 E_4)(E_3 E_5)`.

Thus

`Aut(Sigma_b) ~= C2`

and arbitrary `S_6` symmetry is not forced.

The deterministic checker also preserves the Gen7 regression:

`|(S3 x S3) semidirect C2|=72`

and verifies `b` is absent from that old block-pure envelope. The derived automorphism group of order 2 is also kept distinct from the carrier split `S4 x C2` order 48.

## 8. Consistency audit

Passes the following finite/model guards:

- P000 six axes retained; time separate;
- accepted `J_A` unchanged;
- no carrier linear identity promoted to native identity;
- no carrier-readout collision quotient;
- omitted coordinate never becomes zero;
- finite `J_A -> J_B` adjacency transport is exact;
- `R~_b` is nonempty, partial and involutive;
- invalid mixed-payload state is rejected;
- `E_1,E_6` are fixed;
- full Cell identity tag survives the handle transport;
- only `{id,b}` preserves the declared mixed relation skeleton;
- old Gen7 block-pure no-go remains intact.

Checker:

`research_checks/P000_NATIVE_AXIS_REFINED_BMIX_PRIMITIVE_V8_CHECK_20260829.py`

Model certificate:

`research_artifacts/P000_NATIVE_AXIS_REFINED_BMIX_PRIMITIVE_V8/MODEL_CERTIFICATE.json`

Expected output:

```text
PASS P000_NATIVE_AXIS_REFINED_BMIX_PRIMITIVE_V8_CHECK
terminal_class=MINIMAL_DERIVED_BMix_b_CONSISTENT_PARTIAL_LIFT_CONSTRUCTED
derived_axis_skeleton_automorphism_order=2
gen7_block_pure_wreath_order=72
full_P000_native_rotation_promoted=false
native_state_quotient_used=false
```

## 9. Orbit-completion gate and residue

Do not yet construct `R~_a`, `J_C`, or `J_D`. The current success is at an explicit derived relation-groupoid layer, while the canonical full P000 Cell -> six axis-handle attachment remains unproved.

Unresolved residue:

`AXIS_HANDLE_ATTACHMENT_TO_CURRENT_FULL_P000_CELL_NOT_CANONICALLY_DERIVED; FULL_P000_NATIVE_BASE_b_ROTATION_NOT_YET_CONSTRUCTED`.

Smallest next strictly necessary target:

`P000_FULL_CELL_TO_AXIS_HANDLE_CONTACT_REALIZATION_OR_OBSTRUCTION`.

That task should derive an authorized `AXIS_HANDLE(x,E_i,h_i)` relation from current Cell adjacency/incidence, or prove its exact obstruction. If successful, the present `CONTACT_MATCH_b` certificate becomes the candidate bridge from the derived partial lift toward a full native `J_B` route.

## 10. Theorem-strength statement

Within the explicit derived axis-handle/contact model, shared `E_1` plus the mixed contact matching uniquely determines the `J_A -> J_B` role transport; a tagged `J_B` Cell structure transports the accepted local three-axis relations and adjacency; the two charts glue along the common `E_1` coordinate/incidence interface without quotienting Cell centers; and the induced handled-state transport is a partial involution with axis action `(E_2 E_4)(E_3 E_5)`.

The finite relation skeleton has automorphism group exactly `C2={id,b}`. Hence the construction is consistent, operation-sensitive and nontrivial, yet does not force `S_6`, does not identify carrier readout with native identity, and does not prove a full P000 base-Cell rotation.

Therefore the strongest justified terminal class is exactly:

`MINIMAL_DERIVED_BMix_b_CONSISTENT_PARTIAL_LIFT_CONSTRUCTED`.
