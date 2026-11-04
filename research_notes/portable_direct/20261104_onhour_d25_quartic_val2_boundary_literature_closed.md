# D25 — quartic valuation-two boundary CLOSED as a corollary of Guo–Zudilin (2019)

2026-11-04 +08. **AUTHOR-SIDE SOURCE-BOUND MATHEMATICAL DEDUCTION / EXTERNAL PUBLISHED THEOREM APPLIED / EXACT COROLLARY / UNREVIEWED / NOT_ADMITTED / NO NATIVE RUN.** This note continues the same D25 frozen scientific task, not a new task/result publication.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; original scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Immediate author-side dependencies: `20261104_onhour_d25_quartic_val2_universal_port.md` and `20261104_onhour_d25_quartic_val2_terminal_operator.md`. This note uses their precise coefficient law, **not** an assertion of admission.

## External exact theorem (already proved in 2019; not claimed as new)

Victor J. W. Guo and Wadim Zudilin, *A q-microscope for supercongruences*, Advances in Mathematics **346** (2019), 329–358, DOI 10.1016/j.aim.2019.02.008, arXiv:1803.01830, Theorem 1.1 and its q→1 specializations (2),(3).

- https://arxiv.org/abs/1803.01830
- https://doi.org/10.1016/j.aim.2019.02.008

For each prime `p>3`, write
```text
b_k = binom(4k,2k) binom(2k,k)^2 / (2^(8k) 3^(2k))
    = (4k)! / ((k!)^4 2304^k);
V_p(M) = sum_{k=0}^M (8k+1) b_k;
chi_p = (-3/p) (quadratic character).
```
Their theorem establishes **both**
```text
V_p(p-1)       = p*chi_p  (mod p^3),                 (GZ-full)
V_p((p-1)/2)   = p*chi_p  (mod p^3).                 (GZ-half)
```
The paper explicitly emphasizes that these are *different cutoff statements*, since the intervening terms need not individually vanish modulo p³. This last observation is load-bearing for the present port.

## Exact new source application: the open quartic val2 boundary is proved

For every prime `p>=5` set `h=(p-1)/2`, `N=floor((p+1)/4)`. For `0<=k<p`, the exact valuation is
```text
v_p(b_k) = floor(4k/p).
```
Consequently, the interval `h<k<p` decomposes **without lost ports** into
```text
valuation 2: k=h+n, n=1,...,N;
valuation 3: k>=ceil(3p/4), all terms zero modulo p^3.
```
Subtracting the two already-proved Guo–Zudilin cutoff identities therefore gives
```text
0 = V_p(p-1)-V_p(h)
  = sum_{n=1}^N (8(h+n)+1) b_(h+n)          (mod p^3).      (1)
```
Using the predecessor's coefficient-level rational-normalization theorem, with
```text
d_n = (4n-2)!*(n!)^4 / [9^n*((2n)!)^4];
b_(h+n)/p^2 = 2*d_n (mod p),    1<=n<=N;
8(h+n)+1 = 4p+8n-3,
```
equation (1) becomes
```text
0 = 2*p^2 * sum_{n=1}^N (8n-3)*d_n       (mod p^3).
```
Since `2` is a unit mod odd `p`, this proves the previously-open **all-prime boundary**
```text
THEOREM (literature corollary). For all primes p>=5,
N=floor((p+1)/4),   sum_{n=1}^N (8n-3)*d_n = 0 (mod p).       (2)
```
All denominators are `p`-units on this range. Both `p=4N-1` and `p=4N+1` follow **without class-by-class extrapolation**. The predecessor's exact finite-differential operator `L F_N=x/4` remains valid, and its boundary `(8 theta-3)F_N(1)=0` is now a **proved** corollary, not a numerical conjecture. The extra derivation here is elementary; the deep theorem is correctly credited to Guo–Zudilin.

The reason the 1,227/1,227 exact prime tests worked is now explained by a published all-prime theorem. No new operator/auxiliary bound is required to close this port.

## Integer/exact observer and information boundary

Native quartic coefficient carrier: integer numerator `(4k)!`, denominator `(k!)^4 2304^k`, `p`-valuation and two distinct endpoints `h,p-1`. The claimed cancellation concerns **the signed weighted aggregate** of the valuation-2 band; its individual coefficients need not vanish. Operator observer `(8 theta-3)F_N(1)` is faithful only for that designated scalar aggregate under the proved normalization; it does not license erasure of the 216-model high band or of H0/B0 odd/Frobenius operators. This is a concrete provenance/valuation-preserving reuse, rather than a new X6 axiom.

Local source-independent modular spot checker in this research turn directly regenerated `b_k` and `d_n` and checked `p={5,7,11,13,19,37,373}`, all zero boundary. These **finite checks are auxiliary**, not the proof; the theorem follows from the exact cited GZ two-cutoff statements and the already proved normalization. Checker filename in the turn's evidence bundle: `d25_quartic_tail_theorem_corollary_check_20261104.py`. Formal independent reviewer/Result admission still required by canonical Source.

