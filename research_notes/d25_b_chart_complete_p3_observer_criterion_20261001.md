# D25 portable research: complete observer-regular p^3 cyclic-splitting criterion

Status: AUTHOR_PORTABLE_PROOF / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT

This unit continues the same portable upper-B-chart lane. It does not claim a native session, CLAIM, run, Result, review, or theorem admission.

## Source boundary

- GLOBAL_KNOWLEDGE_V1 canonical main for this execution phase: 8c863c7ec308cfc74dc325af21e41da24d0f10a7.
- Enterprise Math canonical main for this execution phase: ff1e5a5862eba2eb7cd0c6d9159a7191aa2f8fec.
- P000 remains ACTIVE_LOCKED.
- Canonical D25 local-progress blob remains 51dd15a8142f3dda0506a306f9c0693a036f5891.
- Portable predecessor head before this checkpoint: 7d5ca1ceede03f47bf362f3e6a6b36d0eedc8819.
- A fresh recovery_status transport for stable conversation_id EM-DIRECT-C4D02C was attempted in this run and was blocked by the host before Issue creation. The last independently read successful recovery remains Issue #2578: session_state=ABSENT, no pending/run/claim/upload/staging, execution_authorized=false.

## 1. Setup

Retain the exact p-step cyclic transport

Q_p(x) R(x+p) - R(x) = S_p(x),

with

Q_p = 4 + p A + p^2 C  (mod p^3),
S_p = 3 r + p B + p^2 D  (mod p^3),

and a putative observer-regular splitting lifted as

R = r + p T + p^2 U.

Here p=6m+1 is in the target classes p == 13 or 19 (mod 24), and the arithmetic observer is x=m.

Expanding R(x+p) through p^2 gives

R(x+p)
 = r + p(r'+T) + p^2(r''/2 + T' + U)
   (mod p^3).

Substitution into the p-step transport yields the two lower Hensel equations

3T = B - 4r' - A r,                                      (1)

3U = D - 4T' - 2r'' - A(T+r') - C r.                    (2)

The durable preceding checkpoints provide the p^2 criterion

H_p = J_p = K_p = 0

and the leading p^3 condition

L_p = 0,

with

U_{-3} = L_p/216.

Assume from now on that H_p=J_p=K_p=L_p=0, so both r and T are observer-regular and U has no eps^(-3) term.

## 2. Universal principal part of the full q-cycle

Write x=m+eps and z=p/eps. After removing the two p-divisible numerator factors and two p-divisible denominator factors from the exact p-cycle product, the singular ratio is

F(z)
=
(1+z/3)(1+5z/6) / [(1+z/4)(1+3z/4)].

Its exact formal expansion is

F(z)
=
1 + z/6 - 11 z^2/144 + 13 z^3/288 + O(z^4).             (3)

The remaining regular cycle factor is p-integral and congruent to 1 modulo p. Therefore the principal coefficients of A and C are

A_{-1} = 2/3,                                             (4)

C_{-2} = -11/36.                                         (5)

For later use define the regular-cycle first digit

G_p(eps)
:=
Q_p(m+eps) / [4 F(p/eps)],

Gamma_p
:=
(G_p(0)-1)/p mod p.

Since G_p is regular at eps=0 and G_p == 1 (mod p), this is well-defined. The only way the regular factor can contribute to the p^2 eps^(-1) coefficient is by crossing its first p-digit with the z/6 term in (3). Hence

C_{-1} = (2/3) Gamma_p.                                  (6)

For p=811, direct exact rational evaluation gives

Gamma_811 = 548,
C_{-1} = 95   (mod 811).

This numerical value is retained only as a regression witness for (6); p=811 does not satisfy the earlier J condition.

## 3. The p^3 double-pole residual

Because r and T are regular, the terms 4T', 2r'', and A(T+r') in (2) have no eps^(-2) contribution. The eps^(-2) coefficient of C r is

(C r)_{-2} = C_{-2} r(0).

Therefore

3 U_{-2}
=
D_{-2} - C_{-2} r(0)
=
D_{-2} + (11/36) r(0).                                  (7)

Define

N_p
:=
D_{-2} + (11/36) r(0).                                  (8)

Then, after H_p=J_p=K_p=L_p=0,

U_{-2} = N_p/3.                                           (9)

Thus an observer-regular p^3 lift also requires N_p=0.

This definition is intentionally source-faithful: D_{-2} is the exact second divided digit of the p-step source cocycle S_p, not a reconstruction from residue-only data. It may be evaluated by the second lifted wall jet plus quadratic regular-memory transport, but no rowwise Omega state is required.

## 4. The final simple-pole residual

Assume in addition N_p=0, so U has neither eps^(-3) nor eps^(-2) principal part.

