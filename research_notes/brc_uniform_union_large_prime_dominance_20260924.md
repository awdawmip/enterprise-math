# BRC uniform-union large-prime dominance theorem

Status: `PROVED_DERIVATION / PORTABLE_RESEARCH_NOTE / NOT_A_RESULT / NOT_A_REVIEW / NOT_A_SOURCE_CHECKPOINT / UNREVIEWED`

Research-Activity-ID: `RA-7173A2B0D2B62B10023DBFFB`

Task context: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SUPERSINGULAR-UNIT-RECIPROCITY`

Formal D24/UR ownership is unchanged. This note is an auxiliary portable theorem while the lawful successor-session path remains blocked by control issue #1511. It does not start LIFT/JT2 and grants no CLAIM, OPEN, Result, review, Working Truth, or mathematical acceptance.

## Exact carrier

For target primes `p ≡ 13,19 (mod 24)`, keep

`X_j=-((1+4^j)/j) p^(2j) H_{2j}`,

`epsilon_p(j)=0 iff (p-1)|2j, else 1`,

`eta_p(j)=v_p((1+4^j)/j)`,

`beta_p(j)=2j+epsilon_p(j)+eta_p(j)`,

and monomial valuation weight

`W_p(m)=sum_j m_j beta_p(j)-sum_j v_p(m_j!)`.

For the conservative generic branch put

`beta_infty(j)=2j+1`,

`W_infty(m)=sum_j m_j(2j+1)`.

Define the retained supports at observer horizon `N` by

`M_p(N)={m: W_p(m)<N}`,

`M_infty(N)={m: W_infty(m)<N}`.

## Theorem — only primes p <= N can enlarge the uniform sufficient carrier

For every integer `N>=3` and every target prime `p>N`,

`M_p(N) subseteq M_infty(N)`.

Consequently

`union_{target p} M_p(N) = M_infty(N) union union_{target p<=N} M_p(N)`.

Thus a uniform sufficient compiler at precision `p^N` needs special branches only for target primes `p<=N`. A larger target prime may still **prune** generic monomials through source-coefficient cancellation, so its exact-per-prime support can remain different; it simply cannot add a monomial absent from the generic carrier.

### Proof

Start from

`beta_p(j)=2j+epsilon_p(j)+v_p(1+4^j)-v_p(j) >= 2j-v_p(j)`.

Suppose a retained monomial used some `j>=p`. Since `v_p(j)<=j/p`, one copy already has

`beta_p(j) >= 2j-j/p >= 2p-1`.

For multiplicity `a>=1`, factorial correction satisfies

`v_p(a!) <= a/(p-1)`.

Hence the total contribution of this port is at least

`a(2p-1)-a/(p-1) > p > N`,

so no retained monomial can use any `j>=p`.

Therefore every support index has `j<p` and `v_p(j)=0`.

Next suppose `2j>=p-1`. The smallest possibility is the harmonic endpoint `j=(p-1)/2`. There `4^j=2^(p-1)=1 (mod p)`, so `p` does not divide `1+4^j`, and

`beta_p((p-1)/2)=p-1>=N`

because `p>N` and both are integers. Larger `j` have still greater lower bound. Thus every retained support index satisfies

`2j<p-1`.

On this range the harmonic endpoint flag is absent, so `epsilon_p(j)=1`, and therefore

`beta_p(j)=2j+1+v_p(1+4^j) >= 2j+1 = beta_infty(j)`.

It remains only to exclude a factorial lowering caused by very large multiplicity. If some multiplicity `a>=p`, then every retained port has `beta_p(j)>=3`, and

`a beta_p(j)-v_p(a!) >= 3a-a/(p-1) > p > N`.

Therefore every retained multiplicity is `<p`, so all factorial corrections vanish. Hence, for every `m in M_p(N)`,

`W_p(m) >= W_infty(m)`.

Since `W_p(m)<N`, we obtain `W_infty(m)<N`, proving

`M_p(N) subseteq M_infty(N)`.

Taking the union over all target primes gives the stated finite-branch reduction.

## Sharpness

The threshold `p>N` cannot be replaced by `p>=N`. At `N=p`, the endpoint

`j=(p-1)/2`

has actual weight `beta_p(j)=p-1<N`, while the generic weight is

`beta_infty(j)=p=N`.

Thus `M_p(p)` contains a monomial that the generic carrier drops. The boundary is exact.

## BRC interpretation

Population: target primes `p ≡ 13,19 (mod24)` and valuation-partition monomials.

Observer 1 — `UNIFORM_SUFFICIENT_MOD_p^N`: only whether a monomial must be retained in the union needed to cover every target prime. For this observer, every fiber `p>N` factors through the generic branch because `M_p(N) subseteq M_infty(N)`. Collapsing all such branch identities to generic is a **proved safe quotient**.

Observer 2 — `EXACT_PER_PRIME_SUPPORT`: the exact branch support for a specified prime. This observer may still see source-coefficient cancellation at large class-13 primes, which can prune generic ports. Therefore the prime identity and `eta_p(j)` provenance cannot be erased for this observer.

The theorem is therefore an observer-dependent compression statement, not permission to discard coefficient-cancellation provenance globally.

## Exact regression / falsification

Checker: `research_checks/check_brc_uniform_union_large_prime_dominance_20260924.py`.

The exact finite checker evaluated every even horizon

`N in {12,14,...,40}`

and every target prime `p<=200`. For each `p>N` it verified `M_p(N) subseteq M_infty(N)` and verified that the full finite union equals `generic union branches(p<=N)`.

Key output:

`{'horizons_checked': [12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40], 'target_prime_limit': 200, 'N30_union': 265, 'N32': {'generic': 340, 'p13': 320, 'p19': 343, 'reduced_union': 348, 'large_branches_subset_generic': {37: True, 43: True, 61: True}}, 'N34_union': 465, 'sharpness_equalities': [13, 19, 37]}`.

Finite regression is not the proof. The proof is the exact valuation argument above.

## Consequence for the current N=32 compiler

The previously computed N=32 exact branch counts remain valid, including the distinct p=37,43,61 pruning behavior. But for the **uniform sufficient union**, those three large-prime branches are redundant:

`M_37(32), M_43(32), M_61(32) subseteq M_infty(32)`.

Hence the 348-monomial N=32 union can be generated exactly from only

`generic + p=13 + p=19`.

This separates two jobs that should no longer be conflated:

1. uniform carrier generation — finite exceptional branches `p<=N` only;
2. exact branch diagnostics — retain all requested prime identities and cancellation provenance.

The same theorem shows that at N=34 the only target primes capable of enlarging the generic union are again `13` and `19`; the exact checker gives uniform union size `465`.

## Do not repeat / next

Do not re-enumerate large target primes merely to decide the uniform union at a fixed N. Use the theorem to generate the union from generic plus target primes `<=N`, then use larger-prime branches only when the scientific observer actually asks for exact-per-prime pruning or coefficient-cancellation structure.

Formal priority remains unchanged: if #1511 gains a real deployed lossless service-session rollover/disposition operation, stop auxiliary precision work and resume the Source-native D24 frontier through lawful successor identity -> `continuation_prepare` -> CLAIM -> OPEN -> truthful checkpoint/readback -> UR/JT0 Result/freeze -> independent Driver review. Otherwise any further portable work should build on this reduction rather than brute-force all prime branches.
