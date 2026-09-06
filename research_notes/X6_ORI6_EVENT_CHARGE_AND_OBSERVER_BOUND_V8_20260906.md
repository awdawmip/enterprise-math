# X6 rotation V8: Ori6 event charge, hidden-observer lower bound and one-coset extension theorem

Status: `FREE_RESEARCH / EXACT GROUP-AND-OBSERVER DERIVATION / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-NATIVE-ROTATION-DYNAMICS`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- `X6_FULL_INTEGRAL_ISOMETRY_AND_ORI6_GATE_V7_20260906.md`;
- current `R_triad=(C2)^6 semidirect A6` frame dynamics;
- all-20 A6 chart/channel integration.
Checker: `experiments/x6_ori6_event_charge_v8_20260906/check_ori6_event_charge.py`.

## 1. Current exact gate

V7 closes the integer-linear norm-preserving frame envelope as

`O_X6(Z)=(C2)^6 semidirect S6`.

Current triadic/channel/chart generators occupy exactly

`R_triad=(C2)^6 semidirect A6`.

Define the project-specific orientation charge

`chi:O_X6(Z)->C2`

by forgetting coordinate sign flips and taking the parity of the underlying positive-axis permutation.

Then

`ker chi=R_triad`.

This is the exact current `Ori_6` charge. It is distinct from ordinary matrix determinant.

## 2. Event-charge composition law

For frame events `g,h`, permutation parity gives

`chi(hg)=chi(h)+chi(g) mod 2`.

Thus along an event word

`g_n ... g_2 g_1`

the total orientation charge is simply

`chi(total)=sum_r chi(g_r) mod 2`.

Every currently derived triadic positive-frame, minimal unsigned-channel and even chart-lift event has charge zero. Therefore every finite serial composition of the current event language also has charge zero.

This is an exact conservation law **for the current admitted generator language**.

It is not yet a P000 statement that every physically possible event must have zero charge.

## 3. All odd integral frame isometries form one extension coset

Because `R_triad` is normal of index two, choose any odd-positive-permutation frame isometry `o`. Then

`O_X6(Z) = R_triad disjoint_union R_triad o`,

and

`R_triad o = o R_triad`.

More strongly,

`R_triad o R_triad = R_triad o`.

So all `Ori_6=1` static frame isometries belong to one left/right/double coset relative to the current triadic group.

Consequently the unresolved algebraic extension is not a family of unrelated missing sectors. Up to pre- and post-composition by already-available charge-zero frame dynamics, **one odd event type is enough to represent the whole missing static coset**.

If one admissible odd event exists, current even dynamics plus that event generates the full 46080-element integral frame group.

## 4. Odd-event parity is the complete charge ledger

Suppose an enlarged event language contains both current charge-zero events and some charge-one events.

Then after any finite event history the final `Ori_6` sector differs from the initial sector iff the number of charge-one events is odd.

Thus the minimal charge observer is one bit:

`ORI6_LEDGER = (# odd-positive-permutation frame events) mod 2`.

This one-bit observer is operation-safe for future questions that ask only the final `Ori_6` sector. It is not sufficient for full frame, path or event-history reconstruction.

Because the charge is additive in `C2`, swapping certified-independent events does not change it. Hence it descends through the dependency-time quotient even when raw serialization order is forgotten.

## 5. Three-axis observers cannot detect Ori6

Consider a local observer that sees an **ordered** list of `k` distinct positive axes and asks how a frame map acts on those visible axes.

The pointwise stabilizer of those `k` visible axes inside `S6` is

`S_{6-k}`

acting on the hidden complement.

If `6-k>=2`, the hidden stabilizer contains both even and odd permutations. In particular one may swap two hidden axes while leaving every visible ordered slot unchanged.

Therefore, for every `k<=4`, there are two global frame maps with identical ordered `k`-axis observation but opposite `Ori_6` charge.

Only when `k>=5` is the hidden complement of size at most one, so the visible ordered action uniquely determines the full positive-axis permutation parity.

Hence:

`MIN_ORDERED_VISIBLE_AXES_TO_DETERMINE_ORI6 = 5`.

This is a sharp observer lower bound.

