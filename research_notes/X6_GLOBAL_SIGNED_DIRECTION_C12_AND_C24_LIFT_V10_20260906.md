# X6 rotation V10: global signed-direction C12 frame class and intrinsic C24 Cell lift

Status: `FREE_RESEARCH / EXACT CLASSIFICATION + PATH LIFT / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-NATIVE-ROTATION-DYNAMICS`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- `X6_FULL_INTEGRAL_ISOMETRY_AND_ORI6_GATE_V7_20260906.md`;
- `X6_ORI6_EVENT_CHARGE_AND_OBSERVER_BOUND_V8_20260906.md`;
- current signed-X6 BRC shortest-path kernel.
Checker: `experiments/x6_global_c12_v10_20260906/check_global_c12_c24.py`.

## 1. Global rotation question

Local triadic generators act on one three-axis selection and produce a six-phase orbit on that triad's signed primitive directions.

A stronger genuinely six-axis question is now well-typed:

> which integral X6 frame isometries act transitively on the entire primitive signed direction shell
> `D_12={+/-E_1,...,+/-E_6}`?

This condition asks for one single global phase cycle visiting all twelve primitive signed directions. It is a static/frame condition first; path/event admissibility remains separate.

## 2. Signed permutation orbit decomposition theorem

Write an integral frame isometry as a signed permutation

`g(E_i)=epsilon_i E_{p(i)}`,

with `p in S6` and `epsilon_i in {+1,-1}`.

Take one cycle `C` of `p` of length `ell`. Define its sign holonomy

`s_C=product_{i in C} epsilon_i`.

Following a signed unit direction once around the underlying `p` cycle gives

`g^ell(E_i)=s_C E_i`.

Therefore:

- if `s_C=+1`, the signed directions over that cycle split into two disjoint `ell`-cycles, one starting at `+E_i` and one at `-E_i`;
- if `s_C=-1`, the signed directions over that cycle form one `2ell`-cycle.

This completely classifies the action of any integral frame isometry on the 12 primitive signed directions.

## 3. Characterization of a single global C12 phase orbit

The action on all twelve signed directions is one cycle iff:

1. the underlying positive-axis permutation `p` is one 6-cycle;
2. the sign holonomy around that 6-cycle is `-1`.

Necessity: a single signed orbit must involve all six unsigned axes, so `p` has one 6-cycle; its signed orbit has length 12 only when the cycle sign product is negative.

Sufficiency follows immediately from the orbit decomposition theorem.

Hence the global-C12 frame class is

`GLOBAL_C12={signed 6-cycles with negative sign holonomy}`.

For every `g` in this class:

`g^6=-I`,

`g^12=I`,

and the order is exactly 12.

## 4. Global C12 automatically carries Ori6 charge one

A 6-cycle has permutation parity

`(-1)^(6-1)=-1`.

Therefore every global signed-direction C12 frame lies in the odd positive-axis permutation coset:

`Ori_6(g)=1`.

Thus:

`ONE TRANSITIVE C12 ORBIT ON ALL 12 PRIMITIVE SIGNED DIRECTIONS`

`=>`

`ORI6-CHANGING STATIC FRAME`.

This is a new exact link between the global primitive-direction phase requirement and the V8/V9 orientation gate.

It does not prove such a frame event is physically admissible; it proves that **if** full six-axis rotation is required to be one 12-phase primitive-direction cycle, it necessarily crosses the currently missing Ori6 sector.

## 5. Exact count: 3840 global C12 frames

The number of 6-cycles in `S6` is

`(6-1)!=120`.

For a fixed 6-cycle there are `2^6` sign assignments; exactly half have negative product. Hence there are

`2^5=32`

negative-holonomy assignments.

Therefore

`|GLOBAL_C12|=120*32=3840`.

This is a subset of the 23040-element odd half of the full signed frame-isometry group.

## 6. All 3840 form one R_triad conjugacy orbit

The current triadic frame group is

`R_triad=(C2)^6 semidirect A6`.

The 3840 global C12 frames form one conjugacy orbit under `R_triad`.

There are two ingredients.

### Positive-axis part

All 6-cycles form one `A6` conjugacy orbit. Their `S6` conjugacy class does not split when restricted to `A6` because the centralizer of a 6-cycle contains odd powers of the 6-cycle itself. The exact orbit size is 120.

### Sign-holonomy part

For fixed underlying 6-cycle `p`, diagonal sign conjugation changes edge signs by

`epsilon'_i=delta_i delta_{p(i)} epsilon_i`.

The total cycle product is invariant. Conversely any two sign assignments with the same total product differ by such a coboundary: choose one `delta` and solve successively around the cycle; consistency is exactly equality of the products.

Since the full sign kernel `(C2)^6` lies in `R_triad`, all 32 negative-holonomy assignments are connected.

