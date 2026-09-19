# BRC–Shor: executable partial-return certificates

Event-ID: brc-shor-partial-return-block-20260919-6EF011
Researcher-ID: EM-DIRECT-6EF011
Research-Activity-ID: RA-6EF011C2E75C4A799606AFEA
Status: RESEARCH_CANDIDATE; proved elementary derivations and same-assistant finite checks; no independent review or admission.
Source read: enterprise-math@c62b1472db2e6ad90e988247f9590e2cf62957e1.
Inherited frontier: research_notes/brc_shor_adaptive_20260919_6EF011/ at 047232beaaa0058c19866dc3cf9b28bfba8a5b89.

## Result and exact scope

The previous five-position kernel theorem did not cheaply locate its unknown support. This continuation constructs a concrete block-exclusion observer: for a unit a modulo N, let P_T=product_{d=1}^T(a^d-1) modulo N and D_T=gcd(P_T,N). If r_p=ord_p(a), then D_T=1 iff T<min_{p|N}r_p. Proof: a prime divides the product iff it divides a term, equivalently its order is at most T. Thus a unit product excludes the entire interval of partial prime returns and all full returns. A proper gcd supplies a factor. A gcd equal to N requires refinement; it does not imply a full return.

Zero-divisor witness: modulo 21 with base 2, differences at exponents 2 and 3 are 3 and 7. Their product is zero, but neither difference is zero. The code preserves block identity, finds the first nonunit block, and checks at most B leaves within it. Its possible statuses are FACTOR, SYNCHRONIZED_RETURN (with an exact order but no primality inference), and BUDGET_EXHAUSTED.

This advances the factoring objective, NOT complete Shor probability simulation or a generally faster global-order algorithm. Candidate inputs are N,a and an explicit resource bound only; no factors, order oracle or CRT decomposition are supplied.

## Actual BRC/P023 reuse

Use the fixed-modulus result map gamma(x)=gcd(x,N). On divisors of N set g odot h=gcd(gh,N). Then gamma(xy)=gamma(x) odot gamma(y). Both sides have p-valuation min(v_p(N),v_p(x)+v_p(y)). This includes zero divisors and prime powers; modulo 9, 3 odot 3=9, so Boolean support alone is insufficient.

This is an exact T0_BRC result/provenance specialization and P023-T01 fiber-constancy application for future multiplicative block append and the gcd observer. It is NOT safe for arbitrary addition, base change, exact collision mass K_Q or locating an exponent from the gcd alone. Retain interval/generation parameters for reconstruction. Signed polynomial coefficients are arithmetic payloads, NOT signed BRC mass or quantum amplitudes. The old affine 28-moment carrier is not an occupancy oracle. No new general tool family or novelty is claimed.

## Cheap square-block construction

For B a power of two, define F_B(X)=product_{j=0}^{B-1}(X-a^j) over Z/NZ and V_i=F_B(a^{iB}), i=1..B. Then

product_i V_i = a^{B^2(B-1)/2} P_{B^2} modulo N.

Indeed iB-j covers 1..B^2 exactly once, and a^{iB}-a^j=a^j(a^{iB-j}-1). The prefactor is a unit, so gcds agree. Each V_i is a certificate for [(i-1)B+1,iB].

Construct F_{2s}(X)=F_s(X)q^s F_s(X/q), q=a^s, by coefficient scaling and one convolution. Evaluate at geometric points with ij=binom(i+j,2)-binom(i,2)-binom(j,2), reducing all B evaluations to one Hankel convolution. The only inverse is of a known power of a, never of a^k-1 or another potential zero divisor. Polynomial multiplication uses carry-safe integer packing with radix greater than min(s,t)(N-1)^2, followed by exact reduction. No floating point is used.

Doubling B tests horizons 1,4,16,... and stops with B<2sqrt(r_*), r_*=min r_p, apart from the trivial endpoint. Cost is a geometric sum of polynomial multiplication costs M_N(B) plus O(B) scalar modular/gcd operations. With an appropriate fast backend this is the classical soft-square-root q-factorial scale. Python bigint multiplication is not unit cost and is not asserted quasi-linear. Space is O(B) coefficients plus O(B(log N+log B)) packed bits, not five states.

## Fixed-base obstruction and random-unit bound

For square-free N, the first partial-return gcd equals the product of primes whose local order is minimal. If all local orders equal r, every gcd(a^u-a^v,N) is either 1 or N, according as r does not or does divide u-v. Products of such differences still cannot split N. This is a restricted-observer no-go, not a factoring lower bound. N=91, bases 16 and 17 have respective local orders (3,3) and (6,6); base 18 has (3,4) and returns factor 7. One adjacent base change need not repair synchrony.

