# D25 — unified original-216 upper strip and signed probe (2026-11-03)

Role: TASK_RESEARCH (author-side); logical lane chatgpt-research-onhour-enterprise-math-20260923, separate from maintenance chatgpt-hourly-enterprise-math-20260921. Status: AUTHOR-DERIVED / ALGEBRAICALLY PROVED (Theorems A–C) / FINITE EXACT CHECKED (signed conjecture) / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT.

Frozen task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Mother target: Delta_p-R_p=0 (mod p) for primes p=13,19 (mod 24), equivalently the ORIGINAL weighted 216 sum W(p−1)=p (mod p³). Existing accepted D24 first-digit and previously author-proved p=6r+1 mirror are inherited, not re-proved or re-admitted.

For prime p>3, write B_k=binom(2k,k)^2 binom(3k,k)/216^k=(2k)!(3k)!/[(k!)^5 216^k], W(n)=sum_(k=0)^n (6k+1)B_k, h=(p−1)/2, L=floor(2p/3), r=L−h. Let chi=(6/p) and sigma=(-3/p), Legendre symbols. Then r=(p−sigma)/6; sigma=+1 for p=1 mod6 and −1 for p=5 mod6.

## Theorem A (PROVED): original p-adic band filtration

For 0<=k<p, v_p(B_k)=floor(2k/p)+floor(3k/p), since k! and 216 are p-units and 2k<2p, 3k<3p. In particular v_p(B_k)=2 for h<k<=L and v_p(B_k)>=3 for L<k<p. Thus the p² contribution of the original upper strip is precisely the second digit that survives in W modulo p³.

## Theorem B (PROVED): unified finite 4F3 high mirror for every p>3

In F_p define c_t=(1)_t(5/6)_t(7/6)_t / [(3/2)_t^3 2^t] for 0<=t<r, R_p(x)=sum_(t=0)^(r−1) c_t x^t, theta=x d/dx. All denominators are units. Then for every 1<=s<=r,

B_(h+s)/p² = (chi/9)c_(s−1) (mod p),

H_p := sum_(k=h+1)^L (6k+1)B_k/p² = (chi/9)[4R_p(1)+6(theta R_p)(1)] (mod p),

and hence for the ORIGINAL full weighted sum,

W(p−1) = W(h) + p²(chi/9)[4R_p(1)+6(theta R_p)(1)] (mod p³).

PROOF. At the first position k=h+1, 2k=p+1 and 3k=p+h+2. Wilson gives (p+1)!/p=−1 and (p+h+2)!/p=−(h+2)! modulo p. Therefore B_(h+1)/p²=(h+2)/[216^(h+1)((h+1)!)^4] modulo p. Wilson also gives (h!)²=(−1)^(h+1), whence ((h+1)!)^4=1/16; h+2=3/2; Euler gives 216^h=chi. The first normalized coefficient equals 24/(216 chi)=chi/9.

The exact coefficient ratio B_(k+1)/B_k equals
(2k+1)(2k+2)(3k+1)(3k+2)(3k+3)/[216(k+1)^5].
For k=h+s and 1<=s<r, both coefficients have valuation exactly 2. Mod p, k=s−1/2, so the normalized ratio is
s(6s−1)(6s+1)/[9(2s+1)^3] = c_s/c_(s−1).
Each denominator is invertible. The original weight 6(h+s)+1 reduces to 6(s−1)+4. Summing gives H_p, and Theorem A removes all later terms modulo p³. This argument treats BOTH p=6r±1; no first-digit or CM hypothesis is used. QED.

## Theorem C (PROVED): full polynomial terminal differential equation

In F_p[x], R_p satisfies the exact identity
[theta(theta+1/2)^3 − (x/2)(theta+1)^2(theta+5/6)(theta+7/6)]R_p(x)=0.
The inner coefficients cancel by c_t/c_(t−1); the constant coefficient is zero. The only possible terminal x^r coefficient is proportional to r²(r−1/6)(r+1/6)c_(r−1). When p=6r−1, r−1/6=p/6=0; when p=6r+1, r+1/6=p/6=0. Thus the terminal coefficient also vanishes. This proves a full finite polynomial identity, not an infinite-series truncation assumption. QED.

