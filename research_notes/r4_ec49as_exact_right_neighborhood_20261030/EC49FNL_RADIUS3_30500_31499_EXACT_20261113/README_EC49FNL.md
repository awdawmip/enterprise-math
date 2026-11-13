# EC49FNL: exact BRC radius-three seven-key configurations 30500–31499

Date: 2026-11-13. Scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Role: author-side TASK_RESEARCH, NOT_REVIEWED; formal RS-EC49AS CLAIM not obtained. Continuation of EC49FNK, PR #2278. The next non-overlapping index is **31500**.

## Precise finite problem and theorem

Retain the original nine-state BRC generator, 178,850 original lawful operation words, 94 complete raw cache keys, 24 distinguished observations, and the signed ordered six-axis native path. There are exactly 38,169 indexed radius-three seven-key configurations. For a fixed configuration K, let C(K) be the minimum cardinality of the union of nonempty **complete ordered signed native microstep prefixes** of selected lawful words whose observation labels cover all 24 demands; each selected word must have one of the seven allowed complete raw keys.

**Theorem A (exhaustive finite range).**
For every integer i with 30500 <= i < 31500, the exact rooted-trie demand-subset dynamic program yields C(K_i). The minimum is **94**, attained precisely at indices **31310** and **31323**. The maximum is 206, at indices 30697 and 31130. The two minimizers have keys respectively
`[0,4,5,11,34,49,52]` and `[0,4,5,11,34,49,65]`. Each has an explicitly reconstructed lawful 24-word witness of cost 47 + 47 = **94**, with roots 05 and 06 and unused optional root 07.

The raw master and cases inputs are SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e` and `d18c8f3177083c5b39ef6c8ca068589042617a2a797b53f98818a427040e4f33`. The exact 1,000-row native output is SHA256 `e9036fe1eee06a129e4d60703de7cbb5a230f85a65871cae50702f63511fae85`. The accompanying certificate contains the complete lossless 1,000-value cost vector and both witness sets.

## Stronger structural theorem: complete demand-profile equivalence

Define f_{r,K}(S) for an eligible first signed microstep root r and demand subset S as the minimum number of distinct nonempty original native prefixes of lawful words rooted at r sufficient to cover S (empty S has zero cost). The two cases have precisely the same eligible root sets {05,06,07}, and **the complete exact root-cost functions agree**, not merely their 24-demand global minima:

- For root 05: f_{05,K31310}(S) = f_{05,K31323}(S) for all 2^12 = 4096 supported demand subsets.
- For root 06: the same equality for all 2^12 = 4096 supported subsets.
- For root 07: the same equality for all 2^8 = 256 supported subsets.

Every one of these **8448 exact subset entries per configuration** was independently recalculated by a separate Python prefix-trie DP and matched the C++ table. Nevertheless, the rooted trie node counts are different: for case 31310 the three counts are (20202, 14354, 4257), whereas for case 31323 they are (15459, 8105, 2823). Four of the selected 24 witness words differ. This is concrete exact **demand-profile equivalence without literal native-trie identity**.

**Corollary (scope-typed observational equivalence).** For every subset D of the original 24 observation labels, and for any optimization that uses only the same eligible root allocations and sums the exact f_r costs, replacing cache key 52 by 65 in the indicated six-key context leaves its optimum unchanged. Proof: each permitted root assignment has the identical sum of its three root functions; taking a minimum over the same assignment set preserves equality. This claim concerns the specified demand-prefix observer and its allowed allocations, not arbitrary future native operations or a quotient of complete path provenance.

## Sharp third-root margin

The two cases share the same 8 optional demands Q eligible for root 07. Let L05,L06 be their mandatory 12-demand baselines and set
`F_K(T)=f05(L05\\T)+f06(L06\\T)+f07(T)`, `G_K(T)=F_K(T)-94` for T subseteq Q. The exact exhaustive 256-mask calculation gives

`G_K(empty)=0`, and `min_{T nonempty} G_K(T)=8`,

with equality exactly at eight-bit masks **85, 170, 255** in *both* configurations. In fact the entire 256-entry gap vector agrees. Hence the baseline 05/06 allocation is the unique globally minimal root allocation, and every nonempty transfer to root 07 costs at least 102.

## Proof method and verification coverage

For each fixed root, build a trie whose edges are single **signed, ordered, six-axis native microsteps** from the frozen original generator. At each trie node, combine exact integer minimal costs over the union of terminal demand masks; superset closure gives minimal cost for each demanded subset. Distinct first-root trees have disjoint nonempty prefixes. Therefore minimizing the sum of root costs over all admissible root assignments computes the full global minimum *exactly*. This proves the finite theorem under the declared frozen generator.

Execution evidence: ten disjoint native C++17 scans of 100 configurations each, every one completed with `FINISHED`; all 1,000 output IDs contiguous and unique. Four independent Python full optimizations agreed (30500=124, 31310=94, 31323=94, 31499=188). A further independent Python calculation checked all 8448 root-mask entries for **each** minimizer. Separate reconstruction from the original 178,850-word catalogue checked 24 legal native words per minimizer, their keys, demand coverage and exactly 94 distinct ordered prefixes. The certificate verifier checks the compressed cost vector, both 24-word path witnesses, root profile, all exchange masks and sharp values. These computations are finite and integer-exact; no approximation or unverified asymptotic inference is used.

**Evidence lineage:** frozen source commit `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; immediately preceding author-side work PR #2278 `aa17415412b34bc2483605632bcc99ce39245dd8`; local executable evidence package retains the frozen input, C++17 scanner/root dumper, native logs, 1,000 raw result lines, two raw root-cost tables, two reconstructed original-word witnesses, Python independent full-optimizer and all-root verification, and SHA256 manifest. This branch commits the compact lossless mathematical certificate and checker.

**Open question and next work:** compute indices **31500–38168** (6,669 configurations) with the frozen scientific input. Independently investigate a small local certificate characterizing when a cache-key substitution preserves all root-demand cost functions without exhaustive 8448-mask comparison. Keep provenance and ordered native paths whenever considering more aggressive observer quotients. Full unrestricted seven-key BRC has a separate known 84-prefix feasible bound; this interval is not its global optimum theorem.

**Control status:** Original exact task `RS-EC49AS` was queried with request `em-r4-20261113-1726-ec49as-exact-read-01`, result still QUEUED at the observed check. Own new researcher session request `em-r4-20261113-1727-ec49fnl-authorside-session-01` was likewise QUEUED. There is no CLAIM or formal Result asserted; author-side science remains available for independent Driver review.
