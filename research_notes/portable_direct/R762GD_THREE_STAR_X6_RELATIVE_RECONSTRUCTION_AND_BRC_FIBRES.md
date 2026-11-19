# R762GD — Three STAR observations reconstruct the complete X6 relative Cell coordinate

Date: 2026-11-19. Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, TP2-8B7E13C5904A2D6F1142.
Author status: algebraically proved, separately exact-enumerated in Python and JavaScript. Review: NOT_REVIEWED.

## Frozen sources and typed scope

P000 and X6: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389, specifically p000_reality_foundation.json, definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md and definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md. Taskbook: research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md at 857280d1012943290d141d1317179c40ec3cbdf8. Previous frontier R762GC, d6fe17080785dfe4fddff381475f27e865a725cd. K4 STAR sets follow R762FX.

There are six signed primitive axes and a Z^6 Cell torsor with chart-relative origin; PERP_E and the native right angle 120 degrees remain the protected P000 relations. The following are exactly the relative *coordinate* observations of the four realized STAR carriers. They are not asserted to be full carrier Link/Port/path observations, allowed triadic force events, or executable rotations.

Label six axes with the six K4 edges in order 01, 02, 03, 12, 13, 23. The four named STAR triples are
S0=(01,02,03), S1=(01,12,13), S2=(02,12,23), S3=(03,13,23),
with zero-based indices (0,1,2), (0,3,4), (1,3,5), (2,4,5).
For z in Z^6 define q_v(z) as the ordered values of z on S_v after subtracting their minimum. For nonempty A subset of the K4 vertices define Q_A(z)=(q_v(z):v in A).

## Theorem 1 — Full integral kernel for any nonempty STAR subatlas

Let U_A be the union of the selected STAR axis sets, k=|A|. For arbitrary z,z' in Z^6,

