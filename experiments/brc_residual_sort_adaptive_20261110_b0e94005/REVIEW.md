# Author-side review record

The parent delegated kernel implementation, harness integration and a separate
read-only review to three collaborating agents. This is author-side review in
the shared context, not independent external acceptance, formal proof-assistant
certification or an algorithmic novelty determination.

Before measurement, the review covered exact histogram/residual membership,
original-input preservation during early abort, inclusive trim ties, original-S
sample-mass accounting, descending-width pruning with deterministic ties,
non-mutation on rejected proposals, the one-actual-scan rule, recursion contraction,
root versus recursive diagnostics, and the nullptr timing path. The final
optimized and sanitizer verification receipts document the executed checks.

The reviewer authored THEORY.md with the parent's authorization and the parent
read it in full. The positive construction derives its actual spill bound from
the input population and overwrite count, rather than assuming sample coverage
equals population coverage. The abstract greedy counterexample is explicitly
limited to the selection rule and is not presented as a generated benchmark.

After the final benchmark, the reviewer independently recomputed the summaries
from all552 raw rows without compiling or running a sorter. The recomputation
checked all seven-round medians, empirical quantiles, extrema,24 condition
summaries, stage aggregates and the24 Markdown table rows. It also reconciled
the2274 node rows and1372 attempt rows. No numerical discrepancy remained.

The central result was independently confirmed: for the12 fresh seed-bank
conditions, the combined variant has11 median wins and a1.746104542 ratio
against previous compact, but1 median win, no ratio>=1.1, and a0.632727347
ratio against the per-condition fastest of20 frozen controls. Inverse geometric
elapsed-time ratios are approximately0.57270 and1.58046 respectively. The latter
means about58.0% longer elapsed time, not36.7% longer.

The reviewer checked all five frozen local file hashes,10 dependency hashes and
the optimized binary hash against actual files. They match; the recorded freeze
precedes the final run's start by88.185 seconds. This establishes consistency of
the retained files and receipts, not additional external timestamp attestation.

The final traces support the theoretical mechanisms. The central-four-poison
case selects two omitted bins,900 retained learning observations and35644
counter cells, with actual residual/child size9993. The sample-mass-rejection
repair uses the second trim level and actual residual5932. The hidden-majority
case accepts a model but stops at50001 residual occurrences, has child_size0,
and makes only one model attempt. Model selection and actual scan acceptance
are therefore kept distinct in both reporting and verification.

All final performance measurements were run serially by the parent. Review
work did not launch a compiler or benchmark concurrently with those timings.
No must-fix correctness, hash, numerical or proof-text error remained at the
end of this author-side review.
