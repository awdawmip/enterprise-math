# R5: Eight independent two-arc switches for the 954-event predecessor kernel

2026-11-16 · Frozen scientific input: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
Evidence: **AUTHOR_PROVED / EXACT_FINITE_EXHAUSTIVE / NOT_REVIEWED**.
Scope: derived one-dimensional indexed-event, radius-two nearest-center observer. No assertion about native X6/BRC or physical dynamics.

## Previously verified input and current question
The source yields 954 ordered event positions (final coordinate 1065), 28 length-three candidate gaps, and eight effective cut IDs `U=(3,8,9,10,15,17,25,27)`. The original recurrence and batch-count frontier are preserved at `148d21658eae195cbe7395b6851d375c53bea87e:research_notes/portable_direct/r5_fused_three_count_dp_20261116/RESEARCH.md`. The question is whether changing closure bits demands rebuilding an entire predecessor graph.

## New exact theorem
Let `b` be any of 256 effective closure configurations. Let `P_b[j][i]` denote the transition from previous center i to new center j, whose span is at most 7, with all intervening events within distance 2 of an endpoint; its cost is the sum of minimum endpoint distances. Then

```
P_b = P_0 union (union over t:b_t=1 of E_t)
|P_b| = 4383 + 2 popcount(b).
```

Each `E_t` consists of **exactly two new, fixed-cost arcs** listed in `EXACT_EIGHT_SWITCH_KERNEL.json`. No base arc disappears or changes cost. Initial-one-center and terminal-suffix kernels are identical for all 256 masks. Therefore a complete parametric predecessor representation uses **4,383 permanent weighted arcs and 16 conditional weighted arcs**. All eight conditional switches are independent at the kernel level.

## Proof
1. Closing one effective cut at index c subtracts one from coordinates on its right. Only the adjacent gap `(c,c+1)` decreases from 3 to 2; every other adjacent distance stays fixed.
2. The distances strictly between consecutive effective cuts are exactly `75,5,6,82,58,230,49`. Even with both surrounding gap lengths decreased to 2, an index interval crossing any two effective cuts has coordinate span at least `2+5+2=9>7`. No admissible predecessor arc can therefore depend on two closure bits simultaneously. This remains true under any choice of the other six bits.
3. Exact comparison of `P_0` against each of the eight single-bit predecessor maps finds just the two additions `E_t`, with neither deletions nor changed common-edge costs. Each comparison uses the complete original rational/int predecessor test; the finite source reconstruction is reproduced by the verifier. Step 2 upgrades those eight single-bit equalities to the stated formula for every mask.
4. The effective gaps are far from the beginning/end, while initial/terminal admissible spans are at most 2. Neither endpoint kernel crosses an effective cut. The exhaustive checker independently re-evaluates all 256 full kernels and all endpoint arrays against the assembled formula.

## Exact independent-output scope
`VERIFY_R5_EIGHT_SWITCH_KERNEL.py` reconstructs the complete 15-term frozen source via 32,767 nonempty subsets, validates group sizes 538/298/229, the 954 events and 28 gap positions, computes the base kernel and eight toggle kernels, assembles each of the 256 predicted kernels from the 16 fixed arcs, and checks all 256 full actual predecessor graphs arc-by-arc and cost-by-cost. It returns `PASS_R5_EIGHT_SWITCH_KERNEL_EXHAUSTIVE`. Local executed Python source SHA-256: `1e917591477c84855b4850b4e35e33c782860a40d83e5e77813767997c31f3db`. Local full output SHA-256: `9ff6be65ca72800e95e991a37bda223bfd03652d072952ed1751ccef2cee83bf`. Integer and `fractions.Fraction` arithmetic are used. Two arcs are enabled for each selected bit, giving exactly 4,383 to 4,399 arcs across configurations.

## Boundaries and continuation
Kernel locality does **not** establish local influence on the min-plus/tie-count DP output: an added arc may influence many future layers and states. No global computational complexity improvement or BRC-native equivalence is asserted. The exact proof here uses finite enumeration of each single-bit effect and a noninteraction lemma, with a redundant 256-mask full-kernel check; independent mathematical review remains pending.

Next: replace 256 independent graph preparations with one 4,383+16 parametric graph and measure complete preprocessing, big-integer arithmetic and output recovery for all 256 masks. Test any proposed sparse DP-update technique against the full exact counts before claiming a speedup. Preserve the frozen input and prior observation Pareto cost definitions.

Research identity: R5 historical contribution `EM-DIRECT-B78E55` (provenance only); no authenticated current formal CLAIM/Result/Review is implied by this independent GitHub research note.
