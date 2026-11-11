# D25 — original W216 signed-class finite p³ falsification certificate (author side)

2026-11-11 Asia/Hong_Kong. **AUTHOR_SIDE / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0**. Parent `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`, task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Original scientific source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` preserved. Research conversation declared `chatgpt-research-onhour-enterprise-math-20260923`; not the maintenance lane. Scientific work is a separate author-side finite computation; no CLAIM or native run implied.

## Exact question and original observer

Use the same frozen original coefficient and **signed** weight:

\[
a_k=\frac{(2k)!(3k)!}{216^k(k!)^5}
=\frac{\binom{2k}{k}^{2}\binom{3k}{k}}{216^k},\qquad
W_p=\sum_{k=0}^{p-1}(6k+1)a_k.
\]

The program tests the **finite-range** prediction

\[
W_p\stackrel{?}{\equiv}\Bigl(\frac{-3}{p}\Bigr)p\pmod {p^3},\qquad 5\le p\le10000\text{ prime}.
\]

The character equals +1 for p congruent 1 modulo 3 and -1 for p congruent 2 modulo 3. This is a tested hypothesis on the full explicitly bounded prime population, **not an all-prime proof or a novelty claim**. For the frozen D25 classes p mod 24 = 13 or 19 the character is +1. Consume the already accepted exact scalar equivalence
\(\Delta_p-R_p=(W_p-p)/p^2\pmod p\); hence this finite test directly checks the original D25 scalar LIFT, without reopening UR.

## Independently executable finite result

Run `python3 research_notes/portable_direct/d25_original_w216_signed_class_finite_20261111.py` (Python standard library only). Sieve exhaustively lists all primes from 5 through 10000. For each prime the truncated W is computed with unit-denominator recurrence

\[
\frac{a_{k+1}}{a_k}=\frac{(2k+1)(3k+1)(3k+2)}{36(k+1)^3}
\]
modulo p³ (k<p−1). The program asserts every residue and also independently rebuilds a_k using integer binomial coefficients for eleven selected controls on both sides of the sign.

Actual local execution:
- 1,227 primes from 5 through 10000; 0 failures of the signed-class p³ prediction.
- Counts by p mod24: `1:143, 5:157, 7:156, 11:155, 13:157, 17:152, 19:155, 23:152`.
- 312 frozen targets (157 of class 13 and 155 of class 19), last target 9973; 0 failures of their original scalar LIFT. Off-target signed controls: 915 primes, 0 failures.
- Eleven independent factorial/binomial cross-checks at p=7,13,17,19,23,37,43,109,139,157,373, all identical.
- Examples: W_13 mod13³=13; W_19 mod19³=19; W_17 mod17³=4896 (=−17); W_23 mod23³=12144 (=−23); W_373 mod373³=373.

The signed phenomenon across p mod3 complements the previously published p≡13,19 finite scalar test; the 312 target checks extend earlier bounded coverage. Related classical supercongruence literature exists; whether this precise statement is previously published remains unassessed. Do not treat the finite domain as an infinite theorem.

## Typed valuation provenance at the frozen p373 witness

For 0≤k<p, the original coefficient has exact v_p(a_k)=⌊2k/p⌋+⌊3k/p⌋. No valuation-based deletion occurs before the signed observer is assembled. At p=373 with p³=51,895,117, partition W_373 by v=0,1,2,3 and preserve the four signed sums modulo p³:

```
v = 0: 28,094,360
v = 1: 38,687,933
v = 2: 37,008,314
v = 3: 0
total mod p³: 373
```

The v≤1 contribution is 14,887,176 = 373 + 107×139129. The v=2 term is 37,008,314 = 266×139129. Thus the **original** second-digit residual is exactly (107+266) mod 373 = 0. Collapsing the v=2 branch would yield the incorrect residual 107. This consumes and independently corroborates the earlier author-side signed half-range and original scalar ports (L=107, J=266); it is not a new attribution of that earlier formula.

**BRC application:** finite population and p mod24 labels retained; the carrier is original rational/binomial coefficient modulo p³ with valuation and sign/provenance. Readout is weighted signed W, followed only then by the second-digit division; no replacement by positive mass or an unsigned norm. Subsequent operators include cut-off reflection and the original Δ−R. `BRC_REUSE_RESOLUTION=COMPOSE_APPLIED` (existing signed W observer + exact valuations + finite signed-class discriminant).

## Native benchmark remains the priority

The fixed same-original-class H0/B0 divided-power experiment `[X]U mod139129` is still **NOT_RUN/PENDING_OWNER** by existing issue [#1559](https://github.com/awdawmip/enterprise-math/issues/1559). Its true rank, p373 semi-linear Frobenius direction, basis/η, native operator, odd Green/Hesse signed κ, exact original Δ−R comparison, independently reproduced artifact and execution owner are missing. This finite signed W certificate cannot replace it. The actual authorized native evaluator / canonical Research Task owner must take the existing support issue, execute the original fixed object, disclose all operator data and source pins, and publish the Source checkpoint through its legitimate own session/CLAIM/run. Do not force a rank-one model.

## Canonical control / recovery

Research logical lane declared `chatgpt-research-onhour-enterprise-math-20260923`; maintenance ID `chatgpt-hourly-enterprise-math-20260921` **not used**. Current Sources and operating rules have been read. At this scientific checkpoint, fresh read request `onhour11-20261111-0959-exact-cont` remained QUEUED; first same-lane service-issued Researcher session request `onhour11-20261111-1000-onhour-researcher-start` remained QUEUED (receipt showed no final successful active session); no authenticated own CLAIM/open run/Source PROGRESS is claimed. Do not reissue either request while pending: read original receipts/reconcile their effects. Platform identity attestation is not claimed.

Completed this author-side unit: finite 1,227-prime p³ signed scan and 11 crosschecks with executable evidence; p373 valuation recheck. Not to repeat: accepted CM0/SIMPLE/UR, earlier formal E3 positive Frobenius and p373 Δ=R=196, prior half-range L/J, this bounded finite run. Next exact native action: execute `[X]U mod139129` with all original operators; next direct mathematical question after native intake is exact Source bridge from H0/B0 operator and η/κ to the original signed scalar LIFT, preserving both p≡13,19 classes. **Result not frozen, review not performed, no Foundation promotion.**
