# R723 — The global minimum is exactly fifteen directed triad permissions

Date: 2026-11-11 (Asia/Shanghai).
Line: RS-X6-TRIADIC-CLOSURE-DYNAMICS.
Continuation: R719q, R721, R721b, R722.
Frozen science: awdawmip/enterprise-math at a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000 V5).
Behavioral norms: current main, read separately from frozen scientific input.
Status: author-side exact finite proof and reproducible integer certificate; independent review remains open.

## Precise question and result

Take the fixed five-axis palette {0,1,2,3,4} within the six-axis P000 world. Its ten active triads are the three-element subsets of this palette. The universe Omega has 60 directed Johnson-neighbor arcs u>v, with |u intersect v|=2. The root is triad 012 and the initial ordered V17 slot frame is 012.

An admissible positive rooted closed history of length m is a directed sequence v_0=012, v_1,...,v_m=012 whose consecutive triads are neighbors. The cyclic nonbacktracking (CNB) condition is v_{i-1} != v_{i+1} at every cyclic index; in particular v_{m-1} != v_1 across the closing seam. V17 transport replaces the axis that leaves the ordered frame by the entering axis in the same slot. Its final root frame is one of the six permutations S3={012,021,102,120,201,210}.

For a directed permission set E, let H_m(E) be the set of final root frames realized by its CNB histories of length m. Define the global optimization over all 2^60 subsets of Omega:

M* = min { |E| : for every integer m>=4, H_m(E)=S3 }.

**Theorem R723 (sharp global arc minimum). M*=15.**

The lower bound applies to ALL directed permission sets of the 60-arc universe, with no restriction to the R721b edit neighborhood or to a preassigned set of repair triangles. The 15-arc upper bound is attained by the explicit R721b network.

## Lower bound: complete fourteen-arc exclusion

For m=4,5 and h in S3, construct the complete finite path catalog C[m,h]. Each entry is the 60-bit union-of-directed-arcs mask of a legal rooted CNB length-m positive path with final ordered frame h. Keep the original path order while enumerating; use its union mask only to ask whether all needed permissions are present in E. Hence

h in H_m(E) if and only if
there exists c in C[m,h] with (c AND mask(E))=c.

Literal DFS across all ten triad vertices, using the precise V17 replace-slot map and the closing-seam test, yields these distinct-mask counts:

| final frame h | C[4,h] | C[5,h] |
|---|---:|---:|
| 012 | 12 | 60 |
| 021 | 16 | 40 |
| 102 | 16 | 40 |
| 120 | 6 | 66 |
| 201 | 6 | 66 |
| 210 | 16 | 40 |

**Completeness of the exclusion search.** Every E with |E|<=14 and H_4(E)=H_5(E)=S3 must contain at least one mask from each of these twelve groups. Start with the empty selected mask M and remaining budget 14. At any search node, if all twelve groups are already witnessed, return a feasible example. Otherwise choose any unwitnessed group and branch on EVERY witness c from that group that fits the remaining budget, replacing M by M OR c. If a required group has no fitting witness, prune.

The branch rule is complete: any hypothetical feasible final permission set E containing M includes at least one witness c from every unwitnessed group. That c is among the enumerated branches, and M OR c is a subset of E. Every chosen c adds at least one bit, so search depth is at most fourteen. The remaining budget is exactly 14-popcount(M); therefore memoization by M is logically valid. Group ordering only changes search speed.

The executable certificate evaluates this recursion with two separate pruning configurations:

| Exact integer search | Recursive calls | Unique selected masks | Single-group impossibility leaves | Pair-union impossibility leaves | Feasible <=14 |
|---|---:|---:|---:|---:|---|
| Plain branching (no pair pruning) | 6,115 | 6,067 | 4,932 | 0 | 0 |
| Additional exact pair pruning | 3,883 | 3,883 | 2,796 | 732 | 0 |

