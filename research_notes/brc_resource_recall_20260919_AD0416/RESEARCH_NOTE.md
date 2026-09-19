# BRC resource-conditioned recall: a source-executed Nollm counterexample

Researcher-ID: `EM-DIRECT-AD0416`
Research-Activity-ID: `RA-37C0A30C7B1F5A338F03D186`
Progress-Event-ID: `brc-resource-recall-20260919-AD0416`
Session: `chat-local-reciprocal-ceec8bd1559acdf8c10ebc9b` (continuing local key, not a platform-authenticated ID).
Status: `RESEARCH_CANDIDATE / SOURCE_EXECUTED_COUNTEREXAMPLE / SCOPED_PROOF / NOT_FOUNDATION`.
User objective: continue the extracted BRC tool into an actual Nollm coverage/recall operation, locate a concrete observer failure, and retain the smallest justified extra state.
Read pins: global `c55ec4fcc642b0244e68e7f8c3e530d46adb6bc5`; EM `c62b1472db2e6ad90e988247f9590e2cf62957e1`; Nollm `88d63b32329fbbcd18028de1ac83b2db3c988e33`.
No new formal Task-ID, CLAIM, independent review, theorem admission, native-axis change or production modification.

## 1. Actual operator and concrete scope

Executed Nollm `packages/nollm-core/src/nollm_core/recall.py` unchanged, including `resolve_recall` AND `_targets`. Its file bytes match Git blob `02c148caad1929a0f72055100b75f806f55a956d`. Nine complete Nollm source files and three complete EM files are hash-checked in the standalone test. Three verbatim coverage-template functions and the existing prime-valuation dependency excerpt are explicitly marked slices, not complete source modules.

The fixture uses actual `GeometryAddress`, `BridgeSpec`, `GeometryAnchor`, `MemoryAtom`, `AtomHandle` and request/budget validation. It supplies synthetic atom/bridge storage and the exact default-profile lateral template data. The six offsets and Q16 allocation come from current `lab/nollm-lab/geometry/compiler.py:_physical_entries`, `compile_support.py`, and `physical_geometry.py:axial_transform_q32`; expansion uses the unchanged Core functions. The entire 86-KB compiled artifact and production storage/runtime were NOT loaded. Dynamic inter-layer coverage and OpenClaw/LLM semantics were NOT executed.

The selected operator uses step-rounded scores, maximum-at-Cell recoalescence, resource-sensitive Bridge permission, beam selection and occupancy readout. It is not a sum-of-positive-masses observer. The earlier affine degree-two moment theorem remains true in its stated lease but is not a complete interface for this operator.

## 2. Three-step resource-loss witness

All cells are `default_dream_v1/default`, layer 0. Let
S=(0,0), A=(10,0), C=(0,2), T=(20,0).
Declare Bridges S->A, A->C and C->T, each weight 65536, per-Bridge max_steps=3 and fanout=1. Put one synthetic memory atom at T. Permit lateral ring 1 and Bridge; start only at S. Request max_steps=3, max_bridge_steps=2, beam=4096, max_layer_delta=0.

At depth 2 the SAME C is reached by:
- bridge,bridge: score 65536, Bridge use 2;
- lateral,lateral: score floor(10923*10923/65536)=1820, Bridge use 0.

Current `merged[target]` retains only the higher score; `best[cell]` also omits Bridge usage. `_targets` cannot extend the surviving label over C->T because two Bridges were already used. The discarded label could do so legally.

Executed outcomes:
- original `resolve_recall`: no returned atom;
- exhaustive legal-path oracle: T at score 1820, kernel word (lateral,lateral,bridge);
- resource-conditioned adapter: same reached-Cell best scores AND tie-selected paths as the exhaustive oracle.

Exhaustive per-depth path populations: 1,7,43,265 (315 generated labels excluding the initial one). All are below beam 4096; this loss does NOT require beam truncation. Original retained frontier widths: 1,7,18,33. Adapter widths: 1,7,26,63. A control raising the request Bridge budget to 3 restores the original three-Bridge score-65536 result.

This disproves future-safety of the Cell/score-only quotient for this declared legal-continuation observer. It does not establish a measured production recall-rate loss, nor claim that bounded heuristic recall promised exhaustive completeness. It is an implementation-level information-loss witness, not evidence that physical geometry or memory semantics are invalid.

## 3. Minimal scoped repair and actual BRC extension

Compose T0 BRC action/provenance semantics with T6 future-safe quotients; specialize to resource-guarded rounded-score actions. No competing top-level family.

A label is (Cell, score, used_Bridges, depth, kernel_word). Spatial coordinates and resources remain differently typed; resource count is NOT an extra spatial axis. At fixed Cell and depth, keep a resource-conditioned antichain instead of a single winner.

For the score-only observer, label L dominates R if
used(L)<=used(R) and score(L)>=score(R).
For the score AND selected-path observer, additionally require
word(L)<=lex word(R).

