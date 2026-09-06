# X6 rotation V13: triadic Ori6 phase-reversal involution and unique common-node odd event

Status: `FREE_RESEARCH / EXACT CONDITIONAL EVENT CONSTRUCTION + FINITE CHECK / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-NATIVE-ROTATION-DYNAMICS`, `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- `X6_FULL_INTEGRAL_ISOMETRY_AND_ORI6_GATE_V7_20260906.md`;
- `X6_ORI6_EVENT_CHARGE_AND_OBSERVER_BOUND_V8_20260906.md`;
- `X6_ORI6_PAIR_CONTEXT_SELECTOR_V9_20260906.md`;
- `X6_SIGNED_INTERNAL_Q_GAUGE_CORRECTION_V5_20260906.md`;
- `X6_SIGNED_CYCLE_PHASE_ATLAS_V12_20260906.md`;
- atomic triadic common-node scatter and rotation-path BRC results.
Checker: `experiments/x6_ori6_triadic_phase_reversal_v13_20260906/check_ori6_triadic_phase_reversal.py`.

## 1. The V9 gap

V9 showed that a bare odd pair swap can be selected equivariantly once an unordered axis pair `{i,j}` is supplied, but its two-token shortest-path realization remains ambiguous: both `II` and `OO` have a shared midpoint.

The unresolved physical/event gate was therefore not the static odd frame group. It was the simultaneous need for:

1. an `Ori6=1` frame update;
2. P000 triadic rather than binary participation;
3. a concrete operation-safe Cell-path law;
4. compatibility with the current signed-C6/four-twist internal dynamics.

This note gives one exact construction satisfying all four as a **conditional event semantics**. It does not assert that nature must realize this event.

## 2. Pointed-triad odd involutions

Choose three distinct native axes and distinguish an unordered pair plus a third axis:

`({i,j}; k)`.

For `beta in {+1,-1}` define the signed frame involution

`O^beta_{ij|k}` by

`E_i -> beta E_j`,

`E_j -> beta E_i`,

`E_k -> -E_k`,

and fix the other three axes.

Then:

- the positive-axis permutation is the transposition `(ij)`, so `Ori6(O)=1`;
- `O^2=1`;
- the ordinary signed-permutation determinant is `+1` for both beta values, again showing `Ori6 != determinant`;
- all three selected unit-axis tokens are moved nontrivially by native L1 distance two.

There are

`6 * C(5,2) = 60`

pointed-triad contexts and two beta choices, hence 120 distinct frame involutions.

## 3. Exact classification inside the pointed-triad ansatz

Consider the most general signed involution candidate whose positive-axis permutation swaps `i,j`, fixes the pointed third axis `k`, and is identity on the complement:

`E_i -> a E_j`,

`E_j -> b E_i`,

`E_k -> c E_k`,

with `a,b,c in {+1,-1}`.

Involution requires

`ab=1`,

so `a=b=beta`.

Now impose the synchronous atomic-scatter participation condition used by the current triadic event interface: each of the three selected unit force tokens must execute a nontrivial two-primitive-step shell-to-shell move with an intermediate atomic Cell.

The `k` token has displacement length two iff `c=-1`; for `c=+1` it is fixed and does not participate in the two-tick common-node scatter.

Therefore exactly the two events

`O^+_{ij|k}` and `O^-_{ij|k}`

survive for each pointed triad.

This is a classification within the explicitly declared pointed-triad involution ansatz, not a classification of every conceivable odd native event.

## 4. Triadic BRC path law becomes unique

Take arbitrary input sign sheet

`(s_i,s_j,s_k) in {+1,-1}^3`

and the three force-token shell Cells

`s_i e_i`, `s_j e_j`, `s_k e_k`.

Under `O^beta_{ij|k}`:

- the `i` token moves `s_i e_i -> beta s_i e_j`;
- the `j` token moves `s_j e_j -> beta s_j e_i`;
- the `k` token moves `s_k e_k -> -s_k e_k`.

The first two moves each have exactly two shortest two-step Cell paths:

- INNER through the pivot `0`;
- OUTER through the sum of their endpoints.

The third move is two repeated primitive steps on one signed axis and has a **unique** shortest midpoint, namely the pivot `0`.

Hence the three-way intersection of shortest-midpoint sets is exactly

`{0}`.

So among the joint shortest population there is exactly one common-atomic-node realization:

`INNER_i x INNER_j x UNIQUE_k`.

The checker verifies this on all 120 pointed-triad frame events and all eight input sign sheets: 960 signed triadic event cases.

This repairs the V9 binary `II/OO` ambiguity without violating P000: the repair is supplied by a genuine third participating force token, not by reinterpreting the pair as a primitive two-force balance.

## 5. Four-twist gauge-covariant phase reversal

The current signed internal theory uses the gauge-covariant four-twist C6 generator bundle.

Choose an oriented triad

`S=(i_0,i_1,i_2)`

and a twist

`alpha=(alpha_0,alpha_1,alpha_2)`,

`alpha_r in {+1,-1}`,

`alpha_0 alpha_1 alpha_2=-1`.

Define

`Q_{S,alpha}(E_{i_r})=alpha_r E_{i_{r+1}}`

with indices modulo 3. Then `Q^3=-I_S` and `Q^6=1`.

For each oriented edge `i_r -> i_{r+1}`, let the pointed third axis be `i_{r+2}` and define

`O_r^alpha := O^{alpha_r}_{i_r i_{r+1}|i_{r+2}}`.

Then exactly:

`(O_r^alpha)^2=1`,

`O_r^alpha Q_{S,alpha} O_r^alpha = Q_{S,alpha}^{-1}`.

Thus `O_r^alpha` is a native signed-frame **phase-reversal involution** for the local C6 generator.

### Uniqueness of beta

Within the two common-node pointed-triad involutions on the same edge, the phase-reversal condition determines beta uniquely:

`beta=alpha_r`.

So the combined conditions

`TRIADIC COMMON-NODE PARTICIPATION`

plus

`REVERSE THE DECLARED LOCAL C6 PHASE`

select one and only one frame event on a pointed oriented edge.

## 6. Gauge covariance

Under an independent sign-frame gauge `epsilon_i`, the C6 twist transports by

`alpha'_r = epsilon_{i_r} epsilon_{i_{r+1}} alpha_r`.

