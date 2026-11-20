# Euler RR-09 C01: exact core prior-art classification, first pass
Task RS-EULER-RR-20261012-09 / TP2-D6320792C26EFAD4DDCD.
Scope: 2026-10-11 canonical project manuscript at a6627d28d1e02f16ec5ca4d5118801c005cca583:research_notes/chatgpt_direct/20261011_EULER_RELATIONAL_RECORDING.md (blob 03cfdf23f8f1a6208b4ac4eb862a1b7ad3811d8b).
State: authored preliminary comparison only, not independently reviewed, not a completed prior-art audit, no source ZIP replay, no physical native detector acceptance.

## Statement / assumption / elementary mapping
Write all labels in Z/3Z. E(j,a,r)=(j,a,r+j-a) exactly factors into two controlled cyclic additions:
S_(j->r):(j,a,r)->(j,a,r+j);
S_(a->r)^(-1):(j,a,r)->(j,a,r-a).
They commute, so E=S_(j->r) S_(a->r)^(-1). Such controlled modular-shift maps on finite alphabets are the classical basis permutation underlying qudit SUM gates, rather than a novel reversible-gate algebra. E^-1 subtracts j-a, E^3=id, and r=a -> r'=j. The ready relation is a specified correlated ancillary preparation, not an automatic consequence of reversibility.

Simultaneous affine relabeling phi(x)=epsilon*x+k, epsilon in {1,-1}, k in Z3, commutes with E: phi(r+j-a)=phi(r)+phi(j)-phi(a). Since these 6 affine maps equal all permutations of Z3, E is S3-covariant under common relabeling. This is a direct finite-group calculation, not an independent claim of physical frame covariance beyond this alphabet.

Let omega^3=1, omega!=1, and normalized positive weights w_s sum to 1 on complete joint worlds s. Let C_XY=sum_s w_s omega^(x_s-y_s). Then after E,
r'-j=r-a, hence C_RS(after)=C_RA(before).
It is an exact elementary character-pullback identity. Moreover C_RS=1 iff r=a on all positive-weight worlds, because 1 is an extreme point of conv{1,omega,omega^2}; equivalently write real-part sum to obtain P(r-a !=0)=0.
Thus the algebra/convexity portions reuse familiar finite-group and probability theory; the implemented typed-BRC reader/contact realization, preservation of the original old-source projection under permitted future alphabet, and possible native channel-sensitive coupling are model-specific claims requiring separate evidence. Positivity assumptions and complete-world pairing are essential; this does not copy unknown quantum amplitudes.

## Source/provenance and novelty matrix
1. Reversible compute-copy-uncompute: Bennett, "Logical Reversibility of Computation," IBM J. Res. Dev. 17(6):525-532 (1973), DOI 10.1147/rd.176.0525, publisher https://ieeexplore.ieee.org/abstract/document/5391327 . The article's source-facing three-stage construction establishes general reversible preservation of inputs/output but is not verified here to contain the exact E map. Classification: HIGH-LEVEL EXISTING PRINCIPLE, NOT EXACT E ATTRIBUTION.
2. Invertible finite gates: Toffoli, "Reversible Computing," MIT-LCS-TM-151, February 1980, primary MIT repository https://dspace.mit.edu/entities/publication/06a8b271-428a-4379-955c-8c7334aa0288 . General invertibility and reversible circuit composition; not an exact E source claim. Classification: ESTABLISHED METHOD.
3. Qudit / finite-dimensional controlled-shift background: Gottesman, "Fault-tolerant quantum computation with higher-dimensional systems" (1998 technical report; 1999 journal), https://arxiv.org/abs/quant-ph/9802007 ; author bibliography https://www.cs.umd.edu/~dgottesm/papers.html . Controlled modular-addition is a standard finite-register gate; verify the exact section/formula in the original paper before a paper-specific equality attribution. Classification of E as two standard SUM-type permutations follows the explicit algebra above independently of that bibliographic confirmation.
4. Calibration and correlation transfer: directly derived here from E and positive joint weight; no independent prior-art novelty assigned to the formula. Classification: ELEMENTARY FINITE-CHARACTER INSTANCE; TYPED-BRC IMPLEMENTATION SEPARATELY TESTABLE.
5. Receiver persistence, inverse reset, environment historical bound: outside this first pass. Original model and ZIP pins in taskbook remain frozen; a missing PDF page locator or unavailable original ZIP is an OPEN provenance obligation, not evidence of novelty.

## Discriminating next steps
Read original Gottesman formal SUM definition and Bennett's relevant pages directly; record exact theorem/section and compare hypotheses. Validate typed BRC adapter/old-channel source projection using actual pinned model input separately from these finite-register identities. Audit positive finite environment and observation-window claims against original-source Markov/coupling results. Keep provenance and novel native-selector hypothesis distinct.