# R710s — Four-phase port-serializable BRC X6 ring

Date: 2026-11-11 Asia/Shanghai. Independent author-side research candidate, UNREVIEWED. Parent task RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142. Scientific pin unchanged: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000 V5, signed X6 and triadic foundations). Direct predecessor R709b@15057fffe4aef6610e8686b20495771cd071f8ef. R707/R708 supply earlier labelled holonomy families.

## 1. Exact question and declared interface

For m=6(k+l) even, R709b uses a labelled ring of X6 triad symbols with original positive BRC source-labelled packets A,a,B,b, and two independent nonnegative token inventories n_i^+,n_i^-. On edge i between Cells i and i+1 mod m, freeze the OLD-state indicator f_i: endpoints are Johnson-adjacent, n_(i+1)^+>=1 and n_i^->=1. Each fired edge posts two typed V29-style TRANSFER occurrences: + from i+1 to i, and - from i to i+1. The Cell triad update is old-neighbour copy at fired edge, otherwise hold.

Can the paired transfer macrostep be executed using single-token events with at most ONE incident event per Cell per substep? Find its optimal substep count under full firing, and investigate nonuniform stocks.

## 2. Theorem — exact four-phase serializability, optimal at full firing

For every even m>=4, arbitrary old triad labels and nonnegative inventories, choose all f_i from one frozen old-state snapshot. Run exactly four transfer substeps:

(1) even-indexed fired edges, +; (2) even-indexed fired edges, -;
(3) odd-indexed fired edges, +; (4) odd-indexed fired edges, -.

After the four phases, commit the triad copy using the original snapshot and the same f_i. The resulting inventories are exactly

\[
n_i^{+\prime}=n_i^+ + f_i-f_{i-1},
\qquad
n_i^{-\prime}=n_i^- - f_i+f_{i-1}.
\]

Every Cell preserves the integer sum n_i^++n_i^-, and both global species totals are conserved. The completed V29-style port ledger counts both opposite positive typed occurrences; their signed physical edge current is zero at each completed macrostep boundary.

**Proof.** Edges of even index form a vertex-disjoint matching when m is even; so do odd edges, including the wrap-around edge m-1. No Cell participates twice in a phase. Each Cell sends at most one + token, from its unique + outgoing port, and at most one - token, from its unique - outgoing port, per frozen macrostep. Each selected old-state f_i guarantees the relevant source had at least one token. Before that species' only outgoing event, incoming events can only add tokens, hence no overdraft regardless of phase order. Summing additive typed event increments gives the two exact formulas and the original simultaneous V29 ledger. The final old-state triad copy matches the R709b macro map. Positive BRC source weights are never treated as signed amplitudes. QED.

**Sharp lower bound.** If all m edges fire, each Cell participates in TWO physical incident edges, each with TWO typed transfers. Therefore every Cell participates in four distinct elementary events. Under the declared restriction of at most one incident event per Cell per substep, any implementation needs at least four substeps. This four-phase construction attains four. The four substeps are a deliberately declared logical event refinement, not four proven physical heartbeat intervals.

## 3. Theorem — a complete nonuniform full-speed inventory family

Let W be any R709b cyclic positive source-labelled BRC word, and let p_i,q_i be arbitrary nonnegative integers. Initialize the old-state-compatible triad field X_i=S_i along W and

\[
n_i^+=1+p_i,\qquad n_i^-=1+q_i.
\]

All edges fire in every macrostep. The inventories remain constant, and for all integer t>=0,

\[
X_i(t)=S_{i+t\bmod m}.
\]

Proof: at t=0 the packet sequence is pairwise Johnson-adjacent and all required sources have tokens. Theorem 2's displayed updates with f_i=1 have zero increments at every Cell, and the triad copy shifts the entire cyclic word. Induct on t. The full completed V29 ledger and pointed S3 holonomy after m layers are identical to the uniform-stock R709b case. In particular all three S3 outcomes for k,l>0 persist for an unbounded family of genuinely nonuniform stocks. QED.

## 4. Scoped stock-fiber theorem

Observe the complete committed native triad trace, full V29-style typed counters, pointed S3 result, and the two GLOBAL inventory totals, but not individual Cell inventories. Write P_+=sum_i p_i and P_-=sum_i q_i. The compatible positive-inventory raw-state fiber has exact size

\[
F(m,P_+,P_-)=
\binom{P_++m-1}{m-1}\binom{P_-+m-1}{m-1}.
\]

Proof: independent weak compositions of the two surplus totals give a bijection with all nonnegative p and q. By the preceding theorem all have identical declared committed observer traces. For m=12 and P_+=P_-=1, F=144, requiring ceil(log2(144))=8 bits to recover the **raw local stocks**.

For predicting ONLY future observations under the unperturbed four-phase scheduler at macrostep boundaries, these stock states stay observationally equivalent indefinitely; no stock-distribution repair bits are needed for that narrower prediction. Future individual stock probes distinguish raw states. This is a scope-typed fiber certificate, not a global erasure of stock provenance.

## 5. Executable finite verification

The accompanying R710S_FOUR_PHASE_BRC_VERIFY.js is a deterministic exact-integer positive-source BRC enumeration and discrete-event checker; it verifies frozen-gate vs serial event equivalence, the disjoint-port matching, nonnegative stocks, local/global conservation, full field rotation, V29-type ledgers, and the inherited V17/V39 S3 histograms.

Exhaustive for the four declared word populations (k,l)=(1,1),(1,2),(2,1),(2,2): 2,904 oriented source-labelled packet words, 67,248 committed macro layers, 3,143,232 serialized elementary transfers, all tests passed. Additional checks: four unbounded-slack examples for one full orbit each, plus 972 partial-stock layers (81 perturbed stock seeds times three steps in each of four populations). Exact case-by-case outputs are in R710S_FOUR_PHASE_BRC_RESULTS.json. No floating phase, trigonometry, π or non-BRC classical propagation was invoked.

## 6. Research state and next executable unit

This is a new typed prepare/commit extension to the R709b candidate dynamics; real native Link/Port event-time capacity and rollback permissions have not been identified with this extension. The physical-edge signed current is zero at completed macrostep boundaries; within an individual one-direction transfer substep it can be nonzero. Macrostep, substep and heartbeat are separately typed.

The native Enterprise Math gateway returned BACKEND_IDENTITY_CHECK_UNAVAILABLE, operation_sent=false, during this research turn, so Source-issued Researcher-ID/activity and canonical task-owner state cannot be freshly verified. Existing active ownership is not changed; this is only a branch/PR author-side research artifact.

Next: read exact frozen Source Link/Port capacity and V29 timing semantics, then test whether a four-phase frozen-prepare/commit block is a permitted native event bundle; otherwise construct the minimal escrow or rollback semantics and rerun the native reachability/holonomy witness. Preserve original source labels and event microstep observer when relevant.
