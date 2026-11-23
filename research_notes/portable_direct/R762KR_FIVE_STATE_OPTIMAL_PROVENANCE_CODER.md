# R762KR — Five-state exact enumerative coding for M3 provenance fibers

Date: 2026-11-24 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_PYTHON_CHECKED / NOT_REVIEWED.

## Inheritance and declared scope

Direct continuation of R762KQ@cd700a5e4c15bb8b2cc322ded05ae80b4bb6a5a0, KN.1@2ca3fe1ff671a44a1ec4ed4cb90653870a7ddaf7, and the frozen P000 scientific input a72226e2430ffa4786321ac86e7f0c599d5f0389. This is the unsigned auxiliary composite Port–Euler M3 model, with inactive Ports 01,23,45, twelve active Port bits, eight lexicographically ordered supports (i,j,k) in {0,1}^3, and the same twelve positive forced-support incidences. Each support s of positive integer multiplicity m_s chooses an unordered multiset of three *typed* quotient edges AB, AC, BC. Its source is the triple c_s=(x_s,y_s,z_s) of nonnegative counts summing to m_s. Each edge type has the actual support-dependent boundary e_(s,a) in GF(2)^12. The permitted forced-parity boundary set F has 512 elements.

The goal is exact conditional source recovery when the observer retains m=(m_s), the forced boundary b in F and quotient connectivity, but has discarded the eight source triples. The code is an auxiliary BRC-compatible provenance carrier in the information-theoretic sense (a typed, lossless source ID), **not** an implementation of native signed BRC updates, timed TRIADIC_CLOSURE_E or a complete native three-dimensional slice.

## KR.1 — Exact local aggregation independent of the magnitude of m

Let U be the nonempty subset of edge families used at a single support, with h=|U|. Let p_a in {0,1} be each count's parity, with p_a=0 outside U. For a in U define l_a=1 if p_a=1 and l_a=2 if p_a=0, and put L=sum(l_a). The exact number of triples with this nonzero-family set and parity is

W_m(U,p) = binom((m-L)/2+h-1,h-1),

when m≥L and m-L is even, and zero otherwise.

Proof: any positive odd count equals 1+2t_a, and any positive even count equals 2+2t_a. Therefore sum t_a=(m-L)/2; stars and bars counts the solutions. Boundary is e_s(p)=XOR over a with p_a=1 of e_(s,a). Each nonempty U contributes either a singleton family or the already-connected category. Group equal pairs (e_s(p),category), retaining their integer coefficients. There are at most 4 boundary parity possibilities and 4 nonempty connectivity categories for each support, so at most 16 grouped transitions, independent of the numerical value of m_s. The full local weighted sum is binom(m_s+2,2).

## KR.2 — Exact five-state connectivity automaton

The forced supports internally connect the three four-Port components A,B,C. Quotient connectivity holds iff the flexible source uses at least two distinct edge families (AB, AC, BC). Thus track only five states: EMPTY, AB_ONLY, AC_ONLY, BC_ONLY, CONNECTED. CONNECTED is absorbing; adding a different family to a singleton enters CONNECTED. This is a sufficient automaton for any suffix of supports.

For the *abstract variable-length word language* on three quotient edge colors consisting of words containing at least two distinct colors, these five deterministic states are also minimal: EMPTY is distinguished from a singleton by appending one differently colored letter, different singleton colors are distinguished by appending one of those colors, and CONNECTED is distinguished by the empty suffix. The minimality statement concerns this universal color-stream language, not the combined 12-bit parity state under fixed input lengths.

## KR.3 — Exact count and optimal conditional rank/unrank

For a suffix beginning at support i, remaining GF(2) boundary r and incoming connectivity state q, define D_i(r,q) as the number of admissible suffix completions. Its terminal value is 1 iff i=8, r=0 and q=CONNECTED; otherwise zero. Let w_i(e,c) be the grouped local counts from KR.1, and q⋆c the five-state transition. Then

D_i(r,q) = SUM_(e,c) w_i(e,c) D_(i+1)(r XOR e, q⋆c).

