# EC48B — Exact exposed-face component criterion for seedless BRC memory

Date: 2026-10-27. Status: AUTHOR-SIDE PROVED (full argument below); finite exact verifier executed; not native Result, independent Driver review, Working Truth or Heartbeat dynamics.

## Frozen controlling sources

- GLOBAL_KNOWLEDGE_V1 canonical main `7837065118e2cde3fffef339dccde1b886dce741`: 00_BOOTSTRAP.md, OPERATING_MANUAL.md, current P000 V4, ACTIVE worldview, math/code/BRC policies, activity procedure.
- Enterprise Math canonical source main `1685f8991110fba4e47ed85a7eb9a48b7cc0f5e3`: docs/PORTABLE_RESEARCH_PROTOCOL.md, weighted-BRC typed substrate, activity and persistence protocols, toolbox policy.
- Immediate verified mathematical predecessor EC48A: `416814d1fd7fb7f2ac50f9ad683726b778ecd287`, research_notes/r4_ec48_sign_profile_sweep_20261027/PROOF.md. The present unit **does not** assume EC48A solves unconvexified equality.
- Actual connected GitHub login: awdawmip, project write permission. Native owner read `CONTROL_QUOTA`, native session start `STATIC_READONLY_SCOPE_DENIED` (operation_sent=false). No native Task CLAIM.
- Activity: `RA-EMR4-20261027-0130-EC48B-AUTO11`, local writer key `chat-automation-r4-20261027-0130-t11` (not a native server-issued session).

## Observer and formal model

Let H and Y be nonempty finite sets. Under two hypotheses P and Q, let p(h,y),q(h,y)>0 be separately normalized positive rational probabilities on H×Y. The branch pair (h,y) is a positive weighted/provenance-preserving BRC source label; no cancellation or native Cell-dynamics assertion is made.

A seedless K-memory encoder is any hypothesis-independent family `pi_h in Delta_K`; a subsequent decoder, after memory m and second-stage visible y, declares P with probability `u(m,y) in [0,1]`. Its declaration probability is

    w(h,y) = sum_m pi_h(m) u(m,y).

Define alpha = sum_(h,y) p(h,y) w(h,y), beta = sum_(h,y) q(h,y) w(h,y).
Let S_K be all such (alpha,beta). The full-history region is

    Z = sum_(h,y) [0,(p(h,y),q(h,y))]

and the four declared observer coordinates are (error_P,error_Q,depth_P,depth_Q)=(1-alpha,beta,2,2).
Both S_K and Z are compact and S_K subset Z. A persistent public seed mixing complete K-state policies would replace S_K by conv(S_K); that seed is **not** permitted in S_K.

For each distinct positive ratio r=p(h,y)/q(h,y), set
D_r(h,y)=p(h,y)-r q(h,y),
T_r={(h,y):D_r(h,y)=0},
Q_r=sum_(h,y) in T_r q(h,y), and
O_r=sum_(h,y) max(D_r(h,y),0).

## Theorem EC48B.1 — Exact seedless full-region test without real QE

For fixed finite positive p,q and K>=1, construct, for every distinct ratio r, the following finite undirected graph G_r.

A vertex is one *deterministic* policy (f,b), where f:H->{1,...,K} is a pure encoder and b:{1,...,K}×Y->{0,1} a pure decoder, whose support value equals O_r:

    sum_(h,y) D_r(h,y) b(f(h),y) = O_r.

Join two such vertices when they differ in exactly one encoder choice f(h) (to any other memory color) **or** in exactly one decoder bit b(m,y). Let C range over its connected components, and put

    l_C=min_(f,b) in C sum_(h,y) in T_r q(h,y)b(f(h),y),
    u_C=max_(f,b) in C sum_(h,y) in T_r q(h,y)b(f(h),y).

Then

    S_K = Z
    iff, for every distinct r, union_{components C of G_r} [l_C,u_C] = [0,Q_r].          (EC48B.1)

An empty G_r means the condition fails. All tests use finitely many rational additions/comparisons, finite graph search and interval union; no numerical optimization or unverified real quantifier elimination is required.

### Proof, part A: identify every relevant exposed face

The support of Z in direction (1,-r) is O_r, attained precisely when w(h,y)=1 at D_r>0 and 0 at D_r<0, while the tied cells can vary. On this exposed segment the residual free coordinate

    t_r(w)=sum_(h,y) in T_r q(h,y) w(h,y)

ranges over exactly [0,Q_r], and alpha-r beta=O_r. Thus (alpha,beta) on the exposed segment is uniquely determined by t_r (because beta equals a fixed non-tie sum plus t_r; the tie contribution to alpha is r t_r). This also covers coincident ratios and simultaneous ties.

Every nontrivial edge of Z is one of these exposed segments or its central reflection (alpha,beta)->(1-alpha,1-beta). Indeed each generator (p,q) has both coordinates strictly positive; an outer normal with like-signed coordinates exposes only an endpoint, while a mixed-sign normal is (1,-r) or its negative up to positive scale, and an edge occurs only at a generator slope r. The degenerate case p=q gives the diagonal segment, which is the single tied face and is included. The decoder complementation u->1-u reflects S_K about (1/2,1/2), so coverage of all these one-sided faces covers the whole boundary of Z.

