# D25 portable research: explicit factorization of the p^3 double-pole residual

Status: AUTHOR_PORTABLE_PROOF / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT

This checkpoint continues the same portable upper-B-chart lane after the complete p^3 observer criterion. It does not claim a native session, CLAIM, run, Result, review, or theorem admission.

## Source boundary

- GLOBAL_KNOWLEDGE_V1 canonical main: 8c863c7ec308cfc74dc325af21e41da24d0f10a7.
- Enterprise Math canonical main: ff1e5a5862eba2eb7cd0c6d9159a7191aa2f8fec.
- P000 remains ACTIVE_LOCKED.
- Canonical D25 local-progress blob: 51dd15a8142f3dda0506a306f9c0693a036f5891.
- Portable predecessor head: 5647d2b0052a4e2e76763d0e21728ef92c26040a.
- The current recovery_status write transport remains host-blocked before Issue creation; last independently verified success is Issue #2578 with session_state=ABSENT and execution_authorized=false.

## 1. Goal

The preceding checkpoint defines

N_p := D_{-2} + (11/36) r(0),

with

U_{-2}=N_p/3

after H_p=J_p=K_p=L_p=0.

The present unit factors D_{-2} into a second lifted wall jet plus quadratic regular-memory holonomy. It does not rebuild the full p-term cyclic gauge.

Retain

F_j(eps)=K(m+j+eps)Q_j(m+eps),

S_p(m+eps)=sum_{j=0}^{p-1}F_j(eps),

and the four durable wall groups

G_(1/4), G_(1/2), G_(3/4), G_1.

## 2. Second lifted wall double-pole jet

For each wall group c define the exact coefficient, computed before division,

Zhat_c
:=
[eps^(-2)] sum_{j in G_c} F_j(eps)
in Z/p^3 Z.                                             (1)

At mod p there is no eps^(-2) coefficient. At the first divided digit, the total wall contribution is the durable value

B_{-2}=J_p/12

once H_p=0.

Therefore if H_p=J_p=0, the exact grouped coefficient

Zhat_(1/4)+Zhat_(1/2)+Zhat_(3/4)+Zhat_1

is divisible by p^2.

Define the second lifted wall double-pole jet

V2_p
:=
[
 Zhat_(1/4)+Zhat_(1/2)+Zhat_(3/4)+Zhat_1
]/p^2
mod p.                                                   (2)

This quotient is taken only after summing the exact grouped coefficients. No independent representative of an individual wall digit is chosen.

## 3. Quadratic regular-memory transport

The first pole-zero pair contributes the exact singular-memory factor

g_1(z)
=
(1+z/3)/(1+z/4)
=
1 + z/12 - z^2/48 + z^3/192 + O(z^4),                  (3)

where z=p/eps.

After both pole-zero pairs, the cumulative factor is

g_12(z)
=
(1+z/3)(1+5z/6)/[(1+z/4)(1+3z/4)]

=
1 + z/6 - 11z^2/144 + 13z^3/288 + O(z^4).              (4)

At the first divided digit, the z coefficients 1/12 and 1/6 generated the durable regular-memory term M_p in the complete p^2 criterion.

At the second divided digit, the only contributions to eps^(-2) from regular intervals come from the quadratic coefficients

-1/48

after the first pair, and

-11/144

after both pairs.

The same Omega/tau transport used in the p^2 checkpoint gives

Q_j(m)=tau_(m+j)/tau_m,

K(n)tau_n=Omega_(n+1)-Omega_n.

Hence the regular-memory contribution to D_{-2} is

Nmem_p
:=
tau_m^(-1) * {
 -(1/48) [
   (Omega_(3m)-Omega_(2m))
  +(Omega_(ceil(9m/2))-Omega_(3m+1))
 ]
 -(11/144) [
   (Omega_(6m)-Omega_(5m+1))
  +(Omega_(7m+1)-Omega_(6m+1))
 ]
}
mod p.                                                   (5)

No additional regular contribution can enter eps^(-2): a p-adic correction of a regular factor is regular in eps, and crossing it with a linear p/eps memory produces only an eps^(-1) term.

Therefore

D_{-2}=V2_p+Nmem_p.                                      (6)

## 4. Explicit fifth residual

Substituting (6) into the complete p^3 coefficient formula gives

N_p
=
V2_p
+
Nmem_p
+
(11/36)r(0).                                            (7)

Thus, after

H_p=J_p=K_p=L_p=0,

the double-pole of the second Hensel correction is

U_{-2}
=
(1/3)[
 V2_p+Nmem_p+(11/36)r(0)
].                                                       (8)

Consequently an observer-regular p^3 splitting requires the explicit condition

V2_p+Nmem_p+(11/36)r(0)=0.                              (9)

This is the promised factorization of N_p into:

- one exact lifted wall double-pole jet;
- one quadratic regular-memory holonomy;
- one universal q-cycle centering term.

## 5. Why no lower information is sufficient

The three mod-p residue relations H_p=J_p=L_p=0 collapse the residue vector to the one-dimensional form

(W_(1/4),W_(1/2),W_(3/4),W_1)
=
lambda (18,-40,37,-15).

That reduction does not determine V2_p: the latter depends on the p^2 lift of the exact wall blocks.

It also does not determine Nmem_p from the four residues, because Nmem_p depends on regular interval transport between walls.

Therefore the p^3 double-pole obstruction cannot be represented faithfully by the mod-p wall residue carrier alone. The smallest currently proved carrier must retain both the lifted wall jet and regular-memory holonomy.

Reuse disposition: COMPOSE_APPLIED using the durable wall groups, complete p^2 criterion, leading p^3 wall moment, Omega/tau transport, and the residual-faithful BRC observer lease.

## 6. Verification

The two singular-memory expansions used above were checked exactly:

g_1(z)
=
1 + z/12 - z^2/48 + z^3/192 - z^4/768 + ...,

g_12(z)
=
1 + z/6 - 11z^2/144 + 13z^3/288 - 71z^4/2304 + ....

Equation (6) follows coefficientwise because:
- wall groups are the only terms singular before the pole-zero cancellations;
- regular intervals after the first pair carry g_1;
- regular intervals after both pairs carry g_12;
- at p^2 eps^(-2), only their quadratic z^2 coefficients survive.

This is a structural coefficient proof, not an empirical prime scan. No target prime satisfying the preceding H=J=K=L=0 conditions is currently known from the retained finite scans, so no vacuous numerical sufficiency claim is added.

## 7. Next exact unit

The remaining p^3 principal coefficient is the simple pole

P_p
=
D_{-1}
-(2/3)Gamma_p r(0)
-(2/3)T(0)
-(13/36)r'(0).

The next smallest unit is to factor D_{-1} by:
1. a second lifted wall simple-pole jet;
2. derivative memory of the two regular interval transports;
3. first p-adic corrections of the regular prefix factors.

The objective is a representation that is invariant under allowed regular lift choices and does not reintroduce the full cyclic gauge.
