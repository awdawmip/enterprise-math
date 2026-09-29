# D25 portable research: Hensel half-power endpoint and passive multiplicative-companion no-go

Status: `AUTHOR_PORTABLE_PROOF / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT`

Contributor lineage: `EM-DIRECT-C4D02C`.

This is a portable mathematical unit. It claims no native session, CLAIM, run, canonical checkpoint, Result, review, or theorem admission.

## Source boundary and control status

- Global canonical snapshot used here: `chatgpt-global-knowledge@10ab03fe2d7b06983053b5e27a8707e8d3c19c33`.
- Enterprise Math main used here: `70870d3e91ef371ed11830e2d36e4959ada332bb`.
- Canonical D25 local-progress blob remains `51dd15a8142f3dda0506a306f9c0693a036f5891`.
- Durable portable predecessors are the Q-endpoint lift, first-pole finite-part note, regular-chart scalar Gosper obstruction, and first-wall affine-equivalence note on this branch.
- The current logical conversation's verified recovery receipt remains Issue #2578 / request `recovery-20260929T084128-c4d02c-15`: `session_state=ABSENT`, no pending/run/claim/upload pointers, `execution_authorized=false`, and next action `dispatch`. A fresh dispatch attempt in this run was blocked by the host before remote Issue creation, so no new control request or Source side effect is claimed.
- This unit does not reopen the canonical LOW/B11 normal-Dixon derivative or the Gauss-Manin companion lane.

## 1. Setup

Let
[
p=6m+1>3,qquad N=2m-2,
]
and let
[
B_p=sum_{j=0}^{N}b_j.
]

The durable first-wall note defines
[
b_Nequiv rac{20}{9}+peta_ppmod{p^2}
]
and proves that the still-open upper-chart target is equivalent to
[
B_pstackrel?{equiv}rac{27eta_p+19}{30}pmod p.
	ag{1}
]

The durable Q-endpoint and first-pole notes give
[
delta_pequiv rac83q_p(2)-rac43q_p(3)-rac49pmod p,
]
[
eta_pequivrac38delta_p-rac73
= q_p(2)-rac12q_p(3)-rac52pmod p,
]
and the first-wall affine map
[
eta_pequiv-rac{20}{9}eta_p-rac{23}{9}pmod p.
]
Therefore
[
oxed{
eta_pequiv-rac{20}{9}q_p(2)+rac{10}{9}q_p(3)+3
pmod p.
}
	ag{2}
]

For a rational p-unit (u), write
[
q_p(u):=rac{u^{p-1}-1}{p}pmod p.
]
Using (q_p(3/4)=q_p(3)-2q_p(2)), (2) becomes
[
oxed{
eta_pequivrac{10}{9}q_p(3/4)+3pmod p.
}
	ag{3}
]

Hence (1) is exactly equivalent to
[
oxed{
B_pstackrel?{equiv}q_p(3/4)+rac{10}{3}pmod p.
}
	ag{4}
]

This is a reformulation of the open upper B-chart congruence, not a proof of it.

## 2. A proved Hensel half-power endpoint

Define the normalized last-regular endpoint
[
oxed{
E_p:=
left(1-rac{27p}{20}ight)rac9{20}b_{2m-2}.
}
	ag{5}
]

From (b_N=20/9+peta_p) and (3),
[
rac9{20}b_N
equiv
1+pleft(rac12q_p(3/4)+rac{27}{20}ight)
pmod{p^2}.
]
Therefore
[
oxed{
E_pequiv1+rac p2q_p(3/4)pmod{p^2}.
}
	ag{6}
]

Let
[
chi_p:=left(rac3pight).
]
Since (4) is a square modulo (p),
[
chi_pleft(rac34ight)^{(p-1)/2}equiv1pmod p.
]
Its square is
[
left(rac34ight)^{p-1}
equiv
1+p,q_p(3/4)pmod{p^2}.
]
For odd (p), the square root congruent to (1pmod p) is unique modulo (p^2), and equals
[
1+rac p2q_p(3/4).
]
Consequently
[
oxed{
E_p
equiv
chi_pleft(rac34ight)^{(p-1)/2}
pmod{p^2}.
}
	ag{7}
]

Because ((p-1)/2=3m),
[
left(rac34ight)^{(p-1)/2}=left(rac{27}{64}ight)^m.
]
Thus the complete first lifted digit of the last regular B-chart row is losslessly encoded by one Hensel half-power coordinate.

For the original target residue classes,
[
pequiv13pmod{24}Rightarrowchi_p=+1,qquad
pequiv19pmod{24}Rightarrowchi_p=-1.
]

Combining (4) and (6), the still-open target is equivalently
[
oxed{
1+rac p2left(B_p-rac{10}{3}ight)
stackrel?{equiv}
E_p
pmod{p^2}.
}
	ag{8}
]
Since both sides of (8) are (1pmod p), squaring loses no branch information and gives the equivalent multiplicative form
[
oxed{
1+pleft(B_p-rac{10}{3}ight)
stackrel?{equiv}
left(rac34ight)^{p-1}
pmod{p^2}.
}
	ag{9}
]

