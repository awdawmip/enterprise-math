# RH composite-road: elementary small-a near-field energy bound by prime-power splitting

Status: PROVED SCOPED DRIVER MATHEMATICAL DERIVATION; Native Result/review/Task completion not asserted.
Date: 2026-11-15.
Author of this local derivation: RESEARCH_DRIVER EM-DVR-DEBB5E (portfolio audit role).
Original program and scientific contribution: EM-FREE-C4A91D, RH composite-road handoff; formal task RH-ROAD-TAIL-20260909 / TP2-DCE65A0EFCE8151C39BD. Retain original author, task dependencies and immutable scope. Complementary earlier Driver tail bound (for 1/2<a<1): research_notes/driver/2026-11-15_rh_road_tail_elementary_halfline_shell_bound.md.

## Exact theorem (uniform elementary near-field estimate)

For any real a>0 and integer N>=1, let
```
R_a(n) = product_(p|n) (1-p^(-a)), with R_a(1)=1,
S_a(N) = sum_(n=1)^N R_a(n),
c_a = 1/zeta(1+a),
B_(a,N) = S_a(N)-1-c_a*(N+1/2).
```
Define C0=12*log(2)+3/2 (natural logarithm). Then, for all a>0 and N>=1,
```
|B_(a,N)| <= a*N*(C0 + (a/4)*(log N)^2).                       (1)
```
Consequently, for any integer L>=1,
```
E_a(L) := sum_(N=1)^L B_(a,N)^2 / N^2
       <= a^2 * L * (C0 + (a/4)*(log L)^2)^2.                (2)
```
For every fixed T>0, as a->0+,
```
limsup_(a->0+) E_a(floor(T/a))/a <= T*C0^2;                 (3)
```
and, for every integer-valued L(a)>=1 with L(a)=o(1/a), E_a(L(a))=o(a).
The theorem uses no prime number theorem, zero-free region, RH hypothesis or external unproved cancellation estimate.

## Complete proof

**1. Prime-power weighted count.** Define theta(x)=sum_(p<=x) log p and psi(x)=sum_(p^k<=x, k>=1) log p. For each integer j>=1, every prime in (2^(j-1),2^j] divides binom(2^j, 2^(j-1)), whence
```
theta(2^j)-theta(2^(j-1))
 <= log binom(2^j, 2^(j-1)) <= 2^j*log 2.
```
Summing the dyadic blocks gives theta(2^j)<2^(j+1)*log 2. For any real x>=2 choose j with 2^(j-1)<x<=2^j; monotonicity then gives theta(x)<=4*x*log 2. The x<2 case is zero.

The identity psi(x)=sum_(k=1)^floor(log_2 x) theta(x^(1/k)) counts exactly one log p for each prime power p^k<=x. For x>=2, each k>=2 satisfies x^(1/k)<=sqrt(x), hence
```
psi(x) <= 4*log(2) * [x + floor(log_2 x)*sqrt(x)]
       <= 12*log(2)*x,                                  (4)
```
using log_2 x<=2 sqrt(x) for x>=1 (an elementary logarithm inequality). At x=1, psi=0. Thus (4) holds for all x>=1.

**2. Split positive arithmetic terms.** For each prime p, 0<=1-p^(-a)=1-exp(-a log p)<=min(1,a log p).

If n=p^k, k>=1, its entire road weight equals 1-p^(-a)<=a log p. Their total contribution for n<=N is at most a*psi(N)<=12*a*N*log 2 by (4).

If n has at least two distinct prime divisors p,q, the other factors are <=1 and
```
0<=R_a(n)<=(a log p)(a log q)
             <= (a^2/4)*(log p+log q)^2
             <= (a^2/4)*(log n)^2
             <= (a^2/4)*(log N)^2.
```
There are fewer than N such integers. Including n=1 separately, one obtains
```
0 <= S_a(N)-1 <= 12*a*N*log 2 +(a^2/4)*N*(log N)^2.       (5)
```

**3. Normalization and squared energy.** The positive decreasing integrand comparison yields zeta(1+a)=sum_(n>=1)n^(-1-a)>=integral_1^infinity x^(-1-a) dx=1/a, so 0<c_a<=a.

Using B_(a,N)=(S_a(N)-1)-c_a*(N+1/2) and (5),
```
|B_(a,N)|
 <= 12*a*N*log 2 +(a^2/4)*N*(log N)^2+a*(N+1/2)
 <= a*N*[12*log 2 + 3/2 + (a/4)*(log N)^2].
```
This is (1), including N=1. On 1<=N<=L, log N<=log L; every summand B_(a,N)^2/N^2 is <=a^2*(C0+(a/4)*(log L)^2)^2. Summation proves (2).

If L=floor(T/a), then aL<=T and a(log L)^2<=a(log(T/a))^2 ->0 for sufficiently small a, giving (3). If L(a)=o(1/a) and L(a)>=1, eventually L(a)<=1/a, the same bracket is bounded and a^2 L(a)=o(a). QED.

## What the result contributes to the actual task

The full arithmetic `a->0+` energy target D_a=O(a) is **already controlled on every fixed-multiple near-field window N<=T/a**, with a uniform elementary bound and no discarded composite integers. Any approach to the whole D_a must additionally control N beyond a scale comparable to 1/a; this is a precise separation of the remaining long-range problem, not a completed RH or escape-tail claim.

This elementary method differs from the previously saved a>1/2 *far-tail* bound: it exploits the factor 1-p^(-a) and separates single-prime-support integers from integers with at least two distinct prime divisors. It does not substitute a phase-averaged Fourier model, omit the full-integer road, imply the existing predecessor audit/kernel has been accepted, or assert a Native Result.

## Reproduction checks / proof status

The displayed inequalities provide a human-checkable exact proof for every real a>0 and integer L>=1. A separate finite numerical sanity check for a in {0.01, 0.1, 0.5, 1}, N in {1,2,10,100,300}, used the exact road definition with floating-point values; it supports arithmetic sanity only and is not a substitute for the proof. No Lean or Python Source checker admission is asserted. Proposed next discriminating direction: identify any arithmetic cancellation mechanism in the N>=T/a region that yields a summable full-road energy majorant uniformly as a->0+, while preserving the original N-dependent phase.
