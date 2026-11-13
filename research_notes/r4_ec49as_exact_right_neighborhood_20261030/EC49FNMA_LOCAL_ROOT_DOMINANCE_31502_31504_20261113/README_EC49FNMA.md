# EC49FNMA — local exact BRC root-function dominance and new-root exclusion

Date 2026-11-13. Author-side finite mathematical evidence; not a CLAIM, Result or independent review. Exact frozen science commit: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. This is a structural follow-on to EC49FNM's 31500–38168 segment, not another 38,169-case scan. Exact original native master input SHA256: cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e.

## Finite statement

Original nine-state BRC: 178,850 source-lawful words, 94 complete keys and 24 observation labels. Every word uses its original ordered signed-native X6 microsteps, rather than scalar or endpoint projection. Let C(K) minimize the count of distinct nonempty ordered signed-prefix nodes of legal selected words covering all 24 demands.

| Fixed family index | Seven complete key indices | Exact C(K) | Root demand assignments |
|---|---|---:|---:|
| 31502 | [0,4,5,11,34,61,64] | 108 | 256 |
| 31503 | [0,4,5,11,34,61,65] | 106 | 256 |
| 31504 | [0,4,5,11,34,61,66] | 108 | 1296 |

All three values have exact full source-trie lower bounds and a legal root assignment attaining the value. Independent C++17 and Python reconstructions matched 108,106,108.

## Theorem A: pointwise root-function dominance

For each first signed root r in {05,06,07} and every subset S of labels available at r, define f[i,r](S) to be the minimum count of original source-native nonempty prefixes in root r covering S (incidental labels may also be covered). The root label-domain sizes are 12,12,8, unchanged between configurations 31502 and 31503.

Exact exhaustive comparison of all 2^12 + 2^12 + 2^8 = 8,448 root/mask pairs yields f[31503,r](S) <= f[31502,r](S) in every case; strict in 1,850 pairs and equal in 6,598.

Difference histogram (new minus old):
| First root | -3 | -2 | -1 | 0 |
|---|---:|---:|---:|---:|
| 05 | 32 | 274 | 580 | 3210 |
| 06 | 32 | 273 | 575 | 3216 |
| 07 | 4 | 31 | 49 | 172 |

The feasible root demand assignments of these two configurations also coincide. Across every one of the 256 assignments, total cost at 31503 weakly improves relative to 31502, with difference histogram {-4:4, -3:24, -2:63, -1:101, 0:64}. In particular the unique best 05/06 baseline cost changes 108 to 106.

## Theorem B: sharp uniqueness gap

Only eight demand indices can move to 07: Q=[5,7,11,13,15,17,19,21]. The other 16 labels have a unique eligible root. In either 31502 or 31503 the complete root-assignment space is exactly 256 choices indexed by T subset Q. The baseline T=empty has cost B=108 or 106. Direct exact enumeration verifies that min over nonempty T of C(T)-B is 8 for both configurations. Exact sharp masks, with bit j corresponding to Q[j], are:
31502: [21,85,170,191,255].
31503: [85,138,170,223,255].
Both baseline root assignments are unique global minimizers.

## Theorem C: fourth root does not help at 31504

The 05,06 and 07 root functions for 31504 are exactly identical, on *all* 8,448 masks, to the corresponding 31502 functions. Additional first root 03 is eligible only for original labels 15,17,19,21. There are 1,296 feasible demand assignments: 256 do not use root 03, and 1,040 do. Among the latter the **minimum** is 127 (achieved by exactly two assignments). Among those that do not use 03 the minimum is 108, achieved uniquely by the baseline. Hence no optimal root assignment uses 03. In the exact three-configuration domain, the new-root-use exclusion margin is 19 nonempty original signed-prefix nodes.

## Proof kernel and verification

The original lawful-word paths are partitioned by their actual first signed native microstep. In each root, the trie DP stores the cheapest union of terminal observation-label bit masks. Each used nonempty trie node adds one prefix. Superset minimization yields f[i,r](S). Tries of distinct first microsteps have disjoint original signed prefixes, so the full optimum equals the minimum sum of root costs over every feasible assignment of the 24 labels. No approximation or floating point enters.

The companion executable CHECK_EC49FNMA.py accepts the original frozen master_and_radius3_cases.txt, checks its exact SHA256, reconstructs **all** three root DP tables from source, enumerates all 256/1296 assignments, and asserts the stated equalities, strict gap, root-profile dominance and root03 exclusion. It was run successfully on the frozen input. The original input is preserved in the self-contained accompanying evidence package and in the preceding EC49FNL research evidence package; it is not reconstructed from this report.

This theorem concerns only the three fixed radius-three key sets; it does not establish a bound for unrestricted seven-key selections. The formal Task RS-EC49AS has no current immutable publication directory (observed at Source f9b4c24c15cbcb0f515ca643af10413b5d7f65ae); current execution is author-side, NOT_REVIEWED. The native attempt to register specifically against that unpublished Task returned CANONICAL_REJECTED: UNKNOWN_CURRENT_TASK; do not replay it as if registered.

## Next discriminating problem

From the signed trie modifications caused by one complete-key replacement, derive a structural *small* sufficient certificate of rootwise weak dominance, then seek exact examples where optimum improves although rootwise dominance fails. The separate global-family consolidation question is to stitch saved intervals into one master 38,169-value proof certificate, rather than recount previously executed cases.


## Additional structural theorem: the six-key skeleton

Let K0=[0,4,5,11,34,61], the common six complete keys. Exact recomputation from the frozen 178,850-word input proves f[K0,r](S)=f[31502,r](S)=f[31504,r](S) for **every** root r in {05,06,07} and every eligible label subset S, a total of 8,448 root/subset identities. Thus key64 is wholly redundant for these three roots; key66 likewise does not change their cost functions, though it introduces root03. Key65, in contrast, improves 1,850 root/subset values over the skeleton and never worsens any.

The redundancy is not merely a trivial literal-word-prefix containment. In the frozen source, key64 contributes 280 new 06-root legal words, and key66 contributes 9,540 new 05/06/07-root legal words. Of these 9,820 words, **none** has a same-label path from the six shared keys that is literally a prefix of the added path. The result is about the exact optimum of whole native prefix tries, not a claim of per-word path replacement.

The companion checker recomputes the six-key skeleton's three complete integer tables and tests all 9,820 wordwise containment cases. This strengthens the local three-case analysis without changing its frozen input or extending it to the unrestricted mother problem.
