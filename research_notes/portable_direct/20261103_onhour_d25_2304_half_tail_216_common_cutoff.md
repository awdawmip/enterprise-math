# D25 | Published 2304 half-cutoff cancellation and a common-cutoff 216 second-digit bridge (2026-11-03)

**Classification:** AUTHOR-DERIVED MATHEMATICAL CONSEQUENCES OF PUBLISHED THEOREM / EXACT FACTORIAL PROOF / FINITE INTEGER REPLAY; UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT. These author-side notes do not assert native Source task ownership, formal Result or H0/B0 execution.

**Authority/pin:** Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, immutable scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3, logical research lane chatgpt-research-onhour-enterprise-math-20260923 (distinct from maintenance). Parent author checkpoint 19fd9c5b465ddf7399070760b982d2bee839b545.

## Exact existing inputs and source attribution

Let p≡13 or19 (mod24), p prime, h=(p−1)/2, L=floor(2p/3), H=floor(3p/4). Preserve the original distinct weighted series

\[
a_k=(6k+1){\binom{2k}{k}}^2\binom{3k}{k}\,216^{-k},\quad W(N)=\sum_{k=0}^N a_k,
\]
\[
b_k=(8k+1)\binom{4k}{2k}{\binom{2k}{k}}^2\,2304^{-k},\quad S(N)=\sum_{k=0}^N b_k.
\]

All denominators are p-units; sums are in Z_(p). Guo and Zudilin, *A q-microscope for supercongruences*, Adv. Math. 346 (2019), arXiv:1803.01830, **prove both** S(p−1)≡p(−3/p) (mod p³) **and** S(h)≡p(−3/p) (mod p³). For our p≡1 (mod3), (−3/p)=+1. These two theorems are published inputs, not author-originated proofs. Existing D24 source-aligned first-digit result gives W(h)≡p (mod p²) for these primes; the mother goal is W(p−1)≡p (mod p³).

## Theorem A: exact cancellation of two 2304 p² source strips

The previous proof gives b_k divisible by p³ for k>H and a_k divisible by p³ for k>L. The difference of the two **published** S congruences yields, uniformly in the target classes,

\[
\sum_{k=h+1}^{H} b_k\equiv 0\pmod{p^3}.
\]

Each b_k on this band is divisible by p². Therefore the source-preserving p² observation has a finite-field cancellation law:

\[
\boxed{\sum_{k=h+1}^{L} \frac{b_k}{p^2}
+\sum_{k=L+1}^{H}\frac{b_k}{p^2}=0\pmod p.}
\]

Let M_p and T_p denote the first and second signed sums. Then M_p=−T_p (mod p). Crucially, individual terms are not zero: the equality is **signed cancellation** across a cutoff in two distinct source bands. For p=181 each band has sum zero separately, although all 15 terms in its upper strip are nonzero mod181. This is not an assertion of nonzero totals for all primes.

### A zero-safe unweighted factorial carrier

For every h<k≤H, write
\[
c_k=\frac{2(4k-2p)!}{(k!)^4\,2304^k}\pmod p,\quad
\frac{b_k}{p^2}=(8k+1)c_k\pmod p.
\]

The factorial formula follows from the two full p-blocks in (4k)! and Wilson: (4k)!/p²≡2(4k−2p)! mod p. Moreover for h<k<H,
\[
\boxed{c_{k+1}=c_k\,\frac{(4k+1)(4k+2)(4k+3)(4k+4)}
{2304\,(k+1)^4}\pmod p.}
\]
All recurrence denominators are units. Unlike the weighted ratio of b-terms, this **continues across** the internal index
\(r=(5p−1)/8\) for p≡13 (mod24), where 8r+1=5p and b_r/p²=0 but c_r≠0. For p≡19, the unique original weighted root \(r=(3p−1)/8\) occurs below h. This is a concrete BRC source/observer information-preservation benefit: the p² weight-zero observation need not delete the underlying nonzero carrier needed by subsequent recurrence.

## Theorem B: common-half-cutoff original 216 congruence

For every h<k≤L, v_p(a_k)=2 and Legendre/Wilson gives
\[
\boxed{\frac{a_k}{p^2}\equiv
(6k+1)\frac{(2k-p)!(3k-p)!}{216^k(k!)^5}\pmod p.}
\]
Both factorials (2k)! and (3k)! contain exactly one p-block, each contributing −1 after the p-division; their product contributes +1. Write A_p=Σ_{k=h+1}^{L}(a_k/p²) mod p. By the preceding source-valuation theorem,
\[
W(p−1)\equiv W(h)+p² A_p\pmod{p³}.
\]
Hence **exactly on the frozen D25 scope**, the still-open mother target is equivalent to
\[
\boxed{\frac{W(h)-p}{p²}\equiv -A_p\pmod p.}
\]
No 2304 half-tail boundary is needed in this expression because the published S(h)=p (mod p³); the original 216 intermediate band A_p must be retained. Equivalently, writing C_p=(W(h)−S(h))/p², one must prove C_p=−A_p mod p. This is a common-cutoff, source-typed alternative to the preceding D_p/p²=T_p. It changes the selected proof coordinates, not the task's hard target, weights, scientific pin or expected precision.

At p=373, the exact source digits are M_373=92, T_373=281, W-half digit=107, A_373=266, so 92+281=373 and 107+266=373. At p=13: M=7,T=6,W-half=3,A=10. At p=19: M=3,T=16,W-half=10,A=9. At p=181: M=T=0, W-half=29,A=152.

## Finite replay, method and remaining dependency

A new independent Python integer/binomial checker covers all 52 target primes p≤1200. It verifies original p³ values S(h)=S(H)=p and W(L)=p on this **finite domain**, both explicit factorial formulas, the zero-safe c recurrence, 2304 full upper-half signed cancellation, and the W-half/A balance. Finite checks support regression only; the uniform 2304 cancellation uses the cited **published** theorem, while the W-half/A equality is an equivalent form of D25 and remains unproved for all target primes.

BRC result COMPOSE_APPLIED: original source labels (216 vs 2304), ordered k, nonzero carrier c, exact signed weights, division by p², two cutoffs h,L,H and their future summation all retained. The 13-class weight-zero point offers a rigorous noninjective-observer witness: b_r/p²=0 with c_r≠0, so a proposed recurrence in the weighted quotient is singular, while the unweighted carrier is nonsingular. External p-adic arithmetic remains typed separately from native P000/X6.

**Next precise proof action:** obtain a terminating WZ/contiguous or CM-based certificate for the one-source signed equality \((W(h)-p)/p²=-A_p\), using the explicit A_p factorial port and the already published 2304 half-cutoff. Preserve the previous equivalent D_p/p²=T_p and p=181 independent cancellation witness as regression. Do not count this equivalence or bounded replay as solving it.

Native p373 original-class H0/B0 [X]U mod139129, module rank, semilinear eta and signed Green/Hesse/kappa independent replay still NOT_EXECUTED / PENDING_OWNER, existing support #1559. Source gateway Research authorization unavailable; historical request research-onhour-20261031-0205-dispatch-r15 remains CONTROL_REQUEST_NOT_FOUND. No Source session, CLAIM, run or formal checkpoint acquired; original three staging artifacts remain separate.
