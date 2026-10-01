# D25 portable research: canonical p^3 cyclic-defect certificate

Status: AUTHOR_PORTABLE_PROOF / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT

This checkpoint preserves the already-derived canonical defect formulation on the same portable upper-B-chart lane. It does not claim a native session, CLAIM, run, Result, review, or theorem admission.

## Source boundary

- GLOBAL_KNOWLEDGE_V1 canonical main observed for this execution phase: 8c863c7ec308cfc74dc325af21e41da24d0f10a7.
- Enterprise Math canonical main observed for this execution phase: ef041d4ebc3743d8e569f30b8eb6188e58d218e0.
- P000 remains ACTIVE_LOCKED; its blob remains 7334734bd1cff6d60bd6b73cd0c588fe01c88714.
- Canonical D25 local-progress blob remains 51dd15a8142f3dda0506a306f9c0693a036f5891.
- Portable predecessor head before this checkpoint: cfa09fb653ad45c5dc9464d5321fb7ae8743fae7.
- A fresh recovery_status request for stable conversation_id EM-DIRECT-C4D02C was attempted in this run but blocked by the host before Issue creation. The last independently verified successful recovery remains Issue #2578: session_state=ABSENT, no pending/run/claim/upload/staging, execution_authorized=false.

## 1. One-step divided defect

Let

L(F)(x) := q(x)F(x+1)-F(x),

and let R^(2) be any observer-regular one-step splitting modulo p^2,

L(R^(2)) = K  (mod p^2).

Define the second divided one-step defect

e_p(x)
:=
[K(x)-q(x)R^(2)(x+1)+R^(2)(x)]/p^2
mod p.                                                     (1)

Thus a correction U produces an observer-regular splitting modulo p^3 precisely when

L(U)=e_p.                                                   (2)

## 2. Cyclic defect and exact inversion

For

Q_0(x)=1,
Q_j(x)=prod_{i=0}^{j-1} q(x+i),

define the cyclic defect

E_p(x)
:=
sum_{j=0}^{p-1} e_p(x+j)Q_j(x).                           (3)

In F_p(x),

Q_p(x)=4,

and x+p=x. Therefore

q(x)E_p(x+1)-E_p(x)
=
3 e_p(x).                                                  (4)

Hence the unique cyclic correction is

U(x)=E_p(x)/3.                                             (5)

The homogeneous equation L(H)=0 has only H=0 because one full p-cycle gives 4H=H and p>3.

## 3. Canonical principal-part obstruction

Let the arithmetic observer be x=m=(p-1)/6 and write eps=x-m.

A modulo-p^3 observer-regular lift exists if and only if E_p is regular at eps=0:

observer-regular split mod p^3
iff
PP_(eps=0) E_p = 0.                                       (6)

If the lower representative is changed by an observer-regular H,

R^(2)' = R^(2)+p^2 H,

then

e_p' = e_p-L(H),

and exact cyclic telescoping gives

E_p' = E_p-3H.                                             (7)

Since H is regular at the observer,

PP E_p' = PP E_p.                                         (8)

Thus PP E_p is independent of the allowed lower-lift representative.

## 4. Coordinates through p^3

The durable lower residual ladder is

H_p -> J_p -> K_p -> L_p -> N_p -> P_p.

After the complete p^2 conditions H_p=J_p=K_p=0, the canonical cyclic defect has principal part

PP E_p
=
(L_p/72) eps^(-3)
+
N_p eps^(-2)
+
P_p eps^(-1).                                             (9)

Indeed U=E_p/3 and the durable coefficient formulas are

U_(-3)=L_p/216,
U_(-2)=N_p/3,
U_(-1)=P_p/3.

Consequently

observer-regular split mod p^3
iff
H_p=J_p=K_p=L_p=N_p=P_p=0.                               (10)

Equation (9) packages the three p^3 conditions as coordinates of one lift-independent principal-part class rather than independent choices of p-adic digit representatives.

## 5. BRC consequence

The minimal canonical obstruction carrier at this precision is not an arbitrary tuple of digit coefficients. It is the principal-part class

[ E_p ] in F_p((eps))/F_p[[eps]].

Wall residues, lifted wall jets, regular-memory intervals, endpoint jets and lower regular gauge values are provenance coordinates used to compute this class. They may be compressed only after proving that the declared future operations factor through a smaller carrier.

Reuse disposition: COMPOSE_APPLIED using the exact p-step cyclic transport, the complete p^2 criterion, the complete p^3 observer criterion, and the residual-faithful BRC observer lease.

## 6. Next exact unit

Do not rebuild the full cyclic gauge or rowwise Omega channel.

The next smallest unit is to derive a principal-part transport law across precision: isolate the four simple wall blocks and their pole-zero prefix memories, encode their highest-pole contributions by generating functions, and determine whether the leading wall moments satisfy a finite recurrence. The target is a precision-independent description of the highest-pole residual tower and a proof of when the original mod-p wall-residue carrier becomes fully determined.
