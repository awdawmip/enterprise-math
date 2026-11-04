# Stage439-B — Exact unrestricted two-sided X6 POP/APPEND future quotient

Date 2026-11-05. Status: AUTHOR_SIDE_PROOF / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED. Parent: Stage438-B commit 26b3cbfbce897dd5e801ab2fc86662195884e80a; earlier Stage437-B commit e098cfb9417d3df15c89da6843dd4d110917d67a; Draft PR #1736. Frozen science: GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53, EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419, original P000 V5 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current behavioral rules are independently read from canonical main. This is a static 12-signed-direction X6 ordered-path observer, with positive unit match counts, not an asserted physical heartbeat evolution or signed-amplitude BRC cancellation.

## Exact problem

Let D={±E1,...,±E6}; initial ordered words P∈D^m, Q∈D^n. Define the complete observed state
O=(m,n,V_P,V_Q,J_P,J_Q,K), with V_X=sum vec(X_i), J_X(a,b)=#{i:X_i=a, X_(i+1)=b}, K=sum_(i=1)^min(m,n)[P_i=Q_i].
Both sources independently allow at most p_P,p_Q POPs and r_P,r_Q APPEND(d) steps (all d∈D) in any legal interleaving; all operation prefixes are observable. Assume 0≤p_P<m, 0≤p_Q<n, r_P,r_Q≥0; both words remain nonempty. All indices below are 1-based inclusive.

## Theorem 439.1 — Exact full-future equivalence without protected overlap

Put c=min(m-p_P,n-p_Q), t=min(m,n). Define the own-source removal suffixes
S_P=(P_(m-p_P),...,P_m), S_Q=(Q_(n-p_Q),...,Q_n).
When r_Q≥1 define A_P={(i,P_i):n-p_Q+1≤i≤min(m,n+r_Q)}; otherwise A_P=∅.
When r_P≥1 define A_Q={(i,Q_i):m-p_P+1≤i≤min(n,m+r_P)}; otherwise A_Q=∅.
Define the mutable-original-overlap match bits B=([P_i=Q_i])_(i=c+1,...,t).
The repair key is R=(S_P,S_Q,A_P,A_Q,B), with lengths and budgets fixed by the comparison.

For any two histories in the SAME present complete-O fiber, their entire observed traces agree for EVERY budget-respecting labelled finite operation word if and only if their R keys agree. This holds for arbitrary initial length difference and **does not assume** m-p_P≥n+r_Q or the reverse. Consequently, for a finite current-O fiber F, the exact number of future classes is q_F=|{R(P,Q):(P,Q)∈F}|; its optimal fixed-width class label requires ceil(log2 q_F) bits once an encoding table exists. R itself is a sufficient raw carrier of the exact partition and may have redundant fields; the bit minimum is for class labels, not necessarily for the unoptimized R tuple.

### Proof of necessity

For each nonempty X, V_X−sum_(a,b)J_X(a,b)vec(a)=vec(X_last), since every direction except the last is the first endpoint of exactly one adjacent pair. The twelve signed unit directions have distinct native vectors. Along source-only POP prefixes of lengths 0 through p_X, this reconstructs its original final p_X+1 directions, so S_P and S_Q are uniquely forced.

If (i,P_i)∈A_P, leave P unchanged. For i≤n, POP Q exactly n-i+1≤p_Q times, then APPEND(d) at index i; for i>n, APPEND Q exactly i-n≤r_Q times, choosing d for the last letter. Because i≤m, the K increment on that final APPEND equals [P_i=d]. Varying d through all twelve native directions identifies P_i. The identical argument with sources interchanged identifies every Q_i in A_Q.

For any c<i≤t, at least one original source X can legally POP through index i (because |X|−p_X<i). Leave its counterpart unmodified and POP X down to length i−1. At the specific i→i−1 step, K changes by −[P_i=Q_i]; the counterpart has original index i because i≤t. Thus all mutable original match bits are determined by the complete future observations. Every component of R is necessary for exact trace equality.

### Proof of sufficiency

Under total POP budget p_X, every future X is a surviving original prefix of length at least |X|−p_X followed by an explicit current stack of APPEND letters. POP removes stack letters before original letters. The known last p_X+1 original directions and initial V_X,J_X suffice to update all own-source V,J observations and lengths by a constant number of integer operations per POP/APPEND. All legal action words and live append stacks are common/known.

