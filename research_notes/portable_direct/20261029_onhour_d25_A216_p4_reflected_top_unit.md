# D25 / SECOND-DIGIT-LIFT — p^4 reflected top-tier reciprocity

2026-10-29. AUTHOR-DERIVED / EXECUTED / UNREVIEWED / NOT_ADMITTED. Portable external scalar arithmetic, not native H0/B0 or formal Source checkpoint.

Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3. This researcher lane uses chatgpt-research-onhour-enterprise-math-20260923, never a maintenance-lane identity. No authenticated claim/run/session is asserted.

## Exact statement (all primes p >= 5)

Let a_n = binom(2n,n)^2 binom(3n,n) / 216^n = (2n)!(3n)! / [(n!)^5 216^n] and w_n=(6n+1)a_n, in Z_(p). Define R=floor((p-3)/3). For 0<=r<=R put n=p-1-r. Then v_p(a_n)=3 and

\[
\boxed{\frac{a_{p-1-r}}{p^3}\equiv
-2\,216^r\frac{(r!)^5}{(2r+1)!(3r+2)!}\pmod p.}\tag{T1}
\]

\[
\boxed{\frac{w_{p-1-r}}{p^3}\equiv
2(6r+5)\,216^r\frac{(r!)^5}{(2r+1)!(3r+2)!}\pmod p.}\tag{T2}
\]

Multiplication by the original low-index a_r gives a reciprocal-source identity with only p-unit denominators:

\[
\boxed{
\frac{w_{p-1-r}}{p^3}\,a_r
\equiv\frac{2(6r+5)}{(2r+1)(3r+1)(3r+2)}\pmod p.}\tag{T3}
\]

For the original cutoff n<p and signed weight,

\[
\boxed{\frac1{p^3}\sum_{n=\lceil2p/3\rceil}^{p-1}w_n
\equiv 2\sum_{r=0}^{R}(6r+5)216^r
\frac{(r!)^5}{(2r+1)!(3r+2)!}\pmod p.}\tag{T4}
\]

No BRC/X6 native-dimensional correspondence is claimed: this reflection preserves exactly this scalar valuation and signed-observer horizon. Original H0/B0 ranks, operator, GH sign and odd Green/Hesse remain independent sources.

## Proof

For a in {1,2} and 0<=b<p, the factorial p-unit block formula from Wilson's theorem is
(ap+b)!/p^a = (-1)^a a!b! (mod p), where the quotient is an integer. For n=p-1-r and the stated range, p<=2n<2p, 2p<=3n<3p, n<p, giving exactly three numerator p factors and no denominator p factors. Thus

\[
a_n/p^3\equiv -2(2n-p)!(3n-2p)!/[(n!)^5 216^n]\pmod p.
\]

Using (p-1-s)! = (-1)^{s+1}/s! (mod p), we get
(2n-p)!=1/(2r+1)!, (3n-2p)!=(-1)^{r+1}/(3r+2)!,
n!=(-1)^{r+1}/r!, and 216^{-n}=216^r (mod p).
The signs cancel, proving T1. The original weight 6n+1=-(6r+5) (mod p) proves the positive-sign T2. The identity
a_r=(2r)!(3r)!/[(r!)^5 216^r]
proves T3, and exact reindexing of the upper tail proves T4. The domain ensures 3r+2<p, so no illicit division. For p=1 (mod 6), 6r+5 is a unit and every weighted term has valuation exactly 3; other classes retain possible extra p in the signed weight.

This identifies the precision-one-higher (p^4) source previously discarded in the proved p^3 four-tier identity; it does NOT reproach that earlier theorem nor solve the frozen five-port p^3 target.

## Executed exact integer certificate and sharpness

The companion standard-library program d25_a216_p4_reflected_top_unit_20261029.py was executed on every 237 prime 5<=p<1500. It checked 54,892 original reflected pairs against both independently calculated factorial and low-index identities, and separately reconstructed the original literal binomial sums at p=13,19,373. All passed.

For S_p=sum_{n=0}^{p-1}w_n and chi=(-3/p), the earlier conjecture S_p=p chi (mod p^3) was also checked for these 237 primes; this part is finite evidence, **not proof**. The exact p^4 deviations and top-tier contributions are:

| p | top terms | top tail/p^3 mod p | (S_p-p chi)/p^3 mod p | S_p mod p^4 |
|---:|---:|---:|---:|---:|
| 13 | 4 | 5 | 9 | 19786 = 13+9*13^3 |
| 19 | 6 | 4 | 12 | 82327 = 19+12*19^3 |
| 373 | 124 | 278 | 228 | 11832087049 = 373+228*373^3 |

Consequently the tempting stronger universal S_p=p(-3/p) (mod p^4) is FALSE already for target primes 13 and 19. The p^3 statement is unaffected. In the 237-prime finite sample, the upper-tail quotient vanished only for p=5,23,53,431,1327 and the whole p^4 defect vanished only for p=5. No universal classification follows.

Executed script SHA256 4885332fab039ae4b17849ee75cde416ec8108dd6ee638acc1491b79d2a6ba0c; exact Git blob d71e52b9c905c83e4db30467926000f37ca208e2. Observed stdout: PASS_A216_P4_REFLECTED_TOP 237 primes 54892 pairs. This is author-side evidence, not independent review.

## Preserved outstanding obligations

The frozen first-five-port hard target for every p=13,19 (mod24) remains T00+T01+T02+T10+T11 = p-p^2 Theta_p (mod p^3). Next: genuinely character-sensitive WZ/CM or independent finite-sum evaluation of these existing source ports, rather than another already-completed digit-tier theory. Native p=373 same-original-class H0/B0 divided-power [X]U mod139129, module rank, actual semilinear Frobenius/eta, signed odd Green/Hesse, kappa, Delta_p-R_p and independent reproduction remain NOT_EXECUTED here. Support issue #1559 is a capacity intake, not an executable Result.

This author-side GitHub source is **NOT** a canonical session/CLAIM/open, Source execution checkpoint, Result or independent review. The connected Site on 2026-10-29 is read-only for this subject; native registration/checkpoint requires separate authorized research capability, retained as REGISTER_PENDING / SYNC_DEBT. No science pin, P000 or previous writer ownership is changed.
