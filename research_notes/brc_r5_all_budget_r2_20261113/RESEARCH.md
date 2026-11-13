# R5: exact all-cardinality radius-2 checkpoint frontier and unit-distance saturation

Date: 2026-11-13. Researcher: EM-DIRECT-C7966D / TASK_RESEARCH. Research-Activity-ID: RA-B1BAA6BB51A820BCC758B3A1.
Frozen scientific pin: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`. Auxiliary BRC rational-certificate observer only. Existing R5 predecessors include Draft PRs #2220, #2290, #2293 and #2299; do not repin scientific data or claim new P000/Result/review.

## Exact problem

Let `x_0 < ... < x_(N-1)` be strictly increasing **integers**, interpreted as cumulative counts of distinct certificate activation events at consecutive complete-wall boundaries. Given a radius `R >= 0` and cardinality `K`, choose exactly K center indices `S` to minimize

`J_R(K) = min_{|S|=K, max_b d(b,S)<=R} sum_b d(b,S)`, where `d(b,S) = min_{s in S} |x_b-x_s|`.

An infeasible K has no optimal cost. This is the full-cardinality, fixed-radius cost frontier, rather than the lexicographic minimum-K solution of #2293.

## Theorem 1: exact unit-distance saturation threshold

For every strictly increasing integer coordinate array of length N and every R >= 1, write D_1 for the minimum number of selected coordinate centers whose closed distance-1 neighborhoods cover all N points, and D_R for the analogous radius-R minimum.

For each integer `K` with `D_R <= K <= N`:

* `J_R(K) >= N-K`.
* `J_R(K) = N-K` **if and only if** `K >= D_1`.

**Proof.** Every selected point contributes zero. Every unselected point has a positive integer distance to every selected point, hence contributes at least one. The K-center sum is at least N-K; equality holds precisely when every unselected point has distance one to a selected point, which together with the selected points is exactly radius-1 domination. A radius-1 dominating set of D_1 centers can be enlarged to any cardinality K >= D_1 by inserting arbitrary remaining points; all others remain within one. Such a set is automatically radius-R feasible for R >=1, proving the converse. The first equivalence also shows strict inequality below D_1 whenever radius-R feasibility holds. No optimality argument, continuity assumption, or BRC-specific property beyond integral event coordinates is needed. QED.

D_R is found by the standard leftmost-uncovered greedy algorithm: among admissible centers covering the leftmost uncovered point, choose the rightmost one; it has the farthest right endpoint. Replacing the first center of any feasible cover by this choice cannot reduce coverage to the right. Induction on the remaining suffix proves minimal cardinality.

## Theorem 2: exact fixed-budget dynamic program

Set `P(t)=sum_{b<t} x_b`. The cost before first center p is `A(p)=p*x_p-P(p)`; the cost after last center q is `Z(q)=P(N)-P(q+1)-(N-q-1)*x_q`.

For adjacent selected centers `p<q`, all interior boundaries are charged to their nearest of those two centers. Define

`C(p,q)=sum_{b=p+1}^q min(x_b-x_p, x_q-x_b)`.

Let `U(p)=max{b:x_b<=x_p+R}` and `L(q)=min{b:x_b>=x_q-R}`. The directed edge p->q is feasible exactly when `L(q)<=U(p)+1`. Under integer strict growth, every feasible edge has `q-p<=2R+1` (at most R+1 integer coordinates covered near each endpoint). Initialize `F_1(q)=A(q)` for centers covering the first point, and infinity otherwise. Then

`F_k(q)=min_{p<q, p->q} (F_(k-1)(p)+C(p,q))`.

Finally `J_R(k)=min_{q:U(q)=N-1} (F_k(q)+Z(q))`. The Voronoi partition of consecutive centers makes these charges additive, so path decomposition and induction prove this recurrence. With cached edge costs, all cardinalities require `O(N^2 min(N,2R+1))` integer arithmetic operations and `O(N+|E|)` working storage (plus output). The procedure uses exact integers; it does not measure a full 28-coordinate prefix-query runtime.

## Exact pinned R5 census (R=2)

From the original 15 signed integer atom coefficients, enumerate all 32,767 nonempty subsets using Gray one-bit updates; group retained `(n,q)` with q=3,12,15, collapse duplicate positive rational `n/q` **within the same q** and retain multiplicities across q. Exactly 953 distinct rational walls yield N=954 boundaries and total 1,065 cumulative events. The radius-2 transition graph has 4,383 edges.

* `D_2=213`, `D_1=351`; **742 feasible exact budgets** K=213,...,954.
* K=213: J=1070 (matches previously saved radius-2 mean-optimal result). K=214: 1064; K=215: 1059; K=220: 1034; K=250: 912; K=300: 720.
* At **K=351** the frontier first reaches J=603=N-K; for all K=351,...,954 it is exactly `J=954-K`, by Theorem 1 (604 explicitly certified budgets without running later DP layers).
* The computed one-center marginal reductions across the 741 transitions have frequency `{1:603,2:36,3:23,4:70,5:8,6:1}`. On this specific frozen instance they form a non-increasing sequence; no universal diminishing-returns theorem is asserted.
* SHA-256 of the 742 ASCII lines in `EXACT_FRONTIER.csv`, excluding header, using `K,J\\n` per line: `1de18dc9b43790c9bcb66e5ba8a88532dfd2de9979ee4d936cef8a1704b3dab9`. Sum of J over all 742 lines = 292961; sum of K*J = 130909193.

## Verification and evidence

Actual local Python standard-library script `VERIFY_R5_ALL_BUDGETS.py` reconstructs all original rational walls, checks the exact coefficients and event multiplicity distribution, builds all 4383 directed edges, computes the 742-point table, and checks against **3,279 fully enumerated** independent small integer arrays/radii (array sizes 1..7, successive gaps 1/2/3, radii 0/1/2). It additionally checks the greedy D1/D2 counts, the saturation threshold, monotonicity, full-line SHA-256 and selected exact costs. A separately written JavaScript dynamic program checked all 742 cost values through their first rows, selected values, edge count, sum(J)=292961, and sum(K*J)=130909193; the Python source and full table are the replayable archived evidence. See `EXACT_FRONTIER.csv`, `EXACT_OUTPUT.json`.

## Remaining unit

Reconstruct the original 2,520-byte seed and full 28-coordinate/2,880-prefix query index in a fresh process, replay 8,192 rational-prefix queries with byte-identical answer hashes across indexed alternatives, and compare cold-start time, RSS, per-query cost and output serialization. The present 742-point frontier optimizes **complete-wall scalar event corrections**, not the original full query workload or the native X6 observer. Formal R5 Task-ID/owner/CLAIM, Result and independent review remain separate.