## 6. Exact 3-axis stabilizer counts

The lower bound specializes cleanly to current chart observers.

### Unoriented selected 3-set

The setwise stabilizer has order

`3! * 3! = 36`.

It contains exactly 18 even and 18 odd permutations.

So a selected 3-axis set cannot determine `Ori_6`.

### Cyclically oriented 3-chart / directed passage

The active 3-cycle can be rotated in three ways and the hidden three axes can be permuted arbitrarily, giving stabilizer order

`3 * 6 = 18`.

Exactly 9 are even and 9 are odd.

So even the 40-state oriented chart/channel-passage observer cannot determine `Ori_6`.

### Fully ordered visible triple

The visible axes are fixed slot-by-slot; the hidden complement still has `S3` freedom, with 3 even and 3 odd elements.

Thus the 120-state fully ordered visible-triple observer is still insufficient.

A simple explicit invisible odd move is a transposition of two hidden complement axes.

## 7. Relation to the 18/9/3 A6 normalization fibers

Earlier A6 carrier normalization found stabilizers/fibers

`18 / 9 / 3`

for an unoriented 3-set, cyclically oriented chart and fully ordered visible triple.

Passing from A6 to the full S6 static frame envelope doubles each stabilizer:

`36 / 18 / 6`.

The extra half is exactly the hidden `Ori_6=1` sector.

So the previously observed 18/9/3 frame ambiguity is the orientation-preserving half of a larger 36/18/6 full-frame ambiguity. A local chart observer cannot know which half it occupies without extra hidden-frame information.

## 8. Spatial Cell paths alone also do not determine the charge

`Ori_6` is a frame-event property, not a function of spatial endpoint alone.

For example an odd transposition of two hidden axes can fix the visible selected chart pointwise. At a chosen pivot Cell it may also leave the pivot coordinate unchanged while changing the global frame sector.

Therefore

`SAME_SPATIAL_CELL + SAME_LOCAL_3AXIS_OBSERVATION`

can coexist with opposite global `Ori_6` frame charge.

A concrete Cell path without the associated frame/internal event label cannot in general reconstruct `Ori_6`.

This is another reason the upper architecture separates state, path provenance and frame-event type.

## 9. Exact current-language no-go

Let `E_current` be the event language generated by the currently derived:

- triadic C6 frame events;
- their sign-kernel corrections;
- minimal unsigned channel circulations under the frame projection;
- orientation-preserving even chart lifts;
- compositions, inverses at the frame level and dependency-trace reorderings of certified-independent events.

Every frame element generated by this language lies in `R_triad` and has

`chi=0`.

Therefore no amount of branch selection, path concatenation, channel projection, chart rerouting or event reordering **within the current frame generator set** can produce an `Ori_6` change.

To cross sectors requires at least one genuinely new charge-one frame event law. It cannot be manufactured solely by choosing a different INNER/OUTER realization of an already-even frame arrow.

This is the exact current-generator superselection theorem.

## 10. Minimal extension classification

Any admissible charge-one event `o` supplies the entire missing static group algebraically:

`<R_triad,o>=O_X6(Z)`.

Different odd choices are related by current even frame operations. Therefore the physical extension problem reduces to one binary question plus event realization:

> is at least one charge-one native event admissible?

If yes, classify one representative's concrete Cell/path/internal/time law; all other odd static frame maps can then be synthesized algebraically with current charge-zero frame operations, though physical path cost and event semantics may differ.

If no, prove the no-go from a stronger physical/event axiom. Current P000 does not yet provide that no-go.

## 11. Verification

The exact checker verifies:

- A6/odd coset sizes `360/360` in S6;
- the one odd left/right/double coset theorem;
- additive `C2` charge under frame composition;
- exact stabilizer counts for ordered `k`-axis observers, `k=0,...,6`;
- sharp visibility threshold `k=5`;
- 18/18 parity split for selected 3-sets;
- 9/9 split for cyclically oriented 3-charts/passages;
- an explicit hidden-axis odd transposition invisible on an ordered three-axis view;
- charge ledger equals odd-event count mod two.

No Foundation promotion or physical admission of an odd event is claimed.
