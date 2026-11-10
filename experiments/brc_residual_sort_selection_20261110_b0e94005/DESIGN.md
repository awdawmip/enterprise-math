# Selection and output experiment: initial design

Parent question: improve complete ascending integer sorting through residual
classification. This phase follows adaptive experiment commit
1001e80fd510c8de6a9761dc20068e0e3c8c671d. Prior sources and evidence stay unchanged.

The three candidates separate two mechanisms:

1. selection_fused_1024: exactly the phase-two combined selection policy, with
   a bucket-level fused histogram/residual emitter.
2. selection_density_gap_1024: a new sample-coverage/counter-width selector,
   followed by the frozen separate counting emission and backward merge.
3. selection_combined_1024: the new selector and fused emitter together.

New selection retains the existing original compact/full-grid fast paths. An
overbudget grid is considered by density packing: descending exact sample mass
per padded width, ties by larger mass, smaller width, then original bin index.
Whole bins that fit the remaining budget are kept; nonfitting bins are skipped.
Commit requires at least ceil(original sample size/2) learning observations.

If selection fails, sort the original sample once and choose the largest
admissible positive adjacent gap in the current sample window. At least one side
must retain ceil(original sample size/2) observations. Retain the larger side;
equal side mass retains the lower side; equal gap sizes use lower gap index.
Rebuild with frozen grid/padding helpers and reconsider compact/grid/density.
At most three such repairs are tried. The first feasible model receives one
actual scan. The existing actual-half residual rule and unchanged-input radix
fallback remain decisive.

Fused output uses ordered disjoint retained bucket intervals. At each bucket,
lower_bound in the remaining sorted residual finds the preceding residual block;
copy it, then emit exact counts for the bucket. Copy trailing residuals last.
Every input occurrence is written to its final output position exactly once.
No-residual nodes use the existing emitter. Output statistics distinguish
semantic counted values from actual prefix/merge/direct output writes.

Evaluation initially specifies eight exact known phase-two calibration banks,
twelve fresh seed-bank conditions and four deterministic mechanisms. All23 old
implementations are preserved as controls. Formal timing uses8 banks and7 rounds,
including input copy, model construction, allocations, full output and teardown.
The implementation and fresh recipes will be frozen before fresh generation or
timing. Any calibration-driven change will be recorded explicitly.

Separate theoretical analysis studies fractional-knapsack upper bounds and
mass-index dynamic programming on the fixed learned grid. Those methods are not
part of the initial three timed candidates. Their role is to diagnose where
density selection can or cannot meet the sample-mass threshold.

Researcher-ID: EM-DIRECT-10677F / TASK_RESEARCH.
Activity: RA-851F29EFE6B4190069FE0D3B.
