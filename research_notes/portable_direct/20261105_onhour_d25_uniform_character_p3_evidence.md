# D25 SECOND-DIGIT-LIFT: uniform character test and exact all-prime cutoff
Date: 2026-11-05. Scientific source pin: c47e13e4aba0e006366f989d6334d443f6333ae3.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, TP2-B6F4FC938FF94941C1B7.
Research logical conversation: chatgpt-research-onhour-enterprise-math-20260923.
Evidence type: EXACT VALUATION LEMMA + FINITE EXACT COMPUTATION; AUTHOR-SIDE; UNREVIEWED / NOT_ADMITTED.
Predecessor author-side frontier: 3537262a71d7cc40442326bf07fdee17375850fc; original frozen R_p = signed Clausen T_p established there.

## Exact original input and tested generalization
Let a_k = binom(2k,k)^2 binom(3k,k)/216^k = (1/2)_k(1/3)_k(2/3)_k/[2^k(k!)^3], and W_p = sum(k=0..p-1) (6k+1)a_k.
New tested stronger hypothesis: for every prime p>3,
    W_p ≡ p * (-3/p)   (mod p^3),
where (-3/p) is the quadratic character, equal to +1 for p=1 mod3 and -1 for p=2 mod3. The frozen mother target p=13,19 mod24 is a subset of the +1 case. This is a computational hypothesis, not a proof or novelty claim. Nearby techniques: Guo/Zudilin arXiv:1803.01830 and Wang/Hu arXiv:2010.13638. An exact-match prior-art check remains open.

## Proven valuation partition
For every p>3, k<p, 2 and k! are p-adic units. Each of (1/2)_k, (1/3)_k, (2/3)_k contains exactly one p-multiple at or beyond its class-specific threshold. For p=6n+1 their thresholds (the first k after the factor enters) are 2n+1, 3n+1, 4n+1, giving v_p(a_k)=0,1,2,3 respectively on k≤2n, 2n<k≤3n, 3n<k≤4n, 4n<k≤6n. For p=6n+5 the thresholds are 2n+2, 3n+3, 4n+4, giving v_p(a_k)=0,1,2,3 respectively on k≤2n+1, 2n+1<k≤3n+2, 3n+2<k≤4n+3, 4n+3<k≤6n+4. The first p-multiple can be p or 2p and has valuation exactly one. Since (6k+1) is integral, the final tier contributes zero modulo p^3. Therefore FOR ALL primes p>3 (no hypothesis):
    W_p ≡ sum(k=0..floor((2p-1)/3)) (6k+1)a_k (mod p^3).
This is an exact finite reduction; it preserves numerator, signed weighting, order and p-valuation observers of the original 216 model.

## Exact executed computation
The checker d25_uniform_character_scan_20261105.cpp evaluates the original full p-term W modulo p^4 by exact integer modular arithmetic (128-bit products and Euclidean modular inverses), with recurrence
    a_0=1, a_(k+1)=a_k*(2k+1)*(3k+1)*(3k+2)/[36*(k+1)^3].
It enumerated ALL 1227 primes 5≤p≤10000 via a sieve: 611 p=1 mod6 and 616 p=5 mod6. ZERO violations of the p^3 character hypothesis; ZERO violations of the p^3 valuation cutoff.
Independent original-binomial Python code d25_uniform_character_independent_20261105.py checked all 166 primes 5≤p≤997, matching each W mod p^4 and half truncation mod p^3, zero mismatches.
Fourth-digit c_p=[W_p - p*(-3/p)]/p^3 modp (defined after the exactly checked divisibility) is nonzero for EACH of the 1226 primes 7≤p≤10000. At p=5 it is zero, and W_5+5 is divisible by 5^4 but not 5^5. Numerical examples (p, p mod6, W modp^3, c_p):
(5,5,120,0), (7,1,7,1), (11,5,1320,2), (13,1,13,9), (17,5,4896,8), (19,1,19,12), (139,1,139,71), (373,1,373,228), (1009,1,1009,693), (9973,1,9973,2244).
These finite computations provide broad exact evidence, not a proof of the all-prime character congruence. Exact full CSV and original source are in run evidence.

## Next precise research action
Attempt a p-dependent terminating WZ / creative-microscoping certificate for the character congruence, preserving signed original finite boundaries at floor((2p-1)/3). If successful, specialize +1 to the frozen p=13,19 mod24 target and use already established original R=T to derive Delta-R=0. If not, continue the frozen target without turning this enlarged hypothesis into a gate.
The native p=373 original H0/B0 divided-power [X]U mod139129, semilinear Frobenius, eta/kappa and independent audit remain the separate #1559 benchmark, not executed by this author-side scalar scan. Source continuation onhour11-20261105-1405-d25-cont: SUCCEEDED, execution_authorized=false; no native claim/run/checkpoint/admitted Result.
