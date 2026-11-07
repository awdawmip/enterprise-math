# Stage485-B — Variable shared prefix and unrestricted finite Q-APPEND budget

2026-11-07. Research2 author-side mathematical argument, local exact-integer execution; UNREVIEWED / NOT_ADMITTED.

## Frozen provenance and model

Parent Stage484-B: PR #1736, commit `c6ebfa16ca2d18ab49f5af32b39527f9074a7816`; scientific frozen global `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current conduct rules read separately: GLOBAL main@`d0ce1defdb34f5c9323b5668ae5f0705c780e315` and EM main@`2b7c3d19f3e1301ec3b787dd304181731ed3d964`.

Native spatial substrate is six-axis signed X6 (chart-relative affine torsor over Z^6). The original and appended directions belong to `D={+E1,...,+E6,-E1,...,-E6}` (12 signed directions; not 12 dimensions). Time, when needed, is separate. A direction word is a provenance-retaining ordered primitive path, not a final Cell address. Let A=+E1, m=2k+2, k,u>=1, `P=T`, `Q=T W A H A`, with T length m, W length k, H length u. Compare history pairs **within the same complete initial-observation fiber**, where the observer consists of lengths, both signed six-dimensional displacements, both complete directed 144-edge multiplicity vectors and the positional equality count K. Total operation budgets are `P_POP<=k`, `P_APPEND<=k`, `Q_POP<=h`, `Q_APPEND<=a`; appended directions may be any of D, operations interleave arbitrarily, POP requires length>1. Future equivalence means equality of observers after every prefix of every common legal action word.

## Theorem 485.1 — Fixed known T: any finite Q APPEND budget

For any h,a>=0 and `r=min(h,u)`, the exact future key remains

`R_fixed=(W,suffix_r(H))`.

**Proof.** If W differs, append W of the first history to both P paths (k steps, no POP); the new positional matches with Q differ. If retained H suffix differs, POP Q repeatedly, through at most r steps, until the first differing original ordered edge is removed; the full Q adjacency vectors then differ. Neither witness needs Q APPEND. Conversely, at most h original Q letters can be removed by h POP operations, even with arbitrary known APPEND/POP interleavings. When h<=u, all original deletions lie in the known final A and suffix_h(H) boundary, and the Q original prefix T W survives at length >=m+k+2. P never grows beyond m+k, so all comparisons K involve only known T W and action arguments. Q adjacency, displacement and lengths update from the same initial observation and known removed/added edges. If h>u, the key includes all H and the initial Q is completely specified. Thus observers agree for every legal future. QED.

## Theorem 485.2 — T variable within an initial-observation fiber, h<=u

For any a>=0 and 0<=h<=u, the exact future key is

`R_variable=(sigma,W,S)`, where `sigma=suffix_(k+1)(T)`, `S=suffix_h(H)`.

**Proof of sufficiency.** P can delete at most k original letters; all k possible deleted P edges, including their left endpoints, are specified by the last k+1 symbols sigma. Each later P APPEND or POP acts on this known boundary or on known appended letters. Likewise, Q can delete at most h original H letters and the final A, so its edge/displacement changes are determined by S and common operations. Throughout these operations Q retains its own original prefix T W and length >=m+k+2, while P length <=m+k. For K, every unmodified original prefix position of P matches the corresponding original Q prefix in *each* history; any appended P letter aligns with the last k original T positions or W, which are specified by sigma and W. Consequently all observable quantities agree.

**Proof of necessity.** Unequal W is distinguished by appending k letters W of the first history to P; the first history gains k matches and the second fewer. Unequal S is distinguished by up to h consecutive Q POPs and the first different deleted directed edge. Unequal sigma is distinguished by at most k consecutive P POPs: equality of all k deleted ordered P edges, `(T_(m-1),T_m),...,(T_(m-k),T_(m-k+1))`, would determine exactly the last k+1 letters. Hence a different sigma yields a differing observed adjacency vector after some POP prefix. QED.

