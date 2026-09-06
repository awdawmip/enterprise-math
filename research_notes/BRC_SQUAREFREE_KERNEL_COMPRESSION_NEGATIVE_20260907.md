# BRC Squarefree-Kernel Multiplier Compression — Round 8 Negative Result

Status: `FINITE FALSIFICATION / TRAINING COMPRESSION DOES NOT GENERALIZE / NO PRODUCTION TOOL`
Date: `2026-09-07`
Parent line: BRC multiplier basin / squarefree phase calculus

## Question

Every multiplier has a canonical decomposition

`m = a^2 d`

with squarefree kernel `d`.  Since the `a^2` part is an exact BRC square
refinement, can a small set of kernels `d` replace a long multiplier scan while
all square refinements `a^2 d <= M` are retained?

This would be attractive because the expensive irrational direction would live
only at the kernel level.

## Experiment

Horizon:

`M=1000`.

The exact odd-N mod-8 representative set has 625 multipliers:

`m mod 8 in {0,1,3,5,7}`.

Training population:

- all distinct semiprimes `p*q` with primes `101<=p<q<=997`;
- 10,153 values.

For each squarefree kernel, record which training semiprimes have at least one
immediate multiplier-Fermat square-gap factor witness among that kernel's
multipliers.  Greedily select the kernel with largest uncovered training gain.

The greedy training set is

`(1,13,14,3,15,2,5,6,30,22,105,33,7)`.

These 13 kernels induce only 98 of the 625 representative multipliers and cover
all 10,153 training semiprimes that the full horizon covers.

That training compression looks very strong, so it was tested without
re-fitting on two disjoint larger prime ranges.

## Validation

### Validation A

- 20,000 deterministic distinct prime pairs from `[1009,4999]`;
- seed `20260906`.

Full 625-multiplier horizon hits:

`19,481 / 20,000`.

The fixed 13-kernel / 98-multiplier family hits:

`16,513 / 20,000`.

Thus it retains

`16,513 / 19,481 = 84.7646%`

of the full-horizon hittable population.

### Validation B

- 30,000 deterministic distinct prime pairs from `[5003,19997]`;
- seed `20260907`.

Full 625-multiplier horizon hits:

`26,399 / 30,000`.

The same fixed 13-kernel / 98-multiplier family hits:

`14,591 / 30,000`.

Thus it retains only

`14,591 / 26,399 = 55.2710%`

of the full-horizon hittable population.

## Decision

The dramatic training compression is not distribution-stable.

The squarefree-kernel decomposition remains exact and useful as a typed BRC
coordinate, but **a small learned kernel inventory is not a safe replacement
for the long multiplier horizon**.

Kill the production proposal:

`SMALL_FIXED_KERNEL_SET -> UNIVERSAL_LONG_MULTIPLIER_COMPRESSION`.

Do not infer that squarefree kernels are irrelevant.  The negative result is
narrower: fixed kernel selection learned from one bounded factor-ratio
population does not preserve coverage under substantial distribution shift.

## Relation to current production tools

- No existing BRC theorem is retracted.
- `m=a^2 d` exact state composition remains valid.
- Pairwise root/remainder transport remains the current exact nonmonotone
  execution improvement.
- The newer horizontal/vertical wheel remains a separate two-dimensional search
  surface.
- No new executable tool is registered from this negative result.

## Artifacts

- `experiments/brc_squarefree_kernel_compression_probe.py`
- `research_artifacts/brc_squarefree_kernel_compression_probe_20260907.csv`

## Next

For the `m>100` frontier, prefer one of:

1. a table-free exact/conditionally-bounded tail predictor whose validity is
   certified from the current `(J,R,m,N)` state; or
2. a search family justified by an N-independent theorem rather than fitted
   kernel coverage.

Do not spend further cycles optimizing the 13-kernel family unless a new
independent structural theorem changes the selection criterion.
