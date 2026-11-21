# X6 Native Time — Unit242: exact shared-ring triadic exclusion and collective winding lock

Date: 2026-11-21 (Asia/Hong_Kong). Status: **AUTHOR_PROVED / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED**.

Parent: `PO-X6-UPPER-STRUCTURE-20260906`; Task `RS-X6-NATIVE-TIME-DYNAMICS`, publication `TP2-91D4A7C2F63805BE21A3`. Original on-hour research lane `chatgpt-research-onhour-enterprise-math-20260923`. Original recorded author Researcher `EM-X6-FB6990`, Session `MCP-082892eb480e45dea6d4b9fcc0491034`; these are historical source-attribution values, **not assertions of a live CLAIM or newly authenticated execution**.

## Frozen foundations and independently authored comparison

Pinned scientific source: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`, P000 signed-six-axis Cell torsor, native three-axis STAR as a **chosen relative slice**, and frozen source-proved `research_notes/VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md`. A native primitive event is one signed axis step. The six-axis space, 120-degree enterprise orthogonality, full joint/ordered BRC event provenance and chart-independent Cell identity are preserved.

Independently authored 2026-11-18 guarded triadic candidate: `research_artifacts/mcp/RS-X6-NATIVE-TIME-DYNAMICS/MCP-456b8f22a648400585024ffbcc1c2c94/5a04daccb6795e494dbc/X6_TIME_GUARDED_TRIADIC_RESOURCE_CONFLICT_20261118.md` at `f41c2690daba467ecbde99615a1337e67be46ffd`, Git blob `66b3a856b3c566512ada2c2201c6888b06cb0bbc`. It supplies occupied-source/empty-target and intact force-triad guards as a **conditional** model. Unit240 established a necessary signed-direction repair to its positive-only Port alphabet; Unit241 treated a single movable whole triad. This unit studies **shared finite-ring resource interaction**, not a replacement physical update law.

## Declared signed native C12 resource model

Choose relative Cell anchor P and native directions `e1,e2,e3`. Define `a0=e1,a1=e2,a2=e3,a3=-e1,a4=-e2,a5=-e3` and `a_(r+6)=a_r`. The twelve pairwise distinct frozen OUTER Cells are

\[
x_{2r}=P+a_r,\qquad x_{2r+1}=P+a_r+a_{r+1}\quad(r\bmod6).
\]

Every `x_q -> x_(q±1 mod12)` is a signed native primitive axis event. Now allow **k distinct labeled intact nonzero force triads** `F_i` (each a declared `TRIADIC_CLOSURE_E` payload), with `2 ≤ k ≤ 12`, one per occupied Cell, with all required directed signed Ports available. A serial atomic event may move exactly one whole triad along one ring edge if and only if its target Cell is empty; its label, force-token identities, sign, branch/STAR and chronological provenance remain recorded. No shared Cell, force-token splitting, bypass, stacking, parallel swap or off-ring staging is part of this model.

The native physical Port/environment permission for such updates is still an unadmitted assumption. An available ring Port here denotes a **candidate** signed Port, not an actually measured transfer.

## Theorem A — exact observer cocycle and impossible opposing closed loops

Let `q_i(t) in Z/12Z` be the ring-phase address of the distinct labeled triad i. For any ordered pair `i != j`, retain the **joint directed cyclic gap**

\[
D_{ij}(t)=\bigl(q_j(t)-q_i(t)\bmod12\bigr)_{\{1,\dots,11\}}.
\]

Let `L_i(t)` count i's forward ring events minus reverse ring events from the same starting observation. **For every allowed serial trajectory and every pair**

\[
\boxed{D_{ij}(t)-D_{ij}(0)=L_j(t)-L_i(t).}
\]

**Proof.** A move of a third triad changes neither side. Moving i one step `s=±1` changes the gap by `-s`; moving j changes it by `+s`. A wrap from 1 to 0 or from 11 to 12 would occupy the other triad's Cell and is disallowed by the empty-target guard. Consequently each legal move has exactly the asserted *ordinary integer*, not merely modular, difference; induction proves the identity. This certifies the joint observer without factoring away path ordering.

In particular, `|L_j(t)-L_i(t)|≤10` for arbitrary horizon. If all labeled triads return to their exact starting **native Cells**, then each `L_i=12w_i` for an integer winding `w_i`, every gap returns to its initial value and hence

\[
\boxed{w_1=w_2=\cdots=w_k.}
\]

Thus two independent prescribed OUTER full loops with `w_A=+1, w_B=-1`, or one completing a loop while another returns without one, are **jointly infeasible** under shared single-occupancy ring guards, even though each isolated single-triad cycle is possible and all signed Ports are assumed available. This is a guarded *joint-executability* obstruction, not an additional causal precedence hypothesis.

## Theorem B — sharp complete classification of feasible windings

For `2≤k≤11`, the exact attainable closed-return winding vectors are

\[
\boxed{\mathcal W_k=\{(w,\ldots,w):w\in\mathbb Z\}.}
\]

Necessity is Theorem A. For sufficiency, at least one ring Cell is empty. To translate all k labels forward once without collision, process each maximal consecutive occupied run from its forward end (nearest a vacancy) backward; every target is empty when its token moves. Repeat for every run. Every triad moves exactly one primitive forward edge, producing global translation `q_i -> q_i+1`. Repeat 12 times: each returns to its original native Cell with winding +1. Reverse the procedure for -1 and concatenate to achieve every integer common winding. All three force tokens of each labeled triad remain intact.

For `k=12`, every ring Cell is occupied; **no** single-triad move is enabled, so the only winding vector is the zero vector. With one triad, there is no inter-triad coupling (covered by Unit241).

This is a strict sharing correction to a naive product of independent per-triad C12 histories. It does not assume a physically admitted multi-triad rule.

## Exact finite verification

The executed pure-JavaScript integer checker below examines all 12 distinct native C12 Cells and 24 oriented signed native edges; all `12*11=132` ordered two-triad states and their 528 candidate one-triad ± moves; precisely **480 legal directed transitions** and **48 target-occupied rejections**. It verifies the integer gap cocycle for every legal transition.

It then tests **all 4,082 nontrivial occupancy masks with 2 through 11 labeled triads** (labels assigned by initial cyclic Cell position), and for each mask constructs **both** clockwise and anticlockwise full-return schedules: **8,164 closed witnesses**, with **589,248 actual guarded signed primitive transfers**. Each transfer is checked against the frozen X6 C12 native Cell coordinates, occupancy and exact final label/winding. Total **2,455,890 exact assertions; zero failures**. This checks the constructive cases, while the above algebra establishes the all-integer universal statement.

Checker: `research_checks/X6_TIME_UNIT242_MULTITRIAD_C12_EXCLUSION_WINDING_CHECK_20261121_2000.js`.
Machine-readable exact result: `research_checks/X6_TIME_UNIT242_MULTITRIAD_C12_EXCLUSION_WINDING_RESULTS_20261121_2000.json`.

## Immediate scientific implication and next discriminator

The single-triad signed-Port sufficiency in Unit240–241 **does not tensor into independent multi-triad loops**. A physical model claiming independently opposite spinor-selected rotations for multiple intact triads must specify a genuinely different allowed resource/operation: an available off-ring path, an inter-cell exchange, multiple occupancy, a different Port guard, or explicit environmental bypass. Each has different BRC native-event history and must be verified on its own. An off-ring detour does **not** count as the same frozen OUTER trace.

Next exact evidence: obtain Source-admitted multi-triad Cell/Link/Port resource and signed guard transitions, then test whether a shared native loop admits two opposite independently closed trajectories without violating recorded force-token/Cell provenance. Pair the test with the separate C12/C24 before-and-after precision readout in Unit241: the gap witness is an observable resource constraint, not a substitute precision sensor. Reuse previously completed Units233–241; do not replay failed Native PROGRESS or typed prepare from support issue #2903. Distinct R063 six-file native benchmark remains in `RS-X6-LEGACY-PLANE-RECONCILIATION` and is not part of this certificate.

**Evidence scope:** conditional model proved; no current winning Native CLAIM, semantic PROGRESS, independent Driver review, Result acceptance or physical Port admission asserted.
