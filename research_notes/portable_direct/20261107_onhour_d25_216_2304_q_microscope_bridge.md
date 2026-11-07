# D25 portable research — fourth-digit signed bridge between the 216 and 2304 Ramanujan sums

Date: 2026-11-07 (Asia/Hong_Kong). Research lane: `chatgpt-research-onhour-enterprise-math-20260923`.
Scope: author's independent portable research note, `UNREVIEWED / NOT_ADMITTED`; no native Source Result, CLAIM or benchmark.

## Frozen mother target and source separation

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`.
The frozen question is `Delta_p ≡ R_p (mod p)`, for primes `p ≡ 13,19 (mod 24)`. Earlier author's immutable note `7771424fd5f77bc0626385ef9842afc5abd7f820` gives the conditional exact transfer `(W_p-p)/p² ≡ Delta_p-R_p (mod p)`, using accepted earlier inputs. Preserve its provenance and review status.

Set
```text
W_p = sum(k=0..p-1) (6k+1) binom(2k,k)^2 binom(3k,k) / 216^k
V_p = sum(k=0..p-1) (8k+1) binom(2k,k)^2 binom(4k,2k) / 2304^k
chi_p = (-3/p) = +1 if p≡1(mod3), otherwise -1 (p>3)
```
All terms lie in Z_(p), since p>3; reduction mod p^r is unambiguous.

## New independently sourced proven comparison object

V is exactly the Ramanujan-type sum treated by Victor J. W. Guo and Wadim Zudilin, *A q-microscope for supercongruences*, Advances in Mathematics 346 (2019), 329–358, arXiv:1803.01830v6, https://arxiv.org/abs/1803.01830 , abstract:
`V_p ≡ p chi_p (mod p³)` for every prime p>3.

**Do not confuse this published theorem with a proof for W.** V uses binom(4k,2k) and denominator 2304^k, while frozen W uses binom(3k,k) and 216^k. The distinction is the new comparison experiment.

## New candidate, classification: CONJECTURE, FINITE_VERIFIED

For all primes p>3, propose the fourth-digit signed-port relation
```text
H_p := 2 V_p - W_p - p chi_p ≡ 0 (mod p^4).      (H)
```
This is a stronger, more discriminating candidate than merely W≡V(mod p³). It retains the two distinct hypergeometric sources as separate ports.

### Proved conditional reduction (ordinary algebra)

For each p>3, assuming (H) at that p and invoking the Guo–Zudilin theorem at that p:
```text
W_p ≡ 2V_p - p chi_p ≡ p chi_p   (mod p³).
```
For p≡13,19(mod24), chi_p=1; hence (H) implies the frozen W_p≡p(modp³) and, by the already established frozen-transfer bridge, Delta_p≡R_p(modp). This is a logically exact conditional implication; (H) itself still needs a proof.

### Exact finite evidence

The accompanying Python 3 standard-library checker was executed locally using two distinct coefficient streams modulo p^4. For every one of **667** primes 5<=p<5000 (330 with chi=+1; 337 with chi=-1), all 667 satisfy (H). The program checks Guo–Zudilin's V congruence and W's earlier observed congruence independently as diagnostics, and recomputes both sums from direct binomial coefficients for all **77** primes p<=401. Exact arithmetic only; 0 errors.

Representative residue triples (W_p mod p^4, V_p mod p^4, chi_p):
```text
p=  7:      350,      1379, +1
p= 11:     2651,      1320, -1
p= 19:    82327,     41173, +1
p= 61:  1588928,   7717415, +1
p=373: 11832087049, 5916043711, +1
```
At p=373, (W_p-p)/p³ ≡ 228 and (V_p-p)/p³ ≡ 114 (mod 373), exactly the factor two predicted by (H).

### Exact counterexample to universal extension to p^5

At p=11, direct binomial recomputation modulo 11^5=161051 gives W_11=119779 and V_11=103807; chi_11=-1. Therefore
```text
(2 V_11-W_11-11 chi_11) mod 11^5 = 87846 = 6*11^4 != 0.
```
Thus universal strengthening of (H) to mod p^5 is false. This single exact input is a full counterexample to that stronger statement. It does not settle (H).

## Direct verification method / BRC observer

Retain ordered signed provenance ports `(W_p,V_p,p chi_p)` instead of collapsing the two sequences prematurely. The integer observer `(w,v,c) -> 2v-w-c` in Z/p^4Z captures the candidate cancellation, and the p^3 quotient retains the first unreduced residual. This is a concrete signed multi-port, source-preserving use of the BRC observer discipline; it claims no additional BRC theorem or changed scientific model.

The checker generates primes by a sieve, computes both sums from exact factorial-ratio modular recurrences, verifies all 667 cases and separately recomputes the 77 small cases by direct binomial integers. Because 1<=k+1<p, recurrence denominators are p-adic units. There is no floating arithmetic, stochastic sampling or hidden model assumption.

## Next smallest unfinished mathematical unit

Construct a **uniform finite hypergeometric / q-microscoping transformation certificate** whose p-adic specialization proves (H), initially for the frozen positive branch p≡13,19(mod24). Favor a termwise or telescoping *signed difference* linking the 216 and 2304 coefficient streams; explicitly check p=11 (the p^5 sharpness witness), p=19 and p=373. Alternatively, show a counterexample to (H) at a concrete prime or prove the weaker mod p³ equality first. Guo–Zudilin supplies a proven external benchmark, not a replacement for the missing W-to-V transformation.

Native p=373 H0/B0 divided-power, Frobenius/Hesse kappa, independent reproduction (issue #1559) remains a distinct, unexecuted native requirement. Do not count this portable certificate as the benchmark.

## Source and handoff

Original target request: `onhour11-20261106-1400-exact-research-lane-continuation`.
At 2026-11-07T02:00Z gateway status `CONFIGURED_NOT_LIVE_VERIFIED`, `research_authority_granted=false`; direct `em_status`, request receipt and continuation reads returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH; operation_sent=false`. No session/CLAIM/run/Result was obtained. Preserve old request; no duplicate mutation, no maintenance lane use.

Classification: `PROVED_CONDITIONAL_REDUCTION + FINITE_EXACT_CERTIFICATE + MOD_P5_COUNTEREXAMPLE`, plus universally quantified `CONJECTURE(H)`. Author-side only, `UNREVIEWED / NOT_ADMITTED`.
