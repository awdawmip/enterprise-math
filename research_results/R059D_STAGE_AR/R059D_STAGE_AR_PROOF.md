# R059D Stage AR — Proof

Researcher: `EM-R059D-AR-5B8D24`

Task: `RS-R059D-STAGE-AR-STATEFUL-LINE-SEGMENT-MULTIPATH-ESCAPE-TURN-CLOSURE`

## 1. Native one-step state

Work in the accepted signed-origin foundation. `+1 ≡ -1 ≡ O_E`; native zero does not exist. The auxiliary A2 vertex chart is used only for incidence.

Let the six auxiliary one-step neighbors of the origin be

`r0=(1,0), r1=(0,1), r2=(-1,1), r3=(-1,0), r4=(0,-1), r5=(1,-1)`.

Let `e_k=[O,r_k]` be the corresponding primitive radial edge. Its signed-native image is one of the six AP one-step anchors.

A primitive edge in the triangular complex is incident to exactly two elementary triangles. Therefore the smallest state that still represents a line segment, rather than only a cell, is

`S=(e,C)`

with global fixed endpoint `O_E`, where `e` is a primitive radial edge and `C` is one of its two incident triangles. `C` records the side into which the segment is sweeping.

The free endpoint is derivable as the non-origin endpoint of `e`; previous-cell memory is not legitimate here because the segment lies along the primal edge and does not cross it as a dual walker.

## 2. Exactly twelve lifts

Define the six origin-star wedges in positive order:

- `c0=U(0,0)` between `e0,e1`;
- `c1=D(-1,0)` between `e1,e2`;
- `c2=U(-1,0)` between `e2,e3`;
- `c3=D(-1,-1)` between `e3,e4`;
- `c4=U(0,-1)` between `e4,e5`;
- `c5=D(0,-1)` between `e5,e0`.

For every radial edge `e_k` there are precisely two lifts:

`S_k^+=(e_k,c_k)` and `S_k^-=(e_k,c_(k-1))`, indices modulo 6.

Thus there are exactly twelve legitimate one-step segment states. D6 acts on the index `k`; reversal exchanges `+` and `-`.

## 3. Candidate relation from segment semantics

An origin-star triangle `C` has exactly two edges incident to `O_E`. If the current state is `(e,C)`, one is the current segment edge `e`. Let `e'` be the unique other origin-incident edge of `C`.

A continuous incidence sweep through the selected side cell must leave `C` through `e'`:

- crossing back through `e` undoes the chosen side-cell sweep;
- crossing the third/opposite edge cannot produce a fixed-origin one-step segment because that edge does not contain `O_E`;
- `e'` is therefore the unique legitimate next segment edge.

Let `D` be the triangle on the far side of `e'`. The next state is `(e',D)`.

Consequently

`T(S_k^+)=S_(k+1)^+`,

`T(S_k^-)=S_(k-1)^-`.

No angle, source circle, AK orbit membership or AL frontier rule appears in this derivation.

## 4. Stateful farthest escape

AQ shell is the dual-cell graph distance from `STAR(O_E)`. Every `c_k` belongs to `STAR(O_E)`, so every primary AR state has shell zero.

Since the segment-semantic candidate set is a singleton, `FAR_STATE=NEXT` automatically. Therefore every transition satisfies

`Delta SHELL=0`.

AQ's `Delta SHELL=+1` DAG theorem is thus a theorem of the memoryless cell state, not of the stateful one-step segment.

## 5. Closure

The formulas above give two directed cycles:

`S_0^+ -> S_1^+ -> ... -> S_5^+ -> S_0^+`

and

`S_0^- -> S_5^- -> ... -> S_1^- -> S_0^-`.

They are disjoint as lifted states and exchanged by reversal. Every state has minimal positive return time six.

Projecting `S_k^±` to the free endpoint gives `r_k`. Hence both cycles project to the same six-point A1 endpoint orbit with opposite orientation. Every legitimate side lift closes; there are no equally admissible escaping branches.

## 6. One-step length without AK leakage

Define the pre-circle one-step invariant by primitive incidence:

`L_pre(e)=1 iff e is a primitive lattice edge incident to O_E`.

Every AR state edge has this property and the transition replaces one radial primitive edge by another. Therefore `L_pre=1` is preserved identically.

No non-axis native endpoint is invented. The between-anchor turning information is the side triangle itself.

## 7. Jump-budgeted family

From all twelve lifted seeds, `T` is a permutation, so for every `J>=0`:

- exact-J path count is 12;
- exact-J lifted endpoint set is all twelve states;
- projected cell set is the six origin-star cells;
- projected free-endpoint set is all six A1 anchors.

From one visible anchor while retaining its two side lifts, after `J` jumps the two projected endpoint indices are `k+J` and `k-J` modulo six. They coincide exactly for `J=0 mod 3`. The up-to-J visible endpoint set becomes all A1 by `J=3`.

The intrinsic first-return time is six; it is derived, not selected as a tuned budget.

## 8. AL support comparison

AL support is admitted only after the primary theorem is frozen. Every primary AR triangle has vertices consisting of `O_E` and two one-step A1 points, all contained in `K_E(1)`. Since the support carriers are nested, all twelve AR states lie in `K_E(r)` for every `r>=1`.

Therefore the support cap is inactive on primary AR. It agrees with the AL frontier at `r=1`, but increasing `r` does not create a radius-r AR state or higher-radius frontier. General radius remains a separate state-definition problem.

## 9. Post hoc comparison

The AR endpoint projection equals the accepted AP one-step cycle. Under the accepted signed-origin radius-1 conjugacy it also agrees with AK radius-1 endpoint order, D6 action, reversal and period; and it equals the AL radius-1 frontier. These are comparisons only.

The hidden state is genuinely different: AR stores primitive segment edge plus side triangle. No AP collapse raw state, AK `tau` state or AL A8 selector was used.

## 10. Theorem

Within the one-step signed-origin class:

`STATEFUL_ALL_PATH_SEGMENT_ESCAPE_DERIVES_NATIVE_TURN_CLOSURE__NO_SINGLE_PATH_SELECTOR_NEEDED`.

Scope qualifier:

`ONE_STEP_SIGNED_ORIGIN_SEGMENT_CLASS_ONLY__GENERAL_RADIUS_STATE_LIFT_OPEN`.
