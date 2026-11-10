# D25/LIFT — four-stratum p-adic coefficient reflection reciprocity

2026-11-10. Author-side TASK_RESEARCH evidence, AUTHOR_PROVED / FINITE_EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED. Frozen science: `awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3`. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, parent `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`.

## New theorem — *all* prime p>3

Define the p-local rational coefficients `a_k=(2k)!(3k)!/(216^k(k!)^5)` for `0<=k<p`; let `q2=floor(2k/p)`, `q3=floor(3k/p)`, `v_k=q2+q3`. For every prime p>3 and every integer `1<=k<p`, the exact p-adic valuation is `v_p(a_k)=v_k`, its reflected partner has valuation `v_(p-k)=3-v_k`, and

```math
(a_k * a_{p-k})/p^3
  = -(-1)^(q2+q3)*q3!*(2-q3)!/(36*k^3) (mod p).    (A)
```

The normalized units `u_k=(a_k/p^v_k) mod p` and `u_(p-k)` thus determine each other via the explicit right-hand side. This is a pointwise and labeled *product* identity, valid for all primes p>3 (not just the D25 selected classes).

For `p=6m+1`, set `E_k=-18 k^3 a_k a_(p-k)/p^3 mod p`. The exact four-stratum table is:

| k | q2 | q3 | v_p(a_k) | E_k |
| --- | --- | --- | --- | --- |
| 1..2m | 0 | 0 | 0 | 1 |
| 2m+1..3m | 0 | 1 | 1 | -1/2 |
| 3m+1..4m | 1 | 1 | 2 | +1/2 |
| 4m+1..6m | 1 | 2 | 3 | -1 |

## Proof

For q=0,1,2, r in 0..p-1, the factorial-block identity
`(qp+r)!/p^q = (-1)^q q! r! (mod p)` follows from removing the q multiples of p and applying Wilson to each complete block.

Put l=p-k, r2=2k-q2*p, r3=3k-q3*p. Since p>3, both r's lie in 1..p-1. Their partner remainders are p-r2 and p-r3, with respective floor quotients 1-q2 and 2-q3. Hence the combined valuation of `a_k a_l` is `1+2=3`. The floor factorial factors multiply to `q2!*(1-q2)!=1` and `q3!*(2-q3)!`, with overall sign `(-1)^3`.

Wilson supplies `r!(p-r)!=(-1)^r*r (mod p)` and `k!(p-k)!=(-1)^k*k (mod p)`. Fermat gives `216^p=216 (mod p)`. Therefore the normalized product is

```math
-(-1)^(r2+r3-k) * q3!*(2-q3)! * r2*r3/(216*k^5)
 = -(-1)^(q2+q3) * q3!*(2-q3)!/(36*k^3) (mod p),
```

because `r2*r3=6*k^2 (mod p)` and `r2+r3-k=4k-(q2+q3)p`. This proves (A). The four-stratum table follows by evaluating the two floors. The reflected index pair is involutively consistent since `(p-k)^3=-k^3 (mod p)` and the table's reverse row has the opposite `E`.

## Finite exact regression

Original `a_k` were independently computed by their source recurrence modulo p^4. For every one of the **312** primes `p<=10000, p mod24 in {13,19}`, all `1,475,586` pairs `(p,k)` with `1<=k<p` passed exact p^3 divisibility and formula (A). Eleven additional primes outside those D25 classes (`5,7,11,17,23,29,31,41,47,53,59`) passed another **312** pairs. Overall: **1,475,898** exact comparisons, zero discrepancies. Code is delivered in the portable bundle `D25_REFLECTION_TWO_THEOREMS_AUTHOR_PORTABLE_20261110.zip`, SHA-256 `f1bd68fb8e000fe81602617b291ef466cb076269ebba3ec02f9df44cc3f14ca9`; this ZIP is a local download, not a Source artifact.

## Continuation and provenance

The first-stratum specialization is exactly the separately published preceding pointwise theorem `a_(p-k)/p^3=-1/(18k^3 a_k)` for `1<=k<=2m` (author note blob `1c167c9547cbd5573de9e9e6828e239bcdce4be0`). The new contribution here is the *complete four-stratum p-adic reciprocity and all-prime proof*, which supplies a residual transport law for the full original weighted-W representation. The remaining mother-objective route is a genuine WZ/contiguous identity for uniform `W_p=p (mod p^3)` or authentic original-class H0/B0 representation; this note makes no claim of those completions or Source acceptance.

The original UR V2 four-file archive remains an independent historical provenance debt (94,687 bytes, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`). Native Source CLAIM/run/result and independent review are not asserted.
