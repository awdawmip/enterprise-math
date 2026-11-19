# QFT-LP | Conditional peak-to-order bridge with correlated multi-samples (author derivation)

Task: RS-QFT-NATIVE-MULTISAMPLE-DECODING-20261002
Scope: Mathematical, conditional decoding lemma for the pinned native task; no native positive-family assertion, no simulation, no Result/review/admission.
Authors: EM-X6-C7A253 (current own session).
Taskbook pin: enterprise-math@47ed582ec280ad4dbcc5195ff2831fe72e6cae54, research_tasks/RS-QFT-NATIVE-MULTISAMPLE-DECODING-20261002.md.
Prior pinned context: QFT single-walker source@951cc16cb09635fae9f93230d96030fdaa2035b3 and RP3@d5e5ff75902240b9cbdefde7eb221567d3c31c95; RP7@07bab8333ff49b33fcca51693c0f1c7ab27a1d5c.
Status: AUTHOR_SYMBOLIC_DERIVATION / UNREVIEWED / NOT_ADMITTED.

## Exact statement

Let odd N >= 3, gcd(a,N)=1, r=ord_N(a)>=2, n=ceil(log2 N), and choose the **public** s in {1,2,4}, L=n+ceil(n/s), Q=2^L, B=floor(sqrt(Q)). For this *restricted conditional lemma* suppose r < sqrt(Q). No algorithm is supplied r as input.

For k in {0,...,r-1}, let z_k be a deterministically tie-broken nearest integer to Q*k/r. These are distinct integers in {0,...,Q-1}. For m>=2 actual native output registers Y_1,...,Y_m (with the full signed native state, bank, residuals, time-ordered feedback and reset semantics of the pinned model) may be correlated. Assume an as-yet-unproved **native conditional peak floor**: for some 0<lambda<=1, every i, every positive-probability previous output history h=(y_1,...,y_{i-1}), and every k,
    
    Pr_native(Y_i=z_k | h) >= lambda/r.              (A)

Then a deterministic, public-input polynomial-time postprocessor given each Y_i recovers at most one reduced rational u_i/d_i with 1<=d_i<=B and

    |Y_i/Q - u_i/d_i| <= 1/(2Q),                       (B)

by continued fractions plus an exact rational error test, or reports no candidate. Put R=lcm(d_1,...,d_m) if each candidate exists. The probability that R equals the exact order r is at least

    lambda^m * product_{p prime, p|r} (1 - p^{-m})
      >= lambda^m / zeta(m).                          (C)

The bound remains valid for correlated native samples because (A) is history-conditional, rather than a marginal or independence assertion. Its m=2 specialization is lambda^2/zeta(2).

For s=1, Q=2^(2n), r<N<=2^n, so the size hypothesis holds for every such (N,a). For s>1 the size hypothesis only covers orders r<2^(L/2); the statement is not a general short-register decoder.

## Proof, rational reconstruction

Since Q>r^2 and r>=2, distinct phase centers Q*k/r are separated by Q/r>r>=2; nearest-integer peaks z_k are distinct and within register bounds. For a peak Y=z_k, put g=gcd(k,r), u=k/g, d=r/g (k=0 gives 0/1). Then d<=r<sqrt(Q) and |Y/Q-u/d|<=1/(2Q)<1/(2d^2). By the standard exact continued-fraction rational approximation criterion, u/d is a convergent of the rational Y/Q; it can be enumerated in O(poly(L)) arithmetic bit operations and checked against (B).

Uniqueness among reduced fractions with denominator<=B follows because any two distinct reduced fractions u/d,u'/d' in that range have separation at least 1/(d*d')>=1/B^2>=1/Q. If both passed (B), separation would be at most 1/Q. Equality would require Q=B^2, d=d'=B and |u*d'-u'*d|=1. With d=d'=B>=2 the latter difference is divisible by B, contradiction. Thus every native peak Y=z_k yields precisely d=r/gcd(k,r).

For an ordered k-tuple, these d_i obey
    lcm_i(r/gcd(r,k_i)) = r / gcd(r,k_1,...,k_m).
This is the per-prime valuation identity. Thus R=r exactly when gcd(r,k_1,...,k_m)=1. By the chain rule and (A), for each ordered peak tuple, the probability of Y_i=z_(k_i) for every i is >=(lambda/r)^m. Different tuples specify disjoint output events. The Chinese remainder theorem counts exactly r^m*product_(p|r)(1-p^-m) ordered tuples with gcd=1. Summing proves (C). The bound by zeta(m) is the elementary Euler-product comparison for m>=2.

## Authentication, resource accounting and scope

A modular check a^R mod N=1 certifies that R is a multiple of r, but alone does NOT certify its minimality for arbitrary non-peak inputs. Equation (C) bounds the **actual equality event R=r**, not the reliability of the predicate a^R=1 as a self-certifying exact-order flag. If a certified exact order is required for every accepted output, a prime-divisor minimality check after a validated factorization of R (verify a^(R/p) !=1 for each distinct p|R) is needed; factorization or equivalent certification costs must be charged, never hidden as free.

Postprocessing (continued-fraction candidate generation, exact error tests, LCM and one modular exponentiation) costs poly(m,L,log N) bit operations, but the m actual native samples, the proof/cost of a bank at growing n, the certificate for lambda and any minimality certificate have SEPARATE costs. A polynomial native order decoder requires those costs bounded and lambda not too small. With independent fresh full resets between whole m-sample batches, the proven favorable-event probability provides a geometric repeat bound; without such resets it does not.

## Concrete missing native bridge

Neither the pinned row-query theorem nor the RP3/RP7 same-bank TV/error statements prove (A) for the exact low-precision native instrument. They also do not supply a constructive unbounded native input family with QFT phase peaks and a verified lambda, or a general favorable-event density when r>=sqrt(Q).

A discriminating next unit is to derive actual native conditional probabilities Pr(Y_i=z_k|h) for at least a publicly recognizable input family under the fixed source bank and full signed BRC process; exhibit and certify a uniform lower bound or a precise (N,a,s,k,h) zero-mass witness. A failed (A) would refute this *particular* sufficient condition for that input, not every possible joint decoder. The source's independent sample-coupling assumptions should be kept explicit.

This result is a reusable **conditional decoding bridge**, not the required positive native infinite-family theorem or a classical polynomial Shor algorithm. No ideal QFT numerical reference was run.
