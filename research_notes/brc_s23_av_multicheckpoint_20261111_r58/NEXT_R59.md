# R59 — checkpoint-sparse youngest-only source observer

Current frozen scientific pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Authors' predecessors R56, R57 and R58 are preserved at their immutable commits.

R58 proves the Q-checkpoint **full-owner and youngest-array** offline bound O(kmax+Q(H+m)) after initial setup, with reversible cut tape. The per-checkpoint output contains H+m fields, so there is an output Omega(Q(H+m)) bound. The theorem does not price an m-only youngest observer this way.

Next discriminating mathematical unit: find an exact youngest-only checkpoint data structure that outputs Qm historical-label youngest ages while avoiding an H scan at every queried checkpoint when possible. Prove its observer preservation and update costs. Experiment on small m/H and frozen S23 endpoints, including m=1/H=1 and arbitrary checkpoint ranks. Compare with R49 state caching and R56 split-block direct endpoint classification including parameter construction, bit lengths, and output/replay costs.

R58 additionally proves top-(d+1) timestamp retention for up to d arbitrary deletions, while single-latest retention fails after deleting latest timestamp from {1,2} vs {2}. Use this witness in future-operation observer-sufficiency testing.

Independent mathematical review and shared-task owner verification remain pending; do not infer CLAIM/Result/Review or P000 changes from this research note.
