# D25/SECOND-DIGIT-LIFT — exact quadratic-cutoff Frobenius carry and its conditional elimination

2026-11-01 Asia/Hong_Kong. **AUTHOR-SIDE EXACT ALGEBRAIC PROOF / CONDITIONAL CM INPUT / EXECUTED FINITE CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE_NOT_RUN**.

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Logical Research conversation `chatgpt-research-onhour-enterprise-math-20260923`. Consumes the exact polynomial p² reflection and signed quadratic cutoff from predecessor project commit `b3c681ad9428613ef1e9e63b3451fde8a6903ff2`, not a new proof/credit for that earlier result.

## Original coefficient sources and exact Frobenius-carry identity

For any prime p≡5(mod8), p>=13, retain the original finite 1/8–3/8 Gauss polynomial `F_p(z)` and the 1/4–3/4 period `U_p(t)` of the earlier note. Its **exact original finite quadratic pullback difference** is

```
R_p(t) = F_p(4t(1−t))−U_p(t)
       = sum_{j=p}^{2p−2} r_(p,j)t^j = t^p H_p(t),
H_p(t) = sum_{r=0}^{p−2} r_(p,p+r) t^r.
```

All coefficients `r_(p,j)` are the explicit signed, source-labeled finite sum in the predecessor theorem and are p-local. Work in `R₂=(Z/p²)[s]/(s²−2)` at the two original conjugate arguments `t=t_-=1/2−s/3`, `bar(t)=t_+=1/2+s/3`. The earlier proven reflection states `U_p(t)+U_p(bar(t))=0 (mod p²)`. Since (2/p)=−1, the residue Frobenius sends `t^p≡bar(t) (mod p)`. Define the **integral first Frobenius carry**

```
D_p(t) = (t^p−bar(t))/p    in R₂ modulo p,
```

where division is componentwise in the p-local quadratic ring **before reduction**. Let `Tr(x)=x+bar(x)`. Taking the unchanged original even trace yields the new exact two-source formula

```
F_p(1/9)
 = (1/2) Tr(bar(t) H_p(t))
 + (p/2) Tr(D_p(t) H_p(t))          (mod p²).                  (FC)
```

The second term is a **real p-adic carry port**, not a removable decoration. Formula (FC) is an unconditional arithmetic theorem for all such p, with no CM assumptions.

## p13 conditional simplification: proof that the carry is killed by order

For a prime p≡13(mod24), suppose both mod-p CM selectors hold *for the original operators*:

```
F_p(1/9)≡0 (mod p),    U_p(t_-)≡0 (mod p) in F_(p²).          (S)
```

The first is the earlier p13 beta CM selector. The second, a separate 1/4–3/4 Legendre period selector, has **finite supporting evidence given below**; this note does not claim that selector is independently proved for every p. From the exact `F_p(1/9)=U_p(t)+t^p H_p(t)`, the two selectors (S) imply `t^p H_p(t)=0 (mod p)`. Since t is a unit in R₂, `H_p(t)=0 (mod p)`.

Hence the **first Frobenius carry vanishes identically modulo p²**, yielding

```
(p/2)Tr(D_p(t)H_p(t))=0 (mod p²).
```

Define `K_p(t)=H_p(t)/p` by dividing both original quadratic coordinates (well-defined under (S)). The unresolved original beta second digit is then given by a single finite-field trace:

```
boxed:
F_p(1/9)/p = (1/2) Tr(bar(t) K_p(t))         (mod p).         (T)
```

This **removes a whole Frobenius carry source under explicit p13 CM hypotheses**, rather than merely renaming the original target. The still-open universal p13 goal is `Tr(bar(t)K_p(t))=0 (mod p)`. This is a smaller finite-field signed high-degree cutoff problem involving the previously retained coefficients; (T) does not establish its vanishing, nor the mother weighted216 LIFT.

In coordinates `K_p(t)=u_p+v_p s` (mod p), `bar(t)=1/2+s/3`, the requested scalar becomes `u_p/2+2v_p/3` (mod p). Here u_p,v_p are the **original cutoff's high-degree first digits**, not any native H0/B0 module coordinates. BRC COMPOSE_APPLIED preserves the two conjugate source branches, signed original cutoff, valuation and Frobenius carry; eliminating the carry is justified only for this observer after (S).

## Actual arithmetic certificates; precise distinction between proof and finite CM evidence

Executable exact Python source: `research_notes/portable_direct/d25_quadratic_frobenius_tail_carry_20261101.py`, Git blob `fab7049cbace32d76b722da70de0a0009306e898`. It reuses the previously checked original quadratic cutoff routine instead of reproducing another high-degree coefficient implementation. The program uses independent modular Legendre recurrence, p-local two-coordinate arithmetic and original beta recurrence, not floating point.

- All **157 primes** p<=10000 with p≡13(mod24) passed the mod-p Legendre selector `P_((p−1)/4)(2sqrt(2)/3)=0` by independent finite-field recurrence. **This is finite evidence for the second assumption in (S), not its all-prime proof.** The original beta selector has its earlier separate source.
- At p=13,37,61,109,157,181,229,373, independently reconstructed both mod-p CM selectors (S), checked each coordinate of H divisible by p, confirmed the Frobenius carry vanished modulo p², and checked (FC) and the normalized quotient (T) against the original beta Gauss polynomial.
- Non-target controls p=29,53 checked the full formula (FC) with **nonzero carry**: for p29 the main port is 26 and the carry is 261 (mod841), summing to `F_29(1/9)=287`. At p53 the corresponding ports are 1301 and 2226 (mod2809), summing to 718. Deleting the Frobenius carry without the selectors (S) changes the answer.

| p | H_p(t_-) (1,s) mod p² | D_p(t_-) (1,s) mod p | first-digit Gauss F/p | carry |
|---:|---:|---:|---:|---:|
| 13 | (91,143) | (1,5) | 0 | 0 |
| 29 | (580,445) | (1,28) | not p-integral | 261 |
| 373 | (55577,62664) | (0,192) | 0 | 0 |

For example, at p373 one has `K=(149,168)` in `F_373[s]`; the distinguished signed even observer gives `149/2+2·168/3=149/2+112=0 (mod373)`. This is a fixed-prime exact check of (T), not a full-prime cancellation theorem.

## Recovery and distinct native debt

**Immediate mathematical next step:** establish (S)'s Legendre CM selector at all p≡13(mod24) from its exact source or prove it independently without new axiom; then find a signed coefficient involution on the original quadratic cutoff `K_p(t)` that kills `Tr(bar(t)K_p(t))` for the entire target class. Compose with the already sourced 2304 signed beta/CM moment and frozen original216 `Delta_p−R_p`, never replacing the original task with this equivalent target.

The distinct original-class **native p=373 H0/B0 divided-power [X]U mod139129, module rank, semilinear Frobenius direction and eta, signed odd Green/Hesse, kappa and independently replicated experiment** remains issue #1559: NOT_RUN/PENDING_OWNER as checked this run, expected executor canonical Source native owner/maintainer. This polynomial ring calculation does not satisfy native benchmark acceptance.

The Source gateway 0.6.11 in this run returned `research_authority_granted=false` and `executor_binding_configured=false`; own checkpoint list `ACCESS_DENIED`; original request `research-onhour-20261031-0205-dispatch-r15` returned current-client `CONTROL_REQUEST_NOT_FOUND`. No session, claim, run, canonical checkpoint, formal Result or review is asserted. Earlier staging independent; research lane separate from maintenance. Preserve frozen scientific pin, P000, ACTIVE worldview and scheduled settings.
