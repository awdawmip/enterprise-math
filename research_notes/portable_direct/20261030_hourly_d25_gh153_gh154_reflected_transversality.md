# D25/LIFT GH-153–GH-154: critical-root transversality of the reflected tail

2026-10-30. **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.** Research lane `chatgpt-research-hourly-enterprise-math-20260923` (not maintenance). Parent D25/LIFT/JT2 OPEN; task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. P000 ACTIVE_LOCKED; immutable science pin `c47e13e4aba0e006366f989d6334d443f6333ae3`.

## Exact inherited object (do not conflate with original GH-3)

For each prime p=8m+3>=11, d=2m, D=binom(3m+1,m) in F_p, let h_0=1 and h_(j+1)=(4j+3)^3 h_j/((4j+4)(4j+5)(4j+6)), and

```
R_p(z) = sum_{j=0}^{2m} (8j+5) h_j z^{2m+1+j}/(2m+1+j).
```

GH-108/GH-121 established the author-side identity D² R_p'(z)=z^{2m} G(z)(16zG'(z)+5G(z)), where G(z)=z^m H_p((1+T)/8), T²=1-1/z. This R is the **reflected** polynomial, not GH-3's original truncated sum. GH-151 established, for W=(z-1)/(128z),

```
G(z)=z^m f(W),  f(W)=h_* Phi_p(W),
h_*=(-1)^m binom(2m,m) 4^{-m} !=0,
Phi_p(W)=sum_{k=0}^{m} u_k W^k, u_0=1,
u_{k+1}=4(8k+1)(8k+3)u_k/((k+1)(2k+1)),
(2W-256W²)f''+(1-384W)f'-12f=0.
```

Every division above is valid in F_p. GH-108/GH-151 are imported *author-side* mathematical dependencies, not independently reviewed Foundation.

## GH-153 (proved relative to imported identities): nondegenerate stationary point at z=9

Define the orientation-sensitive first-jet observer K(W)=(1-128W)f'(W)-8f(W). Since W'(z)=1/(128z²) and 16m+5=-1 modulo p, substitution gives a **polynomial identity on z≠0**:

```
(1) R_p'(z)=z^{4m} f(W(z)) K(W(z))/(8D²).
```

The Picard–Fuchs equation implies the following additional exact polynomial identity:

```
(2) 2W(1-128W)K' + (1-112W)K - 4(1-160W)f=0.
```

At z=9, W0=1/144, 1-128W0=1/9 and W'(9)=1/10368. The leading coefficient of the differential equation is nonzero. Thus f(W0),f'(W0) cannot both be zero: otherwise the differential equation recursively forces every Taylor coefficient up to degree m<p to be zero, in contradiction with f(0)=h_* !=0. If R_p'(9)=0, (1) implies **exactly one** of:

* f(W0)=0; then K(W0)=f'(W0)/9!=0 and
  **R_p''(9)=9^{4m} f'(W0)^2/(864²D²)!=0.**
* K(W0)=0; then f(W0)!=0, f'(W0)=72f(W0), K'(W0)=-288f(W0) and
  **R_p''(9)=-9^{4m} f(W0)^2/(288D²)!=0.**

Hence for **every p=8m+3>=11**,

```
R_p'(9)=0  ==>  R_p''(9)!=0.
```

This theorem is **conditional on the derivative vanishing**, and does not prove all-prime GH-83. When additionally R_p(9)=0, the reflected polynomial has a root of multiplicity **exactly two**, not three.

## GH-154 (proved): all nonzero critical-root multiplicities; z=5 is the sole possible exceptional point

For finite z!=0, W(z)!=1/128. At z=1, W=0 and f(0)=h_*, K(0)=4h_*, so R_p'(1)!=0. At all other nonzero z the Picard–Fuchs equation has regular leading coefficient 2W(1-128W), hence every zero of f is simple. Also f and K cannot vanish together: at f=0, K=(1-128W)f'!=0.

At any zero of K, f!=0 and equation (2) simplifies to

```
K'(W) = 2(1-160W)f(W)/(W(1-128W)).
```

Therefore every K-zero away from W=1/160 is simple. W=1/160 corresponds to **z=5**. If K(1/160)=0, equation (2) gives K'(1/160)=0; differentiating once gives

```
K''(1/160)=-256000 f(1/160)!=0.
```

The nonzero follows because p>=11, p=3 mod8 and 256000 has only prime factors 2 and 5. Thus **every nonzero root of R_p' is simple except possibly z=5; if K(1/160)=0, z=5 has R_p'-multiplicity exactly two**. At z=0 the original tail definition gives R_p'-multiplicity exactly 2m. This is a conditional classification, not a claim that z=5 attains its exceptional case.

## New p=3347 integer/valuation certificate

Independent construction of the original reflected h_j tail and the Picard–Fuchs coefficients (Python stdlib exact modular arithmetic) yields:

```
p=3347, m=418, D=3073, h_*=3233=-114,
W0=860, f(W0)=783, f'(W0)=2824, K(W0)=0,
R_3347(9)=0, R_3347'(9)=0, R_3347''(9)=2331!=0.
```

Here f(W0)^2=588, and the second derivative agrees with the GH-153 ordinary-branch formula. Consequently the **new exact double-root certificate** is

```
R_3347(z) = 2839 (z-9)^2 + O((z-9)^3) in F_3347[z],
```

where 2839=2331/2 mod3347. The existing R(9)=R'(9)=0 was already known; **R''(9), the order-two bound and the global critical-root classification are this unit's incremental science**.

## Exact executed checks and bounded evidence

Python 3 stdlib directly generates R and its first two formal derivatives, independently regenerates f from the coefficient recurrence, verifies (1) at z=9, checks (2) coefficient-by-coefficient, and matches the nonzero closed R'' formula for all 20 tested primes p=11,19,43,59,67,83,107,131,139,163,179,211,227,251,283,307,331,347,379,3347. All 20 had R'(9)=0 and R''(9)!=0 as **finite observations**, not an all-prime stationary-point proof. A separate exact finite scan found no K(1/160)=0 among 167 primes p=3 mod8, 11<=p<5000; no infinite conclusion follows. Terminal: `PASS_GH153_GH154_REFLECTED_TAIL_CRITICAL_MULTIPLICITIES_EXACT`, exit 0. Full executed script SHA256: `bcf94b527f23cb13c6303368cf0fce3b5c2ef55d341dfe6cd39e771cb357e51c`; executable plus complete log in dated ZIP handoff, not asserted to be a native test.

BRC **COMPOSE_APPLIED**: carrier (p, finite field, selected normalized 2-torsion mark, z, R, formal ordered jets R',R'', f/K branch, operations and provenance). Boolean criticality loses the f-versus-K mechanism, while the root-existence indicator loses double-root multiplicity. This is a precise auxiliary observer result, **not** native X6 spatial transfer. Do not reclassify P000, the ACTIVE worldview, or the frozen science pin.

**Next exact open science:** independently prove the marked ordinary-branch K(1/144)=0 using CM/Jacobi/Gauss or p-adic arithmetic rather than restating GH-83 or GH-151's already-dependent hypergeometric transport; then separately test the source-original GH-3 target. Native D25 H0/B0 divided-power, [X]U mod p², semilinear Frobenius eta, original-class p373, GH-3/GH-83 obligations remain. This GitHub artifact is author-side preservation only: no current native CLAIM/OPEN, Source checkpoint, Result, review, admission, or service identity is claimed. Old session/staging/request/maintenance identities were not modified.
