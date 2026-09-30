# D25 portable research: symmetric-Beta polynomialization of the middle Q-shell channel

Status: `AUTHOR_PORTABLE_PROOF / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT`

This unit continues the durable Q-shell residual note on the same portable branch. It does not claim native session/CLAIM/run authority and does not enter the canonical LOW/B11 derivative lane.

## Source boundary

- Current GLOBAL_KNOWLEDGE_V1 main observed before this write: `688f64b4be0b0594f5a3774bbf88171080ea322e`.
- Current Enterprise Math main observed before this write: `88e814717bd60144e6a5add07fc4ab596d483b62`.
- Canonical D25 local-progress blob remains `51dd15a8142f3dda0506a306f9c0693a036f5891`.
- Immediate portable predecessor commit: `b18ff586fa39c34042387e5514452ebf93d0e689`.
- Immediate predecessor artifact: `research_notes/d25_b_chart_q_shell_three_channel_residual_20260930.md`, readback blob `06cc7006202ecfdeff338c571e85f86e26b6568e`.

## 1. The middle residual channel

For
[
p=6m+1,qquad N=2m-2,qquad n=N+1=2m-1,
]
the preceding unit isolates
[
U_{2/3}(N):=sum_{j=0}^{N}rac{Q_j}{j+2/3},
qquad
Q_j=-rac{(5/6)_j}{(2/3)_j}2^{-j}.
]

Using
[
(2/3)_j(j+2/3)=(2/3)_{j+1}=rac23(5/3)_j,
]
one has the exact rational identity
[
oxed{
U_{2/3}(N)
=
-rac32
sum_{j=0}^{N}
rac{(5/6)_j}{(5/3)_j}2^{-j}.
}
	ag{1}
]

Modulo (p),
[
rac56equiv m+1,qquad
rac53equiv2m+2,
]
and all denominators in the displayed range are (p)-units. Hence
[
oxed{
U_{2/3}(N)
equiv
-rac32
sum_{j=0}^{n-1}
rac{(m+1)_j}{(2m+2)_j}2^{-j}
pmod p.
}
	ag{2}
]

## 2. Symmetric Beta carrier

Let (X) denote the normalized Beta moment carrier
[
Xsimoperatorname{Beta}(m+1,m+1)
]
in the purely algebraic sense
[
mathbb E[X^j]
=
rac{(m+1)_j}{(2m+2)_j}.
	ag{3}
]
No analytic probability assumption is needed; (3) is the beta-integral identity for rational moments.

Then (2) becomes
[
oxed{
U_{2/3}(N)
equiv
-rac32
mathbb E
left[
sum_{j=0}^{n-1}left(rac X2ight)^j
ight]
pmod p.
}
	ag{4}
]

The carrier is symmetric under (Xleftrightarrow1-X). Put
[
Y:=X(1-X).
]
This symmetry allows the truncated geometric observer to be polynomialized exactly.

## 3. Odd-cutoff denominator cancellation

For (kge0), define the symmetric power polynomial (C_k(Y)) by
[
C_0=2,qquad C_1=1,qquad
C_k=C_{k-1}-Y C_{k-2}.
	ag{5}
]
If (Y=x(1-x)), then
[
C_k(Y)=x^k+(1-x)^k.
]

Because (n=2m-1) is odd,
[
C_n(-2)+C_{n+1}(-2)
=
(2^n-1)+(2^{n+1}+1)
=
3cdot2^n.
]
Therefore
[
oxed{
H_m(Y):=
rac{C_n(Y)+C_{n+1}(Y)-3cdot2^n}{Y+2}
}
	ag{6}
]
is a genuine polynomial of degree (m-1).

