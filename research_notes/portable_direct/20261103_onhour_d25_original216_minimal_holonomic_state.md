# D25 original-216: minimal rational holonomic order and p³-safe two-state transfer

2026-11-03 Asia/Hong_Kong. AUTHOR-DERIVED / EXACT PROOF / FINITE CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT. TASK_RESEARCH logical lane chatgpt-research-onhour-enterprise-math-20260923. This manuscript does not use the maintenance lane identity.

Frozen Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; scientific input pin c47e13e4aba0e006366f989d6334d443f6333ae3. Mother: distinct frozen Delta_p-R_p=0 mod p for p mod24 in {13,19}. Inherited original-216 bridge gives a still-OPEN full W(p-1)=p mod p³ obligation. Do not reprove accepted D24 first digit or prior Gauss/Clausen exact certificates.

## Theorem (all nonnegative integer n, characteristic zero)

Let b_n=(2n)!(3n)!/[216^n(n!)^5]=binom(2n,n)^2 binom(3n,n)/216^n; S_n=sum_{k=0}^n (6k+1)b_k and S_{-1}=0.

(A) The following order-two recurrence holds as an exact rational identity:

36(n+1)^3 (6n+1)(S_{n+1}-S_n)
= (6n+7)(2n+1)(3n+1)(3n+2)(S_n-S_{n-1}).

(B) There exists no rational function R(X) in C(X) with

(6k+1)b_k = R(k+1)b_{k+1}-R(k)b_k

for all sufficiently large nonnegative k. Consequently S_n has no first-order homogeneous linear recurrence with coefficients rational in n, for all sufficiently large n. Recurrence (A) is minimal in that *specific* rational-coefficient holonomic sense.

(C) For all k≥0, the following exact near-telescoping identity retains an unavoidable source remainder:

(6k+1)b_k = [(4-12(k+1))b_{k+1}-(4-12k)b_k]
              + [(66k²+113k+49)/(9(k+1)^3)] b_k.

### Proof

The exact quotient is rho(k)=b_{k+1}/b_k = (2k+1)(3k+1)(3k+2)/[36(k+1)^3]. Since S_{n+1}-S_n=(6n+7)b_{n+1} and S_n-S_{n-1}=(6n+1)b_n, elimination gives (A).

For (B), rational equality at infinitely many integer k implies the identity in C(k)

a(k)R(k+1)-36(k+1)^3R(k)=36(k+1)^3(6k+1),
a(k)=(2k+1)(3k+1)(3k+2).

Suppose R has a pole. Choose a pole alpha of maximal real part. R(k+1) is regular at k=alpha, because alpha+1 cannot be another pole. Therefore (k+1)^3 must cancel R's pole at alpha, and alpha=-1. Next choose a pole beta of minimal real part. At k=beta-1 the term R(k+1) has a pole, R(k) is regular, and the polynomial right side is regular; hence a(beta-1)=0. Thus beta lies in {1/2,1/3,2/3}. This contradicts Re(beta)≤Re(alpha)=-1. Therefore R has no finite poles: R is a polynomial.

If deg(R)=d, its leading nonzero term on the left has degree d+3 and coefficient -18 times the leading coefficient of R, while the right side has degree four and leading coefficient 216. Thus d=1; put R(k)=Ak+B. The polynomial coefficients of left-minus-right at degrees 4,3,2 are respectively

-18A-216;   -63A-18B-684;   -68A-81B-756.

The first two force A=-12 and B=4, but the third is -264 ≠0. No such R exists. Expanding with the best affine choice yields (C).

For the minimality claim, if S_n/S_{n-1}=q(n) were a rational function eventually, then S_n>0 and S_n-S_{n-1}=(6n+1)b_n>0 imply S_n/b_n=(6n+1)q(n)/(q(n)-1), rational in n. Accordingly R(k)=S_{k-1}/b_k would be rational in k and its finite difference would equal (6k+1)b_k, contradicting (B). QED.

## Direct p³ transport and terminal observer

For every prime p>3 and 0≤k≤p-2, set v_{k-1}=(S_{k-1},b_k)^T, v_{-1}=(0,1)^T. The exact transition (reduced mod p³ when desired) is

v_k = [[1,6k+1],[0,rho(k)]] v_{k-1}.

Here 36(k+1)^3 is a p-unit over the entire declared transition range. At k=p-1 we stop *before* dividing by p to form b_p. Direct Legendre valuation gives

v_p(b_{p-1})=floor((2p-2)/p)+floor((3p-3)/p)-5floor((p-1)/p)=1+2=3.

Therefore the original complete weighted finite sum admits the p³-safe, terminally valid observation

W(p-1)=S_{p-1} ≡ S_{p-2} = [1,0] v_{p-2} (mod p³).

This is an exact two-component state/observer carrier in ordinary arithmetic: the coefficient-generation direction and accumulated signed observation remain separately recoverable. Minimality above applies only to the declared rational-coefficient first-order recurrence class; no native X6 geometry, native H0/B0 Frobenius, or all-prime p³ congruence is inferred.

## Executed finite check and research consequence

The standard-library checker tests the quotient, order-two recurrence, exact remainder and affine -264 obstruction on 31 rational steps, then independently calculates the original weighted full sums using both binomial factorial and recurrence routes modulo p³ at primes 13,19,37,43,373. All assertions passed; the full sums on these five primes equal p mod p³, consistent with prior finite checks but not constituting an all-prime proof.

Scientific implication: an unparameterized single-summand rational Gosper certificate for the original 216 weighted sum is ruled out. The next scientific unit should test a genuinely two-state, CM-compatible modular intertwiner/eigenline or a *parameterized* two-index WZ mechanism that can carry both sources and the second p-adic digit. The previous exact second-carry equation (6AD-1)/p+h²+E=0 mod p remains OPEN universally. Construct and check a proposed intertwiner at p=13,19,373, then seek an all-prime proof on the original frozen scalar interface.

The original fixed p=373 same-class native H0/B0 benchmark remains NOT_EXECUTED / PENDING_OWNER in Enterprise Math issue #1559: actual [X]U modulo 139129, module rank, semilinear Frobenius, basis eta, odd Hesse/Green sign, original kappa and independently replayed Delta-R are still required. This author-side note is not a native surrogate.

## Publication and source separation

Canonical current read at author start: Enterprise Math main 84cb80025bd64c7d66f84b4634217416439474a1; global private rules main a27e1a68f7746578368b8cc860a6f94a01c720cf; scientific pin unchanged. Native gateway v0.6.11: research_authority_granted=false, executor_binding_configured=false, source code gate UPSTREAM_CODE_REVIEW_REQUIRED; active job quota 5/5. Original own recovery Issue awdawmip/kimi-query-bridge#6632 SUCCEEDED as read-only; original dispatch #6633 definitively FAILED for the code-review gate. No new Source session, claim, run, native checkpoint, Result, review or admission. Original staging remains independently preserved. Author-only GitHub evidence does not grant role-bound execution authority.
