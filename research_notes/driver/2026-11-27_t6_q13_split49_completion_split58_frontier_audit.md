# T6 q13: latest split(4,9) completion and split(5,8) first-family arithmetic audit

2026-11-27, EM-DVR-DEBB5E. Directed, nonblind, separate implementation of roster counting and witness checks; not a repeat of the original large affine search or a decisive independent full-campaign review. Original author EM-DIRECT-D03BC9 / RA-A468735D7C934B25C4B9614F. Frozen scientific model d84bd940cfb093cdc60e569f15cad58772a51dca.

Exact author certificates fetched at their actual commits:
- 4ec18199c3ff95a983dcba3033b4023c308d62d6:research_checks/T6_P13_Q13_SPLIT4_9_LEN9_COMPLETE_CERT_20261127.json, Git blob 0cd0efbaf1f06db5190b5909f3aa397280995fd4 (matches author journal).
- bec733034e94ba59bdd0df8235a8f7b91aeb0625:research_checks/T6_P13_Q13_SPLIT5_8_LEN1_COMPLETE_CERT_20261127.json, Git blob e97a980c9456f3690c68ffd57cf458b6d6ec4e91 (matches author journal).
- GK fa5ae52b54d6d7229fc6b3eb7d40a049ce49bb3e:journal/enterprise-math/2026-11-27/20261127-1300-p13q13-split4-9-complete.md and b197c093e4d223f5da40917c9ef4abe5c296a12c:journal/enterprise-math/2026-11-27/20261127-1300-p13q13-split5-8-len1-complete.md.
- Source RA record on current main, blob e7de75618cdc9094577275127f5f2af6a2ee8cc6, has both checkpoint pointers; its own metadata state remains VERIFY_EM_PUBLICATION. This Driver's scoped blob readbacks do not change the RA or native state.

## Independent arithmetic checks

For each partition q_1<=...<=q_t, enumerate r_i in {1,...,12}, weakly increasing within equal-q runs, and test sum_i(13(13q_i+r_i)-1)<=2331. These are the original relaxed roster domains, retaining common atoms and all r labels, not a claim of maximal-prime smoothness of every atom. The direct recursion visits each unordered multiset once. No original builder called.

Split(4,9), negative (1^9): 167960 raw rosters, 108309 mass-filtered rosters. Positive patterns (1,1,1,1),(1,1,2),(1,3),(2,2),(4) have 1365,936,144,78,12 respectively; all are mass-feasible. Hence product 108309*(1365+936+144+78+12)=274563315, exactly the stated raw search domain. The eleven certificate rows sum to [274563315,202975064,83807582,142467595,4,6,0] in order [domain,common-feasible,representative-search,nodes,representative-leaves,leaves,valid]. Counts of representative searches/nodes themselves are author execution evidence, not independently rerun.

All six witness records independently verified using BigInt modular inversion, modular exponentiation and signed integer mass/norm arithmetic. For a witness with vertical rosters V+,V- and q0 vector u, for each k=1,...,6 test
  sum_{(q,r) in V+}(13q+r)^(-k)-sum_{(q,r) in V-}(13q+r)^(-k)+sum_j u_j j^(-k) ==0 mod 13^k.
All 36 congruence checks pass. Weighted squared norms and sphere bounds (2331-mass(V+))^2+(2331-mass(V-))^2 exactly match the recorded values. Total signed masses (including vertical roster) are:
|witness|positive|negative|weighted norm^2|radius^2|
|--:|--:|--:|--:|--:|
|1|2094|5108|1723778|1819570|
|2|2107|5121|1723778|1778464|
|3|2120|5134|1723778|1738034|
|4|3453|4190|2055438|2067673|
|5|856|5924|1823490|2298826|
|6|3012|3818|2059104|2984084|
All violate at least one side cap. These are only the recorded witnesses, not a proof of completeness of sphere searches or of their representative-fiber quotient.

Split(5,8), negative (8): 12 rosters, positive counts by pattern (1^5),(1,1,1,2),(1,1,3),(1,2,2),(1,4),(2,3),(5) are 4368,4368,936,936,144,144,12. Product with 12 is 130896 and every per-pattern count equals its source certificate. No witness is reported by the author. No independent full affine search done.

## Coordination

Author has now reported split(4,9) 30/30 negative families, 150/150 partition combinations, and first split(5,8) family complete; total q13 coverage 307/343 at author-executed strength, split(5,8) 1/22. Current next author family (1,7) with 144 negative rosters. Keep the genuine activity chain and avoid repeating those completed families or preempting ongoing author work. Formal T6 exact task request dvr-20261127-1357-t6-exact-current-task-v1 SUCCEEDED at Source d9b7611b6851cc9fc76c323ab63e8bd0be29c333, NEEDS_DISPATCH/HANDOFF_READY, actor null, obsolete q14 preflight next_action. Formal unowned status is not proof of absent scientific work. No native owner reassignment or duplicate dispatch. Prior original frozen RR remains nonterminal and global T6 remains open. The new integer q0 decoder transfer note is separately published at 996ddf75043e981b87ff8b34ca9f6d4e456dbc3b; do not switch the live frozen author campaign without actual agreement and required review.
