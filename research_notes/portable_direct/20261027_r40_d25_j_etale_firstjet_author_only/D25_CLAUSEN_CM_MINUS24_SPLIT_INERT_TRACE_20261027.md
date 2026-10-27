# D25 — auxiliary finite Clausen CM(−24) split/inert trace observation (2026-10-27)

**Scope/status:** AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / FINITE CERTIFICATE / UNIVERSAL CONJECTURE / UNREVIEWED / NOT-ADMITTED. GitHub draft preservation only; NOT native Source CLAIM, OPEN, checkpoint, independent review or original H0/B0. Frozen source `c47e13e4aba0e006366f989d6334d443f6333ae3` and taskbook publication `TP2-B6F4FC938FF94941C1B7` unchanged; source-side owner remains unverified.

## Definitions and proven algebra
For prime `p=6r+1>=7`, define
[
 A_p=A_r(1)=sum_{k=0}^{r}inom rkinom{2r}k,2^{-k}quadinmathbb F_p.
]
For `t_0=1`, `t_{k+1}=t_k (r-k)(2r-k)/(2(k+1)^2)`, and `A_p=sum(t_k)`. Every displayed denominator is a p-unit, so this recurrence equals the finite binomial polynomial exactly for all such primes. Reuse the preceding author-only Clausen antecedent `C_{0,p}(z)=A_r(z)^2` and Legendre pullback from this PR; neither antecedent is recredited here.

## New exact finite observation
The companion Python standard-library checker sieves **every prime 7<=p<40000 with p≡1(mod6)**, using independent modular recurrence and factorial/binomial computations, exhaustive integer search for `p=a²+6b²` with signed `a≡1(mod3)`, and Euler's exact quadratic-character test `(-6/p)`.

| p mod 24 | checked | A_p=0 | A_p≠0 | unique `p=a²+6b², a≡1(mod3), A_p=2a modp` |
|---|---:|---:|---:|---:|
| 1 | 501 | 0 | 501 | 501 |
| 7 | 526 | 0 | 526 | 526 |
| 13 | 532 | 532 | 0 | not applicable |
| 19 | 530 | 530 | 0 | not applicable |

**PASS for 2,089 primes**; all 1,062 target-class primes `p≡13,19(mod24)` have vanishing `A_p`; all 1,027 other primes in this domain have signed trace `A_p≡2a(modp)`. Examples: `p=7:(a,b,A)=(1,1,2)`, `31:(−5,1,21)`, `73:(7,2,14)`, `79:(−5,3,69)`, `193:(13,2,26)`; `p=373:A=0`. Exact full-record JSONL SHA-256 from complete author checker: `df4054e51030578be655cb2a52ed051b5455a5a4697c8a40743ef93457d6cc29`. That digest is a reproducibility identifier, not proof of an infinite-prime claim. Companion concise checker below independently reproduces the aggregate 2,089-prime result.

## Universal statement: **CONJECTURE, NOT PROVED**
For every prime `p≡1(mod6)`, the `p≡13,19(mod24)` cases have `A_r(1)=0(modp)`; for `p≡1,7(mod24)`, `A_r(1)=2a(modp)` where `p=a²+6b², a≡1(mod3)`. The quadratic character `(-6/p)` separates the classes. This suggests a discriminant −24 finite-character/Jacobsthal sum trace, but **no CM motive or Frobenius identification is established**. Finite testing does not prove the formula, and prior mathematical novelty is undetermined. Background only: Zhi-Hong Sun, *Jacobsthal sums, Legendre polynomials and binary quadratic forms* (2012), https://arxiv.org/abs/1202.1237; the exact conjecture's presence there is unverified.

## BRC/observer and scientific next step
Carrier: `(p,r,k,t_k,A_p,(-6/p),signed a,b,precision=mod p)`; all operations exact finite ring. Keep signed witness and source labels: scalar collapse without an actual future-operation/observer factorization is not an original-class native transfer. BRC provenance/observer gate REUSE_APPLIED, not positive weighted-mass cancellation. This is an external polynomial observation, not a P000 native three-dimensional slice or H0/B0.

Next **scientific** unit: establish an exact character/Jacobsthal sum identity for `A_r(1)`; prove the signed `a²+6b²` trace and inert zero universally, or falsify with an exact prime. Separately, `p=373` original native H0/B0 `[X]U mod139129`, Frobenius/eta/odd Hesse and `Delta−R` remain PENDING_OWNER/NOT_EXECUTED (Issue #1559); even a proved auxiliary trace will not imply LIFT `W_p≡p(modp³)` without strict original-source transport.

## Native provenance and continuation fence
Current gateway 0.6.11 quota 5/5, `executor_binding_configured=false`, `research_authority_granted=false`; Sites `static_machine_readonly/write_relay_enabled=false`. Historical request IDs `r40_20261027_1543_exact_cont_read_v1`, `r40_20261027_1436_exact_cont_read_v1` each returned `CONTROL_REQUEST_NOT_FOUND`; own checkpoint list ACCESS_DENIED; recovery_status callable not surfaced. Do not invent a Source session, CLAIM, predecessor completed research or evidence admission. For a future `CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS` seed, fully read current input artifacts and retain `frontier_notes.completed_units=[]`. UR V2 four-file original: expected 94,687 bytes / SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`; not recovered. Existing research frequency/phase/enable/notification unchanged.