Therefore the full 3840-element class is one current-even-dynamics conjugacy orbit.

Its stabilizer in `R_triad` has order

`23040/3840=6`.

So, up to change of current triadic frame, there is only one static global-C12 type.

## 7. Canonical representative

A convenient representative is

`G(E_1)=E_2`,
`G(E_2)=E_3`,
`G(E_3)=E_4`,
`G(E_4)=E_5`,
`G(E_5)=E_6`,
`G(E_6)=-E_1`.

Its primitive signed-direction phase sequence is

`E_1,E_2,E_3,E_4,E_5,E_6,-E_1,-E_2,-E_3,-E_4,-E_5,-E_6`.

Then the next phase returns to `E_1`.

This sequence displays directly

`G^6=-I`,

`G^12=I`.

No classical continuous angle or target value of pi is used.

## 8. Every global C12 macro edge has exactly two shortest Cell realizations

Let

`a_r=G^r(E_1)`.

Consecutive phases always lie on two distinct unsigned native axes. Therefore

`a_{r+1}-a_r`

has exactly two nonzero signed unit components.

The current signed-X6 BRC theorem gives

`N_min=2`,

`B_min=2`.

The two shortest paths are again

`INNER: a_r -> 0 -> a_{r+1}`,

`OUTER: a_r -> a_r+a_{r+1} -> a_{r+1}`.

Thus one complete 12-macrostep frame cycle has

`2^12=4096`

distinct concatenated shortest microtrace histories, each of total primitive Cell length 24.

Frame closure `G^12=1` therefore does not erase path holonomy/provenance.

## 9. Exact intrinsic C24 all-OUTER Cell cycle

Define

`m_r=a_r+a_{r+1}`

for `r mod 12`.

Then both

`a_r -> m_r`

and

`m_r -> a_{r+1}`

are primitive signed-axis Cell steps.

The twelve `a_r` are all distinct norm-one Cells. The twelve `m_r` are all distinct norm-squared-two Cells. No `m_r` equals any `a_s` because their native squared component lengths differ.

Therefore

`a_0,m_0,a_1,m_1,...,a_11,m_11`

is an exact **24-state native Cell cycle**.

Call it the global-X6 OUTER C24 lift of the signed-direction C12 frame.

This is intrinsic to signed X6 Cell/path structure once the global C12 frame is supplied.

## 10. Relation to the local Viète C24 obstruction

Earlier STAR-carrier Viète work showed that continuing the planar triangular-carrier half-angle ray refinement from C12 to a single native C24 ray hits a carrier/lattice obstruction.

The present C24 is a different typed object:

- it uses all six native axes globally;
- its even phases are signed primitive X6 directions;
- its odd phases are nonzero two-axis composite Cells;
- it is not a claim that a local STAR triangular carrier contains a 15-degree single-Cell ray;
- it does not supply the missing local half-angle carrier state.

So there is no contradiction. Rather, the result shows that **global six-axis X6 admits an intrinsic 24-Cell rotation microcycle even though one fixed local triangular carrier cannot realize the next half-angle as one lattice ray**.

This may become a bridge in future Viète/precision research, but no such bridge is claimed here.

## 11. All-OUTER is one law section, not a universal rotation law

The C24 cycle chooses OUTER at every macro edge. Generic frame/path semantics still has all 4096 shortest histories.

The earlier branch-selector context theorem already proves that INNER versus OUTER cannot be selected universally from the endpoint/frame arrow alone.

Therefore the C24 OUTER lift is a precise section under an OUTER/nonzero-intermediate style event law, not an automatic physical realization of every global C12 frame.

A different event context could select another branch word.

## 12. New physical gate

The global rotation problem now has an especially sharp conditional form.

If a physical/native principle says:

`FULL SIX-AXIS PRIMITIVE-DIRECTION ROTATION = ONE TRANSITIVE C12 PHASE ORBIT`,

then any such event must:

- carry `Ori_6=1`;
- be equivalent under current triadic frame changes to the canonical signed 6-cycle above;
- possess a 4096-member shortest BRC path fiber per full frame period;
- admit the 24-Cell OUTER cycle as one concrete section.

What remains unproved is the antecedent physical principle and the law selecting a concrete path section.

## 13. Verification

The exact checker verifies across all 46080 signed frame isometries:

- transitive action on `D_12` iff underlying permutation is a 6-cycle with negative sign product;
- exact count 3840;
- every such frame has `Ori_6=1`, `g^6=-I`, `g^12=1`;
- all 3840 are one `R_triad` conjugacy orbit with stabilizer order 6;
- every one has twelve two-branch shortest macro edges;
- the canonical representative has 24 distinct all-OUTER Cell states;
- one full frame period has exactly 4096 distinct concatenated shortest microtrace loops of length 24.

No physical-admissibility, Foundation-promotion or external novelty claim is made.
