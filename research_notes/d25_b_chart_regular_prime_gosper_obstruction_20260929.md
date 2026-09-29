# D25 portable research: regular-chart Gosper obstruction after the prime relation

Status: `AUTHOR_PORTABLE_PROOF / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT`

Contributor lineage: `EM-DIRECT-C4D02C`.

This is a portable mathematical unit. It claims no native session, CLAIM, run, canonical checkpoint, Result, review, or theorem admission.

## Source boundary

- Global snapshot: `chatgpt-global-knowledge@7474d45f38f68ae59bd6d4addcc91e9e952ef8c3`.
- Enterprise Math main observed before write: `43c49c8b95afd40e67c00edd94d10da99bc532ee`.
- Canonical D25 local-progress blob: `51dd15a8142f3dda0506a306f9c0693a036f5891`.
- Immediate durable portable predecessor: `research_notes/d25_b_chart_first_pole_finite_part_20260929.md`, blob `c9d586d8554e503c322937b5a3964ccdd2c720b0`.
- The canonical D25 lane already proved the LOW/B11 normal-parameter defect and the explicit double-pole repair port. This unit does not redo that derivative calculation.
- The previous portable unit already ruled out a scalar Gosper antidifference for the original universal rational sequence `b_j`. The present result is different: it asks whether imposing the prime relation `p=6m+1` and passing to the regular finite-field chart creates a new scalar Gosper certificate. It does not.

## 1. Regular chart after the prime relation

Let `p=6m+1>3` be prime, and on the upper regular chart `0<=j<=2m-2` keep

[
b_j=
rac5{32}
rac{(1)_j(5/2)_j(4/3)_j(11/6)_j}
{(3)_j(3/2)_j(5/3)_j(7/3)_j}2^{-j}.
]

Using the exact quotient from the first-pole note,

[
rac{b_j}{Q_j}
=
-rac{(6j+5)(2j+3)}
{6(3j+4)(3j+2)(j+1)(j+2)},
qquad
Q_j=-rac{(5/6)_j}{(2/3)_j}2^{-j},
]

and the congruences

[
rac56equiv m+1,qquad
rac23equiv 2m+1pmod p,
]

all displayed denominators being p-units on this chart, one gets the exact finite-field representative

[
oxed{
b_jequiv T_{m,j}:=
rac{(m+1)_j}{(2m+1)_j}2^{-j}
rac{(6j+5)(2j+3)}
{6(3j+4)(3j+2)(j+1)(j+2)}
pmod p.
}
	ag{1}
]

Thus any scalar hypergeometric telescoper produced only after using `p=6m+1` would have to telescope `T_{m,j}` over the rational function field `Q(m)`.

## 2. Hypergeometric ratio

Direct cancellation gives

[
oxed{
rac{T_{m,j+1}}{T_{m,j}}
=
rac{(j+1)(2j+5)(3j+2)(3j+4)(6j+11)(j+m+1)}
{2(j+3)(2j+3)(3j+5)(3j+7)(6j+5)(j+2m+1)}.
}
	ag{2}
]

A Gosper normal form for (2) is

[
rac{T_{m,j+1}}{T_{m,j}}
=
rac{A(j)}{B(j)}
rac{C(j+1)}{C(j)},
]

with

[
oxed{
A(j)=rac{(j+1)(3j+2)(3j+4)(j+m+1)}{18},
}
	ag{3}
]

[
oxed{
B(j)=rac{(j+3)(3j+5)(3j+7)(j+2m+1)}9,
}
	ag{4}
]

and

[
oxed{
C(j)=rac{(2j+3)(6j+5)}{12}.
}
	ag{5}
]

Multiplying (3)-(5) back out verifies (2) identically in `Q(m,j)`; no prime scan is used.

## 3. Complete scalar Gosper obstruction on the regular chart

Gosper's criterion says that a hypergeometric antidifference

[
G_{m,j+1}-G_{m,j}=T_{m,j}
]

with `G_{m,j}/T_{m,j}in Q(m,j)` exists only if there is a nonzero polynomial `x(j)in Q(m)[j]` satisfying

[
A(j)x(j+1)-B(j-1)x(j)=C(j).
	ag{6}
]

Assume `deg_j x=d>=0` with leading coefficient `c!=0`. From (3)-(4),

[
deg A=deg B=4,qquad
operatorname{lc}(A)=rac12,qquad
operatorname{lc}(B(j-1))=1.
]

Therefore the leading term of the left side of (6) is

[
-rac c2 j^{d+4},
]

which cannot cancel. Hence its degree is exactly `d+4>=4`. But `C(j)` in (5) has degree two. Contradiction.

Consequently

[
oxed{
	ext{there is no scalar hypergeometric Gosper antidifference for }T_{m,j}
	ext{ over }Q(m,j).
}
	ag{7}
]

This obstruction is uniform in `m`; it is not a failed low-degree ansatz.

## 4. What this rules out

The earlier exact-sequence Gosper obstruction left open a possible shortcut: perhaps after imposing the prime relation `p=6m+1`, replacing the regular chart by its finite-field beta-binomial representative, and allowing the certificate to depend on `m`, a new one-state rational telescoper might appear.

Equation (7) closes that loophole.

Therefore the open bridge

[
pB_p+2p,b_{2m-1}+2+rac{5p}{3}equiv0pmod{p^2}
]

cannot be obtained by a scalar first-order Gosper primitive of the regular chart alone. A successful certificate must retain at least one additional state: for example the first-pole finite part, an inhomogeneous harmonic/parameter jet, or a genuinely coupled two-ended state. This agrees with the independent canonical D25 warning that the normal parameter direction/double-pole moment cannot be replaced by the tangent Dixon value.

This is an information/certificate-class obstruction only. It does not prove the open bridge and does not promote the portable finite-part conjecture.

## 5. BRC typing

Population: regular upper-chart rows `0<=j<=2m-2`, with the first excluded pole `j=2m-1` retained as an external port.

Observer: finite prefix modulo `p`, with future operation being a lift to the pole finite part modulo `p^2`.

Safe compression used: on the regular chart, replace `b_j` modulo `p` by the beta-binomial representative `T_{m,j}` in (1).

Unsafe quotient ruled out: discard every additional port and replace the whole chart by one scalar hypergeometric primitive.

Repair implication: at least one non-scalar/in-homogeneous coordinate must remain. The existing candidate is the first-pole finite part `beta_p`; the canonical LOW/B11 lane independently exhibits a normal-derivative/double-pole repair port.

Resolution:
`COMPOSE_APPLIED / REGULAR_CHART_SCALAR_GOSPER_OBSTRUCTION / ADDITIONAL_REPAIR_STATE_REQUIRED`.

## 6. Exact next unit

Do not retry one-state Gosper summation, either before or after the prime reduction.

The next smallest unit is to construct a two-component inhomogeneous adjoint for the regular prefix plus the first excluded pole. Concretely, augment the beta-binomial state by one source-typed repair coordinate and ask whether the row defect can be made an exact finite difference whose terminal boundary is

[
p,b_{2m-1}=-1+peta_ppmod{p^2}.
]

If the natural harmonic/normal-parameter coordinate fails, preserve the explicit residual as the next repair port instead of enlarging the state without evidence.
