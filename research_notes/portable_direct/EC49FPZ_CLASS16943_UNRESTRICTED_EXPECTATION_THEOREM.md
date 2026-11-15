# EC49FPZ — exact unrestricted minimum expected BRC sensing cost for class 16943

Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Date: 2026-11-15.

## Proposition and domain

Use the original frozen native BRC scientific pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. The original master is SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; its native named-root cost table is SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`. The native BRC domain represented by original configuration 16943 has 310 configurations, 141 different *full named-root cost profiles*, 144 legal complete terminal scalar observations and 84 legal named-root scalar observations.

A correct identification policy may choose any of these 228 scalar observations as a function of previous exact integer responses. It must identify the full named-root profile of every original configuration. Each observation has unit cost. There is no a priori depth limit. For the uniform prior on the 141 distinguishable root profiles, the global minimum expected observation count is

\[
\boxed{E_{141}^{\mathrm{unrestricted}}=296/141\approx2.09929078014.}
\]

The complete list of globally optimal first-action indices, with terminal observations at indices 0..143 and root observations at 144..227, is `[32,34]`.

For the uniform prior on the 310 original configurations, letting each full root profile inherit its source multiplicity, the global minimum is

\[
\boxed{E_{310}^{\mathrm{unrestricted}}=690/310=69/31\approx2.22580645161.}
\]

The complete set of optimal first-action indices for this prior is `[16,23,124,131]`. Every listed first query is a native terminal observation. Both optima can be attained by exact response-indexed decision trees whose worst-case depth is only 3.

The earlier EC49FPY constructive three-level tree had profile-depth histogram `{2:64,3:77}` and source-configuration histogram `{2:94,3:216}`, hence expected costs `359/141` and `836/310`. These are valid previous upper bounds, sharpened here by 63 and 146 total weighted observations, respectively. For the new uniform-root optimal tree the profile depth histogram is `{1:6,2:115,3:20}`; for the source-configuration weighted tree it is `{1:6,2:111,3:24}` and the source-configuration histogram is `{1:7,2:226,3:77}`.

## Exhaustive exact proof

Let \(\Omega=\{0,\ldots,140\}\) be the 141 distinct named-root cost profiles. The 228 legal queries are the 144 native complete terminal allocations followed by the 84 named-root coordinates `(root, optional-subset-mask)`, all reconstructed from the frozen original master and root-cost CSV. Let \(v_q(s)\) be the exact integer query response. For any nonempty \(S\subseteq\Omega\), the partition \(\Pi_q(S)\) is its family of nonempty equal-response fibers. Two priors have positive integer weights \(a_s=1\), or \(a_s=w_s\) where \(w_s\) is the number of original configurations producing profile \(s\). Write \(A(S)=\sum_{s\in S}a_s\).

For an identified singleton set the future accumulated weighted observation count is zero. For every nonsingleton set, the exact optimal accumulated cost over *all finite adaptive trees of arbitrary depth* is

\[
C_a(S)=\min_{q:\,|\Pi_q(S)|>1}\left(A(S)+\sum_{B\in\Pi_q(S),\,|B|>1}C_a(B)\right).
\]

Indeed, all members of \(S\) pay the current query cost once and continue only along their observed response fiber. Queries with one response fiber do not reduce uncertainty and can be omitted from any optimal policy. Every remaining fiber is a strict subset, so this recurrence is a finite well-founded dynamic program over subsets. It considers every native action and every response and is therefore a global optimality theorem in this finite model, not a depth-three assumption.

The supplied executable verifier applies the recurrence to both integer weight systems. Its depth-one and depth-two checks are exact exhaustive finite subproblems; their values furnish admissible incumbent upper bounds. The lower bound for each candidate first action is

\[
A(S)+\sum_{B\in\Pi_q(S),\,|B|>1}A(B),
\]

because each non-singleton response fiber needs at least one further observation. A candidate can be pruned only when this lower bound is no better than the corresponding current incumbent, separately for both priors. Equal response partitions are equivalent and can be deduplicated. The unrestricted recursion evaluates 7,612 distinct nonsingleton/singleton-reached subset states and obtains exact globally minimal weighted totals 296 and 690. Re-evaluating all 228 possible first actions with the unrestricted recurrence establishes *all* optimal first indices listed above. No floating-point arithmetic, sampling, heuristic beam-search or imposed depth limit enters the lower bound.

For achievability, the verifier constructs separate complete three-level optimal trees for the two priors. It checks every one of the 141 named-root profiles, their exact query responses, unique leaf identity, and weighted total. A separate replay implementation rebuilds the original configuration-root-cost map from the frozen master and CSV, rather than importing the optimization module, and independently checks all 310 original configurations on both trees. The replay reports `EC49FPZ_INDEPENDENT_REPLAY_ALL_PASS`. The two earlier terminal-invisible root-state pairs remain preserved because the action set includes, and the certificates use where required, named-root observations.

## Exact validation

- `python3 EC49FPZ_OPTIMAL_UNRESTRICTED.py frozen_original_master.txt EC49FPG_PROFILE.csv EC49FPZ_CERT_UNRESTRICTED.json` — obtains `UNRESTRICTED (296, 690, 32, 16)`, all optimal first actions, full trees, `SAVED`; original scientific input digests asserted.
- `python3 EC49FPZ_INDEPENDENT_REPLAY.py frozen_original_master.txt EC49FPG_PROFILE.csv EC49FPZ_CERT_UNRESTRICTED.json` — obtains `EC49FPZ_INDEPENDENT_REPLAY_ALL_PASS`, validating 310 source configurations and 141 full root profiles under both priors.
- Certificate SHA256: `3e343a2553324579eef28e5de90dcfcbbba624d1c42d715f467439f83f8fa387` (full 41,595-byte JSON, including all 228 first-action exact costs, root weights, both 141-leaf decision trees and replay summaries).

Inputs and machine proof artifacts are in the accompanying verification archive; canonical source evidence for this original cost table is EC49FPG PR #2472 and EC49FPY PR #2509. Current mathematical status is **author-proved with independent configuration replay; no independent project theorem review or formal admission performed**.

## Interpretation and next directions

The optimal first question depends on whether equal weight is assigned to each distinguishable named-root profile or to each underlying configuration. The observation maps are the same; the prior multiplicities affect optimal branching. A rare named-root query is still necessary along the terminal-gauge ambiguity fibers, but the globally optimal first actions for both priors are terminal queries.

Next: (1) exact finite optimization with distinct root and terminal prices in class 16943, including price breakpoints and proof of which regimes require root observations; (2) identify minimal observer repair for other previously unclassified native BRC root domains, preserving the named-root gauge provenance; (3) independent mathematical review of the full finite Bellman checker and its input lineage. No changes to P000, ACTIVE worldview, task publishing or formal CLAIM are proposed.