At every index i≤c both original letters persist forever, so their constant aggregate matching count equals K_0−sum_(i=c+1)^t B_i. For any later current aligned index i>c: if both letters are still original, use B_i (necessarily i≤t). If both letters are appended, their values are in the action stacks. If only source X's letter is appended, i belongs to the reachable rewrite interval [|X|−p_X+1, |X|+r_X], and the other source's original indexed direction is exactly in A_Q or A_P. Thus the equality bit at every current aligned position is determined by O_0, R and the common operation word. Sum to recover K, as well as V,J and legality, at every prefix. This proves sufficiency and the theorem.

### Complexity / coding scope

|S_P|+|S_Q|=p_P+p_Q+2, |A_P|≤p_Q+r_Q, |A_Q|≤p_P+r_P, |B|=t−c≤max(p_P,p_Q). The unreduced key has at most 2(p_P+p_Q)+max(p_P,p_Q)+r_P+r_Q+2 direction/bit slots, hence ≤3(p_P+p_Q)+r_P+r_Q+2, independent of m,n for fixed budgets. Parsing raw words and computing O,R costs O(m+n) word operations. Future observation updates use O(1) label comparisons and constant-many integers of O(log(m+n+budgets)) bits per operation. Building an optimal class rank/unrank table for an arbitrary implicit fiber is an additional task; no universal polynomial-time ranking is claimed. Given an explicitly enumerated fiber of size N, direct tallying/class population and ranking has O(N(m+n)) input processing plus key sorting/hash construction, O(N|R|) naive storage. To recover a particular original history, retain a separate within-class index; class compression only preserves the specified future observer.

## Theorem 439.2 — Strict failure of the formerly protected key without its hypothesis

Let A=+E1, B=−E1, C=+E2, P=C^4, Q(j)=A^(j−1) B A^(8−j) for j=2,3,4,5,6,7. Set (m,n)=(4,8) and (p_P,r_P,p_Q,r_Q)=(1,1,1,1). Exactly these six pairs constitute the full current-O fiber: the endpoint/J of P force CCCC; the endpoint/J of Q force one interior B with the remaining seven A; K=0 for all. The protected-only Stage438 key R+=(S_P,S_Q,P_(n-p_Q+1)..P_(n+r_Q)) yields just two classes (j=7 versus the rest), since its P interval is empty here.

Yet P:POP then P:APPEND(B) rewrites position 4, producing final K=1 for j=4 and K=0 for j=2; P:APPEND(B) writes position 5 and yields K=1 for j=5 versus K=0 for j=2. Q's own suffix observations distinguish j=7. The unrestricted key retains Q_4,Q_5,Q_7,Q_8 and precisely yields four classes with integer populations (3,1,1,1): {2,3,6}, {4}, {5}, {7}. The sharp class code is therefore 2 bits. The 3-element class needs a separate within-class index if lossless original word reconstruction is requested.

## Reproduction and scope

Execute Python 3 stdlib-only REPRO_STAGE439B.py; compare its exact one-line canonical JSON with REPRO_STAGE439B_EXECUTED.json. The script enumerates complete present-O fibers over the initial three native letters A,B,C, and for every pair within a common fiber independently recursively checks ALL legal operation words with ALL twelve signed APPEND letters and full O at EVERY prefix. It covers 11 declared parameter domains with initial lengths 3–5, 153,819 initial pairs, 25,368 intra-fiber pair comparisons (5,508 equivalent, 19,860 distinguishable), plus the full six-history counterexample fiber (15 pair checks). PASS means no detected disagreement in these exact finite domains; the arbitrary-parameter assertion rests on the proof, not finite enumeration. No actual heartbeat/phase experiment, signed BRC cancellation, or independent review was performed.

## Next unit

Stage440-B: compute implicit rank/unrank and exact integer class populations under the unrestricted two-sided repair for double-defect P,Q families, comparing budgets (1,1,1,1) and (2,1,1,1). Audit representation conversion, codebook, population and original-history recovery costs. Preserve frozen P000, native-source ownership and admission boundaries.
