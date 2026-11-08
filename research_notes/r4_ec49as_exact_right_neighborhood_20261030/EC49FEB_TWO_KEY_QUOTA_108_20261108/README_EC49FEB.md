# EC49FEB: exact two-key obstruction and 108 full-key late triples

Date: 2026-11-08. Frozen scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Scope: H4–H9 of original typed native-X6 six-operator model with the nine-state observer and full positive BRC cache key; late quotas (2,4,2,4,4,2), rank nine at each horizon. Author-side exact finite research; independent canonical Driver review pending.

## Definitions and proof

For complete words consisting of original ordered operators a,c,d,e,f,g, the exact nonnegative integer DP tracks (na,nc,nd,ne,nf,ng,q), initially zero counts and observer state zero, appending each of six typed operations by the original state transition. Accepted words satisfy ne=na+1 and a nonzero terminal signature from {1,2,4,8,16,32}. Their complete positive BRC cache key is k=(2ne+nc+nd+nf,nc+nd+ng,ne), and the final signed native-X6 displacement is +2E1. Each window's rational rank-nine signature mask m is characterized by (m&18),(m&20),(m&33),(m&40) being nonzero. A two-word rank-nine choice forces the distinct signatures 16 and 32. At quota four, the minimal covers are {16,32}, {16,1,8}, {32,2,4}, {1,2,4,8}; any such cover extends to quota four if the pool has at least four distinct words.

**Theorem I.** There are 155 keys available to H4–H9. Exactly 124 unordered pairs have sufficient rank-nine support at all six horizons, but none satisfies all six rank-and-quota requirements. Indeed x+y=h+1+nc+nd gives x+y<=9 for H4 and x+y>=10 for H9. A two-key candidate must assign one key to H4 and the other to H9. Quota-two rank nine forces the H4 key to A={(3,2,1),(4,1,1)}, neither of which has any H6 word. Exactly 16 keys independently satisfy H9 quota-two rank nine; none has an H6 word of signature 16 or 32. Thus the required two-word H6 rank nine cannot hold.

**Theorem II.** Of 23728 rank-feasible unordered 3-key sets, precisely 108 meet all six exact quotas. Exactly these sets form the Cartesian family A × B × C, where
A={(3,2,1),(4,1,1)};
B={(3,4,1),(4,3,1),(5,2,1),(5,2,2),(6,1,1),(6,1,2)};
C={(4,6,1),(5,5,1),(6,4,1),(6,4,2),(7,3,1),(7,3,2),(8,2,1),(8,2,2),(8,2,3)}.
Thus 2×6×9=108. Among 16994 rank-feasible triples containing a globally rank-sufficient pair, exactly 44 meet quota as triples. Among 6734 genuinely three-key-needed-for-rank triples, exactly the earlier known 64 meet quota. Every one of the 108 admits a three-block *existence witness* with H4:A; H5,H6:B; H7,H8,H9:C. The exact DP/census script independently checks the 608685 3-subsets, the 108-count, and equality of the surviving set with the displayed family.

**Theorem III.** For the 96 triples with C != (6,4,1), every legal full-word selection is key-rigid in the above block pattern. For the remaining 12 triples with C=(6,4,1), H5 can genuinely mix B and C while retaining four distinct signatures 1,2,4,8. H4 still has to select both signature-16/32 words from A; H6 must take its two signature-16/32 words from B; H7–H9 use C. An exact 18-word H4–H9 mixed witness is recorded in EC49FEB_EXACT_WITNESS.json. For example H5 words are deggg (B,1), edggg (B,2), ceggg (B,4), and ecccc (C,8), with B=(3,4,1), C=(6,4,1).

## Files and verification

EC49FEB_REPRODUCTION_MINIMAL.py: independent executable standard-library integer DP, exhaustive pair/triple census and asserted 108-family equality.
EC49FEB_EXACT_WITNESS.json and VERIFY_EC49FEB_WITNESS.py: all 18 literal operation words, full BRC keys and signatures, with independent primitive signed-X6 expansion and observer-mask checks. A separate local literal enumerator also matched 74 (h,key) signature multiplicity profiles and 17 primitive expansions; full local evidence sources are in the handoff package attached to the run.

This is a finite H4–H9 construction/classification. The H2–H9 mother objective still requires <=5 full keys and <=93 signed native-prefix Trie edges; verified incumbent 94. Next unit: optimize the 12 genuinely mixed H5 triples in the full early+late model and compare with forced all-B H5 under identical early-path constraints.

Current normative reads: GLOBAL_KNOWLEDGE_V1 main@62a1dacf3d36e58f81333cd94f6ba804524f5649; Enterprise Math main@03f893a3c65c84844a40a82d8c31c58d934282b8. The native EM status/control endpoint reported STATUS_DATABASE_UNAVAILABLE, operation_sent=false; active owner, CLAIM, Source Result and Driver admission remain unconfirmed. Author-side GitHub persistence is not a native CLAIM or review.
