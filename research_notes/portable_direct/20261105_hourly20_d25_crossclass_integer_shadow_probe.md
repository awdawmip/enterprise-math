# D25 complementary signed residues and terminating integer-shadow probe

Date: 2026-11-05; Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication: `TP2-B6F4FC938FF94941C1B7`; frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Logical Research conversation: `chatgpt-research-hourly-enterprise-math-20260923`. Status: AUTHOR FINITE EXACT CHECK / EXACT FIRST-DIGIT REDUCTION LEMMA / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CM.

## New finite signed-residue result

Define signed 216 and 2304 sums in Z_(p):
$
W_p=\sum_{k=0}^{p-1}(6k+1)\frac{(2k)!(3k)!}{216^k(k!)^5},\quad
V_p=\sum_{k=0}^{p-1}(8k+1)\frac{(4k)!}{2304^k(k!)^4}.
$
A fresh exact BigInt modular computation for **all 237 primes 5<=p<=1500** gives `W_p=V_p=p` modulo p^3 for 115 primes p=1 mod6 and `W_p=V_p=-p` modulo p^3 for 122 primes p=5 mod6; zero failures. The complementary p=5 mod6 sign sector is the new discrimination axis; p=1 mod6 overlaps prior author scans. The 2304 all-prime statement is previously known (Guo–Zudilin); these are finite checks of W216, not an all-prime W216 theorem.

## Proven exact first-digit reduction

For n>=1 define the integer
$
C_n=\sum_{k=0}^{2n}(6k+1)(-1)^k2^{2n-k}
\binom{2n}{k}\binom{3n}{k}\binom{4n}{k}.
$
For every prime p=6n+1, `W_p congruent 2^(-2n) C_n (mod p)`. Proof: the rational parameter tuple (1/2,1/3,2/3) equals (-3n+p/2,-2n+p/3,-4n+2p/3). At k<=2n, reduction modulo p of the hypergeometric coefficient yields `(-1/2)^k binom(3n,k)binom(2n,k)binom(4n,k)`. At k>2n the original (1/3)_k has a factor p/3, so its coefficient vanishes modulo p. All denominators are p-units. Multiplying by 6k+1 and summing proves the identity.

Direct exact integer-binomial recurrence verifies `C_n=0 (mod 6n+1)` for **every n=1..500, including composite 6n+1**, with no primality assumption in this finite experiment. A general integer divisibility theorem `(6n+1)|C_n` remains a conjecture, now an explicit one-parameter WZ search target.

## Why the p-adic jet is necessary

Write `S_n=2^(-2n) C_n` in Z[1/2]. Exact values are `S_2=-11843/8 = 104 (mod 13^2)` and `S_3=1299125/8 = 76 (mod 19^2)`. These are respectively 8*13 and 4*19 modulo p^2. The first-digit shadow by itself loses essential second-digit corrections. To advance the frozen scalar LIFT `Delta_p-R_p=0 mod p` (equivalent to `W_p=p mod p^3` under the existing author-aligned scalar bridge), calculate original p-adic parameter first/second jets and the valuation-one shell and compare with the existing independent on-hour lane's precise half-jet `K_p+Xi_2+C_A=0 mod p` target.

## Exact checker and recovery

This report's results were computed with BigInt integers and extended-Euclid modular inverses; verification summary `237 primes PASS (115+122); n=1..500 PASS; n=2 mod169=104; n=3 mod361=76`. Code publication planned as `research_notes/portable_direct/d25_crossclass_integer_shadow_exact_20261105.js` and should be separately read back; the report records the math regardless of code transport state.

As of 2026-11-05 16:35 +08: successful earlier Source read `em-h20-20261105-1520-current-continuation` gave Source `7649a210a8c61901f371ce4cca0842eab3bf6deb`, existing checkpoint `SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED`, no new claim/run and execution_authorized=false. New request `em-h20-20261105-1620-current-continuation` returned FAILED / `CANONICAL_REJECTED: unknown current immutable task publication`; do not replay without fresh contract and Source diagnosis. Preserve the Source-native checkpoint, all inherited contributor IDs, and native p373 H0/B0 [X]U mod139129 / eta / kappa / signed observer under open issue #1559. Do not confuse portable arithmetic with original-class native benchmark.

Next exact action: derive integer-shadow telescoping/WZ certificate for `(6n+1)|C_n`; more urgently derive its p-adic jets and test their signed original 216/2304 half-endpoint residual against the onhour `K+Xi_2+C_A` interface; maintain LIFT mother target and independently address native p373 benchmark.
