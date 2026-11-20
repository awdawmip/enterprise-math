# X6 native time: graded signed-path action, exact return-loop provenance obstruction

Date: 2026-11-21 (Asia/Hong_Kong). Author: TASK_RESEARCH lane `chatgpt-research-onhour-enterprise-math-20260923`, researcher `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`.
Task `RS-X6-NATIVE-TIME-DYNAMICS`; publication `TP2-91D4A7C2F63805BE21A3`; parent `PO-X6-UPPER-STRUCTURE-20260906`.
Status: **AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**.

## Immutable premises and preserved previous results

Frozen taskbook: `f41c2690daba467ecbde99615a1337e67be46ffd:research_tasks/RS_X6_NATIVE_TIME_DYNAMICS_20260906.md`.
Frozen P000 V5: `a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`, and the mandatory joint-relation/observer preservation companion at that pin.
P000 provides six signed native Cell-adjacency directions, Cell torsor over Z^6, the S6 axis-permutation frame skeleton, and temporal ordering of relational change; primitive stability additionally requires a legal three-force `TRIADIC_CLOSURE_E`. Here we work **only with the source-supported coordinate-path vocabulary**, not an admitted physical action/force update law.

Consume the earlier exact frame-quotient notes `X6_TIME_S6_FRAME_SIGNED_AXIS_MIXED_DIAMOND_AND_OBSERVER_QUOTIENT_20261121.md`, `X6_TIME_SIGNED_TRIAD_S6_PORT_OBSERVER_QUOTIENT_20261121_0500.md`, and `X6_TIME_JOINT_TRIAD_PORT_CELL_PROBE_MINIMAL_FRAME_20261121_0600.md`. Consume separately the frozen Viète `VIETE_PHASE_REFINEMENT_VS_PRECISION_PROSTATE_CLOCK_20260905.md` and `VIETE_NATIVE_HALF_TURN_PRINCIPAL_ROOT_BUNDLE_20260905.md`: precision-address refinement and elapsed native event sequence are different arrow types.

## New result 1: exact graded path transformation monoid

Fix an arbitrary chosen Cell coordinate anchor, so a start state is `(x,sigma)` with `x in Z^6` and `sigma in S6`. Define two *typed* generator kinds:

- Signed native local step `U(j,eps): (x,sigma) -> (x + eps * e_{sigma(j)},sigma)`, `j=1..6, eps=+-1`.
- Frame relabeling `R(h): (x,sigma) -> (x,sigma h)`, `h in S6`.

For each ordered word `w`, there exist unique `d_w in Z^6, h_w in S6`, and event-grade counts `n_U(w), n_R(w) in N` such that

`w(x,sigma) = (x + sigma d_w, sigma h_w)`,

with `n_U` counting signed Cell steps and `n_R` counting frame events. For *word concatenation* (first `w`, then `v`), write

`Phi(w)=(d_w,h_w,n_U(w),n_R(w))`.

Then the exact composition rule is

`(d,h,s,r) * (e,k,t,u) = (d + h(e), h k, s+t, r+u)`.

Therefore `Phi` is a monoid morphism from the **ordered event-word monoid** to the graded affine-permutation transformation monoid `(Z^6 rtimes S6) x N^2`, where the grading uses addition and no cancellation. An induction on word length proves the state action and composition formula. Uniqueness of the transformation part follows from its action at `(0,id)`; the counts are determined by the typed word.

### Information meaning

For *only* final Cell, final reference frame, and the two counts, `Phi` is an exact sufficient and future-step-stable summary: the composition rule computes the effect of any appended event word. This is an **explicit observer-safe BRC quotient** for that observer, not a claim that path identity, all prefixes or physical time duration are recoverable. In particular, `n_U` and `n_R` are primitive-event grade counts, not a calibrated physical duration or an extra spatial axis.

The two words `U(1,+) U(2,+)` and `U(2,+) U(1,+)` have identical `Phi` but different first-prefix Cells. Hence an observer allowed to ask for ordered path prefixes does not factor through `Phi`.

## New result 2: sharp provenance lower bound on a fixed endpoint, frame AND event count

For any integer `W>=1`, define an alphabet of twelve signed *return-pair labels* `(i,eps)` for `i=1..6, eps in {+1,-1}`. Such a label represents the **ordered** two-event word `U(i,eps) U(i,-eps)`. Every pair returns to its starting Cell and preserves the frame.

Concatenate `W` pairs and vary their twelve independent labels. All `12^W` resulting event words have **exactly the same** Cell endpoint, final frame, and grades `(n_U,n_R)=(2W,0)`. The map from the W-tuple of pair labels to the entire ordered signed-native step record is injective.

For the explicitly declared future observer that may query these W ordered return-pair labels (or the complete last 2W step record at the known boundary), every distinct W-tuple is distinguishable. Therefore any exact summary for this declared word family requires at least

`N_provenance(W)=12^W` distinct states, or `B_provenance(W)=ceil(W log2 12)` bits.

Storing the W labels attains this bound for **this restricted return-pair population and observer**, so it is sharp. For an unbounded window and an observer retaining arbitrary past pair-label queries, the state requirement grows unboundedly; no fixed finite-state compression of these histories is possible. A weaker endpoint/grade observer can use `Phi`, as proved above. This is precisely a scope-typed distinction between *future endpoint sufficiency* and *BRC ordered provenance sufficiency*.

Examples: `W=1 -> 12 states, 4 bits`; `W=2 -> 144 states, 8 bits`; `W=3 -> 1728 states, 11 bits`; `W=4 -> 20736 states, 15 bits`. These are information-theoretic fixed-width lower bounds; the proof does not rely on timings or floating-point fitting.

## Exact executed finite checks

Checker `research_checks/X6_TIME_GRADED_S6_PATH_AND_LOOP_MEMORY_CHECK_20261121.py`, result `research_checks/X6_TIME_GRADED_S6_PATH_AND_LOOP_MEMORY_RESULTS_20261121.json`.

Enumerated 720 S6 start frames and all ordered pairs of 17 typed generator choices (12 signed steps plus the five adjacent-transposition frame generators), giving **208,080 direct-versus-semidir​ect action comparisons**, all equal. Independently enumerated all `12^W` histories for `W=1..4` and checked same Cell, frame and event grade. A pair of commuting endpoint steps with different first-prefix Cells was checked. Total mismatches: **0**.

These finite executions test the precise formulas, while the preceding monoid induction and injectivity argument prove the parameterized claims.

## Limit, next exact scientific action and carry-forward

The paired signed-Cell moves belong to P000's native coordinate-path language. This note does **not** assert every such pair is admitted as a physical time evolution of the still-open three-force Cell/Link/Port law. To transfer the unbounded-history lower bound to a physical dynamical system, first prove that the selected return-pair family is genuinely admissible with the actual guard/environment update, or prove a new lower bound on its admitted sublanguage.

Next: inspect a pinned, admitted native Cell/Link/Port incidence and physical environment-transition source, if one exists; otherwise advance the task's general **phase/refinement cocycle** using frozen Viète restrictions and keep the admitted-dynamics interface explicitly open. The original R063 six-file benchmark is a separate native experiment and remains unexecuted by this unit.

Source/review: no independent Driver review, formal Result, Foundation promotion or native experiment completion is claimed. Do not redo prior port/frame orbit classifications or the original R063 benchmark under an altered target.