This recurrence counts each unordered multiset of event edge types exactly once, because every source triple belongs to one unique (boundary, local-family-category) class and the same suffix state captures its complete connectivity effect. Hence the exact connected fiber is Q_m(b)=D_0(b,EMPTY), including the heterogeneous-multiplicity corrections of KN.1.

Order local count triples lexicographically (x,y,z), then order the eight-support sources lexicographically by their sequence of triples. At each prefix, the number of completions below any candidate triple is exactly the corresponding suffix value D_(i+1). Summing these blocks produces a zero-based rank in [0,Q_m(b)); choosing the unique block containing a given rank and subtracting preceding sizes gives the inverse unrank. Induction over the eight supports proves rank(unrank(k))=k and unrank(rank(source))=source for all admissible sources.

When m and b are already known, an exact *fixed-width* conditional source annotation requires and attains ceil(log2 Q_m(b)) bits for Q_m(b)>0 (zero bits when Q=1); this follows by pigeonhole lower bound and the rank construction. The code preserves every deterministic future observation **defined solely on these eight unordered auxiliary triples**, since those triples are recovered exactly. A future signed phase, timestamp, original event order, native third slice coordinate, or BRC temporal carrier is additional input and is not manufactured by this code.

The memoized count automaton has at most 9×4096×5=184,320 (i,r,q) states, each with at most 16 grouped transitions, independent of the magnitudes of m_s apart from exact integer bit complexity. The attached reference rank/unrank enumerates up to O(sum m_s^2) local candidate triples and is a correct baseline rather than a logarithmic-time random-access decoder.

## Exact evidence

The attached independent Python standard-library verification regenerates all 12 Port bits, 8 support edge triples, the 512 forced boundaries and exact grouped weights. It compares the five-state suffix DP to a separate GF(2) group-algebra recurrence with the correct three heterogeneous monochromatic boundary corrections v_j from KN.1. This covers all 512 boundaries for each of five multiplicity vectors: uniform m=1,2,3,4 and (1,2,3,4,1,2,3,4), i.e. 2,560 per-boundary equality checks. For every positive fiber it also verifies ranks 0, floor(Q/2), Q-1 and all ranks if Q≤12. Every assertion passed in the local execution of the reference script.

| multiplicities | Q_m(0) | SUM_(b in F)Q_m(b) | memoized DP states |
|---|---:|---:|---:|
| (1)^8 | 6 | 1,638 | 26,624 |
| (2)^8 | 7,197 | 420,093 | 28,672 |
| (3)^8 | 71,197 | 25,000,189 | 29,184 |
| (4)^8 | 2,788,422 | 640,727,574 | 29,184 |
| (1,2,3,4,1,2,3,4) | 5,984 | 1,822,605 | 27,136 |

Concrete invertible witness: at uniform m=2 and b=0, k=3598 un-ranks to the eight triples
(0,2,0),(0,2,0),(0,2,0),(2,0,0),(0,2,0),(0,2,0),(0,2,0),(2,0,0).
Ranking this vector gives exactly 3598. For the mixed vector and b=51, Q=8863 and k=4431 also round-trips.

The heterogeneous corrections v_j are important: e.g. m=(2,1,1,1,1,1,1,2) yields v_j=165,2337,2436. Subtracting three disconnected cases from zero rather than at these three boundaries gives wrong individual fibers. KN.1 already uses the correct rule; this is a regression witness, not a claim of a flaw in KN.

## Next research question

Develop a subquadratic local rank/unrank selector that uses closed combinatorial block sums rather than scanning all local triples; then specify a typed source-operation interface and determine the minimal additional data for preserving one native ordered/signed update and one nontrivial BRC future observer. Explicitly choose the three-dimensional slice embedding, temporal order and signed source type before any native-fidelity theorem.

Evidence strength: mathematical proof by exact counting and induction, executable finite regression, author check. Independent Review: NOT_REVIEWED. Existing Task/CLAIM/PROGRESS authority is separate.
