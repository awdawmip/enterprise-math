# PREFIX-802 — Exact memoized multivariate Laurent fiber enumerator and sufficient residual states

Date: 2026-11-15. Research line: R6 independent portable research. Predecessor: PREFIX-801 (2026-11-15), at `enterprise-math@959d4efe21613154167f5ed5d613f863b8a1ecdf`. Frozen scientific input pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Status: AUTHOR_PROVED / EXHAUSTIVE_EXACT_INTEGER_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## The precise research problem
For a finite named bipartite BRC source graph `G=(U,V,E)`, each named source edge `e=(i,j)` has nonnegative integer capacity `K_e`. Fix integer row margins `r_i`, column margins `s_j`, with matching totals. A complete named source table is `x_e in {0,...,K_e}`, `sum_j x_ij=r_i` and `sum_i x_ij=s_j`. Each named edge carries an arbitrary signed integer observer vector `w_e in Z^d`. Define the joint Laurent histogram

```text
H_(K,r,s)(z) = SUM_{all named feasible x} z^(SUM_e w_e*x_e).
```

Its coefficients are exact multiplicities; negative observer weights give Laurent exponents, not negative coefficients. No factor-only or independent-edge projection is used.

## Theorem 802.1 — Exact suffix recurrence, including observer repair
Choose any fixed ordering `e_0,...,e_(m-1)` of the named edges. Let `F_k(R,S)` be the joint Laurent polynomial of *all* feasible completions using exactly the suffix `e_k,...,e_(m-1)` with remaining row margins `R` and column margins `S`. Define `F_m(R,S)=1` precisely if all components of `R,S` are zero, and 0 otherwise. If `e_k=(p,q)`, then

```text
F_k(R,S) = SUM_{t=0}^{min(K_e,R_p,S_q)}
            z^(t*w_e) F_(k+1)(R-t*unit_p, S-t*unit_q)
```

for nonnegative margins, with infeasible states giving zero. Every coefficient is a finite nonnegative integer. Induction on suffix length gives equality with the complete named source-table histogram. Thus the suffix polynomial is determined by precisely the suffix index `k` and remaining margins `(R,S)`, conditional on the fixed capacities, edge ordering and complete named weight vectors. Memoizing that tuple is exact, including multiplicity. Different prefixes with the same residual margins may be merged *for their common suffix*, but their already accumulated Laurent monomial shifts must be retained or added separately. The recursive polynomial performs those shifts.

**Proof.** Each complete suffix solution chooses one unique integer `t` for its first named edge. The rest is a feasible suffix solution with the displayed residual margins; conversely each such pair determines exactly one complete suffix table. The observer contribution splits additively. The base case is the empty suffix, proving the identity and integral coefficients. A cache hit returns the same polynomial because the remaining constraints and weights are functions of the suffix and residual margins only. QED.

**State and operation bound.** With fixed original margins `r,s`, the number of potential memo states is at most `(m+1)*PRODUCT_i(r_i+1)*PRODUCT_j(s_j+1)`. The actual reachable state set may be much smaller. For each reachable nonterminal state and candidate integer edge value, the implementation shifts and adds each monomial in the child polynomial. Hence arithmetic work is bounded by the sum of those child support sizes plus map/index overhead; coefficient bit lengths and support/memory costs are not suppressed. Setting every monomial to 1 gives the identical state-space recurrence for exact table counts `F_k(R,S;1)`.

## Theorem 802.2 — Factorization at disconnected suffix components
Suppose the remaining suffix-edge graph decomposes into disjoint connected components `G_1,...,G_h` on named row and column vertices. Its suffix Laurent histogram is zero unless each component has equal total residual row and column demand. If balanced componentwise, then
`F_k(R,S;z) = PRODUCT_a F_(G_a)(R_a,S_a;z)`,
with multivariate Laurent multiplication. Proof: the component source assignments are independent Cartesian factors and observer sums add, giving a bijection and polynomial product.

This is an additional *exactly certified* compression under the specified static suffix observer. It is not an erasure of Cell, Link, Port, signed provenance, branch order, or event time in a native X6 system.

## Minimal prefix-identity witness
For the full `2x2` unit-capacity graph with row and column margins `(1,1)`, the two named tables are the diagonal and anti-diagonal permutation matrices. An observer that records only edge `(0,0)` yields `H(z)=1+z` (multiplicity 1 for each score). Both completed paths have residual margins zero; a cache that discards the prefix observer shift would falsely replace the histogram by a single score. The exact recurrence preserves both.

## Exact finite evidence
Executable standard Node.js JavaScript, using `BigInt` for integer polynomial coefficients:
- Exhaustively enumerated all capacity patterns for `2x2, K<=2`, `2x3, K<=2`, and `3x3, K<=1`; within each, all attainable row/column margin fibers and every named integer table. Compared the complete two-observer signed Laurent histogram of an independently enumerated table population against memoized recursion for every fiber, and checked total coefficients.
- Total patterns: **1322**; margin fibers: **58421**; complete named tables: **67635**; exact histogram/count assertions: **116842**.
- Four specified larger cases compare the non-memoized exact DFS table count to memoized exact count. 3x3 K=2, margins 3: count 31; DFS calls 5341; memo unique states 1683; 4x4 K=1, margins 2: count 90; DFS calls 20057; memo unique states 4881; 4x4 K=2, margins 4: count 2371; DFS calls 5152152; memo unique states 143852; 5x5 K=1, margins 2: count 2040; DFS calls 949201; memo unique states 53468.
- For a disconnected `4x4` pair of `2x2` blocks (capacities 1 on in-block edges, 0 otherwise), verified the complete polynomial equals the product of the two component polynomials; the complete fiber has 4 named tables.
- Exact result: `ALL_CHECKS_PASS PREFIX802 LAURENT_SUFFIX_MEMO`.

These are complete finite checks only for the declared cases. The general theorem is proved by the bijective recurrence and Cartesian-product argument. Exact node-count reduction is recorded; no wall-clock speedup, asymptotic advantage or native X6 temporal dynamics is inferred.

## Source and next unit
Sources: PREFIX-798 cycle-weight/histogram, PREFIX-799 chord parametrization, PREFIX-800 Hall-pruned prefix enumeration, PREFIX-801 incremental Hall slack certificates; the current project P000/ACTIVE worldview, observer-preservation contract, and portable research protocol. This extends the same finite named nonnegative integer source-fiber auxiliary model and keeps the original scientific pin unchanged. Shared Task `RS-X6-NATIVE-TIME-DYNAMICS` is not claimed in this paper.

Files:
- `research_notes/portable_direct/PREFIX802_R6_EXACT_LAURENT_SUFFIX_CHECK.js`
- `research_notes/portable_direct/PREFIX802_R6_EXACT_LAURENT_SUFFIX_RESULTS.json`

Next: study when an incremental Hall cut test is worth applying before the suffix DP cache lookup and test memory/support growth for larger sparse and dense fibers. A separate native-source task is to identify exact Cell/Link/Port and event-time admissibility so these auxiliary source-count observers can be soundly connected to heartbeat X6 dynamics.