Equations (8)-(9) remain conjectural because they are equivalent to (4). Equation (7) is proved.

## 3. Passive multiplicative-companion no-go

The durable regular-chart note defines
[
T_{m,j}equiv b_jpmod p,qquad
r_j:=rac{T_{m,j+1}}{T_{m,j}},
]
and proves that no rational scalar adjoint (a_jinmathbb Q(m,j)) solves
[
r_j a_{j+1}-a_j=1.
	ag{10}
]

The Hensel endpoint (7) suggests a distinct multiplier
[
lambda:=rac{27}{64}.
]
One might try to append a one-way companion carrying this multiplier while leaving the original regular carrier unchanged. Consider the entire class
[
oxed{
M_j=
egin{pmatrix}
r_j&0\
s_j&lambda
end{pmatrix},
qquad
s_jinmathbb Q(m,j),
}
	ag{11}
]
where the first coordinate remains the original (T_{m,j}), and the second coordinate may receive any rational feed-forward source from it.

Suppose there were a rational local adjoint
[
g_j=(a_j,c_j)inmathbb Q(m,j)^2
]
extracting the first-coordinate source:
[
g_{j+1}M_j-g_j=(1,0).
	ag{12}
]

The second component of (12) is
[
lambda c_{j+1}-c_j=0.
	ag{13}
]
If (c_j
eq0) is rational in (j), then
[
rac{c_{j+1}}{c_j}=rac1lambda.
]
But for every nonzero rational function (c(j)inmathbb Q(m,j)),
[
rac{c(j+1)}{c(j)}longrightarrow1
qquad(j	oinfty)
]
over the coefficient field (mathbb Q(m)). Therefore a constant shift ratio can occur only when (lambda=1). Since here
[
lambda=rac{27}{64}
eq1,
]
equation (13) forces
[
c_j=0.
]
Then the first component of (12) reduces exactly to (10), already proved impossible.

Hence
[
oxed{
	ext{no rank-2 lower-triangular rational local adjoint of the form (11) exists.}
}
	ag{14}
]

The argument is independent of the choice of (s_j). More generally, a passive companion block whose rational transfer tends to a constant matrix with no eigenvalue (1) cannot contribute a nonzero rational adjoint coefficient: the leading rational asymptotic would require a left eigenvector with eigenvalue (1).

This closes a specific candidate class suggested by the half-power endpoint. The multiplier (27/64) is a correct terminal coordinate, but it cannot simply be appended as an autonomous/feed-forward state and expected to repair the scalar Gosper obstruction.

## 4. BRC interpretation

Population:
- regular B-chart rows (0le jle2m-2);
- last-regular first digit (eta_p);
- Hensel half-power endpoint (E_p).

Safe compression proved:
- the two Fermat-quotient directions (q_p(2),q_p(3)) collapse to the single observer (q_p(3/4)) for the current endpoint;
- (eta_p) is losslessly replaceable by (E_pmod p^2).

Unsafe extension ruled out:
- append an autonomous/feed-forward constant-multiplier (27/64) companion while leaving the primary transfer unchanged.

Required next structural change:
- either a companion with unit asymptotic multiplier (an additive/divided coordinate);
- or genuine back-coupling that changes the local transfer class while preserving an exact embedding;
- or a two-ended boundary certificate that uses the Hensel endpoint nonlocally.

Resolution:
`COMPOSE_APPLIED / HENSEL_HALF_POWER_ENDPOINT / PASSIVE_CONSTANT_MULTIPLIER_COMPANION_NO_GO / REPAIR_PROVENANCE_RETAINED`.

## 5. Regression

A fresh dependency-free modular regression was executed for every prime
[
p<10000,qquad pequiv1pmod6,
]
611 primes total.

Using the original exact B-chart recurrence:
1. compute (b_{2m-2}mod p^2);
2. verify the proved endpoint identity (7);
3. compute the regular prefix (B_pmod p);
4. falsify the still-conjectural target (4)/(9).

Result:
[
oxed{611/611,qquad0	ext{ failures}.}
]

The finite scan is regression/falsification evidence only. The proof of (7) is the finite p-adic argument above; (4), (8), and (9) remain open.

## 6. Exact next unit

Do not retry scalar Gosper, same-diagonal self-jets, or a passive (27/64) companion.

The next smallest certificate class is a genuinely different transfer:
- a unit-eigenvalue divided/additive companion derived from a faithful p-adic endpoint digit, or
- a back-coupled / two-ended finite adjoint whose terminal boundary is the proved Hensel coordinate (7).

For any candidate, require an exact local identity and an exact terminal match. If it fails, retain the explicit residual as the next repair coordinate rather than enlarging the state without evidence.
