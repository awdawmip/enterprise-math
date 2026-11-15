# R186 — Sharp pair-query versus unrestricted source-oracle complexity gap

Date: 2026-11-15. Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.
Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Dependency: R185 in immutable commit `d043e98cae0a25ae2dab4e168ac2b7f9264ba8fb`; underlying R182–R184 source-only quotient.

## Observer and promise

Fix r distinct named source IDs whose **exact support set S is known**. The unknown state is the chronological order of their last occurrences, a permutation of S. Each underlying history is still composed of whole native signed-X6 atoms and retains original path, branch, multiplicity, rational positive BRC mass, provenance and joint relations in its full carrier as required by other observers. Here the declared observer reads only the latest element of a queried subset, under whole-history concatenation.

Restrict the allowed query subsets to cardinality at most 2. A singleton query is predetermined by the known support. For distinct i,j∈S, `q_{\{i,j\}}` returns the later element. Thus one informative query is precisely a binary comparison of the last-occurrence positions of i and j.

## Theorem A: exact equivalence with deterministic comparison sorting

Every deterministic adaptive pair-query recovery algorithm on known S corresponds to a comparison-sorting decision tree on r distinct labeled items, with the same worst-case number of informative queries, and conversely every comparison-sorting decision tree gives such a source-recovery algorithm.

**Proof.** Both tasks have the same r! possible strict total orders and exactly the same available binary experiment for each unordered pair (i,j): which one comes later. A query algorithm's branching is therefore a comparison tree, and any comparison tree can be evaluated by the source oracle. Singleton queries return i independently of the order and can be deleted. QED.

Write `C_pair(r)` for the exact deterministic worst-case number of pair queries. Then
`ceil(log2(r!)) <= C_pair(r) <= O(r log r)`.
The lower bound follows because each binary transcript tree with h queries has at most 2^h leaves while r! different orders require different leaves. A mergesort of the known source IDs gives the upper bound using at most O(r log r) comparisons, implemented by the reproducible checker. Consequently
`C_pair(r)=Theta(r log r)` for r≥2, with asymptotic constants understood in the usual external algorithmic sense.

By R185, allowing arbitrary-size subset selectors recovers the same known-support permutation in exactly `r-1` queries. **Restriction to pair queries changes the optimal worst-case order of growth from Theta(r) to Theta(r log r)** while preserving the same source-order quotient.

## Theorem B: exact small-r values, not an extrapolated formula

Finite exhaustive decision-tree minimax, with all r! permutations and all C(r,2) pair comparisons, establishes

| r | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| Optimal worst-case pair queries | 0 | 1 | 3 | 5 | 7 |
| Unrestricted-subset queries (R185) | 0 | 1 | 2 | 3 | 4 |

The checker uses the exact Bellman equation on every non-singleton candidate-belief set B:

`D(B)=1+min_{i<j, both outcomes possible} max(D(B_{i>j}),D(B_{j>i}))`, with `D({state})=0`.

Queries that do not split B are omitted because they give no information. The recursion strictly decreases |B| and enumerates all viable pair choices. This is an exact finite exhaustive proof for r≤5. No closed all-r comparison-sorting formula is asserted.

## Verification

`R186_pair_oracle_sort_check.py` uses exact integers and stdlib permutations. `R186_verification.json` records:

- Exact minimax values above and 1, 3, 19, 219, 4,231 memoized belief states for r=1..5.
- Direct mergesort reconstruction of all 46,233 distinct source orders over r=1..8 (sum of factorials), always matching the original permutation.
- Observed maximum comparison counts r=1..8: 0,1,3,5,8,11,14,17.

The finite checks corroborate the exact observer equivalence and algorithms; the all-r complexity follows from the proof. Native `src/enterprise_math/brc_transport.py` integration remains a separate pending engineering exercise, not represented by this reference checker.

## Interface consequence

For BRC positive weighted ports, apply this compression only after fixing the source query language and preserving all separately observable branch/path/joint identity on the native carrier. R185–R186 now separate **information state size**, **fixed query repertoire size**, and **adaptive query count with or without large-subset access**. Query restriction changes resource complexity even though it does not change the semantic permutation state.

Next: determine exact or bounded comparison counts under partial-support uncertainty, and test the source-query adapter against the actual repository-native BRC port module while preserving provenance.

Historical Researcher-ID `EM-DIRECT-BF4AD7`, SID `MCP-46f202db13e64ad6b4c8860e06908245`, Activity `RA-7A118452894D2600AE7DE5A2`; no formal CLAIM, independent Review, or Foundation admission is asserted.
