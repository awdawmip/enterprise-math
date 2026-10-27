# D25/LIFT R35 — Wilson-free exact relative source transfer at the p≡19 weight-zero index

Date: 2026-10-27, Asia/Hong_Kong. Same legitimate Research-lane logical conversation `chatgpt-research-hourly-enterprise-math-20260923` (distinct from control maintenance). Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`; scientific frozen pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Mother D25/LIFT/JT2 OPEN. **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY**.

## Consume prior exact results; new question

R23 reduced the original W/S p³ supercongruence to a low-half W/S port plus genuinely W-sourced high-jet. R29 proved the unique p≡19 S weight-zero index has `v_p(w_k)=1`, `v_p(s_k)=2`, thereby excluding a **valuation-preserving unit-diagonal same-index** transfer. R34 now provides independent Wilson-quotient/harmonic normalized jets of *both* terms up to their required digits. This unit asks whether, **after explicitly retaining their differing valuations**, one can relate the original W and S terms by an exact, Wilson-quotient-free **relative** transfer. No original input or summation coefficient is altered.

For prime `p≡19 (mod24)`, put `k=(3p−1)/8`, `r=(p−3)/8`, `R=(p−1)/2`; thus `3k=p+r`, `4k=p+R`, `2k<p`, and `6k+1=(1+9p)/4`. Keep the genuine, source-labelled, unchanged original terms

```text
w_k=(6k+1)(2k)!(3k)! /[(k!)^5 216^k],
s_k=(8k+1)(4k)! /[(k!)^4 2304^k].
```

Define p-unit `G_p`, harmonic difference `h_1` and squared harmonic difference `h_2` in `Z_(p)`:

```text
G_p = 12 (3/32)^k k! R! /[(2k)! r!],
h_1 = H_R−H_r = Σ_(j=r+1..R) 1/j,
h_2 = H_R^(2)−H_r^(2) = Σ_(j=r+1..R) 1/j².
```

## Theorem — exact all-order local transfer, free of Wilson quotient

For *every* prime p≡19 (mod24) the ratio

```text
gamma_p := s_k/(p w_k)
         = G_p/(1+9p) Π_(j=r+1..R)(1+p/j) ∈ Z_(p)^×       (T1)
```

is an **exact rational identity**, not merely a congruence. Thus `s_k=p gamma_p w_k`; both original series-source identities and their distinct valuations are retained. The Wilson quotient `Q_p=((p−1)!+1)/p` cancels entirely from the transfer.

In particular its third-digit expansion is

```text
gamma_p ≡ G_p[1+p(h_1−9)
   +p²((h_1²−h_2)/2−9h_1+81)]                  (mod p³). (T2)
```

More generally every digit is obtained without an extra factorial-block or Wilson-quotient input from the exact product (T1). It is a **unit map between the p-valuation-shifted one-index source lines**, not a valuation-preserving map between the unscaled W/S families; nor does it transfer different indices, finite Green endpoints or infinite boundary families.

**Proof.** For the original factorial terms `8k+1=3p` and `216/2304=3/32`, direct cancellation (with unchanged W/S coefficients) yields

```text
s_k/(p w_k)
 = [3/(6k+1)] [k!/(2k)!] [(4k)!/(3k)!] (3/32)^k.
```

As `3k=p+r`, `4k=p+R`, the exact integer quotient is

```text
(4k)!/(3k)! = Π_(j=r+1..R)(p+j)
             = (R!/r!) Π_(j=r+1..R)(1+p/j).
```

Substitute `3/(6k+1)=12/(1+9p)` to establish T1 exactly. Every factor is a p-unit because `k,2k,r,R<p` and `p>3`; hence `gamma_p` is a p-unit. For T2 the first two elementary symmetric polynomials of `1/j` are `h_1` and `(h_1²−h_2)/2`, while `(1+9p)^(−1)≡1−9p+81p² (modp³)`. Multiply with `G_p`. QED.

## Corollary — faithful compression condition for the actual low-half defect

At this sole index the exact original difference is

```text
w_k−s_k = w_k (1−p gamma_p).                   (C1)
```

Since `v_p(w_k)=1`, the local defect modulo p⁴ is recovered from `w_k/p mod p³` and `gamma_p mod p²`; the p³ relative jet in T2 is a spare next-digit coordinate. This gives a lossless **same-index, valuation-shifted** representation for this particular additive observer. It is **not** evidence that the original W/S source labels or any cross-index/infinity/Green Hasse ports may be collapsed under other observers.

The global p³ bridge `D_p≡−p²U_p` (R23) remains OPEN: neither the exact local relation (T1) nor R34's p⁴ source lift provides the **cross-index** nonlocal WZ cancellation.

## Actually executed author verification

The accompanying Python-standard-library checker reconstructs `s_k/(p w_k)` from the unchanged factorial definitions, independently constructs the short exact ratio, tests the **exact Fraction equality** of T1, tests the unit property, and evaluates the third-digit approximation T2. It passes for **all 37 primes p<2000 with p≡19 (mod24)**: 37 exact rational equalities and 74 mod-p³ assertions. Selected rows `(p, gamma_p mod p³)`:

```text
(19,2158), (43,22249), (67,41349), (139,2111822),
(163,1928584), (211,3856261).
```

This finite author check corroborates the general exact algebra; no native original-class CM computation, Source task execution or independent Driver review was performed.

**BRC COMPOSE_APPLIED** with the typed carrier `(original-series, rank, v_p, unit, rational product, observation modulus, permitted future operations)`: valuation shift is a required repair coordinate. The local rank is an arithmetic index and not an Enterprise X6 axis. No source pin, protected P000 or ACTIVE worldview modification.

**Next precise research unit:** insert this Wilson-free relative unit jet together with R34's normalized W first/second/third digits into the R28 endpoint-sensitive Green adjoint, and seek a truly unchanged-input cross-index WZ compensator for R23's `U_p`. Retain p≡13 distinct S-mid/W-high ports, six fixed-z=2 Hasse J/E ports, finite and infinity Green sources and native Frobenius eta/kappa. Current Source claimant/session mismatch still requires control owner #1558; portable evidence and Research-Activity records are not the native Task checkpoint.
