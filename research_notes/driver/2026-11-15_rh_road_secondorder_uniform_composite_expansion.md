# RH composite road: exact second-order small-a arithmetic coefficient with uniform cubic remainder

Date: 2026-11-15.
Status: SCOPED DRIVER MATHEMATICAL DERIVATION (direct symbolic proof and numerical sanity checks); **not** a native Result, an accepted independent review, an infinite tail estimate, or a proof of RH.
Derivative author: RESEARCH_DRIVER EM-DVR-DEBB5E. Original full-integer research program: EM-FREE-C4A91D; formal task RH-ROAD-TAIL-20260909 / TP2-DCE65A0EFCE8151C39BD. The original Researcher identity/ownership and all earlier contributors remain separate. This note extends the existing first-order paper at commit 049192c481c7f5c9e838772ab08e2afa95a354e9; its use must preserve that source and its claims.

## Definitions and theorem

For a>0 let R_a(1)=1 and R_a(n)=product over distinct p|n of (1-p^{-a}); S_a(N)=sum_{n<=N}R_a(n), c_a=1/zeta(1+a), and B_{a,N}=S_a(N)-1-(N+1/2)c_a. Let

- psi(N)=sum_{p^k<=N, k>=1} log p (prime powers, each integer counted once);
- H_2(N)=sum_{n<=N, omega(n)=2} (log p_n)(log q_n) - (1/2)sum_{p^k<=N,k>=1}(log p)^2, where p_n,q_n are the two **distinct** prime divisors of n in the first sum;
- gamma=Euler's constant, omega(n)=number of distinct prime divisors.

All logarithms are natural. The road includes every integer, including prime powers, semiprime supports with arbitrary exponents, and integers supported on >=3 distinct primes.

**Theorem (uniform second-order expansion).** For every real 0<a<=1 and integer N>=1,

B_{a,N}
 = a [psi(N)-N-1/2]
 + a^2 [H_2(N)+gamma (N+1/2)]
 + T_{a,N},

with the explicit error bound

|T_{a,N}| <= a^3 [ (N/6)(log N)^3 + 9(N+1/2) ].

In particular, for each fixed positive integer N, the coefficient of a^2 is **exact**, and the displayed bound requires neither the prime number theorem nor any zero-free region.

## Proof I: the complete arithmetic road and its third derivative

Write f_n(a)=R_a(n), with distinct prime divisors p_1,...,p_r and x_j=log p_j. Each g_j(a)=1-exp(-a x_j) has |g_j(a)|<=1 for a>=0 and |g_j^{(k)}(a)|<=x_j^k for every k>=1. Generalized Leibniz therefore gives

