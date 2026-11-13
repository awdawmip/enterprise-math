# R710 — Named hidden-third triad observer: minimal three-state BRC future memory

Date: 2026-11-11 Asia/Shanghai. Task RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142; frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389. Researcher EM-X6-640177, activity RA-BC55A6E8FF1DD5106A03841E. Continues R708/R709 in PR #2037.

## Candidate state and observation

R709 has a fixed X6 Cell, m>=2 labeled native force quanta per saturated axis A,B, and m labeled third tokens C, all attached to the same chosen Cell, with source, axis and sign retained. Full complete triadic decompositions are pairs (f,g) of bijections A->B and A->C. The positive-rational source update holds with probability 1/2; otherwise choose one of f/g channels with probability 1/4 each and one unordered A pair uniformly, swapping the selected channel's two partners simultaneously. No intermediate stable two-force event occurs.

Fix a* in A, b* in B, c* in C and define E=1{f(a*)=b*}, F=1{g(a*)=c*}. The named three-token triad occurs exactly when H=E*F=1. Let K=E+F in {0,1,2}.

Put alpha=1/(2m) and beta=1/[2m(m-1)].

## Theorem R710-A — complete four-state joint observer and 3-state quotient

For all m>=2 the joint observer (E,F) is a strong Markov quotient of the full (m!)²-source transition kernel. From (e,f), only the transitions (1-e,f) and (e,1-f) occur, with probabilities alpha when the corresponding bit equals 1 and beta when it equals 0; the probability of staying at (e,f) is the remaining mass. In particular, the probability that BOTH bits flip in one elementary event is zero.

Proof. An f-channel transposition changes only f(a*) and hence E; a g-channel transposition changes only g(a*) and hence F. The transposition includes a* with probability (m-1)/binom(m,2)=2/m if the corresponding bit is 1, producing loss alpha. If the bit is 0, exactly one A partner currently maps to the named B or C token, and swapping that partner with a* creates the bit with probability 1/[4binom(m,2)]=beta. These weights depend only on the current bits, independent of the remainder of the full source. Hence strong lumpability holds. QED.

Exchanging E and F is a symmetry of the joint quotient. Consequently K=E+F is itself an exact strong Markov quotient, with the following birth/death transition probabilities:

K=0 -> K=1: 2beta = 1/[m(m-1)];
K=1 -> K=0: alpha = 1/(2m);
K=1 -> K=2: beta = 1/[2m(m-1)];
K=2 -> K=1: 2alpha = 1/m;
each K->K probability is one minus the listed outgoing probabilities.

All transitions are positive rational BRC source masses. The three-state stationary law is Binomial(2,1/m): pi_k=binom(2,k)(1/m)^k(1-1/m)^(2-k). This follows either by direct detailed balance (pi_0*2beta=pi_1*alpha and pi_1*beta=pi_2*2alpha) or from the independently uniform permutations f,g, where both named matches are independent Bernoulli(1/m) at stationarity.

## Theorem R710-B — three-state minimum to predict future named full-triad occurrence

The instantaneous binary observer H=1{K=2} does not define a Markov quotient for m>=2: both K=0 and K=1 give H=0, yet from K=0 the one-step probability of H'=1 is 0 and from K=1 it is beta>0. The states K=0 and K=1 are thus predictively distinguishable at horizon 1, and K=2 differs at horizon 0. Every state K=0,1,2 is attainable in the full labeled population for m>=2. Therefore every exact finite-state observer sufficient for all future H-trajectories must distinguish at least THREE classes; K attains this bound with strong lumpability, and the minimal fixed-length binary encoding uses ceil(log2 3)=2 bits.

The exact two-step transition K=0 to K=2 is 2beta²=1/[2m²(m-1)²]; every such transition necessarily passes K=1 and retains the intermediate one-pair source. This gives a concrete BRC joint-relation residual: the present yes/no truth value of the named full triad discards a future-relevant partial match, but the count of matched named partners completely repairs it for this kernel. For queries of WHICH partner or port was involved, retain upstream (f,g) source identities.

## Exact verification

Executed standard-library Fraction checker covering all complete labeled source states for m=2,3,4, respectively 4,36,576 states. For every source it evaluates the full transition kernel, verifies normalization, four-state joint-fiber constancy, 3-state K-lumpability, no simultaneous bit flips, stationary detailed balance, and K0->K2 two-step activation. K-fiber sizes: m=2 (1,2,1); m=3 (16,16,4); m=4 (324,216,36). Verified marker R710_THREE_STATE_NAMED_TRIAD_BRC_MINIMAL_FUTURE_OBSERVER_PASS. Source program and JSON evidence provided in experiments/R710_TRIADIC_NAMED_TRIPLE_OBSERVER_VERIFY_20261111.py and experiments/R710_TRIADIC_NAMED_TRIPLE_OBSERVER_EVIDENCE_20261111.json.

## Remaining native scope

This is an exact source-counting BRC candidate under the R709 whole-triad simultaneous swap operation. Native X6 Link/Port permission, V29 PASS/TRANSFER, V39 loop current j and native rotation transport remain to be checked at frozen science. Next test the m=2 witness K=0/1 under one legitimate native update; if the native event distinguishes more hidden state than K, retain an explicit source/port/loop residual. All proofs preserve P000 and separate sign/phase from positive branch mass.
