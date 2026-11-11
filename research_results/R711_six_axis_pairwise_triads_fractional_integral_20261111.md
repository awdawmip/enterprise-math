# R711 | Six-axis pairwise triangle licenses: an exact fractional–integral equivalence

**Task:** `RS-X6-TRIADIC-CLOSURE-DYNAMICS` · **Researcher-ID:** `EM-X6-912721` · **Research-Activity-ID:** `RA-54F16A1A0CB4F90FE4E40A54`

**Source boundaries:** Frozen task science `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`; applicable rules read at global `57368497026a5b2318fed62d23d6429eb42c150a` and project `b06c8f2d839da9499909e982c18da4166fa3ecd2`. Source science is unchanged. Scientific status: exact finite combinatorial certificate and a hand-verifiable obstruction proof; author-side only, pending native X6 event interpretation and Driver review.

## Exact question and BRC carrier

Fix **six** labeled native-axis indices `V={0,1,2,3,4,5}`. Let `G=(V,E)` be a simple undirected **pairwise license graph**. A triple `T⊂V` is eligible precisely when its three pairs are edges of `G`; write `H(G)=Triangles(G)`.

A **fractional triad saturation** is a rational nonnegative branch-weight family `w_T≥0` for `T∈H(G)` satisfying, for each `v∈V`, `Σ_{T∋v}w_T=1`. An **integral two-triad factor** is a pair `T,V\T∈H(G)` (hence two disjoint triples cover all six axes). The weights are positive-rational BRC branch masses, **not signed force amplitudes**.

## R711.1 Theorem

For **every simple graph on six vertices**, a fractional triad saturation exists **if and only if** two vertex-disjoint graph triangles exist.

*Reverse implication.* Assign weight one to the two disjoint triples, zero to all other triples.

*Forward implication — complete finite certificate with transparent witnesses.* There are exactly `2^15=32,768` labeled graphs (15 possible edges) and 20 candidate triples. The accompanying Python program checks every 15-bit graph, licenses a triple iff all three edge bits are present, and tests every complementary pair of triples. Exactly 4,106 graphs contain an integral two-triad factor; the remaining 28,662 do not. Among the latter, 182 are **maximal** under edge addition, falling into exactly four six-vertex relabeling orbits:

| Canonical 15-bit graph | Labeled orbit size | Triangles | Fractional infeasibility witness |
|---|---:|---:|---|
| `4095` | 20 | 10 | `S={0,1,2}` meets each triangle in at least two vertices |
| `5887` | 30 | 10 | Vertex `5` belongs to no triangle |
| `6142` | 60 | 7 | Vertex `5` belongs to no triangle |
| `7071` | 72 | 5 | Vertex `0` belongs to every triangle |

All four witnesses are immediate contradictions to a fractional saturation. Indeed, summing six vertex equations implies `Σ_T w_T=2`. An uncovered vertex has mass zero. A vertex common to every triangle has mass two rather than one. In the `S` case, `Σ_{v∈S}Σ_{T∋v}w_T≥2Σ_Tw_T=4`, but saturation demands exactly three.

Every factor-free graph is contained in a maximal factor-free graph: add missing edges while this property persists, terminating within 15 edge additions. Each displayed obstruction survives graph edge deletion and relabeling. The four classes therefore exclude fractional saturation for **all** 28,662 factor-free graphs, proving the theorem.

*Finite certification details.* The executable uses only integer bit operations, all 720 vertex permutations, exact orbit-canonicalization, and complete maximal-graph verification. It checks every graph is either factor-containing or a subgraph of a classified maximal graph. This is a finite exhaustive proof *for the specified six-vertex graph-generated license family*, not a generic hypergraph integrality theorem.

## R711.2 Connected nine-quantum counterexample

The exact six-vertex property is scale-sensitive. Let **nine separately labeled force quanta** (not nine X6 axes) form `K4` on labels `0..3`, `K5` on labels `4..8`, and a **single** bridge edge `(3,4)`. The graph is connected, but all its triangles lie within one clique.

Assign `1/3` to each of the four `K4` triangles and `1/6` to each of the ten `K5` triangles. Every `K4` vertex occurs in three such triangles and every `K5` vertex in six, so all nine vertex saturation equations hold. Total branch mass is `4/3+10/6=3`. No integral partition into three triangles exists: each triangle stays inside a 4- or 5-vertex clique, and neither component size is divisible by three. The bridge participates in no triangle.

Thus a genuine fractional–integral gap exists for this connected graph-generated **force-quantum** example; it does not add axes to P000.

## R709/R710/R711 synthesis and application

R709's four Pasch triples give a fractional but not integral **arbitrary three-uniform** license. R710 showed the particular Pasch family gains complementary triples under graph-generated pairwise closure. R711.1 extends that observation to **every** possible six-axis pairwise graph. It establishes existence, not unique source decomposition or dynamic BRC equivalence. Different integral factors retain separate provenance.

**Next discriminating native test:** at the frozen task pin, choose an actual X6 Cell/Link/Port occupancy with V29 PASS/TRANSFER and V39 loop-flow `j`. Compute all twenty triple eligibility bits `H(c,state,t,source)` and derive its pairwise graph. Compare `H` with `Triangles(G)`; either obtain a valid native instance of R711.1 or exhibit the first exact license that cannot be represented by one pairwise graph. Record Cell address, signed directions, event order, source tags, and rotation transport. This test does not require revising P000.

## Verification

Run `python3 R711_triangle_clique_fractional_integral.py`. Actual local result:

```
R711_SIX_VERTEX_CLIQUE_TRIANGLE_GAP_EXACT_PASS 32768 28662 182 4 14
```

`R711_triangle_clique_fractional_integral_evidence.json` records the four representatives and exact nine-quantum mass test. Science is exact finite graph combinatorics, not yet admitted as X6 full dynamics or independently reviewed.