# Stage283-B — Non-serial BRC gate composition / minimal port residual

PROPOSED_PORTABLE_AUTHOR_HANDOFF / UNREVIEWED / NOT_ADMITTED.
Source: Stage282-B same PR #1571; preserve separate open Stage278-A N=12 Bellman next-face problem.

**Exact verified starting point.** In a strict serial two-gate finite ordered-history tree with source-blind coins x,y, all terminal observer expectations have form c_i+d_i*x+e_i*x*y. The feasible causal simplex after lifting z=xy is exactly 0<=z<=x<=1. Stage282-B's positive nonIID depth3 counterexample has global minimax observer distortion 3/16 uniquely at (x,y)=(1,1/2), Stage279 local action-mass risk 5/16, and Stage281-style original-occupancy two-pass observer risk 9/32. Read PROOF_STAGE282B_CAUSAL_SIMPLEX.md and REPRO_STAGE282B.py, not just the PASS marker.

**New question.** Give the smallest explicit finite positive-rational non-serial DAG with two depth-homogeneous control coins that breaks the prefix-simplex LP representation. A useful first candidate reuses y twice on one complete ordered path, producing xy^2. Introduce v=xy^2; a relaxation with x,z,v must retain equality x*v=z^2 (when x>0), not merely positivity. Seek a rational target and bounded terminal observer with a strict exact optimum gap between relaxation and implementable coins, or prove a sufficient BRC port-factorization law for a broader class of branching DAGs.

**Required proof/certificate.** Specify complete positive source masses, ordered path transitions, action semantics and observer horizon; give a valid global lower bound or constructive obstruction, explicit rational witness, and independent executable Fraction ordered-history replay with captured stdout. Do not label a finite grid as a proof of continuous optimality. Report the smallest information lost by the attempted quotient, and distinguish positive-mass BRC from signed/phase cancellation.

**Native transfer is separately pending.** Only transfer to Heartbeat-world X6 with an actual registered six-field nonnegative address codec, a declared 3D slice/third component, time/port/ordered-axis path mapping, allowed operations and a relation-preservation proof. P000 and ACTIVE worldview are protected. Native session/claim cannot be inferred from a GitHub author commit.
