# X6 R173 — Exact segment incompatibility graph and conditional clique lower bound

2026-11-24. AUTHOR PROOF / EXACT INTEGER REPLAY / NOT_REVIEWED. Independent informed static six-pair BRC observation, P000 V5, joint relation preservation. Frozen R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@1e4ab68c4f9c91bc60c07017acc57be20829832f. No native spatial or time-dynamics claim. Continue R171 and correct R172.

## Corrected R172 statement (supersedes its initial candidate claim)

R172 initial note @69cc88565b5a66cfae2e9060e3c61780494ccb23 proposed 53 leaves and 731 excluded first queries. Withdraw both: differences in admissible optimizer masks do not entail incompatibility. The strict replay @43567b3d433d39f2f0c7c63405a0c77473f9095b and strict witness table @9c62120c907888faef260b4d2c87db75819ac739 establish 44 leaves and 518 excluded first queries. The previously cited counterexample p=(384615384,769230768,8846153832), q=(512820512,512820512,8974358960) has common singleton M=4,N=132 at endpoints; M=68,N=132 at their sum still admits the old answer. This is not an incompatibility witness.

## Theorem: conditional clique pruning

Use positive parameters p=(t,B,D), weights (17t,B,22t,D), capacities s=(17t+B,39t,17t+D,22t+B,B+D,22t+D). Port 10 contains 1935 unoriented directions as in R121. Keep every six-gap term and score F_v=max_j g_j(v)/s_j. Eta=min_v F_v and N={v:2F_v<3eta}. Leaf output is a named one of the 15 T terms equal to eta plus the exact N. The 884 allowed predicates are the two strict orientations of nonconstant comparisons between 30 raw candidate terms, with ratios 1 and 3/2 (R170/R171). The parameter simplex is an auxiliary weight model, not native spatial geometry.

Group exact endpoints by distinct singleton legal output (m,N). Within each group build a graph, joining p,q only after exhibiting a positive combination r=a*p+b*q where that same output is illegal, i.e. m is not a valid optimum at r or N differs. Every correct homogeneous linear comparison leaf is convex; for affine comparisons on the normalized simplex the normalized r is likewise a convex combination. Thus endpoints of an edge cannot share a leaf. Different singleton labels cannot share a leaf either. For a node containing endpoint subsets S_i from each group, a valid lower bound on its required number of leaves is L(S)=sum_i omega(G_i[S_i]), where omega is maximum clique size. The same argument applies after any sequence of allowed queries; there is no need for the incompatibility intermediate r to be in the endpoint table, because if both endpoints reach a leaf, the true full-domain leaf contains r too.

For each group and each subset U, the exact recursion is omega(empty)=0 and omega(U)=max(omega(U minus v),1+omega((U minus v) intersect neighbors(v))). In a node of remaining depth d, L(S)>2^d is impossible. For a candidate root split both children must have L<=32 if total depth is six. Each child must admit some second query whose two grandchildren have L<=16. These are necessary conditions; they do not assert existence of a valid tree.

## Exact segment discovery and full-population validation

Combine the two pinned R172 endpoint tables, deduplicate within the 35 singleton groups. For fixed candidate output m,N and p,q, enumerate rational roots on the segment of the cross-multiplied comparisons of m against each H term at factors 1 and 3/2. These expressions are affine in the segment parameter, because capacities are positive linear forms. Endpoints, interior roots and a rational midpoint in every open interval cover the sign states of these particular comparisons. The ten-direction bank is used only as a discovery filter. A purported incompatible intermediate is checked using every one of the 1935 directions, without needing a candidate coverage theorem. At an exact positive integer representative r, let m=g/s_j. It equals eta iff no direction has all six terms strictly less than m and at least one direction has maximum term exactly m. The near-set test conditional on eta=m is all six inequalities 2*g_k*s_j < 3*g*s_k; any extra near direction is detected. Endpoint uniqueness is separately checked against all 15 T terms. Positive rational interpolation coefficients and intermediate points are stored by the executable. Lack of a discovered edge is not a proof of compatibility in the full domain.

Actual JavaScript BigInt run (arbitrary-precision cross products; small finite subset bitmasks):
- 63 distinct endpoints, 35 singleton labels, 46 within-group pairs.
- 17 certified incompatibility edges; exact maximum clique in each of these finite certified graphs sums to 44.
- 80 full-population checks = 154800 direction evaluations.
- 15 T terms, 30 H terms, 442 canonical nonconstant lines, 884 oriented strict comparisons.
- Conditional-clique first-query survivors 341, excluded 543. The second-query capacity test excludes zero additional roots: all 341 have at least one permitted split on each child satisfying this necessary bound.
- This improves the strict R172 fixed-clique filter (366 survivors) by 25 further exclusions, without increasing its unconditional 44-leaf lower bound.
- The whole-domain optimal depth remains 6 or 7. No runtime benchmark, formal Result, independent mathematical review or native dynamics claim.

Self-contained replay with both pinned endpoint datasets, full score checks, rational obstruction witnesses and surviving root indices: [x6_r173_segment_graph_replay.cjs](https://github.com/awdawmip/enterprise-math/blob/f20c4ac4ab48c937f570f5193051eba733a5b563/research_notes/portable_direct/x6_r173_segment_graph_replay.cjs). Run with Node; output is JSON. The exact function was executed in a JavaScript runtime before publication; the saved wrapper's bytes were read back and matched the generated source.

## Next

A larger graph may strengthen the lower bound without a larger global clique. In particular, graph coloring gives chi(G[S]) >= omega(G[S]) as a necessary leaf count; disconnected groups still add because their singleton outputs differ. Seek finite exact obstructions with multiple competing cliques and evaluate conditional bounds on the R171 799-state frontier. To resolve six versus seven, a full-domain six-depth tree or a finite obstruction covering all 884 possible queries is still required.

## Control and provenance

Original read-only continuation r2-20261124-1910-x6-independent-status returned FAILED / CANONICAL_REJECTED: unknown current immutable task publication, worker phase NO_CURRENT_FORMAL_TASK, no execution authority. No retry, CLAIM, owner change, task creation or identity adoption. Current native owner not established. Existing historical activity RA-B60559848FD879270DCA6317, EM-DIRECT-AE5AD5, remains provenance; current Sites client identity does not authenticate that historical session. Global canonical entry blobs checked against main@2cec938cf365f585ce906413db4f28906132808d. Scientific inputs were read at their original immutable pins.
