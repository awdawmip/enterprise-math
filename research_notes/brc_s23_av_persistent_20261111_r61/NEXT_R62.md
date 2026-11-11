# R62 — Age-centered persistent-index rebasing and full bit-cost crossover

Frozen scientific pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Source frontier: R60 Draft PR #2054 and R61 author-side source (this branch).

1. Construct a versioned anchor-rebasing scheme, preserving source identifiers and exact labels. Determine when to rebuild and amortize the real O(n log n) rebuild cost across a dynamic stream of source mutations.
2. Measure exact integer bit costs, not only tree word operations: parameter-enclosure precision, source timestamp-minus-anchor multiplication, precomputation, history boundary sort, updates, output and validation. Compare against R49 caching, R56 split-block, R58 grouped checkpoints and R59 static RMQ on identical workloads.
3. Strengthen R61-C from index ordering to an `x`-aware per-label membership certificate. Locate the exact observation-phase boundary exceptions and whether sparse checkpoint queries can use less precision than a full-vector query.
4. Examine branch IDs and repeated timestamps with explicit source identities. Preserve future arbitrary deletion and historical version roots.

R61 status: author proof and exact finite verification, independent review pending. Shared S23 Owner/CLAIM must be checked through native live authority before any formal shared task/result mutation. Preserve P000 and original frozen science.
