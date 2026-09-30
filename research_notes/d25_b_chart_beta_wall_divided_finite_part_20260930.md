# D25 portable research: divided finite part of the symmetric-Beta valuation wall

Status: `AUTHOR_PORTABLE_PROOF / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT`

This unit continues the portable upper B-chart lane on `portable/c4d02c-b11-kummer-dilog-20260927`. It does not claim native session/CLAIM/run authority and does not reopen the canonical LOW/B11 normal-derivative or Research1 Gauss-Manin lane.

## Source boundary

- GLOBAL_KNOWLEDGE_V1 canonical main observed for this unit: `688f64b4be0b0594f5a3774bbf88171080ea322e`.
- Enterprise Math main observed for this unit: `912b49c89d29d36b1f5cfe1ed18bc7cb94a3a410`.
- `docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md` blob remains `83723848b8deb6d408e3af6d290088c58a6d88c6`.
- P000 blob remains `7334734bd1cff6d60bd6b73cd0c588fe01c88714`, `ACTIVE_LOCKED`, with residual-faithful discrete-relational research position.
- Canonical D25 local-progress blob remains `51dd15a8142f3dda0506a306f9c0693a036f5891`.
- Immediate durable predecessor on this portable lane: `research_notes/d25_b_chart_beta_m_shift_valuation_wall_residue6_20260930.md`, blob `ffb18bf1fa3087fa0474a9f10d597f9687fbf627`.
- Current control recovery Issue #2578 is read-only and still reports `session_state=ABSENT`, no pending/run/claim/upload/staging, and `execution_authorized=false`. A fresh canonical dispatch attempt for this run was blocked by the host before remote Issue creation, so no control-side effect is claimed.

## 1. Starting wall residue

Let
[
p=6m+1>3.
]
The predecessor studies the (m	o m+1) transport of the single symmetric-Beta terminal observer. Its only (p)-pole comes from the newly exposed (D)-channel row (j=2m-1), and after the next Beta measure is applied the scalar principal-part numerator is
[
oxed{
mathcal V_m
=
rac34,2^{-2m}
rac{(m+2)_{2m-1}}{(2m+4)_{2m-1}}.
}
	ag{1}
]
It proves
[
oxed{mathcal V_mequiv6pmod p.}
	ag{2}
]

Thus the transported observer contains the Laurent contribution
[
rac{mathcal V_m}{p}
=
rac6p+
u_p
quad(mod p),
]
where the next divided finite part is
[
oxed{

u_p:=
rac{mathcal V_m-6}{p}pmod p.
}
	ag{3}
]

The purpose of this unit is to compute (
u_p) exactly.

## 2. Exact reduction to the already-owned Q-endpoint quotient

Set
[
A_m:=
rac{(m+2)_{2m-1}}{(2m+4)_{2m-1}},
qquad
R_m:=
rac{inom{3m}{m}}{inom{4m}{2m}}.
]
The predecessor already used the exact ratio
[
rac{A_m}{R_m}
=
rac{2(2m+1)(2m+3)}
{(4m+1)(4m+2)}.
	ag{4}
]
With (p=6m+1), (4) simplifies exactly to
[
oxed{
rac{A_m}{R_m}
=
rac{p+8}{2p+1}.
}
	ag{5}
]

The durable Q-endpoint lift proves
[
oxed{
R_m
equiv
4^m
left[
1+pleft(H_{3m}-rac12H_might)
ight]
pmod{p^2}.
}
	ag{6}
]
Since (2^{-2m}=4^{-m}), equations (1), (5), and (6) give
[
mathcal V_m
equiv
rac34,
rac{p+8}{2p+1}
left[
1+pleft(H_{3m}-rac12H_might)
ight]
pmod{p^2}.
	ag{7}
]

Now
[
rac{p+8}{2p+1}
=
8-15p+O(p^2),
]
hence
[
oxed{
mathcal V_m
equiv
6+
pleft[
6left(H_{3m}-rac12H_might)
-rac{45}{4}
ight]
pmod{p^2}.
}
	ag{8}
]

Therefore
[
oxed{

u_p
equiv
6left(H_{3m}-rac12H_might)
-rac{45}{4}
pmod p.
}
	ag{9}
]

Using the durable relation (H_mequiv H_{2m}+H_{3m}pmod p),
[
oxed{

u_p
equiv
3(H_{3m}-H_{2m})-rac{45}{4}
pmod p.
}
	ag{10}
]

## 3. Fermat-quotient and endpoint-coordinate forms

On this lane,
[
H_{3m}equiv-2q_p(2),
qquad
H_{2m}equiv-rac32q_p(3)
pmod p.
]
Substituting into (10) yields
[
oxed{

u_p
equiv
-6q_p(2)
+rac92q_p(3)
-rac{45}{4}
pmod p.
}
	ag{11}
]

