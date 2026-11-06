# D25 — Wieferich-linked outer-source fiber bifurcation (portable author result)

Date: 2026-11-06. TASK_RESEARCH, task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. AUTHOR-DERIVED / EXACT ALGEBRA AND FIXED-PRIME CERTIFICATES / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT. Neither a native H0/B0 nor a Frobenius experiment.

## Definitions

For a prime p=6m+1 >=7, define s=(2m,3m,4m), U_j(x)=(-1/2)^j * product_{i=1}^3 binom(s_i+x_i,j), and the signed, labelled-source observer W_p(v)=sum_{j=0}^{p-1}(6j+1)U_j(pv) mod p^3. The original 216-series parameter path is v*=(-1/3,-1/2,-2/3). Study the one-dimensional perturbation d=(1,0,1). All j! with j<p are p-adic units.

Let A_i=partial_i W_at_zero mod p^2, H_ik=partial_i partial_k W_at_zero mod p. Only for primes with the exact, independently verified *first-digit hypothesis* A_1+A_3=0 mod p, define
c_p=(H11+2H13+H33)/2 mod p,
k_p=(A1+A3)/p + v*^T H d mod p.
The quotient uses integer representatives of A1,A3 and is well-defined modulo p.

## Theorem 1 — exact diagonal collision polynomial

For every lambda in F_p under the displayed first-digit hypothesis,

W_p(v*+lambda d)-W_p(v*) = p^2*(k_p*lambda+c_p*lambda^2) (mod p^3).

PROOF: expand each integral binomial polynomial to second order, using p A·delta + p^2(v*^T H delta + (delta^T H delta)/2). Every omitted degree-three-or-higher term contains p^3; the first derivative contribution is p^2-divisible by hypothesis. Summing yields the equality. This is a symbolic finite algebra theorem, not an inferred fitting curve.

If c_p !=0, the scalar collision set within this fixed-middle-source diagonal is exactly {0,-k_p/c_p} when k_p !=0, and the singleton {0} when k_p=0. No conclusion about the whole three-source space is implied.

An independent labelled-source witness is (U_1(p(v*+lambda d))-U_1(pv*))/p = (3m/2)*lambda mod p, since s1+s3=p-1. Thus a nontrivial diagonal scalar collision can still change its labelled first term.

## Theorem 2 — exact prime-specific degeneracies

The undivided binomial/derivative recurrence gives:

p=1093 (p mod24=13): T=A modp=(291,914,802); A1=557721, A3=1173591 (mod p^2); (H11,H13,H33)=(509,883,340); (A1+A3)/p=491 and v*^THd=602 (modp). Hence k=0, c=761 !=0.

p=3511 (p mod24=7): T=(1594,566,1917); A1=2989455, A3=2902003 (mod p^2); (H11,H13,H33)=(1533,341,1299); (A1+A3)/p=1678 and v*^THd=1833. Hence k=0, c=1757 !=0.

Both satisfy T1+T3=0 modp. Therefore for ALL lambda in their respective prime fields:
W_1093(v*+lambda d)-W_1093(v*) = 1093^2*761*lambda^2 (mod 1093^3);
W_3511(v*+lambda d)-W_3511(v*) = 3511^2*1757*lambda^2 (mod 3511^3).

The zero-difference fiber on this line is exactly lambda=0 at both primes. This *fixed-prime result* is proved by the algebra theorem and exact modular certificates. An independent full p-term modular-binomial summation finds W_p(v*)=p mod p^3 for both primes and second-digit differences at lambda=1,2 of (761,858) and (1757,6), respectively. Their labelled j=1 first-digit differences at lambda=1,2 are (273,546) and (2633,1755).

## New finite conjecture evidence: base-2 Fermat quotient

Put q_p(2)=(2^(p-1)-1)/p modp. Every one of the 330 primes 7<=p<=5000 with p=1 mod6 passes both first-digit A1+A3=0 and

k_p = -3*q_p(2) (mod p),

and c_p !=0. Exactly 166 of these are in the target classes p=13,19 mod24. This is **FINITE CHECKED**, not universally proved. The only q_p(2)=0 cases in this tested domain are p=1093,3511, precisely the known base-2 Wieferich primes (the latter outside the target). Direct modular exponentiation verifies the defining congruence at both.

The outer first-digit rank is zero only at p=7,211 in this scan; the p=211 full two-dimensional 212-point conic/norm classification was already completed and is NOT repeated as a new result here. Among the 328 nonzero-rank outer cases, 326 have two diagonal collisions and 1093/3511 have only one. The conjectural Fermat-quotient identity would explain the exceptional fibers, conditional also on c_p!=0; no all-prime assertion is made.

Exact finite verification used two actually executed independent Python routes: undivided modular A/H jets for all 330 primes, and direct complete weighted sums at p=13,19,373,1093,3511 for lambda=0,1,2, including labelled j=1 differences. Runtimes used only invertible denominators 1..p-1 and -2. Companion scripts: d25_outer_fiber_strata_20261106.py and d25_wieferich_fiber_direct_20261106.py.

## Open dependency and Source boundary

Next exact science: find symbolic WZ/finite-transformation proof or counterexample to k_p=-3 q_p(2) and independently T1+T3=0; look for c_p=0 and outer-rank-zero primes beyond p<=5000. Preserve observer/source labels before any quotient. This auxiliary arithmetic does not discharge the frozen mother goal Delta_p-R_p=0 modp for p=13,19 mod24, its same-original-class p373 H0/B0 divided-power module, [X]U mod p^2, source semilinear Frobenius, eta, kappa or independent review.

Research logical ID: chatgpt-research-hourly-enterprise-math-20260923; maintenance logical ID chatgpt-hourly-enterprise-math-20260921 is not used. Existing native Source checkpoint not overwritten. Original read request IDs em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13 remain QUEUED after reconcile following EVENT_COLLECTION_IO, not an affirmative current Source packet. Current service advertises recovery_status and session_preserve_staging contracts, but connected callable tools for these operations are not exposed in this run; own old session/staging transition remains unresolved under enterprise-math#1558. No new native session/CLAIM/OPEN/checkpoint/review/freeze asserted.