Write

r(eps)=r_0+r_1 eps+O(eps^2),
T(eps)=T_0+O(eps),

A(eps)=A_{-1} eps^(-1)+O(1),

C(eps)=C_{-2} eps^(-2)+C_{-1} eps^(-1)+O(1),

D(eps)=D_{-1} eps^(-1)+O(1)

after the higher negative powers have been killed by the preceding residual conditions.

Taking the eps^(-1) coefficient of (2) gives

3 U_{-1}
=
D_{-1}
- A_{-1}(T_0+r_1)
- C_{-1} r_0
- C_{-2} r_1.                                           (10)

Using (4)-(6),

3 U_{-1}
=
D_{-1}
- (2/3) Gamma_p r_0
- (2/3) T_0
- (13/36) r_1.                                          (11)

Define the final p^3 observer residual

P_p
:=
D_{-1}
- (2/3) Gamma_p r(0)
- (2/3) T(0)
- (13/36) r'(0).                                        (12)

Then

U_{-1}=P_p/3.                                             (13)

The coefficient 13/36 is not an ad hoc correction. It is the exact combination

A_{-1}+C_{-2}
=
2/3 - 11/36
=
13/36

arising from the simple q-cycle pole acting on r' together with the double q-cycle pole acting on the first Taylor coefficient of r.

## 5. Complete observer-regular p^3 criterion

Under the existing state-linear cyclic observer class, the second divided correction U has pole order at most three:

- D has pole order at most three at this precision;
- C has pole order at most two;
- A has pole order at most one;
- r and T are regular once the complete lower-precision criteria hold.

Therefore the principal part of U is exhausted by U_{-3}, U_{-2}, and U_{-1}.

Combining the durable lower hierarchy with (8) and (12) yields:

An observer-regular cyclic splitting modulo p^3 exists
iff

H_p = 0,
J_p = 0,
K_p = 0,
L_p = 0,
N_p = 0,
P_p = 0.                                                (14)

Equivalently, the precision-typed residual ladder through p^3 is

H_p -> J_p -> K_p -> L_p -> N_p -> P_p.

The criterion is scoped to the current state-linear cyclic gauge class. It is not a theorem that no larger, p-dependent, nonlinear, or nonlocal representation can split the cocycle.

## 6. Formal coefficient audit

A direct symbolic Laurent audit of (2), with

A=a_{-1} eps^(-1)+...,
C=c_{-2} eps^(-2)+c_{-1} eps^(-1)+...,
D=d_{-3} eps^(-3)+d_{-2} eps^(-2)+d_{-1} eps^(-1)+...,

and regular r,T, gives exactly

[eps^(-3)] 3U = d_{-3},

[eps^(-2)] 3U = d_{-2}-c_{-2}r_0,

[eps^(-1)] 3U
=
d_{-1}
-a_{-1}(T_0+r_1)
-c_{-1}r_0
-c_{-2}r_1.

Substituting a_{-1}=2/3 and c_{-2}=-11/36 reproduces (7) and (11) exactly.

The singular-ratio expansion (3) was independently expanded to z^4; its first terms are

1 + z/6 - 11z^2/144 + 13z^3/288 - 71z^4/2304 + ...

and therefore independently certify (4)-(5).

## 7. BRC consequence

The minimal sufficient observer state is precision-dependent.

At p^3, residue-only wall data are not enough. After the lower wall moments vanish, the surviving information needed for the final two poles is:

- the second divided source jets D_{-2}, D_{-1};
- the regular-cycle digit Gamma_p;
- the regular cyclic-gauge jet r(0), r'(0);
- the regular first Hensel value T(0).

This is a strict compression relative to rebuilding the full p-term cyclic gauge or the rowwise Omega channel, but it is not safe to compress further without proving that these jets factor through a smaller future-operation interface.

Reuse disposition: COMPOSE_APPLIED using the durable H/J/K complete p^2 criterion, the durable leading p^3 L obstruction, exact q-cycle singular factorization, and BRC residual/provenance retention.

## 8. Next exact unit

Do not restart the cyclic gauge or rowwise Omega sums.

The next smallest unit is to factor D_{-2} and D_{-1} into explicit lifted wall jets plus regular-memory holonomy, then test whether N_p and P_p admit lower-dimensional endpoint expressions. In particular:

1. express D_{-2} by the second lifted wall double-pole jet and the quadratic regular-memory intervals;
2. express D_{-1} by the second lifted wall simple-pole jet and derivative memory of those intervals;
3. determine whether Gamma_p, r(0), r'(0), and T(0) can be reduced to existing endpoint coordinates without losing observer regularity.

Only after that factorization should a broader cancellation-prime scan be resumed.
