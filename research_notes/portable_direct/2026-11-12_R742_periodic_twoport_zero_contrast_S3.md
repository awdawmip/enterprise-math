# R742 — Periodic bounded-inventory two-port BRC lift with zero terminal V29 contrast

Date: 2026-11-12 (Asia/Shanghai). Author-side conditional constructive lemma; exact finite test, independent review pending.

Parent task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, publication TP2-8B7E13C5904A2D6F1142, frozen P000 science awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Reuse the exact R739/R741 five-triad conditional TRIADIC_CLOSURE_E witnesses, seven selected arcs and rooted three-generator loops at immutable R741 source e3b3e7ec3685ac97f0e3a923c75abc3ad61e49c6. V29 PASS ledger and contrast grammar: awdawmip/enterprise-math@30fb16d39465708fd1b54c70a58d06ad20f310f8:research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md.

## Declared refinement and source-frame interface

Work at a single selected X6 Cell C with two **local internal ports** 0,1 (not X6 spatial axes), five distinct source-attached force tokens and current typed active-triad witness. At every typed triad transition, use R741's source-conditioned decoder and one actual V29 PASS count event; preserve the full triad, branch, previous vertex and source-slot frame. A root-only **identity return PASS** is added after every completed three-arc generator: it has the genuine count increment M[0,1] += 1 and leaves the current rooted triad and V17 holonomy unchanged. This root guard/identity coupling is explicitly an extra candidate scheduler rule, not a primitive transition rule already supplied by V29.

For capacity analysis only, refine each PASS(a->b) with local conserved integer stock b[a] -= 1, b[b] += 1, guarded by b[a]>=1. This stock-moving refinement and its capacity bound are **new explicitly declared assumptions**. Original V29 specifies count updates only, so capacity compatibility here does not establish native permission for token stock or for the triad-switch coupling.

Let F=PASS(0->1), R=PASS(1->0). R741's rooted I,P,Q codewords are
- carrier A: I=FRR, P=RFR, Q=RRF;
- carrier B: I=RRF, P=FRR, Q=RFR.

Every word has exactly one F and two R and returns to active triad 012. The added root identity return PASS contributes F. Thus each augmented generator is respectively FRRF, RFRF or RRFF, with fixed four-event phase boundary and an externally declared root-identity tag. The decoder reads only its first three context-coded events as arc transitions.

## Theorem 1 — Three tokens suffice, and are necessary for a shared periodic stock

Initialize the local stock vector (b0,b1)=(1,2). For any one of the three generator codewords:
- FRR follows stock path (1,2)->(0,3)->(1,2)->(2,1);
- RFR follows (1,2)->(2,1)->(1,2)->(2,1);
- RRF follows (1,2)->(2,1)->(3,0)->(2,1).

The root-identity return F then sends (2,1)->(1,2). Consequently any ordered concatenation of I,P,Q is feasible for all k>=0 with exactly three conserved tokens, no negative stock and each port capacity 3. The auxiliary return is a genuine V29 PASS, not a silently erased event. The same proof works for both carriers.

If one fixed initial stock must permit all three codewords without replenishment before the first generator, FRR begins with F and forces b0>=1, while RRF begins with RR and forces b1>=2. Thus at least 3 tokens are required. The displayed construction attains this. With this three-token common start, the first FRR intermediate state reaches b1=3 and the first RRF intermediate state reaches b0=3, so capacities 3 for both ports are also sharp in this specified shared-start subclass.

## Theorem 2 — Sharp one-PASS periodic refill and symmetric count ledger

Each original three-event codeword moves one token net from port 1 to port 0. For a schedule whose full local stock returns after every complete generator and whose only extra stock-changing operations are two-port PASS events, at least one extra F is necessary per generator (since the extra events must have net #F-#R=1). Exactly one F suffices by Theorem 1. Therefore four PASS events per generator are optimal for this **block-periodic, PASS-only stock-moving refinement**.

For every k>=0, every W in {I,P,Q}^k and either carrier, the terminal count ledger is
M(W)= [[0,2k],[2k,0]], Rin=Rout=0,
hence Omega=M-M^T=0, u=Omega*1=0, Gamma=4k and final stock (1,2). Each of the 3^k provenance-distinct histories has this identical terminal ledger. This exhibits a full six-way ordered-relation residual over a **zero-contrast, balanced, capacity-3** count observer.

## Theorem 3 — Six holonomies at 12 PASS events, and all longer periods

The six 3-generator witness words from R741 remain valid after adding the root-identity F and still have six different final named V17 relations:
word   | A   | B
III    | 012 | 012
IIP    | 021 | 021
IIQ    | 102 | 210
IPQ    | 201 | 120
IQP    | 120 | 201
PQP    | 210 | 102

Each uses exactly 12 actual PASS events and has M=[[0,6],[6,0]], u=0, Omega=0, stocks (1,2), same rooted Cell/triad. For k<=2 at most five relations arise from k symbols of {I,P,Q}; at k=3 all six occur. Thus 12 is the **first full-six-state period endpoint** in this specified fixed-four-PASS-generator family. Prepending I^(k-3) proves six-state realization at every k>=3. Existing R741 character/census formulas apply unchanged to this augmented family because the new return F has identity holonomy and deterministic placement.

The exact terminal quotient (M,u,Omega,stock,current-root) discards all six names on this fiber; at least six residual register values are required to recover named relation, and storing S3 suffices. This is a scoped observer repair, not an assertion that every V29 use needs a six-state register.

## Theorem 4 — Why unpumped finite stock scales with horizon

For a specific sequence of raw F/R moves, write S_j=#R-#F in the first j moves, S_0=0. The exact necessary and sufficient initial stocks for nonnegative execution are b0 >= max_j(-S_j,0), b1 >= max_j(S_j,0). For all 3^k possible unpumped k-generator words from the common initial stock, max S_j = k+1 (select RRF at the final generator), and min S_j = -1 (select FRR at the first). Hence the universal initial stock inequalities are b0>=1, b1>=k+1 and total stock>=k+2. The periodic root F construction removes this linear initial stock scaling without changing the original three generator holonomies.

## Verification and unresolved native interface

The companion standalone JavaScript test runs exact integer exhaustive enumeration for both original carriers and every k=0..8: 9,841 histories per carrier, 19,682 total. It checks all port-level stock prefixes and capacity 3, the reset phase, both complete V29 matrices, the universal unpumped stock construction, the exact S3 permutation compositions and the six named k=3 witnesses. Output is deterministic JSON with status PASS, reproduced in the companion results artifact. The all-k assertions follow from the above per-generator proof, finite-group multiplication and prefix-stock lemma, not from extrapolating the k<=8 finite checks.

P000 native closure source and S6 axis-label provenance remain the declared R739/R741 premises. The next actual task is to determine whether the intended X6 Cell/Link/Port state system admits the proposed root-identity PASS and triad-switch guards together with genuine TRIADIC_CLOSURE_E consumption, temporal dependency, signed-axis/source-token conservation and rotation interlock. If it does, the current result is a periodic capacity-compatible implementation; if a guard is not admitted, its exact failed clause identifies what must be revised. No primitive-event or Foundation promotion is asserted by this research note.
