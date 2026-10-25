# D25/LIFT — corrected Clausen third Hasse port and exact fourth-band signed convolution

Date: 2026-10-25. Research lane: chatgpt-research-hourly-enterprise-math-20260923 (distinct from control maintenance). Formal Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is not changed.

**Status:** AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. This is an externally parameterized finite hypergeometric algebra statement, not a native CM or X6 experiment. It neither replaces nor upgrades the existing Source checkpoint or contribution history.

## Precise question and prior input

The already recorded source-corrected Clausen family replaces the fixed-denominator Jacobi series with a genuine parameterized Clausen port. Can its Hasse coefficient structure explain **each signed fourth-band original coefficient**, rather than only a collapsed fourth-band total? Here the known Clausen identity and prior original four-band decomposition are consumed input, not claimed anew.

Let p=6m+1 >=7 be prime, N=p-1. Work p-locally at x=m+t. For 0<=n<p define

\[
B_n(x)=\frac{(-x)_n(-2x)_n}{(\tfrac12-3x)_n\,n!},\quad
C_n(x)=\frac{(-2x)_n(-3x)_n(-4x)_n}{(\tfrac12-3x)_n(-6x)_n\,n!},
\]
\[
\beta_{n,k}=[t^k] B_n(m+t),\qquad
\gamma_{n,k}=[t^k] C_n(m+t).
\]

All lower denominator factors have p-unit constant terms for 0<=n<p, so the Taylor/Hasse coefficients lie in Z_(p). Set F_k(z)=sum_{n=0}^{p-1} beta_{n,k} z^n. As an external finite power-series identity, the **classical** Clausen square gives, exactly over Q,

\[
\boxed{\gamma_{n,k}=\sum_{j=0}^n\sum_{a=0}^k
\beta_{j,a}\beta_{n-j,k-a}\quad(0\le n<p,\ k\ge0).}\tag{1}
\]

This coefficient window is below the finite-truncation corner n=p; it does not authorize discarding the original ordered corner of the full truncated product.

## New result A: exact high-rank annihilation and first surviving two-port convolution

For each 4m+1 <= n <= p-1, the three numerator factors of C_n(m+t) have distinct simple zeros at indices 2m,3m,4m. Consequently

\[
\boxed{\gamma_{n,0}=\gamma_{n,1}=\gamma_{n,2}=0\quad\text{exactly},}\tag{2}
\]

whereas their third Hasse coefficient is **exactly**

\[
\boxed{
\gamma_{n,3}=
-\frac{24(-1)^m\,\prod_{q=2}^{4}(qm)!\,(n-qm-1)!}
{(\,1-p/2\,)_n(\,1-p\,)_n\,n!}.}\tag{3}
\]

No denominator or numerator is divided by a vanishing source coefficient. Formula (3) is nonzero over Q, and its reduction in F_p is also nonzero:

\[
\boxed{
\gamma_{n,3}\equiv
-24(-1)^m
\frac{\prod_{q=2}^{4}(qm)!\,(n-qm-1)!}{(n!)^3}
\pmod p.}\tag{4}
\]

All factorials have arguments <p, hence are units.

By (1), for the same high-rank interval the **exact signed convolution** has first nonzero Hasse order three:

\[
[z^n]F_0^2=[z^n](2F_0F_1)
=[z^n](2F_0F_2+F_1^2)=0,
\]
\[
\boxed{\gamma_{n,3}=2[z^n](F_0F_3+F_1F_2).}\tag{5}
\]

Because F_1 has degree at most 2m, F_1^2 has degree at most 4m. Thus (2) also supplies the **exact high-rank signed-annihilation certificate**
\[
\boxed{[z^n]F_0F_2=0\quad (4m<n<p).}\tag{6}
\]
Individual terms of the F_0 F_2 convolution need not vanish; this is a source-sensitive signed cancellation, not a positive-weight support argument.

**Proof:** Separate each factor (-qx)_n at x=m+t into its unique vanishing factor -qt at j=qm and the remaining product. For q=2,3,4 the latter equals (-1)^{qm}(qm)!(n-qm-1)!, giving the factor (-2)(-3)(-4)(-1)^{9m}=-24(-1)^m. The two denominator Pochhammer products have p-unit constant terms. This proves (2) and (3). Reducing them modulo p replaces both lower Pochhammer factors by n!, proving (4). Apply the coefficientwise Clausen identity and the exact degree bounds for F_0 and F_1 to obtain (5)–(6). QED.

## New result B: rankwise fourth-band port to the original 3F2 coefficients

