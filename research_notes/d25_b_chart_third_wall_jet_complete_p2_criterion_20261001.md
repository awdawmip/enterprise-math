# D25 portable research: third wall jet and a complete observer-regular p^2 criterion

Status: AUTHOR_PORTABLE_PROOF / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT

This unit continues the same portable upper-B-chart lane. It does not claim a native session, CLAIM, run, Result, review, or theorem admission.

## Source boundary

- GLOBAL_KNOWLEDGE_V1 canonical main for this execution phase: 8c863c7ec308cfc74dc325af21e41da24d0f10a7.
- Enterprise Math canonical main for this execution phase: ff1e5a5862eba2eb7cd0c6d9159a7191aa2f8fec.
- P000 remains ACTIVE_LOCKED.
- Canonical D25 local-progress blob remains 51dd15a8142f3dda0506a306f9c0693a036f5891.
- Portable predecessor head: a8910b41d139886e146c383ecca0271f5ee16e32.
- Fresh recovery_status transport for EM-DIRECT-C4D02C was blocked by the host before Issue creation; last independently read successful recovery remains Issue #2578 with session_state=ABSENT and execution_authorized=false.

## 1. Setup

Let

q(x)=4 (x+1/3)(x+5/6)/((x+1/4)(x+3/4)),

Q_0(x)=1,
Q_j(x)=prod_{i=0}^{j-1}q(x+i),

F_j(eps):=K(m+j+eps)Q_j(m+eps),

where p=6m+1 and p == 13 or 19 (mod 24).

Let

S_p(m+eps)=sum_{j=0}^{p-1}F_j(eps).

If the mod-p cyclic gauge is observer-regular, write

Q_p=4+pA,
S_p=3r+pB

in the punctured p-adic Laurent expansion at eps=0, with r regular. The unique first Hensel correction satisfies

3T=B-4r'-Ar.                                   (1)

The preceding checkpoint gives the first two obstruction coordinates:

H_p = W_(1/4)+W_(1/2)+W_(3/4)+W_1,

J_p = 7W_(1/4)+5W_(1/2)+2W_(3/4),

with

T_{-2}=J_p/36

once H_p=0.

The remaining task is the eps^(-1) coefficient.

## 2. Canonical lifted wall jet

Put

a=floor(m/2),
b=ceil(7m/2).

Partition the mod-p singular terms into four wall groups

G_(1/4) = {a,...,m-1},
G_(1/2) = {2m},
G_(3/4) = {b,...,4m},
G_1     = {5m}.

For c in {1/4,1/2,3/4,1}, define the exact mod-p^2 lifted wall coefficient

What_c := [eps^(-1)] sum_{j in G_c} F_j(eps)
          in Z/p^2 Z.                           (2)

Its reduction is the durable wall residue

What_c mod p = W_c.

If H_p=0 then the exact sum of the four lifted coefficients is divisible by p. Define the first lifted wall jet

V_p :=
(What_(1/4)+What_(1/2)+What_(3/4)+What_1)/p
mod p.                                           (3)

No representative choice is involved in (3): divisibility follows from H_p=0 and the numerator is the actual mod-p^2 Laurent coefficient of the four exact grouped blocks.

## 3. Regular-memory transport

After the first q pole/zero pair

p/4 -> p/3,

a regular prefix retains the punctured first-digit memory

1 + p/(12 eps).

After the second pair

3p/4 -> 5p/6,

the cumulative memory is

1 + p/(6 eps).

Therefore regular terms outside the four singular groups contribute to B_{-1} with weights 1/12 and 1/6.

Using

Q_j(m)=tau_(m+j)/tau_m,

K(n)tau_n=Omega_(n+1)-Omega_n,

the regular-memory contribution telescopes to

M_p :=
tau_m^(-1) * {
 (1/12)[
   (Omega_(3m)-Omega_(2m))
  +(Omega_(ceil(9m/2))-Omega_(3m+1))
 ]
 +(1/6)[
   (Omega_(6m)-Omega_(5m+1))
  +(Omega_(7m+1)-Omega_(6m+1))
 ]
}
mod p.                                           (4)

Each displayed difference is the sum over a regular interval and is valuation-safe as written. Do not split it into unrelated absolute endpoint values before the p-adic cancellation is accounted for.

The full simple-pole coefficient of B is

boxed:
B_{-1}=V_p+M_p.                                 (5)

This is the first point at which the four mod-p residues alone are insufficient: the next observer residual depends on the lifted wall jet V_p and on regular transport memory M_p.

## 4. Universal prefix coefficient A_{-1}

The exact p-cycle product is

Q_p(x)
=
4^p
 (x+1/3)_p (x+5/6)_p
 /[(x+1/4)_p (x+3/4)_p].

At x=m+eps the p-divisible numerator/denominator factors occur at

p/3, 5p/6
and
p/4, 3p/4.

Hence the punctured first divided digit has pole coefficient

A_{-1}
=
4[(1/3-1/4)+(5/6-3/4)]
=
2/3
mod p.                                           (6)

## 5. Third obstruction and complete p^2 criterion

When H_p=0, r is regular. If in addition J_p=0, then B has no double pole. Since A has at most a simple pole and r' is regular, the remaining principal part of T is

3T_{-1}
=
B_{-1}-A_{-1}r(0).

Using (5)-(6), define

K_p :=
V_p + M_p - (2/3) r(0).                        (7)

Then

boxed:
T_{-1}=K_p/3.                                   (8)

Every term in the first divided digit has pole order at most two. Therefore, in this cyclic state-linear observer class,

boxed:
an observer-regular splitting modulo p^2 exists
iff
H_p=0, J_p=0, K_p=0.                            (9)

This is a sufficient as well as necessary criterion at precision p^2: H_p kills the mod-p simple pole, J_p kills the divided double pole, and K_p kills the final divided simple pole.

The class K_p is unchanged by replacing the chosen observer-regular coefficient lift by another regular lift. Such a change modifies T only by a regular function.

## 6. p=811 consistency certificate

For p=811, m=135, the exact mod-p^2 grouped wall coefficients give

V_811=174.

The regular-memory transport (4) gives

M_811=523.

The regular mod-p cyclic gauge has

r(0)=479.

Therefore

B_{-1}
=
174+523
=
697
mod 811,

and

K_811
=
697-(2/3)*479
=
648
mod 811.

Consequently

T_{-1}=648/3=216 mod 811,

matching the independent direct Laurent computation.

This simple-pole value is not needed to block p=811 because J_811=797 already yields T_{-2}=315 != 0. It is retained as a consistency check on the full p^2 hierarchy.

## 7. BRC consequence

The observer-safe residual ladder through p^2 is now

H_p  ->  J_p  ->  K_p.

H_p is the visible four-wall residue.
J_p is the renormalized first wall moment left by pole-zero displacement.
K_p is the first lifted wall jet plus regular-memory holonomy, centered by the cyclic gauge value.

Thus a cancelled residue cannot be represented only by its mod-p wall values at the next precision. Provenance must retain the p-adic wall lift and the regular transport memory.

Reuse disposition: COMPOSE_APPLIED using the durable cyclic cancellation, Hensel criterion, p=811 p^2 obstruction, Omega/tau transport, and BRC valuation retention.

## 8. Next exact unit

The p^2 observer criterion is now closed.

The next smallest unit is to move one precision higher without rebuilding the full cyclic gauge: derive the leading p^3 obstruction after H_p=J_p=K_p=0. The expected object is a second lifted wall jet / quadratic renormalized wall moment. Keep the exact wall groups and regular-memory transport; do not revert to rowwise Omega channels.
