# D25 portable research: p=811 Hensel obstruction and renormalized four-wall second digit

Status: AUTHOR_PORTABLE_PROOF / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT

This unit continues the portable upper-B-chart lane only. It does not claim a native session, CLAIM, run, Result, review, or theorem admission.

## Source boundary

- GLOBAL_KNOWLEDGE_V1 canonical main for this execution phase: 8c863c7ec308cfc74dc325af21e41da24d0f10a7.
- Enterprise Math canonical main for this execution phase: ff1e5a5862eba2eb7cd0c6d9159a7191aa2f8fec.
- P000 remains ACTIVE_LOCKED.
- Canonical D25 local-progress blob remains 51dd15a8142f3dda0506a306f9c0693a036f5891.
- Portable predecessor head before this unit: acd2b86f0cafeaa289ea3df2d8553937a87934f4.
- A fresh recovery_status transport was attempted for stable conversation_id EM-DIRECT-C4D02C and was blocked by the host before Issue creation. The last independently read successful recovery remains Issue #2578: session_state=ABSENT, no pending/run/claim/upload/staging, execution_authorized=false.

## 1. Setup and exact cyclic identity

Let

q(x)=4 (x+1/3)(x+5/6)/((x+1/4)(x+3/4)),

L(F)(x)=q(x)F(x+1)-F(x),

Q_0(x)=1,
Q_j(x)=prod_{i=0}^{j-1}q(x+i),

and for the Omega/tau cocycle let

S_p(x)=sum_{j=0}^{p-1} K(x+j)Q_j(x).

The durable mod-p cyclic gauge is R_0=S_p/3. For p=811, m=(p-1)/6=135, the preceding checkpoint proves R_0 is regular at x=m.

The characteristic-zero p-step transport is

Q_p(x)R(x+p)-R(x)=S_p(x).

At x=m+eps write, modulo p^2 in the punctured p-adic Laurent sense,

Q_p = 4 + p A,
S_p = 3 r + p B,

where r is the regular mod-p gauge.

A p^2 lift R=r+pT must satisfy

3T = B - 4 r' - A r  (mod p).

Hence

PP(T)= (1/3) PP(B-Ar).

## 2. Exact p=811 Laurent certificate

A direct coefficientwise computation in (Z/p^2 Z)((eps)), retaining the true p-adic carries of every rational coefficient, gives

PP(A)=271 eps^(-1),

PP(B)=134 eps^(-2)+697 eps^(-1),

r(0)=479

mod 811.

Therefore

A_{-1} r(0)=271*479=49 (mod 811),

and

PP(T)
= (1/3)[134 eps^(-2)+(697-49)eps^(-1)]
=315 eps^(-2)+216 eps^(-1)
(mod 811).

In particular

315 != 0 mod 811.

Thus p=811 has an observer-regular cyclic split modulo p, but no observer-regular cyclic split modulo p^2.

This obstruction is independent of the chosen regular coefficient lift: replacing the lift by rtilde+pH with H regular changes T by -H and cannot change its principal part.

## 3. Four-wall residue and the second-digit highest pole

For target primes p == 13 or 19 (mod 24), the mod-p observer singular schedule has four walls, centered at

p/4, p/2, 3p/4, p.

Let their aggregated mod-p residues in S_p be

W_(1/4), W_(1/2), W_(3/4), W_1.

The first observer obstruction is

H_p := W_(1/4)+W_(1/2)+W_(3/4)+W_1.

Observer regularity modulo p is equivalent to H_p=0.

At the next divided digit, prior pole-zero cancellations leave transport memory. The two q pole/zero pairs are

(p/4 -> p/3),    (3p/4 -> 5p/6).

Consequently the effective second-digit wall centers are

1/4, 5/12, 2/3, 5/6.

The eps^(-2) coefficient of B is therefore

B_{-2}
= -[
  (1/4)W_(1/4)
 +(5/12)W_(1/2)
 +(2/3)W_(3/4)
 +(5/6)W_1
].

If H_p=0, eliminate W_1 to obtain

B_{-2}
= [7 W_(1/4)+5 W_(1/2)+2 W_(3/4)]/12.

Define the renormalized first wall moment

J_p := 7 W_(1/4)+5 W_(1/2)+2 W_(3/4).

Since A r has at most a simple pole when r is observer-regular,

T_{-2}=B_{-2}/3=J_p/36.

Therefore an observer-regular p^2 split must satisfy the two necessary conditions

H_p=0,
J_p=0.

## 4. p=811 wall evaluation

For p=811 the durable four wall residues are

W_(1/4)=268,
W_(1/2)=543,
W_(3/4)=536,
W_1=275.

They satisfy

268+543+536+275 = 1622 = 2*811,

so H_811=0, as required by the known mod-p cancellation.

But

J_811
=7*268+5*543+2*536
=5663
=797 (mod 811),

hence

B_{-2}=797/12=134 (mod 811),

T_{-2}=797/36=315 (mod 811),

exactly matching the independent p^2 Laurent certificate above.

Thus the exceptional p=811 cancellation dies at the next p-adic digit already in the highest pole.

## 5. BRC consequence

Safe quotienting is precision-typed.

- H_p != 0: the mod-p cyclic gauge is observer-singular.
- H_p = 0: the mod-p pole cancels, but Omega may not be deleted beyond that precision.
- At the next digit the retained residual is J_p; J_p != 0 forces a double pole in the unique Hensel correction.

A cancelled wall still carries transport memory into later precision. Current invisibility is not future irrelevance.

Reuse disposition: COMPOSE_APPLIED using the durable p=811 cancellation checkpoint, the durable Hensel criterion, the Omega/tau transport, and BRC valuation retention.

## 6. Verification

For p=811, the exact Z/p^2Z Laurent recurrence was rerun with truncation windows 10, 12, 16, 20, 24 and 30; all runs gave the same decisive coefficients

A_{-1}=271,
B_{-2}=134,
B_{-1}=697,
r(0)=479,
T_{-2}=315,
T_{-1}=216.

The wall formula independently reproduces B_{-2}=134 and T_{-2}=315.

## 7. Next exact unit

Do not rebuild the full cyclic gauge.

Assume H_p=J_p=0 and derive the remaining simple-pole coefficient

K_p := 3 T_{-1}
     = B_{-1} - A_{-1} r(0),

with A_{-1}=2/3.

The next task is to express K_p as a faithful wall-jet / transport-holonomy invariant. This requires first p-adic wall jets and regular-memory transport; it cannot be inferred from the four mod-p residues alone.
