# D25 — original W full-truncation stress test and character-extension candidate
Date: 2026-11-02. Source class: AUTHOR-SIDE EXACT FINITE EVIDENCE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT. Not an authenticated TASK result, not native H0/B0.

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, **frozen scientific pin unchanged** `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research-lane historical label: `chatgpt-research-onhour-enterprise-math-20260923`; maintenance lane `chatgpt-hourly-enterprise-math-20260921` never used. This is a new direct mother-goal finite stress test, not a reproof or restaging of prior 107-prime test, D24, or other-lane Cauchy work.

## Target-object identity and exact modular algorithm

The *original* weighted 216 series has integral numerator form

```
W(N)=sum_{k=0}^N (6k+1)*B_k,  B_k=binom(3k,k)*binom(2k,k)^2/216^k.
```

This is exactly the frozen `(6k+1)*(2k)!(3k)!/(216^k*(k!)^5)`, not a substitute hypergeometric model. From factorial ratios the p-local recurrence is

```
B_0=1,
B_k/B_{k-1} = (2k)(2k-1)(3k)(3k-1)(3k-2)/(216*k^5).       (R)
```

For prime p>3 and 1<=k<p the denominator 216*k^5 is a p-unit. Thus (R) is a rigorous *termwise exact identity* modulo p^3 using integer modular inverses, even at indices where numerator factors are divisible by p. The implemented sum uses O(p) modular steps and preserves the original half/full cutoff and high-band difference; no division by p is performed until an independently checked p^2-divisibility.

Using the already sourced and proved original D25 bridge

```
Delta_p-R_p = (W((p-1)/2)-p)/p^2 + B2,W(p)              (mod p)
B2,W(p) = [W(p-1)-W((p-1)/2)]/p^2                       (mod p),
```

the original mother claim in its target classes is *equivalent under accepted D24/CM0 and the original cutoff source* to the single full-truncation claim

```
                         W(p-1) = p    (mod p^3),     p=13,19 (mod24).   (T)
```

This is a reduction to the **same original weighted coefficients**, not a change in scientific input or a proof of (T).

## Executed discriminating finite checks

`d25_full_original_w_stresstest_20261102.py`: exhaustively checked all **575** primes `p<=20000` in target classes 13 or 19 (mod24); no failures of (T), or of the high-band p^2 divisibility and signed half/high second-digit balance. This extends the predecessor's 107 targets through p<=3000 with original coefficient recurrence and checks the mother-target equivalent.

`d25_original_full_W_character_test_20261102.py`: separately checked *every* **1227** prime `5<=p<=10000`, broken down into 611 primes p=1 (mod6) and 616 primes p=5 (mod6). All satisfy the stronger **finite-supported candidate**

```
W(p-1) = p*chi_{-3}(p)   (mod p^3),                       (C)
chi_{-3}(p)=1 if p=1 (mod3), else -1 if p=2 (mod3).
```

No failure in 1227 tests, but **(C) has not been proved for all primes**, nor established as new relative to all published literature. It gives a distinct possible WZ target: prove (C) directly, whose 13/19 residue-class restriction gives (T).

An independent `math.comb` exact-integer implementation compared **complete and half** original truncations with recurrence for p=13,19,373,3019, all matching. The check at 3019 is outside the predecessor's 107-prime sample. Example values:

| p | W(p-1) mod p^3 | W((p-1)/2) mod p^3 | B2,W mod p | signed second digit |
|---:|---:|---:|---:|---:|
| 13 | 13 | 520 | 10 | 0 |
| 19 | 19 | 3629 | 9 | 0 |
| 373 | 373 | 14887176 | 266 | 0 |
| 3019 | 3019 | 20097169024 | 814 | 0 |

For p=5,11 (outside target, p=5 mod6), the full sums are `-p mod p^3` (120 mod125 and 1320 mod1331), rather than +p; these are positive controls of the character-class distinction and are not counterexamples to (C). The proof status remains **finite exact arithmetic, not universal supercongruence**.

## Next proof obligation, source discipline, and native benchmark

Prioritize a terminating WZ/contiguous identity for the **original full W(N)** or an admissible published theorem matching all three precise data: weight (6k+1), parameter triple (1/2,1/3,2/3) with argument 1/2, and cutoff p-1, precision p^3. A theorem for the 2304 model, for a half cutoff, or only p^2 does not by itself discharge (C)/(T). The alternate joint-quotient observer bridge (same lane) preserves CM-root and deformation repair needed for a source-level proof. Test any candidate on p13,p19,p373, plus p5/p7 controls. Report exact scoped result if no uniform proof is found.

Native p373 H0/B0 divided-power `[X]U mod139129`, actual rank, semilinear Frobenius, eta, signed Green/Hesse/kappa, independent replay still NOT_EXECUTED, no confirmed owner (existing issue #1559). New scalar W checks do not satisfy it.

Current client control (read-only): gateway v0.6.11, research_authority_granted=false, write_relay_enabled=false; own checkpoint ACCESS_DENIED; exact continuation CONTROL_QUOTA; original request `research-onhour-20261031-0205-dispatch-r15` CONTROL_REQUEST_NOT_FOUND in client, older receipt FAILED/UPSTREAM_CODE_REVIEW_REQUIRED on bridge #6633. No retry or role-bound write, no Source session/claim/run, no maintenance-lane identity. Author-side GitHub evidence is not Source checkpoint/Result/admission. Preserve old independent staging and unchanged scheduler/notifications.
