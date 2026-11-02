# D25 W216 — consume accepted CM0 to eliminate the first carry and identify the second

2026-11-02 (+08:00). AUTHOR-DERIVED / SOURCE-ALIGNED CONDITIONAL ALGEBRA / EXACT FINITE CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; unchanged frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Mother objective Delta_p-R_p=0 modp, p≡13,19 mod24.

## Inherited exact polynomial data and roles

Let p=6r+1>=7, theta=z d/dz, z0=1/2, and a_k=(1/2)_k(1/3)_k(2/3)_k/(k!)³. Define

\[
F_p(z)=\sum_{k=0}^{p-1}a_kz^k,\qquad
\ell_r(z)=\sum_{j=0}^{r}\binom rj\binom{2r}jz^j.
\]

The earlier independently published finite Clausen reduction is F_p(z)≡ell_r(z)² (modp) **coefficientwise**. Its original finite p² correction was already defined in the other research lane as

\[
R_A(z)=\frac{F_p(z)-\ell_r(z)^2}{p}\pmod p
\]
with coefficientwise division before reduction. This note consumes that exact previously established source and is not claiming a new Clausen theorem, a new CM0 theorem or author ownership of that earlier lane's work.

For target p≡13,19 mod24, consume the *already accepted* CM0 input ell_r(1/2)≡0 (modp). Put

\[
g=\frac{\ell_r(1/2)}p\pmod p,\qquad
j=(\theta\ell_r)(1/2)\pmod p,\qquad
q=[(1+6\theta)R_A](1/2)\pmod p.
\]

The earlier new three-band D25 note defines S0,S1,S2 for precisely the original b_k=a_k2^{-k} and W_p(4r)=sum_{k<=4r}(6k+1)b_k; its original-source theorem gives W=S0+pS1+p²S2 (modp³).

## Applied bridge proposition and proof

For every target prime, the first three-band carry obligation is already discharged by the cited earlier CM0 and finite Clausen results:

\[
\boxed{S_0\equiv0\pmod p.}
\]

Moreover, the original shortened cutoff's exact second-digit reduction is

\[
\boxed{\frac{W_p(4r)}p\equiv 12gj+q\pmod p.}
\]

Consequently, the remaining *second carry* statement W_p(4r)≡p (modp²) is **equivalent**, under the declared accepted CM0 input, to the concrete source-matched identity

\[
\boxed{12gj+[(1+6\theta)R_A](1/2)\equiv1\pmod p.}\tag{A}
\]

Proof. Since the original coefficient has p-adic valuation at least three for every 4r<k<=p-1, the original full F_p weighted evaluation W_full=(1+6theta)F_p(1/2) and shortened W_p(4r) agree modp². From the *exact* coefficientwise identity F_p=ell_r²+pR_A (modp²), apply (1+6theta) and evaluate at z0. The Leibniz rule gives

\[
(1+6\theta)(\ell_r^2)=\ell_r^2+12\ell_r\theta\ell_r.
\]

At CM0, ell_r(z0)=p g (modp²). Thus ell_r²≡0 modp² and 12ell_r theta ell_r ≡12p g j (modp²). Therefore W_p(4r)≡p(12gj+q) modp². Reduction modp shows S0=0 (this also follows directly from the polynomial square). Division by p proves the displayed bridge and (A). QED.

No second-digit vanishing conclusion was assumed. This is an exact conditional source reduction, not a universal proof of (A) and not a native original-class H0/B0 experiment.

## New executed original arithmetic cross-check

A newly executed independent Python standard-library checker built F_p from its original hypergeometric recurrence, independently built ell_r from integer binomials, formed the complete ell_r² polynomial (not merely its value), verified every coefficient of F_p-ell_r² is p-divisible, divided to get R_A, and checked the original weighted W_p(1/2) modulo p². Exact observations:

| p | g | j | q | 12gj modp | W_full/p modp |
|---:|---:|---:|---:|---:|---:|
| 13 | 7 | 7 | 11 | 3 | 1 |
| 19 | 6 | 1 | 5 | 15 | 1 |
| 37 | 21 | 24 | 21 | 17 | 1 |
| 43 | 4 | 20 | 30 | 14 | 1 |
| 373 | 340 | 294 | 49 | 325 | 1 |
| 1171 | 1082 | 544 | 177 | 995 | 1 |

Every entry reconstructs the direct original W_full/p and the finite target second-digit value 1; the six cases are tests, not the all-primes proof of (A). The complete code for this check was executed locally under the present conversation as d25_cm0_second_carry_reuse_20261102.py.

## BRC interface and next research action

The six-port p³ carrier of the predecessor note includes the original low/middle/upper provenance, valuation and signed weight. The current CM bridge reuses the full polynomial coefficientwise R_A because the future operation is differentiation, evaluation at z=1/2 and division by p. It is not valid to replace R_A by an untagged scalar before applying theta.

The next smallest **unresolved** step is the source-aligned all-target identity (A), using terminating/WZ/finite-field methods; the first carry S0 modp is inherited as solved. After (A), prove the third p³ carry cancellation via S2 and the second-order source deformation. Preserve the original full W216 normalization and cutoff, distinguish prior 2304 results and the separate Cauchy observer, do not duplicate earlier author contributions.

Control at 2026-11-02T13:26Z: Gateway 0.6.11 UPSTREAM_CODE_REVIEW_REQUIRED, native research_authority_granted=false. Existing historical recovery #6637, failed continuation #6638, support #1558 and pending native benchmark #1559 are unaffected. This source note is portable author-side evidence only, UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. No Source-native CLAIM/OPEN/checkpoint/Result. Research logical identifier remains chatgpt-research-hourly-enterprise-math-20260923, maintenance separated, scheduler untouched.
