# D25/LIFT — full p-adic-depth semilinear square-orbit lifting by odd-order square roots

2026-10-25 | TASK_RESEARCH portable author derivation | **AUTHOR-DERIVED / AUTHOR-CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CM / NO_NEW_NATIVE_CHECKPOINT**

## Exact predecessor and authority

Parent D25/LIFT/JT2 **OPEN**, Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` is unchanged. Native canonical predecessor checkpoint `220ee1ba360f21152912d0b4c1abdf867a1e4496` is historical; this note is not a native checkpoint.

This work **consumes, rather than duplicates**, the diagonal-base and arbitrary-base *top-digit* results, particularly `research_notes/portable_direct/20261025_hourly_d25_general_semilinear_square_orbit_lift.md` first published on 2026-10-25. The new unit removes the top-digit/square-zero restriction and proves a global finite-precision lifting theorem at **all** digits, using an explicit odd-order correction.

## Theorem — full congruence-kernel faithfulness of the square

Let `p` be any odd prime, `r>=2`, and let `R=(Z/p^r Z)[t]/(t^2-2)`, with the involutive ring automorphism `sigma(t)=-t`. (In the intended D25 primes `p=13,19 mod 24`, this is the quadratic unramified coefficient ring.) Let `C,C' in GL_n(R)` be **any** invertible matrices satisfying `C'=C mod p`. Write
```
F_C(v)=C sigma(v),       S=C sigma(C),
F_C'(v)=C' sigma(v),     S'=C' sigma(C').
```

The following are exactly equivalent:

1. There exists a `P in I+p M_n(R)` such that `C'=P^(-1) C sigma(P)`.
2. There exists a `P in I+p M_n(R)` such that `S'=P^(-1) S P`.

No diagonalizability, semisimplicity, restriction to `p^(r-1)`, or bound on `n` is required. The theorem treats the entire congruence kernel simultaneously, rather than inductively asserting an unverified Hensel step. The operator `sigma`, the modulus, and the congruence class of `C` remain fixed.

**Caution:** `S` modulo arbitrary `GL_n(R)` similarity, trace, determinant, characteristic polynomial, or just `S mod p` is *not* claimed to be sufficient. Both (1) and (2) use the **same near-identity group** `I+p M_n(R)`.

## Constructive proof

(1) immediately implies (2). For (2) implies (1), choose a certified square conjugator `P=I+pX` such that `S'=P^(-1) S P`. Transport the second semilinear matrix to the same square:
```
C_hat = P C' sigma(P)^(-1).
```
Then `C_hat sigma(C_hat)=P S' P^(-1)=S`, and `C_hat=C mod p`.

Put `W=C_hat C^(-1)`. Thus `W in I+pM_n(R)`. Define the multiplicative ring-automorphism on the matrix group
```
T(U)=C sigma(U) C^(-1).
```
Since `C_hat=W C`, equality of squares gives
```
W T(W)=I,       hence T(W)=W^(-1).
```

**Odd-order lemma.** For any `W=I+pV`, the exact integer power
```
W^m=I,     m=p^(r-1)   (odd).
```
To prove this, observe by the integer binomial theorem that for `k>=1`,
`(I+p^k V)^p=I mod p^(k+1)` for odd `p`; the matrices `I` and `V` commute in this expansion. Iterate `r-1` times, starting at `k=1`.

Let `h=(m-1)/2` and choose **explicitly**
```
Q=W^h.
```
Then `Q in I+pM_n(R)`, `Q^2=W^(m-1)=W^(-1)`, and by multiplicativity `T(Q)=T(W)^h=W^(-h)=Q^(-1)`. Consequently,
```
Q^(-1) T(Q)=Q^(-2)=W.
```
Thus
```
C_hat = W C = Q^(-1) C sigma(Q).
```
Undo the transport:
```
C' = P^(-1) C_hat sigma(P)
   = (Q P)^(-1) C sigma(Q P).
```
The **actual lifted semilinear gauge** is `H=Q P in I+p M_n(R)`. This is constructive, uses only integer powers of a genuine unit, and introduces no square-root choice or extension ring. QED.

This proof also shows a more general interface: if a finite ring has a stable nilpotent congruence kernel of **odd order** and the coefficient automorphism is involutive, the same cocycle/odd-root argument works inside that kernel. The present verified theorem is only claimed for the explicit `R` and `p,r` above.

## Exact finite-ring certificates

Use `(a,b)` for `a+bt` modulo `M=p^r`, with `t^2=2`, and the exact multiplication
```
(a,b)(c,d)=(ac+2bd,ad+bc) mod M.
```
A nontrivial norm-one scalar unit at every precision `r>=2` is
```
W = (1+p t) / (1-p t).
```
The denominator is invertible, with inverse `sum_(j=0)^(r-1) (p t)^j`. Thus `sigma(W)=W^(-1)` exactly and `W=1 mod p`. Set `m=p^(r-1)`, `Q=W^((m-1)/2)`. Then the **explicit certificate equation**
```
Q^(-1) sigma(Q) = W
```
holds modulo `p^r`, not just in the top digit.

The following author-executed exact integer-pair checks used both `r=2` and `r=3` for all three primes; selected `r=3` witnesses are:

| p | M=p^3 | W as (a,b) | Q as (a,b) | checks |
|---:|---:|---|---|---|
| 13 | 2197 | (677,26) | (170,2184) | `W sigma(W)=1`, `Q^(-1)sigma(Q)=W` |
| 19 | 6859 | (1445,38) | (362,6840) | same |
| 373 | 51895117 | (556517,746) | (139130,51894744) | same |

For an actual **nondiagonal** matrix instance, take
```
C=[[1,-1-t],[0,2+t]],       P=I+p E12,
C'=P^(-1) (W C) sigma(P).
```
Here `W` acts as the scalar matrix `W I`. The author evaluated these exact `2x2` ring products independently with `H=Q P` and verified
```
C'=H^(-1) C sigma(H),
S'=P^(-1) (C sigma(C)) P
```
for each `p=13,19,373` and each `r=2,3` (six finite cases). For `r=3`, `S'_12` is respectively `2183`, `6839`, and `51894743` modulo the tabulated `M`. These computations are author consistency checks; the argument above supplies the proof for all specified `n,p,r`.

## Boundary and information consequence

The prime-two hypothesis is **structural**: the congruence-kernel order would not be odd, and the half-exponent proof would fail. In the simpler subcase `R=Z/4Z`, `sigma=id`, rank one, `C=1` and `C'=3` have equal squares and equal reductions modulo 2 but cannot be conjugate by any scalar gauge. No p=2 extension is claimed.

This theorem gives a lossless BRC-style **full square-orbit observer** only for a fixed coefficient ring, fixed involution, fixed residual class and the declared near-identity gauge group. It is a `COMPOSE_APPLIED` extension of the preceding full-square top-digit interface; no signed/odd port, native 6D provenance or actual original CM source is discarded by assertion. Whether the target scalar `kappa`, `omega+6 nabla_lambda omega` or `Delta_p-R_p` factors through this quotient is **unproved** and must be tested against a real same-class source representative.

**Immediate benefit to the D25 program:** once an actual invertible source-authenticated Frobenius coefficient matrix is obtained, a verified near-identity square comparison at the *full* finite precision would be sufficient to reconstruct a compatible semilinear change of basis explicitly. No diagonalization is required. This does not, by itself, produce the original CM/divided-power operator or verify the LIFT target.

## Status and next parent unit

Status: **portable mathematical author proof + six exact finite checks; UNREVIEWED / NOT_ADMITTED / NO_NEW_NATIVE_CHECKPOINT**. The current native CM experiment remains `NOT_RUN`. The frozen Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` and already authenticated checkpoint are unchanged.

Control tool `em_status` was read (v0.6.11). This host did not expose the task-bound typed `recovery_status` action; no fresh own CLAIM/open/run authority has been authenticated. Prior `CONTROL_QUOTA` for exact task control is not `NO_DISPATCH`; no privilege-bound write was attempted on stale authority. GitHub authorship of this portable artifact does not create Source publication or research admission. The existing control support path is Enterprise Math Issue #1558.

**Next precise scientific action:** obtain original-class and same-prime `H0/B0`, `[X]U mod p^2`, actual Frobenius `C` with verified semilinear direction and normalization. Compare its **full square** under an explicitly justified near-identity basis equivalence; invoke this lifting theorem only after all ring, invertibility and mod-p congruence hypotheses are established. Then check whether the original target observers factor through the resulting source map. Native CM experiment and D25/LIFT/JT2 **OPEN**.

**Next precise control action:** first use this lane's actual `recovery_status` when available, reconcile original pending requests, consume current canonical continuation/frontier and any winning claim; publish only through a newly authenticated Research owner run and read back Source checkpoint. Do not recycle a maintenance conversation, claim ownership from GitHub storage, or repeat the already completed top-digit proof.