Conjugating the odd involution by the same sign gauge gives exactly

`g_epsilon O_r^alpha g_epsilon^-1 = O_r^{alpha'}`.

The third-axis sign remains `-1` because it is conjugated twice by the same `epsilon`.

Hence the phase-reversal event family closes on the existing four-twist bundle. The construction is not tied to the canonical `(-,-,-)` gauge.

There are

`40 oriented triadic passages * 4 twists * 3 pointed edges = 480`

gauge-context triples `(S,alpha,r)`, but only 120 distinct odd signed frame maps. Exact enumeration shows every one of the 120 maps occurs in exactly four such contexts.

## 7. One complete B6 conjugacy class

Every `O^beta_{ij|k}` has signed cycle type

`lambda_+ = (2,1,1,1)`,

`lambda_- = (1)`.

Its B6 centralizer order is

`(2*2) * (2^3 * 3!) * 2 = 384`.

Therefore its full B6 conjugacy-class size is

`46080 / 384 = 120`.

The 120 pointed-triad odd events are pairwise distinct, so they are exactly this entire B6 conjugacy class.

Because the signed cycle type contains an even positive-axis cycle of length two, V12's splitting theorem says the class does not split under current `R_triad` conjugacy. Direct enumeration confirms:

`one R_triad conjugacy orbit = all 120 events`.

Thus a single representative is a normal form for the whole structurally admissible pointed-triad odd-event family under current even frame transport.

The primitive signed-direction orbit partition of such an involution is

`(2,2,2,1,1,1,1,1,1)`:

three signed-direction 2-cycles and six fixed signed directions. It is a localized involution, not a global C12 frame.

