# D25 216–2304 transfer with six valuation strata (2026-11-07)

Research TASK_RESEARCH lane: `chatgpt-research-hourly-enterprise-math-20260923`; distinct from CONTROL_PLANE_MAINTENANCE. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen science `c47e13e4aba0e006366f989d6334d443f6333ae3`. AUTHOR-SIDE PROVED VALUATION THEOREM / EXACT FINITE / UNREVIEWED / NOT_ADMITTED.

## Independently sourced bridge

For p>3 prime and 0<=k<p define
```
A_k = binom(2k,k)^2 binom(3k,k)/216^k = (2k)!(3k)!/[216^k(k!)^5]
B_k = binom(4k,2k) binom(2k,k)^2/2304^k = (4k)!/[2304^k(k!)^4]
W_p = sum_(k=0)^(p-1) (6k+1)A_k; S_p = sum_(k=0)^(p-1) (8k+1)B_k.
```
Guo–Zudilin, *A q-microscope for supercongruences*, Advances in Mathematics 346 (2019) 329–358, DOI 10.1016/j.aim.2019.02.008, arXiv:1803.01830, rigorously proved `S_p = p*(-3/p) (mod p^3)` **for every p>3**. This is the 2304 series, not the 216 source. For the frozen classes p=13,19 (mod24), `(-3/p)=+1`. With the previously proved independent frozen Clausen/reflection bridge `Delta_p-R_p=(W_p-p)/p^2 (mod p)`, the frozen LIFT target is equivalent to the **OPEN** finite transformation `W_p=S_p (mod p^3)` on those classes. The 2304 theorem does not already prove this transfer.

## New exact theorem: six distinct source strata

By factorial valuations, `v_p(A_k)=floor(2k/p)+floor(3k/p)`, `v_p(B_k)=floor(4k/p)` (denominators p-units). For the intervals k/p in [0,1/4), [1/4,1/3), [1/3,1/2), [1/2,2/3), [2/3,3/4), [3/4,1), the exact UNWEIGHTED valuations (A,B) are (0,0), (0,1), (1,1), (2,2), (3,2), (3,3).

In I_p={integer k: ceil(2p/3)<=k<ceil(3p/4)}, nonempty for p>=7, `(6k+1)A_k=0 (mod p^3)` but `v_p((8k+1)B_k)=2`. The latter weight is a p-unit because the only possible multiple of p between 8(2p/3)+1 and 8(3p/4)+1 is 6p, excluded by parity. Put r=4k-2p with 0<=r<p. Wilson's theorem gives `(2p+r)!/p^2 = 2*r! (mod p)`. Therefore the exact labelled port is
```
(8k+1)B_k/p^2 = 2(8k+1)(4k-2p)!/[2304^k(k!)^4] (mod p).
```
There is a **universal failure of naive same-index termwise transfer at precision p^3**. A cross-index identity remains viable. Do not discard the extra 2304-only band in a WZ or p-adic gamma attempt.

At p=181, all fifteen high-band ports k=121..135 are individually nonzero but sum to 0 mod181. Their exact ordered values are `129,118,141,143,129,82,63,30,74,134,34,67,88,173,43`. At p=373, 31 such ports sum to 281 mod373. This is a BRC provenance/observer collision: the scalar high-band total hides nonzero labelled terms. Existing signed/valuation BRC family: COMPOSE_APPLIED.

## Executed finite checker and sharpness

The companion Python executable independently uses modular term recurrences for W and S, and factorial/binomial sums for 9 primes. All 301 primes 5<=p<2000 (148 p=1 mod3, 153 p=2 mod3) passed `W_p=S_p=p*(-3/p) (mod p^3)`. Factorial/binomial independent checks for p=7,11,13,19,31,37,43,109,373: 9/9. Six-band source differences reconstruct each scalar difference. Selected tuple `(W mod p^3,S mod p^3,extra S band/p^2 modp,(W-S)/p^3 modp)`:
```
7:(7,7,2,4); 11:(1320,1320,8,1); 13:(13,13,6,11);
19:(19,19,16,6); 109:(109,109,42,43); 373:(373,373,281,114).
```
Nonzero p^4 residual at p=7 disproves the universal stronger transfer `W=S (mod p^4)`. All-prime original216 quadratic twist scan through p<10000 and its own p4 witness were published by another lane at `78823c266218450a0c31004dc920c20d94a8ae79`; this note consumes, does not reattribute, those results.

**Next scientific unit:** construct a genuine finite WZ/parameterized/microscoping or Frobenius transfer for ORIGINAL 216 to DIFFERENT proven 2304 series, including six-stratum compensation and cutoff p^3. Falsification set: 7,11,19,181,373. Uniform target p=13,19 mod24 is open.

**Native control:** actual `em_status` and original request receipt `em-h20-20261106-1324-d25-task-r13` failed 2026-11-07T01:18Z with `BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false`; Site `CONFIGURED_NOT_LIVE_VERIFIED`, Researcher authority unverified. Preserve also `em-h20-20261106-1324-d25-cont-r13` and protected session/claim/run/upload as UNKNOWN. Support `awdawmip/enterprise-math#1558`: operator restore dedicated Site client/version/credentials, then original reconciliation, exact Source continuation, lawful owner CLAIM/OPEN, durable checkpoint. No native experiment or Source publication; `REGISTER_PENDING/SYNC_DEBT`.
