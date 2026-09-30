# D25 portable research: leading p^3 quadratic wall moment

Status: AUTHOR_PORTABLE_PROOF / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT

This checkpoint preserves the already-derived staged unit from the same logical conversation after the complete p^2 observer criterion. It does not claim a native session, CLAIM, run, Result, review, or theorem admission.

## Source boundary

- GLOBAL_KNOWLEDGE_V1 canonical main for this execution phase: 8c863c7ec308cfc74dc325af21e41da24d0f10a7.
- Enterprise Math canonical main for this execution phase: ff1e5a5862eba2eb7cd0c6d9159a7191aa2f8fec.
- P000 remains ACTIVE_LOCKED.
- Canonical D25 local-progress blob remains 51dd15a8142f3dda0506a306f9c0693a036f5891.
- Portable predecessor head before this checkpoint: 9e046e26bf0c6d7814faf5629df26d0e7fd5236a.
- A fresh recovery_status transport for stable conversation_id EM-DIRECT-C4D02C was attempted in this run and was blocked by the host before Issue creation. The last independently read successful recovery remains Issue #2578: session_state=ABSENT, no pending/run/claim/upload/staging, execution_authorized=false.

## 1. Precision-p^3 setup

Let

Q_p = 4 + p A + p^2 C  (mod p^3),

S_p = 3 r + p B + p^2 D  (mod p^3),

and let a putative observer-regular cyclic splitting be lifted as

R = r + p T + p^2 U.

Expanding the exact p-step transport

Q_p(x) R(x+p) - R(x) = S_p(x)

through p^3 gives

3U = D - 4T' - 2r'' - A(T+r') - C r    (mod p).      (1)

Assume the complete p^2 observer criterion already holds,

H_p = J_p = K_p = 0,

so r and T are observer-regular.

Then the terms 4T', 2r'', A(T+r'), and Cr have pole order at most two at the arithmetic observer. Hence the highest possible pole of U is the eps^(-3) term inherited from D:

U_{-3} = D_{-3}/3.                                  (2)

## 2. Four-wall quadratic skeleton

Retain the same four wall groups and provenance as in the p^2 analysis. Their mod-p simple-pole residues are

W_(1/4), W_(1/2), W_(3/4), W_1.

Tracking the second divided digit of the exact wall blocks, including the pole-zero transport memory already responsible for the effective p^2 wall centers, gives the cubic-principal coefficient

D_{-3}
 =
 (1/16) W_(1/4)
 +(3/16) W_(1/2)
 +(23/48) W_(3/4)
 +(109/144) W_1.                                  (3)

When the first two wall conditions hold,

H_p = W_(1/4)+W_(1/2)+W_(3/4)+W_1 = 0,

J_p = 7W_(1/4)+5W_(1/2)+2W_(3/4) = 0,

eliminating W_1 and W_(3/4) reduces (3) to

D_{-3}
 = (20W_(1/4)+9W_(1/2))/72.                       (4)

Define the quadratic wall moment

L_p := 20W_(1/4)+9W_(1/2).                        (5)

Combining (2) and (4),

U_{-3} = L_p/216.                                  (6)

Therefore an observer-regular splitting modulo p^3 must satisfy, in addition to the complete p^2 conditions,

L_p = 0.                                           (7)

This is a necessary leading-pole condition at precision p^3. No sufficiency claim is made yet because the eps^(-2) and eps^(-1) coefficients of U remain to be classified.

## 3. Verification retained from the staged unit

An independent coefficientwise computation in (Z/p^3 Z)((eps)) checked equation (3) for the target primes

13, 19, 37, 43, 61, 67, 109, 139, 157, 163,

with 10/10 agreement.

For p=811 the same direct recurrence gave

D_{-3}=133 (mod 811),

again agreeing with the four-wall expression (3).

These checks are regression/certification only; the structural claim is the exact wall-expansion argument above.

## 4. BRC consequence

The precision-typed observer residual ladder now begins

H_p -> J_p -> K_p -> L_p.

H_p is the visible mod-p four-wall residue.
J_p is the renormalized first wall moment.
K_p is the complete remaining p^2 wall-jet/transport residual.
L_p is the leading quadratic wall moment exposed one digit later.

Even after H_p=J_p=K_p=0, the wall provenance cannot be deleted: the same wall residues can re-enter through the quadratic combination L_p at precision p^3.

Reuse disposition: COMPOSE_APPLIED using the durable complete p^2 criterion and the same four-wall valuation/provenance carrier.

## 5. Next exact unit

Assume

H_p=J_p=K_p=L_p=0.

Do not rebuild the full cyclic gauge. Derive the eps^(-2) coefficient of U directly from:
- the second lifted wall jet in D,
- the p^2 prefix correction C,
- the regular p^2 gauge T and its derivative,
- the already retained wall provenance and transport memory.

The target is the next observer residual that kills U_{-2}; only after that should the eps^(-1) coefficient be attacked.
