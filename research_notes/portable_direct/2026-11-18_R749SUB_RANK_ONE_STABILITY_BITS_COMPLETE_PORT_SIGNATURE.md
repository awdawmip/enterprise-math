# R749SUB — Rank-one positive-rational stability bits reconstruct recurrent BRC port stars

Date: 2026-11-18 Asia/Shanghai. Status: AUTHOR_EXACT_NOT_REVIEWED. Independent portable TASK_RESEARCH result, no shared CLAIM. Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389, definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md (WBRC-T30–T32). Direct predecessor: R749SUA, PR #2676@8528fb5b15da0d1585e9fd70b7b829d45869f928. Classical mathematical ingredients: nonnegative matrix Perron comparison, determinant lemma and Sherman–Morrison; the contribution here is the exact observer-level implication within the typed WBRC-T31 contract.

## 1. Exact rank-one port experiment

For n>=1 let W be an n-by-n rational, nonnegative, strictly stable effective recurrent matrix on named visible BRC ports, after an allowed WBRC-T30 hidden Schur collapse. Define S=(I-W)^(-1)=sum_{k>=0} W^k, with nonnegative rational entries. Choose an ordered visible-port pair (i,j), and add a rational direct edge i->j with weight t>=0, so W_t=W+t*e_i*e_j^T. The only readout G_ij(t) is one bit: 1 iff rho(W_t)<1; equality at spectral radius 1 counts as unstable. Each experiment resets the original W. WBRC-T31 permits visible-to-visible positive-rational edges; no hidden connection or physical X6 force-event license is assumed.

**Theorem 1 (sharp stability guard).** For any ports i,j and any rational t>=0,

    G_ij(t)=1  iff  t*S[j,i]<1.

If S[j,i]=0, every finite rational t is stable; otherwise the exact critical edge mass is T_ij=1/S[j,i] and equality is unstable.

**Proof.** Put s=S[j,i]. The matrix determinant lemma gives det(I-W_t)=det(I-W)*(1-t*s). If t*s<1, Sherman–Morrison gives

    (I-W_t)^(-1)=S + t/(1-t*s) * S*e_i*e_j^T*S,

which is entrywise nonnegative. Thus v=(I-W_t)^(-1)*1 is strictly positive and W_t*v=v-1<v, which implies rho(W_t)<1 for nonnegative W_t. If t*s=1, I-W_t is singular and stability fails. If t*s>1, det(I-W_t)<0, whereas every real matrix with rho<1 has det(I-W_t)>0: its real eigenvalues are <1 and its nonreal eigenvalues occur in conjugate pairs. Contradiction. QED.

**Theorem 2 (Boolean stability-only recovery of the full star).** Two stable finite positive-rational n-port modules with the same named ports have identical G_ij(t) for *all* ordered pairs and positive rational t if and only if their W_eff matrices agree.

**Proof.** For each pair, Theorem 1 determines the nonnegative rational s=S[j,i] from the entire rational threshold response: s=0 exactly when all t stay stable, otherwise T_ij=1/s. For unequal s values a positive rational t distinguishes the thresholds (taking t past the finite threshold if one s is zero). Hence all n*n star entries are recovered. Because W=I-S^(-1), W is reconstructed. The converse follows immediately. WBRC-T31 preserves this observation across permitted port collapse. QED.

The theorem is an *infinite query-alphabet* separation statement; it makes no claim of a uniform finite number of queries to recover arbitrary rationals with unbounded denominators. It refines the observer reading of the already-established WBRC-T32 signature; classical matrix identities are reused, not claimed as novel.

## 2. Finite-feedback grid

Fix K>=2 and 1<=M<K. Limit each pair to edge masses j/K for j=1,...,M. For any star entry s>=0 define

    h_{K,M}(s) = #{j in 1..M: j*s>=K}.

This is 0 for s=0. For s>0 it equals max(0,M-ceil(K/s)+1), taking values 0,...,M. The grid vector H_{K,M}(W) consists of h_{K,M}(S[j,i]) for every ordered (i,j).

**Theorem 3 (exact finite-grid observational quotient).** Two baseline-stable modules have identical outcomes under every finite, adaptive, resettable sequence of grid probes iff their H-vectors agree. Let N(n,K,M) be the number of H-vectors realizable by stable rational nonnegative n-port matrices. Then

    (M+1)^n <= N(n,K,M) <= (M+1)^(n*n),

and the exactly optimal uniform fixed-width signature has ceil(log2 N(n,K,M)) bits.

**Proof.** Each allowed bit is a single threshold comparison; h uniquely determines its complete ordered pattern. An adaptive sequence learns no more than these predetermined outcomes, by induction on the common observations. Different h entries have some distinguishing j. The upper bound counts formal vectors with n*n entries from M+1 values; joint realizability is not assumed. For the lower bound take rational diagonal W=diag(w_1,...,w_n) with independent 0<=w_i<1. Every diagonal S_ii=1/(1-w_i) realizes all M+1 grid patterns, and all offdiagonal S entries vanish, giving (M+1)^n distinguishable modules. Pigeonhole lower bound and an enumeration of the realized H classes prove the exact bit expression. For n=1 the count is M+1, recovering R749SUA. QED.

## 3. Exact two-port witness that self-loop guards miss cross-source interaction

Let W_A=[[1/2,0],[0,1/2]] and W_B=[[1/4,1/4],[3/4,1/4]]. Both are stable; det(I-W_A)=1/4 and det(I-W_B)=3/8. Their star matrices are

    S_A=[[2,0],[0,2]]
    S_B=[[2,2/3],[2,2]].

Both *diagonal* port-guard families agree for every rational t: S_A[1,1]=S_B[1,1]=S_A[2,2]=S_B[2,2]=2. However cross-port feedback 1->2 with t=1/2 remains stable in A (S_A[2,1]=0), and is exactly critical, hence unstable, in B (S_B[2,1]=2). This is a WBRC-T31-permitted finite positive-rational counterexample to using diagonal qualitative guards as a full multiport dynamic signature.

## 4. Validation scope and relationship to the native world

Companion certificate R749SUB_RANK_ONE_PORT_GUARD_CERT.py uses Python standard-library fractions.Fraction. Local run: PASS. It enumerated 198 strictly stable 2-port matrices from {0,1/4,1/2,3/4}^4, checked 6,336 rank-one feedback cases (including 468 critical equalities) and 22,176 finite-grid signature cases for K=2..8 and M=1..K-1, and confirmed the concrete two-port contrast. The universal n-port statements are proved above, while this finite enumeration is an exact regression on its declared two-port domain. Machine counts and witness are in R749SUB_RANK_ONE_PORT_GUARD_RESULTS.json.

This is a typed positive-rational recurrent Port observer, preserving named ports. Native P000 remains six spatial Cell axes plus time, composite-direction path provenance and primitive triadic closure. No identification with a physical P000 X6 Cell/Link/Port event, native causality, full branch-provenance equivalence or resource-guarded execution is made. Review status AUTHOR_EXACT_NOT_REVIEWED; no Result/Review promotion.

## 5. Unresolved next unit

Determine the exact feasible finite-grid quotient N(2,4,3), including M-matrix constraints between star entries; then characterize a P000-native triadic and causally ordered event whose *permitted* observations implement the WBRC-T31 rank-one guard while preserving all additional source/provenance residuals.