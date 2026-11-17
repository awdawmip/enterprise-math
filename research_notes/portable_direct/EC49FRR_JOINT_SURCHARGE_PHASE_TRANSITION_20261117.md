# EC49FRR-B — Exact native-BRC joint named-observer surcharge transition

Date 2026-11-17. Original BRC class-16943, immutable frozen scientific pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Original source / unrestricted Bellman baseline from EC49FRQ PR #2642@350043ef311e2a3fe292f586657386e61ad2854a. Evidence: AUTHOR_PROVED / EXACT_FINITE_BELLMAN_228 / NOT_REVIEWED.

**New price model.** Preserve the original 141 complete named profiles (310 original configurations), all 228 original *named physical BRC observations* q=0..227, all native response relations and legal full identifying trees. Work at uniform root/terminal price ratio x=1, profile-uniform prior lambda=0. Charge each observation t>0, except **both** named terminal observations q32 and q34, each costing (1+epsilon)t, real epsilon>=0. This modifies the decision-maker's cost functional, not the native BRC scientific input.

**Theorem (complete real surcharge domain).** The global Bellman optimum over all legal full original deterministic identifying trees Q is

\[
\boxed{V(\varepsilon)/t=\min\{296+141\varepsilon,298\}/141,\quad\varepsilon\ge0.}
\]

The exact set of *all* optimal first named physical actions equals {32,34} for 0<=epsilon<2/141; {32,34,140,142} at epsilon=2/141; and {140,142} for epsilon>2/141. The transition is unique at epsilon_*=2/141.

**Original complete named tree witnesses.** The original unrestricted x=1,lambda=0 Bellman certificate has optimum uniform path total 296 and precisely the optimal first physical actions [32,34]. Original complete tree A (root q32) and A' (root q34) each identify all 141 profiles at worst depth 3 and have original 141-state path cost total 296; their combined q32/q34 path incidence total is exactly 141. A uses q32 on all 141 state paths and never q34, while A' uses q34 on all paths and never q32. Original complete trees B (root q140) and B' (root q142) each have uniform path total 298 and **zero uses of both charged q32 and q34** on all 141 paths, with depth 3. All four full trees are replayed against the original exact native physical BRC responses, with all original configuration multiplicities retained. Therefore A,A' attain path sum 296+141epsilon, and B,B' attain 298 for every real epsilon>=0.

**Full original Bellman certificate at the transition.** At epsilon*=2/141, multiply path costs by 141 to work entirely with integers. Original named q32/q34 each costs 143 integer units; every other named original observation costs 141. For a set S of original named states, every legal first query q separates S into exact original native BRC response fibers S_{q,z}. The unrestricted recurrence is

\[
F(S)=\begin{cases}
0,&|S|=1,\\
\min_{q:\;q\;\mathrm{separates}\;S}
\bigl[(141+2{\bf1}_{q\in\{32,34\}})|S|+\sum_z F(S_{q,z})\bigr],
&|S|>1.
\end{cases}
\]

Enumerate **all 228 physically named observations** and every nontrivial response subset, without dropping relations by name. The original frozen 94-family BRC source master and root-profile CSV reconstruct the 141 native state profiles, including all 310 configuration weights. Exhaustive memoized integer Bellman evaluation visited **13,063** finite state subsets and returned exact root value **42018 = 141*298**, and *all* minimizing first observations precisely **(32,34,140,142)**. The attached Python checker reconstructs independently all original 228 query response vectors. The source's 144 terminal query names agree entrywise; the two implementations enumerate 84 root subset labels in differing orders, so comparison uses an **explicit bijection by source-native (root,subset) key**, not assumed positional equality. The checker verifies both source SHA256 fingerprints, unrestricted original baseline, all four full original named-tree witnesses and surcharge incidence.

**Continuous proof.** Every fixed full original Q costs the affine function

\[
C_Q(\varepsilon)/t=[U(Q)+\varepsilon(n_{32}(Q)+n_{34}(Q))]/141,
\]
where U(Q) is the number of observations summed across all 141 state paths and each incidence is nonnegative. At eps=0 the exhaustive minimum is 296; at eps*=2/141 the exhaustive minimum is 298. For any 0<=eps<=eps*, linear interpolation of the two exact lower bounds gives minimum >=296+141eps, attained by A. For eps>eps*, monotonicity of each tree cost implies global minimum >=298, attained by B. This proves the formula for *every real epsilon*, with no continuous sampling assumption.

**Exact first-action classification.** In the strict interior 0<eps<eps*, a competing tree can meet the interpolated global minimum only if it meets both endpoint minima (both endpoint gaps are nonnegative, and their positive convex combination must vanish); consequently its initial named observation belongs to the intersection of [32,34] and [32,34,140,142], namely [32,34]. For eps>eps*, any tree optimal at eps must already be optimal at eps* (positive price increments and constant value 298); any first q32 or q34 imposes positive extra cost on all state paths, so neither can remain optimal. The two other original first actions [140,142] are witnessed by B/B'. Boundary first sets were obtained by complete original Bellman enumeration. QED.

**Exact evidence:** new source-faithful Python checker EC49FRR_JOINT_SURCHARGE_PHASE_VERIFY_20261117.py and exact JSON certificate in this commit. Original raw master sha256 cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e; original profile CSV sha256 a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f. Archive with all original frozen data, inherited full named trees/DP and new verified results: **EC49FRR_NAMED_OBSERVER_PRICE_PHASE_COMPLETE_EVIDENCE_20261117.tar.xz**, **241904 bytes**, SHA256 **7f35a89b7daa4c62e091caa5e2bf32ba85293ffcdf57ef91366de715e055b14d**. After decompression all 26 manifest-listed files verified by size and SHA256.

**Research consequence / next:** Original four aggregate count coordinates cannot capture even this two-query price sensitivity: an observation-indexed native action incidence vector is required. Next construct the exact 228-action parametric Bellman/Pareto oracle under a specific bounded surcharge polytope, retaining source labels/provenance and future-observer-safety scopes. P000, native X6, named joint BRC observations, original frozen science and current Source authority are unchanged. No CLAIM, Activity, Result, Review or admission authority is implied by this proof/publication.
