# D25 — complementary middle/high reciprocal observer for the original 216 family

2026-11-04 (Asia/Hong_Kong). **AUTHOR-DERIVED / EXACT SCOPED PROOF / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED.** Author-side mathematics, **not** a native Source checkpoint/Claim/Result.

Frozen task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; scientific input pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research conversation `chatgpt-research-onhour-enterprise-math-20260923` is not the maintenance conversation `chatgpt-hourly-enterprise-math-20260921`.

## Theorem: a universal complementary-index product

For every prime `p=6r+1>=7` and integer `0<=n<r`, put

```text
a_k = (2k)! (3k)! / [ (k!)^5 216^k ]
m_n = a_(3r-n) / p    (mod p)
h_n = a_(3r+1+n) / p² (mod p).
```

The two indices sum exactly to p. Their factorial valuations are 1 and 2 respectively, and both normalized coefficients are nonzero in `F_p`. The following **exact congruence is proved for all such p,n**:

```text
(2n+1)^3 m_n h_n = -2/9 (mod p).                         (1)
```

In particular, for the complete original-216 weighted valuation-two band,

```text
H_p := [Σ_(k=3r+1)^(4r) (6k+1) a_k] / p²  (mod p)
     = -(2/9) Σ_(n=0)^(r-1) (6n+4) / [(2n+1)^3 m_n] (mod p).  (2)
```

The inverse denominators are units. This is a *source/valuation-preserving reciprocal observer*, not a claim that positive BRC weights cancel or that an ordinary finite field model realizes the native X6 H0/B0 experiment.

### Proof

Set `h=3r=(p-1)/2` and `chi=(6/p)`. With Wilson's theorem,
`(p-1)!=-1`, `(3h)!/p=-(h-1)!`, `(h!)^4=1` and `216^h=chi` modulo p. Thus
`m_0=a_h/p=1/[h(h!)^4 216^h]=-2chi (mod p)`.
The original high-band endpoint (or its direct analogous factorial calculation) gives
`h_0=a_(h+1)/p²=chi/9 (mod p)`.

The **exact** original rational coefficient ratio is

```text
a_(k+1) / a_k = (2k+1)(3k+1)(3k+2) / [36(k+1)^3].
```

For `0<=n<r-1`, substitute `k=h-n` (backward) and `k=h+1+n` (forward) to obtain in `F_p`:

```text
m_(n+1)/m_n = 9(2n+1)^3 / [(n+1)(6n+5)(6n+7)],
h_(n+1)/h_n = (n+1)(6n+5)(6n+7) / [9(2n+3)^3].
```

All factors used in these interior ratios are units modulo p. Their product is `[(2n+1)/(2n+3)]^3`. Hence `(2n+1)^3m_nh_n` is constant, equal at n=0 to `(-2chi)(chi/9)=-2/9`, proving (1). Because `6(h+1+n)+1=3p+6n+4`, weighted summation proves (2).

## Directly targeted remaining D25 bridge

Let `A_0,A_1,A_2` be the actual original-216 weighted valuation-0,1,2 contributions modulo `p³` and let
`V_h=Σ_(k=0)^(3r)(8k+1)(4k)!/[(k!)^4 2304^k]`.
Use the already sourced Guo–Zudilin 2019 full/half 2304 result `V_full=V_h (mod p³)`. Then (2) yields the **unconditional identity**

```text
W_p - V_full =
 A_0 + A_1 - V_h
 - (2p²/9) Σ_(n=0)^(r-1) (6n+4)/[(2n+1)^3 m_n]  (mod p³).   (3)
```

Unlike the preceding `M_p` quotient, (3) needs **no preliminary assumption** that `p² | A_0+A_1-V_h`. The remaining proof target is to show the right-hand side vanishes uniformly, which would give that divisibility and the signed cross-valuation compensation at once. No all-prime proof of this cancellation is claimed.

## Exact independent checks and concrete observations

The companion Python checker reconstructs both families from their **original** factorial coefficient laws with p-free factorial units modulo `p³`, and separately computes (2). For all 148 primes `7<=p<=2000, p=1 (mod 6)`, it checked **22,952** middle/high index pairs and all high-band observers with zero failures. The same 148 primes satisfied (3) and the still-conjectural *signed final cancellation* in these finite tests. There were 24 further direct ordinary-integer factorial coefficient crosschecks on 7,13,19,37,373.

At `p=373`: `(n,m_n,h_n)=(0,2,290),(1,203,8),(61,320,181)`. Every product `(2n+1)^3m_nh_n` equals `207=-2/9 (mod 373)`; `H_373=266`; the observed low/mid quotient is `M_373=107` and `M+H=0 (mod 373)`. The actual weighted high port is `37008314 (mod 51895117)`.

## Source-exact continuation and obligations

**Frozen mother:** `Delta_p-R_p=0 (mod p)` for `p=13,19 (mod 24)`. Source pin unchanged. **Consume/do not redo:** accepted D24 UR/CM0, Guo–Zudilin quartic second-valuation cancellation, original-216 high kernel, existing first-digit and finite scans. **Smallest unresolved science:** construct a genuine terminating *signed* WZ/Green certificate for the right-hand side of (3), first auditing every port and boundary at 13,19,373; then establish the all-prime relation. The reciprocal observer uses the already-required middle valuation data and reduces separate high input.

**Native benchmark debt:** original fixed-373 class H0/B0 divided-power `[X]U (mod 139129)`, true semilinear Frobenius/rank/odd Green/κ and independent replay tracked in `#1559`; still pending and not replaced by this calculation. The 2026-11-04 Site gateway 0.6.11 gave `research_authority_granted=false`; exact continuation read failed `CONTROL_QUOTA`, old request `research-onhour-20261031-0205-dispatch-r15` failed `CONTROL_REQUEST_NOT_FOUND`. Formal own Source session/claim/run/checkpoint/Result **not established**. Research and maintenance logical lanes remain separated. No scheduler or notification changes.

Mathematics proof is an author-side scoped result; mathematical independent review/Result admission remains pending.