Equivalently, since
[
q_p(3/4)=q_p(3)-2q_p(2),
]
[
oxed{

u_p
equiv
3q_p(3/4)
+rac32q_p(3)
-rac{45}{4}
pmod p.
}
	ag{12}
]

The durable Q-endpoint digit is
[
delta_p
equiv
rac83q_p(2)-rac43q_p(3)-rac49
=
-rac43q_p(3/4)-rac49
pmod p.
]
Hence
[
oxed{

u_p
equiv
-rac94delta_p
+rac32q_p(3)
-rac{49}{4}
pmod p.
}
	ag{13}
]

Using (H_{2m}equiv-rac32q_p(3)),
[
oxed{

u_p
equiv
-rac94delta_p
-H_{2m}
-rac{49}{4}
pmod p.
}
	ag{14}
]

The last-regular B-chart digit
[
eta_p
equiv
rac{10}{9}q_p(3/4)+3
pmod p
]
gives another equivalent form:
[
oxed{

u_p
equiv
rac{27}{10}eta_p
+rac32q_p(3)
-rac{387}{20}
pmod p.
}
	ag{15}
]

Thus the first divided finite part of the valuation-wall residue is explicit in already familiar arithmetic coordinates.

## 4. BRC consequence: the one-dimensional endpoint quotient is not enough for this divided observer

The fixed-(m) terminal endpoint coordinates (delta_p) and (eta_p) both depend only on
[
q_p(3/4)=q_p(3)-2q_p(2).
]
At the formal two-Fermat carrier level, the tangent direction
[
Delta q_p(2)=t,
qquad
Delta q_p(3)=2t
]
keeps (q_p(3/4)), hence (delta_p) and (eta_p), fixed. But (11) changes by
[
Delta
u_p
=
-6t+rac92(2t)
=
3t.
	ag{16}
]

Therefore the quotient that keeps only the one-dimensional endpoint repair coordinate is not fiber-constant for the new divided-wall observer.

Precisely:
- for the fixed terminal observer modulo (p), (delta_p) / (eta_p) remains a safe compression;
- after the future operation (mmapsto m+1) followed by principal-part subtraction and divided finite-part readout, one additional direction must be restored;
- a sufficient repair coordinate is (q_p(3)), equivalently (H_{2m}), together with (delta_p).

This is a statement about the current formal carrier and observer. It does not assert an independent all-prime algebraic-independence theorem for Fermat quotients.

## 5. Exact regularized wall statement

The singular contribution to the transported symmetric-Beta observer can therefore be written, through its finite part, as
[
oxed{
rac{mathcal V_m}{p}
=
rac6p
-rac94delta_p
-H_{2m}
-rac{49}{4}
pmod p.
}
	ag{17}
]

Equation (17) is the correct one-wall regularization datum for the next transport step. Subtracting only (6/p) and then retaining only (delta_p) would erase the (H_{2m}) / (q_p(3)) component.

This does not yet evaluate the entire regular part of (mathbb E_{m+1}[Phi_{m+1}]); it closes the principal-part contribution through one additional (p)-adic digit and identifies the exact extra port that the remaining finite transport must either cancel or retain.

## 6. Independent regression

A fresh dependency-free exact/modular check was run for every prime
[
p<10000,qquad pequiv1pmod6,
]
611 primes including (p=7).

For each prime it computed the exact rational value of (1), formed
[
(mathcal V_m-6)/ppmod p,
]
and compared it with (9), (11), and (13).

Result:
[
oxed{
611/611,qquad 0	ext{ failures}.
}
]
The scan is regression only. Equations (8)-(15) follow from the exact ratio (5) and the already-proved endpoint lift (6).

Concrete target-prime examples:
[
egin{array}{c|c|c|c}
p&q_p(2)&q_p(3)&(delta_p,
u_p)\ hline
13&3&8&(7,10)\
19&3&18&(11,9)\
31&6&17&(17,6)
end{array}
]

## 7. Next exact unit

Do not treat the universal residue (6) as the complete wall datum.

The next smallest unit is to transport the (p)-integral remainder of the (m	o m+1) symmetric-Beta observer after subtracting the full principal part (17). Test whether its (H_{2m}) / (q_p(3)) component cancels against the regular (V/W/D) transport and the durable endpoint digit. If cancellation occurs, the one-dimensional endpoint quotient is restored at the completed two-ended observer; if not, retain the surviving (H_{2m}) coefficient as the next explicit repair coordinate.

Tool disposition: `COMPOSE_APPLIED` using the existing BRC residual/observer lease, exact valuation enumeration, and operation-safe quotient audit. No new general toolbox family is claimed.
