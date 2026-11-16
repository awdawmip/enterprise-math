# EC49FQN — Frozen-source machine-certificate index

Date 2026-11-16. Scientific status AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Research type: independent portable contribution; no formal Task/CLAIM/Result/Review.
Frozen scientific commit: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Predecessor: PR #2552 (EC49FQM), PR #2548 (EC49FQL), PR #2539 (EC49FQI).
The complete theorem is EC49FQN_SEVEN_PRICE_GLOBAL_ENCLOSURE_THEOREM_20261116.md.

## Original pinned native inputs
- source/frozen_original_master.txt SHA256 cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e
- source/EC49FPG_PROFILE.csv SHA256 a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f
- 141 complete named-root profiles; 310 original configurations; 144 terminal plus 84 root query indices; 228 physical queries grouped to 209 response partitions for Bellman state calculations while retaining all physical first-query labels.
- At prior lambda=a/b, Bellman integer weights w_i=310(b-a)+141*a*m_i. The *unnormalized* optimum sums w_i times integer root/terminal action prices; to recover expected monetary cost, divide by 141*310*b. For r:t=4:3 or 8:3, the dimensionless cost v=V/t also divides by t.

## Eight newly generated exact rational Bellman anchors

| Price r:t | lambda | Unnormalized optimum | Complete optimal physical first query indices | Certificate SHA256 |
|---|---|---:|---|---|
| 4:3 | 0 | 277140 | 32,34 | 3cefe11f933f46472d2b02a45b223d3bee8a91203f719ee693e9e37354f3d7e4 |
| 4:3 | 310/4399 | 1232753130 | 32,34,140,142 | 13622cbb01d72a54ebab8208870855557602989194105ea70b5f8f2018fe995b |
| 4:3 | 620/3299 | 932989950 | 16,23,140,142 | e3274d20e57bfee44a9194e4ae7709009384431cd63e2e1019aec2fb012d51e9 |
| 4:3 | 1 | 292575 | 16,23 | 3d3ed7aa931b9c76330cccb0b1c1c2fbfe9f452fc0cfb67c19d7606d1dd8a5b6 |
| 8:3 | 0 | 284580 | 32,34 | ced0b1132a2789d5551db1505bf5a077bb74bbf7a767a9d28f7301bdc5538fac |
| 8:3 | 310/21319 | 6079317930 | 32,34,140,142 | 991597fad390e203d9f59e89ca03150f2527fe64aafddb3d5ecbe656c97b3c47 |
| 8:3 | 620/3299 | 951348150 | 16,23,140,142 | 54cbaccc1f949723bb637c2dceb5e7514a47601786e05e04eeccf41880b41e06 |
| 8:3 | 1 | 295395 | 16,23 | b17786726486caf098105a697ae3814484ce2e9037bb8bae1f1de3852b0f9770 |

The exact filenames follow certificates/r4_t3_lambda_{a}_{b}.json and certificates/r8_t3_lambda_{a}_{b}.json with lambda=0 and 1 written as 0_1 and 1_1. The 17 inherited complete anchors consist of 13 from EC49FQM and four x=2 anchors from EC49FQL. The complete reproduction archive includes all 25 actual full JSON certificates.

## Original independent validation and archive

Evidence archive: EC49FQN_SEVEN_PRICE_GLOBAL_ENCLOSURE_COMPLETE_20261116.tar.xz
SHA256 e8e8c825ebf45f4f0dc3cae56101dd0e955482d3f1d533416b88336d8c21126b
The archive contains 38 verified files, including raw source bytes, 25 complete Bellman certificates, native decoder, primary and independent solvers, a full standalone paper, machine summary, exact validation logs, and SHA256SUMS.
Reproduce by unpacking into one directory, then running:
1. sha256sum -c SHA256SUMS
2. PYTHONPATH=code python3 code/EC49FQN_VERIFY_25.py 0
3. PYTHONPATH=code python3 code/EC49FQN_VERIFY_25.py 1
4. PYTHONPATH=code python3 code/EC49FQN_VERIFY_25.py 2

All three partitioned runs (9,9,7 cases) and the independent 8-new-anchor run passed in the author environment. The exact-recurrence validator rebuilds the 228 physical observations and 209 partitions from the frozen source, recomputes all unrestricted optimal first-query sets, and replays every optimal-first witness tree. The separate mathematical argument uses concavity and affine endpoint contact, which is what extends these rational anchors to real parameters.

## Certified continuous enclosure

Exact full-prior price sections: x=1,4/3,3/2,2,5/2,8/3,3.
Every real lambda in [0,1] and x>=1 satisfies
0 <= min(A,B,C)-v(lambda,x) <= 25/28538 when 1<=x<=3,
and on x>=3 the exact optimum is min(B_h,C_h).
For lambda>=620/3299 and 1<=x<=3 the exact optimum is C.
The error is expressed in units of one terminal-query price t; monetary gap <=25*t/28538.
The six rational grid-gap bounds from left to right are
5/8798, 25/87642, 25/28876, 25/28538, 25/85276, 1/1692.

## Next scientific dependency

Test whether v(lambda,x)=min(A,B,C) exactly on the remaining interior low-prior corridor 0<lambda<155/1847, 1<x<3; either prove full coverage with a parametric Bellman lower envelope in (x,lambda,x*lambda) or give an explicit native tree and exact rational strictly improving witness. Current theorem and checks are author-derived with independent implementation, not externally reviewed or formally admitted.