Write
\[
U_n=\frac{(1/3)_n(1/2)_n(2/3)_n}{(n!)^3}.
\]
At x_0=-1/6=m-p/6, C_n(x_0)=U_n *exactly*, with both lower denominators equal to 1. Formula (2) makes the Taylor remainder divisible by p^4 in the p-local ring. Therefore, for every 4m<n<p,

\[
\boxed{
\frac{U_n}{p^3}\equiv-\frac{\gamma_{n,3}}{216}
\equiv\frac{(-1)^m}{9}
\frac{\prod_{q=2}^{4}(qm)!\,(n-qm-1)!}{(n!)^3}\pmod p.}\tag{7}
\]

This is a **term-by-term** bridge between the genuinely source-corrected Clausen third Hasse derivative and the previously found fourth band. If
\(d_n=(6n+1)2^{-n}U_n/p^3\in\mathbb Z_{(p)}\),
then
\[
\boxed{
d_n\equiv
-\frac{6n+1}{108\,2^n}
[z^n](F_0F_3+F_1F_2)\pmod p.}\tag{8}
\]
Consequently, for the exact original fourth-band sum
\(B_3=p^3\sum_{n=4m+1}^{p-1}d_n\),
\[
\boxed{
\frac{B_3}{p^3}\equiv
-\frac1{108}\sum_{n=4m+1}^{p-1}
\frac{6n+1}{2^n}[z^n](F_0F_3+F_1F_2)
\pmod p.}\tag{9}
\]

Formula (9) retains the ordered rank N, **signed** Cauchy composition, Hasse derivative order, original weight 6N+1, factor 2^-N, and original-vs-terminating parameter ports. It is not an inference from scalar moments or positive BRC mass.

At the endpoint n=p-1, Wilson complementation of (4) gives
\[
\boxed{\gamma_{p-1,3}\equiv-m^{-3}\pmod p.}\tag{10}
\]
Indeed (2m)!(4m)!=-1 mod p and (3m)!^2=(-1)^{m+1} mod p, so (4) reduces to (10). Because 6m=-1 mod p, equation (7) gives U_{p-1}/p^3=-1 mod p and hence d_{p-1}=5 mod p. **That endpoint d=5 was already proved in the prior fourth-band note; it is a cross-method consistency check and is not credited as a new standalone result.**

## Reproducible finite certificate (author check, not independent review)

The adjacent script verifies the p-local Taylor identities in F_p[t]/(t^4) from **two distinct recurrences**: (i) corrected 2F1 and 3F2 rational coefficient recurrences at x=m+t, and (ii) the original hypergeometric 3F2 recurrence modulo p^4. It checks four Clausen Hasse orders for every rank 0<=n<p, the rankwise factorial formula and valuation for all 4m<n<p, equation (7), the signed sum (9), the endpoint and d=5. No floats, sampling, or original CM simulation.

Tested primes p=7,13,19,31,37,43,61,73,97,103,109,127,157,199,373. Total: 5,796 coefficient/Hasse comparisons and 478 high-rank terms, all PASS.

For p=13, the four high-rank triples (n, gamma_{n,3}, U_n/p^3, d_n) mod 13 are (9,8,12,2), (10,10,2,7), (11,5,1,4), (12,8,12,5). The signed band sum is 2+7+4+5=5 mod 13, reproducing the earlier B_3=10985 mod 28561. For p=19, the rankwise sum is 4 mod 19. These finite cases illustrate the general proof, not establish it.

## BRC/provenance and unfinished scope

**COMPOSE_APPLIED:** Use the typed signed rank-weight/Hasse-jet carrier, Cauchy composition, and future observer (6n+1)2^-n modulo p^4. Exact vanishing is claimed only for the explicit coefficients/observer and rank interval; it does not erase the original ordered cutoff corner or CM provenance. The native six-dimensional X6 world is the project frame, but the proved hypergeometric auxiliary identities have **no asserted X6 embedding or CM Frobenius transfer**.

The original all-target-prime D25/LIFT congruence and same-original-class H0/B0, [X]U mod p^2, Frobenius direction/eta and kappa bridge remain UNPROVED / NOT_RUN. No native Source CLAIM, authorized run, checkpoint, freeze or independent review is asserted by this portable artifact. Existing project Task/Source/claim and author history remain immutable.

**Next smallest mathematical action:** apply the exact high-rank annihilator (6) and rankwise two-port expression (8) to seek an actual finite signed telescoping/cancellation certificate for the lower-rank second-jet defect in the original mod-p^3 target. Check the ordered n>=p Clausen corner separately. Do not rederive endpoint d=5 or repeat finite scans in lieu of a uniform identity.
