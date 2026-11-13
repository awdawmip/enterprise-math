# Stage412-B — Exact paired Euler/K boundary transfer and minimal two-POP counterexample

Date: 2026-11-04 (Asia/Shanghai). Parent: Research2 Stage411-B, commit 67957048ffd5bcd609d82cc38d69fbff8d8293e5, Draft PR #1736.
Classification: PORTABLE_AUTHOR_PROOF / EXACT_BIGINT_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Scientific pins remain GLOBAL main bf84bd7c61a2444b59b1da96be57df0e9ae47e53, EM main 2af3fc484eb11060b69e0afc1b562bcaf5ad1419, original P000 Git blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current normative rules are read independently; no alteration to P000, protected worldview or frozen inputs.

## Model and the information to be retained

The native signed spatial alphabet D={+E_j,-E_j:1<=j<=6} has twelve directions in the original six-dimensional X6 space. A=+E1 and B=-E1 denote two actual members of D, not a separate native two-dimensional plane. A path is an ordered finite word in D. The paired observer at every instant is (|P|,|Q|,z(P),z(Q),J_P,J_Q,K), with the full directed labelled adjacent-edge matrices J_P(a,b),J_Q(a,b) and absolute aligned match count K=sum_{i<=min(|P|,|Q|)}[P_i=Q_i]. Action enabledness is also observed. Positive BRC multiplicities count distinct path words; signed amplitudes are not inferred from those counts.

Future language L_1: arbitrary paired APP(a,b) in D^2, up to one Q-only POP, up to one simultaneous inverse-adjacent-pair CANCEL (both sources must end with adjacent inverse directions). Expanded language L_2 changes the Q-only POP budget to two and leaves all other rules intact.

## Theorem 412.1 — exact non-enumerative paired Euler/K boundary transfer

For any equal-length n>=1, finite D with a fixed displacement map e:D->Z^6, prescribed directed edge counts J_P,J_Q with sum n-1 each, prescribed endpoints z_P,z_Q and prescribed absolute K, a dynamic program computes EXACT integer counts of all current-observation histories by any bounded terminal suffix pair (suffix_lP(P),suffix_lQ(Q)), without listing individual full path pairs.

For every candidate first-letter pair (a,b) in D^2, check the exact endpoint laws:

 z_P = e(a) + sum_{u,v in D} J_P(u,v)e(v),
 z_Q = e(b) + sum_{u,v in D} J_Q(u,v)e(v).

Start with residual edge vectors R_P=J_P,R_Q=J_Q, last letters (a,b), k=[a=b], suffixes (a,b), and integer mass 1. For each pair of possible NEXT LETTERS (c,d) with R_P(a,c)>0 and R_Q(b,d)>0, decrement these TWO directed counts by one, set last letters (c,d), update k <- k+[c=d], and append/truncate suffixes. Add integer masses of identical resulting states. Accept exactly when both residual edge vectors vanish and k=K. The coefficient of each terminal suffix pair is precisely its number of ordered source-path pairs.

Proof: every accepted history determines exactly one initial letter pair and one sequence of ordered next-letter pairs, and conversely every such sequence defines exactly one history. The update consumes exactly its labelled adjacent edge, preserves the endpoint identity, and counts the exact contribution to aligned K at the new absolute position. Induction on the number of consumed edges gives a weight-preserving bijection between DP walks and path pairs. Repeated occurrences of one directed edge are indistinguishable edge TYPES, not individually numbered edges; thus the transition has unit weight rather than a factor R(a,c)R(b,d). No overcounting occurs.

For fixed d=|D| and fixed suffix lengths, the memoized state consists of 2d^2 residual counts, two last letters, two constant-length suffixes, and K in [0,n]. A loose bound is O(d^(lP+lQ+4) * (n+1)^(2d^2+2)) elementary transition/addition operations, with output counts of O(n log d) bits. This bound is polynomial in the NUMERIC n for fixed d and suffix lengths; it is not a polynomial-bit-input claim when n and J entries are binary encoded. A general observer-safe minimal quotient requires an independently proved equivalence map of terminal signatures; the DP by itself only counts safe suffix signatures.

## Corollary 412.2 — direct transfer for the complete defect family F_n

Use the Stage411-B complete observation with:
 J_P(AA)=n-3, J_P(AB)=J_P(BA)=1;
 J_Q(AA)=n-5, J_Q(AB)=J_Q(BA)=2;
 all other native directed entries zero; endpoints z_P=(n-2)E1, z_Q=(n-4)E1; K=n-1; n>=5.
