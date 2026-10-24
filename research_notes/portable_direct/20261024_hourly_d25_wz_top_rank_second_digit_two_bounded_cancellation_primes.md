# D25/LIFT — two finite-range cancellation primes for the complete original WZ top-rank second digit

2026-10-24 | TASK_RESEARCH portable exact-arithmetic computation and independent source-factorial residue reconstruction. **UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**. This is a bounded finite certificate, not an all-prime classification, independent Driver review, or the original LIFT congruence.

**Bound provenance.** Mother RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific Source c47e13e4aba0e006366f989d6334d443f6333ae3. Research logical lane chatgpt-research-hourly-enterprise-math-20260923 is not the maintenance lane. The previous new algebraic theorem, without re-crediting its proof, is the exact source-preserved prime-only identity in 20261024_hourly_d25_wz_four_tail_unit_second_digit_fermat_closure.md:
\[
\frac{S_{m+1}-S_m}{p}\equiv\frac23+p\,c_p\pmod{p^2},\qquad
c_p=q_p(3)-\frac43q_p(2)-\frac{233173}{3942400}\in\mathbb Z_{(p)}
\]
for **prime** p=6m+1>=13; q_p(a)=(a^(p-1)-1)/p. The genuine S has the original source WZ factorial and its actual four new-rank tails. The operation changes rank at fixed p, not the prime parameter.

## Exact bounded result

**Finite computation certificate.** Among all **20,732 primes** 13<=p<=500000 with p≡1 mod6, exactly
\[
\boxed{p=1423,\ 5827}
\]
satisfy \(c_p\equiv0\bmod p\). The original D25 target prime classes \(p\bmod24\in\{13,19\}\) contain **10,412** primes in this bound; **only p=5827 (p mod24=19)** satisfies this cancellation criterion. Thus any proposed *universal nonvanishing of the complete WZ second-digit correction* is false even inside the original target-prime classes. This does **not** contradict or establish the original LIFT hard target: \(S_m\equiv p(4/3)^{p-1}\bmod p^3\) is a different original same-rank congruence.

The exact modular witnesses (all denominators are p-units) are:

| p | p mod24 | q_p(2) mod p | q_p(3) mod p | -233173/3942400 mod p | c_p mod p | (S_(m+1)-S_m)/p mod p² |
|---:|---:|---:|---:|---:|---:|---:|
| 1423 | 7 | 299 | 1147 | 1149 | 0 | 674977 = 2/3 mod 1423² |
| 5827 | 19 | 3373 | 1422 | 1133 | 0 | 11317977 = 2/3 mod 5827² |

**Independent original-factorial reconstruction of the two witnesses.** Compute the genuine old edge via its exact rational product \(U_mC(p)\) modulo p² (every product denominator is a p-unit) and *separately* compute each actual new WZ tail's p-free factorial unit \(E_j/p^2\bmod p\), without invoking the new closed formula for c_p or compressing the four distinct ports. This gives:

| p | original E0/p mod p² | four original E_j/p² mod p | total four tails mod p | old edge + p*tails mod p² |
|---:|---:|---|---:|---:|
| 1423 | 558291 | (951,1056,1378,966) | 82 | 674977 |
| 5827 | 30179976 | (3258,1037,3179,943) | 2590 | 11317977 |

The last column equals \(2\cdot3^{-1}\bmod p^2\) at both primes. This confirms the **same source port types** independently of the Fermat-quotient scan formula. The calculations preserve individual nonzero new-tail ports; the cancellation is between the old-edge correction and their aggregate at the declared additive observer, not disappearance of the labeled carrier.

## Reproducible exact finite scan

A sieve marks composites by their least encountered prime divisor. Modular exponentiation modulo p² computes q_p(2), q_p(3) mod p without constructing unbounded powers; the constant's denominator has prime factors only 2,5,7,11 and is invertible for every scanned p. There is no floating point and no unverified modular division.

~~~python
from math import isqrt, gcd

N=500000
prime=bytearray(b"\x01")*(N+1)
prime[0:2]=b"\x00\x00"
for d in range(2,isqrt(N)+1):
    if prime[d]:
        prime[d*d:N+1:d]=b"\x00"*((N-d*d)//d+1)

visited=0
target_visited=0
exceptions=[]
for p in range(13,N+1):
    if not prime[p] or p%6!=1:
        continue
    visited+=1
    target_visited+=(p%24 in (13,19))
    assert gcd(3942400,p)==1
    a=(pow(2,p-1,p*p)-1)//p
    b=(pow(3,p-1,p*p)-1)//p
    c=(b-4*pow(3,-1,p)*a
       -233173*pow(3942400,-1,p))%p
    if c==0:
        exceptions.append((p,p%24,a,b))
assert visited==20732
assert target_visited==10412
assert exceptions==[(1423,7,299,1147),(5827,19,3373,1422)]
print("bounded complete scan PASS")
~~~

The independent factorial reconstruction used (i) the original exact \(U_mC(p)\) product from the preceding genuine old-edge note, reducing each unit factor modulo p², and (ii) stripped p powers one integer at a time from each factorial in the original \(V_{m+1,4m+j}\) at j=1,...,4. For each j the numerator minus denominator p-valuation was **exactly two**; only after stripping did we invert the denominator modulo p, multiply by the authentic linear factor \(6p+6j+7\), and sum. Original WZ/FIVE and exact old-edge product were already proved; this is an independent *finite arithmetic check*, not a second universal proof or a native experimental run.

## Implication, BRC, and remaining problem

This is a new bounded search result that changes a useful obstruction: **the combined** top-rank second digit can vanish at p=5827 in the actual LIFT residue class, despite the original old-edge second digit and the four-tail aggregate having nonzero individual contributions. In particular, the older search of 100,000 primes for vanishing of the *old edge alone* is not contradicted; the observers are different.

BRC/Enterprise coordinates: **COMPOSE_APPLIED**. The carrier keeps prime, rank, signed p-free factorial units, old edge and four labeled new tails. The coarse additive observer vanishes in its second digit, but the portwise future operations need not vanish; this is an exact instance of observer-dependent cancellation without a new P000 axiom or an unsupported physical claim.

The scientific Source owner still requires a same-prime CM/divided-power representative, directed semilinear map, ordinary \(\omega+6\nabla_\lambda\omega\) first-jet normalization and same-class \(\kappa\) bridge, including actual [X]U mod p² and H0/B0 coefficients. This finite scan does not provide those missing Source-authenticated data. D25/LIFT remains OPEN. Work is **UNREVIEWED / NOT_ADMITTED**, native experiment NOT_RUN, independent review absent, no Source checkpoint. No scheduler, notification, ACTIVE worldview, owner or scientific Source pin change.
