# D25/LIFT — reflected divided-difference rank-two reduction of the high/low Cauchy bridge

2026-10-24 | New **exact** author-side algebraic research unit, `UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT`.

Parent objective `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`, immutable scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research lane `chatgpt-research-onhour-enterprise-math-20260923` alone; no maintenance lane identity/permission. Consumes the new [one-kernel seam and LOW-binomial Cauchy bridge](20261024_onhour_d25_high_seam_single_beta_cauchy_bridge.md) without changing the native task, terminal, or source. No Source CLAIM/run or benchmark is asserted.

## Precise new theorem

For `m>=1`, set
$$
I_m=\{1,2,\ldots,m-1\}\cup\{m+1,\ldots,3m-1\},\quad
w_r=1\ (r<m),\quad w_r=1/3\ (r>m),
$$
$$
\kappa(x)=-2+\frac4{6x+1}+\frac2{2x+1},\qquad
F_m(n)=\sum_{r\in I_m}\frac{w_r}{2^r(r+n)},
$$
$$
F_{m,6}=\sum_{r\in I_m}\frac{w_r}{2^r(6r+1)},\qquad
F_{m,2}=\sum_{r\in I_m}\frac{w_r}{2^r(2r+1)}.
$$
Write `(x)_(m+1)=x(x+1)...(x+m)` for the ordinary rising factorial. Then the **exact rational high-carrier identity**, true for *every* integer `m>=1` (no prime assumption), is
$$
\boxed{
\mathcal Z_m=
m\binom{2m}{m}2^m
\left[
\sum_{n=0}^m(-1)^n\binom mn\kappa(-n)F_m(n)
+\frac{4m!}{(-1/6)_{m+1}}F_{m,6}
+\frac{2m!}{(-1/2)_{m+1}}F_{m,2}
\right].}\tag{MR}
$$
Here `mathcal Z_m=sum_(r in I_m) w_r a_(m,r) kappa(r)`, so the original `Z_hi ≡ mathcal Z_m (mod p)` for `p=6m+1` prime by the preceding exact seam theorem. This **replaces a joint two-index kernel by one reflected LOW-binomial sum plus two scalar finite high moments**, preserving the sole high seam weight.

### Proof

The crucial exact **rank-two divided difference** is
$$
\boxed{\frac{\kappa(r)-\kappa(-n)}{r+n}
=-\frac{24}{(6r+1)(1-6n)}
-\frac4{(2r+1)(1-2n)}.}\tag{DD}
$$
This follows by subtracting `4/(6x+1)+2/(2x+1)` at `x=r` and `x=-n`; there is no approximation. Insert (DD) into the already proved exact Cauchy transform
$$
\mathcal Z_m=m\binom{2m}{m}2^m
\sum_{n=0}^m(-1)^n\binom mn
\sum_{r\in I_m}\frac{w_r\kappa(r)}{2^r(r+n)}.
$$
The reflected term becomes the first sum in (MR). The residual is a sum of the two separable products `F_(m,6)` and `F_(m,2)`. Complete both terminating binomial sums via the independent elementary partial-fraction identity
$$
\sum_{n=0}^m\frac{(-1)^n\binom mn}{x+n}
=\frac{m!}{(x)_{m+1}},\qquad
\sum_{n=0}^m\frac{(-1)^n\binom mn}{1-cn}
=-\frac{m!}{c(-1/c)_{m+1}},
$$
with `c=6,2`. The coefficients become `+4m!/(-1/6)_(m+1)` and `+2m!/(-1/2)_(m+1)`, respectively, proving (MR).

For `p=6m+1` prime, all denominators in (MR) are p-units: `r+n<=4m-1<p`, the omitted `r=m` is the only `6r+1` pole, the absent `r=3m` is the `2r+1` endpoint pole, and `6j-1,2j-1` for `0<=j<=m` are nonzero modulo `p`. Thus reduction modulo `p` is valid **without erasing either original seam or terminal**.

## Why the reduction matters, and what it does *not* establish

The high term is now a reflected Cauchy pairing with the same signed `(-1)^n binom(m,n)` that generates the LOW coefficients `b_n`, plus two explicitly evaluated rank-one moments. The defect from reflecting `\kappa(r)` to `\kappa(-n)` is **rank two** (equation DD). Hence any prospective LOW/high telescoping must account for these two moments; simply replacing the high kernel by its reflection is algebraically false.

The reflected kernel may be viewed as `F_m(n)=2^n[sum_(j=n+1)^(n+m-1) 2^(-j)/j + (1/3)sum_(j=n+m+1)^(n+3m-1)2^(-j)/j]`, making the original seam cut visible in shifted finite harmonic-type sums. This supplies concrete, finite quantities for a next `J_lo` matching attempt. Equation (MR) is a **strict reduction of FIN's high obligation**, not a proof that `D_finite=0 (mod p)`; the original normalized first digit, Fermat quotient, LOW jet, benchmark, and Driver checks remain untouched.

## Actual exact arithmetic validation

The companion `20261024_onhour_d25_high_seam_single_beta_cauchy_bridge_check.py` now checks (MR) against the original rational `sum w_r a_(m,r) kappa(r)` for **every m=1..13**, using exact `Fraction` with no floating tolerance; all pass. Earlier independently checked high p-unit recurrence agrees with the unified carrier for **all 80 primes p<=1000, p≡1 mod6**, including 45 target-class primes. These are author-side checks, not universal proof or independent review. Equations (DD) and the terminating binomial partial fraction prove (MR) algebraically at the stated exact scope.

**BRC interface applied:** signed LOW branch IDs indexed by `n`, high branch IDs `r`, seam weight `w_r`, and exact finite moments; `\kappa(r)-\kappa(-n)` is a typed algebraic reflection defect with exactly two separable port terms, not positive-mass cancellation, physical residual or P000 promotion. One scalar observer `U_hi/p mod p` is preserved. No native BRC run.

## Continuation; truthful control state

**Next smallest proof unit:** substitute (MR) in the full frozen `D_finite`; first test a terminating low-index discrete-antiderivative against `J_lo` and `(A-G+B)/p`, including both closed moment coefficients, seam/terminal and `q_p(6)`. Either prove all-target-prime zero or exhibit an exact obstruction; a rank reduction alone cannot discharge LIFT/JT2.

Source session/claim/run are still unavailable to this authenticated Sites identity; fresh Source exact read in this turn returned `CONTROL_QUOTA`. Research-lane old requests remain `recovery-status-20261023-1704-onhour-01` (unverified provisional ACTIVE), `continuation-d25-20261023-1709-onhour-01` (prerequisite rejected), and `dispatch-research-20261023-1710-onhour-01` (TimeoutExpired). Existing support Issue #1539 retains the required repair and acceptance test. Neither GitHub research preservation nor a research note establishes source-registered Researcher activity, native checkpoint, frozen Result or admission; old neutral staging remains isolated.
