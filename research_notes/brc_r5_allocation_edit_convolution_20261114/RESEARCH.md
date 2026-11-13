# Frozen R5: exact blockwise optimal-allocation edit convolution, K=215→217

Date: 2026-11-14. Author-side continuation of Draft PRs #2307, #2312, #2320, and #2326. Scientific input pinned to \`awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551\`. The question concerns integer **event boundaries** and radius-two sampled centers; it is not a native six-axis geometric theorem or the 28-coordinate end-to-end prefix-query experiment. Preserve P000 as the project premise.

## Exact theorem: blockwise coupling of optimal-set edit distances

Let \`X\` be a finite increasing set of distinct integers. A selected center set \`S ⊆ X\` is feasible at radius \`R ≥ 0\` when \`max_{x∈X}min_{s∈S}|x-s|≤R\`. Its cost is \`J(S)=Σ_{x∈X}min_{s∈S}|x-s|\`. Suppose the gaps between consecutive nonempty blocks \`X_1,...,X_m\` all exceed \`R\`, so a feasible center in one block cannot cover a point in another block. For block \`i\`, define \`f_i(a)\` as the minimum cost of a feasible center subset of size \`a\`, and \`O_i(a)\` as *all* minimizers at that cardinality (only define these for feasible \`a\`).

For a global budget \`K\` let

\`\`\`
J_R(K) = min_{a_1+...+a_m=K} Σ_i f_i(a_i),
A_K    = {a: Σ_i a_i=K and Σ_i f_i(a_i)=J_R(K)}.
\`\`\`

For any two local (not necessarily consecutive) budgets \`a,b\` define the asymmetric deletion metric

\`\`\`
δ_i(a,b) = min{|S\T|: S∈O_i(a), T∈O_i(b)}.
\`\`\`

For adjacent feasible global budgets \`K,K+1\`, write

\`\`\`
ρ_K = min{|S\T|: S∈Opt(K), T∈Opt(K+1)}.
\`\`\`

**Theorem.** The exact global minimum number of deleted old centers is

\`\`\`
ρ_K = min_{a∈A_K, b∈A_(K+1)} Σ_(i=1)^m δ_i(a_i,b_i).
\`\`\`

The minimum symmetric difference is exactly \`2ρ_K+1\`. This theorem also applies when an optimal allocation *decreases* the center count in some blocks while increasing it elsewhere; treating each block's budgets as necessarily monotone would miss these legal comparisons.

**Proof.** Any feasible global solution decomposes into feasible blockwise solutions because each gap exceeds \`R\`: cross-block centers cannot satisfy radius-\`R\` coverage for points in another block, while in-block feasible centers always give a nearer candidate than any cross-block center. Thus the total nearest-center cost is the sum of local costs. In a globally optimal solution, every local subset must minimize cost for its actual local cardinality; replacing a non-minimal local subset strictly improves global cost at unchanged budget. Therefore the global optimal-set family is precisely the disjoint union over \`a∈A_K\` of Cartesian products \`∏_i O_i(a_i)\`. For any pair of these products, the cardinality of deleted old centers is the sum of blockwise deletion counts (the blocks are disjoint). Minimizing the independent choices within each pair of allocations gives \`Σ_iδ_i(a_i,b_i)\`; minimizing the finite allocation pairs proves the formula. Since \`|T|=|S|+1\`, \`|T\S|=|S\T|+1\`, so \`|S△T|=2|S\T|+1\`. QED.

### Computing δ without enumerating optimal-center families

For any \`a,b\`, construct two acyclic languages of all locally optimal center sequences, using the exact min-plus predecessor-equality test in the existing radius-two dynamic program. The asynchronous product consumes a common center synchronously (zero deletions), an old center alone (one deletion), or a new center alone (one addition). A complete path has old-only count \`d\` and new-only count \`d+b-a\`. Search bounded values of \`d\`, using memoized product states, to obtain exact \`δ_i(a,b)\` and a witness. This extends the preceding #2326 adjacent-local-budget construction to arbitrary budget pairs needed by global allocation changes.

For a fixed finite input this is a terminating exact procedure, with no need to enumerate the exponentially large optimal-set languages. This note does **not** claim a universal polynomial bound on the total joint state/allocation problem.

## Reproducible frozen R5 calculation

The same 15 integer atoms, Gray-code subset generator, rational threshold construction and integer event grouping rebuild \`953\` distinct activation thresholds, \`954\` event boundaries, \`1065\` events and \`29\` blocks separated by \`28\` gaps of size three. The 29 local minimum budgets sum to 213, with minimum total cost 1070.

For extra-center budgets \`u=K-213\`:

| K | Extra units u | J_2(K) | Number of optimal **block allocations** |
|---:|---:|---:|---:|
| 213 | 0 | 1070 | 1 |
| 214 | 1 | 1064 | 1 |
| 215 | 2 | 1059 | 7 |
| 216 | 3 | **1054** | **22** |
| 217 | 4 | **1049** | **41** |

These are counts of optimal budget *allocations across blocks*, not counts of actual optimal center sets, which may be vastly larger.

The exact coupled product was checked over all optimal allocation pairs at each transition:

| Transition | Allocation pairs | Exact ρ_K | Minimum symmetric difference |
|---|---:|---:|---:|
| 213→214 | 1 | 3 | 7 |
| 214→215 | 7 | 2 | 5 |
| **215→216** | **154** | **2** | **5** |
| **216→217** | **902** | **2** | **5** |

The \`215→216\` witness changes only zero-based block 23, using center coordinates relative to that block's origin:
\`S={1,7,12,17,22,27}\`, \`T={1,7,12,17,20,23,28}\`.
It removes \`22,27\`, adds \`20,23,28\`, and preserves \`1,7,12,17\`.

The \`216→217\` witness changes only zero-based block 19:
\`S={2,8,13,18,23}\`, \`T={2,8,13,16,21,24}\`.
It removes \`18,23\`, adds \`16,21,24\`, and preserves \`2,8,13\`.

Choose identical locally optimal centers for all other blocks under the indicated jointly optimal allocations. Exact direct nearest-center checks validate each witness's radius-two feasibility and its optimal local cost. The allocation-pair search rules out all choices with at most one old center removed, completing the global lower bound.

## Verification and provenance

The companion \`VERIFY_R5_ALLOCATION_EDIT.py\` reconstructs the frozen input, computes the complete local cost/count DPs, enumerates only optimal block **allocations** for \`u≤4\`, and uses memoized exact optimal-path products for local pairs. It directly verifies returned witness center sets and their costs. Its finite independent crosscheck enumerates all center subsets for 218 exact point sets \`X={0}∪Y\`, \`Y⊆{1,...,8}\`, \`2≤|X|≤6\`; across these, 2,162 ordered unequal-budget comparisons match the product algorithm. A total of 3,370 feasible center-subset evaluations are included. Integer and \`fractions.Fraction\` arithmetic are used; no floating point or approximate rounding.

Current result: mathematically justified block-convolution theorem and an author-side exact computation. The small finite crosscheck tests implementation, not general proof; formal independent Result/Review and an authenticated R5 Task CLAIM have not been asserted. Historical source attribution remains Draft PR #2326 and the frozen pinned R5 source, without reassigning prior author identities.

Next independent research choices: extend the allocation-coupled product through all 741 consecutive feasible budgets; exploit the earlier marginal-savings decomposition to avoid enumerating unnecessary pairs; and measure the actual complete compressed-certificate, 28-coordinate, 8192-query prefix-index path with a stable workload and explicit resource accounting.
