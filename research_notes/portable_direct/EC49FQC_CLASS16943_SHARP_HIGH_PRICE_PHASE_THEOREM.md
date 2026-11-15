# EC49FQC — Exact high-price phase diagram for native BRC class 16943

Date: 2026-11-16. Research status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Frozen input and precise observer

Scientific commit: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Original master SHA256: cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e. Native root CSV SHA256: a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f. Reuse EC49FQA–FQB #2515 exact integer Bellman solver and independent 310-configuration replay, preserving these input hashes.

Class 16943 comprises 310 original configurations, 141 distinct complete named-root scalar cost profiles, 144 legal terminal scalar actions and 84 legal named-root scalar actions. The goal is to identify the full rooted profile certainly with a finite adaptive decision tree; there is no depth cutoff. Let terminal action price t>0 and named-root action price r>0. For a tree, let (R,T) count its named-root and terminal reads summed over the 141 distinct profiles (uniform prior) or over all 310 original configurations (multiplicity prior). The corresponding expected price is (Rr+Tt)/141 or (Rr+Tt)/310. These priors optimize their own respective trees.

## Exact global theorem for every real r/t >= 4/5

UNIFORM-ROOT-PROFILE PRIOR (141 states):

| Price interval r/t | Exactly optimal expected cost | Aggregate reads (R,T) |

|---|---|---|

| [4/5,153/184] | (242r+85t)/141 | (242,85) |

| [153/184,1] | (58r+238t)/141 | (58,238) |

| [1,3] | (6r+290t)/141 | (6,290) |

| [3,infinity) | (4r+296t)/141 | (4,296) |

MULTIPLICITY PRIOR (310 source configurations):

| Price interval r/t | Exactly optimal expected cost | Aggregate reads (R,T) |

|---|---|---|

| [4/5,7/8] | (179r+517t)/310 | (179,517) |

| [7/8,33/35] | (147r+545t)/310 | (147,545) |

| [33/35,1] | (112r+578t)/310 | (112,578) |

| [1,3] | (5r+685t)/310 | (5,685) |

| [3,infinity) | (4r+688t)/310 | (4,688) |

At shared endpoints the adjacent expressions coincide and distinct aggregate-count strategies tie. At an interior price ratio of each open phase, all globally optimal deterministic trees have that phase's (R,T) aggregate counts; their query topology need not be unique.

## Exact finite endpoints and witness trees

The full unrestricted integer Bellman recursion uses all 228 native actions (209 different response partitions after price-dependent deduplication). For each non-singleton profile subset S it minimizes price(q)*weight(S) plus the optimal costs of all informative response fibers. Every informative fiber is a strict subset, so recursion is exact, terminating and covers arbitrary finite adaptive depth. Any query with a single response is positive-cost dominated. The independently reconstructed original source verifies every witness tree.

| Exact prices (r,t) | Optimal integer total, 141-profile prior | Optimal integer total, 310-configuration prior |

|---|---:|---:|

| (4,5) | 1393 | 3301 |

| (153,184) | 52666 | 122515 |

| (7,8) | 2310 | 5389 |

| (33,35) | 10244 | 23926 |

| (1,1) | 296 | 690 |

| (3,1) | 308 | 700 |

Feasible witness count vectors: uniform (242,85) certified at r:t=157:189, (58,238) at 153:184, (6,290) at 1:1, (4,296) at 3:1; weighted (179,517) at 4:5, (147,545) at 7:8, (112,578) at 33:35, (5,685) at 1:1, (4,688) at 3:1. Each exact tree identifies all 141 profiles and was independently replayed on all 310 original configurations. The same fixed tree can be evaluated at any other positive price without changing a response. All the listed witness lines match the unrestricted Bellman optimal value at both endpoints of their respective finite intervals.

## Proof: exact finite intervals

Fix terminal price t=1 and set x=r/t>0. For any valid tree P, the population-total cost C_P(x)=R_P*x+T_P is affine in x with nonnegative integer coefficients. The unrestricted optimum f(x)=inf_P C_P(x) is concave as the pointwise infimum of affine functions. Suppose a feasible tree L(x)=Ax+B attains the Bellman optimum at two prices a<b. For every x in [a,b], concavity gives f(x)>=(b-x)/(b-a)*f(a)+(x-a)/(b-a)*f(b)=L(x), and feasibility gives f(x)<=L(x). Thus f(x)=L(x) throughout. Apply this lemma to each interval using the anchor table and the listed feasible trees. Homogeneity in (r,t) establishes the formulas for arbitrary t>0.

## Proof: infinite ray from 3 to infinity

Directly compute the complete 144-component terminal-response signature of each of the 141 rooted profiles from the frozen original configurations. There are exactly 139 distinct terminal signatures. The only two nonsingleton fibers consist of representative original-configuration pairs {17928,38165} and {24541,38166}; all four have multiplicity one. Members of a fiber yield identical outputs to every terminal-only observation. Along each of their four identification paths, some named-root action is therefore compulsory, hence every valid tree has R>=4 under both priors (with reads aggregated over the corresponding population).

At x>=3, every tree has C_P(x)=C_P(3)+(x-3)*R_P >= f(3)+4*(x-3). Bellman shows f_uniform(3)=308 and f_weighted(3)=700; feasible 4-root-read trees with 296 and 688 terminal reads, respectively, attain these lower bounds for all x>=3. Therefore the formulas on the entire infinite price ray are sharp. If x>3, any R>4 entails strictly greater cost, so every optimum has R=4.

## Proof: aggregate-count uniqueness within open phases

If an affine candidate C_P(x) equals a locally affine optimum L(x) at one interior point of an open phase and is above or equal to L throughout a neighborhood, then the nonnegative affine difference C_P-L must have zero slope (otherwise it is negative on one side of the contact point). Hence R_P is the phase slope, and equality fixes T_P as the intercept. This proves the aggregate-count characterization; it does not assert uniqueness of individual decision trees.

## Verification and follow-up

The source archive contains: unchanged EC49FQA exact priced Bellman solver; separately implemented independent replay against original 310 configurations; EC49FQC terminal-signature fiber enumerator; exact phase theorem checker; full response-labelled decision trees at all anchor prices; and execution logs. The compact companion certificate records exact anchors and source hashes. EC49FQC is a finite native-BRC result with exact input and observer scope; independent peer review and project theorem admission remain pending.

Next: determine every remaining transition on 0<r/t<4/5, connecting the present diagram to EC49FQB's proven pure-root thresholds 4/7 for the uniform prior and 26/71 for the multiplicity prior. Parametric Bellman envelopes and exact rational breakpoint certificates are candidate methods. Research topic RS-EC49AS has no current immutable Task publication, so this deliverable uses independent portable research; it is not a Task CLAIM/Result.
