# EC49FIW — Exact optimum for 98 six-path cache-reallocation backgrounds (2026-11-11)

Researcher: EM-DIRECT-0DCE73 / TASK_RESEARCH; activity RA-F42EB5F7DE32683F23A39134. Frozen science fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Independent author-side finite exact result; sources EC49FGJ/FGW/FIS/FIT/FIU/FIV on PR #1730.

## Exact theorem
For each original BRC witness A and B with 24 observation labels, seven complete raw cache keys and 94 distinct nonempty ordered signed X6 native-microstep prefixes, fix the 18 original paths outside one of the 49 previously unresolved genuine cache-key-reallocation six-path position sets Q, and replace the six Q paths by any legal words meeting their six original observation requirements. Require at most seven complete raw cache keys among all 24 paths. For **all 49 Q for each of A and B (98 subproblems)** the exact minimum total distinct native prefix cost is **94**.

Writing F_Q for the literal native-prefix union of the unchanged 18 paths and P(w) for the full signed ordered prefix set of w:

    min_{legal six replacements, #complete raw keys <=7} |F_Q union P(w1) union ... union P(w6)| = 94.

The original A or B witness provides the upper bound 94. The exact lower bounds below exclude 93. The frozen BRC grammar has 178,850 legal words and 94 possible complete raw key types. No endpoint-only or unordered compression is applied.

## Full 49-background classification per profile
| 93-prefix residual budget B=93-|F_Q| | Q per witness | Exact minimum new prefix cost |
|---:|---:|---|
| 11 | 6 | 12 (unrestricted-key) |
| 15 | 32 | 16 for 28 unrestricted-key; 4 require seven-key proof |
| 17 | 8 | 18 (unrestricted-key) |
| 18 | 2 | 19 (unrestricted-key) |
| 23 | 1 | 24 (unrestricted-key) |
| Total | 49 | Every constrained optimum B+1 |

The disjoint 49 Q are: all six pairs from 14..17 plus (18,19,20,21); all 36 sets (i,18,19,20,21,j) with i=0..17 and j in {22,23}; (10,11,12,13,22,23), (14,15,16,17,22,23); the four (10+i,14+i,18,19,20,21) with i=0..3; and (18,19,20,21,22,23). Their exact budgets computed from the original witnesses equal the stated histogram for A and B.

## Exact signed native-prefix-tree dynamic programming
Construct the complete rooted trie of legal full signed ordered X6 microstep prefixes for the six observation demands. Set edge cost c(e)=0 iff that literal nonempty prefix is already in F_Q, and c(e)=1 otherwise. Let d_v(S) be the minimal subtree cost below vertex v covering each required observation label in S. The exact child merge is:

    d_new(S)=min_{T subset S}[d_old(S\T)+d_child(T)+c(e)*1[T != empty]].

Proof: At a trie vertex any selected rooted subtree partitions its covered label set among existing child branches and the newly merged child; its edge is paid exactly once iff the new child is used. Conversely, every partition in the recurrence yields a feasible union of rooted native word-prefix paths. Induction over all vertices proves equality. A separately executed second implementation uses attained-terminal-label masks and OR-union, rather than requested-mask subset partitions. Both agree on all 98 unrestricted-key optimizations. In 90 cases their minima exceed the budget B by 1, proving 94 without any cache-key cap.

## Remaining eight cache-key-sensitive cases
The four Q per profile are (10,14,18,19,20,21), (11,15,18,19,20,21), (12,16,18,19,20,21), (13,17,18,19,20,21). For each fixed 18-path background |F_Q|=78 and exactly six original raw cache keys remain used. Hence any <=7-key completion uses these six plus no more than one additional key. Among 94 possible keys, 88 are outside these fixed six. Enumerate all 89 legal key pools (six alone, six plus each extra key), and solve the exact six-label weighted-prefix trie problem restricted to each pool. The attained-label-mask independent solver also recomputed **every 89 x 8 = 712 exact key-choice minima**.

All eight profile/Q cases have minimum new prefix count **16**, each checked by both algorithms, and zero keys attain <=15. Therefore every exact optimum is |F_Q|+16=78+16=94. Actual run: KEY_AWARE_COMPLETE 8 new94 8, with four Q for each of A,B, each 89 key choices and no improving key.

## Combined frontier and verification
After EC49FIU the genuine cache-reallocation residue was 87 per witness. EC49FIV solved 38 budget-9 Q per witness, and this unit solves the remaining 49, closing **all 87 genuine cache-reallocation Q per witness**. The distinct forced-original-seven-key Q described in EC49FIS/FIR (26,681 per witness reported there) remain to be compared against EC49FIQ's seven-key radius-six theorem; the full-radius-six and global seven-key optimum questions retain their stated separate scopes.

Full local evidence archive prepared: EVIDENCE_EC49FIW.tar.xz, SHA-256 12ab5b7b45bf7047b6094432127ae5d90fed27f1839d961ad61b7780fac01196, containing both executed C++ implementations, two Python drivers, original pinned generator/witness, full 49-Q report, full 712-key-choice report, original logs and README. The original EC49AS task is not current as an immutable publication (CANONICAL_REJECTED: NO_CURRENT_IMMUTABLE_PUBLICATION); no CLAIM, Result or Driver acceptance is asserted. P000 and native X6 premises unchanged.

Next: exact set intersection of EC49FIS/FIR forced-restoration Q and EC49FIQ's covered six-path Q; test uncovered cases with complete seven-key trie, then radius-seven or global 93-prefix constructive search.
