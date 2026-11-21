# R284DE — Forest topology of the frozen Port equal-distance mutation graph

Date: 2026-11-21 (Asia/Shanghai)  
Scientific status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**  
Scope: the pinned 34-bit Port auxiliary observer only; **no native X6 or P000 theorem is asserted**.

## Question

R284CZ identified exactly 307 legal source-mutation edges preserving the farthest-arc readout, and R284DD reconstructed their endpoints and labels. What is the complete connected topology of this graph, and what residual information is discarded when equal farthest-distance values are identified without regard to admissible source mutations?

## Definitions and frozen input

Use the R284CO input without repinning: modulus `P=17179869143`, 65,536 distinct Port residues indexed by four upper binary entries and twelve lower binary entries, 64 labeled residual arcs, and the distance readout
`D(x)=max_{0<=j<64} dist_circle(x,A_j)`.
The ordered word-list SHA-256 is
`b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4`.

Define an undirected source-neighbor graph `G_D` on all 65,536 indexed words: an edge `{i,j}` exists exactly when (a) the four upper entries agree, (b) the lower entries differ by a single binary flip or by swapping two unequal entries, and (c) `D(X[i])=D(X[j])`. An equal value does not imply the same underlying source state. Isolated vertices are retained.

## Exact finite theorem

For this frozen input, `G_D` has **307 edges**, **612 nonisolated vertices**, and precisely:

- **303** connected components isomorphic to `K_2` (one edge, two vertices);
- **2** connected components isomorphic to the three-vertex path `P_3` (two edges, three vertices);
- **64,924** isolated vertices.

Therefore **every component is a tree** and the full graph has
`64,924+303+2=65,229` connected components. In contrast, equality of the single observable `D` gives **65,139** distinct fibers. The mutation-connected quotient has **90 more classes** than the readout-only quotient:

```text
#(source-mutation connectivity classes) - #(D-value classes)
= 65,229 - 65,139 = 90.
```

This 90 is the **difference in equivalence-class counts**, not a count of 90 new source edges or a claim that 90 particular codeword pairs are equivalent.

The two nontrivial paths (using original zero-based source indices) are:

| Upper index | Ordered path vertices | Equal D | Winning arc labels in vertex order |
| --- | --- | --- | --- |
| 0 | 64 → 96 → 2144 | 8,366,177,878 | 14, 15, 47 |
| 15 | 64351 → 64383 → 65407 | 8,285,210,914 | 32, 33, 49 |

Their endpoints are not adjacent under the allowed single flip / unequal-bit swap rule, although a two-step path joins them.

## Proof and reproducible completeness

The checker `R284DE_equal_distance_mutation_forest_checker.py` uses the original pinned R284CO word/arc constructors and the R284DD labeled event envelope. It independently recomputes **all 65,536 × 64 = 4,194,304 integer circular distances**, and asserts identical farthest values **and** full maximizer-label sets to the event method.

For every one of the 65,536 source indices, it enumerates all twelve lower-bit flips and all 66 two-position unequal-bit exchanges. The constraint `i<j` counts each legal undirected edge once and never changes an upper entry. This yields exactly **393,216** candidate flip edges and **1,081,344** candidate exchange edges, or **1,474,560** in all. The equality filter returns precisely 307 edges. Their canonical labeled edge-list SHA-256 is

`251a3ca8d2d72cf6f7ca19869f174eb9e370f330533e484faf13dcb2a68dab8b`,

identical to the independently published R284CZ/R284DD graph certificate. Exhaustive graph traversal over these edges obtains the component histogram above. The vertex count and edge count for every traversed component match either `(2,1)` or `(3,2)`, establishing acyclicity and exhausting the nonisolated graph. All remaining vertices are isolated.

Every edge joins equal-D vertices, so each mutation component lies inside one D fiber. Thus the connected-component quotient refines the D-fiber quotient. The stated difference follows by the verified two exact counts. No assumption of a bijection between residues and native X6 states is made.

The independent full-distance pass is **validation**, not the most efficient graph construction. R284DD's attributed envelope and 420-pair fiber join remain a cheaper route to the same 307 edges; the exhaustive edge scan here supplies a separate covering argument. The result is exact finite computational mathematics with a fully specified loop and assertions, not an externally peer-reviewed theorem.

## Provenance, role boundary, next question

Frozen scientific input: `enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py`, blob `b46e0f682b58e47c27094b4bea6fa4e55119a3ee`. Exact prior labeled-envelope source: `R284DD_attributed_envelope_checker.py`, observed blob `634e10b8f613e2eb3df31d72099f3525de01d5e5`. No other scientific pins were substituted.

The result retains historical provenance `EM-DIRECT-20B766` / `RA-617F40704F37299B15489DCA` only as previously sourced metadata; no claim of current authenticated possession, formal CLAIM, Activity write, independent review, or Source Result admission is made.

**Next discriminating problem:** derive the two path-of-three configurations (at upper masks 0 and 15) directly from the signed determinant updates and endpoint translation equations, without enumerating 1,474,560 potential source-neighbor edges. Determine whether the absence of cycles has an arithmetic explanation within this frozen model, or is only a finite census fact.
