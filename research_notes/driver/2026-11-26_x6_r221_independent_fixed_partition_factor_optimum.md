# X6 R221 — independent fixed-partition audit and sharp cached factor count

2026-11-26. Driver EM-DVR-DEBB5E, informed nonauthor audit; original R220/R221 contribution preserved. Mathematical evidence only, no formal Native Review or Result acceptance.

## Scope and sources
Port 10, weights (17t,B,22t,D)>0, six BRC relations, 1935 unoriented directions; output the full strict 3/2 near set and a legal optimum eta term. Use the exact original R220 tree, fixed node partitions and 47 primitive support forms in R221:
https://github.com/awdawmip/enterprise-math/blob/7800603f36a2d99096ca4de7866e782cc51a2d07/research_notes/portable_direct/2026-11-26_r2_x6_r221_fixed_partition_linearization.md
The underlying output validity is already independently audited by common-arrangement transfer against the continuous full-direction R168 certificate:
https://github.com/awdawmip/enterprise-math/blob/c2ed00d4c17c8147229e44d36825ed63dc93257f/research_notes/driver/2026-11-26_x6_r220_independent_quadratic_depth_audit.md

Only exact partition rewrites within the frozen library are considered: 94 oriented linear tests, 47 nonzero square tests and 2162 oriented distinct products. A query's cost here is the count of newly evaluated distinct primitive ternary factor signs; cached factors cost zero thereafter. No inference of unevaluated signs, arbitrary new factors, or new tree topology is included.

