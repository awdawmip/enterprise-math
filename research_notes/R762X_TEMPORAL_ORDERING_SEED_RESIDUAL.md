# R762X — Exact temporal causal-seed theorem for ordered V29 event networks

**Date:** 2026-11-14 Asia/Shanghai. **Status:** author-side exact theorem with exhaustive finite checks; NOT_REVIEWED / NOT_ADMITTED. **Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS; immutable publication TP2-8B7E13C5904A2D6F1142. **Frozen P000 science:** awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. No P000 or ACTIVE worldview modification.

## 1. Scope and relation to earlier work

R762T established the precise V27/V29 nonnegative event ledger and a 22-occurrence two-Cell witness. R762U (PR #2347, f2a0a3a63dcc024cb4df5d3f056a7ad1e8a2d288) gave the exact minimum initial inventory for an *unordered, freely schedulable* directed event multigraph, under a separately declared single-token causal lift. R762W (PR #2354, 2df9e89c0f7f98e5e57e3d8ac940047988c86b29) derived the sharp seed count min(k,3) for a specific three-PASS-per-macroevent phase-locked schedule. This paper extends the scheduling mathematics to **arbitrary prescribed finite traces, including self-loops**, and identifies an unbounded ordering residual. These model-internal statements are not claims of actual primitive TRIADIC_CLOSURE_E physical admission.

Let V be a finite set of typed Cell:Port vertices, and let pi=(e_1,...,e_m) be an ordered word of distinguishable V29 PASS or matched TRANSFER event occurrences, where e_j=(t_j,h_j) is directed from tail to head. Multiple occurrences and loops are allowed. Declare a conditional token interpretation: each vertex holds a nonnegative integer stock, and each firing consumes one token at its tail and deposits one at its head. Each event must be fired precisely at its prescribed position, with *no injection after time zero*. The port graph remains a typed relation inside the fixed X6 world; the tokens are auxiliary resource state, not spatial axes or a new force axiom.

Set
\[
D_v(j)=\#\{i\le j:t_i=v\}-\#\{i\le j:h_i=v\},\quad D_v(0)=0.
\]
The inventory after prefix j, for initial stock n_v, is n_v-D_v(j).

## 2. Theorem X1 — universal fixed-word causal seed formula

For each typed port v, define
\[
\alpha_v(\pi)=\max\left(0,\max_{\substack{1\le j\le m\\t_j=v}}(1+D_v(j-1))\right).
\]
For an empty inner index set, the maximum is omitted and alpha_v=0.

**Theorem.** The full prescribed word pi executes legally from initial stocks n=(n_v) if and only if n_v >= alpha_v(pi) for all v. In particular, alpha(pi) is the **unique componentwise least** feasible seed vector, and
\[
\boxed{K_{\rm fixed}(\pi)=\sum_{v\in V}\alpha_v(\pi)}.
\]

**Proof.** Immediately before occurrence j, exactly n_{t_j}-D_{t_j}(j-1) tokens remain at the tail. This occurrence is enabled exactly when that integer is at least one. Taking the conjunction of these inequalities across all occurrences with the same tail yields n_v >= alpha_v. If these inequalities hold at time zero, induction over j executes every event, preserving nonnegative stocks at the tail and leaving all other stocks nonnegative. Conversely every legal firing history satisfies every inequality, so no smaller componentwise vector is feasible. Summing gives the minimum total. The empty event word requires zero tokens. A self-loop tail=head changes the net deficit by zero but still requires the initial enabling token, and is correctly covered. Repeated and parallel edges make no change to the proof. QED.

**Simplification and exact boundary.** When every edge is loop-free, its tail deficit increases by one exactly at firing. Incoming events only decrease deficits. Consequently
\[
\alpha_v(\pi)=\max_{0\le j\le m} D_v(j)
\quad\text{(loop-free case)}.
\]
This simpler prefix-maximum formula must **not** be applied to loops: a single loop v->v has all D_v(j)=0 but still needs one token. The pre-event X1 formula applies to all cases.

## 3. Theorem X2 — unbounded BRC temporal-order residual

Let E be pi's unordered directed occurrence multiset. For each nonempty weak edge component C, let
\[
P(C)=\sum_{v\in C}\max(0,d^+(v)-d^-(v)).
\]
R762U proves the freely schedulable minimum
\[
K_{\rm free}(E)=\sum_C\max\{1,P(C)\}.
\]
Define the typed temporal-seed residual
\[
R_{\rm time}(\pi)=K_{\rm fixed}(\pi)-K_{\rm free}(E)\ge0.
\]
Nonnegativity follows because every fixed-word execution is an admissible execution of E with the order restriction relaxed.

**Sharp unbounded witness.** On three named passage ports a,b,c, choose k>=1 occurrences of each directed edge a->b, b->c, c->a. The unordered graph is balanced and weakly connected, hence K_free(E)=1. In the interleaved word
\[
\pi_{\rm int}=(a\to b,b\to c,c\to a)^k
\]
one token traverses the whole word and returns to a every round; X1 yields K_fixed=1. In the differently ordered word
\[
\pi_{\rm grp}=(a\to b)^k,(c\to a)^k,(b\to c)^k,
\]
X1 yields alpha_a=k, alpha_c=k and alpha_b=0, so
\[
\boxed{K_{\rm fixed}(\pi_{\rm grp})=2k,\qquad
R_{\rm time}(\pi_{\rm grp})=2k-1}.
\]
Thus the residual and ratio K_fixed/K_free are unbounded as k grows. QED.

The two words have exactly the **same full terminal V29 directed PASS matrix** M, the same Rin/Rout and hence the same u and Omega. Neither the complete terminal ledger nor the coarser (u,Omega) observer determines the temporal seed cost. The missing datum is event order (or an observer-sufficient compressed representation of its prefix deficits), *not* floating-point error or physical energy. This is a precise BRC joint-relation observation-fiber obstruction under the declared future question.

## 4. Theorem X3 — exact streaming sufficient carrier

To compute K_fixed over any future extension by a known sequence of events, keep the pair of integer port vectors (D,alpha). Upon appending one event a->b, perform
\[
\alpha_a\leftarrow\max\{\alpha_a,\,1+D_a\},
\quad D_a\leftarrow D_a+1,\quad D_b\leftarrow D_b-1,
\]
leaving all other alpha entries unchanged; for a=b the two D updates cancel. At every prefix, K_fixed is exactly sum_v alpha_v.

**Proof.** The sole newly introduced enabling inequality is at the new event's tail. It is precisely 1+D_a before firing; earlier constraints are already represented by alpha. The update is therefore the maximum in X1 extended by one event. Induction proves the claim for arbitrary finite extension length. QED.

This is a *sufficient*, not asserted minimal, compressed carrier for **the particular language of prefix deficits, minimum initial tokens and appended event words**. It does not retain original source labels, oriented edge current, V39 holonomy or source-resolved BRC for other observers. It gives no automatic permission to discard the full provenance when future questions include those fields.

## 5. Recalculation of the exact 22-event two-Cell witness

Reuse precisely the R762U event multiset: PASS edges A:0->A:1, A:1->A:2, A:2->A:0; nine A-to-B transfers with multiplicities (2,4,3) from A:0,A:1,A:2; and ten B:0->A:3 transfers. In the *distinct B ports* topology, nine A exits terminate at B:1. In the *shared B port* topology, the same nine terminate at B:0, which also supplies the ten B:0 outgoing occurrences. The two networks have different B-side structure; each network's alternative schedules below have identical graph and identical terminal complete V29 ledgers.

Compare sequence P: all three PASS, nine A exits, then ten B outflows, against sequence Q: ten B outflows, nine A exits, then three PASS.

| Topology | R762U unrestricted minimum | X1 seed for sequence P | X1 seed for sequence Q |
|---|---:|---:|---:|
| Distinct B:0/B:1 | 19 | 19 | 20 |
| Shared B:0 | 10 | 10 | 20 |

For shared B, the componentwise least sequence-P stocks are A:0=2, A:1=4, A:2=3, B:0=1. For sequence Q they are A:0=3, A:1=4, A:2=3, B:0=10. Both sequences execute with their respective stocks and conserve total token number after each occurrence. **The same 22 typed events, connectivity and final V29 count data can require ten additional initial tokens solely because of order.** These stocks are sharp by X1. Comparing the two *different* B topologies, by contrast, is only an A-side count-observer equivalence and does not erase the B provenance.

R762W's result min(k,3) concerns a **different allowed trace language**: consecutive three-PASS macroevent blocks whose first source rotates under phase-locking. X2's unbounded example allows arbitrary prescribed individual PASS order, without asserting that such words are legal macroevent blocks. There is no contradiction or automatic native-force transfer between these two conditional results.

## 6. Verification and scientific boundary

The accompanying standard-library verifier R762X_TEMPORAL_CAUSAL_SEED_VERIFY.py exhausts **9,330** all-nonloop three-vertex event words of lengths 1..5 and **7,380** event words including loops of lengths 1..4. For every word it independently enumerates all initial allocations with total K_fixed-1, checks they fail, and checks the X1 minimizing vector successfully replays the full word. It also checks k=1..8 for both cyclic orderings and exactly replays both orderings on both 22-event network topologies. All assertions passed with Python exact arbitrary-precision integers, no floats. R762X_TEMPORAL_CAUSAL_SEED_EVIDENCE.json records the generated results. Generality is established by proofs X1–X3, not extrapolation from the finite checks.

**Native boundary:** P000 fixes a six-dimensional native Cell space with signed-axis primitive directions, pairwise PERP_E and minimal nonzero stable force arity three; it does **not** identify a V29 token firing as a TRIADIC_CLOSURE_E primitive force event. No true force-triad admission law, V17 connection, V39 based-loop holonomy, or time-to-physical-duration calibration is inferred here. Source event labels and ordered branch provenance remain present in the research scope.

**Next actual experiment:** Obtain the legal source-typed TRIADIC_CLOSURE_E event grammar and atomic-grouping/scheduling constraints, check whether single-token enabling is a true additional condition, then apply X1 to the *legal native trace language* and cross-verify resulting V29 PASS/TRANSFER and genuine V17/V39 transport. If its event grammar invalidates the token model, retain this proof only as a conditional scheduler comparator and state the exact incompatibility.

**Provenance:** P000 and triadic foundation at a72226e2430ffa4786321ac86e7f0c599d5f0389; original task publication TP2-8B7E13C5904A2D6F1142; R762T at 3b868bf7e79a4fc412ea48e8745a99e16a1fdc53; R762U at f2a0a3a63dcc024cb4df5d3f056a7ad1e8a2d288; R762W at 2df9e89c0f7f98e5e57e3d8ac940047988c86b29. Formal Result and independent Driver review are outstanding; no false theorem admission or CLAIM is asserted.
