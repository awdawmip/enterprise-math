# R711b — Sharp transient current and first-phase repair memory in optimal even-ring serialization

Date: 2026-11-11 (Asia/Shanghai). Author-side candidate-model exact theorem; unreviewed. Same Source/P000 frozen scientific pin as R711: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Direct dependencies: R709b, R710s and R711; exact native event grammar: `research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md` (V29).

## Problem

Take a full-firing even m-Cell ring, m>=4. Every physical edge executes two separate positive V29-style typed occurrences with opposite directions. Capacity: at most one incident transfer per Cell in each microphase. Freeze the gate/triad inputs; commit the triad field after all phases. Define derived signed physical-edge current after phase t: `j_i(t)=(# completed plus transfers on edge i)-(# completed minus transfers on edge i)`. This is an INTEGER edge-incidence readout, not an algebraic subtraction of positive BRC path weights. At the completed macrostep, each edge has one transfer of each type, so `j_i(4)=0` for all edges.

## Theorem 1 — complete structure of four-phase optimal schedules

For every even m>=4, any valid four-phase full-firing schedule consists of two occurrences of the even-edge perfect matching E and two occurrences of the odd-edge perfect matching O. Each of the m edges has an independent choice of which occurrence carries its positive-type event first, yielding exactly `binom(4,2) * 2^m = 6 * 2^m` distinct typed phase schedules when within-phase order of disjoint events is ignored.

Proof. Each Cell participates in four elementary events (two incident ring edges times two opposite types). Four phases with incidence capacity one force each Cell to participate in every phase; therefore every phase executes exactly m/2 disjoint events and is a perfect matching. The simple even cycle has exactly two perfect matchings, E and O. Each physical edge must appear twice, so each matching appears twice. Given the matching phase positions, the two event types on an edge may be ordered either way, independently among m edges. QED.

## Theorem 2 — exact transient signed-current profiles

Let `D_t = sum_i |j_i(t)|` after phase t, t=1,...,4. If the first two phases use the same perfect matching, the exact profile is

    (D_1,D_2,D_3,D_4)=(m/2,0,m/2,0).

If the first two use different matchings, the exact profile is

    (D_1,D_2,D_3,D_4)=(m/2,m,m/2,0).

Indeed, an edge has nonzero signed current exactly between its two opposite typed occurrences. After the first phase exactly m/2 edges have one event; the second phase either cancels those same edges, or exposes the previously unvisited disjoint matching in addition. The remaining two phases finish each edge once. The absolute values are independent of event type orientation.

Thus the sharp minimum possible peak residual at microphase boundaries is `m/2`, achieved by grouped matching order E,E,O,O or O,O,E,E; mixed orders have peak `m`. The sum `D_1+D_2+D_3` is respectively `m` or `2m`. There are exactly `2*2^m` grouped optimal schedules and `4*2^m` mixed ones. At least one nonzero transient edge-current observation is unavoidable in any such four-phase implementation even though the completed V29-style counterflow ledger has zero signed current.

## Theorem 3 — exact first-microphase information fiber

Under the completed macrostep's fixed positive typed-event ledger and fixed labelled full ring, phase 1 may choose E or O, and each of its m/2 edges may send the plus or minus event first. Therefore there are precisely `2*2^(m/2)=2^(m/2+1)` distinct derived signed physical-current vectors `j(1)` compatible with the same completed macro ledger. Any fixed-length reversible record of `j(1)` needs at least and exactly `m/2+1` bits. This is an observer- and horizon-specific first-phase memory cost, not a claim about raw complete history.

## Proof scope, computation, and native interface

The V29 original grammar declares a TRANSFER to be a positive increment of `Rout` at one Cell and `Rin` at another, and explicitly separates cumulative counts from native event order. R711/R711b use legal V29-style event *shapes* on declared bidirectional ports. The additional token inventory gate, one-incident-event-per-Cell phase capacity, and four-phase frozen-state commit are explicit candidate extensions, not constraints already supplied by the standalone V29 grammar. V36 supplies the synchronous triad-copy mechanism when its admitted old-neighbor setting holds.

R711B_FOUR_PHASE_MICROCURRENT_VERIFY.js exhaustively checks every matching-phase order and every per-edge first-type assignment for even m=4,6,8,10,12. Exactly 32,736 typed phase schedules were checked, verifying Cell disjointness, per-edge event multiplicities, signed-current trajectories and exact information-fiber counts; JSON evidence is attached. No continuous model, cancellation of BRC positive mass or probabilistic physical assumption is used.

## Next

Test actual admissibility of the frozen-prepare/commit event bundle under the current Source Link/Port semantics, then optimize peak current and information repair when some edges are disabled or the ring length is odd. Preserve both the V29 count ledger and the microphase order observable when the future language queries it.
