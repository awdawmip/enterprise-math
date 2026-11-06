# D25: Exact two-port Green reciprocity for the original 216 / mixed-CM endpoint

2026-11-06 | TASK_RESEARCH author-side, logical research lane `chatgpt-research-onhour-enterprise-math-20260923` | scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3` | task `TP2-B6F4FC938FF94941C1B7`.

**Classification:** algebraic propositions proved by finite factorial manipulation; integer checks executed for 80 primes; UNREVIEWED / NOT_ADMITTED. This consumes the immutable mixed-CM exact cubic endpoint at `c8a36bd133ac6397ce1e6d37859ae52764427837` and original-216 Green observer at `8b4c34383377166ba1cba395bad631b2ad6abbd3`. No assumption of native H0/B0 execution.

## Objects and source-preserving ports

Let `p=6m+1>3` be prime, and let

```
gamma_k = binom(2k,k)^2 binom(3k,k) = (2k)!(3k)!/(k!)^5
b_0 = 1; b_n/b_(n-1) = 6(6n-5)(3n-2)/n^2
a_k = gamma_k/216^k,       d_k=b_k/216^k
h_1 = 1/24;
h_(r+1)/h_r = r^2(6r+1)/[(r+1)(2r+1)(3r+2)]
T_k=gamma_k b_(p-k)
M={2m+1,...,3m}, U={5m+1,...,6m}
V_k=T_k/p^3 in Z_(p) for k in M union U.
```

The indices `k` and `r=p-k`, p-adic valuations, and the signed weight remain separate observer coordinates.

### Theorem A — universal kernel ratio (exact in Q)

For every integer `r>=1`,

```
h_r = b_r/(12*r^2*gamma_r),       a_r*h_r=d_r/(12*r^2).
```

**Proof.** The ratio `gamma_r/gamma_(r-1)=6(2r-1)(3r-2)(3r-1)/r^3`. Thus the ratio of `b_r/(12r^2 gamma_r)` to the preceding term is `(r-1)^2(6r-5)/(r(2r-1)(3r-1))`, exactly the defining ratio for `h_r`. The initial value is `b_1/(12 gamma_1)=6/(12*12)=1/24`.

### Theorem B — two signed factorial-reflection phases

For every prime `p=6m+1>3`,

```
gamma_k gamma_(p-k)/p^3 == -12/k^3 (mod p),  1<=k<=2m;
gamma_k gamma_(p-k)/p^3 ==  +6/k^3 (mod p),  2m<k<=3m.
```

All quotients on the left are p-integral. **Proof.** Write `gamma_k=(2k)!(3k)!/(k!)^5`. For `0<=s<p` and `a=1,2`, Wilson's theorem gives `(ap+s)!/p^a == (-1)^a a!s! (mod p)`, while `(p-t)! == (-1)^t/(t-1)! (mod p)` for `1<=t<p`. For the first interval `3k<p`, the only three p-factors belong to `gamma_(p-k)` and substitution gives `gamma_(p-k)/p^3 == -12/(k^3 gamma_k)`. For the second interval `2k<p<3k<2p`, `gamma_k/p == -(2k)!(3k-p)!/(k!)^5` and `gamma_(p-k)/p^2 == -(k-1)!^5/[(2k-1)!(3k-p-1)!]`, yielding the product `2(3k-p)/k^4 == 6/k^3 (mod p)`.

### Theorem C — full middle and upper valuation-three port transport

Using exactly the *same* universal Green sequence `h` as the earlier signed original-216 boundary,

```
V_k       ==  72*h_(p-k)/k (mod p),   k in M;
V_(p-r)   == -144*h_r/r   (mod p),   1<=r<=m (k in U).
```

**Proof.** The exact identity `T_k=12(p-k)^2 gamma_k gamma_(p-k)h_(p-k)` follows from Theorem A. Apply the two respective phases of Theorem B (to `k` on M, to `r` on U), and `(p-k)^2==k^2 (mod p)`. The `h_r` in both claimed intervals are p-integral and p-units: for `1<=r<=m` both `b_r,gamma_r` are units; for `3m+1<=r<=4m` both have valuation two. The formula is coefficientwise and therefore transports arbitrary p-integral linear observation weights without erasing branch identities.

For the exact weighted endpoint observer,

```
sum_(k in M) k V_k ==  72 sum_(r=3m+1)^(4m) h_r (mod p),
sum_(k in U) k V_k == 144 sum_(r=1)^m h_r (mod p).
```

Consequently the previously proved mixed-CM cubic endpoint becomes

```
(gamma_p-2*b_p)/p ==
 -3 sum_(k=1)^(2m) k L_k
 +p*(2 sum_(k=1)^(2m) L_k
      -216 sum_(r=3m+1)^(4m) h_r
      -432 sum_(r=1)^m h_r)                    (mod p^2),
