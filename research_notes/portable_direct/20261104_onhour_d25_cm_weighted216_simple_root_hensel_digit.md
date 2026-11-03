# D25 — A simple CM zero of the ORIGINAL weighted-216 polynomial and a two-digit Hensel observer
Date: 2026-11-04 (+08). **AUTHOR-DERIVED / EXACT SCOPED PROOF / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.** This is author-side mathematics, not the original-class native H0/B0 experiment or a Source-authenticated checkpoint.

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, **frozen scientific pin** `c47e13e4aba0e006366f989d6334d443f6333ae3` (no rebase). Logical Research lane `chatgpt-research-onhour-enterprise-math-20260923`; no maintenance-lane identity. Consume the already accepted first digit, CM0 inert Legendre zero, finite Clausen, and the existing F4 signed source formula.

## Exactly defined object and first new theorem
For prime `p=6r+1>=7` put
`c_k=(1/2)_k(1/3)_k(2/3)_k/(k!)^3`,
`B_p(z)=sum_(0<=k<p) (6k+1)c_k z^k`,
`F_r(z)=_2F1(-r,-2r;1-p/2;z)`, and `z0=1/2`.
The **original** 216 scalar is `B_p(z0)=W_(p-1)`, since
`c_k 2^(-k)=binom(2k,k)^2 binom(3k,k)/216^k`.

**Theorem A, polynomial and all primes in scope:**
```
B_p(z) = F_r(z)[F_r(z)+12*z*F_r'(z)]       (mod p)  in F_p[z].
```
The terminating Clausen identity gives `F_r(z)^2=_3F2(-2r,-4r,-3r;1-p,1-p/2;z)`. Its coefficients modulo p equal `c_k` for `k<=2r`, while `c_k=0 (mod p)` for `2r<k<p` because `(1/3)_k` has a p factor. Apply `1+6z*d/dz` coefficientwise. This retains the actual original k-index and source valuation.

## Simple CM root, valid in both frozen residue classes
**Theorem B:** for every `p=13,19 (mod24)`,
```
B_p(z0)=0 (mod p);
d_p := B_p'(z0) = 24*[theta F_r(z0)]^2 != 0 (mod p);
theta=z*d/dz.
```
Indeed `F_r(z)=G_r(z)=P_(2r)(sqrt(1-z)) (mod p)`; the first equality follows from `1-p/2=1 (mod p)`, the second from
`P_(2r)(sqrt(1-z))=_2F1(-r,r+1/2;1;z)` and `r+1/2=-2r+p/2`.
The *consumed* CM0 inert theorem gives `P_(2r)(1/sqrt2)=0` at these target primes. It is a **simple root**: the Legendre differential equation
`(1-x^2)P''-2xP'+2r(2r+1)P=0` at `x^2=1/2` forces all derivatives to vanish if P=P'=0; since `deg P=2r<p` with p-unit leading coefficient (`4r<p`), this is impossible. Differentiating Theorem A at F=0 yields the displayed unit slope. Hensel's lemma therefore gives a **unique** `zeta_p in Z_p` with `zeta_p=1/2 (mod p)` and `B_p(zeta_p)=0`.

Consume the accepted first digit `B_p(1/2)=p (mod p^2)`. If
`zeta_p=1/2+p*a_p+p^2*b_p (mod p^3)`, then
```
a_p = -d_p^(-1) = -[24*(theta F_r(z0))^2]^(-1)  (mod p).
```

## Exact second-digit root comparison (new typed observer)
Fix the representative `a_p in {0,...,p-1}`; set `w1=B_p'(z0)`, `w2=B_p''(z0)`, and define the p-integral
```
beta_p = [p+p*a_p*w1+(p^2*a_p^2/2)*w2]/p^2   (mod p),
b_base = -d_p^(-1)*beta_p                      (mod p).
```
**Theorem C (exact equivalence of second digits):**
```
[B_p(1/2)-p]/p^2 = -d_p*(b_p-b_base)          (mod p).
```
Proof: substitute `z0+p a_p+p^2 b_p` into the original B polynomial; Taylor to order p^2 gives
`0=B(z0)+p*a*w1+p^2*(b*d+a^2*w2/2) (mod p^3)`.
The p^2 divisibility of beta uses `1+a*d=0 (mod p)`. Subtract the baseline containing p instead of B(z0). No unproved supercongruence enters the argument.

Hence, **using the already established frozen exact Clausen bridge**, the D25 mother target is equivalent to `b_p=b_base` for both residue classes, *when b_p is independently obtained from the true original polynomial root*. Computing b_p from the original full W just re-encodes the unresolved target; it is not yet a strict complexity reduction. A potential independent CM/Frobenius-to-original-root map must be proved with its native operator/basis before using this observer.

## Executed integer witness (separate from proof)
An independent local Python standard-library program computed F and its theta derivative from unit-ratio terminating hypergeometric coefficients, and B,B',B'' from the **unshifted original binomial 216 coefficient recurrence modulo p^3**. It separately substituted the Hensel root into the original polynomial with a distinct c-recurrence, rather than just its Taylor truncation. Exact modular arithmetic; no floating point. Coverage: all 148 primes `7<=p<=2000,p=1 mod6`; for all 77 target primes: P/G/F mod-p zero, nonzero slope, derivative identity, both root digits, literal root evaluation modulo p^3 and second-digit observer. All 77 passed. Finite W=p checks in these 77 are previous regressions, **not** an all-prime proof.

|p|theta F mod p|d mod p|Gauss-root first digit|original W-root a|original W-root b|b_base|zeta mod p^3|
|--:|--:|--:|--:|--:|--:|--:|--:|
|13|7|6|11|2|9|9|449|
|19|1|5|7|15|13|13|1549|
|373|294|211|290|274|329|329|19928085|

At 373, `W'(1/2)=29305 (mod 139129)`, `W''(1/2)=157 (mod 373)`, `W(1/2)=373 (mod 51895117)`. The local complete executable script and all 77 row results form this run's separately delivered evidence bundle; they are not represented as native Source artifacts.

## BRC and exact continuation
Carrier: original `(p,k,c_k,v_p(c_k),z)`; observers: literal W at 1/2, derivative slope/curvature, and the root's two p-adic displacement digits. Information is preserved for the **remaining scalar digit** by unit slope, under explicit local observer map and modulus; this is a classical auxiliary-coordinate construction and not an automatic X6/native promotion.

Mother objective: `Delta_p=R_p (mod p)` for p=13,19 mod24. Highest new author frontier: coefficientwise factorization, uniform simple zero, first Hensel displacement and an exact second-digit observer; 77 finite integer checks. **Unresolved:** uniform second-digit cancellation and original native p373 H0/B0 `[X]U mod139129`, rank, true semilinear Frobenius, basis/eta, odd signed Green/Hesse, kappa and independent replay (#1559; PENDING_OWNER at last read). Next exact action: test whether the *original-class* CM/native structure constructs this specific weighted-polynomial root digit independent of evaluating W; if yes, compare to b_base at 13/19/373 and derive the all-target identity; if the mapping fails, return to the original F4 signed boundary Green/WZ route without redefining the native object.

Current gateway 0.6.11: Research authority not granted, Site write relay disabled, historical exact dispatch request `research-onhour-20261031-0205-dispatch-r15` returned `CONTROL_REQUEST_NOT_FOUND` on this gateway (prior GitHub receipt `FAILED/UPSTREAM_CODE_REVIEW_REQUIRED`). No new dispatch, own session/claim/open/run/Source checkpoint/Result/review is asserted; native experiment remains NOT_RUN. Authenticated control roles are independent of this authorside file.