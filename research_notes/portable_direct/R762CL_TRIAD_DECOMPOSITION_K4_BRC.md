# R762CL — Six native X6 force quanta: triadic decomposition, K4 symmetry, and exact BRC switch dynamics

**Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142.
**Frozen input:** awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000 triadic balance, native signed X6, V17 shortest paths).
**Previous units:** R762CH, CI, CJ, CK; no repetition of pair-area computations.
**Evidence grade:** author proof + independent exact integer Python checker; independent review NOT_REVIEWED.

## Typed scientific question

P000 makes exactly three nonzero primitive force quanta the minimal stable unit, with the canonical equal-quantum triad closed under pairwise PERP_E. The exact Cell/Port/Link event admission law remains open. Consider an explicit **incidence candidate** with six distinguishable equal-quantum positive-axis force tokens, one on each of six different X6 axes, all attached to a chosen Cell. In this candidate, each triple of distinct tokens is a permitted triadic closure *candidate*. Since all six axes satisfy pairwise PERP_E by P000, every proposed triad satisfies the fixed arity and equal-quantum angular premises. A transition defined below is a candidate local recombination, not an attested native TRIADIC_CLOSURE_E event.

Use K4's six unoriented edges E={01,02,03,12,13,23} as *names of the six independent X6 axes* (not a new native plane). An assembly state is an unordered pair {T,E\T} of complementary 3-force triads. Branch identities are retained separately from Cell/force multiset observations.

## Theorem 1 — ten assemblies and the exact K4/S4 orbit split

There are exactly C(6,3)/2=10 such unordered partitions. K4 vertex permutations S4 act on their six named edges and split these ten assemblies into exactly two orbits:

* SF: 4 star/face partitions, where a 3-edge star is paired with its complementary triangular face;
* PP: 6 path/path partitions, where a 3-edge simple path on four vertices is paired with the complementary simple path.

**Proof.** A 3-edge subset of K4 has exactly one of the degree profiles (3,1,1,1), (2,2,2,0), or (2,2,1,1), respectively star, face, path. Their labeled counts are 4,4,12. Complements pair stars with faces and paths with paths. Thus the ten unordered partitions comprise four SF and six PP. Vertex relabelings act transitively within either class. QED.

A full named branch index needs exactly ceil(log2 10)=4 fixed bits. The S4-invariant SF/PP observation needs one bit; conditional on that orbit type, the largest fibre has six members, and the **optimal additional fixed-length repair is 3 bits**. Orbit-local enumeration attains the bound. For the named predicate Q_T(s)=[a particular 3-token set T is one of the two complete triads], every distinct pair of partitions has a distinguishing T, because the two complete triples uniquely determine the partition. Thus the 4-bit bound is sharp for this declared named-membership language.

## Theorem 2 — all nine other states occur by one candidate swap

Define a candidate exchange to select a in the first triple A and b in the complementary triple B, then replace {A,B} by {(A\{a})∪{b},(B\{b})∪{a}}. This preserves six token identities, equal quanta, co-attachment and two triad cardinalities, and preserves distinct-axis membership.

**Claim.** The candidate exchange graph on the 10 unordered partitions is K10, degree nine.

**Proof.** There are 3x3=9 pairs (a,b). Each resulting triple A' meets the original A in exactly two labels. Different exchanges give different A', and complementing A' meets A in one label, so no pair of exchanges yields the same unordered partition. Conversely, for any other partition {C,E\C}, exactly one of C,E\C meets A in two labels and must be obtained by swapping one a in A with one b in B. Hence every other partition is a unique candidate exchange neighbour. QED.

This is a complete **typed candidate rewrite system**. It does not supply the currently missing physical Cell/Link/Port permission predicate.

## Theorem 3 — exact two-orbit positive N-BRC transport

Assign each named candidate exchange integer source mass one, retaining all distinct named transition histories. The SF/PP division is equitable. For a starting SF branch, exactly three of its nine outgoing neighbours are SF and six are PP. For a starting PP branch, four are SF and five are PP. Thus the exact aggregate **integer N-BRC** row transfer is

    M = [[3,6],
         [4,5]]         (row and column order SF,PP).

For a row of start counts v_0, v_t=v_0 M^t counts all t-exchange sources by orbit. Every single named starting assembly has 9^t distinct labeled t-step exchange histories. M has eigenvalues 9 and -1. For one named SF start:

    SF_t=(4*9^t + 6*(-1)^t)/10,
    PP_t=(6*9^t - 6*(-1)^t)/10.

For one named PP start:

    SF_t=(4*9^t - 4*(-1)^t)/10,
    PP_t=(6*9^t + 4*(-1)^t)/10.

All quantities are exact nonnegative integers. The normalized homogeneous-exchange transition kernel is

    P = [[1/3,2/3],
         [4/9,5/9]].

Its stationary masses are (2/5,3/5), exactly the positive branch proportions 4:6. The nonstationary eigenvalue is -1/9: every initial orbit-level deviation decreases in magnitude by a factor 9 per candidate exchange, with alternating sign.

**Proof.** Each named assembly sees every other named assembly exactly once, and orbit class sizes are 4,6. Hence the outgoing neighbour matrix is M. Each source has nine successors; iteration is exact positive N-BRC path enumeration. The characteristic polynomial is (x-9)(x+1) and its stationary left eigenvector is (4,6), giving the displayed formulas; the Markov kernel divides M by 9. The identical outgoing orbit counts for every member of each class prove strong lumpability for the specific language of homogeneous candidate exchanges followed by S4-invariant orbit readings/positive aggregate counts. QED.

This two-state BRC quotient is safe only for that declared operation/observation language. A fixed named triad-membership query distinguishes some states in the same orbit. Token-dependent asymmetric weights can change the neighbour totals. Under those enriched languages the corresponding source bits or an independently proved finer quotient remain necessary.

## Exact validation and provenance

The companion R762CL_VERIFY.py uses pure exact integer operations: enumerate 10 unordered K4 edge partitions, check triad degree-profile classes, check the action of all 24 S4 vertex permutations, verify the complete 9-neighbour exchange graph on all 10 named starts and the 2x2 orbit count matrix, and enumerate exact BRC walks from all 10 starts for t=0,...,12 against the closed formulas. The verified bounded family comprises 130 start-depth pairs and 240 group-action/graph-covariance comparisons. R762CL_EVIDENCE.json records the parameters and outputs. General conclusions are proved above; finite checks are author-side.

The unrestricted number of partitions of 3m *distinguishable* tokens into m *unlabeled* triples is (3m)!/(6^m m!), e.g. m=1,2,3,4 gives 1,10,280,15400. This supplementary identity counts abstract partitions; m>2 requires a compatible force-incidence model before being read as allowed native triadic states.

**Next native test:** Obtain the actual licensed TRIADIC_CLOSURE_E signed Cell/Link/Port admission and V17/V29/V39 transport predicates. Check which of the ten typed co-attached triad assemblies are actually admissible and which of the nine candidate swaps satisfy licensed update conditions. Restrict the resulting graph to genuine legal edges and recalculate exact BRC orbit transport, adding path source/provenance or named queries from R762CH/CK as required. A single genuine rejected candidate swap is a decisive refinement of the model; a full legal transition table can establish or refute safe S4 lumpability without redoing prior pair-area theorems.