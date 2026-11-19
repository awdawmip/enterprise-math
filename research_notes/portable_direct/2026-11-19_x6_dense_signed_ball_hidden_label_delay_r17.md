# X6 R17 — Arbitrarily delayed source identity visibility inside a fully occupied signed six-axis Cell ball

Date: 2026-11-19 (Asia/Shanghai). Research Task RS-X6-NATIVE-TIME-DYNAMICS / TP2-91D4A7C2F63805BE21A3; predecessor R14, R14B, R15, R16. Frozen P000 scientific pin `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. **Exact conditional Boolean-BRC vacancy theorem; NOT_REVIEWED.** This is not native `TRIADIC_CLOSURE_E` permission or a physical time calibration.

## Why this is a new edge case

R15 proved that permutations of a contiguous source chain can have identical immediate Port languages but different two-event futures. R16 identified a strong mobility/connectivity regime where two events reconstruct a complete labelled adjacency graph. This result proves a complementary obstruction: **if initially immobile interior blockers are embedded in a dense moving population, source-label identity can remain hidden for arbitrarily many future events even when all twelve signed axis directions are available to every source.**

## Model

The spatial carrier is the native chart-relative signed `Z^6` Cell torsor, with no global origin. Choose one Cell anchor for the proof and represent locations by signed six-tuples. The primitive signed directions are `D={±e_1,...,±e_6}`. There are finitely many distinguishable labelled sources, at most one source per Cell. A labelled action `(s,v)`, `v∈D`, succeeds precisely when its target Cell is unoccupied, then moves that source one native signed unit. All labels and ordered source/Port events remain visible in Boolean-BRC support. Time is **event order**, not a seventh space axis.

For an integer `R≥2`, define the finite occupied ball
```
B_R = { x∈Z^6 : ||x||_1 ≤ R },    ||x||_1 = sum_{i=1}^6 |x_i|.
```
Here the 1-norm counts the minimum signed-primitive *event hops* and is not the P000 squared enterprise geometric length. Fill every Cell of `B_R` with exactly one individually labelled source, with the exterior vacant. Choose two labels `A`, `B`; in placement `P_R`, put `A` at `0` and `B` at `e_1`; in `Q_R`, exchange just these **two labels**. Every other source retains exactly the same label and Cell in both placements. The unlabelled occupancy set is identical.

Let `L_h(P)` denote the successful ordered source/Port words of length at most `h`, including the empty word. Let `δ(P,Q)` be the smallest `h` such that `L_h(P)≠L_h(Q)`.

## Theorem R17.1 — Exact arbitrary delay

For **every integer `R≥2`**,
```
                 δ(P_R,Q_R) = R.
```
Thus `L_{R-1}(P_R)=L_{R-1}(Q_R)`, while a length-`R` word is legal from exactly one placement. This gives an unbounded delay in distinguishing two configurations that share the same occupied Cell set, all labels except a two-label transposition, and all current unconditional scalar source counts and count-derived phases.

### Proof: lower bound using vacancy propagation

An allowed move exchanges an occupied Cell with a neighbouring vacancy. Given any initial occupied Cell `z∈B_R`, every vacancy that could be brought to `z` must travel through at least `R+1-||z||_1` signed-unit edges from the initially vacant complement. The reason is that every originally vacant Cell has hop norm at least `R+1`, while one legal vacancy-exchange event moves a vacancy at most one edge. This lower bound holds even when many other labelled sources are moved and many exterior vacancies exist.

Before the label initially at `e_1` can make its *first* move, a neighbouring destination of hop norm at most 2 must become vacant. Its nearest initial vacancy is at distance `R-1` from such a destination, so at least `R-1` earlier events are necessary: the label cannot move before event `R`. Similarly, the label initially at `0` cannot move before event `R+1`: all its neighbours have norm 1 and need at least `R` prior vacancy exchanges.

Therefore, in **every** successful word of length `h<R`, neither of the two exchanged labels moves from either initial placement. Every other source has the same label and initial position in both placements. The two systems consequently have identical occupied Cell sets at every common word prefix and agree on the legality of all other labelled moves. An action of either exchanged label is blocked in both until length `R`. Induction over all length-`h` words gives `L_h(P_R)=L_h(Q_R)` for `h<R`.

### Proof: a matching labelled event word

Consider the following `R-1` moves, in exactly this order, all along `+e_1`:
```
source initially at R e_1     -> (R+1)e_1,
source initially at (R-1)e_1 -> R e_1,
...
source initially at 2e_1     -> 3e_1.
```
Every move is legal: the first moves into the initially vacant exterior, and each subsequent move enters the vacancy created by its predecessor. All these source labels are unchanged by the initial two-label swap, so the prefix is legal in both placements and leaves `2e_1` vacant.

Now attempt `(B,+e_1)` as event `R`. In `P_R`, label `B` is at `e_1` and enters the newly vacant `2e_1`, so the entire word is legal. In `Q_R`, `B` is at `0`, its target `e_1` is still occupied by `A`, and the final move is blocked. The two length-`R` languages differ, which matches the lower bound. QED.

## Population dependence and exact shell count

The number of sources is the number of integer lattice Cells in this occupied ball:
```
N_6(R) = |B_R| = sum_{j=0}^{min(6,R)} 2^j * C(6,j) * C(R,j).
```
This is obtained by choosing `j` nonzero components, their signs and positive magnitudes whose total does not exceed `R`. The leading term is `(4/45)R^6`, so this family has `δ=Θ(N_6(R)^{1/6})`. A fixed number (six) of spatial axes therefore does **not** force a uniform finite source-identity observation horizon when the population can grow.

Unlike R14B's long-distance two-source example, these two configurations have **identical occupied coordinate sets**; the delayed observable is explicitly the identity of an initially shielded source. Unlike R10's fixed-obstacle model, every source is offered the same complete signed 12-Port alphabet, subject only to vacancy.

## Executed reproducible evidence

Companion files: `x6_dense_ball_delay_brc_verify.py` and `x6_dense_ball_delay_brc_results.json`.

- Exact six-component integer ball generation and source count checked at `R=2,3,4,5,6,7`: source populations `85,377,1289,3653,8989,19825` and matching constructive witness lengths `2,3,4,5,6,7`. Each encoded witness was actually run through the vacancy move operator in both states and accepted in `P_R` but rejected at the last event in `Q_R`.
- At `R=2` the program additionally exhausts all one-letter moves for 85 labelled sources in both placements and the complete legal second-move alternatives after each common one-letter move: `732` common permitted first events and `222` ordered two-letter words with different success. All assertions PASS.
- The exclusion of *all* shorter words for arbitrary `R` rests on the symbolic vacancy-distance invariant above; the larger finite cases test the exact matching construction and population formula, not an exponentially large full language enumeration.

## Actual remaining native question

An admitted X6 event must also honor the native signed Link/Port source, triadic closure, force and causal time guards. To transfer this result from the vacancy-only interface, first exhibit native permitted sequences corresponding to the vacancy-release moves and the final formerly blocked Port; then check whether their complete labelled source observer is preserved by that mapping. If any native guard forbids the release chain, the exact delay must be recomputed in the actual native event alphabet, not asserted from this conditional model.

R16's two-event blocker tomography and R17's dense interior delay are compatible: R16's two-event reconstruction applies to blockers that can **move immediately**, while R17 purposely places the swapped sources inside a region where their first legal movement is delayed by the vacancy depth. Both the science source and Activity link are independent of formal CLAIM/PROGRESS and independent review.
