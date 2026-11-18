# EC49FIV — B=9 remaining cache-reallocation cases: exact six-path local optimum (2026-11-11)

## Scientific question and frozen inputs
Under the frozen 24-observation nine-state BRC problem, determine whether any six-path replacement of each known seven-key, 94-native-prefix witness A/B can reach at most 93 distinct signed ordered six-axis prefixes, with at most seven complete raw cache keys.

Science pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Source witness and legal-word generator: EC49FGJ / EC49FGW (in the existing EC49 research line); previous exact source EC49FIS, EC49FIT, EC49FIU in PR #1730. All 178,850 admissible BRC words are used where a full catalog is required. P000 and native X6 path semantics unchanged.

For a replaced six-observation set Q, write F_Q for the native-prefix union of the other 18 fixed original words. Every case here has |F_Q|=84, hence the 93-prefix target permits at most 9 new prefixes. Original witnesses give feasible cost 94.

## New exact finite result
For **both A and B**, the **38 previously unresolved six-path cache-reallocation backgrounds with B(Q)=9** have exact minimum **94** native prefixes among legal completions using <=7 complete raw cache keys. Across A+B this resolves **76 distinct fixed-background instances**. The originally reported per-profile 87 unresolved possible-key-reallocation instances (EC49FIU) thereby fall to **49** (budgets B11:6, B15:32, B17:8, B18:2, B23:1). The stronger global seven-key optimum remains an open question.

### Exhaustive proof and computation
1. **H8 quadruple plus one H7 label**: for each profile, 26 of the 38 B9 backgrounds share two H7-target variants of a fixed H8 four-target prefix background. Over *all* legal raw keys, the exact native prefix-tree Steiner/coverage DP yields min 10 newly used prefixes for all four distinct five-label problems. It excludes 26 cases per profile, **52 across A/B**, without using the key cap. The four H8 labels are (8,1),(8,2),(8,4),(8,8); H7 label is profile-specific. Actual result: `EC49FIV_H8H7_PASS 52 52`.
2. **H6 quadruple plus two tail observations**: the remaining 12 per profile contain four H6 labels at positions 10..13. In eight of twelve backgrounds per profile, the last two observations alone already require **10** new native prefixes (all legal keys, exact two-label trie); this excludes **16 across A/B**. The other four per profile remain for step 3. Actual result: `EC49FIV_H6TAILPAIR_PASS excluded 16`.
3. **Complete six-demand key-aware exact DP**: for those final four per profile, fixed paths use exactly six distinct complete raw keys. Any <=7-key completion uses the fixed six and at most one additional raw key. Enumerate every new-key choice (or none), all 178,850 admissible words, and all six required labels. A candidate word with more than nine new prefixes is dominated by the budget. Encode remaining exact signed ordered native prefixes as bitsets. At each demand, merge bitsets by union, reject cardinality >9, and retain inclusion-minimal antichain states. Dominance is sound because X subset Y implies X union Z subset Y union Z for every future Z. Every allowed key choice ends with zero feasible states. **8 backgrounds excluded**. A distinct second implementation using exact, non-pruned bitset states agrees on all eight: `INDEPENDENT_8_CASES_VERIFIED`.
4. In all cases the original witness remains a legal 94-prefix completion. Thus finite lower bound >=94 and original upper bound <=94 establish the exact local value 94.

Coverage by profile: **26+8+4=38**, therefore **76** across A+B. Directly excluded B9 instances: **zero 93-prefix completions**. The proof optimizes the stated fixed-18/six-replacement neighborhoods, not arbitrary global construction space.

## Reproduction and durable evidence
The three executed programs, an independent non-pruned checker, three complete JSON reports, and actual run logs are stored, losslessly, in three contiguous UTF-8 base64 text chunks (no newline within chunks):
`EVIDENCE_EC49FIV.tar.xz.b64.part01`, `part02`, `part03`. Concatenate in numerical order, base64-decode, and xz-extract. Exact tar.xz SHA-256: `e6dd0812f51afc045ff9b9778377405547785937b8cc8efa72d69afbe928073e`. The four programs use the previously pinned EC49FGW / EC49FHD source and EC49FIS / EC49FIU report inputs; original dependency files are also contained in the separate full working evidence package. No new science input pin is created.

The proof's complete native-prefix tree recurrence uses submask convolution, and the bitset DP counts native *prefix unions*, not coarse cell endpoints. Run logs: H8+H7 `wall=29.61s`, H6+tails `wall=17.93s`, final six-label key DP `wall=4.67s`, independent audit `wall=4.77s`. These are the actual local executions, not a benchmark claim.

## Next research unit and admission status
Next: exact B11 cache-reallocation six-path backgrounds (6 per profile); for Q={two H7 observations, all four H8 observations}, compare key-free six-label prefix-tree lower bound with the actual B=11 budget and, if tied, run complete <=7-key DP. Then B15 backgrounds.

Researcher author-side result, **not yet an approved immutable Task Result or independent Driver mathematical admission**. Preserve the frozen pin and the actual current owner/CLAIM state. GitHub PR material is durable research evidence; it is not a canonical task-state mutation.
