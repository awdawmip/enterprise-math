# EC49FOD — Native BRC adjacent-cache forcing-core phase change
2026-11-14 · `AUTHOR_PROVED / TWO_EXACT_ALGORITHMS_PASS / NOT_REVIEWED`

Scientific continuation of [EC49FOC](https://github.com/awdawmip/enterprise-math/pull/2363), with unchanged frozen input pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. The problem is the auxiliary native signed ordered-prefix rooted minimum-cover problem for 24 demands, four roots `03,05,06,07`, and threshold `B=155`.

## Theorem (a single-key neighbor preserves the full optimum triple but changes its forcing-core hypergraph)

For configuration K, write `D_(K,r)(A)` for the exact minimum cost of native signed ordered-prefix words under root r covering the label set A in the unchanged 94-key/178850-word source. Fix the same legal four rooted masks in order 03,05,06,07:

`p=(0,5,138,8192)`, so `U=(4,5,6,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23)` (18 future demands).

For `T⊆U`, define `f_(K,p)(T)=min_(lawful root assignments of T) Σ_r D_(K,r)(S_r∪T_r)`. An obstruction has `f_(K,p)(T)>155`; it is inclusion-minimal if every proper subset is feasible. Its minimal size is `h*(K,p)`.

* At K=32279: the only strict obstruction among all 262144 future subsets is the complete U, with cost 156. Thus `h*=18`.
* At K=32315 **and** 32318: there are exactly six strict subsets, five of size 17 and U itself. The five inclusion-minimal cores are `U\\{4}`, `U\\{5}`, `U\\{6}`, `U\\{8}`, `U\\{9}`, with respective costs `(156,156,157,156,156)`. The full U costs 158, and `h*=17`.
* Both `(32315,32279)` and `(32318,32279)` occur in the frozen single-key `FIRST_NEUTRAL_EDGES_EC49FNS.txt` list. Yet all three caches have exactly the same original **full 24-demand global** cost, optimizer multiplicity, and next distinct cost `(C,m,next)=(154,1,155)`, hence `g=1`, in `EXACT_NATIVE_32000_32999.txt`.

Therefore the triple `(C,m,g)` does **not** determine the threshold forcing-core hypergraph of the named auxiliary partial-state observer, even across these two exact globally-neutral single-key exchanges.

Comparison caches 32264 and 32274 also have five size-17 minimal cores. No direct one-key adjacency from them to 32279 is claimed.

| K | H16 | H17 | H18 | h* | Strict subset counts for sizes 16/17/18 |
|---|---:|---:|---:|---:|---|
| 32264 |155|157|158|17|0 / 5 / 1|
| 32274 |155|157|158|17|0 / 5 / 1|
| 32279 |153|155|156|18|0 / 0 / 1|
| 32315 |155|157|158|17|0 / 5 / 1|
| 32318 |155|157|158|17|0 / 5 / 1|

Here `H_h=max_{|T|=h} f(T)`. All 16-element future subsets in the compared cases cost at most 155, making the 17/18 boundaries sharp. At K=32279 all 17-element subsets also cost at most 155.

## Full numerical observer versus threshold observer

Across all 262144 exact future subset values `f(T)`, the 32264 and 32315 maps are **equal entry-by-entry**, notwithstanding their different cache records. The 32315 and 32318 maps differ at **22154** subsets, first witnessed by `T={12,20}` with costs 70 and 69, but their entire threshold-obstruction hypergraphs coincide. The 32279 and 32315 maps differ at **211351** subsets and at the core hypergraph. Hence (i) full subset cost map, (ii) threshold hypergraph, and (iii) original global optimizer triple are three inequivalent observers on these cases.

The 32279 legal roots for future demand 11 are `03,07`, whereas 32315 and 32318 permit `07` alone. Root cost tables also differ. We assert the observed *combined* change, not that eligibility alone explains it.

## Exact proof and verification

**Monotonicity lemma:** Every cover of A' covers A⊆A', so `D_r(A)≤D_r(A')`; restriction of a lawful root assignment similarly yields `f(T)≤f(T')` for T⊆T'. Consequently `T` is a minimal strict obstruction iff `f(T)>B` and all one-deletion subsets cost at most B; and ruling out all size-(h−1) obstructions rules out every smaller cardinality.

**Exhaustive proof:** Reconstruct each four-root cost table from the original ordered signed-prefix word tries. A min-plus partition recurrence over eligible rooted submasks computes `f(T)` for all `2^18=262144` T per configuration: **1,310,720** subset values across five configurations. Enumerate all strict T and test their proper one-deletions, which returns the stated core families and full `H_0,...,H_18` sequences. A separate direct root-choice enumerator checks every subset of size 16,17,18, totaling `5×(153+18+1)=860` boundary subsets, with identical exact integer values and strict-count histograms. No floating-point or random approximation is used.

Scientific inputs and reproducible executables: source master SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; original independent trie checker `VERIFY_EC49FNY_INDEPENDENT.py` ([PR #2343](https://github.com/awdawmip/enterprise-math/pull/2343)); the complete original source and two new executed programs and machine certificate are supplied in the companion local evidence bundle. Certificate SHA256 `b91ed8bbfa9c1c990f89fc06b0a549860f09c71417160e52c39b06873d0dcf26`.

## Frontier and provenance

Extend to other 84 globally-neutral key swaps and contrast genuine DFS states with the auxiliary p; seek a low-cost root-coupling bound that predicts core-hypergraph transitions without a full subset-lattice pass. This is exact finite author validation; the scientific statement is `NOT_REVIEWED`. No formal Task CLAIM/Result, P000 modification, or mathematical admission follows from storing the note.
