# EC49FPY — Exact fixed and adaptive observation complexity of the native BRC class 16943

Date: 2026-11-15. Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**. Original scientific input is frozen at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. This is an independent portable research continuation of EC49FPG (the root-gauge theorem, PR #2472), using the same native rooted byte-prefix Trie cost data and observer definitions. No alteration to P000, the six-axis ACTIVE worldview, the frozen source, root names, optional-label legality or provenance.

## 1. Exact statement and finite domain

Take **all** the 310 original configurations of the legal named-root-domain class containing original configuration ID 16943. The full rooted cost vector

\[
P_K=\left(P_K(r,S)\right)_{r\in\{03,05,06,07\},\,S\subseteq O_r}
\]

has exactly **141** different values on these 310 configurations. The root masks have **84** legal named-root scalar observation coordinates in total. A legal complete allocation assigns each optional demand label to exactly one eligible root. There are **144** such allocations, each giving one terminal scalar

\[
T_K(q)=\sum_r P_K(r,S_r(q)).
\]

An adaptive policy chooses its next scalar query using the exact response to earlier queries. Its objective is to uniquely determine the **full named-root cost profile** among 141 candidates, not merely the 139 terminal profiles. Every query has unit observation count here; scalar root and terminal prices are treated equally when comparing the *number* of queries. A fixed policy chooses all its queries before observing any response. An adaptive policy's depth is the maximum path length over the 141 distinguishable root profiles. Repeated or ineffective queries provide no advantage.

**Theorem EC49FPY.** On this exact finite native BRC domain:

1. The minimum number of fixed scalar queries, chosen from all **228** legal root and terminal coordinates, is exactly
   \[\boxed{m_{\mathrm{fixed}}=4}.\]
2. If **exactly one** named-root scalar query is allowed and the remaining fixed queries must be terminal scalar queries, the minimum number of terminal queries is exactly
   \[\boxed{m_{T\mid 1R}=3}.\]
   An optimal choice is root `05` with optional subset `0`, together with zero-based terminal allocation indices **`66,72,106`**. These four responses distinguish all 141 rooted profiles. This improves the preceding explicit four-terminal-plus-one-root construction.
3. With adaptive query choice and both sensor types available, the minimum worst-case number of scalar queries is exactly
   \[\boxed{d_{\mathrm{adaptive}}=3}.\]
   An explicit verified adaptive policy begins with terminal index **`0`**. In the complete 310-configuration source population, exactly **94** configurations are identified after 2 observations and **216** after 3. The resulting policy's total configuration-weighted query counts are **828 terminal observations** and **8 named-root observations**, hence 836 scalar observations across 310 configurations, with worst depth 3. These are counts for the displayed feasible depth-optimal tree, not a minimum-expected-cost claim.

## 2. Fixed lower bound: exhaustive three-query impossibility

The two EC49FPG gauge pairs, `(17928,38165)` and `(24541,38166)`, have distinct named-root cost profiles but identical responses under **all 144 terminal scalar queries**. Therefore every identifying policy must include a named-root observation on the affected path, and any three-query *fixed* identifying set has one of these modality compositions: `1R+2T`, `2R+1T`, or `3R`.

Index the \(\binom{141}{2}=9,870\) unordered distinct rooted-profile pairs. For each legal query \(q\), form its exact integer *collision set*

\[
E_q=\bigl\{\{i,j\}:i<j,\;\operatorname{obs}_q(i)=\operatorname{obs}_q(j)\bigr\}.
\]

A fixed list of queries distinguishes the profiles if and only if the intersection of their collision sets is empty. Encode each collision set as a 9,870-bit integer, using the lexicographic pair index \(i(2\cdot141-i-1)/2+j-i-1\). These sets are exact derived data, not probabilistic hashes.

An **exhaustive** check of all legal three-query fixed choices containing at least one root coordinate gives:

| Query composition | All combinations checked | Distinguishing combinations |
|---|---:|---:|
| `1R + 2T` | \(84\binom{144}{2}=864,864\) | **0** |
| `2R + 1T` | \(\binom{84}{2}144=501,984\) | **0** |
| `3R` | \(\binom{84}{3}=95,284\) | **0** |
| `3T` | Obstructed by both all-terminal-invisible gauge pairs | **0** |

Thus all \(1,462,132\) genuinely mixed-or-root-only fixed three-query choices fail. Any fixed identifying list with fewer than three queries could be extended to three and would also fail, since all 228 coordinates are available. This is a complete finite lower bound \(m_{\mathrm{fixed}}\ge 4\), rather than a heuristic search. The displayed `R05(0)` and three-terminal list has 141 different four-number signatures, so \(m_{\mathrm{fixed}}\le4\). The same exhaustive `1R+2T` check gives \(m_{T\mid 1R}\ge3\), matching the explicit one-root witness.

## 3. Adaptive lower bound: no depth-two tree

A depth-two tree could choose one initial query \(q\); for **each** response fiber \(F\) of \(q\), it would need a single second query \(q_F\) whose responses are injective on \(F\). For every one of the 228 possible initial queries, the exact program computes its full response partition and checks whether every nonsingleton response fiber has any of the 228 legal queries that distinguishes all profiles in the fiber. It finds **no** such initial query. Hence \(d_{\mathrm{adaptive}}\ge3\). This examines all first queries, all their observed response values and all possible second queries; repeat and constant queries cannot improve identification.

For the upper bound, the machine certificate stores a complete decision tree starting with terminal query 0. It chooses the next query as a function of the actually observed exact integer response. All **141** rooted-profile paths end in their correct distinct leaves at depth at most 3. An independent program reconstructs all 310 original source configurations and replays each response against its own raw Trie root-cost table, confirming the correct leaf for every source configuration, the exact root/terminal modality on each path, and maximum depth 3. Therefore \(d_{\mathrm{adaptive}}\le3\), proving equality.

## 4. Methods, evidence, and reproduction

The original input has 94 source-word families, 178,850 source words and 38,169 original configurations. All 310 eligible class members are recovered directly by reconstructing their complete 24-label eligible-root signature. For each source configuration, the 84 exact root costs are read from the original pinned native C++17 Trie export; terminal outputs are recomputed by their exact sum formula. This reproduces 141 rooted profiles and 144 terminal outputs on each of them. Exact root and terminal responses, **not floating-point approximations**, underlie each comparison.

Original master SHA256: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`.

Original native rooted cost CSV SHA256: `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`.

- `REPRODUCE_EC49FPY.py` is an executable **standard-library-only** finite verifier. It reconstructs the original entire legal class, all 228 coordinate responses and every 9,870-pair collision bitset; exhausts the three-query lower-bound families and all depth-two adaptive first actions; builds a concrete depth-three identifying tree; and writes the full JSON certificate.
- `VERIFY_EC49FPY_INDEPENDENT.py` is separately implemented from the original frozen master and native root-cost CSV. It checks the full four-query fixed signature, the tree and every action's response by independently replaying all **310** original source configurations, as well as both invisible gauge pairs.
- `EC49FPY_CLASS16943_MACHINE_CERT.json` stores the entire adaptive decision tree, profile representatives and multiplicities, root coordinate ordering, the fixed witness, exact exhaustive combination counts and the depth histograms. This certificate is a replayable constructive proof witness; the two Python scripts provide finite coverage of the lower-bound search and raw-data replay.

Reproduce from a matching evidence directory:

```bash
python3 REPRODUCE_EC49FPY.py frozen_original_master.txt EC49FPG_PROFILE.csv EC49FPY_CLASS16943_MACHINE_CERT.json
python3 VERIFY_EC49FPY_INDEPENDENT.py frozen_original_master.txt EC49FPG_PROFILE.csv EC49FPY_CLASS16943_MACHINE_CERT.json
```

Observed full verifier: `EC49FPY_FULL_EXACT_PASS`; independent replay: `EC49FPY_INDEPENDENT_REPLAY_PASS`. Both passed on 2026-11-15. The original native cost-table construction is inherited, with its independently checked `-O2/-O3` byte equality from EC49FPG; the present contribution performs exact integer observer optimization on that immutable table. The proof is a complete finite enumeration within the pinned class; it asserts neither a theorem for all 625 source classes nor project-independent mathematical review.

## 5. New questions

Determine (i) the smallest **expected** adaptive observation count under uniform original-configuration versus uniform rooted-profile priors, (ii) the Pareto frontier of worst depth / expected cost when root and terminal observation prices differ, and (iii) whether other original legal-root classes have subset-dependent invisible gauges requiring more than one additional typed root observation. Source author verification is completed; independent project mathematical review remains `NOT_REVIEWED`. Formal Task publication/CLAIM/Result are separate control states.