**Boundary witness.** Set k=1,u=2,h=0, P1=AABA,P2=ABAA, W=A,H=AA and Q_i=T_i W A H A. Both initial complete observers agree; `(W,suffix_0(H))` agrees, but `sigma_1=BA` and `sigma_2=AA`. One P_POP deletes B->A in the first history and A->A in the second. A nontrivial same-key pair is k=2,u=2,h=0, T1=AABAAA,T2=ABAAAA,W=AB,H=AB: initial complete observers and sigma=AAA agree; all 73,947 synchronously explored paired future states under two Q APPENDs agree.

## Theorem 485.3 — Exact positive Euler–BRC raw populations

Let `ThetaP=E(P)`, `ThetaQ=E(Q)`, with E(word) its directed edge multiset. The initial signed P displacement `DeltaP` determines its first direction s through

`v(s) = DeltaP - sum_(x,y) ThetaP(x,y) v(y)`

because indegrees count all word letters except the first and `v:D-> {+-e_i}` is injective.

Let `N(L,s,t,e)` count length-L words with first s, last t, exact edge multiplicities e, using **integer counts of words** (indistinguishable repeated edge instances). Then `N(1,s,t,0)=[s=t]` and
`N(L,s,t,e)=sum_(v:e(s,v)>0) N(L-1,v,t,e-1_(s,v))`.
This is an exact finite integer dynamic program, equivalent to a directed Euler-word count.

For a key `(sigma,W,S)` with r=h<=u set
`P_rem=ThetaP-E(sigma)`,
`R=ThetaQ-ThetaP-[sigma_last->W_1]-E(W)-[W_k->A]`.
Negative residual => zero population. Otherwise

`M(sigma,W,S)=N(m-k,s,sigma_1,P_rem) * G_r(R,S)`,

where `G_0(R,empty)=N(u+2,A,A,R)` and, for r>=1,
`G_r(R,S)=N(u-r+2,A,S_1,R-E(SA))` when the residual is nonnegative.

**Proof.** Any T with suffix sigma uniquely decomposes as an overlapping prefix U of length m-k ending sigma_1 followed by sigma_2...sigma_(k+1). Its prefix U has exactly P_rem edges. Given sigma and W, Q edges split as `ThetaP + [T_last->W_1]+E(W)+[W_k->A]+E(A H A)`. The H completion starts A and joins the fixed suffix S through S_1, so has precisely the stated residual Euler count. Choices of T-prefix and H-prefix are independent and counted with positive integer multiplicity; multiply. Summing `[M>0]` over keys counts future classes, and summing M recovers raw history population. QED.

## Actual finite numerical evidence

Executed full local Python 3 standard-library verifier using exact integers. Original words range over `{A=+E1,B=+E2,G=-E1}`, T length 4, W length 1, H length 2: exactly 3^7=2,187 raw pairs partitioned into 1,350 complete-observation fibers. All M populations checked exhaustively for h=0,1,2: class counts respectively **1,701; 2,187; 2,187** and same numbers of exact key-population checks; each h recovers 2,187 histories. Each initial fiber contains at most 8 histories. In the h=0 case maximum class population is 2; for h=1,2 it is 1. Across each h, 306 same-fiber pairs have distinct T and distinct keys.

Separately a synchronous paired-future explorer permits all 12 signed APPEND directions, Q APPEND budget 2, and all legal interleavings. It checked 28 unequal-key pairs plus three distinct-history equal-key pairs, with **86,339 visited paired states**; all equivalence assertions passed. The equal-key traversals visited 4,082 (fixed T,h=0), 8,164 (fixed T,h=1) and 73,947 (variable T,k=2,h=0). This finite scope supports the worked examples; the all-parameter statements follow from the proofs.

## Continuing question: Stage486-B

For variable T, extend the key beyond h=u as Q POP crosses the separator A, W and eventually the original T. Characterize the exact merged P/Q-visible suffix and derive an Euler–BRC count for h=u+1,..,u+k+3; begin with k=1,u=2 and all 12 future APPEND directions. Independently measure bit complexity, type enumeration and rank/unrank cost as k,u and the sparse active directed-edge count grow. Preserve frozen scientific inputs, P000, Source role/owner conditions and independent Driver review.

**Research status:** Author-side proved derivation and local finite exact execution; native session FAILED/OSError; owner query WAITING_RESOURCE/EVENT_COLLECTION_IO; no CLAIM or Native Result; independent Driver review pending.
