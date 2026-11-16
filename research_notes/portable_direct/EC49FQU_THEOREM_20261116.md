# EC49FQU — Four exact native-BRC price slices, 34-node enclosure

Date: 2026-11-16. Evidence: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.
Frozen science: awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Lineage: EC49FQT PR #2571, commit a30e207a382b49088d60402e119fedf97e0959e7; inherited EC49FQM PR #2552.

## Native identification problem and feasible strategies

Class 16943 has 310 original configurations, 141 complete named-root response profiles, 228 physical queries (144 terminal, 84 named-root) and 209 distinct query partitions. A finite adaptive tree must identify the **full** named-root profile. Let x=r/t with t>0, 0<=lambda<=1, and profile probability p_i=(1-lambda)/141+lambda*m_i/310. Multiplicities m_i and physical queries are computed from the unchanged frozen scientific inputs.

Write beta=620/3299, K(x)=7557-169x and gamma(x)=310(3-x)/K(x). The following normalized costs belong to explicitly replayed, complete native trees:

- A=(1-lambda)(6x+290)/141 + lambda(6x+751)/310; first index 32 or 34, observation vector (6,290;6,751).
- B=(1-lambda)(5x+293)/141 + lambda(5x+704)/310; first index 140 or 142, vector (5,293;5,704).
- C=(1-lambda)(5x+295)/141 + lambda(5x+685)/310; first index 16 or 23, vector (5,295;5,685).

Vectors are (uniform summed root, uniform summed terminal; configuration multiplicity summed root, configuration multiplicity summed terminal). Named-root distinctions are preserved, not collapsed to the terminal observer.

## Theorem 1: four new complete-prior sections

For every real lambda in [0,1] at each x in {61/24,21/8,65/24,67/24}, the unrestricted finite native-BRC Bellman optimum is exactly t * min(A,B,C).

| x | gamma(x) | beta |
|---|---|---|
| 61/24 | 3410/171059 | 620/3299 |
| 21/8 | 310/18969 | 620/3299 |
| 65/24 | 2170/170383 | 620/3299 |
| 67/24 | 310/34009 | 620/3299 |

All optimal physical first-observation indices:
- 0<=lambda<gamma: {32,34}.
- lambda=gamma: {32,34,140,142}.
- gamma<lambda<beta: {140,142}.
- lambda=beta: {16,23,140,142}.
- beta<lambda<=1: {16,23}.

**Proof.** At each of the eight new rational points with lambda=0 or gamma(x), one native exact Bellman implementation and one independently written unrestricted subset solver both reproduce the full integer optimum and *all* 228 physical first-label minima, and replay every tied-first complete native tree. All 141 full profiles and exact masses are derived from pinned data; for lambda=a/b the integer profile weight is 310(b-a)+141*a*m_i. The relevant Bellman integer optimum divided by 310*141*b*t equals the dimensionless cost, which equals A at 0 and A=B at gamma. At each fixed x, all individual tree costs are affine in lambda. Endpoint nonnegativity of every competitor's cost gap proves A throughout [0,gamma]. The inherited exact EC49FQM right-prior theorem proves C optimal throughout beta<=lambda<=1 for all x>=1; B=C at beta, so endpoint nonnegativity likewise proves B on [gamma,beta]. Any additional physical first label strictly inside one phase would have to be optimal at both endpoints of that phase by concavity of its fixed-first Bellman value relative to the established affine optimum. The exact endpoint first-label sets give their stated intersections; full tied-first witnesses certify both transitions. QED.

## Theorem 2: certified continuous region

Add the four x nodes to the inherited 30-node exact mesh in [1,3]. There are now 34 exact price nodes and 33 adjacent intervals [a,b]. On each, A is globally optimal for lambda<=gamma(b); B for gamma(a)<=lambda<=beta; C for lambda>=beta. In each A/B rectangle the gap of a *fixed* competing tree to the explicit witness is bilinear in (x,lambda). Four-corner Bellman optimality implies that the bilinear gap is nonnegative throughout the rectangle. C uses the inherited exact high-prior theorem.

Any still unproved region lies inside the 33 strips gamma(b)<lambda<gamma(a). Their containing-rectangle areas sum exactly to

S34 = 928306751394905/174216767434670952.

Therefore the certified fraction of [1,3]×[0,1] is at least

1-S34/2 = 347505228117946999/348433534869341904 = 99.7335770933348857...%.

## Theorem 3: uniform regret bound over all prices and priors

For every real lambda in [0,1] and price x>=1, the explicit strategy min(A,B,C) for 1<=x<=3 and inherited high-price optimal strategy for x>=3 satisfies

0 <= C_strategy - C_opt <= [ (25/6) / (sqrt(87811/12)+sqrt(14607/2))^2 ] * t
< 0.000142489*t.

**Proof.** For each pair of consecutive certified prices [a,b], V_opt as a function of x is concave, so its endpoint chord is a lower bound while the displayed feasible trees are upper bounds. The inherited exact analytic chord envelope is M(a,b)=50(b-a)/(sqrt(K(a))+sqrt(K(b)))^2. Using rational intervals around each square root built with integer isqrt at 12-decimal resolution, the lower bound on M(17/12,3/2) exceeds the upper bounds on M for **all** other 32 price intervals. The unique maximum occurs at [17/12,3/2], where K(17/12)=87811/12 and K(3/2)=14607/2. For x>=3 inherited EC49FQM proves zero regret. The previous FQT upper envelope was about 0.0001470199428*t, so the certified uniform guarantee improves by about 3.0823%. QED.

## Evidence and next unit

Frozen data SHA256: master cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e; profile a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f. Reused 117 full FQT machine certificates, SHA-checked against the inherited manifest. Twelve additional finite certificates were generated at four prices: eight (lambda=0 and gamma) independently recomputed and full-tree replayed, and four right-prior anchors at beta and 1 on two prices were additionally generated, while their complete global validity is inherited from EC49FQM. The complete original native source inputs, 129 full certificate files, original generator, independent solver, exact geometry script and three grouped verification logs are in the user-delivered archive EC49FQU_FOUR_SLICES_34GRID_COMPLETE_EVIDENCE_20261116.tar.xz. No additional review or mathematical admission is asserted.

**Next question:** settle the 33 remaining enclosing strips by a parametric Bellman lower bound or a legal full native decision tree improving min(A,B,C). The largest currently certified chord interval is [17/12,3/2]. This is an independent portable artifact, not a formal RS-EC49AS CLAIM, Result, Review, or P000 modification. The exact RS-EC49AS immutable publication directory was absent from inspected main on 2026-11-16.
