# BRC-X6 — exact two-source balanced-block support bound and native 10-term witness

Date: 2026-11-09. **AUTHOR_PROVED / EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED.** Frozen native source: `f42f2906d77f24085c123f3ccfe9667d41caa96d`; source ports (6,7,28,29), four signs (+,-,-,+), six original labeled actions and nine frozen roots (zero and ±e1,…,±e4). Full signed joint edge observer: next native port, R1–R6 and gate K. This is author portable evidence, not a Source Task checkpoint, Result or Driver review.

## General exact theorem

For positive real marginal vectors `a∈R^r_{>0}`, `b∈R^s_{>0}` of equal total mass, let `c*(a,b)` be the maximum number of **balanced blocks**: nonempty partitions `I_1,…,I_c` of all r row labels and `J_1,…,J_c` of all s column labels satisfying `sum_{i∈I_h} a_i = sum_{j∈J_h} b_j` for each h. Then the smallest support of any unrestricted nonnegative coupling is exactly

`minAtoms_2(a,b) = r+s-c*(a,b)`.

**Proof of lower bound.** Each positive coupling entry is an edge of a bipartite graph. Each connected component is a balanced block and its connected graph requires at least (vertex count - 1) positive edges. If c is the number of graph components, c≤c*, so the edge total is at least r+s-c≥r+s-c*.

**Proof of upper bound.** Fix a maximal c*-block balanced partition. Each block has a nonempty transportation polytope and admits an extreme point. An extreme point has acyclic positive support, because a cycle admits a signed perturbation. If a block's support were disconnected, its components would split that block into more balanced blocks, contradicting maximal c*. Thus the support graph is a spanning tree per block with exactly |I_h|+|J_h|-1 edges. Summing proves equality.

For any restricted deterministic four-source native policy model, projection onto two sources yields such a coupling, so `minSupport_native(x) >= r+s-c*(a,b)`. Equality for unrestricted couplings does not alone grant a native policy representation.

## New exact native example: lower bound 10 where previous cap residual is only 9

The full-positive four-source policy has integer numerators over denominator 54:

```
source 6:   17   1  17   1  17   1
source 7:    8  10  17   1  17   1
source 28:   7   5  25   1   8   8
source 29:   7   5  16  10   8   8
```

It is exactly the convex combination of the following 10 distinct legal native deterministic strategies. Each tuple gives original labeled action indices at sources 6,7,28,29:

```
lexicographic vertex index | action tuple   | numerator
27 | (4,4,4,4) | 8
12 | (2,2,0,0) | 7
11 | (1,5,3,1) | 1
 4 | (0,0,5,5) | 8
19 | (3,3,2,2) | 1
31 | (5,1,1,3) | 1
26 | (4,4,2,2) | 9
14 | (2,2,2,2) | 6
 5 | (0,1,2,3) | 9
13 | (2,2,1,1) | 4
```

The weights total exactly 54. Re-enumerating all 6^4=1296 deterministic action tuples gives exactly 38 legal signed native strategies, and the 10 tuples above preserve the full signed joint observation at every one of the nine frozen roots. Hence minSupport_native≤10.

For p=6 and q=28, take `a=(17,1,17,1,17,1)`, `b=(7,5,25,1,8,8)`. The subset `{a_0}` has total 17 and corresponds to `{b_3,b_4,b_5}`, totaling 1+8+8=17; complements match, establishing c*≥2.

**Complete exact exclusion of c*≥3.** Every partition into at least three balanced blocks can be merged into exactly three. A surjective three-color assignment to six labeled values has `3^6-3*2^6+3 = 540` possibilities. Enumerate all 540 row and 540 column assignments and form each sorted triple of block masses. For a, there are 11 distinct signatures; for b, 50. Their intersection is **empty**, so c*≤2. Thus c*=2, and `minSupport_native ≥ 6+6−2 = 10`. Together with the explicit ten-term representation:

`minSupport_native(X)=10` (exactly).

For this same X, the earlier max-cell-cap residual gives at most 9, so the new partition-aware certificate is strictly stronger. The pairwise balanced-block method by itself yields at most 11 on six-by-six positive marginals, motivating the next step of three-source incidence certificates for compact 12/13-term witnesses.

## Reproduction and source distinctions

Two locally executed author-side exact checkers:
- `verify_brc_two_source_partition.py`: original signed native nine-root oracle, full 24-coordinate recomposition, 38 pure strategies, 14 reachable subset-DP states, c*=2. Certificate JSON SHA-256 `77f880a2d268b47abbb23a783ebcb64546c114d3b6633ce86ef6742b3f133424`.
- `verify_partition_independent.py`: independent 540+540 three-color partition enumeration, 11 vs 50 signatures with empty intersection, 24 proper two-block matching pairs. Both exact PASS on 2026-11-09, no floating point.

Local reproducible five-file author package SHA-256 `14d9e21d3f547e54bf3bf20a38a3a49f6f876799ed1ac6ea6b6956d4d60fde65`. No platform source execution is claimed from these local tests. Native D25 predecessor frontier and historical contributions remain unchanged; original D25 continuation request `h40-r11-d25-exact-continuation-20261109t0137-read-v1` was read as SUCCEEDED but execution_authorized=false. Current own recovery status requires an issued private session. No current winning own Source claim or run has been established. UR V2 original four-file 94,687-byte, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76` remains a separate provenance/writer restoration target, not redone here.

**Next exact action:** 3-source joint action-incidence partition certificate capable of distinguishing 12/13-term support with a short positive rational denominator, retaining all frozen source and joint observer labels.
