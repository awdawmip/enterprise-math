# D25 portable research: Q-shell three-channel residual and support-minimal local repair

Status: `AUTHOR_PORTABLE_PROOF / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT`

Predecessor portable lineage: `EM-DIRECT-C4D02C` (historical lineage only; this scheduled turn does not claim that native conversation/session identity).

## Source / authority boundary

- GLOBAL_KNOWLEDGE_V1 canonical main observed for this unit: `3fd74ab314cf7744415c9f8574a032ba3e5c3d5b`.
- Enterprise Math main observed for this unit: `be31c9c1928a40cebfb390ad97f37868c8b1b5a5`.
- `docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md` blob: `83723848b8deb6d408e3af6d290088c58a6d88c6`.
- P000 blob remains `7334734bd1cff6d60bd6b73cd0c588fe01c88714`, `ACTIVE_LOCKED`, research position `RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM`.
- Canonical D25 local-progress blob remains `51dd15a8142f3dda0506a306f9c0693a036f5891`; this unit does not redo the LOW/B11 normal-Dixon derivative or double-pole port.
- Portable branch head immediately before this write: `ec0b86cb21200042926f82b39ff303371105c870`; branch was `ahead=5 / behind=32` relative to current main, merge base `cb1ac1d3822fadf586cea44acaf724dcb4623a25`.
- Historical control recovery Issue #2578 is read-only evidence for its own authenticated subject/session: `session_state=ABSENT`, no pending/run/claim/upload/staging, `execution_authorized=false`, `source_authority_verified=false`. It is not used here as current ownership or write authority.

## 1. Durable input

Let
[
p=6m+1>3,qquad N=2m-2,qquad J=2m-1,
]
and
[
B_p=sum_{j=0}^{N}b_j.
]
The durable portable lane has
[
Q_j=-rac{(5/6)_j}{(2/3)_j}2^{-j},
qquad
rac{b_j}{Q_j}
=
-rac{(6j+5)(2j+3)}
{6(3j+4)(3j+2)(j+1)(j+2)}.
]
It also proves
[
Q_Jequiv-rac83pmod p
]
and reduces the still-open upper-chart target to
[
B_pstackrel?{equiv}q_p(3/4)+rac{10}{3}pmod p.
	ag{1}
]

Define the exact Q-transfer
[
q(j):=rac{Q_{j+1}}{Q_j}
=rac{6j+5}{4(3j+2)}
]
and the Q-twisted difference
[
Delta_Q R(j):=q(j)R(j+1)-R(j).
]
Then
[
Q_jDelta_QR(j)=Q_{j+1}R(j+1)-Q_jR(j).
]

## 2. Exact shell decomposition

Partial fractions give
[
rac{b_j}{Q_j}
=
-rac1{6(j+1)}
+rac7{48(j+2)}
-rac5{16(3j+2)}
+rac3{8(3j+4)}.
	ag{2}
]

Choose
[
R_0(j):=rac1{6(j+1)}.
]
Direct rational simplification gives
[
oxed{
Delta_QR_0(j)
=
-rac1{6(j+1)}
+rac7{96(j+2)}
+rac1{32(3j+2)}.
}
	ag{3}
]
Therefore
[
oxed{
rac{b_j}{Q_j}
=
Delta_QR_0(j)+ho(j),
}
	ag{4}
]
where
[
oxed{
ho(j)=
rac7{96(j+2)}
-rac{11}{32(3j+2)}
+rac3{8(3j+4)}.
}
	ag{5}
]
Equivalently,
[
ho(j)=
rac7{96}rac1{j+2}
-rac{11}{96}rac1{j+2/3}
+rac18rac1{j+4/3}.
	ag{6}
]

Summing (4) over (0le jle N) telescopes the Q-boundary exactly:
[
oxed{
B_p=
rac{Q_J}{6(J+1)}+rac16+mathcal R_p,
}
	ag{7}
]
with
[
oxed{
mathcal R_p:=
sum_{j=0}^{2m-2}Q_j
left[
rac7{96(j+2)}
-rac{11}{32(3j+2)}
+rac3{8(3j+4)}
ight].
}
	ag{8}
]

Since (J+1=2m), (12m=2(p-1)), and (Q_Jequiv-8/3pmod p),
[
rac{Q_J}{6(J+1)}+rac16
=
rac{Q_J}{12m}+rac16
equivrac32pmod p.
	ag{9}
]
Thus
[
oxed{
B_pequivrac32+mathcal R_ppmod p.
}
	ag{10}
]

Consequently the durable open target (1) is exactly equivalent to the three-channel residual target
[
oxed{
mathcal R_p
stackrel?{equiv}
q_p(3/4)+rac{11}{6}
pmod p.
}
	ag{11}
]
Using the durable endpoint digit (delta_p=(Q_J+8/3)/p), the same right side is
[
oxed{
q_p(3/4)+rac{11}{6}
=
rac32-rac34delta_p
pmod p.
}
	ag{12}
]
Equation (11) remains conjectural because it is equivalent to the original upper-chart target.

## 3. Support-minimality in the simple-pole Q-shell class

Let
[
P={-1,-2,-2/3,-4/3}.
]
Consider rational shell corrections (R(j)inmathbf Q(j)) subject to the following explicitly restricted certificate class:

1. (S(j)-Delta_QR(j)), where (S=b_j/Q_j), has no finite pole locations outside (P);
2. all retained finite poles are simple;
3. the residual has no polynomial part.

This is a local support-preservation condition, not a claim about all rational cohomology classes.

