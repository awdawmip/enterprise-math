# EC49FQH — 全正价格下精确最优首次观测集合（类别16943）

Date: 2026-11-16. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Scientific provenance and scope

The frozen scientific input is commit fc0f038e7bfd12c886b4d37f900bfb770c0f61ab, with original configuration file SHA256 cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e and native named-root cost table SHA256 a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f. Reuse EC49FQD–FQG, in particular [EC49FQG PR #2533](https://github.com/awdawmip/enterprise-math/pull/2533). This is independent portable research; source RS-EC49AS had no current immutable Task publication on the last original authenticated lookup, hence no formal CLAIM/Result is asserted.

The finite model comprises 310 original configurations, 141 distinct complete named-root cost profiles, 144 terminal scalar queries indexed 0–143, and 84 named-root scalar queries indexed 144–227. All 228 physical queries remain available in every descendant node. Two priors: U is uniform on the 141 profiles, M weights profiles by their multiplicities among the 310 configurations. Let root-query price be r>0, terminal-query price t>0, x=r/t. Define A_U(x), A_M(x) to be the sets of every physical index that starts at least one globally optimal, arbitrary-finite-depth, exact-identification decision tree.

## Theorem — complete exact A_U(x), A_M(x) for every real x>0

For U:

| Price region | All optimal initial indices |
| --- | --- |
| 0<x<153/184 | {153,161} |
| x=153/184 | {32,34,153,161} |
| 153/184<x<3 | {32,34} |
| x>=3 | {32,34,140,142} |

For M:

| Price region | All optimal initial indices |
| --- | --- |
| 0<x<17/24 | {153,161} |
| x=17/24 | {59,88,153,161} |
| 17/24<x<7/8 | {59,88} |
| x=7/8 | {46,59,88,93} |
| 7/8<x<33/35 | {46,93} |
| x=33/35 | {16,23,46,93} |
| 33/35<x<1 | {16,23} |
| x=1 | {16,23,124,131} |
| 1<x<3 | {16,23} |
| x>=3 | {16,23,59,88} |

These are equalities for the complete native 228-query action set, not only upper inclusion bounds. In particular, the 15 (M) and 10 (U) price breakpoints where the optimal total cost changes need not be first-query switching points. The M-only indices 124 and 131 remain optimal exactly at x=1. Indices 59 and 88 are optimal again at x>=3 after being absent throughout 33/35<x<3 (including x=1).

## General three-point contact and constant-root-set lemma

For a finite exact-identification experiment with finitely many queries and strictly positive linear prices, discard zero-information and repeated path queries; an irredundant strategy has finite depth, hence finitely many distinct decision-tree strategies. Every strategy pi has cost f_pi(x)=R_pi x+T_pi with R_pi,T_pi nonnegative integers. Thus V(x)=min_pi f_pi(x) is concave and piecewise affine.

Let 0<a<c<b, and suppose exact unrestricted Bellman values V(a), V(b) are known. If a feasible decision tree pi is optimal at c and its exact cost equals the endpoint chord,
f_pi(c)=V(a)+(V(b)-V(a))(c-a)/(b-a),
then the affine difference between f_pi and the chord is nonnegative at a and b (optimality of V) and vanishes at c. Hence this affine difference is identically zero. By concavity V(z) is at least its endpoint chord, and by feasibility V(z)<=f_pi(z), so V(z) equals that chord for every z in [a,b].

Moreover, for any z in (a,b), a tree optimal at z has a nonnegative affine gap from this common value function on both endpoints and zero gap at z; therefore it attains the optimum on all of [a,b]. Consequently, the *entire physical optimal first-query index set* is constant over (a,b), and it equals the exact set computed at the single interior sample c. This lemma applies to every real x in the interval; it does not rely on interpolation of sampled probabilities.

## Native exact computations and certificate coverage

Prior EC49FQD–FQG supplied 25 independently audited endpoint Bellman certificates (9 U finite open intervals and 14 M finite open intervals), together with exact low-price pure-root and high-price minimum-root-count tails. This continuation solved the full unrestricted Bellman problem from the unchanged native original files at 14 new rational interior prices, chosen to collectively hit all 23 open intervals. Each certificate includes all 228 forced-first-query cost entries, two globally optimal trees, exact weighted root/terminal counts, the original 141-profile map and all 310 configuration weights. Original optimizer: EC49FQA_MIXED_PRICE_OPTIMUM.py; original native-data replayer: EC49FQG_PALETTE_VERIFY.py.

| Interior ratio | U optimal first | M optimal first | U weighted (R,T) | M weighted (R,T) |
| --- | --- | --- | --- | --- |
| 1/2 | 153,161 | 153,161 | 362,0 | 962,26 |
| 16/31 | 153,161 | 153,161 | 362,0 | 791,113 |
| 15/26 | 153,161 | 153,161 | 355,4 | 731,144 |
| 13/22 | 153,161 | 153,161 | 338,14 | 648,192 |
| 11/18 | 153,161 | 153,161 | 323,23 | 638,198 |
| 5/8 | 153,161 | 153,161 | 323,23 | 555,249 |
| 7/10 | 153,161 | 153,161 | 311,31 | 549,253 |
| 5/7 | 153,161 | 59,88 | 311,31 | 213,491 |
| 10/13 | 153,161 | 59,88 | 303,37 | 202,499 |
| 18/23 | 153,161 | 59,88 | 267,65 | 193,506 |
| 9/11 | 153,161 | 59,88 | 242,85 | 179,517 |
| 8/9 | 32,34 | 46,93 | 58,238 | 147,545 |
| 17/18 | 32,34 | 16,23 | 58,238 | 112,578 |
| 2 | 32,34 | 16,23 | 6,290 | 5,685 |

For each of the 23 finite open intervals, a sample interior tree matches the exact endpoint-cost chord, both in cost and in its integer pair (R,T); the original Bellman calculation exhaustively verifies all 228 first costs and both priors. The lemma therefore proves the above root sets across the continuum, not merely at 14 sampled prices. Every relevant optimal first index is its own response-partition singleton; the 19 aliases among the 228 physical queries do not hide any additional tied first queries.

A separate independent native-source verifier rebuilds all 228 response vectors and weights from the pinned files, checks 25 original endpoint certificate hashes, replays 54 original trees, checks all 14 new certificate hashes, replays 28 newly saved complete decision trees, verifies exact first-query cost minima and equality with each interval chord and integer slope pair. Outcome: EC49FQH_ALL_14_INTERIOR_BELLMAN_AND_23_OPEN_PHASES_PASS. Arithmetic is integer/rational throughout, no floating-point threshold comparisons. Unrestricted Bellman global optimality is supplied by the exact recursive solver plus inherited endpoint computations; the replayer independently validates input compatibility and tree costs rather than rerunning each Bellman subproblem.

Low-tail exact physical initial indices remain {153,161} for both priors; high-tail first sets are the x=3 endpoint sets. These tail proofs use the inherited pure-root and four-required-root lower bounds. Theorem scope is this specified native class and the two stated priors; it makes no new P000/worldview claim.

## Reproduction and full evidence

Recreate all 14 new certificates using the supplied frozen files and EC49FQA_MIXED_PRICE_OPTIMUM.py with the integer price pairs in the table. The accompanying EC49FQH manifest records all 14 SHA256 hashes and their source pin. Run the new verifier on an unpacked EC49FQG evidence bundle and the new certificates directory. The full local evidence archive includes raw input, 27 prior certificates, 14 new certificates, reproducible solver, two independent replayers, execution log, theorem and per-file SHA256 manifest. GitHub contains this theorem, the exact new-certificate manifest and a concise executable certificate checker; the bundled archive retains the full original 14 machine certificates.

## Next mathematical question

Classify the actual optimal decision-tree families *below* the initial action, including phase-boundary multiplicities, and determine which isolated ties/re-entries survive continuous perturbation of the prior weights between U and M. The present theorem fully settles first-index classification for both specified priors.

### Authority and source state

Independent portable research, no newly claimed formal Task, no Result/Review admission. Researcher provenance EM-DIRECT-E78124, session MCP-ef2538941eb64c15bb3d261fcb4f56b7; existing Activity RA-D62DDE05DA91C7CB0E8C8919. Native continuation request r4-ec49fqg-continuation-20261116-0434-v1 returned FAILED / CANONICAL_REJECTED: unknown current immutable task publication. Checkpoint linkage remains a separate Source operation.
