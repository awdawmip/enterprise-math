# D24 second-digit LIFT: I0 parameter-jet compression and reflection no-go

Status: PROVED_DERIVATION_UNIT / LIFT_NOT_YET_CLOSED
Date: 2026-09-24
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7

## 0. Consumed frontier

Keep the already-published I0 terminating deformation. Let p=6m+1 and n=2m=(p-1)/3. Define

u_k=(6k+1)(1/2)_k(-n)_k(2/3)_k/((k!)^3 2^k),
A_k=H_n-H_{n-k},
B_k=H_n^(2)-H_{n-k}^(2).

The durable checkpoint has
S_0 congruent U_0-(p/3)U_1+(p^2/18)U_2 (mod p^3),
where U_0=sum u_k, U_1=sum u_k A_k and U_2=sum u_k(A_k^2-B_k), with the k=m source kept separately.

This note does not rederive that checkpoint. It tests the requested parameter-derivative and k -> n-k routes.

## 1. The three I0 carriers are one exact parameter jet

For an auxiliary parameter epsilon define the finite polynomial

F_n(epsilon) = sum_{k=0}^n (6k+1)(1/2)_k(-n+epsilon)_k(2/3)_k / ((k!)^3 2^k).

Since -n+p/3=1/3, the original lower shell is exactly

S_0 = F_n(p/3).

For k<=n, logarithmic differentiation of the finite factor (-n+epsilon)_k at epsilon=0 gives

[d/d epsilon] log(-n+epsilon)_k |0 = -A_k,
[d^2/d epsilon^2] log(-n+epsilon)_k |0 = -B_k.

Therefore

boxed: F_n(0)=U_0,
boxed: F_n'(0)=-U_1,
boxed: F_n''(0)=U_2.

Consequently the previous deformation is precisely the second-order Taylor jet

boxed:
S_0 congruent F_n(0)+(p/3)F_n'(0)+(p^2/18)F_n''(0) (mod p^3).

Every third and higher Taylor term contains p^3. Thus U_0,U_1,U_2 are not three unrelated sums: they are the 0th, 1st and 2nd coordinates of one source-preserving parameter jet.

The special fixed port k=m remains visible inside this jet. Its zeroth coordinate carries the explicit factor 6m+1=p; its first derivative contributes the already-published -(p^2/3)v_m A_m correction; its second derivative is p^3-invisible only after the p-adic observer is applied.

## 2. At epsilon=0 the base carrier is an alternating binomial transform

Using (-n)_k/k! = (-1)^k binom(n,k), put

a_k=(6k+1)(1/2)_k(2/3)_k / ((k!)^2 2^k).

Then

boxed:
U_0(n)=sum_{k=0}^n (-1)^k binom(n,k) a_k.

Let

f(t) = _2F_1(1/2,2/3;1;t),
y(t) = (1+6 t d/dt) f(t).

Since a_k is the coefficient of t^k in y(t) after t=z/2, the ordinary generating function of the base terminating carrier is

boxed:
sum_{n>=0} U_0(n) x^n
 = 1/(1-x) * y(-x/(2(1-x))).

This follows directly from sum_{n>=k} binom(n,k)x^n=x^k/(1-x)^(k+1). It is an exact reduction from the terminating weighted 3F2 base sum to a rational pullback of a Gauss 2F1 solution and its first theta derivative.

The Gauss equation

t(1-t)f'' + (1-13t/6)f' - f/3 = 0

implies, after eliminating f from y=f+6tf', the second-order equation

boxed:
6t(t-1)(6t-1)y'' + (78t^2-19t+6)y' + 2(6t-7)y = 0.

Thus the epsilon=0 base carrier lives in a two-dimensional holonomic Gauss system. The next proof search can differentiate/contiguously shift this system rather than treating U_0,U_1,U_2 as independent n-term populations.

## 3. Exact k -> n-k reflection is not an antisymmetric cancellation

For n=2m even, direct division gives

rho_{n,k}=u_{n-k}/u_k
 = [6(n-k)+1]/[6k+1]
   * 2^(2k-n)
   * (1/2)_{n-k}/(1/2)_k
   * (2/3)_{n-k}/(2/3)_k
   * (k!/(n-k)!)^2.

All displayed factors are positive rational numbers. The signs from (-n)_k and (-n)_{n-k} agree because n is even. Hence

boxed: rho_{n,k}>0 for every 0<=k<=n.

In particular u_{n-k} and u_k always have the same rational sign, so the naive involution cannot satisfy u_{n-k}=-u_k. At the fixed point k=m it would moreover require u_m=0, while u_m=p v_m is a nonzero rational source before reduction.

Therefore an exact rational reflection-pair cancellation is ruled out. This does NOT rule out a nontrivial contiguous/WZ certificate or a p-adic reflection after additional weighted operations; it only eliminates the simplest antisymmetric pairing route and preserves the fixed k=m source rather than silently cancelling it.

## 4. BRC information audit

Population: the finite I0 ports k=0..n, their source index, p-adic weight and first two parameter derivatives.

Allowed compression: (U_0,U_1,U_2) is replaced by the second-order jet (F_n(0),F_n'(0),F_n''(0)); this is lossless modulo p^3 because it is an identity, not a numerical fit.

Base-state compression: only epsilon=0 is further mapped to the binomial/Gauss generating system. The derivative coordinates are not discarded.

Forbidden shortcut: k<->n-k cannot be used as an exact signed cancellation. The fixed source k=m and derivative provenance remain live.

## 5. Deterministic algebraic regression

The companion exact-rational checker verifies for even n through 40: the two derivative coefficient identities term by term, the alternating binomial transform, the reflection-ratio formula and positivity, and the Gauss-derived differential equation by exact series coefficients. These finite checks are regression only; every boxed statement above is proved algebraically.

## 6. Next exact unit

Work in the single parameter-jet family F_n(epsilon). Derive a contiguous/differential relation that transports its first two epsilon derivatives through the rationally pulled-back Gauss system, and compare the resulting boundary terms with the already-persisted I1 derivative carrier b_1 J_m and signed I2 carrier (4/9)(6/p)K_m. Do not revisit naive antisymmetric reflection and do not collapse the fixed k=m source.