The opposite upper Pochhammer parameter supplies the terminal zero in the two prime classes. The previous p=6r+1 result is reused at its exact statement; the p=6r−1 extension and all-class formulation are the new mathematical contribution.

## Supplemental p=6r−1 three-jet port (PROVED)

For p=6r−1 put a=2r−1,b=3r−1,c=4r−1 and
C_k(t)=(-b+t/2)_k(-a+t/3)_k(-c+2t/3)_k/[2^k(k!)^3].
Then C_k(p)=B_k exactly, since the parameter values become 1/2,2/3,1/3. The Taylor jets F_j(x)=sum_(k=0)^c [t^j]C_k(t)x^k, j=0,1,2, have degrees a,b,c and satisfy, in Z_(p)[t,x]/(t³),
[theta³−(x/2)(theta−b+t/2)(theta−a+t/3)(theta−c+2t/3)](F_0+tF_1+t²F_2)=0.
The coefficient recurrence proves the internal equations. At degree x^(c+1), C_c(t) is divisible by t² (roots a,b already crossed), while the final operator factor is divisible by t (root c), so no terminal remainder occurs mod t³. An independent Python exact-integer checker ran this finite construction on 12 p=5 mod6 primes, checking 1,056 original positions and 724 complete ODE coefficients, all PASS. This is an auxiliary p-adic coordinate, not a native X6/H0/B0 experiment.

## Exact finite observation: global signed candidate remains OPEN

The companion executable independently computes every original B_k and the upper mirror for every one of the 1,227 primes 5<=p<=10000, covering all eight p mod24 classes, 956,066 high-strip coefficient positions. Every proven mirror identity and full/half decomposition passes; selected p=5,7,11,13,17,19,373 are independently crosschecked with direct integer binomial coefficients.

In the same *finite* complete tested set, the new signed conjecture W(p−1) ?= p sigma (mod p³), sigma=(-3/p), has 1,227/1,227 matches. It is NOT an all-prime theorem; no external published proof was verified. Exact examples: p=5 =>120 mod125 (−5), p=11=>1320 mod1331 (−11), p=13=>13 mod2197, p=19=>19 mod6859, p=373=>373 mod51895117.

Combining the proved mirror with the OPEN signed conjecture isolates the divided half carry:
[W(h)−p sigma]/p² ?= −(chi/9)[4R_p(1)+6(theta R_p)(1)] (mod p).
For the frozen p=13,19 mod24 class sigma=+1 and the quotient exists by the accepted D24 first-digit result. For other primes quotient divisibility is currently established only by the finite tests, not proved here.

BRC source/observer preservation: ordered original k, factorial valuation, exact original 6k+1 sign, chi/sigma character, and BOTH upper-mirror derivative observations are retained. No CM-to-native operator identification. Next smallest mother-goal unit: derive a *uniform terminating contiguous/WZ or p-adic CM proof of the original half-cutoff divided second carry* for p=13,19 mod24, with p=13,19,373 as exact discriminators; the all-prime signed extension is optional, not a prerequisite.

Native benchmark enterprise-math#1559 remains NOT_EXECUTED / PENDING_OWNER: original p373 H0/B0 [X]U mod139129, module rank, true semilinear Frobenius and eta, signed Hesse/Green κ, independent replay. Control support #1558 remains OPEN. Historical own recovery #6632 was a read-only projection with no opened own run/claim; original dispatch #6633 failed UPSTREAM_CODE_REVIEW_REQUIRED. Latest gateway status 0.6.11 has research_authority_granted=false and write_relay_enabled=false. No native session/claim/open/run/Source checkpoint/Result/review/admission is claimed or created by this author-side publication. Original scheduler/notifications untouched.
