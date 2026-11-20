# R762HD — An S6-equivariant Port gate and its exact positive-BRC return law

Status: AUTHOR-PROVED CANDIDATE / EXACT FINITE CHECK PASS / NOT_REVIEWED.
Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142.
Continuation: R762HC (Draft PR #2861 @ e513901d104bc00e5dc2397a777f5c10adb4adb0). Original researcher provenance: EM-X6-3050F6; live native authorization is independent of this artifact.

Frozen science: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389: p000_reality_foundation.json, definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md, definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md and definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json. Current rules read separately. Preserve P000's six signed axes, native 120-degree PERP_E, six-axis Cell torsor, independent time, required genuine triadic primitive balance, and BRC provenance. Nothing below promotes a three-axis spatial translation to a primitive three-force balance.

## Exact model: explicit candidate gate

Let I={0,1,2,3,4,5}. An unordered named Port P is a two-element subset of I, one of 15 possible Ports. Let C in Z^6 be the displacement relative to a chosen Cell, ell in Z^6 a relational Link accumulator (not more spatial dimensions), and t the independent integer event-time index. Each candidate positive BRC source event is named (P,k,a,sigma), where k in I\P (four options), a in P (two options), sigma in {+1,-1} (two options). Put S=P union {k}, h_S=sum_{i in S} e_i and define

~~~
P'   = {a,k}
C'   = C + sigma*h_S
ell' = ell - sigma*h_S
t'   = t + 1
~~~

Each branch is an OUTER three-axis composite-path label; any internal ordering of the three primitive native steps is further provenance that must not be discarded. There are 16 named signed branches per Port, all with positive BRC counting mass. Sigma labels a signed Cell increment but does not make BRC source mass negative. The candidate relation K=C+ell is conserved. The rule is S6-covariant: permute all axis labels in P,k,a,C,ell simultaneously. This is a model of proposed permission, NOT an established TRIADIC_CLOSURE_E event or complete native rotation.

## Theorem 1: minimal selector for all eight unsigned branches

For one fixed unordered P, the stabilizer is S2 x S4: S2 swaps the two endpoints of P and S4 permutes its complement. Its action on the eight choices (k,a) in (I\P) x P is transitive. Therefore no deterministic function of P alone can choose a (k,a) while remaining S6-equivariant: every stabilizer element would have to fix the chosen option. Any equivariant selector state realizing ALL eight such choices must have at least eight distinguishable local states (3 binary bits). A positive BRC retaining all eight distinct outgoing choices needs no hidden selector; including independent sigma gives 16 branches.

This separates R762HC's four choices of k from an additional unavoidable two-way next-Port endpoint choice a. The lower bound is for this fully specified all-options selection interface, not for every possible narrower native gate.

## Theorem 2: local saturated incidence and global mod-three residual

For fixed P={i,j}, four increments h_{P,k}=e_i+e_j+e_k, k outside P, have exact integer span

~~~
L_P = { y in Z^6 : y_i=y_j=sum_{k outside P} y_k }.
~~~

Indeed, with integer coefficients n_k, y_k=n_k for each outside coordinate, while y_i=y_j=sum n_k. Conversely n_k=y_k reconstructs every vector satisfying these equalities. The outside-coordinate projection is an integral isomorphism L_P -> Z^4, so L_P has rank 4, Z^6/L_P is free of rank 2 (no lattice torsion), and the nonzero Smith factors are (1,1,1,1). A free additive Link decoder of the four local increments needs rank >=4 and this is attained.

When the Port label ranges over ALL 15 two-element subsets, every three-axis S appears under exactly three Ports P subset S. Their aggregate columns are precisely the 20 columns of R762HC; their integer span is

~~~
L_all = {y in Z^6 : sum_i y_i == 0 mod 3};
rank(L_all)=6; index=3; Smith factors=(1,1,1,1,1,3).
~~~

The aggregate minimum free additive decoder rank is 6, attained by ell in Z^6 with the update above. Thus a rank-four saturated fixed-Port relation coexists with a rank-six, index-three aggregate incidence lattice. IMPORTANT: a column span is not a reachability assertion for ordered Port-constrained trajectories starting from a fixed Port.

## Theorem 3: all-length positive-BRC named-Port return theorem

For any P, the eight distinct unsigned successor Ports Q satisfy |P intersect Q|=1. Thus the unsigned Port graph is the Johnson graph J(6,2), 15 vertices of degree 8. Two distinct vertices, whether adjacent or disjoint, have exactly four common neighbors; each vertex has eight length-two returns. If A is the graph adjacency matrix, J the 15x15 all-ones matrix,

~~~
A^2 = 4 I + 4 J.
~~~

The constant vector has A-eigenvalue 8. On its orthogonal complement, A^2=4I, and trace(A)=0, yielding eigenvalues 8 (multiplicity 1), 2 (5), -2 (9). By transitive S6 action, every diagonal entry of A^m equals trace(A^m)/15. Hence for every integer m>=0, the exact unsigned Port-return count from any P0 is

~~~
U_m=(8^m + 5*2^m + 9*(-2)^m)/15.
~~~

Each unsigned branch has two independent sign labels. Accordingly the number of POSITIVE BRC sources returning the same named Port and their normalized positive mass are

~~~
R_m = 2^m * U_m.
Pr(P_m=P0) = [1 + 5*(1/4)^m + 9*(-1/4)^m]/15.
~~~

In particular R_0=1, R_1=0, R_2=32; the probability tends to 1/15, with an exact alternating exponentially small correction. This is model-internal BRC source counting, not native force cancellation or a physical Markov law.

## Theorem 4: full Cell/Port observer needs residual information

Let F_m(P,C) denote the number of named positive-BRC source histories ending at Port P with six-axis signed displacement C, starting from (P0,0). Exact recurrence:

~~~
F_0(P,C)=[P=P0 and C=0].
For all Q adjacent to P and sigma in {+1,-1}:
  F_{m+1}(Q,C+sigma*h_(P union Q)) += F_m(P,C).
~~~

Zero full Cell displacement is possible only for even m, since the coordinate sum changes by +3 or -3 on every event. At m=2, every Port-return path P->Q->P uses the same triple support twice; only opposite signs give a Cell return. Exactly 8 choices Q times 2 first signs = 16 joint Cell-and-Port returns, whereas there are 32 Port-only returns. Thus forgetting Cell is not observer-safe for future joint returns even at horizon two. Time t still increases at every event.

The supplied standard-library Python checker tests all 720 S6 permutations across 86,400 directed transitions, exact A^2, local lattice reconstruction and all length 0..12 Port-return formulas. It performs independent positive integer dynamic programming for all joint Cell/Port returns through m=6:

| m | Signed Port-return sources | Joint full-Cell/Port return sources |
|---:|---:|---:|
| 0 | 1 | 1 |
| 1 | 0 | 0 |
| 2 | 32 | 16 |
| 3 | 256 | 0 |
| 4 | 4608 | 624 |
| 5 | 69632 | 0 |
| 6 | 1122304 | 34688 |

The m=4 and m=6 joint counts are author-side exhaustive integer recurrence results, not a universal closed-form joint theorem. R762HD_EVIDENCE.json records the captured output; the code is R762HD_CHECK.py. Independent review: NOT_REVIEWED.

## Remaining native target

Frozen P000 specifies the meaning and required arity of primitive TRIADIC_CLOSURE_E but does not in the inspected frozen definitions supply a complete attached Cell/Link/Port/time update predicate or native rotating permission. The gate above is a mathematically explicit candidate to compare with an actual admitted primitive law, not a proposed amendment to P000. The next discriminating action is to supply/derive that typed native law and identify an actual witness candidate event (allowed or rejected), then recompute the legal Port graph, rank and positive-source transfer counts. Keep the separate q9 full-vector period/lift obligation open; do not repeat already saved R762EU/FG evidence.
