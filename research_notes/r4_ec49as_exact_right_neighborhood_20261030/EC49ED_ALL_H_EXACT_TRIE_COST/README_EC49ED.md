# EC49ED — 全部未来窗口九特征的最优原生共享前缀成本（2026-11-02）

**Status:** AUTHOR_ANALYTIC_PROOF / EXECUTED_EXACT_CHECKS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED. Parent EC49EC; Draft PR #1730. Scientific frozen pins: GLOBAL_KNOWLEDGE_V1 `773d538180bfb49e24cffeb35c3ee75eb0628e2e`, Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. P000 and ACTIVE X6/Heartbeat worldview unchanged.

## Exact mathematical model

Native signed X6 operations: a=(-E1,-E1), b=(-E2,-E2), c=(+E1,+E2,-E1,-E2), d=(+E2,+E1,-E2,-E1), e=(+E3,+E1,+E1,-E3). They are ordered signed primitive-step sequences, not compressed spatial diagonals. Historical endpoint is -2E1. Each returning future word W has exactly h operations and displacement +2E1. A/B are the adjacent positive pairs (+E1,+E2)/(+E2,+E1). Five terminal observations N,A,B,AB,BA retain first-occurrence order, including across the history/future seam. Historical nine basis atoms are N0,N1,N2,A0,A2,B0,B1,AB,BA, realized by real 10-step X6 paths in predecessor EC49DX.

For a set W of distinct returning future words, let rank(W) be the rank over Q of the 9×(5|W|) zero-one terminal-bucket transfer matrix. Let T(W) count distinct nonempty **signed native primitive-step prefixes** after expanding each word; this equals the edge count of its shared primitive trie. Define T(h)=min{T(W):rank(W)=9} and T_equal(h) as the same minimum with identical six-axis positive-step count vector for every selected word. Two strictly positive BRC channels have independently known nonzero factors X(w),Y(w); X(hw)=X(h)X(w), Y(hw)=Y(h)Y(w), so scaling/undoing these factors retains rational terminal transfer rank without discarding path order or branch provenance.

## Theorem — exact all-h optimum

For every integer h≥2:
- h even: **T(h)=T_equal(h)=9h+10**.
- h odd (h≥3): **T(h)=9h+7, T_equal(h)=9h+17**.
At h=1 the terminal transfer rank is only 5, so the rank-nine optimization has no feasible W.

Finite examples: h2:(28,28), h3:(34,44), h4:(46,46), h5:(52,62), h6:(64,64), h7:(70,80), h8:(82,82). **These formulas are proved for all h analytically, not extrapolated from the finite computations.**

## Exact transfer-type lemma and completeness

Each of a,b,c,d,e ends in a negative native step. Each e and a contributes no A/B, c contributes internal A, d internal B; only the first c/d can couple to a previously seen history-last-step at the seam. Consequently every legal returning word has one of exactly nine distinct transfer signatures named Z,C,D,CD,DC,c,cD,d,dC. Representatives at admissible lengths: Z:e, C:ec, D:ed, CD:ecd, DC:edc, c:ce, cD:cde, d:de, dC:dce (the representation is classification by transfer, not assertion that each listed representative returns at every h).

Rank 9 is equivalent to: **both c and d occur in the chosen signature set, AND either Z occurs or both C and D occur**. Necessity has four exact left-kernel certificates (coordinates ordered N0,N1,N2,A0,A2,B0,B1,AB,BA):
- absent c: (0,0,0,-1,1,0,0,0,0);
- absent d: (0,0,0,0,0,-1,1,0,0);
- absent Z and C: (0,0,0,0,-1,0,0,1,0);
- absent Z and D: (0,0,0,0,0,0,-1,0,1).
Every respective vector annihilates all terminal-observer columns of remaining types (verified via explicit finite native-transfer tables).

