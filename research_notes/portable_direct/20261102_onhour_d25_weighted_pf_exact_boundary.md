# D25 — original weighted W216 Picard–Fuchs exact boundary certificate

2026-11-02. **AUTHOR-DERIVED / HAND-PROVED / EXACT FINITE REPLAY / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_SOURCE_SYNC_DEBT.** Original TASK RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, immutable publication TP2-B6F4FC938FF94941C1B7, frozen scientific input c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Research lane chatgpt-research-onhour-enterprise-math-20260923; maintenance lane never used.

## Exact original object and theorem

For every prime p>3, work over p-integral rationals, put theta=x*d/dx and

\[
a_k=\frac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3}
=\frac{(2k)!(3k)!}{108^k(k!)^5},\qquad
G_p(x)=\sum_{k=0}^{p-1}(6k+1)a_k x^k.
\]

The frozen original 216-model full weighted truncation is **exactly** W(p-1)=G_p(1/2), with original weight 6k+1 and cutoff p-1. Define the weighted finite hypergeometric differential operator

\[
\mathscr M=\theta^3(6\theta-5)
-x(6\theta+7)(\theta+1/2)(\theta+1/3)(\theta+2/3).
\]

**Theorem (all primes p>3):**

\[
\boxed{\mathscr M G_p(x)=-(6p+1)(6p-5)(p-\tfrac12)(p-\tfrac23)(p-\tfrac13)a_{p-1}x^p} \quad\text{(exact rational polynomial)}.
\]

\[
\boxed{a_{p-1}\equiv-p^3\pmod{p^4}},\qquad
\boxed{\mathscr M G_p(x)\equiv(5p^3/9)x^p\pmod{p^4}},
\]

\[
\boxed{(\mathscr M G_p)(1/2)\equiv5p^3/18\pmod{p^4}}.
\]

For p>=7 the operator residual has exact p-adic valuation 3 and normalized scalar boundary digit 5/18 modulo p, nonzero. Exception p=5: (6p-5)=25 raises its exact valuation to 5; the stated mod-p^4 formula still holds (zero).

## Complete proof

The coefficient recurrence holds exactly for 1<=k<p:

\[
a_k/a_{k-1}=\frac{(k-1/2)(k-2/3)(k-1/3)}{k^3}.
\]

Writing g_k=(6k+1)a_k, cross-multiply **without inverting potentially nonunit 6k-5**:

\[
k^3(6k-5)g_k=(6k+1)(k-1/2)(k-2/3)(k-1/3)g_{k-1}.
\]

These are exactly the x^k coefficient cancellations of \(\mathscr M G_p\) for k=1,...,p-1 (constant term also zero). The x^p coefficient has only the negative shifted term, yielding the exact polynomial identity.

For each rising factorial (r/d)_{p-1}, with (r,d) in {(1,2),(1,3),(2,3)}, the sequence j+r/d for j=0,...,p-2 has exactly one factor divisible by p, because the excluded j=p-1 gives r-d nonzero mod p. Across all three rising factorials the exceptional factors are p/2,p/3,2p/3, in the latter two's order according to p mod3. Their product is p^3/9. Wilson's theorem plus Fermat gives for the remaining factors

\[
\prod_{j\ne j_*}(j+r/d)
\equiv d^{-(p-2)}\,(-1)/(r-d)
\equiv d/(d-r)\pmod p.
\]

The three products are 2,3/2,3, multiplying to 9. Hence the numerator after dividing by p^3 is 1 mod p. The denominator ((p-1)!)^3 is -1 mod p, proving a_{p-1}/p^3=-1 mod p. In the exact differential identity, (6p+1)(6p-5)=-5 mod p and the product (p-1/2)(p-2/3)(p-1/3)=-1/9 mod p. This yields \(5p^3x^p/9\pmod{p^4}\). Evaluate x=1/2, use 2^{-p}=2^{-1} mod p, and obtain 5p^3/18. All denominators are p-units for p>3. At p=5, 6p-5=25 supplies two extra p powers. QED.

## Executed check, exact scope

The independently runnable checker in this commit performs integer-only mod-p^4 recurrence tests for every one of **428 primes 5<=p<=3000** (**593390 checked inner coefficient indices**) and validates both exact boundary forms. An independent Fraction computation at p=5,7,13,19,37 confirms a_{p-1} modulo p^4. All assertions passed. Check summary JSON in same commit.

| p | a_(p-1) mod p^4 | [x^p] M G mod p^4 | M G(1/2) mod p^4 | normalized at-half digit mod p |
|---:|---:|---:|---:|---:|
| 5 | 500 | 0 | 0 | 0 |
| 7 | 2058 | 2058 | 1029 | 3 |
| 13 | 26364 | 4394 | 2197 | 1 |
| 19 | 123462 | 61731 | 96026 | 14 |
| 373 | 19304983524 | 2179594914 | 1089797457 | 21 |

## BRC observer and scientific significance

Input carrier: all original ordered indices k<=p-1, signed weights (6k+1), valuations and exact cutoff. The declared external arithmetic observer is M G_p modulo p^4, with optional x=1/2 evaluation; its future operation is division of the residual by p^3 then reduction mod p. The homogeneous equation M G_p=0 modulo p^3 forgets precisely the nonzero 5/9 boundary digit (5/18 at x=1/2) for all p>=7. **Retaining this digit is an actual BRC valuation/jet observer-safety use**, not a claim about the project's native X6 geometry or a different source model.

The mother scalar target remains open: \(\Delta_p-R_p=0\pmod p\) for p=13,19 mod24 has been reduced under accepted D24/CM0 to \(W(p-1)=p\pmod{p^3}\); a broader all-prime character congruence has finite checks but requires proof. This local theorem neither proves nor disproves that special-value congruence. A future terminating WZ or contiguous identity must preserve original triple (1/2,1/3,2/3), argument x=1/2, weight 6k+1, cutoff p-1 and modulus p^3; if differentiating to higher precision, the nonzero boundary from this theorem must be included. Check any candidate on p13,p19,p373 plus p5,p7 controls.

The original **native** p373 H0/B0 divided-power [X]U modulo 139129, module rank, actual semilinear Frobenius/eta, odd signed Green/Hesse/kappa and independent replay remain NOT_EXECUTED in support issue #1559, without a confirmed executor at 2026-11-02 read. No scalar surrogate discharges it.

Current Site read-only client service 0.6.11 reported research_authority_granted=false and write_relay_enabled=false; Source sync control UPSTREAM_CODE_REVIEW_REQUIRED, original request research-onhour-20261031-0205-dispatch-r15 CONTROL_REQUEST_NOT_FOUND. This is author-side GitHub research persistence only; no authenticated own session, CLAIM, run, Source checkpoint, formal Result or review/admission. Original scheduler/notifications unchanged.
