# R284DC — Complete 307-edge source graph from only 420 equal-value candidate pairs

Date: 2026-11-21 (Asia/Shanghai)  
Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**  
Source scope: original frozen 34-bit Port auxiliary observer (R284CO), with unchanged 65,536 original source-matrix indices and 64 labeled circular arcs; source proof pins remain unchanged.

## Mathematical question

R284CZ reconstructed the 307 source-neighbor edges with equal farthest-arc distance by examining all 1,474,560 permitted lower-matrix single flips and unequal-entry swaps. R284DA computes the farthest-arc values D without individually evaluating 64 arcs per site. R284DB classifies each of those 307 equalities by its winning-arc affine endpoint shift.

Can the exact equality graph be **constructed** without enumerating all 1,474,560 source mutation edges? Yes: invert the finite farthest-distance observation D and test source adjacency *only inside its collision fibers*.

## Exact general fiber-join theorem

Let V be any finite set of source-labeled objects, let f:V→Y be any deterministic observable with an exact equality relation, and let G=(V,E) be any specified simple undirected source graph whose adjacency can be decided directly from the two source labels. Define fibers V_y={v∈V:f(v)=y}. Then

```text
E_equal = { {u,v} ∈ E : f(u)=f(v) }
        = union over y of { {u,v}⊆V_y : u≠v and Adj_G(u,v) }.
```

Proof: every equality edge is contained in the fiber of its common observable value, so the right-hand side includes it; every pair emitted by the right-hand side satisfies both exact equality and the graph adjacency predicate, so it is an equality edge. A strict index-order comparison prevents duplicates.

If the cost of computing f on all n vertices is C_f, and B=∑_y binom(|V_y|,2), grouping by a hash table takes expected O(n) additional time and the join takes exactly B adjacency tests, plus the cost of output. Alternatively sorted grouping costs O(n log n) deterministically. The algorithm's cost is therefore C_f+O(n+B), with B data-dependent. This is **not** a universal worst-case subquadratic claim: when f is constant, B=n(n-1)/2.

## Frozen Port graph and adjacency test

The frozen generator creates 16 upper configurations ×4,096 lower binary vectors, enumerated by source index i=4096 u+l. The source graph permits edges with the *same upper index* and one of:

- A single differing lower bit (Hamming distance one); or
- Exactly two differing lower bits, one changing 0→1 and the other 1→0 (a swap of unequal original entries).

Thus a pair i<j is adjacent exactly when floor(i/4096)=floor(j/4096) and its lower 12-bit XOR mask has one set bit, or has two set bits and the initial lower vector contains precisely one set bit at the differing positions. This exact bit predicate depends only on original source indices, not a geometrically guessed neighbor relation.

## Exhaustive exact result

Compute all D(x) via R284DA's two-slope integer event envelope; hash original source indices by their D value. For the fixed R284CO scientific generator, the full distribution of fiber sizes is:

| Fiber size | Number of distinct D values | Sites accounted for | Within-fiber pairs |
|---:|---:|---:|---:|
| 1 | 64,760 | 64,760 | 0 |
| 2 | 366 | 732 | 366 |
| 3 | 8 | 24 | 24 |
| 4 | 5 | 20 | 30 |
| **Total** | **65,139** | **65,536** | **420** |

There are 379 non-singleton fibers. Of the 420 pairs, 53 have different upper configurations, and 367 have the same upper configuration. Among these 367 pairs, 306 are admissible single flips, 1 is an admissible unequal-entry swap, and 60 are not source neighbors. The 60 failed same-upper tests consist of 29 pairs with two bits changed in the same direction, 25 with three differing bits, 4 with five, and 2 with six. Hence **307** source-neighbor equality edges are recovered after only **420** candidate adjacency tests, and 113 candidates are rejected.

These 307 edges have mutation counts:

| Mutation | Exact equal-distance edges |
|---|---:|
| Flip lower index 0 | 3 |
| Flip lower index 1 | 14 |
| Flip lower index 2 | 228 |
| Flip lower index 4 | 16 |
| Flip lower index 6 | 45 |
| Swap lower indices 0,1 | 1 |
| **Total** | **307** |

Original source indices are retained in increasing order; for equal-index source order, flips are ordered by lower position before swaps. For 612 distinct endpoint source indices, the unique maximizing arc labels are obtained by 39,168 direct integer arc distance evaluations. Hashing the complete ordered list of tuples `[mutation_kind,lower_positions,lower_source_index,higher_source_index,D,winning_arc_low,winning_arc_high]` reproduces exactly the independent R284CZ digest:

```
251a3ca8d2d72cf6f7ca19869f174eb9e370f330533e484faf13dcb2a68dab8b
```

Therefore this exact collision-fiber join reconstructs the entire previously verified 307-edge graph, including the original index ordering and winner labels, *without traversing the original 1,474,560 candidate graph edges*. The edge-predicate comparison count is reduced by a factor `1,474,560/420 = 3,510.857142857...`. This is a comparison-count reduction; end-to-end speed and memory depend on codeword generation, envelope preprocessing, hash grouping, source decoding and optional winner-label recovery.

## Evidence, reproducibility, provenance

Reproducible code: `R284DC_equal_value_join_checker.py`, and full JSON certificate: `R284DC_equal_value_join_certificate.json` in this directory. The checker imports the unchanged frozen `R284CO_spectral_witness_checker.py` and verified R284DA `R284DA_envelope_checker.py`, uses Python unbounded integers, verifies the exact codeword SHA-256 `b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4`, the full collision histogram, excluded-pair counts, mutation classes and the R284CZ canonical edge digest. A local execution returned all assertions successfully. R284DA separately compared all 65,536 D values against the full 4,194,304 direct arc-distance baseline.

Frozen immutable source: `awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py` (Git blob `b46e0f682b58e47c27094b4bea6fa4e55119a3ee`). Results apply to this exact finite Port observer, not any unproved native X6 dynamics. The mathematics is author-proved and exact finite certified; independent mathematical review remains `NOT_REVIEWED`.

## Residual, applicability and next question

The full f-value bucket preserves exact farthest observation; every candidate test uses **original matrix indices** to retain the source-neighbor meaning. It does not silently identify equal residues or erase upper/lower provenance. The project-wide forced-rank `tau(x)` classification of four unforced and 303 absorbed edges remains the separate verified input R284CW.

The next useful step is to exploit the source determinant's lower-bit mutation formulas together with the R284DB 35 translation classes to generate only plausible collisions *before* forming all 65,536 farthest values. Compare total construction/preprocessing and evidence recovery costs, and check whether a formal deterministic bounded-fiber property can be proved beyond the frozen input.

Historical contribution source `EM-DIRECT-20B766` and Activity `RA-617F40704F37299B15489DCA` remain as attribution; fresh Activity semantic checkpoint association requires the current exact legitimate session/CAS and readback, separately from this already preserved GitHub scientific artifact. No formal Task CLAIM, Result, Review or P000/worldview update is asserted.
