# R698 | Exact observer-minimal state for anisotropic port deletion (X6 candidate)

Date: 2026-11-10. Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; immutable publication TP2-8B7E13C5904A2D6F1142. Scientific pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (preserved from R462); direct author-side predecessor R697: PR #2001 @ 9a7000a9f4bd3a5a39ca45b6774b8fe14fb69ec7. Proof type: exact abstract rational port model, not an accepted native X6 TRIADIC_CLOSURE_E event.

## Typed model and BRC branch semantics

Preserve P000 native signed six-dimensional Cell torsor; the third-axis options for fixed distinct first/second axes i,j form the remaining four native axis labels R={0,1,2,3} in a relative labeling. A_t subset R is the live third-port set at separately typed event time t. Fix positive rational weights w_i with sum w_i <= 1. At each event draw X_t=i with probability w_i or null with remaining probability, independently of previous draws. If i remains live, delete i; otherwise hold. Thus T(A,A\{i})=w_i for i in A and T(A,A)=1-sum_{i in A} w_i. Every labeled draw word is a positive rational BRC provenance branch; projection by endpoint adds exact positive masses, without force cancellation. Unlike R697's hold-with-2/5/otherwise-uniform-from-live model, these candidate rates are fixed for the duration of the experiment. The real X6 Link/Port mapping remains the next scientific question.

## Theorem 1: coarsest exact future port-count quotient

For fixed w define Phi(A)=multiset{w_i:i in A}. For any A,B, all joint future distributions of (|A_t|) at all finite horizons, including the present observation, agree if and only if Phi(A)=Phi(B). Moreover Phi is a strongly lumpable Markov quotient.

Proof (sufficiency). If rate multisets agree, identify labels within identical-weight classes. For a state with m_v active labels of weight v, the total probability of decreasing m_v by one equals m_v*v, while holding has probability 1-sum_v m_v*v. The count-class transition kernel depends only on the vector (m_v), establishing strong lumpability and matching all finite-time count trajectories.

Proof (necessity). Equality of present observations gives |A|=|B|=r. For j=1,...,r, the event |A_j|=r-j requires all j independent draws to hit pairwise distinct currently active labels. Its exact probability is j!e_j(A), where e_j(A) is the j-th elementary symmetric polynomial in the active weights. Equal future count laws imply equality of all e_j for A,B, so the monic polynomials prod_{i in A}(x-w_i) coincide. Equality of roots with multiplicity gives Phi(A)=Phi(B), as required. This argument uses only horizons j<=r.

If the full four-port weight vector has distinct rates with multiplicities m_1,...,m_g, the number of future-count equivalence classes across all A is exactly prod_v(m_v+1). For the five partitions of four these counts are respectively: 4 -> 5; 3+1 -> 8; 2+2 -> 9; 2+1+1 -> 12; 1+1+1+1 -> 16. This is a rate-anisotropic generalization of the exact size-only five-state quotient in R697. Complete source-sensitive or named-port observations still require the label-to-rate and provenance information.

## Witness: (cardinality, total live rate) loses a two-step observable

Set (w_0,w_1,w_2,w_3)=(1,2,3,4)/10. Let A={0,3}, B={1,2}. Both have two live labels, and both have rate sum 1/2, hence the same one-tick port-count law. However the exact probability of emptying both within two events is
P_A(|A_2|=0)=2*(1/10)*(4/10)=2/25,
P_B(|B_2|=0)=2*(2/10)*(3/10)=3/25.
The second elementary symmetric coefficient preserves this difference. This is a strict counterexample to a proposed total-rate-and-count state compression in this model.

## Theorem 2: exact laws of all subset states and the absorption time

Let w(S)=sum_{i in S}w_i. For S subset A, all S still live after n ticks iff no one among S was drawn at any of n independent ticks. Thus P(S subset A_n)=(1-w(S))^n. Inclusion-exclusion gives, for B subset A:
P(A_n=B)=sum_{C subset A\B} (-1)^|C| (1-w(B union C))^n.
The exact count probability generating function is
E[z^|A_n|]=sum_{S subset A}(z-1)^|S|(1-w(S))^n.
Let tau=inf{n>=0:A_n=empty}. For positive rates,
P(tau<=n)=sum_{S subset A}(-1)^|S|(1-w(S))^n,
E[tau]=sum_{empty != S subset A} (-1)^(|S|+1)/w(S).
The expectation follows by summing the finite inclusion-exclusion expression for P(tau>n) over n>=0; each individual geometric series converges since 0<w(S)<=1.

For full A=R, w=(1,2,3,4)/10, subset-sum coefficient grouping gives
P(tau<=n)=1-(9/10)^n-(4/5)^n+2*(1/2)^n-(1/5)^n-(1/10)^n+0^n.
Integer exponent notation uses 0^0=1 at n=0. In particular E[tau]=445/36, P(tau<=4)=36/625 and P(tau<=8)=319977/781250. Alternating inclusion-exclusion coefficients are algebraic and do not represent negative BRC branch masses.

## Computation, scope, literature, next question

The exact verifier checks 16 starting port sets, 13 horizons n=0,...,12, 16 potential endpoints (3328 Fraction-equality cases) via independent dynamic programming and inclusion-exclusion; j!e_j for all starting sets and j, full 5 partition quotient counts and pairwise count-law equivalence, explicit witness and absorption quantities. The theorem itself applies to any finite horizon in the stated positive rational fixed-rate model.

Classical unequal-probability coupon collection already includes inclusion-exclusion completion formulas; compare Russell May, Coupon Collecting with Quotas, Electronic Journal of Combinatorics 15(1), N31 (2008), DOI:10.37236/906; Christian Berthet, On Von Schelling Formula for the Generalized Coupon Collector Problem (2017), arXiv:1703.01886. The Enterprise Math contribution here is the typed, observer-minimal BRC quotient and explicit evidence of the first failure of cardinality-plus-rate compression under candidate X6 port asymmetry.

Open: read frozen actual X6 Cell/Link/Port occupancy and V29 PASS/TRANSFER, V39 loop current j; instantiate legal three-nonzero-action Cell events, identify the actual conditional port kernel, and test covariance/rotation, conservation, native TRIADIC_CLOSURE_E, and future observer sufficiency on the actual source semantics. Formal CLAIM, Result, Driver review and P000 promotion are separate operations.
