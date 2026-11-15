# R188 — Exact unknown-support pair-oracle minimax via adjacent-comparison witnesses

Date: 2026-11-15. Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**. Independent portable research, no formal CLAIM, Result, Review or native BRC acceptance.

**Frozen scientific input** 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Mathematical predecessors R185–R186 at commit 09f4c0c6eebf51a6cc15778b9101ccbe097004c1; newly preserved R187 at commit 1a7b6b5de98dbba25993c99416623db8308d840b. R188 *resolves the R187 general equality question*, leaving R187's immutable original note as historical frontier rather than rewriting its former open status.

## Defined observer and operation scope

Fix k>=1 labeled source IDs. A full underlying history is a concatenation of whole typed native X6 branches retaining ordered signed paths, distinct branch identities, positive-rational BRC weights, multiplicities and provenance. The **declared source-only observer** is the partial permutation s of all appearing source IDs, ordered by their last occurrence from oldest to newest. For each nonempty U of at most two IDs, the oracle returns its latest present member or NONE if none is present. An algorithm may adapt queries; the number of occurring source IDs is not supplied. It must recover s exactly on every partial permutation. Concatenating whole histories respects the prior delete-then-append quotient.

Define Q2(k) as optimal deterministic worst-case number of singleton/pair queries. Define Cpair(k) as the exact optimal worst-case comparison count for sorting k distinct labeled objects whose entire support is known (the R186 comparator decision-tree invariant). In particular Cpair(1)=0. The proof below treats Cpair(k) as a finite minimax integer; it does **not** assume any closed formula for comparison-sorting complexity.

## Main theorem — exact all-k minimax equality

For every integer k>=1,

**Q2(k) = Cpair(k) + 1.**

In particular, known R186 exact values Cpair(1..5)=0,1,3,5,7 give new exact unknown-support values **Q2(1..5)=1,2,4,6,8**. For k>=2 the asymptotic class is Theta(k log k).

### Lemma 1 — adjacent comparisons are indispensable in any correct comparison sort

Consider a deterministic comparator sorting algorithm correct on every strict total order of k named elements. For any fixed input total order, the algorithm must directly compare each pair of adjacent names in the resulting sorted order.

**Proof.** Suppose adjacent names a_i and a_{i+1} were never directly compared along that execution. Swap them in the input strict total order, leaving all other relative comparisons unchanged. For every third name z, its relative order with the two swapped adjacent names is unchanged, because no z occurs between them. Hence every comparison actually made along the original adaptive transcript gives the same outcome on the swapped input (the only potentially different comparison is precisely their unasked direct pair). The deterministic algorithm would reach the same output, though the correct sorted outputs differ. Contradiction. QED.

### Lemma 2 — comparison lifting preserves the hidden absence boundary

Choose once and for all an arbitrary total tie-breaking order on the k source IDs. For a query of distinct x,y, define a derived binary strict comparator:

- If the oracle returns x, declare y < x.
- If it returns y, declare x < y.
- If the oracle returns NONE, both are absent; use their fixed tie-breaking order.

This comparator defines a strict total order: all absent IDs come first, sorted by tie-break, then all present IDs in chronological last-occurrence order. Consequently any correct comparison sort on this comparator returns a_1,...,a_k with an absent prefix of some length m. During its run, retain the raw oracle answer (including NONE) for every compared pair.

By Lemma 1 **every adjacent pair (a_i,a_{i+1}) was directly compared during sorting**, so its raw answer is already available. For i<m both names are absent and this answer is NONE; for i>=m at least the later a_{i+1} is present, so the answer is non-NONE. One singleton query on a_1 decides whether m=0. If it returns a_1, all names are present. If it returns NONE, then m equals one plus the number of consecutive leading adjacent comparisons whose saved raw answer was NONE. Thus the exact present suffix and its order are recovered without any further pair queries. QED.

### Upper bound

Select an optimal deterministic comparison-sorting decision tree with worst-case depth Cpair(k). It exists by the definition of the finite minimax, independently of having an efficient explicit construction. Simulate its comparison questions using the derived comparator of Lemma 2. Every such question requires one pair oracle call and yields both a binary comparator result and the raw answer; therefore at most Cpair(k) pair calls are used. After sorting, the recorded adjacent answers and **one** singleton q_{a_1} reconstruct all possible partial permutations by Lemma 2. Hence Q2(k)<=Cpair(k)+1.

For a practical explicit implementation, use ordinary mergesort instead of an optimal decision tree, obtaining at most M(k)+1 oracle queries, where M(k)=k ceil(log2 k)-2^{ceil(log2 k)}+1; this algorithm is the accompanying reference checker.

### Lower bound

R187 Theorem A shows that on every full-support permutation s=(s1,...,sk), any exact unknown-support algorithm must explicitly query singleton {s1}, since deleting only its oldest element leaves every pair query and every other singleton answer unchanged. Restrict the algorithm to all full-support permutations: singleton answers are fixed and their queries can be pruned from the decision tree, leaving an ordinary pair-comparison sorting tree. Some full-support input requires at least Cpair(k) pair comparisons, and its transcript also requires at least one singleton. Thus Q2(k)>=Cpair(k)+1. Combining bounds proves equality for every k>=1. QED.

## Verification and resource accounting

The file R188_optimal_lift_check.py implements top-down mergesort with the derived strict comparator and caches every raw pair result. On every resulting sorted list, it asserts that each adjacent pair was already compared, reconstructs the absent prefix using these recorded results plus precisely one singleton, and checks equality with the original partial source order.

All partial orders for k=1..7, totaling **16,071**, are checked using exact integer/source-ID operations, with zero failures, zero additional pair queries after sorting and exactly one singleton each. Maximum comparisons of the explicit mergesort by k are 0,1,3,5,8,11,14, matching its known comparison bounds for these k. The compact JSON outcome is R188_verification.json. These finite checks corroborate the constructive proof; the all-k theorem follows from the two lemmas and the lower-bound argument. No project-native brc_transport module execution or independent mathematical review is claimed.

BRC/X6 scope: source order is an observer-specific quotient; no arbitrary collapse of complete branch identities, paths, multiplicity, rational weight spectra or composite/joint relation fields follows. The stated minimal count measures queries to the selector, not full input transformation, selector implementation cost or bit complexity.

## Next scientific problem

For arbitrary subset-aperture b>=3 and unknown support, characterize the deterministic minimax Q_b(k) and optimal catalogs. The one-present-source special case Q_b(k | r=1)=ceil((k-1)/b) was proved in R187; the pair-only general case is now fully resolved. In parallel, test the source-selector adapter against actual src/enterprise_math/brc_transport.py with distinct tagged X6 branches and exact positive-rational weights. Historical researcher EM-DIRECT-BF4AD7 / SID MCP-46f202db13e64ad6b4c8860e06908245 / Activity RA-7A118452894D2600AE7DE5A2 are provenance only; no current author capability or active shared Task owner is asserted.