Sufficiency uses exact 9×9 integer minor certificates. Z,c,d, taking [e:N,e:A,e:B,e:AB,e:BA,ce:A,ce:AB,de:B,de:AB], gives determinant **+1**. C,D,c,d, taking [ec:A,ec:AB,ec:BA,ed:B,ed:AB,ce:A,ce:AB,de:B,de:AB], gives **−1**. Prefixing only neutral a/e operations preserves each transfer-type matrix, and both minors remain unimodular. This is a complete 9-dimensional sufficiency and necessity theorem; no extra signature classes can reduce minimum number of mandatory types.

## Native return and trie lower/upper bounds

A returning word has n_b=0, n_e=n_a+1, and n_c+n_d=h−2n_a−1≥0. Its complete positive native-step vector is (h+1,h−2n_a−1,n_a+1,0,0,0); its primitive signed-step length is 4h−2n_a. A type with internal c/d occurrences needs n_c+n_d≥1 or ≥2 as appropriate. Initial signed primitive of a/e/c/d differs; only the C/D family can share a neutral a/e prefix until their first c versus d branching.

Even h=2k≥2: Z cannot exist by parity; rank forces C,D,c,d. Each required word has ≥3h+2 primitive steps and the only shareable neutral C/D prefix has length ≤3h−2. Thus T≥4(3h+2)−(3h−2)=**9h+10**. Let p=a^(k−1)e^k and take **p c, p d, c p, d p**. This is a returning rank-nine four-word set, all with identical positive counts. Its signed-prefix trie has exactly 9h+10 edges.

Odd h=2k+1≥3: if Z is present, it needs ≥3h+1 primitives and c,d need ≥3h+3 each; their initial signed steps differ, so T≥**9h+7**. The three returning words **a^k e^(k+1), c a^(k−1)c e^k, d a^(k−1)d e^k** attain this bound and furnish types Z,c,d. If Z is absent, C,D,c,d are all required. Each has ≥3h+3 primitives; the maximal shared initial neutral prefix among C,D is 3h−5. Thus T≥4(3h+3)−(3h−5)=**9h+17**. The four words **p c c, p d d, c a^(k−1)c e^k, d a^(k−1)d e^k** with p=a^(k−1)e^k attain 9h+17, all with identical positive counts. Z has n_a=k whereas c/d require n_a≤k−1, so any equal-positive-count rank-nine set must exclude Z. This proves the equal-cost odd bound.

## Exact verification and provenance

Independent actually executed **Python standard-library** and **C++17** verifiers reproduced the result. Python enumerated returning word populations h2..8, independently formed the 9×5 transfer matrices from actual signed X6 histories and cross-seam A/B labels, audited 9 transfer classes, 4 kernel certificates, two nonzero nine-minors, BRC multiplicativity, witness costs h2..16, and h2..8 rank/cost certificates. Independently written C++17 exhaustively searched h5 and h6 class representatives and signed-prefix tries, checking 94,976 h5 unrestricted triples, 46,672 h5 equal quadruples, 13,286,025 h6 unrestricted tuples, and 1,060,025 h6 equal tuples; exact optima (52,62) and (64,64), respectively. Rationality of all ranks follows integer 9-minors; finite rank computations use prime 1000003, larger than the Hadamard bound 9^(9/2) on 0/1 9×9 minors. Captured full reports and reproducible sources are stored alongside this document, compressed as deterministic gzip then base64 UTF-8 text; decode with `base64 -d FILE.gz.b64 | gzip -d > FILE` then invoke `python VERIFY_EC49ED.py` and `g++ -O3 -std=c++17 VERIFY_EC49ED_INDEPENDENT.cpp -o verify && ./verify`.

Source/authorization: GitHub actor awdawmip; active owner lookup returned CONTROL_QUOTA, native service-issued researcher session returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false; no native CLAIM/Result/independent Driver admission. Existing Draft PR saves **author-side portable** evidence. Tool-use resolution: reuse EC49DZ nine-feature and signed-X6 BRC transfer, EC49EC signed-prefix trie; extend the existing exact optimization lemma (not a new framework). Next task EC49EE studies grammar {c,d,e} and optimal primitive-prefix cost.