Under these conditions, the only possible finite pole of (R) is a simple pole at (j=-1). The reason is orbit-by-orbit under the shift (jmapsto j-1):

- a pole of (R) at (eta) contributes through (-R(j)) at (eta) and through (q(j)R(j+1)) at (eta-1);
- outside the allowed pole set, cancellation would require an adjacent pole of (R), forcing a finite shift chain;
- in the integer orbit, the only chain that can terminate at allowed poles without propagating indefinitely is the single pole (-1), whose shifted image is the allowed pole (-2);
- the (1/3) orbit contains the allowed (q)-pole (-2/3), but a pole of (R) in that orbit propagates indefinitely to the left or right; regular (R) may still change the (-2/3) residue through the factor (q);
- the (2/3) orbit has the allowed pole (-4/3) but no zero/pole of (q) that terminates an (R)-pole chain;
- the zero of (q) at (-5/6) does not permit a finite support-preserving chain because the opposite end would introduce an unallowed pole;
- any nonzero polynomial part of (R) produces a nonzero polynomial part in (Delta_QR), since (q(j)	o1/2), contradicting condition 3.

Hence
[
R(j)=rac{a}{j+1}
]
is the complete correction family in this restricted shell class.

For general (a),
[
Delta_Qrac{a}{j+1}
=
-rac{a}{j+1}
+rac{7a}{16(j+2)}
+rac{3a}{16(3j+2)},
]
and therefore
[
oxed{
S-Delta_QR=
rac{6a-1}{6(j+1)}
-rac{7(3a-1)}{48(j+2)}
-rac{3a+5}{16(3j+2)}
+rac3{8(3j+4)}.
}
	ag{13}
]

The first three coefficients vanish respectively at
[
a=rac16,qquad a=rac13,qquad a=-rac53,
]
while the (3j+4) coefficient is invariant and nonzero. Thus no single (a) cancels more than one of the four original pole locations. Every support-preserving simple-pole Q-shell reduction retains at least three pole channels, and (a=1/6) attains this lower bound via (5).

Therefore
[
oxed{
	ext{three retained pole channels are minimal in this explicitly declared local shell class.}
}
	ag{14}
]

This does **not** rule out nonlocal/two-ended certificates, certificates that introduce new intermediate pole locations and later cancel them, or terminal observer quotients such as (11).

## 4. Hypergeometric typing of the three channels

For
[
U_a(N):=sum_{j=0}^{N}rac{Q_j}{j+a},
]
one has the exact finite representation
[
oxed{
U_a(N)
=
-rac1a,
{}_3F_2^{[N]}
left(
egin{matrix}1,5/6,a\2/3,a+1end{matrix};rac12
ight),
}
	ag{15}
]
where the superscript means truncation after (j=N).

Thus
[
oxed{
mathcal R_p=
rac7{96}U_2(N)
-rac{11}{96}U_{2/3}(N)
+rac18U_{4/3}(N).
}
	ag{16}
]
The middle channel simplifies by cancellation of the common (2/3) parameter:
[
oxed{
U_{2/3}(N)
=
-rac32,
{}_2F_1^{[N]}
left(
1,rac56;rac53;rac12
ight).
}
	ag{17}
]

This identifies a concrete next interface: one truncated ({}_2F_1) channel and two truncated ({}_3F_2) channels, rather than an unspecified extra state.

## 5. BRC / toolbox disposition

Applied existing interfaces rather than inventing a new tool family:

- `T0_BRC`: retained row provenance, pole locations, valuation wall and terminal observer;
- `T1_SCALE_ENUMERATION_VALUATION`: used exact shell extraction / finite-difference certificate logic;
- `T6_OPERATION_SAFE_QUOTIENT`: distinguished the local-shell observer from the terminal scalar observer.

Reuse resolution:
[
oxed{	exttt{COMPOSE_APPLIED}.}
]

Population: regular rows (0le jle2m-2) plus the owned endpoint (Q_J).

Local future operation: Q-twisted finite differencing without introducing new pole support.

Local minimal carrier: three residual pole channels (14).

Terminal observer: only (mathcal R_pmod p). At that later observer the three channels may be collapsed only after proving a relation such as (11); the present shell-minimality theorem does not forbid such a terminal quotient.

## 6. Independent regression

A fresh dependency-free modular check was run for all
[
p<10000,qquad pequiv1pmod6,
]
611 primes.

Verified independently from the original (b_j) recurrence and the (Q_j) recurrence:

1. the exact modular decomposition (7)-(10);
2. the boundary term in (9);
3. equivalence of the original open target (1) and residual target (11).

Results:
[
oxed{
611/611	ext{ decomposition passes},qquad
611/611	ext{ boundary passes},qquad
0	ext{ equivalence mismatches}.
}
]
The same finite sample has 611/611 agreement with the still-open congruence on both sides, but that is regression/falsification evidence only and is not used as a proof of (1) or (11).

The algebraic identities (2)-(17) are exact finite rational identities; finite scanning is not their proof.

## 7. Next exact unit

Do not retry scalar Gosper or re-enter the canonical LOW/B11 normal-derivative lane.

Work directly on the three-channel residual (16). The smallest next unit is to derive a contiguous/two-ended relation that transports
[
(U_2, U_{2/3}, U_{4/3})
]
to the already-owned endpoint digit (delta_p), while preserving the cutoff (N=2m-2). The ({}_2F_1) middle channel (17) is the lowest-order entry point. If a contiguous reduction leaves a nonzero boundary/tail term, retain that exact term as the next repair coordinate rather than hiding it in a larger state.