Now use the symmetry (Xleftrightarrow1-X):
[
egin{aligned}
&rac{1-(X/2)^n}{1-X/2}
+
rac{1-((1-X)/2)^n}{1-(1-X)/2}\
&=
rac{6}{2+X-X^2}
-
2^{1-n}
rac{
X^n(1+X)+(1-X)^n(2-X)
}{
2+X-X^2
}.
end{aligned}
	ag{7}
]
The numerator in the second fraction is
[
C_n(Y)+C_{n+1}(Y)
=
(Y+2)H_m(Y)+3cdot2^n.
]
The rational denominator terms in (7) cancel exactly, leaving
[
oxed{
rac{1-(X/2)^n}{1-X/2}
+
rac{1-((1-X)/2)^n}{1-(1-X)/2}
=
-2^{1-n}H_m(Y).
}
	ag{8}
]

Taking the symmetric Beta expectation and dividing by two,
[
oxed{
sum_{j=0}^{n-1}
rac{(m+1)_j}{(2m+2)_j}2^{-j}
=
-2^{-n}mathbb E[H_m(Y)].
}
	ag{9}
]
Combining (4) and (9),
[
oxed{
U_{2/3}(N)
equiv
rac{3}{2^{2m}},
mathbb E[H_m(Y)]
pmod p.
}
	ag{10}
]

Thus the length-((2m-1)) truncated ({}_2F_1) channel has been replaced by one degree-((m-1)) polynomial observer of the symmetric Beta coordinate (Y=X(1-X)).

## 4. Explicit finite moment basis

For (rge0),
[
oxed{
mathbb E[Y^r]
=
rac{(m+1)_r^2}{(2m+2)_{2r}}.
}
	ag{11}
]
Hence if
[
H_m(Y)=sum_{r=0}^{m-1}h_{m,r}Y^r,
]
then
[
oxed{
U_{2/3}(N)
equiv
rac{3}{2^{2m}}
sum_{r=0}^{m-1}
h_{m,r}
rac{(m+1)_r^2}{(2m+2)_{2r}}
pmod p.
}
	ag{12}
]

The first polynomials are
[
H_1=-2,
]
[
H_2=2Y-11,
]
[
H_3=-2Y^2+18Y-47,
]
[
H_4=2Y^3-27Y^2+88Y-191.
]

This is not yet a closed evaluation of the middle channel. It is a strict structural reduction with all cutoff dependence retained.

## 5. BRC interpretation

Population: the (n=2m-1) regular middle-channel rows.

Fine carrier: the ordered row moments ((m+1)_j/(2m+2)_j).

Symmetry quotient: (Xleftrightarrow1-X).

Retained observer: the complete truncated geometric readout through (n).

Safe quotient proved: because (n) is odd, the symmetrized rational denominator cancels identically, so the current observer factors through the single invariant coordinate (Y=X(1-X)) and the polynomial (H_m(Y)).

Information not discarded: cutoff (n=2m-1), the (m)-dependent Beta law, and all moments through degree (m-1).

No positivity claim is transferred to the full three-channel signed residual; positivity/symmetry applies only to this middle Beta carrier before it is recombined with the two other signed channels.

Tool resolution remains
[
oxed{	exttt{COMPOSE_APPLIED}}
]
using `T0_BRC`, `T1_SCALE_ENUMERATION_VALUATION`, and `T6_OPERATION_SAFE_QUOTIENT`.

## 6. Checks

Two independent checks were used.

1. Exact rational check for (m=1,ldots,20): direct truncated Beta sum equals (-2^{-n}mathbb E[H_m(Y)]), 20/20 with zero failures.
2. Modular check for every prime
[
p<10000,qquad pequiv1pmod6
]
(611 primes): the original (Q_j/(j+2/3)) channel agrees with the symmetric-Beta form (2), 611/611 with zero failures.

These checks are regression only. Equations (6)-(12) follow from the exact symmetry and polynomial divisibility argument above.

## 7. Next unit

The middle channel is now reduced to a symmetric polynomial moment problem. The next action is not to introduce another generic state. Test whether the polynomial family (H_m), paired with moments (11), has a contiguous (m)-recurrence whose boundary can be expressed through the durable endpoint digit (delta_p). In parallel, retain the two untouched channels (U_2) and (U_{4/3}); no quotient of the full three-channel residual is yet justified.