L_k = gamma_k b_(p-k)/p^2.
```

This is a genuine **source-preserving adjoint reduction of both M/U endpoint ports**, not an identification of the mixed-CM coefficient with the original evaluation.

### Corollary — exact meeting with original 216 signed Green boundary

The pre-existing original Green observer is `J_p=sum_(t=1)^m h_t P_t` with `P_t=sum_(k=0)^(t-1)(6k+1)a_k`. Hence the new upper-port transport gives

```
J_p - (1/144)sum_(k in U) k V_k
 == sum_(t=1)^m h_t (P_t-1)  (mod p).
```

It identifies a shared `h_t` channel but preserves the additional original-evaluation prefix `P_t-1`; it is the explicit remaining interaction/repair coordinate.

## Executed check / reproducibility

The accompanying Python standard-library program computes `gamma` from integer binomials, `b` from the original ratio modulo `p^3`, and `h` from its independent valuation/unit recurrence (not from `b/gamma`). All 80 primes `7<=p<=997, p==1 (mod 6)` passed (45 target primes), covering 18,294 gamma reflection checks and 6,098 checks on each port, plus signed moments and original `J` reconciliation. No floats or assumed theorem checker. Representative `(M_moment,U_moment,mid_h_sum,upper_h_sum,J)`: `p=19:(7,17,3,5,6)`; `p=373:(323,150,134,172,98)`. The mixed-CM M/U total corrections are respectively `4 mod 19` and `73 mod 373`. Full code is in `d25_mu_green_reciprocity_20261106.py`.

**BRC resolution: COMPOSE_APPLIED.** Carrier consists of exact integer factorials, p-adic valuation, low/M/U label, reflected original index, signed k weight and Green h, with future observations including general weighted moments, the cubic endpoint and original J. The corollary exhibits the non-discardable original prefix interaction.

## Frozen parent, authorization, next exact action

The frozen parent remains `Delta_p-R_p == 0 (mod p)` for `p=13,19 (mod24)`, equivalently via the frozen scalar interface to original `W_p == p (mod p^3)`. The new proof discharges the coefficient-level M/U port representation for the cubic endpoint, not the full W adjoint. Next: combine the existing **low port deformation** (previous commit `7269634545edb59ac7ff2acf164e8f9ec1071d31`) with this M/U Green transport, and seek a finite original evaluation functional mapping; test whether `sum h_t(P_t-1)` is exactly canceled by the remaining low-port first-order jet. Preserve all source labels and compare `p=19,373` without treating the CM coefficient as original W. Separate original native p373 H0/B0 experiment remains at Issue #1559, awaiting actual authorized execution and replication.

Last native Source operation `onhour11-20261106-1400-exact-research-lane-continuation` was re-read by its original request ID; status `QUEUED`, progress phase `EVENT_COLLECTION_IO`. Current status reports `research_authority_granted=false`. No new native session, CLAIM, open, run, Result, or review is asserted. Research lane is `chatgpt-research-onhour-enterprise-math-20260923`; maintenance lane remains excluded.
