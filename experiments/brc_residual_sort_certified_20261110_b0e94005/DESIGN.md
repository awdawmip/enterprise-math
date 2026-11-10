# Fixed-grid half-mass feasibility repair: initial design

This phase continues the frozen phase-three selection/output implementation.
It adds one fixed candidate, `certified_combined_1024`, alongside all26 preceding
candidates in the same binary. Full ascending `uint64_t` multiset output remains
the observable result. No associated-record stability is claimed.

The policy is fixed before any phase-four fresh-bank generation or timing:

1. Preserve phase-three compact, whole-grid and successful density-greedy paths.
2. After a failed density half-mass proposal, inspect individually feasible bins
   for the best singleton; accept it if its original-sample half-mass gate passes.
3. Compute the exact integer floor of the fractional-knapsack upper bound,
   excluding individually infeasible bins. Reject this grid if the bound is
   below ceil(original S/2).
4. For the remaining ambiguous grid, run the exact mass-index dynamic program
   and reconstruct a maximum-sample-mass subset within the counter budget.
5. After an infeasible fixed-grid decision, use the unchanged phase-three
   majority-gap sequence. At most three gaps, first feasible model, one actual
   scan and actual residual<=floor(n/2) remain fixed. Use the same fused emitter.

This is a complete decision procedure for the fixed whole-bin sample-feasibility
problem. Only the DP branch claims maximum sample mass. It does not optimize
actual population coverage, different numerical grids, or measured runtime.

## Planned matrix

20conditions,27candidates,8banks,7randomized-order within-process rounds. Each
round uses a nominal12ms target rounded to whole-bank cycles. Input copy,
learning, allocations, exact repair, scanning, recursive sorting, full output
and destruction are included. Diagnostics are collected outside timed calls.

Ten known conditions reuse phase-three banks exactly: popularwide, rarewide,
12% asymmetric tails,15% high tails,15% low tails, uniform uint64, narrow offsets,
interior contamination,128clusters with12% tails, and the densitymasswidth
mechanism. These are labeled known calibration, including the inherited
deterministic witness. They are not new evaluations.

Six fresh targeted bank families:

- Three bins with actual masses40%/30%/30%, aligned coarse-bin origins.
- The same population proportions with an internal coarse-bin offset+2048.
- Three bins with actual masses20%/40%/40%.
- Three bins with actual masses44%/28%/28%.
- Eight bins with45% in a wider dominant interval and55% across the others.
- A scaled three-bin40%/30%/30% family at one million values.

Fresh families use natural deterministic-position samples of randomly generated
and shuffled populations; no sample-position endpoint prescription. Their seeds,
integer geometry and exact population allocation will be recorded in the frozen
harness before they are generated. They are targeted distribution families
motivated by the selector theorem, not a deployment-population sample.

Four separate deterministic mechanisms:

- Exact DP witness: masses410/307/307; padded widths30000/25000/25000; C50000.
- The same prescribed sample with hidden actual majority in the rejected bin.
- Best singleton witness: masses1000/24, padded widths50000/9.
- Fractional rejection: masses341/341/342, each padded width50000.

Primary comparisons are the fixed preceding `selection_combined_1024` and the
fastest median of all26 frozen preceding candidates for each condition. The
latter is a retrospective reference, not an implemented algorithm selector.
No best-of-new-candidates aggregation is needed because there is one new policy.

## Validation and evidence

Before performance, verify exact small-subset feasibility and reconstruction,
fractional upper bounds, failed-model nonmutation, all-node actual membership,
half+1 rejection, maximum values, diagnostic/nullptr parity and old-model parity
when no successful repair changes a node. Run optimized and ASan/UBSan builds.
Fresh performance banks are excluded from pre-freeze validation.

New diagnostics retain old greedy failures as failures. A separate certified
trial records singleton/fractional/DP outcomes, selected repair, DP state visits,
logical vector capacities and peak repair auxiliary bytes. Actual scan acceptance
remains a distinct event. Logical vector capacity is not process RSS.

Researcher-ID: EM-DIRECT-10677F / TASK_RESEARCH.
Research-Activity-ID: RA-851F29EFE6B4190069FE0D3B.
