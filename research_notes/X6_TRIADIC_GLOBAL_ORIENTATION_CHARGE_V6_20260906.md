# X6 triadic rotation V6: global six-axis orientation torsor and conserved parity charge

Status: `FREE_RESEARCH / EXACT DERIVATION / NOT_FOUNDATION`
Date: `2026-09-06`
Task: `RS-X6-NATIVE-ROTATION-DYNAMICS`
Depends on:
- V4 index-two frame parity;
- V5 static underdetermination;
- current concrete path/event and triadic/time/internal-state layers.

## 1. Orientation as the exact quotient object

Let `A` be the six positive native-axis labels. An ordering/frame of `A` is a bijection from a six-slot reference set to `A`.

Define two orderings to have the same **global six-axis orientation** iff they differ by an even permutation.

Thus the orientation set is

`Ori_6 := S6/A6 ~= C2`.

It has exactly two elements and no canonical preferred element from the current static P000 substrate alone.

This is the exact quotient already detected algebraically as the positive-axis part of

`B6/R_triad`.

Sign flips in `(C2)^6` do not affect this orientation label because the quotient records only positive-axis permutation parity.

## 2. Triadic frame moves preserve Ori_6

Every elementary triadic frame generator `Q_S` has an underlying positive-axis 3-cycle, hence even permutation parity.

Therefore every `Q_S` preserves the current orientation class.

Any finite composition of triadic generators also preserves it. Equivalently, the triadic-generated frame graph has exactly two connected components inside the full signed frame skeleton, labeled by `Ori_6`.

The component stabilizer is

`R_triad=(C2)^6 semidirect A6`.

Thus `Ori_6` is a conserved two-sector label for the pure triadic frame dynamics.

## 3. The conservation law survives path/internal/time refinements

The parity character

`par:B6 -> C2`

is a group homomorphism.

For a concrete native rotation event whose frame update is `g`, define its orientation increment as

`delta_omega=par(g)`.

Then serial event composition satisfies

`delta_omega(E2 o E1)=delta_omega(E2)+delta_omega(E1) mod 2`.

All current triadic `Q_S` events have `delta_omega=0`.

Changing INNER/OUTER path branch, retaining Path-formal history, adding triadic internal phase, or refining the event-time description does not alter the frame parity unless the frame update itself changes.

Hence the orientation charge is independent of the current shortest-path branch law and of the concrete BRC path lift.

## 4. Odd frame events are precisely sector-changing events

A frame event with odd positive-axis permutation has

`delta_omega=1`

and swaps the two `Ori_6` sectors.

If a history contains several admitted odd frame events, the net orientation change is the parity of their count:

`omega_final-omega_initial = number_of_odd_frame_events mod 2`.

Thus an odd frame event is not just “another generator”. It is exactly an event that crosses the two triadic orientation sectors.

## 5. Dependency-time compatibility

Suppose several certified-independent frame events occur in one dependency antichain. Their serialization may be quotiented by the native event-trace rule.

Because addition in `C2` is commutative, the total orientation increment is independent of serialization order:

`sum par(g_e) mod 2`.

Therefore the orientation charge descends safely from serialized event words to the dependency-trace/partial-order time carrier whenever the individual frame labels themselves remain in scope.

This gives one exact global event invariant compatible with the current native-time architecture.

## 6. Minimality of the repair bit

Suppose a future observer must distinguish whether a frame history lies in the same triadic orientation sector as its initial frame.

Discarding the `Ori_6` label identifies one even and one odd frame class. A future parity query separates them. Hence one bit is necessary.

One bit is also sufficient because `S6/A6` has exactly two elements.

Therefore `Ori_6` is the minimal repair coordinate for full-frame parity information.

This is a global six-axis frame-orientation bit. It is **not**:

- a seventh spatial axis;
- the local FCC/Viète STAR chirality sheet;
- the all-20 local `S3` chart-slot holonomy;
- a Path-formal branch bit;
- a time/precision bit.

V4 proves these distinctions.

## 7. Two possible physical laws now have exact formulations

The static Foundation does not choose between the following.

### Orientation-preserving native rotation law

Postulate/derive that every primitive physical frame-rotation event has

`delta_omega=0`.

Then the complete physical frame group is contained in `R_triad`. If the already-derived triadic generators are all physically admitted, they generate all of `R_triad`, so the physical frame group is exactly `R_triad`.

### Orientation-changing events admitted

Admit at least one event with `delta_omega=1` and close the frame law under the current triadic group and S6-covariant relabeling. Then the generated frame group is all `B6`.

The difference between these theories is one exact C2 event-charge law.

Neither is promoted here.

## 8. Relation to local chirality

A local three-axis STAR chart can reverse its cyclic chirality under an even global six-axis permutation. Therefore local sweep chirality is not the restriction of `Ori_6` parity.

A model may simultaneously carry:

- global `Ori_6` sector;
- local STAR chirality sheet;
- local triadic C6 phase;
- concrete path provenance.

Their updates and safe quotients must be checked separately.

## 9. Current rotation frontier

The full static/dynamical frame question is now reduced to one explicit conserved-charge gate:

`DO_PHYSICAL_PRIMITIVE_ROTATION_EVENTS_PRESERVE_Ori_6?`

Everything below that question is closed at current research strength:

- exact two-sector orientation torsor;
- exact triadic conservation law;
- exact sector flip by odd frame events;
- exact event-composition and dependency-time parity law;
- one-bit minimal repair coordinate.

Resolving the final physical gate requires a new dynamical principle, empirical/external calibration, or direct Foundation definition. More static group enumeration cannot decide it by V5.

No Foundation promotion or identification with classical spatial orientation/spin is made.
