# D25/LIFT R22 — Sharp p³ companion-only tail and a reflected finite certificate

Date: 2026-10-27. Requested independent TASK_RESEARCH logical lane: chatgpt-research-hourly-enterprise-math-20260923 (not CONTROL_PLANE_MAINTENANCE). Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Parent D25/LIFT/JT2 OPEN.

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** No native claim/open/checkpoint, no original-class CM experiment, no Result, no independent Driver review.

## Exact question, prior work consumed, observer types

Consume rather than recredit the separate on-hour author note 20261027_onhour_d25_guo_zudilin_companion_bridge_precision_gate.md and its prior-art finding. Guo and Zudilin, *A q-microscope for supercongruences*, Adv. Math. 346 (2019), 329–358 (arXiv:1803.01830), proved a p³ supercongruence for the distinct *S* weighted sum. Their theorem is not an equality between W and S. This R22 unit does not reproduce the earlier bounded full-sum census or R13/R15/R17/R20/R21 genuine Clausen-Hasse source constructions.

For every prime p=6m+1>=7, work in R=Z_(p) and define the source-distinct finite summands

~~~
w_k = (6k+1) C(2k,k)^2 C(3k,k) / 216^k,
s_k = (8k+1) C(4k,2k) C(2k,k)^2 / 2304^k,
W_p = SUM_(k=0..p-1) w_k,   S_p = SUM_(k=0..p-1) s_k.
~~~

The original D25 target only requires p==13 or 19 (mod24), a subset of p=6m+1. Both weights and denominators stay exactly as declared; neither summand is a finite Hasse face nor native Frobenius. The new narrow question is to identify the contribution in S that survives at third-digit precision after the corresponding W summands have already vanished.

## Theorem 1 — different exact valuation gates and third-digit transfer criterion

Put K=4m, H=floor((3p-1)/4), and define

~~~
D_p = SUM_(k=0..K) (w_k-s_k),
T_p = SUM_(k=K+1..H) (s_k/p²)  (mod p).
~~~

The termwise division by p² is in R, so T_p is well-defined. Then, for every prime in scope,

~~~
W_p-S_p == D_p-p²*T_p                 (mod p³).        [1]
W_p==S_p (mod p³) iff D_p==p²*T_p   (mod p³).        [2]
~~~

**Proof.** For all 0<=k<p, the integer binomial products are exactly

~~~
C(2k,k)^2 C(3k,k) = (2k)!(3k)!/(k!)^5,
C(4k,2k) C(2k,k)^2 = (4k)!/(k!)^4.
~~~

By Legendre's formula their p-valuations are respectively floor(2k/p)+floor(3k/p) and floor(4k/p). A possible p-factor in 6k+1 or 8k+1 raises these valuations; it cannot lower them. Therefore all w_k with k>=ceil(2p/3)=4m+1 vanish modulo p³. All s_k with k>=ceil(3p/4)=H+1 vanish modulo p³. For the *different* intervening interval K+1<=k<=H, each unweighted S integer product has valuation exactly two, so its weighted term is divisible by p². Splitting the two original finite sums at these exact support thresholds proves [1] and [2]. This does not rely on an unproved supercongruence or an analytic infinite-series transformation. QED.

## Theorem 2 — two source-faithful finite forms of the unmatched S-only tail

For K+1<=k<=H, 2p<=4k<3p. Removing the two factors p and 2p from (4k)!, with two complete (p-1)! blocks, gives by Wilson

~~~
(4k)!/p² == 2(4k-2p)!                         (mod p).
T_p == 2 SUM_(k=4m+1..H)
       (8k+1)(4k-2p)! / [(k!)^4 2304^k]      (mod p).   [3]
~~~

Now apply the invertible *index reversal* j=p-1-k. The interval becomes J_m={floor(3m/2),...,2m-1}. Write b_j=4j-6m+2. Every b_j is even with 0<=b_j<p and 4k-2p=p-1-b_j, so

~~~
(4k-2p)! == -1/b_j!      (mod p),
k! == (-1)^(j+1)/j!       (mod p),
2304^(-k) == 2304^j      (mod p),
8k+1 == -(8j+7)          (mod p).
~~~

After substitution all signs cancel, giving a shorter complementary *exact* certificate

~~~
T_p == 2 SUM_(j=floor(3m/2)..2m-1)
       (8j+7) 2304^j (j!)^4 / (4j-6m+2)!   (mod p).   [4]
~~~