## 8. Canonical gauge factorization

For the canonical C6 gauge on one selected triad,

`Q_S(E_i)=-E_j`, `Q_S(E_j)=-E_k`, `Q_S(E_k)=-E_i`,

let

`J_S=Q_S^3=-I_S`.

For pointed pair `{i,j}` with third axis `k`, the canonical phase-reversal event is

`O^-_{ij|k}=J_S P_{ij}`,

where `P_{ij}` is the pure positive-axis transposition from V9.

This explains the repair algebraically:

- `P_{ij}` alone is the odd pair swap with binary `II/OO` midpoint ambiguity;
- multiplying its **frame map** by the already-current triadic half-turn `J_S` flips the third token too;
- the third token's unique pivot midpoint reduces the three-way common-node path law to one branch.

This is a frame factorization. It does **not** mean the direct odd event path is the serial physical execution of a pair swap followed by a separate half-turn event.

## 9. Local dihedral completion

Fix one four-twist local C6 generator `Q=Q_{S,alpha}` and one compatible pointed-edge phase reversal `O=O_r^alpha`.

The exact relations are

`Q^6=1`,

`O^2=1`,

`O Q O = Q^-1`.

Therefore

`<Q,O> ~= D_12`

with group order 12 (the dihedral group of a six-phase cycle).

For the canonical gauge, projection to positive-axis labels gives

`C3` from `Q` and one transposition from `O`, hence the full local

`S3`.

The kernel of this projection inside `D_12` is exactly

`{1,Q^3} ~= C2`.

So there is an exact local sequence

`1 -> C2 -> D_12 -> S3 -> 1`.

This is the three-axis local analogue of the global signed-frame extension

`1 -> (C2)^6 -> B6 -> S6 -> 1`.

No classical mirror/reflection ontology is imported; `phase-reversal involution` is the typed term used here.

### Six odd involutions inside local D12

The six charge-one involutions are `Q^m O`, `m=0,...,5`.

Exactly three of them are the pointed-triad common-node phase reversals described above: they move all three selected unit tokens nontrivially. The other three leave one selected signed phase direction fixed and reduce to the pair-only kind on the shell, so they fail the synchronous three-token participation condition.

Thus the triadic common-node gate selects the three alternate odd involutions of the local dihedral completion.

## 10. Event-time and observer typing

The common-node realization is a two-relation-tick atomic scatter:

`shell triad -> common pivot closure -> transformed shell triad`.

Its raw primitive path layer still contains three labeled force-token paths and must retain BRC provenance when future operations inspect those paths.

`Ori6` is the additive one-bit frame-event charge from V8. This event contributes charge one. A three-axis spatial observer alone cannot infer that charge; the event/frame label remains necessary until an observer-safe quotient is proved.

The odd event does not add a spatial dimension or a new primitive direction. It changes the relational frame and has a concrete triadic Cell-path realization.

## 11. What this does and does not close

Closed as an exact conditional construction:

- a 120-element pointed-triad odd frame family with `Ori6=1`;
- classification of the two common-node involutions per pointed triad;
- unique common-pivot shortest BRC law for all 960 signed token cases;
- gauge-covariant phase-reversal selection on every four-twist C6 edge;
- one full B6/R_triad conjugacy class;
- local dihedral `D_12` completion and `S3` projection.

This materially answers the V7--V9 question **conditionally**: there is no structural incompatibility between an Ori6-changing event and current P000 triadic/Cell/path/internal/time rules; one explicit event semantics satisfies them all.

Still not claimed:

- P000/Foundation admission that this event physically exists;
- uniqueness among all possible Ori6-changing event semantics outside the pointed-triad/two-tick ansatz;
- a calibration deciding when such an event occurs;
- a probability/rate/energy assigned to the event;
- external novelty.

The next gate is therefore no longer algebraic existence. It is **law/admission/calibration**: what internal or physical condition triggers one of these charge-one triadic phase reversals, if any?
