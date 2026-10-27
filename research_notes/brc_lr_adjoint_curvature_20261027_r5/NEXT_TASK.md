# R5 next problem: rational signed Bellman curvature chambers

Status: author proposal only; no canonical Task/CLAIM/Result/review.

**Mother question.** Can a strictly positive rational N=3 two-measure tree have `conv(O_LR)=O_full` but `O_LR != O_full` with all seedless LR local randomization probabilities genuinely ranging over the full real interval [0,1]?

**Verified frontier.** Adjacent `PROOF.md` derives the exact BRC occupancy adjoint identity and affine-curvature inequality for every real behavioral policy. The exact 12-leaf witness gives `K_a=(1/4,1/2,1/4)`, `K_b=(1/8,3/4,1/8)`, `Y=(1/2,1,3/2)`, and `J_full-J_bar=-7/1024`. This is a projection error, not an all-support equality certificate.

**Smallest next proof.** For a fixed rational N=3 tree and deterministic seedless LR policy q, explicitly dualize the rational LP
`rho(lambda)=min_{A,B,M,m} M-m` subject to `m <= V_{t+1}^{q,lambda}(y)-A-B*y <= M` for every successor y. Prove piecewise rational-linearity and positive homogeneity in signed lambda, derive rational dual witnesses and the exact zero-curvature subspace. Compute the complete chambers for the three-point hinge in the existing witness.

**Next candidate gate.** For a distinct rational N=3 candidate, enumerate all full and LR deterministic four-vectors; use exact rational convex-hull membership/separation certificates for every full deterministic vector. If all supports are equal, use real polynomial feasibility/quantifier elimination for a missing vector in the seedless image. Neither a finite parameter grid nor a positive curvature bound proves nonattainability or hull equality.

**Reuse and authority.** Read predecessor `d246c865427d3383570f83778dc18e05995a4f3a` and this result first; use weighted BRC/provenance and T6 observer-safe quotient. Preserve P000 and ACTIVE worldview, strict native transfer boundary and real owner/CLAIM/Driver gates. Persist actual next source and evidence in project research_notes; add a knowledge journal event.