For N=pq with distinct odd primes and uniform unit a, put g=gcd(p-1,q-1). Independence under CRT and the phi(d) count in a cyclic group give

Pr[local orders equal]=S(g)/((p-1)(q-1)), S(g)=sum_{d|g}phi(d)^2.

S is multiplicative and S(ell^e)=((ell-1)ell^{2e}+2)/(ell+1). Since g is even, S(g)<=g^2/2. Writing p-1=gu,q-1=gv gives coprime distinct u,v, hence uv>=2. Synchrony probability is at most 1/4, attained at p=3,q=5. Thus the first-partial-return route succeeds with probability at least 3/4 under these precise random-unit and sufficient-budget assumptions. This is a derivation, not a benchmark success rate or a novelty claim; it does not apply unqualified to fixed small bases or prime powers.

## Executed evidence

All finite comparisons passed: 560 exact convolutions; 560 geometric-evaluation batches/38,089 points; 25,765 block grids; 14,725 unit first-return cases; 9,365 input-gcd cases; 338,349 gcd-monoid checks; 91 exact odd-prime-pair probability counts; 1,800 synchronized difference checks; one resource-bound case and six invalid inputs. The candidate AST contains no float literal, true division or SymPy import. Tests use independent computational reference paths but were authored and executed by the same assistant. No full-repository or Lean verification was run.

23 selected examples were benchmarked in isolated workers. Five repetitions per method, except three for the 64-bit case; median core wall times, GC before each repeat and alternating method order, no CPU pinning. All postchecks passed using reference factors/orders imported after candidate runs. Old order runs were skipped above 40 bits; rho was skipped for the prime example 71. Interrupted orchestration resumed completed saved rows; interrupted unfinished repetitions are not evidence.

Median milliseconds, old complete order / new factor / classical rho factor:
- N=10002200057,a=2: 167.222245 / 4.884970 / 0.193985.
- N=1000036000099,a=5: 1169.870388 / 12.202917 / 0.212983.
- N=1000000016000000063,a=2: not run / 876.225535 / 8.509593.
- N=18446743979220271189,a=2: not run / 8600.690267 / 30.890643.

For N=1000036000099,a=5, factor 1000003 appears at exponent 1000002 with B=1024; postchecked full order is 166672333344. For the 64-bit example, factor 4294967279 appears at exponent 2147483639 with B=65536 and cofactor 4294967291. Two billion exponents were not individually enumerated. However the polynomial work is substantial: this implementation does not outperform the tested Brent-Pollard rho factor baseline. Comparing a weaker factor output with complete order is not an equal-output speedup claim.

## Prior art

Fast q-factorial construction belongs to the classical geometric BSGS family: Bostan and Yurkevich, arXiv:2012.08656. Strassen-scale factoring and improvements are discussed in Hittmeir, arXiv:1608.08766; the resulting N^(1/4)-type scale is not a new record. The direct-factor baseline is Brent's 1980 improvement to Pollard rho, BIT 20, 176-184. None is attributed to BRC as a newly invented general algorithm. Bounded repository search does not prove exhaustive novelty.

## Persistence limits and resumable artifacts

The GitHub.create_blob call carrying block_engine.py was blocked by the platform with "couldn't determine the safety status of the request"; no blob or commit was returned. That blocked code request was not encoded or rerouted to evade the block. This separate text checkpoint preserves derivations and observed results only. Code/full raw results remain in the current delivered research package; their repository publication is PENDING. Do not claim code publication or a complete executable handoff from this note alone.

Local artifact SHA256:
- block_engine.py: 90dc8af383b571408280da0d625f9d22efcf6646f367152fb47f07926b058a82
- verify.py: 79337ed93aafa6a2fa51f37c996cbfbfde1a6a5f644ccef6e50169b1b5283084
- bench_worker.py: b627d88da485bfb116e2d9599c54bc77324fabd601e48daee4745d7949333318
- benchmark.py: e330ff1011284fdd6728d22602d49e9f983b2437650d68d194ff0572874d61b7
- full RESEARCH_NOTE.md: edcfffbcdbc2d810e64068c7192472509cbbfb7ed2e9413530aec6236a3a8540
- verification_results.json: d2d8b38ba5b32a7f0f3e8ac635ce992d2b6a01534cfb4a794a4e86e9b923b13f
- benchmark_results.json: 9ff1f31061f24796c4f48d2eebdc1afe75a016215ec67801f2e5ac9cb1f314f7

Next mathematical unit: a factor-blind nonuniform exponent/base schedule with total certificate-construction cost compared against rho and q-factorial baselines. Charge for constructing and selecting the schedule, not just representing the answer. Original global-order/unknown-five-position problem remains open in this work; retain the useful partial-factor exit and fixed-base no-go without repeating completed old experiments.