Pair pruning is used only if, for two required groups i,j, every pair of paths p in C[i], q in C[j] has popcount((p OR q) AND NOT M) greater than the remaining budget. This is a logically necessary condition, not a heuristic cut. The plain solver proves the lower bound independently of the pair-pruning implementation.

Both exact integer recursions return no feasible mask with at most 14 distinct directed arcs. Consequently, every network satisfying all lengths m>=4, which in particular satisfies lengths 4 and 5, must have at least fifteen directed arcs.

No floating-point computation is involved in this certificate.

## Upper bound: an explicit fifteen-arc witness for every length

Use the exact R721b permission set:

    012>024  012>123  012>124
    013>012  013>023
    023>012  023>013
    024>023  024>124
    123>013  123>023  123>134
    124>123  124>134
    134>013

For the complete type-preserving state (previous triad, current triad, ordered slot frame, first neighbor after root), let D_t be the set of states after t legal transitions. The finite deterministic successor operator F gives D_(t+1)=F(D_t). Exact set propagation returns

| t | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| |D_t| | 3 | 7 | 13 | 25 | 55 | 113 | 183 | 244 | 268 | 270 | 270 |

The checker compares full typed sets and establishes D_10=D_11, not merely equal cardinalities. Therefore D_t=D_10 for every t>=10 by induction. At each m=4,...,11, all six final root frames occur with the seam condition satisfied. Their support remains the full S3 for all m>11. Independent positive-path DFS reproduces R721b's six-bin ordered history counts at m=4,5,6,7.

Thus a fifteen-arc all-length carrier exists, yielding M*<=15. Together with the exhaustive lower bound, M*=15.

## Research interpretation and preserved scope

The new theorem closes R722's global open optimization question for the declared five-axis, rooted, ordered V17, directed-CNB **existential relationship-support observer**. R722's local radius-two result remains a more detailed locality classification; R721's 18-arc optimum under fixed repair triangles is a separate constrained optimum.

Bitmask reachability preserves the yes/no existence of a path for each final frame under the same permitted-arc set. It is not a replacement for positive branch multiplicity, exact BRC weight, full path provenance, or the native V29 Link/Port inventory and event-time semantics. The existing P000 six-axis space and three-axis slice typing are unchanged.

## Reproduction and evidence

Primary executable certificate (Python standard library, exact integers and sets only):

    python R723_GLOBAL_MIN_15_ARC_VERIFY.py > R723_GLOBAL_MIN_15_ARC_RESULTS.json

Expected status: R723_GLOBAL_15_ARC_SHARP_PASS.

The generated JSON records the complete 60-arc ordering, the twelve catalog counts, both fourteen-arc exhaustive searches, all eleven lifted-state sizes, full support at lengths 4..11, the concrete 15-arc witness, and independent positive-history counts at lengths 4..7. It can be regenerated from the adjacent Python file without Git access.

Prior sources: R721b, immutable commit ab1faa492bec4e7f56a81dc8bba09d96b0d6cffc; R722, immutable commit 4f8bb38d903e47d18577c89611916d7afc2a3d41; project portable research and continuation contracts (current norms, not frozen science).

## Next discriminating scientific units

1. Enumerate fifteen-arc minimizers and their equivalence classes under permutations of the three initial axes and two reserve axes. Determine which minimizers satisfy all lengths, not just the two lower-bound constraints.
2. Map the explicit fifteen directed triad transitions into V29's actual typed Link/Port inventory and time-dependent event dependency rules. Check whether the abstract permission graph is realizable without extra native transitions or staging state, and quantify the native cost.
3. For the resulting native histories, distinguish existential S3 support from provenance-sensitive future observers and determine the smallest sufficient memory. Preserve the exact source and branch carriers until an observer-preserving quotient is proved.

The shared mother task and its mathematical review/Result controls continue under their own current authority. This document records an author-side exact finite proof, not a native accepted Result.
