# R5: exact optimizer-recourse distance and minimal multi-swap obstructions

Date: 2026-11-14. Scientific input: frozen R5 commit 435e77af0d180eac32bd1f9c4c464bc4010b7551. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Scope: derived one-dimensional integer-event, radius-two, original event-index center observer.

## Reconfiguration observable

For increasing integer events x_0 < ... < x_{n-1}, let Opt_x(K) be the family of all K-element original-index subsets T that cover all events within radius 2 and minimize C_x(T)=sum_t min_{j in T}|x_t-x_j|. Closing one original length-three gap to two shifts the later coordinates by -1 but keeps original event labels.

For any newly optimal K-set S, define its pointwise old-family recovery distance:

    rho_x(S;K) = min_{T in Opt_x(K)} |S \ T|
               = K - max_{T in Opt_x(K)} |S intersect T|.

This counts center replacements, half the symmetric difference. It differs from the minimum *between* the two optimizer families: when the optimal cost is unchanged, the old optimal family is included in the new family, so that latter minimum is zero. A particular new optimum can nevertheless require multiple replacements to return to the old family.

## Theorem: exact lexicographic center-path dynamic programming

**Theorem.** For strictly increasing integer event coordinates with steps in {1,2,3}, a fixed K, and a K-index reference set S, a finite shortest-path recurrence with state (number of centers k, last selected center j) exactly computes

    lexmin_{T: |T|=K, covering-radius<=2} (C_x(T), |T \ S|).

The first coordinate is J_x(K), the second rho_x(S;K). There are O(nK) states, with at most seven possible predecessor indices per state.

**Proof.** Every sorted set T={j_1<...<j_K} has a unique selected-center path. The first center contributes prefix cost sum_{t<j_1}(x_{j_1}-x_t), and the last contributes suffix cost sum_{t>j_K}(x_t-x_{j_K}), each admissible only if the relevant distances are at most 2. Every edge i<j between consecutive centers is admissible precisely when min(x_t-x_i,x_j-x_t)<=2 for every i<t<j, with edge weight sum_{i<t<j}min(x_t-x_i,x_j-x_t). Those prefix, edge and suffix pieces partition all event indices; their weights sum to the exact nearest-center objective.

Add 1_{j not in S} for each center index j selected. Its path sum equals |T\S|. Lexicographic min-plus relaxation therefore finds the exact minimum (primary total distance, secondary number of replacements). For a feasible center path, any pair of consecutive selected centers cannot be at coordinate distance 8 or greater: their radius-two neighborhoods would be separated by a gap of length at least four between consecutive observed events, contrary to the step bound three. Hence only predecessor coordinate differences up to seven need inspection; strict integer monotonicity leaves at most seven predecessor indices. This proves the recurrence and finite sparsity bound.

## Exact minimal counterexamples

**Two replacements: four events.** Let

    x=(0,1,3,6), y=(0,1,3,5), K=2.

Exactly the final length-three gap closes. The unique old optimum is T={1,3}, with total cost 3. The new S={0,2} has radius two and cost 3 at y, but has radius three at x. S and T are disjoint, so rho_x(S;2)=2 despite J_x(2)=J_y(2)=3. Fewer than four indices cannot support two replacements between equally sized subsets: K=1 permits at most one, and two 2-subsets of three indices must meet. Thus four is the minimum cardinality for two replacements.

**Three replacements: seven events.** Let

    x=(0,1,2,3,4,6,9), y=(0,1,2,3,4,6,8), K=3.

The old optimum is unique: T={1,4,6}, with total cost 5. The newly feasible and optimal S={0,3,5} also costs 5 after closing the last gap, while its old covering radius is three. S and T are disjoint, so rho_x(S;3)=3. Exhaustively checking every step word in {1,2,3}^{n-1}, all candidate length-three gap closures and every budget with unchanged optimum cost for 2<=n<=6 proves there is no such three-replacement instance with fewer than seven points in this declared model.

Consequently, a universal existence theorem for a one-swap repair witness does not imply one-swap recovery of every newly admitted optimizer.

## Exhaustive validation and actual frozen R5 continuation

The accompanying Python 3 script directly enumerates all K-center subsets on every step-1/2/3 word of length n=2,...,7 and every one-gap closure. At unchanged-optimum-cost budgets it compares *each* new optimizer to the full old optimizer family, independently crosschecking the exact nearest-family replacement count with the lexicographic DP.

There are precisely 2,005 original-word/single-gap-closure transitions and 31,689 compared new-optimum index sets. The maximum necessary replacements by n=2,...,7 are (0,1,2,2,2,3), with transition counts (1,6,27,108,405,1458). See EXACT_OUTPUT.json for all counts and explicit witnesses.

For the **frozen 954-event R5 input** the script imports the exact deterministic input reconstruction and constrained optimal-center path routine from the parent PR #2398 file at research_notes/brc_r5_universal_cut_15_17_20261114/VERIFY_R5_UNIVERSAL_CUT_15_17.py. At budget K=293 it rebuilds newly admitted optimal witnesses for both original cut indices 15 and 17, with boundary event indices 194 and 245. The independent lexicographic recourse recurrence then verifies:

    J_old(293)=741;
    rho_old(S_15;293)=rho_old(S_17;293)=1.

This provides a separately derived objective-and-recourse computation for two previously exhibited frozen-R5 one-swap witnesses. The small counterexamples are auxiliary exact mathematics, not a claim that the frozen 954-event instance contains a three-swap case.

Run Python 3 from the PR branch:

    python research_notes/brc_r5_reconfiguration_20261114/VERIFY_R5_RECONFIGURATION_DISTANCE.py

The exact output is stored as EXACT_OUTPUT.json. The executed local Python bytes and saved output bytes match their immutable Git blobs. The original parent module remains part of the stacked source branch. No floating-point decisions or external credentials are required. Independent mathematical review: NOT_REVIEWED.

## Next research unit

For frozen gaps 15 and 17, classify the **maximum** of rho_B(S;K) across all S in Opt_{B union {i}}(K), all backgrounds B and relevant K. A path-pair product construction can enumerate membership intersections, but computing max_S min_T requires retaining the max-min quantifier order, rather than minimizing over both paths. Seek an exact small-block decomposition for the 29 original blocks and 17 optimizer-relevant closure bits. The original 2,520-byte certificate, 28-coordinate and 8,192-prefix-query performance objective remains separate.

**Provenance:** frozen input at 435e77af0d180eac32bd1f9c4c464bc4010b7551; Draft PR #2398 (44 all-background one-swap witnesses); Draft PR #2379 (cost-inert gap and optimizer-family results). This is an author-side mathematical contribution; no formal Task CLAIM, independent reviewer acceptance or Result publication is asserted.