Assumptions: fixed environment, finite horizon, state-independent edge weight once Cell/edge is selected, monotonically permissive Bridge guards (lower prior use admits every edge admitted from higher use), identical edge resource increments, and no beam approximation. These are the relevant `_targets` rules for the selected fixture. Do not silently extend to history-dependent weights, changing occupancy or arbitrary resource predicates.

Proof: any suffix admitted from R is also admitted from L, inductively preserving the resource inequality. Each integer map f_w(s)=floor(s*w/65536) is monotone, so score inequality is preserved. Equal-depth prefix words have the same length; their lexicographic order is preserved under appending the same suffix. Hence a dominated label cannot improve any later reached-Cell maximum score, or its selected path under the stronger rule. Repeating the quotient at each depth preserves the corresponding bounded-path observations. No pruning between different depths is assumed.

For score-only queries, at most B+1 labels per Cell per depth suffice: keep the greatest score for each usage 0..B and remove dominated resource entries. For exact tie paths, at most (B+1)(65536+1) score/resource classes suffice before further dominance: within an identical pair keep only the smallest equal-length word. This is a finite bound, NOT constant bit memory, a tight complexity bound, or a practical bound on number of reached Cells. Current path strings also cost O(depth) storage. A frontier cap raises an explicit error rather than silently clipping a beam.

Generic necessity: remaining budgets r=0..B are pairwise distinguishable by Bridge-only legal-continuation words. If r<s, a word of r+1 Bridges fails from r but succeeds from s. Thus B+1 live resource classes are necessary for that universal continuation language. A fixed graph/horizon can need fewer. Executing unchanged T6 with B=5 gives class counts 2,3,4,5,6,7,7, including one failed state. This is a task-relative minimum, not a universal hidden-state inventory.

## 4. Two additional observer barriers

### A. Moments are not maximum scores

Executed the extracted `enterprise_math.brc_transport` file, blob `be1debe367263931bd5e93fd750be3ed54624fe1`. Two packets at the same six-axis coordinate, weights (3/4,1/4) versus (1/2,1/2), have the same 28-entry spatial moment AND count 2, but dominant weights 3/4 versus 1/2. The existing weight-histogram observer distinguishes them. No fourth or sixth spatial moment can repair this same-position maximum query; choose the correct branch observer instead.

### B. Step rounding is an action, not an associative scalar product

Let x circle y=floor(x*y/65536). For a=b=65535,c=32768:
(a circle b) circle c=32767, while a circle (b circle c)=32766.
Do not flatten/regroup rounded weights as an ordinary semiring product. Keep the composed monotone integer actions f_w; function composition is associative. The reference `RoundedWord` keeps the weight sequence and may materialize its 65537-entry finite score table at an explicitly stated cost. None denotes unreachable; integer score zero remains a reachable state, matching source behavior.

There is a further path-tie witness: same Cell/depth/resource, score 2 with word (bridge,lateral), score 3 with word (lateral,bridge). Weight 16384 sends both to 0. The lower original score then supplies the lexicographically smaller final word. A score-only skyline is correct for maximum scores but not sufficient for exact tie-selected paths. The stronger antichain retains this distinction. No positive-mass cancellation or path-multiplicity preservation is inferred from max recoalescence.

## 5. Execution, reuse and boundary

10 check groups PASS: 12 complete source byte identities; actual-source recall witness; budget control; executed BRC moment/max collision; Q16 nonassociativity and 65536 monotonicity comparisons; rounding/tie witness; executed original T6 minimum-resource partition; 180 finite random resource-guarded transition systems compared to independent unpruned path enumeration (8556 generated path labels); 800 input-order antichain checks; 6 invalid-input rejections. Compilation passed.

Reuse resolution: T0 extracted affine/histogram interface `REUSE_EXECUTED` for the failure audit; T6 `REUSE_EXECUTED` for predictive resource classes; existing action/provenance and resource-precision laws `COMPOSE_APPLIED`; new `brc_resource_recall.py` is a narrow research-domain adapter, `EXTEND_EXISTING_TOOL`, not a novel minimization family. Path enumeration is an algorithmic cross-check, not an independent mathematical reviewer.

No full project test suite, independent review, Lean proof, Nollm deployment, actual-user memory mutation, semantic recall benchmark or full inter-layer coverage result is claimed.

## 6. Next exact frontier

The selected no-beam legal-continuation unit is closed by an exact witness, adapter and proof. Next test finite-beam semantics explicitly: Cell budget versus label budget; a beam is a coupled selection operation and invalidates any blanket claim that local antichain preservation alone proves whole-runtime equivalence. Then add current dynamic coverage as a frozen callback and measure retained-label growth. Do not restart the 5/7 experiments or replace the field with an external semantic graph. Moving this candidate into production requires Nollm's ordinary runtime/storage regression and admission, not just this EM research note.

Classical comparison (not novelty claims): Bhaduri, arXiv:2109.00732, weighted-language/bisimulation observer distinctions; Sadykov, Uchoa, Pessoa, Transportation Science 55(1), 2021, resource-constrained path labeling. No external source is needed for the elementary witness or monotone-action proof above.
