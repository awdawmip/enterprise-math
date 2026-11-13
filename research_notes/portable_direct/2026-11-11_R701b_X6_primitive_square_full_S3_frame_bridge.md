# R701b — a four-Cell native X6 square realizes every S3 based-loop holonomy; exact 120-state microframe monitor

Date: 2026-11-11 (Asia/Shanghai). Task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`; publication `TP2-8B7E13C5904A2D6F1142`. Follow-up to R701 on the same Draft PR. Status: **EXACT CONDITIONAL MODEL MATHEMATICS + EXHAUSTIVE FINITE CHECK; UNREVIEWED**. No P000, active worldview, frozen scientific input pin, formal CLAIM or Result changed.

## 1. A genuine X6 coordinate adjacency issue: three-Cell physical rings

P000 V5 establishes primitive signed unit coordinate steps `x -> x ± e_i` on the six-dimensional native Cell torsor `Z^6`, where a chosen Cell anchor supplies a relative chart. The integer parity map `chi(x)=(sum_{i=1}^6 x_i) mod 2` switches value on every such step. Consequently **every closed primitive-coordinate step word has even length**. In particular the three-Cell directed network triangle used for the V17 three-transition loop in V36 cannot simultaneously have all three edges realized by primitive signed native coordinate adjacency. This is a precise typing distinction: V36 permits a *relational Cell network* whose edges need not all be primitive spatial coordinate neighbors.

Four is sharp. Within the full X6 space select four distinct Cells with relative signed charts:

`x0=(0,0,0,0,0,0)`,
`x1=(1,0,0,0,0,0)`,
`x2=(1,1,0,0,0,0)`,
`x3=(0,1,0,0,0,0)`.

The directed cyclic edges `x0->x1->x2->x3->x0` are `+E1,+E2,-E1,-E2`, all P000-native primitive coordinate steps. This is a *four-Cell subgraph in the complete six-dimensional world*, never a new native 2D plane or a replacement for X6.

## 2. Constructive V36/V17 theorem: the primitive-coordinate four-Cell circuit realizes all six holonomies

Fix base active triad `S0=(0,1,2)`, using 0-based labels for six native axes. Let `W=(S0,S1,S2,S3)` be a cyclic word of 3-subsets of the six axes, such that each adjacent pair, including `S3->S0`, shares exactly two axes (`J(6,3)` relation). Initialize each physical Cell `xi` with `Si`. Couple the Cells along the above *primitive-coordinate* directed four-cycle by the V36/V20 pure-triadic rule: at each synchronous **relation layer**, Cell i selects the adjacent triad matching its successor's previous state. V36's strict matching score property makes this update deterministic; inductively

`X_i^t = S_(i+t mod 4)`.

Thus the active Cell configuration returns after four relation layers, while Cell x0 follows the based V17 triad walk `S0->S1->S2->S3->S0` with its exact shared-axis slot transport `h(W) in S3`.

A finite exact enumeration of **all** length-four based admissible active-triad words returns 369 words and full six-valued holonomy distribution:

| V17 endpoint slot tuple | Number of four-switch based words |
|---|---:|
| `(0,1,2)` | 207 |
| `(0,2,1)` | 48 |
| `(1,0,2)` | 48 |
| `(1,2,0)` | 9 |
| `(2,0,1)` | 9 |
| `(2,1,0)` | 48 |

All six values occur on **the same four Cell coordinate-adjacent network topology**, varying only the declared legal initial triad word. For example a single four-transition loop

`012 -> 013 -> 023 -> 123 -> 012`

has holonomy `(1,2,0)`, a nonidentity 3-cycle. By V36's precise conditional law it is a completed autonomous four-relation-layer recurrence.

## 3. Complete V17 intermediate frame carrier requires 120 states, not only the S3 macro frame

The six-port R701 transducer encodes the six **based-loop boundary holonomies** in `S3`. Inside a V17 loop, the active support changes, so the actual three-slot state is an *injective ordered 3-tuple* of six native axes:

`q=(a,b,c)`, with `a,b,c` pairwise distinct in `{0,1,2,3,4,5}`.

This exact microframe carrier has

`6*5*4 = 120`

states: 20 choices of active support and six slot orderings per support. Each primitive J(6,3) update replaces **one of the three slot axes** by **one of the three absent axes**; the resulting nine successors are distinct, and the other two slot identities are preserved. A complete BFS from the base `(0,1,2)` reaches all 120 microframes, with exact distance shells

`(1,9,36,63,11)`

at distances 0 through 4. The maximal shortest distance is **4** micro-updates.

The 120-state monitor distinguishes exact active support and slot assignment at **each** intermediate relation layer. It is the minimal *direct port-name inventory* when every distinct ordered active frame must have a distinct labelled port, whereas the 6-state R701 macro monitor suffices at based-loop boundaries for the declared holonomy-only future language. This is typed observer-specific compression, not an additional spatial dimension.

## 4. Candidate V29 event encoding on the same ordered four-layer history

A **declaration of the joint event scheduler** associates one matched V29 TRANSFER with each of the four oriented primitive-coordinate edges per relation layer. Four layers produce directed physical transfer counts `(4,4,4,4)`, with zero scalar Cell boundary at each vertex and net closed integer transfer cycle chain `j=4C`, where C is the directed square circuit. These are valid nonnegative V29 matching counts on actual P000 unit-step Cell links.

Separately, construct a **diagnostic** V29 internal PASS monitor at the observed Cell, using 120 internal ordered-frame ports. The V17 active transition `q_t->q_(t+1)` writes one nonnegative count `M[q_t,q_(t+1)]+=1`, preserving raw BRC token sequence and relation-layer order. V29 count algebra gives the telescoping identity

`u_int = (M-M^T)1 = delta_(q0) - delta_(q4)`.

Since the based loop returns to support 012, `q4=h(W)` is one of the six permutations of base axes, so the **same four-layer history** yields the pair `(j,h)=(4C,h(W))`, consistent with the declared V39 based-loop observer. The *diagnostic* frame-port PASS is a compatible count encoding of the actual V17 update, not an independently admitted physical PASS routing/energy law. V29 TRANSFER matching here counts declared completed relation-edge events; an autonomous physical event scheduler and deeper Cell inventory law remain separate admission questions.

The simultaneous V36 relation update and the V29 transfer-count emission are an explicit combined conditional model. The V20 matching law is what selects the active successor; V29 alone selects no next triad and need not be treated as a force law. Four event layers are ordered relation layers, not automatically four calibrated physical heartbeat intervals.

## 5. Exact proof and finite verifier

The parity obstruction is a direct mod-2 invariant of P000 unit steps. The four-Cell construction explicitly checks every signed coordinate edge. V36's successor-copy induction proves cyclic recurrence for any legal W. The microframe count is `6P3`, its successor degree is `3*3`, and the S3 return classification follows complete finite enumeration of all possible 20^3 intermediate support triples, with exact adjacency and slot-update checks. The V29 monitor identity follows telescoping for any finite path; the 369-instance enumeration checks every four-layer V36 schedule and its nonnegative event ledger.

Actual executed deterministic JS `R701B_X6_SQUARE_120FRAME_VERIFY.js` returned `R701B_X6_SQUARE_FULL_S3_PASS`, checked the 120 state graph, 369 cyclic words, 6 complete holonomy classes, and 44,280 frame-coordinate contrast conditions (369×120), and the four-edge matched TRANSFER conservation.

## 6. Next smallest research step

Reconcile the candidate *diagnostic* V29 frame-PASS semantics with a source-defined actual X6 Link/Port inventory and V20 coupling, by writing an explicit per-Cell event dependency packet. Determine whether active relation switches correspond to completed internal channel passages or must be represented as a separate typed frame update. Preserve the exact BRC path and Cell identities; compare candidate frame monitor with the true admissible network observer. The mother triadic force-closure dynamics and independent rotation-covariance admission remain open.

References: P000 V5, `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`, `research_notes/X6_ACTIVE_TRIAD_HOLONOMY_CONTROL_V17_20260906.md`, `research_notes/X6_ACTIVE_LOOP_TO_DIRECTED_RING_REALIZATION_V36_20260906.md`, `research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md`, `research_notes/X6_CYCLE_CURRENT_S3_OPERATION_SAFE_PORT_V39_20260906.md`, and R701 at PR #2023. All original source bytes and frozen scientific pins are preserved.
