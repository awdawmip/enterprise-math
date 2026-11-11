# R63 — persistent circular rebasing and exact bit-cost crossover

Frozen science pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Consume R61 PR #2055 and R62 author results at this branch.

1. Implement a persistent circular-order source tree with movable cut (split/join or equivalent), using the R62-C exact anchor rotation identity. Check inherited immutable roots after forks and prove structural O(log n) operation counts; separately measure integer bit costs and interval validity for inserted sources.
2. Implement interval-adaptive query-selective certification from R62-A, refining only the source/boundary pairs that affect the youngest age at requested historical labels. Compare precision and full costs with nonselective certificates at identical inputs.
3. Support repeated source timestamps with distinct branch IDs, stable tie ordering, deletion, historical version roots and future provenance readouts.
4. Compare matched workloads R49 caching, R56 split-block, R58 grouping, R59 static, R60 dynamic and R61 persistent, including construction/preprocessing, precision, updates, requested output size, risk observation and verification.

Status: author proof + finite exact experiments. Native Researcher-ID/activity and S23 Owner remain unverified; no formal shared CLAIM or independent review asserted. P000 protected.