The endpoint equation forces first letters A,A. The transfer therefore works on just three nonzero directed edge TYPES for each source, while keeping the original twelve-direction native embedding. Stage411-B proved the all-future L_1 quotient; it gives the following exact map from safe suffix_3(P)/suffix_4(Q) labels:

 C0: P ends BA, Q ends BABA.
 C1: P ends BA, Q ends AABA.
 C2: P does not end BA and Q ends BAA.
 C3: P does not end BA and Q ends BA.
 C4: P does not end BA and Q ends AAA (suffix BAAA or AAAA).

All five are distinguished by the Stage411 tests and each is future-equivalent internally under L_1. Summing the transferred terminal suffix counts under this proved class map yields, for EVERY n>=5,

 (|C0|,|C1|,|C2|,|C3|,|C4|) = (1,n-5,2(n-5),n-4,(n-5)(n-6)).

Consequently |F_n|=(n-3)(n-4) and q_L1(F_n)=2 for n=5, 4 for n=6, 5 for n>=7. Direct inspection of the suffix cases additionally gives the precise number of distinct raw sufficient suffix keys: 2 for n=5, 6 for n=6, 7 for n=7 and 8 for every n>=8. Thus the all-horizon exact L_1 quotient has 5 states even where the safe suffix representation has 8. The new computational increment is that all class multiplicities are obtained FROM J/endpoints/K by a residual-edge transfer rather than by enumerating F_n. The current equivalence mapping is family-specific and uses the still-unreviewed Stage411 mathematical certificate.

## Theorem 412.3 — two Q-POPs defeat the four-state quotient at the shortest family length

For F_6 under L_2 (two POP_Q, one simultaneous CANCEL), the exact all-future quotient has SIX states. This is the earliest n in the family where L_2 gives a strict refinement over the L_1 quotient.

At n=6, Stage411-B partitions the six histories into four L_1 classes C0,C1,C2,C3, of sizes 1,1,2,2. The old distinguishing traces remain admissible in L_2, hence different old classes cannot merge. The two members of EACH nonsingleton class are now separately observable:

C2 pair: (ABAAAA,ABABAA) and (AAABAA,ABABAA). They have exactly the same initial full observer. Apply POP_Q, POP_Q, APP(B,A), CANCEL. This is enabled in both states and results in (ABAAA,ABA) versus (AAABA,ABA). The resulting absolute K equals 3 versus 2, respectively.

C3 pair: (ABAAAA,ABAABA) and (AABAAA,AABABA). These also share their full initial observer. Apply POP_Q, POP_Q, APP(B,B), CANCEL. This yields (ABAAA,ABA) versus (AABAA,AAB). The resulting Q directed adjacency histograms are {AB:1,BA:1} versus {AA:1,AB:1}.

Therefore the six elements are pairwise distinguishable; 6 is both the lower bound and the total-history upper bound: q_L2(F_6)=6. At n=5 the L_1 quotient already consists of two singleton histories, so both L_1 and L_2 have q=2. The smallest n for strict refinement is 6. The new residual revealed by a second POP is the original cross-source alignment or labelled edge immediately behind the earlier deletion boundary. This does not refute the Stage411 five-state L_1 theorem: the future operation language has changed.

## Executed verification and boundaries

REPRO_STAGE412B.js uses exact BigInt transition weights; it independently enumerates full F_n ONLY as a crosscheck for n=5..10. The residual transfer is run on n=5..14 and n=16. Every class multiplicity, entire raw suffix histogram, admissible starting endpoint and all stated finite checks pass. For n=16 the transfer counts 156 histories using 303 memoized nonterminal states and eight raw safe suffix labels. The two L_2 witness traces are checked step by step with their full initial observer and distinct final K or J_Q. Two separate executions return identical JSON bytes.

The general recurrence and the F_6 exact quotient have mathematical proofs above. The finite program specializes the general recurrence to the sparse AB edge-support input; it does not execute a fully general 12-direction input experiment. Stage411 future bisimulation and class map are reused as an author-level proved source, pending independent review. A safe suffix count is not by itself a full minimal-memory proof for other arbitrary histograms.

BRC usage: native exact path multiplicity and the residual labelled directed-edge/Euler operator are COMPOSE_APPLIED; initial/full alignment K is explicitly retained. No positive-mass-to-signed-amplitude conversion, native time dynamics, physical calibration, canonical task CLAIM, formal Result, independent Driver review or Foundation promotion is asserted.

## Next discriminating question

Stage413-B: characterize q_L2(F_n) for all n>=7 without listing F_n; find the minimal extra cross-alignment/boundary residual needed after two POPs and one CANCEL. As a second route, generalize the histogram transfer to an automatic observer-safe symbolic class refinement for arbitrary sparse J and bounded eraser budgets, with a proof of exact future-language correspondence. Preserve all 12 native signed directions and the current source/firewall context.
