# R762KF — Exact complete classification for two inactive Port pairs

**Date:** 2026-11-23. **Status:** AUTHOR_PROVED_WITH_FINITE_CONNECTED_PARITY_SEARCH / EXACT_INTEGER_CHECKED / NOT_REVIEWED.

## Frozen source, observer and question

Scientific input is unchanged: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`, task publication `RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142`. Predecessors are R762KC, R762KD and R762KE on the same line, especially R762KE's all-positive one-inactive-Port construction in PR #3012.

Here again an **unsigned auxiliary** graph has six axis labels `0..5`, 15 two-axis Ports, and 20 three-axis colors. Each color `abc` may emit an undirected event joining **two distinct active pair Ports** among `ab,ac,bc`. Every color has an arbitrary prescribed **positive** integer number of events `n_s≥1`. A feasible realization is one connected colored multigraph across **all active Ports** with exact color multiplicities and every degree positive and even.

Now remove **exactly two distinct Ports** from the 15, leaving 13 active Port vertices.

## Theorem KF.1 — Complete disjointness criterion

Let the two removed Ports be (u,v\in\binom{\{0,\ldots,5\}}2), (u\ne v). Then the following are equivalent:

1. (u\cap v=\varnothing) (the missing Port pairs use four distinct native axes).
2. Every positive integer inventory (n\in\mathbf Z_{>0}^{20}) admits a connected exact-color 13-Port graph with all degrees positive even, hence an Euler circuit from any prescribed active Port.
3. At least one strictly positive 20-color inventory admits such a realization.

If (u\cap v\ne\varnothing), **no** strictly positive all-20-color inventory is feasible in this auxiliary graph.

### Necessity is a one-color exact obstruction

When (u=ab), (v=ac), the triple color (abc) has the pair-Port set ({ab,ac,bc}). Only (bc) remains active, so there are **zero** legal event edges of color (abc). Since (n_{abc}\ge1), no exact-color realization is possible. This proves the negative direction for every such pair and every positive inventory; it does not assume a failed numerical search.

There are (60) intersecting pairs of Port pairs and (45) disjoint pairs among the \(\binom{15}{2}=105\) choices, as the exact checker also verifies.

### Sufficiency reduces by six-axis symmetry to removed Ports 01 and 23

The full axis relabeling group (S_6) acts transitively on unordered **disjoint** Port pairs. Fix (u=01,v=23). All twenty triple colors remain usable: eight are *forced*, each allowing one edge, and twelve are *flexible*, each allowing a full triangle of three possible edges. Exact color lists:

```text
forced:    012 013 014 015 023 123 234 235
flexible:  024 025 034 035 045 124 125 134 135 145 245 345
active:    02 03 04 05 12 13 14 15 24 25 34 35 45
```

For any prescribed forced multiplicities, let (b_F\in\mathbf F_2^{13}) be the XOR of the forced edges with odd counts. The eight forced edges yield (2^8=256) oddness masks, but only **128 distinct** XOR boundaries.

**Exact finite connected-parity lemma.** For **each of these 128 forced boundaries** there is a choice of **one legal edge from each of the twelve flexible colors** with (i) total XOR boundary equal to the forced boundary; and (ii) all thirteen active Ports connected after adjoining all eight forced edges.

This is a complete finite certificate, given by the attached deterministic standard-library Python verifier `R762KF_TWO_INACTIVE_CLASSIFICATION_VERIFY.py`. It constructs the suffix reachability sets using only exact GF(2) integer XOR, verifies the final 4096-state even boundary space, and then for each of the 128 explicit targets uses complete lexicographically ordered DFS, pruning branches solely when the target boundary cannot be achieved by remaining colors. It **asserts that a connected witness exists**, then independently checks its connectivity, edge count, legal colors and exact XOR. No random sampling is used to establish the lemma, and failure of a search would halt the program. Unlike an unverified heuristic, the finite search exhausts all candidate branches for each target if necessary.

### Symbolic extension to arbitrary positive counts

Choose the finite certificate for the actual forced boundary (b_F). For each flexible triangle ({x,y,z}) with selected base edge (xy), and exact count (n):

- (n=1): emit (xy) once.
- Even (n\ge2): emit (xz,yz), followed by ((n-2)/2) pairs of identical legal edges.
- Odd (n\ge3): emit (xy,xz,xz), followed by ((n-3)/2) pairs of identical legal edges.

This preserves the chosen GF(2) edge boundary and a connected path between endpoints of the base edge, at every integer multiplicity. Emit every forced color's unique legal edge its exact positive number of times. The total boundary is (b_F\oplus b_F=0), so all degrees are even; the certified connected base graph remains connected after the replacements, so all thirteen degrees are positive. Exact multiplicities are maintained. Euler's theorem completes sufficiency for **every** positive inventory.

The enumeration of all 105 removed Port pairs is also exact and confirms that each intersecting case has one unusable triple color, while each disjoint case has none.

## Corollary KF.2 — All 42-event target inventories for each disjoint pair

For a fixed disjoint removed Port pair, choose exactly five singleton colors and seven triple colors, the other eight being doubles. All
\[
\boxed{\binom{20}{5}\binom{15}{7}=99,768,240}
\]
labeled target inventories admit a connected **42-event** Euler realization. Across the 45 distinctly named disjoint removed Port pair choices, the total number of pair-labeled target configurations is
\[
\boxed{45\binom{20}{5}\binom{15}{7}=4,489,570,800}.
\]
Adding two copies of a legal edge on any *marked* singleton support produces a 44-event connected source from each target. This yields (498,841,200) marked source constructions **per fixed disjoint pair**, without asserting that every arbitrary 44-event source is compressible.

For intersecting removed Port pairs the positive-color hypothesis is inconsistent with the absence of an allowed event edge for one triple, so the 42-event ((5,8,7)) all-positive class is empty of realizations.

## Actual verification range

The exact checker covers: all 105 Port-pair choices (60 incident/45 disjoint); all 4096 even Port boundaries for the flexible suffix; 256 forced parity masks reduced to 128 distinct targets; **all 128 connected-parity witnesses**, with exact edge legality, 13-Port connectivity and boundary checks; and 512 separate full-inventory realizations (256 arbitrary positive profiles plus 256 42-event profiles), all passing exact color count and positive even degree. The 512 concrete realizations are regressions; the all-input theorem is proved by the finite complete 128-target lemma plus the general symbolic extension.

The verifier is a short pure Python program, no floating point and no external dependencies. It provides reproducible finite proof checking without assuming a search-generated witness is accepted merely because a routine returned.

## Scope and continuation

These are **auxiliary unsigned Port–Euler observation theorems**. The signed native six-axis P000 ontology, primitive `TRIADIC_CLOSURE_E`, 120° Enterprise orthogonality, ordered Cell/Link/Port path identity, and BRC historical source fidelity remain original fixed obligations. This result is not a typed signed native event realization or an observer-safe BRC quotient. Independent mathematical review: `NOT_REVIEWED`.

**Next question:** Extend Port removal to three inactive pair Ports, classifying which missing-Port graphs leave every color with at least two active pair vertices, and then checking connected parity realizability on the resulting graph. In parallel, construct native signed event lifting conditions and check BRC provenance under time-ordered updates.
