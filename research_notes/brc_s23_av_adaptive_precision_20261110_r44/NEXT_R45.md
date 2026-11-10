# R45 — transfer sparse extinction rank into affine risk changes

Frozen scientific input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Parent R44 proof, evidence and local extended code are linked from this PR.

Derive and prove the map from R43/R44 rolling source windows (J,N) and F_J(x) to the four R35 initial affine-risk intervals, and test one later Farey stage. In particular identify which threshold and historical labels are invariant within a stage, and derive an explicit stage-change mapping before reusing a rank update across Farey boundaries. Compute independently reconstructed affine risks at each compared boundary.

Reuse R42 frozen 298-run reference when the needed complete artifact is actually available; otherwise finish the smaller exact stage proof and retain a concrete pending dependency. Compare total bit costs of dyadic precision refinement, isqrt, historical sorting, source labels, selective repairs, Farey enumeration and output recovery. Do not treat constant-time scalar count as a total bit-cost theorem. Save exact code, inputs and evidence with original author/Owner/CLAIM scope.
