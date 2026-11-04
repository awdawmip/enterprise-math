# Stage441-B — exact future quotient for two moving nonadjacent X6 defects

Date 2026-11-05; AUTHOR_SIDE_PROOF / EXACT_FINITE_EXECUTED; UNREVIEWED / NOT_ADMITTED.
Parent Stage440-B commit 0effc40db7eba9707afb316e0d04943ffd85fe86; Draft PR #1736.
Frozen science: GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current behavioral rules loaded independently. Model is static ordered native-X6 paths; A=+E1, B=-E1 for initial letters; future APPEND uses all twelve signed directions. K is an exact positive-unit position-match count.

## Full initial-observation fiber F(L,h)

For every integer L>=7, P,Q each have length L, exactly two interior nonadjacent B defects, with all remaining directions A. Both endpoint vectors equal (L-4)E1, and directed edge histograms have J(A,B)=2, J(B,A)=2, J(A,A)=L-5 and all other counts zero. These endpoint/J restrictions define the entire binary two-defect family as a single-source fiber. Let h=|B_positions(P) intersection B_positions(Q)| in {0,1,2}. The match observable is K=L-4+2h. Thus F(L,h) is exactly the complete current O=(lengths, six-dimensional endpoints, J_P,J_Q,K) fiber. Both paths allow one arbitrary native-direction APPEND each, and respectively (pP,pQ)=(1,1) or (2,1) POP budgets. Legal POP/APPEND operations can interleave freely, and all prefixes are observed.

## Theorem 441.1 (complete future equivalence)

For POP budgets (1,1), the precise future equivalence key in F(L,h) is R11=(P[L-1]==B,Q[L-1]==B).
For POP budgets (2,1), it is R21=(P[L-2]==B,P[L-1]==B,Q[L-1]==B).
Indices are one-based. Two original histories have identical complete observation at every prefix of every common legal labelled operation word if and only if their respective keys coincide.

Proof: Each original P_L and Q_L is A. The signed last direction of a nonempty word X is recoverable from the observed endpoint V_X and directed edge counts by vec(X_last)=V_X - sum_(u,v) J_X(u,v)*vec(u). All 12 native signed direction vectors are distinct. Hence POP once from either source exposes its original L-1 direction; POP twice from P exposes its original L-2 direction. These operations prove necessity of all listed key bits.

For sufficiency, every legal trajectory has a surviving original prefix followed by an explicit sequence of appended letters, some of which may subsequently be removed. Because pP<=2 and pQ<=1, original positions 1..L-2 of BOTH sources always persist. The aggregate K contribution of these permanent original-original matches is K_initial minus the match bits at L-1 and L, which the key fixes (both last letters are A). All aligned positions beyond L-2 are either original-original (known at L-1 and L), original-appended (the only relevant original unmodified letter is P[L-1] or Q[L-1], fixed by key, or original L=A), or appended-appended (known action labels). The last-removable letters are also fixed by key, allowing exact updating of each own-source vector, J and length under POP and APPEND. Thus all complete prefix observations coincide. The proof covers arbitrary legal interleavings, including APPEND before POP.

## Theorem 441.2 (exact quotient counts for every L>=7)

The following are precisely the possible key strings, ordered lexicographically.

| overlap h | K | R11 support | q11 | R21 support | q21 |
|---:|---:|---|---:|---|---:|
| 0 | L-4 | 00,01,10 | 3 | 000,001,010,100,101 | 5 |
| 1 | L-2 | 00,01,10,11 | 4 | 000,001,010,011,100,101 | 6 |
| 2 | L | 00,11 | 2 | 000,011,100 | 3 |

Necessity of the support restrictions follows from nonadjacency of P[L-2],P[L-1], absence of same-position B when h=0, and P=Q when h=2. For every listed R21 key the following concrete L=7 defect-position pairs Pset/Qset supply existence (concatenate two single-digit positions in each set):
h=0: 000 24/35; 001 24/36; 010 26/35; 100 35/24; 101 25/36.
h=1: 000 24/25; 001 24/26; 010 26/24; 011 26/36; 100 25/24; 101 25/26.
h=2: 000 24/24; 011 26/26; 100 25/25.
For L>7 insert L-7 A letters after the first A in both paths; all B indices shift, preserving overlap, nonadjacency and each right-tail key. Projecting R21 to R11 yields all claimed R11 cases. Hence the formulas hold at all L>=7, and increasing P's POP budget strictly splits classes at each h. Optimal fixed-width future-class bits change 2->3 (h=0), 2->3 (h=1), 1->2 (h=2).