## Continuation: mother D25 remains OPEN; stop re-solving quartic tail

**Mother goal:** `Delta_p-R_p=0 mod p` for `p=13,19 mod24`, exactly as frozen. The previous author-side proposal `W_p=V_p mod p^3` is **not proved** by (2), because the 216 and 2304 models have different valuation profiles and the former has a generally nonzero valuation-two weighted band. The external GZ theorem is sufficient for `V_p` alone.

**Closed / do not repeat:** quartic val2 complete weighted aggregate and its `F_N` terminal boundary (2), for every prime `p>=5`. The two prior proofs of normalization/operator need not be repeated. Existing previous CM0/UR/first-digit accepted material remains intact.

**Smallest unresolved science:** construct or disprove the actual signed cross-model, cross-valuation relation
```text
W_p - V_p = 0 (mod p^3),
W_p = sum_{k=0}^{p-1} (6k+1)*(2k)!(3k)!/(k!^5 216^k),
V_p = sum_{k=0}^{p-1} (8k+1)*(4k)!/(k!^4 2304^k).
```
Test a *proposed transport certificate* on `p={5,11,13,19,373}`, not merely final sums; preserve low/mid/high 216 bands and the terminated quartic band. A future proof of W=V combined with GZ implies W=p*(-3/p) mod p³ and hence the frozen scalar target through its existing separately verified bridge.

**Native benchmark debt unchanged:** issue #1559: same-original-class H0/B0 `[X]U mod 139129`, real semilinear Frobenius, actual module rank, eta, signed odd/Green observer, same-definition kappa and independent replay; responsible executor PENDING_OWNER. This literature result is **not** that experiment.

**Source/lane boundary:** author-side GitHub research note only, independent of canonical control checkpoint. Current Site configuration explicitly gives `research_authority_granted=false`, `write_relay_enabled=false` at 2026-11-04. Prior unresolved control request `research-onhour-20261031-0205-dispatch-r15` returned `CONTROL_REQUEST_NOT_FOUND` from the Site adapter in this turn; retain historical failure/receipt provenance rather than replay. Research logical lane `chatgpt-research-onhour-enterprise-math-20260923` is never substituted with maintenance lane `chatgpt-hourly-enterprise-math-20260921`. No Source session, claim, run, release or Result is asserted; site research role registration remains `REGISTER_PENDING` and native checkpoint `NOT_WRITTEN`.

**Status:** AUTHOR-DERIVED EXACT COROLLARY OF PUBLISHED THEOREM; UNREVIEWED / NOT_ADMITTED; QUARTIC PORT CLOSED; D25 MOTHER OPEN.

## Same-turn follow-on science: signed residual discriminator (finite exact)

After closing the quartic val2 term rigorously, the **remaining** cross-family observer can be written, using original integer/valuation carriers, as
```text
M_p = [ (A_(216,v0)+A_(216,v1)-V_p(h)) mod p^3 ]/p^2 mod p;
H_p = A_(216,v2)/p^2 mod p;
W_p-V_p = p^2*(M_p+H_p) mod p^3,
```
whenever the numerator defining `M_p` is divisible by `p²` (which has been **checked** in the listed samples, not proved universally). The `p²`-divisibility of `H_p` follows from the exact 216 valuation partition. No equivalence or homomorphism between unrelated BRC ports is inferred merely from a common scalar output.

A new independent exact integer recurrence script checked the 216 original coefficients and 2304 truncated coefficients at `p={5,11,13,19,37,373}`:

| p | M_p (mod p) | H_p (mod p) | M_p+H_p |
|---:|---:|---:|---:|
| 5 | 4 | 1 | 0 |
| 11 | 10 | 1 | 0 |
| 13 | 3 | 10 | 0 |
| 19 | 10 | 9 | 0 |
| 37 | 17 | 20 | 0 |
| 373 | 107 | 266 | 0 |

For `p=373`, `p²=139129`, and the low/mid-versus-quartic-half defect is exactly `139129*107=14886803` modulo `p³`; the original 216 second-valuation contribution is `139129*266=37008314`. These are **individually nonzero and oppositely signed as scalar port observations**, giving a concrete required compensation for any future cross-model certificate. The code is retained in the same-turn portable evidence bundle `d25_216_quartic_signed_residue_port_20261104.py`; these samples are not a proof of W=V or of all-prime p²-divisibility of M.

The next actual proof obligation is now specifically `M_p=-H_p` for all required p, with full source/denominator/band endpoint preservation. Prefer a terminating 216-to-quartic-half WZ or parameter-transform certificate. First test any candidate against the nonzero `(M,H)=(3,10),(10,9),(107,266)` at `p=13,19,373`, not just against final zero residues.