Finally S_K is star-shaped with respect to (0,0): scaling every decoder probability u by t in [0,1] scales (alpha,beta) by t without changing K. If all boundary faces lie in S_K, any z in Z lies on the segment from 0 to the farthest boundary intersection on its ray and hence lies in S_K. Necessity is immediate. Therefore S_K=Z is equivalent to covering [0,Q_r] at every tied exposed face.

### Proof, part B: optimal policies form a finite component complex

For a fixed r, the seedless support functional
    F(pi,u)=sum_(h,y,m) D_r(h,y) pi_h(m) u(m,y)
is affine separately in every encoder simplex pi_h and every decoder interval u(m,y). Thus it is multi-affine on a finite product of simplices and intervals. Expanding against the product of the individual vertex barycentric weights writes its value as a convex combination of its deterministic values F(f,b), each at most O_r.

Consequently F(pi,u)=O_r iff **every deterministic vertex of the Cartesian product of the positive supports of its variables** also has F(f,b)=O_r. Every maximizing policy therefore lies in a closed product face all of whose deterministic corners are vertices of G_r; conversely each such face consists only of maximizing policies. The one-skeleton of such a product face is connected using precisely the graph moves prescribed above.

The union of all maximizing faces belonging to one graph component C is path-connected, and distinct graph components cannot be joined by a maximizing face or path (the faces form a finite closed union, intersecting only through shared corners/edges). The tied mass t_r(pi,u) is continuous and multi-affine on each face. Hence its image over the connected union belonging to C is a compact interval. Its minimum and maximum are reached at deterministic corners and are exactly l_C,u_C. The complete image of tied mass at support optimum is therefore exactly union_C[l_C,u_C]. Combine with part A to prove EC48B.1. QED.

**Complexity/type.** G_r has at most K^|H| 2^(K|Y|) deterministic vertices, and each vertex has at most |H|(K-1)+K|Y| possible one-coordinate neighbors. There are at most |H||Y| distinct r. The test is exponential in H,K,Y but exact, finite and constructive; no polynomial-time claim is made. Using positive integer source counts P0,Q0, ratios can be compared by products. At the raw count ratio p_i/q_i the support score can be multiplied by a common positive constant to use the integer coefficients d_j=p_j*q_i-p_i*q_j; tied mass can likewise be measured in unnormalized integer q counts. Independent normalization does not change feasibility or interval coverage.

## EC48B.2 — Exact finite stress test

The executable source EC48B_VERIFY.js enumerates **all 4096 ordered pairs** of positive integer source arrays P,Q in {1,2}^(3×2), independently normalized. For each pair it computes EC48A's exact generic-signature peak, then checks every distinct tie face of K=2 whenever K_hull<=2, constructing G_r, BFS components and checking the union of integer tied-mass intervals.

Results: K_hull histogram (1:100, 2:2412, 3:1584); 2512 pairs with K_hull<=2; 6470 distinct-ratio face tests; 792 face tests with more than one maximizing-graph component; **zero uncovered faces**. This is a complete finite-domain result only: there is no universal proof from this bounded enumeration.

Example P=[1,1,1,1,1,2], Q=[1,1,1,2,1,1] as 3×2 row-major positive counts has K_hull=2. At raw tie ratio 1, G_r has 16 optimal vertices in two components, with tied-mass intervals [0,4] and [0,4]. Thus graph **disconnectedness alone does not establish an unattainable ROC face**.

No numerical randomness, floating-point comparisons, Lean formal checking or independent mathematical review is claimed. The exact finite checker is an implementation test for EC48B.1, and EC48B.1 is established by its separate finite-dimensional proof above.

## Actual gain, tool reuse and unfinished question

EC48A computes least memory for **convexified** ROC preservation via ratio-signature sweep. EC48B.1 supplies a **necessary and sufficient test for seedless S_K=Z itself**, by explicit optimal-face components. This replaces the previously proposed generic real-algebraic QE step for this narrowly declared two-stage binary-terminal model; it does not resolve a universal yes/no implication for all dimensions.

BRC reuse: REUSE_APPLIED to positive weighted/provenance-preserving BRC labels and EC47/EC48A exact ratio-support laws. Tool coverage: checked current enterprise_toolbox_registry.json, research_method_inventory.json and targeted current code search; no concrete current face-component optimizer was identified. REUSE_APPLIED to EC48A signature-peak filtering; EXTEND_EXISTING_TOOL as a narrow, author-side exact face-component verifier, not a new Foundation tool family. Signed/amplitude cancellation and native X6/heartbeat transfer remain outside this source-count model.

**Next EC48C:** search for a positive rational counterexample to `conv(S_K)=Z => S_K=Z` with K>=2 using EC48B.1 beyond H=3,Y=2,P/Q entries {1,2}. For a found witness output the exact r, all optimal graph components and a specific missing open rational tied-mass interval as an algebraic infeasibility certificate. If none, investigate a graph-reconfiguration theorem giving boundary filling for the appropriate family. Separately, the general variable-depth four-coordinate N4 problem still needs its full behavioral image analysis.
