# R750 — Actual V1R internal-state witness and correction of R749 closure-observer claim

Date: 2026-11-12. Task RS-X6-TRIADIC-CLOSURE-DYNAMICS. Run RUN-aea48b2b684b1204bf7fd828, generation 1, checkpoint revision 2 before this update. Researcher EM-X6-BD7DE5. CLAIM MCP-aa543cb564e2a231d3fe6017.
Status: author-side exact finite theorem and corrected proof scope; not a native coupled-event authorization or independent mathematical acceptance.
Frozen P000 source: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.

## Read sources and their authority
- research_notes/X6_CELL_TRIADIC_PORT_FRAME_INTERNAL_STATE_V1_20260906.md, main, V1R corrected: 960 ordered signed frames and deterministic SHELL/CLOSURE C12 transition.
- research_notes/X6_UPPER_TYPED_EVENT_INTEGRATION_V1_20260906.md, main: typed event source/target, concrete path and internal update are separate fields; event composition only on matching decorated states.
- research_notes/X6_ATOMIC_TRIADIC_PASSAGE_DRIVES_ODD_HOLONOMY_V27_20260906.md, main: one unit directed 3-cycle creates rank-2 antisymmetric passage; a declared ingress/egress bias yields a deterministic active-triad successor, not a complete autonomous Cell network law.
- research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md, main: PASS and TRANSFER update nonnegative count ledger only.
- research_notes/X6_CYCLE_CURRENT_S3_OPERATION_SAFE_PORT_V39_20260906.md, main: (j,h) quotient safe only for declared based-loop language.
- R747 and R749 author-side documents, not independent reviewed source.

## Theorem A: legal SAME-ledger distinct internal modes, without invented closure truth
Fix a native Cell c, a valid ordered signed three-axis frame F, and the same nonnegative V29 count ledger L=0. V1R explicitly declares two internal states (F,SHELL) and (F,CLOSURE). Their V29 ledger is identical because V1R mode is separate internal decoration; they are distinct and have distinct next-state modes under the declared V1R map:
  T(F,SHELL)=(F,CLOSURE)
  T(F,CLOSURE)=(R_can(F),SHELL).
Therefore the projection (L,F,mode)->L is not sufficient to reconstruct the declared mode or its exact next-state readout. There are exactly 960 such same-ledger pairs.

IMPORTANT: V1R's mode label CLOSURE is not, by itself, an explicit theorem that TRIADIC_CLOSURE_E is true in that mode and false in SHELL. The two-mode construction is a real native internal-state witness, but NOT a proof of differing TRIADIC_CLOSURE_E truth values. R749 theorem 2, as originally phrased with arbitrary true/false closure labels, lacks an admissible same-ledger counterexample in the inspected contracts. Replace it by this narrower mode-observer theorem; the stronger closure-truth assertion remains UNPROVED.

## Theorem B: exact period of all declared internal states
The V1R generator R_can cyclically rotates ordered axis slots and reverses token signs. It has exact order six on every signed frame. V1R T alternates SHELL/CLOSURE and applies R_can every second step, hence all 1920 states have exact period twelve and split into 160 C12 cycles. This is a native DECLARED internal law, not a new ad hoc permission rule.

## Theorem C: precisely scoped coupling gap
V29 PASS(x;a->b) updates M_x[a,b] by +1 and leaves other ledger entries unchanged; V1R T updates a declared internal mode/frame. Both are independently well-typed operations on their own domains. Neither source declares a single primitive coupled event E:(L,F,mode)->(L',F',mode') that must apply both, nor a source-preserving mapping from an R748 chosen signed port substitution to a specific allowed Cell-to-Cell Link/Port incidence. The general upper typed-event integration supplies the RECORD SHAPE for such an event, not an unconditional event-existence axiom.

A CONDITIONAL product event can be defined on an explicitly admitted compatible domain D by E(L,F,m)=(PASS(L),T(F,m)). This deterministic map is algebraically valid and preserves the declared mode transition and V29 scalar Q, but its native permission and TRIADIC_CLOSURE_E certificate are not established by the inspected sources. If a future permission predicate G(L,F,m,edge,source) and closure-preservation predicate K are specified, the exact admissibility test is G and K, not count conservation alone.

R748 adaptive selector: a chosen branch must be a declared allowed signed-port Link/Port incidence and have source/target closure witnesses; no exact R748 source was verified in this turn, so no claim is made that any of its candidate branches passes this guard.

## Reproducible exact finite verification
Companion R750_V1R_MODE_WITNESS_VERIFY.py enumerates 6*5*4*8=960 frames and 1920 states, checks all exact period-12 orbits and the 960 same-ledger distinct-mode pairs. Executed with Python integer/tuple enumeration; output:
{"result":"PASS","framed_states":960,"declared_internal_states":1920,"period_histogram":{"12":1920},"same_V29_ledger_distinct_V1R_mode_pairs":960,"closure_truth_counterexample_proved":false,"coupled_V29_C1_event_authorized":false}

## Next precise research unit
Find an explicit declared predicate for coupled Cell/Link/Port events and a TRIADIC_CLOSURE_E preservation certificate. If absent, test the conditional product event with a fully typed source, signed port edge and witness, explicitly marking that as a proposed extension rather than already-authorized native dynamics. Preserve R747/R748 branch provenance.
