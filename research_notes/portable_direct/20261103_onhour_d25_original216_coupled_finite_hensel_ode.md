# D25 — exact terminating third-order differential certificate for the ORIGINAL 216 three-strip Hensel jets

2026-11-03, Research lane `chatgpt-research-onhour-enterprise-math-20260923`, **AUTHOR-DERIVED / EXACT ALGEBRA PROVED / FINITE BIGINT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. This unit directly consumes the prior immutable author-side 2-jet three-strip proof `42ed8f8ad43ef5179c67dd50f6f688953c8178aa`. It is an actual next mathematical unit, NOT repetition of accepted D24 first-digit or a surrogate for native p373 H0/B0.

## Task and exact representation

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Mother goal remains the *unproved* original `W216(p-1)=p (mod p^3)` for prime `p=13,19 (mod 24)`, or equivalently frozen `Delta_p-R_p=0 (mod p)`.

Let `p=6r+1>=7`, `a=2r,b=3r,c=4r`, and

```
C_k(t) = ((-b+t/2)_k (-a+t/3)_k (-c+2t/3)_k)/(2^k (k!)^3).
```

The preceding proof established `C_k(p)=B_k` where `B_k=binom(2k,k)^2 binom(3k,k)/216^k`, and `C_k(t)=C_{k,0}+t C_{k,1}+t^2 C_{k,2}+...` with three exact root crossings. Let `theta=z*d/dz` and define

```
F_j(z) = sum_{k=0}^{c} C_{k,j} z^k, j=0,1,2.
F(t,z)=F_0(z)+t F_1(z)+t^2 F_2(z) in Z_(p)[t,z]/(t^3).
```

The coefficients and the source index are unchanged from the first mathematical unit. Degrees are **exactly** `deg F_0=a`, `deg F_1=b`, `deg F_2=c` (the indicated leading coefficient is p-unit).

## Theorem — homogeneous finite third-order jet system, including highest boundary

In the polynomial ring `Z_(p)[z]` define

```
A0(X)=(X-b)(X-a)(X-c);
A1(X)=(1/2)(X-a)(X-c)+(1/3)(X-b)(X-c)+(2/3)(X-b)(X-a);
A2(X)=(1/6)(X-c)+(1/3)(X-a)+(2/9)(X-b);
D0 = theta^3 - (z/2) A0(theta).
```

Then the following **three exact polynomial identities** hold, with no high-boundary defect:

```
[PROVED] D0 F0 = 0,
[PROVED] D0 F1 = (z/2) A1(theta) F0,
[PROVED] D0 F2 = (z/2) [A1(theta) F1 + A2(theta) F0].
```

Equivalently, with `A(t,X)=(X-b+t/2)(X-a+t/3)(X-c+2t/3)`, the genuinely terminating `t^2` polynomial solution satisfies

```
[theta^3 - (z/2) A(t,theta)] F(t,z) = 0 in Z_(p)[t,z]/(t^3).
```

**Proof.** The exact rational recurrence for `C_k(t)` is

```
2 k^3 C_k(t) = (k-1-b+t/2)(k-1-a+t/3)(k-1-c+2t/3) C_{k-1}(t).
```

For every `1<=k<=c`, taking coefficients of `t^0,t^1,t^2` yields the three displayed ODE coefficient equations. At the *only* potentially uncancelled coefficient `z^{c+1}`, the factor `A(t,c)` is divisible by `t` (root `c`), while `C_c(t)` is divisible by `t^2` (roots `a,b` already crossed), so their product is divisible by `t^3`. Thus **all three** boundary coefficients vanish exactly; the constant coefficient vanishes because `theta^3(1)=0`. There are no other coefficients. The degree statements follow from the nonzero product of the remaining constant factors after the first/second root crossings. QED.

This is a finite **coupled** (triangular 3-jet) operator, not a scalar ODE for the original weighted sum alone, and not an untruncated infinite-series ODE casually imposed on a cutoff. The boundary vanishing is verified for the exact finite polynomial, which is the load-bearing part of the certificate.

## Relation to original second-digit observation

Because `C_k(p)=B_k` and `C_{k,0}=C_{k,1}=C_{k,2}=0` for `k>c`,

```
[PROVED] W216(p-1) = [(1+6 theta)(F0+p F1+p^2 F2)]_{z=1} (mod p^3).
```

This law retains the index `k`, unsigned/weighted coefficient, original p-adic source valuations and all three first/second-jet ports. It can be composed without changing signs with the existing original 216 terminating upper-strip `4F3` at `H2`, but does not identify a finite original period with the external CM elliptic fiber. It does not prove the universal second-digit cancellation. The current open obligation remains

```
(L0+p(L1+M1)-p)/p^2 + L2+M2+H2 = 0 (mod p), for p mod24 in {13,19}.
```

The exact `p`-integral numerator divisibility on these classes follows from the already accepted first-digit D24 input.

## Executed certificate and BRC scope

The standalone Node.js/BigInt checker independently evaluates original integer-binomial coefficients at ALL `k<p` and verifies the jet reconstruction, checks all three finite differential identities coefficientwise through `z^{c+1}`, and verifies root-crossing support degrees and original weighted readout. Cases: primes `7,13,19,37,43,109,181,373`, **782 original coefficients** and **532 differential coefficient positions**, all PASS. Every modulus is `p^3`, with exact p-unit inverses. These are finite computational regressions, not the all-prime proof (the proof is the coefficient recurrence and terminal zero count above). At p373 the original sum is 373 mod 51895117, independently consistent with the prior 2-jet and high `4F3` records.

`BRC_COMPOSE_APPLIED`: the three retained source jets and their root-crossing filtration are a sufficient carrier for future weighted/derivative readouts through precision p^3. The z-differential operator is an auxiliary arithmetic coordinate, **not** a native ENTERPRISE X6 direction, native Frobenius, or the frozen H0/B0 experiment. This is a specialized original 216 result, not a newly claimed general-purpose tool family. The concurrent sibling reciprocal-index three-atom theorem is independent and concerns `B_k B_{p-1-k}`, not the unreflected original `B_k`.

**NEXT EXACT MATHEMATICAL ACTION:** try a terminating WZ or parameter-contiguous certificate using this exact triangular `(F0,F1,F2)` differential system and evaluation functional `(1+6theta)|_{z=1}`. Test a candidate against p13,p19,p373 with the signed three-strip sources, showing the divided second digit and retaining the upper `H2` 4F3. A scalar differential-jet/spectrum comparison alone cannot discharge the frozen LIFT. Separately, native p373 H0/B0 divided-power `[X]U mod139129`, module rank, true semilinear Frobenius/eta, kappa, signed observer and independent reproduction at issue #1559 remain `NOT_EXECUTED / PENDING_OWNER`.

Current native Source research authentication absent (`research_authority_granted=false`), exact continuation read `CONTROL_QUOTA`, original request `research-onhour-20261031-0205-dispatch-r15` not replayed. This document is GitHub *author-side proof evidence only*: no session, CLAIM, run, Source checkpoint, Result, review or admission has been claimed.
