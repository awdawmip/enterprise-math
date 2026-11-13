# R65 continuation — subtree exclusion and adaptive precision

Scientific input remains frozen: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Predecessor: R64 sparse-interval certificate, researcher `EM-DIRECT-E75625`, activity `RA-3AE5D6FCA0C04F1999E69F27`.
Parent: source-labelled auxiliary S23/AV circular rotation observer; original P000 and native X6/BRC typing unchanged.

## Exact unfinished questions

1. **Certified subtree exclusion.** Given an R63 persistent root constructed at exact `theta0`, queried original label `z`, selected winner `t*`, parameter interval `I=[L,U]`, and a subtree whose `max_t>t*`, develop a certificate that no event in this subtree can enter the moving arc `A_z(theta)-b(j,x,theta)` throughout `I`. Start with a small finite family and explicit reachable circular enclosures for timestamps. Show the exact conditions that allow using cached subtree time maximum and identity even when phases reorder within that subtree.
2. **Adaptive repair.** If the R64 selected-source certificate is inconclusive, bisect the rational parameter interval. Reuse all proven history and source-boundary noncollision certificates at surviving subintervals, and identify exact collision endpoints. Do not assert that every interval can be finitely resolved when a parameter lies on an actual boundary event.
3. **Branch-typed persistence.** Support unique keys `(phase,t,branch_id)` and exact branch-specific deletion. Verify that the age-only max-time quotient is used for readout but that future deletion retains identity.
4. **Full integer-bit comparison.** Compare to R49/R56/R58/R59/R60/R61/R62/R63 under matched `m,n,U,Q,B` and precision widths. Count phase construction from original source times, timestamp index construction, historical-boundary sorting, exact affine checks, interval splits, source updates, output and independent verification. Avoid word-operations-only speedup claims.

## Concrete initial experiment

Reuse R64's counterexample `theta0=1/30`, `theta1=1003/30000`, `m=13`, `j=10000`, `x=8/15`, label `z=12`, events at timestamps `9,15,6042`. First prove an interval exclusion/pruning rule that detects the uninspected 6042 leaf's migration across the lower arc endpoint; then add a fourth newer source whose phase changes order without changing membership, demonstrating safe pruning.

Continue to preserve exact source/branch provenance, and distinguish local authored proof, finite tests, independent mathematical review, and formal task Result.