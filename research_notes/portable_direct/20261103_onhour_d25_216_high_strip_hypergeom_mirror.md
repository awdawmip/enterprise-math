# D25 | Original 216 p² upper strip as a terminating 4F3 mirror

2026-11-03 (+08). AUTHOR-DERIVED / ALGEBRAICALLY PROVED / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT. Logical Research lane: chatgpt-research-onhour-enterprise-math-20260923. Frozen task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, scientific input pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research context main@6ee763e4f675bbab86e1d95aa1f9624d565f2a4d; predecessor author-side frontier 1365a0da0b59597abc390000ded4983991e0ebfb. No native session or CLAIM was acquired.

## Frozen original 216 source

For every prime p=6r+1 >= 7 let h=3r=(p-1)/2 and L=4r=floor(2p/3). All statements below are in the localization at p or the reduction field F_p. Put

b_k=binom(2k,k)^2 binom(3k,k) 216^(-k), a_k=(6k+1)b_k, W(N)=sum_{k=0}^N a_k.

The inherited original factorial valuation theorem gives v_p(b_k)=2 for h<k<=L and v_p(b_k)>=3 for L<k<p. Retain k, original weight, sign, p² quotient, future summation and differentiation. Write chi=(6/p), theta=x d/dx, and

c_t=(1)_t (5/6)_t (7/6)_t / ((3/2)_t^3 2^t), 0<=t<r,
R_p(x)=sum_{t=0}^{r-1} c_t x^t in F_p[x].

All finite denominators are units. This is the terminating mod-p specialization of 4F3(1,1,5/6,7/6; 3/2,3/2,3/2; x/2), where 7/6 = 1-r in F_p.

## Theorem A (proved): exact normalized source coefficients

For 1<=s<=r,

b_(h+s)/p² = (chi/9)c_(s-1) (mod p).                                               (A1)

The original signed high-strip observation is therefore

A_p := sum_{k=h+1}^{L} a_k/p² = (chi/9) [(4+6theta)R_p(x)]_(x=1) (mod p).             (A2)

Proof. Set U_s=b_(h+s)/p² mod p. At s=1, since 2(h+1)=p+1 and 3(h+1)=p+h+2, Wilson's theorem yields (p+1)!/p=-1 and (p+h+2)!/p=-(h+2)! mod p. Substitution in the original exact factorial coefficient gives

U_1=(h+2) / (216^(h+1) ((h+1)!)^4) (mod p).

Wilson gives (h!)²=(-1)^(h+1) and hence ((h+1)!)^4=1/16 (mod p), while h+2=3/2 mod p. Euler's criterion gives 216^h=(6/p)=chi. Therefore U_1=24 / 216^(h+1)=chi/9 mod p.

For 1<=s<r and k=h+s, the original rational adjacent coefficient ratio reduces to

U_(s+1)/U_s = [(2k+1)(2k+2)(3k+1)(3k+2)(3k+3)]/[216(k+1)^5]
             = s(6s-1)(6s+1)/[9(2s+1)^3] mod p.

This is exactly c_s/c_(s-1). Every denominator is a p-unit and c_0=1, establishing A1 termwise. The original weight becomes 6(h+s)+1=3p+6s-2=6(s-1)+4 mod p, yielding A2. Neither A1 nor A2 needs CM0. For p=13 mod24, chi=-1; for p=19 mod24, chi=+1. QED.

## Theorem B (proved): a homogeneous terminating differential certificate

The entire polynomial R_p in F_p[x] satisfies

[ theta(theta+1/2)^3 - (x/2)(theta+1)^2(theta+5/6)(theta+7/6) ] R_p(x) = 0.    (B1)

Proof. The coefficient ratio is

c_t/c_(t-1) = t(t-1/6)(t+1/6) / [2(t+1/2)^3], 1<=t<r.

This cancels the coefficient at x^t for 1<=t<r. The constant coefficient vanishes by theta. The sole possible upper-boundary term is x^r, proportional to (r+1/6)=p/6=0 in F_p. Every higher coefficient is zero. Thus B1 holds as a complete polynomial identity, with its natural termination boundary, not just a formal infinite-series relation. QED.

## Exact mother-goal consequence and open proof obligation

Using the inherited original-source valuations,

W(p-1) = W(h) + p² (chi/9) [4R_p(1)+6(theta R_p)(1)] (mod p³).                (C1)

On the frozen D25 target primes p=13 or 19 mod24, the accepted first-digit theorem gives W(h)=p mod p². Therefore the still OPEN uniform second-digit identity is precisely

(W(h)-p)/p² ?= - (chi/9) [4R_p(1)+6(theta R_p)(1)] (mod p).                   (OPEN-C2)

B1 gives a genuine order-four finite-field operator with a vanishing high boundary; it is not by itself a proof of OPEN-C2. The next scientific unit should seek a terminating WZ/contiguous or CM period comparison for the p-adic half-cutoff carry and *both separate* mirror jets R_p(1) and theta R_p(1). Preserve the independent 2304 comparative route and p=181 cancellation as regression; no equality between 216 and 2304 original coefficients is assumed.

## Actually executed integer verification, finite scope only

The companion standard-library script d25_reflected_high_strip_20261103.py independently computes the original binomial coefficients mod p³ and the mirror using a finite-field recurrence. It has been run on every 148 primes 7<=p<=2000 with p=6r+1, covering 22,952 original upper-strip positions. It checks A1 term by term and EVERY coefficient of the homogeneous polynomial B1 including the x^r boundary. It recomputes W(h) directly for 77 target primes and checks the OPEN-C2 congruence only on this finite set (77/77 PASS); this is not a general proof.

Sample original-source observer coordinates (all modulo p):
- p=13, chi=-1: half carry 3, mirror (value,theta)=(2,1), high 10.
- p=19, chi=+1: half carry 10, mirror=(15,13), high 9.
- p=181, chi=-1: half carry 29, mirror=(131,107), high 152.
- p=373, chi=-1: half carry 107, mirror=(121,142), high 266; 107+266=373.
- p=1171, chi=+1: half carry 123, mirror=(635,368), high 1048.

BRC/Enterprise-coordinate usage: COMPOSE_APPLIED to ordered original 216 indices, weighted source, precise p² valuation, Legendre character, reversible coefficient recoding and two operator jets. This period is a scoped external arithmetic observer, not a new native X6 spatial direction; no unjustified quotient of joint information is taken.

## Durable continuation and native independent benchmark

Mother goal: Delta_p-R_p=0 mod p for every prime p=13,19 mod24, equivalent to W(p-1)=p mod p³. The exact frozen publication, proof strength and independent-lane authorship are unchanged. Inherited prior unit: 216/2304 half-cutoff source strips, now the high original 216 strip has a terminating 4F3 carrier and homogeneous ODE; its half carry comparison remains OPEN-C2.

Original native p=373 H0/B0 at issue #1559 is NOT_EXECUTED: coefficient [X]U mod139129, module rank, genuine semilinear Frobenius, signed Green/Hesse/kappa and independent replay remain pending. Control #1558 separate. Gateway 0.6.11 reports research_authority_granted=false, executor_binding_configured=false, upstream code review required and active quota 5/5. The old request research-onhour-20261031-0205-dispatch-r15 read as CONTROL_REQUEST_NOT_FOUND and was not reissued. No native session/claim/run/checkpoint/Result/review exists for this authored unit. Existing historical staging artifacts remain isolated. Formal Source registration/admission remain pending authorized execution. This author GitHub note is a mathematical evidence checkpoint only.
