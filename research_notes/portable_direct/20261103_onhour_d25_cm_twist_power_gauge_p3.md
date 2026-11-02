# D25: exact p-adic arithmetic-power CM twist gauge (new local scientific unit)

2026-11-03. TASK_RESEARCH author-side, conversation chatgpt-research-onhour-enterprise-math-20260923 (not maintenance). Frozen task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Classification: ALGEBRAICALLY PROVED IN DECLARED POWER MODEL / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT.

## The new theorem

Consume the previously established 216/2304 elliptic-curve CM twist from immutable author commit 8ddead488745b4b0d1a73717aed869ac76613d9f. Its twist factor d=3t, t^2=2, u^2=d, and differential relation omega_4=u^(-1)omega_3 are pre-existing. For any prime p>3 with p mod24 in {13,19}, define

    N=(p^2-1)/4, A=u^(p^2-1)=18^N,
    Q=(18^(p-1)-1)/p in Z, epsilon=Legendre(-18,p).

The following **exact p-adic equality** holds in 1+p Z_p:

    A/epsilon = (1+p Q)^((p+1)/4).                          [A]

The right side is the unique p-adic binomial branch congruent to 1 mod p, including when (p+1)/4 is not an ordinary integer. Here epsilon=-1 for p=13 (mod24) and epsilon=+1 for p=19 (mod24).

Consequently, with denominators interpreted as p-adic units,

    A = epsilon * [1 + p Q/4 + p^2 (Q/4 - 3 Q^2/32)] mod p^3,    [B1]
    A^(-1) = epsilon * [1 - p Q/4 + p^2 (-Q/4 + 5 Q^2/32)] mod p^3. [B2]

In particular A differs from the finite-field sign epsilon modulo p^2 by epsilon*p*Q/4. The sign-only arithmetic-power lift is valid mod p^2 if and only if Q=0 mod p. For a valuation-one scalar p*c, insertion of the inverse **power** gauge adds a signed second-digit contribution -epsilon*p^2*c*Q/4 compared with insertion of epsilon alone, conditional on such a transport actually being defined.

## Proof with source and operation kept separate

Since u^4=(3t)^2=18 and 4 divides p^2-1, the identity A=18^N is exact in any containing coefficient extension, hence A is a base-ring scalar. For both target prime classes (2/p)=-1. In F_(p^2) the conjugation t^p=-t implies Norm(3t)=-18; so

    A mod p=(3t)^((p^2-1)/2)=(-18)^((p-1)/2)=epsilon.

The signs follow from quadratic reciprocity, or directly from p mod24. The exact integer identity

    A^4=18^(p^2-1)=(18^(p-1))^(p+1)=(1+pQ)^(p+1)

shows that A/epsilon and the right side of [A] lie in 1+p Z_p and have the same fourth power. The fourth-power map is injective there for p>3; [A] follows.

For [B1], expand the p-adic binomial to order p^2, using (p+1)/4=1/4+p/4 and (1/4)(-3/4)/2=-3/32. Inverting 1+x by 1-x+x^2 gives [B2]. All expressions have proved all-prime scope for the declared residue classes. The mod-p^3 error is exact arithmetic divisibility, not a numerical fit.

## Discriminating exact checks

The independent original-integer Python checker reconstructs A=18^N mod p^3, the Fermat quotient from modular exponentiation mod p^3, Legendre(-18/p), [B1], [B2], and inverse multiplicativity. All 77 eligible primes p<=2000 pass. Sign-only lifting at mod p^2 fails at 75 of the 77 primes. Representative exact outputs:

| p | epsilon | Q mod p | A mod p^2 | A mod p^3 | inverse A mod p^3 |
|---:|---:|---:|---:|---:|---:|
| 13 | -1 | 6 | 64 | 2092 | 272 |
| 19 | 1 | 1 | 96 | 3706 | 5321 |
| 37 | -1 | 0 | 1368 | 17796 | 32855 |
| 373 | -1 | 60 | 133533 | 26568043 | 45918164 |

Thus p=13 refutes the candidate naive congruence A=-1 mod 13^2 (actual 64, not 168); p=19 likewise refutes A=+1 mod 19^2 (actual 96, not 1). The p=37 case has Q=0 mod p and a vanishing first correction, but the next correction still matters modulo p^3. These are counterexamples to **only the declared ordinary-power sign lift**, not to the D25 mother congruence.

## Observer scope and remaining actual target

The distinction is essential: on a ring of characteristic p^2, x -> x^(p^2) is not a ring homomorphism. [A]-[B2] describe an ordinary arithmetic power ratio of the established algebraic gauge, **not** the actual semilinear Frobenius operator of the original H0/B0 class, nor an automatic 216->2304 finite-weighted-sum identity. A genuine Galois automorphism, period normalization, original weight, cutoff and signed eta must be separately specified. BRC usage is the exact scalar descent for this one declared operator, retaining ring/precision, p-adic valuation, sign, source and permitted future operations.

The mother objective Delta_p-R_p=0 mod p for p=13,19 mod24, equivalently original W_216(p-1)=p mod p^3 by the established source bridge, remains OPEN. Next science: build a source-backed CM/WZ map for the **fixed original** 216/2304 coefficient-accumulator observers, typed as true semilinear Frobenius versus ordinary-power operator; test on 13,19,373 with exact signed cutoff and the new correction. Avoid re-proving accepted D24 and completed Gauss/Clausen/holonomic units. The native original-class p=373 H0/B0 divided-power [X]U mod139129, rank, semilinear Frobenius eta, odd Green/Hesse signs and independent replay are still NOT_EXECUTED / PENDING_OWNER in Enterprise Math #1559; no surrogate is presented here.

Control provenance: verified global canonical read main@e693993599de367f0f27c3da8821e8838eadc848; Enterprise main at start f58994bdfc7df5e7a562b0c2ff8f7732395bcd01; original separate prior author frontier caacb89727744b6df7a17e1abe278910f8783344. Other research lane's latest H5/H6 was read but not copied. Sites gateway v0.6.11 reported research_authority_granted=false, write_relay_enabled=false, backend_connected=false; exact continuation attempt returned CONTROL_QUOTA, not NO_DISPATCH. Historical recovery bridge awdawmip/kimi-query-bridge#6632 has no own claim/run; original dispatch request research-onhour-20261031-0205-dispatch-r15 at #6633 was FAILED UPSTREAM_CODE_REVIEW_REQUIRED. No request replay, no session/claim/run/native Source checkpoint/Result/admission and no maintenance-lane identity. Historical neutral staging remains segregated. No scheduler mutation.
