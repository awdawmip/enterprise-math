# R5 — Actual-real-image classification by 3-polytope face lifting and degree

Date: 2026-10-30 (Asia/Shanghai). Author-side status: AUTHOR_PROVED / EXACT_BIGINT_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Mathematical auxiliary two-law/BRC stopping model; no claim of native physical X6 dynamics or P000 modification.

## Frozen inputs

GLOBAL_KNOWLEDGE_V1 canonical main 96380d0434ed98c5425defd71c8bd31c86639859; Enterprise Math main 4e72c173d9a6e82db691a8ececa673890d2e0429. Read global bootstrap/manual, ACTIVE worldview, project P000, AGENTS, joint observer preservation, BRC/mathematical policies and current portable/autonomous research protocols. Scientific predecessor: Draft PR #1663 commit 722d9eaaf00d2510cf697813441b8a8194207414, research_notes/brc_r5_collision_residual_equality_locus_20261030_t1050/RESEARCH.md and FACET_CERT.json. Its all-real unequal-parameter separation remains author-side evidence, not independent review.

Positive labelled path masses (360P,360Q): t1 A(120,240) B(240,120); t2 A0(60,180) A1(60,60) B0(180,60) B1(60,60); t3 A00(30,108) A01(30,72) A10(30,45) A11(30,15) B00(90,36) B01(90,24) B10(20,40) B11(40,20). Stop optional t1–t3, mandatory t4. FULL has 14 real stop parameters; seedless LR has 12 indexed by time and likelihood ratio L=P/Q. LR shares A1/B1 (t2,L=1) and A11/B11 (t3,L=2). No persistent correlated random seed; every natural path visits each key at most once, hence the policy observation map is multi-affine.

Terminal errors p=1/5+t/20+(t+1)/(100L); q=2/5-t/30+(t+2)L/200+eta*c_h, with c_A11=a, c_B11=b and other residuals zero. All terminal probabilities must lie strictly between zero and one. Our exact verifier separately checks legality for eta=1/1000 and equal coefficients c=0,1 including mandatory t4. Retain labelled P/Q mass until the final named four-observer, BRC usage REUSE_APPLIED. No quotient is asserted observer-safe beyond the four readouts at the finite time horizon.

Write DP=4-TP, DQ=4-TQ, and R=sum of stopped Q mass times residual c_h. Direct change of measure yields, for every real policy,
eP=21/100+TP/20+TQ/100;
eQ=41/100+TP/200-TQ/30+eta*R.
For a=b=c we have R=c*R1, where R1 is stopped Q mass on A11/B11. Thus for c nonzero the original four-observer is an injective affine image of the three-dimensional integer-scaled map (r,x,y)=360*(R1,DP,DQ); for c=0 it is a projection to (DP,DQ).

## Theorem: exact actual-image equality locus

On this fixed tree and error family, for all eta>0 and all admissible real a,b, actual four-observer real behavioral images of FULL and seedless LR **coincide if and only if a=b**. For a=b nonzero they both fill their common rank-three convex hull, and for a=b=0 they fill the common rank-two projected hull. For a!=b the predecessor's signed universal support inequality separates the convex hulls. Therefore this two-parameter family cannot realize the mother problem's equal convex hull but unequal actual image.

## General exact face-lifting lemma

Let F:[0,1]^n -> P subset R^3 be a multi-affine map, where P is the convex hull of its binary corner images and is a full-dimensional convex 3-polytope. Suppose (i) for each edge E of P, binary corner masks mapped into E form a connected single-bit graph, and (ii) for each facet H the preimage X_H={x:F(x) in H} is star-shaped. Then **F([0,1]^n)=P**.

Proof. Multi-affine interpolation expresses each F(x) as a convex combination of corner images, hence F(cube) subset P. Choose a binary input mask for each polytope vertex. For each polytope edge, connect its chosen endpoint masks along the connected optimal-mask graph. Every single-bit segment maps affinely into the same exposed geometric edge; so the entire 1-skeleton lifts continuously into the policy cube. For each polygonal facet H, its lifted boundary loop lies in X_H; coning to a star center of X_H fills the polygon, with the same edge paths shared by adjacent facets. The face fillings glue into h:boundary(P)->cube, and F(h(z)) and z lie in the same convex face for every boundary z. The straight homotopy (1-s)F(h(z))+s*z stays in that face, so F∘h has degree one on the boundary 2-sphere. Since the cube is convex, extend h over the solid polytope by coning to an arbitrary cube point. Were any interior y of P missing from F(cube), radial projection of the extension away from y to boundary(P) would extend a degree-one sphere map over a ball: impossible by Brouwer's no-retraction/degree theorem. The degree-one boundary map is also surjective on the boundary. Therefore F(cube)=P. QED.

Boolean star certificate. For an exposed facet H with support ell(F)<=d, let E_H denote the binary masks attaining d. The product-weight multiaffine interpolation shows that X_H is exactly the union of coordinate subcubes whose corners all belong to E_H. If there is a mask z_H in E_H such that, for every m in E_H, flipping any differing bit of m *towards z_H* stays in E_H, then E_H XOR z_H is a Boolean down-set. For each maximizing subcube C, select the corner of C maximally distant from z_H coordinatewise. Its Boolean interval to z_H contains C, and all interval masks are optimal by downward closure. Consequently every point of X_H has its entire segment to z_H in X_H: X_H is star-shaped. QED.

## Exact verification and scope

VERIFY.js is its own actually executed source, using BigInt for exact Cramer determinants and rational halfspace cross products, and bounded exact integers for all mass, support and graph operations. It enumerates every FULL 16384 and LR 4096 binary policy, returning 647/272 distinct integer observations. It tests the 24 signed facet planes from the predecessor on every FULL policy, adds four bounding planes, exhausts 3276 plane triples (3075 nonsingular), and checks that all 31 feasible polytope vertices are actual LR deterministic images. Each auxiliary bounding plane meets only one vertex; all 24 original planes have noncollinear vertices and are genuine facets.

For the 24 facets, star-center 12-bit masks in the listed plane order are (hex):
00b 00a 012 100 809 004 805 10a 000 90b 410 192
024 112 18a 000 985 1c7 992 997 b13 9d6 1cb b95.
For every facet the checker scans **every** optimal binary mask and **every** bit differing from its center, verifying the exact downward closure. It enumerates 53 geometric edges, checks both endpoints are attained, and verifies connectivity of all 53 binary optimizer graphs. The incidences satisfy Euler 31-53+24=2. Thus both hypotheses of the lemma are certified at the exact combinatorial level, and the analytical lifting argument proves coverage of **all real** stop policies. Output in EXACT_OUTPUT.txt ends PASS_EXACT_R5_REAL_IMAGE_DEGREE_CLASSIFICATION.

No independent review or formal Lean checker has been performed. The a!=b half of the iff statement explicitly relies on the prior author's universal signed support separation theorem; this run independently resolves the equal-line real-image question and checks its finite combinatorial prerequisites.

## Next exact scientific unit

The mother's full four-observer problem remains OPEN. Add an independent P-terminal error basis to lift the equal-line model to rank four while preserving genuine two-law path collisions and provenance. First prove complete full-dimensional signed-direction convex hull equality with exact LR Caratheodory mixtures or Farkas certificates; if a support gap exists, preserve the exact failed candidate. Only then attack real-image separation by a valid higher-dimensional topological face-lifting obstruction or quantifier elimination. Failure of a sufficient star criterion alone does not establish image inequality. Persist author-side evidence on existing Draft PR #1663; formal Source activity, CLAIM/Result and Driver review depend on current native authorization.
