# D25: exact Frobenius-carry root multiplicity and second-jet witness (2026-11-07)

**Status:** AUTHOR-SIDE ALGEBRA PROVED; finite exact checks 815/815; UNREVIEWED / NOT_ADMITTED. No native Researcher CLAIM, execution, result or project admission is asserted.

**Scope and provenance.** Research lane `chatgpt-research-hourly-enterprise-math-20260923`, not the separate maintenance lane. Parent `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Continuation from `20261107_hourly20_d25_frobenius_carry_factorization.md` at `dd3af761bcce0a6dd420b7e3fdde7a982fe547b1`. The distinct on-hour D25 Gauss-monodromy/quadratic-*p-adic* jet note (commit `d115e8c962930b2726c0f5463565dee08109ebac`) addresses a different operator and is not counted as our result.

## Theorem 1: compressed binomial expression for the exact mod-p carrier

Let `p=8k+5` be prime (`k>=0`), and work **only over** `F_p`. Set

```
r=5k+3, s=7k+4, t=4k+3=(p+1)/2,
G(z)=sum_{i=0}^r binom(r,i)binom(s,i)z^i,
H(z)=sum_{j=0}^k binom(3k+1,j)binom(k,j)z^j.
```

Then the exact polynomial identity in `F_p[z]` is

[
G(z)=(1-z)^t H(z).
]

**Proof.** The terminating Gauss polynomial is ({}_2F_1(-r,-s;1;z)). Euler's transformation of its formal power series gives ((1-z)^{1+r+s}{}_2F_1(1+r,1+s;1;z)). In characteristic p, for coefficients of degrees (<p), (1+requiv-(3k+1)) and (1+sequiv-k), so the transformed series truncates to the displayed (H). Also (1+r+s=p+t), and ((1-z)^p=1-z^pequiv1mod z^p). Both sides of the claimed identity have degree (r=5k+3<p), hence equality through degree (p-1) is an exact polynomial identity. This is a more compact reconstruction of the preceding Frobenius-carry factorization, **not** a new p-adic lifting theorem.

## Theorem 2: all roots of H are simple

[
H(0)=1,qquad H(1)=inom{4k+1}{k}
e0pmod p.
]

The second identity is Vandermonde; `4k+1<p` ensures nonzero. As a hypergeometric polynomial, (H) satisfies

[
z(1-z)H''+[1+4kz]H'-k(3k+1)H=0
quad	ext{in }mathbb F_p[z].
]

If (alpha) in an algebraic closure of (mathbb F_p) were a multiple root, then (alpha
e0,1) and (H(alpha)=H'(alpha)=0). Differentiating the equation successively at (alpha), with leading coefficient (alpha(1-alpha)
e0), implies (H^{(j)}(alpha)=0) for all (jle k). Since (deg H=k<p), all factorials (j!) are invertible, contradicting (H(0)=1). Thus (gcd(H,H')=1) for **every** prime `p=8k+5` (the `k=0` case is immediate).

## Theorem 3: complete multiplicity classification of aggregate Frobenius carry

Define (Q(z)=(1-z)H(z)^2). By Theorem 1 and (2t=p+1),

[
G(z)^2=(1-z^p)Q(z).
]

Since (deg Q=2k+1<p), the exact degree-(ge p) part of (G^2) is

[
C(z)=-z^p Q(z)=-z^p(1-z)H(z)^2
quad	ext{in }mathbb F_p[z].
]

Consequently, over an algebraic closure, the complete root multiset of (C) is: `z=0` with multiplicity `p`; `z=1` with multiplicity one; and each of the `k` distinct roots of (H) with multiplicity **exactly two**. This exhausts (deg C=p+2k+1).

At any root (alpha) of (H), (alpha
e0,1), and
[
C(alpha)=C'(alpha)=0,qquad
C''(alpha)=-2alpha(1-alpha)H'(alpha)^2
e0.
]
For the logarithmic derivative (	heta=z,d/dz) and the 2304 weighted polynomial observer (mathcal W=1+8	heta), one has
[
mathcal W C(alpha)=0,quad
	hetamathcal W C(alpha)
=-16alpha^3(1-alpha)H'(alpha)^2
e0.
]
In particular, **if** (H(1/9)=0), then
[
C''(1/9)=-rac{16}{81}H'(1/9)^2
e0,qquad
	hetamathcal W C(1/9)=-rac{128}{6561}H'(1/9)^2
e0
quad (mod p).
]

This is a complete second-jet distinguishability certificate for the **aggregate Gauss–Clausen mod-p carry**. It does **not** identify that aggregate with the original term-labelled 2304 `p^2` tail or a native `p^3` experiment.

## Exact computations and open boundary

The adjacent standard-library script evaluates (H,H',H''), its ODE and three carry jets with integers modulo each prime, independently of the polynomial-factor expansion. Every prime `p<30000, p%8==5` was checked (815/815). Among these, all 407 primes `p%24==13` yielded `H(1/9)=0` with a nonzero (C''(1/9)); the 408 primes `p%24==5` yielded nonzero (H(1/9)). This is **finite evidence**, not a proof of the residue-class-zero conjecture.

| p | H(1/9) | H'(1/9) | C''(1/9) | theta(1+8theta)C(1/9) |
|---:|---:|---:|---:|---:|
| 13 | 0 | 4 | 10 | 5 |
| 29 | 7 | 0 | 18 | not a root |
| 37 | 0 | 11 | 30 | 29 |
| 61 | 0 | 27 | 39 | 40 |
| 109 | 0 | 14 | 3 | 77 |
| 181 | 0 | 124 | 42 | 98 |
| 373 | 0 | 369 | 333 | 323 |

The exact unresolved assertion remains (H_p(1/9)=0) for all `p%24==13` (or the first counterexample). A compact binomial/evaluation form now available for any prime `p=8k+5` is
[
H_p(1/9)=sum_{j=0}^{k}inom{3k+1}{j}inom{k}{j}9^{-j}pmod p.
]
This takes `O(k)` modular updates, instead of constructing the `O(p)`-degree polynomial and dividing it or doing quadratic convolution. It is the next input for a finite-field character-sum/CM or creative-telescoping proof search.

**BRC semantics.** Carriers are the indexed coefficient/valuation/source sets prior to aggregation, (G^2) and its truncation carrier (C) afterward. Observers are evaluation, first weighted (mathcal W), and further (	hetamathcal W); the allowed future operation is differentiation. At a root, the first two scalar readouts erase a nonzero second jet; the last readout retains a certificate. No per-port equivalence or lossless inverse is implied by the aggregate identity.

**Mother objective remains OPEN:** (Delta_p-R_pequiv0pmod p) for (pequiv13,19pmod{24}), via the frozen (W_pequiv ppmod{p^3}) bridge. No role-bound checkpoint/Result/admission occurred. Native Site currently reports `BACKEND_IDENTITY_OR_VERSION_MISMATCH`, `operation_sent=false`; old session/claim/staging status is UNKNOWN_PRESERVE; support issue `#1558` remains the recovery path. Next math action: derive a rigorous character-sum or modular/CM evaluation of (H_p(1/9)), then use the nonvanishing second jet to constrain any two-legged 216/2304 weighted transfer. 