Q_A(z')=Q_A(z) if and only if some integer c satisfies
z'_e-z_e=c simultaneously for all e in U_A.

Coordinates on the remaining E\U_A are free. Hence the entire invisible-difference lattice is exactly

K_A = Z 1_{U_A} direct-sum (direct-sum over e in E\U_A of Z e_e),

and is a saturated free subgroup of rank 1+binom(4-k,2).

| Selected STARs k | Unobserved axes | Kernel rank | Full relative Cell class z mod Z(1,1,1,1,1,1) reconstructed |
|---:|---:|---:|---|
|1|3|4|No|
|2|1|2|No|
|3|0|1|Yes|
|4|0|1|Yes|

Proof. Min-normalized triples q_v(z),q_v(z') are equal exactly when the three coordinates differ by a single constant c_v. For any distinct selected K4 vertices v,w their STARs intersect at edge vw. Thus c_v=c_w. All c_v equal c. An edge is missing from their union exactly if both its endpoints are outside A, giving binom(4-k,2) free coordinates. The converse is immediate. The indicator 1_{U_A} and unit vectors of the omitted edges have disjoint supports and form an integral basis of the kernel. For k>=3 all edges occur, yielding exactly the global diagonal Delta. For k=2 there is one independently invisible missing edge. QED.

The fourth STAR **coordinate** observer is thus an exact function of any three STAR coordinate observers. No reduction of fourth-carrier incidence, port, source or BRC trace follows from this coordinate theorem.

## Theorem 2 — Explicit reconstruction and optimality

Fix any three K4 vertices a,b,c. Let y_v=q_v(z), m_v=min_{e in S_v} z_e. Set reconstructed m_a=0. At the shared edge av, compute

m_v-m_a = y_a(av)-y_v(av).

Then for each of the six edges choose any selected incident vertex v and form r_e=y_v(e)+(m_v-m_a). Overlap consistency holds by the shared-edge equations. The vector r equals z minus m_a times the global all-one vector. Therefore

can6(r) = can6(z), where can6(z)=z-(min_e z_e)(1,1,1,1,1,1).

Retaining a further integer h=min_e z_e recovers the entire full signed X6 displacement as z=can6(z)+h D.

Optimality is global on Z^6: a 3-axis relative observer provides at most two independent difference constraints, so any two such observers impose at most four linear constraints on six free integer coordinates. Their invisible-difference lattice cannot be merely rank-one Delta (five independent differences are required). Three are necessary and the K4 STAR triple achieves this minimum using already-realized carrier coordinate selections. QED.

## Theorem 3 — Exact signed-triad fibres and a new global-diagonal obstruction

Define Omega3={z in {-1,0,+1}^6: exactly three entries are nonzero}. There are 20*2^3=160 signed endpoints. Each is reached by exactly 3!=6 ordered signed primitive three-axis paths; total 960 source-labelled paths, retaining path order, sign, branch identity and provenance.

For **any three STARs**, Q_A has precisely 140 endpoint classes: 120 singleton classes and 20 doubleton classes. The doubletons are exactly

{1_S, -1_{S^c}}, for the 20 three-axis supports S subset {1,...,6}.

Their difference is D=(1,1,1,1,1,1). Every other endpoint is a singleton. Thus these 20 pairs are indistinguishable by every one of the 20 coordinate triple min-zero observers, even if their labelled axis permutations are also read. They are distinguished by the integer common depth: h(1_S)=0, h(-1_{S^c})=-1.

Proof. Theorem 1 reduces observational equality to z'-z=tD. Each Omega3 vector has exactly three zero components, so t lies in {-1,0,1}. For t=1, every coordinate of z must be either -1 or 0; otherwise z' has a +2 component. Thus z=-1_{S^c}, z'=1_S with three entries of each kind. t=-1 is the reverse and t=0 gives equality. Hence 20 pairs and 160-40=120 singletons. Exactly six orderings reach each endpoint. Every min-zero coordinate observer annihilates D; permutations keep D invariant. QED.

Note the exact distinction from R762GC: that note separated +1_S and -1_S on the **same support** by swapping a selected and omitted axis. This theorem pairs positive support S with negative *complementary support* S^c, so the difference is the global diagonal and no coordinate permutation or relative-min observer can separate it.

For the uniform positive 960-word BRC, the 20 two-endpoint classes each contain 12 source histories and the 120 singleton classes each contain 6 histories. The combined probability of the doubleton classes is 20*12/960=1/4. The 140 relative classes and 160 endpoint states each require eight fixed binary bits if encoded without an additional source-order obligation, while all 960 distinct ordered source words need ten bits. Keeping one conditional common-depth distinction only repairs the 20 ambiguous relative classes; it does not restore the sixfold path-order fibre.

## Theorem 4 — Exact finite STAR selection counts on Omega3

All nonempty subfamilies of the four STARs were exhaustively counted in the included deterministic integer-only program.

| k | Observation classes | Endpoint fibre-size spectrum, size:count |
|---:|---:|---|
|1|19|1:6, 6:6, 10:1, 18:6|
|2|100|1:60, 2:20, 3:20|
|3|140|1:120, 2:20|
|4|140|1:120, 2:20|

Every subset of a given k has the same counts. In particular three are also minimal on this specific signed-endpoint population for fully retaining the all-20-observer partition. This is a finite exhaustive statement, supported by the exact checker. The stronger all-integer reconstruction and minimality claims are established by Theorems 1–2.

## Limits, validation and next research question

Coordinate-permutation and state-independent signed coordinate-translation futures preserve the D difference, so they cannot split the 20 complementary pairs when the final query is relative. Any actually legal native operation sensitive to full common depth, named signed incidence, or absolute Cell/Port state could refine the fibres. The frozen P000 axioms specify triadic arity/angle and X6 coordinate adjacency but leave the detailed executable signed Cell/Link/Port TRIADIC_CLOSURE_E permission/transition open. The present BRC source family is a typed model and does not assert every path is an allowed force-closure event.

Companion program R762GD_VERIFY.mjs and JSON evidence use exact integer arithmetic: 15 nonempty STAR subfamilies, 160 signed endpoints, 960 source orders, 20 diagonal-obstruction pairs, 640 reconstruction cases, and 10,935 finite-grid kernel checks. A separate Python standard-library checker corroborated every displayed fibre count and obstruction. Neither a finite grid nor author computation alone establishes a universal lattice theorem; the unrestricted proof is given above. Independent mathematical review: NOT_REVIEWED.

Next: inspect source-pinned signed Cell/Link/Port event predicates, test the 20 complementary-pair incidence histories for an actual future gate that depends on global depth, and compute the exact observer partition of that legally allowed operation family. Preserve the fourth STAR carrier's non-coordinate relations and the source-ordered BRC paths until separately certified safe. The separate q9 full-vector period/lift question remains open.
