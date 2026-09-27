# One-window reduction: shared-context proof review

Status: **READ_ONLY_SYMBOLIC_REVIEW / SHARED_CONTEXT / NOT_ADMITTED**.
No scientific calculation, native replay, web query or source modification was performed. This reviews the proof, not an execution of the proposed replacement.

Reviewed `ONE_WINDOW_REDUCTION.md` at SHA-256 `ee13a8d8bc03dd8359f3a3a3d80ac7cfdc9a0094f19deeb2af91189d75a42095`. Also read the frozen `SIGNED_GAPS_REFINEMENT.md` at `1a84d09ed1fecdf7a42de9c1b1e48da881c820e544214011703c79a688938776` and the actual `interval_count`/`window_weight` methods in `sep27-qft-adaptive/nonzero_structure/typed_floor_moments.py`, whose pinned source is `633502c9b484e60e5dc5fcf6edd0420f12d52c33c43e88851b9e1e6465ea94a2`.

**PASS within the stated scope; no material mathematical defect found.**

For the contiguous stride-one interval, the four bit-pair classes are a disjoint exhaustive partition. The two equal-bit classes each have the same unsigned count J0. Hence the full interval count is T_L=2J0+Jplus+Jminus and the signed count is exactly K=4J0-T_L. This identity does not require an odd R, invertible stride, a no-wrap promise, positivity of K or an order oracle. The proof deliberately restricts itself to stride one; the older typed gcd/inverse stride reduction can be a separately charged caller step if that wider interface is later used.

The interval formula agrees with the actual interface: for L=qR+u, residue multiplicity equals q plus the indicator of [0,u), whose cyclic autocorrelation is max(u-r,0)+max(u-(R-r),0). At r=0 this correctly contributes u once; at R=1 it yields L^2. The endpoint sign positions k=0 and k=g-1 correspond respectively to U=1 and H=1 and remain valid arguments of `window_weight(H,U,2,R,r,0)`. No empty-gap case is claimed because g>=1.

The raw scaling remains 4^-g. The output K may be negative, so a replacement wrapper must retain the signed outer observer and must not copy the nonnegative guard belonging to an individual unsigned window count. These requirements are already explicit in the proof. Reducing three outer window queries to one plus a paid interval count is established; it does not imply a fixed elapsed-time ratio because the existing window routine has inner interval calls, memoization and receipt costs.

The proposed comparison with the frozen three-window payload is a future bounded validation target. This review does not upgrade it to completed execution, an arbitrary Walsh-mask algorithm, a multiple-gap contraction or a Shor complexity result.

Global-Knowledge-Sync: main@b98c6e4 / GLOBAL_KNOWLEDGE_V1
