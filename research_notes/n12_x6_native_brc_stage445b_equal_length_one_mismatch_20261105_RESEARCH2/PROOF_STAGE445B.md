# Stage445-B — Polynomial exact future classes of equal-length one-mismatch native-X6 histories

2026-11-05 · Research2 · AUTHOR_SIDE_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED.

## Sources, model and observer
Stage444-B parent fd59ad5f215f809449598bb7b24841f3ebf05800; Stage439-B future-repair theorem 7f9456031a9fdfdf12836116f178a17bf50be965. Frozen scientific pins: GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; original P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current normative context independently read from canonical main.

In the native X6 signed alphabet D={+E1,-E1,...,+E6,-E6}, set A=+E1, B=-E1. Initial ordered paths P,Q have length L>=3, endpoints A, and nonadjacent internal Bs. P has k B letters, Q k+1; exactly one original position differs (K=L-1). Each source has identical POP budget p, 0<=p<L, but arbitrary separate APPEND budgets rP,rQ>=0 with all 12 directions and arbitrary legal interleaving. Full observer O=(lengths, both six-vector endpoints V, both complete directed adjacency histograms J, joint absolute-position matching count K). BRC integer masses are exact unit-positive original branch populations; source provenance retained.

Since Q has one additional B and the Hamming difference equals one, the letter-pair alphabet is Sigma={(0,0),(0,1),(1,1)} with exactly one (0,1), where 1 is B. Consecutive pairs z=(u,v), w=(x,y) are compatible iff u*x=v*y=0; initial and final symbols are (0,0). The present endpoints are V_P=(L-2k)E1, V_Q=(L-2k-2)E1, and the adjacency counts for P are (AA,AB,BA,BB)=(L-1-2k,k,k,0), likewise replacing k with k+1 for Q. Therefore all such histories lie in one complete current-O fiber.

## Theorem 445.1 — Exact future quotient
Two histories in this fiber have identical observations at every prefix of every legal labelled future operation word if and only if their paired original suffixes
T=((P_(L-p),Q_(L-p)),...,(P_L,Q_L)) are identical.

Proof: Under m=n=L and pP=pQ=p, Stage439-B's unrestricted exact future-repair key R contains both source original suffixes S_P,S_Q over [L-p,L]. Its additional cross-source original-direction slots A_P,A_Q and mutable original equality slots E all have original indices in [L-p+1,L]. Thus R is determined by T, and R also determines T. The Stage439-B necessity/sufficiency theorem equates equality of R with entire labelled future-O observational equivalence. The result holds for every nonnegative pair rP,rQ and is a conditional author theorem inherited from Stage439-B, awaiting independent review.

## Theorem 445.2 — Exact O(L^2)-addition support algorithm and class populations
Let s=L-p; g=s-1 is the unobserved original prefix length. A candidate pair suffix T has p+1 symbols over Sigma, final symbol (0,0), first symbol (0,0) if g=0, compatible consecutive pairs, and at most one mismatch. Put a(T)=number of P-coordinate 1s, d(T)=number of (0,1) symbols.

Define integer C_g(a,d,z) to count unobserved length-g pair prefixes with a P-defects, d mismatches (d<=1), and final pair z, with the first pair fixed (0,0) and compatible consecutive symbols. For g=0 use the virtual zero pair C_0(0,0,(0,0))=1; for g>=1 start C_1(0,0,(0,0))=1. At each step add all compatible w with d+[w=(0,1)]<=1 via

    C_(j+1)(a+w_P,d+[w=(0,1)],w) += C_j(a,d,z).

The exact integer raw-history population of a candidate suffix T is

    M(T) = SUM_z C_g(k-a(T),1-d(T),z) * [compatible(z,T_first)],

and is zero if T violates its own terminal, adjacency, or mismatch constraints.

Proof: Every original pair with suffix T corresponds bijectively to a hidden prefix H. Its P B-count must be k-a(T), and its unique mismatch number must be 1-d(T). Q's B-count k+1 then follows automatically. The only inter-block adjacency condition is compatibility of the last H symbol with T_first. The C recurrence counts distinct compatible H exactly once. Therefore the sum counts original histories, not merely supported outputs.

To count DISTINCT future classes without enumerating supported T, perform a second dynamic program over suffix prefixes, with state (i,a,d,last,first): emitted length, P B-count, mismatch count, last and first pair symbols. Each compatible choice w extends a unique visible word and increments its count. At i=p+1 count only states with M(T)>0; the terminal predicate is expressible entirely in (a,d,first) and precomputed C_g. The terminal sum is q_F=number of feasible T. Each emitted visible suffix has one path in this second DP; prefixes with identical state can be added without conflating distinct words.

Both DPs use O(L(k+1)) states up to constant 3-letter factors and at most 3 transitions per state. Since k<=L, this is O(L^2) exact integer additions, O(L^2) integer cells; counts are <=3^L and require O(L) bits, yielding O(L^3) schoolbook addition bit-operations including precomputation. Input construction is O(L). Suffix completion counts yield class lexicographic ranking/unranking. A separate conditional-prefix completion DP ranks/unranks raw pairs within each class; its O(L^2) setup and O(L) reconstruction preserve source identity. The minimum fixed class label uses ceil(log2(q_F)) bits when q_F>0.

## Corollary 445.3 — Independent raw population checksum
The total number of current-fiber raw histories is
    |F|=(k+1)*binomial(L-k-2,k+1).
Indeed choose Q's k+1 nonadjacent internal B positions in binomial(L-k-2,k+1) ways, then select one of Q's k+1 B positions to erase in P. This is a bijection with all one-mismatch pairs.

## Exact executed evidence and continuation
Python3 standard-library reproduction: REPRO_STAGE445B.py loads the preserved complete source STAGE445B_FULL_REPRO.py.gz directly (no installation/network); stdout is STAGE445B_EXECUTED.json. Gzip source Git blob 67cbdea403ea5033fb89ba02e7cf60099642d503; original uncompressed source Git blob 149c0970dcb8035025bb38a29f4fb0377b4cead5.

The complete parameter sweep for L=4..11, all eligible k and p=0..L-1, covered 230 cases, 202 nonempty, 5061 raw history instances and 2602 supported classes. It checked 2602 integer class masses, 5204 class rank/unrank operations and 5061 complete raw-history recovery roundtrips against direct enumeration. Four independent complete all-12-direction future enumerations for L=5..7, p=1, rP=rQ=1 visited 16900 future states and checked 90 intra-fiber history pairs; the full (V,J,K) future signatures agree with the proposed partition.

Examples: L=8,k=1,p=2 gives |F|=20, q_F=5 and populations (3,3,4,4,6); L=10,k=2,p=3 gives |F|=60, q_F=10, with histogram {3:2,4:3,6:3,12:2}. A DP-only large case L=128,k=30,p=60 yields q_F=71880922565861 (10657 memoized states and 16572 transitions), without enumerating the original histories or the supported classes. Exact sweep digest: 6fef0a09b377ce5c2dac61339a9add0d57fb506be671a18b93e6d35935e1a859.

The theorem is an exact static native-X6 ordered-path statement; independent proof review, formal Source Result and physical heartbeat/signed-amplitude extensions retain their own research boundaries.

Next Stage446-B: unequal lengths and asymmetric POP budgets at one mismatch. The Stage439 repair key now contains separate source-letter and equality windows. Search explicit false merges of a candidate mismatch-marker/hidden-gap-capacity carrier and retain distinguishing labelled operation traces; develop an observer-safe support/mass automaton and two-level decoder.
