# R644｜V29 实际保守事件账本上的最小零净流入奇 holonomy 见证

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR_SIDE_EXACT_CONSTRUCTION + SHARP_SCOPED_LOWER_BOUND / UNREVIEWED / NOT_ADMITTED.

## 1. Accurate source typing and improvement on R643

Frozen signed BRC R462@18783e01e3646c72b7aab3b16d3f565e83e6446f unchanged.
Original source: enterprise-math@b62110008321d9147212cb89f2627ff613c2550d, V23 four-field code and V26/V27 typed signed active-triad score; V28 passage-continuity source and V29 source-defined PASS/TRANSFER event ledger from `research_notes/X6_PASSAGE_CONTINUITY_AND_NETWORK_BIAS_V28_20260906.md` and `research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md`; V17 S3 shared-slot transport.

R643@5ef4f724a5357bb39db360b600d24b5104b96b7f constructed a proposed count-changing auxiliary source using `M→M+C` while holding `I,O` fixed. R644 replaces that auxiliary count choice by the **actually source-defined V29 PASS events and its exact reconstructed I/O**, then constructs a smaller *zero-net-accumulation*, conservation-respecting typed witness. The scheduling decision to apply a whole 3-PASS packet before one V27 score update remains an explicitly **proposed** coupling; V29 already defines individual PASS and TRANSFER updates, not an autonomous complete joint scheduler.

Four PF10 internal ports are separately typed from the six native X6 axes. The 20 active triaxes are finite subsets of these six axes, not Cell addresses; no native plane or seventh space axis is introduced. One packet step is a relation-event grouping, not a calibrated heartbeat duration. Positive Weighted-BRC and signed contrast are separate observers.

## 2. Exact source-defined nonnegative conservative seed

Use the original V29 source state at Cell x:
`(M_x,Rin_x,Rout_x)`, with V29 reconstructed counts
`I_x=M_x 1+Rin_x`, `O_x=M_x^T 1+Rout_x`,
`u_x=I_x−O_x`, `Ω_x=M_x−M_x^T`.
All stored entries are nonnegative integers.

Start with a two-Cell finite network x,y with all-zero counts. Perform the following five **actual V29 event types** in the declared typed two-Cell port network:
```
PASS(x;0→1);
PASS(x;1→2);
PASS(x;2→0);
TRANSFER(x:0 → y:0);
TRANSFER(y:0 → x:3).
```
After these, x has exactly one directed closed 3-cycle `C_{01}=C_{12}=C_{20}=1`,
`Rin_x=(0,0,0,1)`, `Rout_x=(1,0,0,0)`, and so
```
I_x=(1,1,1,1), O_x=(2,1,1,0),
u_x=(-1,0,0,1),
Ω_0=((0,1,-1,0),(-1,0,1,0),(1,-1,0,0),(0,0,0,0)).
```
The other Cell y has `Rin_y=Rout_y=(1,0,0,0)`, `M_y=0`, so `u_y=0`.
The scalar network charge `Q=Σ_cells Σ_ports u` begins at 0, is 0 after each of the five events and remains 0 after all subsequent PASS events by V29 exact conservation. In fact each Cell has zero total contrast at the end of the seed.

**Theorem A (sharp seed / residual count, within specified V29 event grammar).** Fix the exact target x-state above, a zero initial two-Cell ledger, and distinct-cell TRANSFER edges. It requires at least three PASS events to create the three distinct nonzero M entries, and at least two TRANSFER events to create both `Rout_x[0]=1` and `Rin_x[3]=1` (one distinct outgoing, one incoming). Thus five primitives are necessary; the five-event construction attains the lower bound. Separately, for the fixed closed C and **zero total local bias** `Σu_x=0`, any nonnegative residual choice has `Σ Rin_x=Σ Rout_x`. At zero residual budget `Rin=Rout=0`, `u=0`; V26/V27's score at active triad 012 ties exactly on 015,024,123. Therefore a deterministic 012-directed odd loop needs positive residual budget. One residual on each side is the least possible, and this construction attains it. Minimality is for this declared exact target/loop and observer, not all possible field configurations.

## 3. Infinite odd holonomy on true V29 passage increments

Let `C` be the directed 3-cycle above. At relation-packet index n=0,1,2,..., suppose x currently has `M_n=(n+1)C` and the seed residuals fixed. Set `S_0=012`. Define a proposed packet-boundary active-triad operator:
```
S_(n+1) = unique argmax_(T∈N(S_n)) [u_nᵀ c(T) + c(S_n)ᵀ Ω_n c(T)];
PASS(x;0→1), PASS(x;1→2), PASS(x;2→0) (the following packet).
```
Here the four-field code `c` and score are exactly from V23/V26/V27, while each PASS operation is exactly the published V29 primitive. Because the three PASS deltas sum to zero in u,
```
u_n=(-1,0,0,1),   Ω_n=(n+1)Ω_0,
I_n=(n+1,n+1,n+1,1),   O_n=(n+2,n+1,n+1,0).
```
The complete stored counts stay nonnegative and the exact V29 identity `u=Ω1+Rin−Rout` holds at all n.

**Theorem B (all-index conservative six-cycle).** For every n≥0 the proposed packet-boundary selector started from S0=012 follows
```
012→123→234→034→035→025→012→...
```
with **unique** winner at each visited step and exact V17 slot permutation `(2,1,0)` after 6 steps (an odd transposition), returning to identity after 12 steps. The full PF10 count ledger increases, while the active-triad sequence is periodic.

Proof. For each of the six displayed transitions S→W, evaluate the exact V23 matching code. Relative to every of its eight alternative neighbors, the initial score gap under `u=(-1,0,0,1)` and `Ω_0` is at least 1, and the *minimum* gap on each of the six steps is **exactly 1**. Simultaneously the circulation slope `a(S,W)=c(S)^TΩ_0c(W)=1` is maximal among all nine neighbors of S. At arbitrary n the difference is
```
Φ_n(S,W)−Φ_n(S,T)
 = [Φ_0(S,W)−Φ_0(S,T)] + n[a(S,W)−a(S,T)] ≥1.
```
Therefore the exact same winner is unique on those six triads at every nonnegative n. Induction and V17's original shared-slot transport finish the all-n trajectory/holonomy proof. The finite matching-code computation (6×9 neighbor rows) is reproduced by `R644_VERIFY.py`. The supplied checker additionally performs 151 consecutive source-defined passage packets and exact conservation, continuity and slot tests.

## 4. Scope and transfer to real network problem

This gives a genuine **V29 primitive-event** realization of source-defined PF10 signed changes and a typed two-Cell zero-Q seed using only five primitive events; it shows conservation and inherited odd holonomy are compatible in a particularly small integer family. It replaces R643's unchanged-I/O auxiliary source choice with V29-compliant reconstructed I/O, and replaces R643's nonzero-Q u with the minimal zero-Q u. Both are meaningful, distinct changes to the declared auxiliary dynamical class.

The selected loop is uniquely determined at all n, whereas other starting triads can retain score ties; no globally unique autonomous selector is claimed for this minimal bias. The V29 primitive scheduler itself, its port-to-field injection, physical inter-Cell passage trigger, full X6 spatial legality and independent Driver review remain open. V30 already establishes a stronger event-order/frame obstruction; the present work reuses that theorem rather than claiming a new universal time-order no-go.

NEXT: test whether a locally specified V29 scheduler can naturally select the two TRANSFER seed events and the subsequent internal PASS triple using actual neighboring Cell field states, with source-to-port types, energy/mass constraints, noncommutative order memory and covariance.