All displayed factorial denominators are p-units. The map (k,S-source) <-> (j,reflected S-source) is bijective. It does not create a missing W source, a positive-infinity Clausen source, or a high/high-sector identity. Equations [3]–[4] are algebraically valid for every declared prime, whether or not the open congruence [2] holds. QED.

## Exact independent computations and a target-class exception

The companion Python standard-library checker computes each T_p by three independent arithmetic routes: actual huge-integer binomials modulo p³ with checked p² divisibility, normalized factorials modulo p, and Wilson-reflected factorials. **All three agree for all 80 primes p=6m+1, 7<=p<=997.** It separately recomputes the full W and S weighted sums from two distinct modular coefficient recurrences and checks [1] on 14 explicitly selected primes. For those 14, W==S==p modp³ was observed; this finite sample does not prove the universal bridge.

| p | unmatched S-only k | reflected j | T_p modp | independently computed D_p modp³ |
| ---: | --- | --- | ---: | ---: |
| 13 | 9 | 3 | 6 | 1014 |
| 19 | 13..14 | 4..5 | 16 | 5776 |
| **181** | 121..135 | 45..59 | **0** | **0** |
| 373 | 249..279 | 93..123 | 281 | 39095249 |
| 733 | 489..549 | 183..243 | 559 | 300344551 |

The explicit *exception* p=181 belongs to the original hard target class p==13 (mod24). Its 15 individually computed j=45..59 summands in [4] equal

~~~
[43,173,88,67,34,134,74,30,63,82,129,143,141,118,129]
~~~

modulo 181, whose integer sum is 1448=8*181. Thus T_181=0 even though these 15 true S-only source contributions are nonzero. The companion core D_181 also vanishes mod181³ in the separately executed full-sum check. A blanket nonvanishing/no-go for T_p on the target class would be **false**. Among the finite 80-prime scan, only p=181 had T_p=0; this is **not** a classification of all primes.

Executable author evidence: research_notes/portable_direct/20261027_hourly_d25_ws_extra_tail_valfiltration_r22_check.py. Executed PASS: 80 independent triple-route tail cases, 14 full weighted-sum recurrence cases. General theorems derive from valuation and Wilson proofs, not finite extrapolation. No floats, custom axioms, admit, sorry or native CM checks; this is not independent mathematical admission.

**BRC / Enterprise residual fidelity (COMPOSE_APPLIED).** The preserved typed state contains both summand families, original finite cutoff, discrete k and reflected j with their mapping, rational p-unit denominators, p²/p³ filtration, source provenance and subsequent comparison observer D_p-p²T_p. Aggregating W and S to an equal observed total erases a genuinely nonzero S-only subport at p=13,19,373,733; the vanishing at p=181 is likewise observer-specific, not a justification to discard source labels. These arithmetic indices are not six native Enterprise spatial axes; P000/worldview remains fixed.

## Continuation package — exactly what remains

The full all-prime matching obligation [2] is OPEN; this note proves a smaller exact witness interface, *not* its cancellation. Next executable portable subunit: seek a true finite WZ/hypergeometric telescoper, or a rigorously controlled p³ identity, transferring the core differences w_k-s_k (k<=4m) to precisely the reflected S-only right side [4] for every p==13 or 19 (mod24). Preserve the sharp p=181 cancellation case rather than assuming the unmatched tail never vanishes. Keep the separate R20/R21 six genuine Hasse source labels, original scalar, two finite faces per sign, positive-infinity and high/high sectors as independent ports until a proof supplies their transfer maps.

Independent native original-class H0/B0 divided-power module, [X]U mod p², Frobenius eta/kappa, Delta_p-R_p, p=373 native experiment and independent review are NOT_DONE. No formal Result/freeze or claim of D25/JT2 closure. Scientific Source pin is unchanged.

Existing read-only genuine Research-lane recovery #6571: service session MCP-3a7c6c3a67bd4e52b1cdf49064751829, no pending request/current own CLAIM/open run/unpublished upload, two protected neutral staging dispositions. Complete continuation #6572/#6573/#6574: SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED, NO_LIVE_CLAIM, NEEDS_DISPATCH, execution_authorized=false, historical predecessor-claim pointer mismatch. Current native em_status is 0.6.11 / research_authority_granted=false. This portable GitHub evidence cannot replace native checkpoint or grant an old role identity. Control restoration remains with existing enterprise-math#1558; role-activity registration for this increment remains REGISTER_PENDING/SYNC_DEBT until separately verified. Do not mutate old session/staging or maintenance lane. Mother objective OPEN.
