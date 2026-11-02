# D25: Valuation-zero ordinary moment contraction and signed p=373 refinement (2026-11-02)

**AUTHOR-DERIVED / CONDITIONAL ALGEBRAIC LEMMA / EXACT FINITE CHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0.**

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; immutable scientific pin `c47e13e4aba0e006366f989d6333ae3`; Research lane `chatgpt-research-onhour-enterprise-math-20260923`. Consumes the just-published full p^4 carry transport at `research_notes/portable_direct/20261102_onhour_d25_full_p4_digit_carrier.md`. This is neutral author math evidence, **not** Source checkpoint, Research Activity, claim, review or Result.

## Statement: exact p² digit of the no-valuation rectangle

Let `p>=5` prime. For the original 216 stream use `J={2,3}`, `d0=5`, `d=216`, `lambda=6`; for the original 2304 stream use `J={4}`, `d0=4`, `d=2304`, `lambda=8`. Define

```
u(n) = prod_(j in J)(jn)! / ((n!)^d0 * d^n),  h=floor((p-1)/max J).
M_t = sum_(a=0..h) a^t*u(a)  (mod p^3).
```

For `k=ap+b`, `0<=a,b<p`, **the unweighted source coefficient has p-adic valuation zero if and only if `a,b<=h`**; this follows from nonnegative Legendre factorial carries. Its weighted observation is retained exactly, including indices where the weight itself vanishes mod p.

Assume the *explicitly testable* one-digit CM moment conditions `M0=M1=0 mod p`. Do not mistake this condition for an independently established all-prime theorem in this note. Let `q=(d^(p-1)-1)/p mod p`, `H_n^(t)=sum_(r=1..n)r^{-t} mod p`, and

```
A(b) = sum_j j*H_(jb)^(1) - d0*H_b^(1) - q     (mod p),
B(b) = -[sum_j j^2*H_(jb)^(2)-d0*H_b^(2)]/2 + A(b)^2/2 (mod p),
C(b) = lambda*b + 1,
L1    = sum_b C(b)*u(b)*A(b)   (mod p),
L1u   = sum_b u(b)*A(b)        (mod p),
L2    = sum_b C(b)*u(b)*B(b)   (mod p),
c0=(M0/p) modp, c1=(M1/p) modp, m2=M2 modp.
```
All b-sums run 0..h, all field divisions are by p-units.

For the **original zero-valuation rectangle alone** define
`R_J(p)=sum_(0<=a,b<=h) (lambda*(ap+b)+1)*u(ap+b)`. Then, for every prime p>=5 satisfying the two stated one-digit hypotheses,

```
R_J(p)=0 mod p^2,
R_J(p)/p^2 =
  c0*(c0+lambda*c1) + c1*L1 + m2*(L2+lambda*L1u)  (mod p).  (*)
```

**Proof.** On this rectangle all factorial carry indicators `c_j,delta_j` are zero and the carry factors `Gamma_j=1`. The previously proved exact p^4 digit formula expands the unit into `u(a)u(b)` times `1+p*a*A(b)+p^2*a^2*B(b)`, plus terms at p^2 **linear in a** arising from the next harmonic/Fermat-quotient digits; these linear terms vanish in the **aggregate modulo p^3**, as `M1=0 modp`. Do not claim this approximation is a termwise p^3 identity. Keeping the full weight `C(b)+p*lambda*a`, the double sum becomes, modulo p^3,
```
M0*(M0+lambda*M1)
 + p*M1*L1 + p*lambda*M1*M0
 + p^2*M2*(L2+lambda*L1u).
```
The p*lambda*M1*M0 term is divisible by p^3; divide by p^2 using both M0 and M1 divisible by p to get (*). This is a **conditional all-prime algebraic reduction**, not an all-prime proof of the two-stream congruence.

## Executed original arithmetic and discriminating values

An author-executed Python checker evaluated original low-index u(n) by the exact original coefficient recurrence, evaluated the moment expression and compared with a **separately coded full-index original p-adic recurrence**. The moment formula matched for each of 11 test primes p=13,19,37,43,61,67,109,139,211,373,1171, both original models (**22 finite cases**). For the first ten primes through 373 the independent full-index recurrence was also executed (**20 matched independent comparisons**). For p=1171 only the moment-based calculation was executed, not an independent high-index check.

For **p=373**:

| Source | M0/p mod373 | M1/p mod373 | M2 mod373 | Rectangle R/p^2 mod373 |
|---|---:|---:|---:|---:|
| original W216 | 304 | 318 | 173 | **284** |
| original S2304 | 50 | 224 | 336 | **257** |

The **signed ordinary valuation-zero rectangle** therefore contributes `284-2*257=143 mod373` to the p^2 digit. Combining with the earlier *independently measured* signed anomaly digit 4 and signed full ordinary+baseline digit 369 shows the **still distinct** positive-valuation ordinary+baseline source contributes `369-143=226 mod373`. Thus, exactly at this prime, the source-typed decomposition is

```
anomalous 4 + ordinary valuation-zero 143
     + ordinary positive-valuation and baseline 226
 = 373 = 0 mod373.
```

One-digit residues `M0=M1=0 mod373` alone would lose the nonzero p-adic first digits `(304,318)` and `(50,224)`, which genuinely contribute to (*). These are **finite exact source/observer witnesses**, not a universal telescope or native X6 equivalence.

## Next genuine scientific obligation

Use the p^4 carry formula and (*) to construct/defeat a finite **signed positive-valuation ordinary-source telescope**, separately for target classes 13,19 mod24, that cancels the already established anomaly. Return any proof to the original `Delta_p-R_p=0 modp` and the signed Clausen cutoff. The higher digit of any guessed telescope requires its own proof, not extrapolation from p=373.

Fixed-373 same-original-class H0/B0 divided-power `[X]U mod139129`, module rank, semilinear Frobenius direction and eta, signed odd Green/Hesse and κ, independently reproduced, remain **PENDING_OWNER / NOT_EXECUTED** (Enterprise Math #1559). The existing original onhour control dispatch `research-onhour-20261031-0205-dispatch-r15` is terminal FAILED / UPSTREAM_CODE_REVIEW_REQUIRED (kimi-query-bridge #6633); no duplicate was submitted, no maintenance session borrowed. Existing schedule/notification settings were not changed.