Explicit newly exposed distinction: at L=7 and h=1 compare left (P defects {2,4}, Q defects {2,5}) against right (P defects {2,5}, Q defects {2,4}). They share full current O and R11=00. P:POP;P:POP yields different P terminal directions at position 5 (A vs B), so R21=000 and R21=100 separate.

## Theorem 441.3 (exact population and codebook-free ranking)

For a valid key R define a nonnegative-integer transfer over interior positions t=2,...,L-1. State (i,j,z,u,v) contains counts i,j of defects in P,Q, coincidence count z, and previous-position defect bits u,v. Initialize (0,0,0,0,0) with count 1. For each (x,y) in {0,1}² satisfying u*x=v*y=0, i+x<=2, j+y<=2, z+xy<=h, and the key's visible bits at t, add its count to next state (i+x,j+y,z+xy,x,y). Sum terminal weights with i=j=2,z=h to obtain exact M(R).

Proof: each admissible raw ordered pair determines precisely one path of (x,y) choices, with the transfer constraints exactly enforcing nonadjacency, two defects each, overlap h and fixed visible key. Conversely each accepted transfer path determines one admissible history pair. Thus M(R) is exact; sum_R M(R)=|F(L,h)|. All listed support classes have positive M by the L=7 witnesses.

Class rank/unrank is direct lexicographic indexing of the support list with at most six entries, without enumerating original histories or building a length-dependent codebook. For lossless recovery of a specific raw history, separately save index z in [0,M(R)); use the transfer backward to count completions for each lexicographic (x,y) branch and skip counted branches to recover both original words. The inverse index sums earlier branch counts. This is an exact bijection between (class rank, within-class rank) and F.

There are at most 3*3*3*2*2=108 transfer states per position and four transitions per state. Total ordered histories are at most binom(L-3,2)^2=O(L^4); each transfer count therefore has O(log L) integer bits. Raw input conversion and complete O construction cost O(L) primitive operations. The class label/q cost O(1) integer operations after the input is known; M(R) costs O(L) exact-integer additions on O(log L)-bit values using O(1) rolling DP states; within-class rank/unrank costs O(L) such operations and O(L) states for backward DP, plus Theta(L) output. These resource statements include input conversion and output recovery.

At L=10, h=1, K=8 there are exactly 180 original ordered pairs. Pop (1,1) has 4 classes with masses (100,25,25,30); pop (2,1) has 6 classes with masses (64,20,25,30,36,5). Both mass lists sum to 180.

## Actual exact verification

Python stdlib arbitrary integers, command: python REPRO_STAGE441B.py. Exhaustive population/rank/unrank comparison on L=7..15, h=0,1,2 and both POP budgets: 54 parameter combinations, 24,576 original ordered pairs, 207 class population checks and 24,576 within-class rank/unrank checks. Independently for all six complete L=7 fibers, compare all native six-vector endpoints, all 12x12 directed J counts, K and length at every legal POP/APPEND-prefix with all twelve future APPEND directions: 49 equivalent within-class tests, 38 different-class separation tests, 119,300 observation-prefix comparisons; PASS marker STAGE441B_DOUBLE_DEFECT_TRANSFER_AND_QUOTIENT_PASS. Finite domains are declared; the universal L>=7 claim rests on the above proof. Source and evidence: REPRO_STAGE441B.py / REPRO_STAGE441B_EXECUTED.json.

This is author-side evidence pending independent Driver review. The native P000 ontology and frozen science remain unchanged.

## Stage442-B next question

General kP,kQ nonadjacent defects, arbitrary unequal lengths and POP/APPEND budgets. Construct implicit support determinization and class rank/unrank with exact integer populations; quantify parameterized automaton state cost and full input/output costs. Test (L,kP,kQ,pP,pQ,rP,rQ)=(8,2,1,2,1,1,1) against all twelve future labels and exact full-O brute partition. Preserve formal owner/claim authority and immutable scientific pins.