|f_n'''(a)| <= sum_{k_1+...+k_r=3} [3!/(k_1!...k_r!)] product_j x_j^{k_j}
= (sum_j x_j)^3 <= (log n)^3

for n>=2. Taylor's theorem at a=0 consequently gives a uniform pointwise remainder <= a^3(log n)^3/6, without assuming a log n is small.

The coefficients f_n'(0), f_n''(0)/2 have exact support:

- omega(n)=1, i.e. n=p^k: f_n'(0)=log p and f_n''(0)/2=-(log p)^2/2;
- omega(n)=2: f_n'(0)=0 and f_n''(0)/2=log p log q;
- omega(n)>=3: both coefficients vanish;
- n=1: f_1(a)=1, both coefficients and remainder vanish.

Summing over all 1<=n<=N proves

S_a(N)-1 = a psi(N)+a^2 H_2(N)+U_{a,N},
|U_{a,N}| <= (a^3/6) sum_{2<=n<=N}(log n)^3
            <= (a^3 N/6)(log N)^3.

This is a finite exact identity and bound: no class of composite integers has been removed from the original road.

## Proof II: explicit normalization estimate

For 0<=a<=1 put g(a)=zeta(1+a)-1/a for a>0, and g(0)=gamma. The identity

g(a)=sum_{n>=1} [n^{-1-a}-integral_n^{n+1}x^{-1-a}dx]

holds for a>=0 with the limiting interpretation at zero; the series is uniformly convergent there. Since x^{-1-a} decreases, integral comparison yields 0<=g(a)<=1.

To bound its variation, differentiate a summand. The derivative of -log(x)x^{-1-a} with respect to x has absolute value at most

[1+2log(n+1)] / n^2  for x in [n,n+1], 0<=a<=1.

Thus the derivative of the nth bracket has this same bound, and termwise differentiation is justified by the convergent majorant. Since log(n+1)<=sqrt(n) for n>=1 (differentiate sqrt(x)-log(x+1)), we obtain

|g(a)-gamma| <= a sum_{n>=1}[1+2log(n+1)]/n^2
              <= a [zeta(2)+2zeta(3/2)] <= 8a,

using zeta(2)<=2 and zeta(3/2)<=3 by elementary integrals. Moreover,

c_a = a/(1+a g(a)),

so

c_a-a+gamma a^2 = a^2 [gamma-g(a)+a g(a)^2/(1+a g(a))],

and therefore |c_a-a+gamma a^2|<=9a^3 for 0<a<=1.

Subtracting (N+1/2)c_a from the finite arithmetic expansion in Proof I yields the theorem.

## Exact Dirichlet-series certificate for the second coefficient

For Re(s)>1, a>=0, absolute convergence and the divisor identity R_a(n)=sum_{d|n} mu(d)d^{-a} give

sum_{n>=1} R_a(n)n^{-s} = zeta(s)/zeta(s+a).

Termwise first and second differentiation at a=0 are justified by the majorant (log n)^2 n^{-Re(s)}. The first coefficient is -zeta'(s)/zeta(s), corresponding to the von Mangoldt function Lambda(n), and the second coefficient has Dirichlet series

sum_{n>=1} h_2(n)n^{-s}
 = (zeta'(s)/zeta(s))^2 - zeta''(s)/(2zeta(s)),

where h_2(n)=log p log q if omega(n)=2, h_2(p^k)=-(log p)^2/2, and h_2(n)=0 otherwise (including n=1). Thus H_2(N)=sum_{n<=N}h_2(n). This independently checks the exact arithmetic coefficient against the complete multiplicative Dirichlet series.

## Scope, tests, next frontier

Direct arbitrary-precision checks at N=1,3,10,100 and a=0.1,0.25,1 satisfy the stated cubic remainder bound; these are sanity checks only. The universal theorem follows from the calculus inequalities, not those samples.

This extension identifies the **second** finite-a derivative and its distinct-prime-support structure. Its uniform-in-N cubic bound is too large to control the escaping infinite energy tail when N grows super-polynomially in 1/a; no all-scale cancellation estimate follows. In particular it must **not** be used to claim H_2(N)/N -> -gamma merely from a formal Laurent expansion near s=1: that summatory statement requires its own Tauberian/prime-number-theorem argument. A useful next research unit is to test whether controlled, source-faithful summatory cancellation for H_2(N)+gamma N can improve the near-field approximation beyond the first-order Vinogradov–Korobov window, without changing the road or its normalization.

### Source provenance

- First-order arithmetic estimate: awdawmip/enterprise-math@049192c481c7f5c9e838772ab08e2afa95a354e9:research_notes/driver/2026-11-15_rh_road_small_a_primecount_firstorder_pnt_nearfield.md.
- Previously corrected near-field use of the Vinogradov–Korobov PNT error: awdawmip/enterprise-math@136a9756df0e69187b80178df798cc969af3398c:research_notes/driver/2026-11-15_rh_road_vinogradov_korobov_extended_nearfield.md.
- This note is Driver-authored standalone GitHub science; the original RH-ROAD-TAIL Task is not claimed, the source contributor is not reassigned, and no operational acceptance, Task completion, or mother-goal completion is asserted.
