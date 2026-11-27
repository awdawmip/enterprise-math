# Stage284-B — joint compatibility of repeated-port convexifications

Status: `PROPOSED_PORTABLE_AUTHOR_HANDOFF / UNREVIEWED / NOT_ADMITTED`. Scientific predecessor: Stage283-B exact tied-port DAG proof + Fraction witness, current Draft PR #1571. Separately preserve the Stage278-A N=12 Bellman next-face task.

## Exact proved input (do not recalculate without a changed premise)

For source-blind fixed parameters `x,y∈[0,1]`, terminal types from two consecutive visits to the tied y port have `(p0,p1,p2,p3)=(1-x,x-xy,xy-xy²,xy²)`. True lifted moments obey `0<=v<=z<=x<=1` and `xv=z²`, where `z=xy,v=xy²`. Their **single-route convex hull** is `0<=v<=z<=x<=1, z²<=xv`; for every affine terminal observable the conic hull gives the same extremal value as true policies. Dropping the conic constraint permits loss 0 when the true minimum is 3/4 for `F=1_T2`.

## New precise question

Construct a finite source-tagged non-IID DAG with two distinct pre-port route fibers `C0,C1`, reached with strictly positive rational P/Q source masses, both using the **same** policy port y twice along downstream paths. The route-wise conic relaxations of `(x_i,z_i,v_i)` may be individually exact, but they need not arise from a **single compatible distribution of shared y** when optimizing a joint observer. Determine whether independent per-route cones are sufficient for the joint achievable convex hull. Either produce rational sources/terminal-observer coefficients and a **strict exact global optimum gap**, or prove a sufficient and necessary shared-mixture compatibility condition with explicit assumptions.

Suggested first check: if all routes use the *same* shared y and have fixed positive x_i, joint moments satisfy `z_i/x_i=E[Y]` and `v_i/x_i=E[Y²]` under a common ex ante policy mixture. Independent cones omit these cross-route equations. Check that a proposed observer uses a single policy across both routes rather than illicit source-dependent controls. Establish global continuous bounds by algebra/separation, not a finite numerical grid.

## Evidence and acceptance

Give complete positive rational source laws and actual ordered-history DAG, shared-port semantics, a bounded terminal or source-tagged observable, precise cone and true feasible sets, an exact primal witness and matching universal bound, and an independently executed `Fraction` replay. State whether the problem has fixed parameters, ex ante mixing, or history-dependent controls; do not conflate them. Preserve path symbols, port occurrences and future observer scope. Submit full proof, code, stdout and a one-unit continuation via the existing author PR. Native X6 transfer is independently pending and requires declared time/port/axis and registered address semantics. Do not infer formal CLAIM or independent review from an author commit.
