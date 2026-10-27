# Portable N=4 successor: precise residual observability criterion

**Mother question.** Characterize the minimal future-relevant branch information needed to preserve the entire attainable four-vector set (P(decide Q),Q(decide P),E_P tau,E_Q tau) for all randomized finite-horizon stopping and decision policies.

**Source/frontier:** PROOF.md and VERIFY.py in this directory; prior N=3 one-bit repair: research_notes/brc_n3_rational_lifting_onebit_repair_20261026_r5. All assumptions are positive rational conditional branch weights, fixed horizon N=4, nonanticipativity, both P and Q known, terminal decision by t=4. Example: L1(a)=L1(b)=1; b=1[first=a] distinguishes them but L2(ax)=L2(ay)=1 while time-3 L distributions differ; support gap exactly 1/96 under J=e_P+e_Q-(33/8)E_P tau+(17/4)E_Q tau. An extra t2 bit separating ax/ay repairs this tree only.

**First unanswered question:** For an arbitrary specified same-LR time-2 fiber in a positive rational N=4 tree, find the exact necessary and sufficient Bellman root-envelope criterion for identifying all its histories without losing any reachable four-vector. Can that all-real-coefficient criterion be reduced to finitely many rational polyhedral breakpoints, including root early stopping and signed support coefficients?

**Next computations/proofs:** (1) derive the finite-dimensional support-polytopes for complete and compressed policies, including conditional occupancy-flow updates; (2) give a complete exact LP/dual witness algorithm, then prove correctness of the resulting minimal deterministic partition search; (3) bound bit count and rational denominator growth for a specified tree; (4) test degeneracy with equal-LR hidden histories but observationally identical future kernels.

**Verification requirements:** exact P,Q tree, source-visible rational proof/certificate, reproducible checker with explicit finite scope, and the precise quantifiers for policy class and observations. Do not call this native P000, X6, Heartbeat, or formal Claim/Result/Driver acceptance. The native session start was denied under STATIC_READONLY_SCOPE_DENIED, operation_sent=false; only author-level GitHub storage is currently evidenced.

**Completion threshold:** either a proved full characterization with exact algorithm and a nontrivial instance, or a new sharp counterexample narrowing an explicit conjecture. Preserve the completed 32-leaf support-gap result without re-running it as new work.
