# EC49FQD: complete native BRC class-16943 uniform-prior price-phase theorem

Date: 2026-11-16. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Portable independent research only; no new Task CLAIM, Result, or Review.

## Frozen scope

Frozen science pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Master SHA-256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; native BRC named-root CSV SHA-256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`.
Source domain class 16943 has 310 original configurations collapsing into 141 distinct complete named-root scalar profiles. The exact observer has 144 terminal scalar actions and 84 named-root scalar actions. Every tree must identify the **complete named-root profile**. Trees are unrestricted in adaptive depth, and root/terminal action prices are positive reals `r,t`. The present prior is uniform on the 141 distinct profiles, not uniform on 310 original configurations. Write `x=r/t`, and let `(R,T)` count root and terminal actions aggregated over the 141 distinct profile paths.

## Theorem: all real positive prices

For every `r,t>0`, the globally minimum expected identification cost is `(R*r+T*t)/141` according to:

| Exact price ratio x=r/t | Globally optimal (R,T) | Optimal population-total cost |
|---|---:|---|
| `0<x<=4/7` | (362,0) | 362r |
| `4/7<=x<=10/17` | (355,4) | 355r+4t |
| `10/17<=x<=3/5` | (338,14) | 338r+14t |
| `3/5<=x<=2/3` | (323,23) | 323r+23t |
| `2/3<=x<=3/4` | (311,31) | 311r+31t |
| `3/4<=x<=7/9` | (303,37) | 303r+37t |
| `7/9<=x<=4/5` | (267,65) | 267r+65t |
| `4/5<=x<=153/184` | (242,85) | 242r+85t |
| `153/184<=x<=1` | (58,238) | 58r+238t |
| `1<=x<=3` | (6,290) | 6r+290t |
| `3<=x<infinity` | (4,296) | 4r+296t |

The eleven feasible witness lines match exact unrestricted Bellman lower bounds at their respective endpoints. At each displayed breakpoint the neighboring lines tie. Within every open phase, every deterministic globally optimal tree has the displayed aggregate (R,T), though its topology may differ.

## Exact endpoint Bellman evidence

| Integer prices (r,t) | Exact optimal total across 141 rooted profiles | Origin |
|---|---:|---|
| (4,7) | 1448 | EC49FQB, previously verified, PR #2515 |
| (10,17) | 3618 | EC49FQD new |
| (3,5) | 1084 | EC49FQD new |
| (2,3) | 715 | EC49FQD new |
| (3,4) | 1057 | EC49FQD new |
| (7,9) | 2454 | EC49FQD new |
| (4,5) | 1393 | EC49FQC, previously verified, PR #2518 |
| (153,184) | 52666 | EC49FQC, previously verified, PR #2518 |
| (1,1) | 296 | EC49FQC, previously verified, PR #2518 |
| (3,1) | 308 | EC49FQC, previously verified, PR #2518 |

Additional interior computations at (7,12), (23,39), (7,10), (48,61) agree. The original EC49FQA unrestricted exact integer Bellman program compares all 228 native legal actions and recursively optimizes every informative response fiber. Duplicate partitions are safely represented by the lowest-priced action; uninformative positive-cost actions cannot improve the objective. Every proper fiber has strictly fewer profiles, so the recurrence covers arbitrary finite decision-tree depths without a depth cutoff. Stored certificates contain exact first-action costs, complete response-labelled trees, source-profile representatives and multiplicities. An independently written verifier reconstructs source responses and replays each theorem witness against all 310 original configurations and all 141 distinct profiles. Results: `EC49FQD_FULL_UNIFORM_POSITIVE_PRICE_PHASE_CERTIFICATE_PASS`, `EC49FQA_ALL_INDEPENDENT_REPLAYS_PASS`.

## Proof: continuum interpolation

For any feasible tree P at t=1 its population-total cost is affine `L_P(x)=R_P*x+T_P`. The unrestricted optimum `f(x)=inf_P L_P(x)` is concave because it is the infimum of affine functions. If a feasible tree L is Bellman-optimal at both rational endpoints a<b, concavity gives `f(x)>=(b-x)/(b-a)*f(a)+(x-a)/(b-a)*f(b)=L(x)` on [a,b], and feasibility gives `f(x)<=L(x)`; hence equality. Each intermediate phase has a response-labelled feasible witness whose aggregate (R,T) matches the exact optimum at its two tabulated endpoints. Therefore the exact finite endpoint checks prove the entire **real interval**, not merely tested rational sample prices. Homogeneity restores general positive (r,t).

For the low-price ray, the previously verified all-root tree has (362,0). At x0=4/7, exact Bellman gives `f(x0)=362*x0`. For any feasible P and 0<x<=x0, `L_P(x)>= (x/x0)L_P(x0)` because its terminal count is nonnegative; taking the infimum yields `f(x)>=362*x`, attained by the all-root tree.

For the high-price ray, independent enumeration of the entire 144-terminal response signature produces exactly 139 signatures across 141 full rooted profiles, with two non-singleton two-profile fibers: representative source IDs {17928,38165} and {24541,38166}. All four profiles have multiplicity one. At least one root action is compulsory along each of these four paths, so every feasible tree has `R_P>=4`. Bellman at x=3 gives `f(3)=308`; hence for x>=3, `L_P(x)>=308+4(x-3)=4x+296`, attained by the feasible (4,296) tree.

Finally, suppose another optimal feasible tree at an interior price has affine cost with a different root-count slope from the displayed optimum. Their difference is nonnegative in a neighborhood and zero at an interior point; a nonzero linear slope would make it negative on one side, a contradiction. Therefore both aggregate counts are fixed in an open phase.

## Validation and next problem

All finite math is exact integer arithmetic over frozen native BRC source-response profiles. Full certificates, independent replays, code and frozen source pair are included in the conversation's EC49FQD evidence bundle. The companion GitHub checker and machine anchor summary preserve the theorem's exact proof relations; GitHub PR #2515 and PR #2518 preserve the original optimizer and independent verifier. Independent mathematical peer review and formal admission remain pending.

The separate **310-original-configuration multiplicity prior** still has unresolved phases in `26/71<x<4/5`; certified subintervals include (648,192) on [7/12,3/5], (549,253) on [2/3,7/10], and (202,499) on [3/4,7/9]. Continue its exact parametric lower envelope without changing the frozen science pin, P000 or source observer definitions.
