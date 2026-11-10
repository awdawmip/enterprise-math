# BRC-X6: full-positive original-native rational strategies with denominator D≤12 have exact integer policy decompositions

2026-11-10. AUTHOR_PROVED / FINITE_EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED. Author-only portable mathematical evidence; no Source CLAIM, checkpoint, Result, review or admission is asserted.

## Frozen native problem and exact result

Science pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Use original 96 ports, six separately labelled actions, source ports (6,7,28,29), signed source charges (+,-,-,+), nine frozen roots, and all tagged destination/observer coordinates. Let the 38 lawful four-action deterministic strategies be `v_0,...,v_37` in lexicographic order; their original 24-coordinate incidence matrix is `C in {0,1}^{24x38}`.

**Finite integer-decomposition theorem.** For every integer `6 ≤ D ≤ 12` and every `b∈Z_{>0}^{24}` with each source's six coordinates summing to D, if the exact signed nine-root native joint flow of b vanishes, then there is an integer vector `n∈Z_{≥0}^{38}` with `C n = b`, `sum_j n_j = D`. Conversely, any such nonnegative legal integer policy decomposition satisfies the root-wise native conservation. Thus every full-positive original-native lawful rational strategy x=b/D with D≤12 admits at most D≤12 distinct legal deterministic policies.

**In particular, a full-positive original-native x with `minSupport(x)=13` has reduced denominator at least 13.** This is an exact lower bound for this frozen four-source/nine-root model, not an assertion about another model or about D≥13.

## Exact construction, algorithm and counts

Let `J=(1,...,1)∈Z^{24}`. There are exactly 268 perfect six-policy covers of J in the frozen 38-policy system; a concrete one uses policy IDs `(0,9,13,19,27,37)`. For D=6+m, 1≤m≤6, write b=J+r, where each source's six nonnegative residual coordinates sum to m. Native conservation is linear and J is conserved, so r is conserved.

Represent each source residual by an m-element multiset of actions 0..5, of which there are `binom(m+5,5)`. For each of the nine roots compute its exact original `(root, destination port, full joint observer)` signed-flow signature. Compute the first two source signature sums, hash them, and match with negatives of the latter two source sums; the matches enumerate all exactly conserved residual vectors. In a separately generated collection, enumerate all multisets of m among the 38 legal native policies and record their complete four-source action multisets. For every m=1..6 these two **sets of native integer residual vectors are exactly equal**, which supplies the m native policy terms. The J cover supplies the other six, proving the theorem.

| D | m | conserved full-positive 24-count vectors | vectors constructible from m lawful policies | all m-policy multisets | vectors with a unique m-policy multiset |
|---:|---:|---:|---:|---:|---:|
| 6 | 0 | 1 | 1 | 1 | 1 |
| 7 | 1 | 38 | 38 | 38 | 38 |
| 8 | 2 | 605 | 605 | 741 | 472 |
| 9 | 3 | 5,672 | 5,672 | 9,880 | 2,830 |
| 10 | 4 | 37,184 | 37,184 | 101,270 | 10,950 |
| 11 | 5 | 188,312 | 188,312 | 850,668 | 32,454 |
| 12 | 6 | 784,536 | 784,536 | 6,096,454 | 80,880 |

Each vector is distinguished by all 24 original-source/action integer counts. This is a complete finite enumeration of the stated denominator range.

## Independent exact audit

The author ran two different integer verifiers.

* A direct 81-key original-root signed-flow hash join, plus an independently enumerated m-multiset of the 38 lawful policies, compares the *entire* conserved/constructible residual sets for m=1..6. Checks: exact 38 policies; nine roots; J conserved and 268 perfect covers; no unmatched/duplicate conservation solutions; checksum `sum(multiplicities)=binom(37+m,m)`. Output certificate SHA-256: `1246ca64fc2b0ea314841e83f16fea8b9eb68f037ee323ebcd6cf0f1e1de3f61`.
* A separate SymPy/strict-rational calculation reconstructs C, establishes `rank(C)=13`, computes a primitive integral basis of the eleven-dimensional left nullspace, and uses **11 dual integer coordinates rather than the 81 original flow keys** to recount D=7..12. Its independent totals exactly match the first verifier.

The frozen kernel copy `frozen_native_kernel_prefix577.py` has SHA-256 `d2b84a22928e8160315e8578ea99a62f91b8688462d2b6451a71eef871df88b0`, identical in nine previously retained author portable packages. The local reproducible bundle contains the precise kernel copy, both executable verifiers, the JSON certificate, a full Chinese proof and an integrity manifest.

## Contribution boundary and next question

Earlier U12/δ rank-13 extension results and the D511 examples are **prior work**, not claimed here as newly discovered. The current increment is the exact D≤12 full-positive integer-point enumeration and its constructive ≤D decomposition, which makes D=13 the first remaining possible reduced denominator for a 13-minimal strategy under the stated model. The next discriminating test is D=13 with a complete 38-policy min-support certificate, or an extension of this special-case integer-decomposition method.

UR V2 four-file original remains a separate unresolved source-recovery objective: 94,687 bytes, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`. Mathematical UR work should not be repeated for provenance repair.

Source Task native session/CLAIM remains unverified. This evidence is NOT_ADMITTED; this GitHub author note is not formal Source publication or review.