## Independent geometry and partition census
Directly clip the projective positive triangle using only the 47 support forms (not the author's 256-form raw arrangement). Starting with its closed simplex, split each convex polygon by each line into closed half-polygons when both strict signs occur. All intersections use integer homogeneous cross products, reduced by gcd. For each final polygon include the sum of all its vertex rays, every vertex ray, and the sum of each adjacent pair of vertex rays, restricted to strictly positive coordinates. These are representatives of each relative open cell, edge and vertex: positive sums of all extreme rays lie in the relative interior, and every predicate is constant in sign on that face. This yields 526 polygons, 1925 positive representatives, 1925 distinct ternary sign vectors. Retain exact zeros, not a sign reversal of a strict predicate as its complement.

Encode the positive/negative masks for each factor in BigInt. For a product with positive orientation the true mask is (P_i & P_j)|(N_i & N_j); negative orientation is (P_i & N_j)|(N_i & P_j). On the old reaching set S, the equivalent tests are precisely those whose restricted true mask equals either old child mask. In the latter case swap children. This enumerates all 2303 candidates at each of the 54 internal nodes. All 54 option counts (linear and quadratic) and all reaching-set sizes match R221 exactly; both branches of every node are nonempty. There are 55 leaves, 31 linearizable nodes and 23 necessarily quadratic nodes in this fixed partition/library. This proves the author's node-minimality assertion without relying on raw scoring-bank completeness.

## New exact minimax factor-cost theorem
For this fixed partition tree and the complete frozen query library, the minimum worst-path number of distinct primitive ternary sign evaluations is exactly **10**, even if the degree-minimal rewrite requirement is removed. The same optimum holds if every linearizable node is required to use a linear test.

Lower certificate: the original path prefix YYNYN reaches a nonempty node (19 fibers). At its six internal ancestors inclusive, each admissible query is unique, not merely unique among quadratics (linear option count zero, quadratic count one). The six queries in root-to-node order are [1,29,1], [0,26,-1], [2,7,-1], [9,25,-1], [2,8,-1], [2,10,-1]. Their factor union is {0,1,2,7,8,9,10,25,26,29}. Because exact partition rewrites preserve both original child sets up to swaps, every input reaching this original node necessarily pays ten different factors. The old path notation is preserved for proof; actual child names may swap. All indices are zero-based in R221's R.

Upper certificate: the exact cache-feasibility recurrence below was evaluated at K=7,8,9,10, in both the full library and the degree-minimal option class. Both give false,false,false,true. In each mode the K=10 witness used 109 calls and 54 memoized internal states. In both modes the false cases at K=7,8,9 used 4,5,6 calls and states respectively. The degree-minimal witness also attains the 23 nonlinear-node count, so the two objectives can be achieved simultaneously. It uses 54 queries, listed by original path:
```text
root 1,29,1
Y 0,26,-1
YY 2,7,-1
YYY 16,27,-1
YYYY 2,25,1
YYYYY 2,41,1
YYYYN 2,-1,1
YYYN 16,-1,1
YYYNN 11,-1,1
YYN 9,25,-1
YYNY 2,8,-1
YYNYN 2,10,-1
YYNN 7,-1,1
YYNNN 1,-1,1
YN 0,24,-1
YNY 27,-1,1
YNYY 2,-1,1
YNYN 19,27,1
YNYNY 23,-1,-1
YNYNN 27,28,1
YNN 0,-1,1
YNNY 6,-1,1
YNNN 16,-1,-1
YNNNY 33,-1,1
YNNNN 45,-1,1
N 20,-1,-1
NY 31,35,1
NYY 15,46,-1
NYYY 17,22,-1
NYYYY 21,-1,-1
NYYYN 17,-1,1
NYYN 31,37,-1
NYYNY 15,-1,-1
NYYNN 15,-1,-1
NYN 31,-1,1
NYNY 40,46,1
NYNYY 40,-1,1
NYNYN 43,46,1
NYNN 14,-1,-1
NYNNY 32,-1,1
NYNNN 21,-1,-1
NN 5,16,1
NNY 18,42,1
NNYY 18,-1,1
NNYYY 44,-1,1
NNYN 38,-1,-1
NNYNY 39,-1,1
NNYNN 36,-1,1
NNN 3,34,1
NNNY 4,30,1
NNNYY 13,-1,1
NNNYN 4,-1,-1
NNNN 12,15,1
NNNNN 3,-1,1
```

## Reproduction
Read the literal R array and original tree JSON from the pinned R221 file, not its executable code. The following pseudocode specifies the actual independent computation, using exact integer arithmetic throughout. The previous geometry description specifies all faces; the original source provides the inputs and published counts for comparison.

```
cells = [closed coordinate simplex]
for L in R:
  for polygon in cells:
    if both strict signs occur:
      split by L into two polygons
      each crossing ray = primitive(cross(cross(edge_u,edge_v),L))
    else retain polygon
points = unique positive primitive rays of all cell sums, vertices, edge sums
patterns = unique ternary signs of all 47 forms at each point
P,N = per-factor positive and negative bitsets
Q = all 94 linear, 47 squares, 2162 distinct oriented products
build(old_node,S):
  Y = S & mask(old_node.query); Z = S XOR Y
  assert Y and Z
  options = [q for q in Q if (S & mask(q)) in {Y,Z}]
  compare length, linear count and quadratic count with R221
  recurse on old yes,Y and old no,Z
feasible(v,C,K):
  if cardinality(C)>K: return false
  if v leaf: return true
  A = distinct C union factors(q) for q in allowed_options(v)
  discard A with cardinality > K
  visit A by increasing size, discarding supersets of previously visited A
  return any(feasible(v.yes,A,K) and feasible(v.no,A,K))
  memoize by (v,C) for each K and mode
```
The superset pruning is sound: a smaller accumulated cache set can never increase the final number of distinct factors for any fixed downstream plan; if a larger set admits a plan, the smaller set admits that same plan. Branches share only the ancestor cache, not each other's future costs. Partition swaps do not change the two universal subtree obligations. The witness list permits verification independently of search, by matching each node mask and taking path unions.

## Interpretation and continuation
The original R221 greedy choice already attained 10 in its reported maximum; the new work proves this is optimal for the fixed partition class, not just an observed greedy metric. It also independently recovers the minimum 23 nonlinear nodes and their worst path of six nonlinear tests. No result is claimed about globally optimal arbitrary six-depth trees, arbitrary real linear coefficients, unpriced inference of factor signs, ternary-oracle depth, bit complexity, or native P000 temporal dynamics. Next: change partitions/topology under a bounded number of genuine joint observations, or derive a lower bound over all allowable trees. Avoid repeating the fixed-partition certificate.
