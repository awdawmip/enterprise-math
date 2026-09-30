# D25 portable research: single symmetric-Beta terminal observer for the upper B-chart

Status: `AUTHOR_PORTABLE_PROOF / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT`

This unit continues the portable Q-shell lane only. It does not claim native session/CLAIM/run authority and does not reopen the canonical LOW/B11 normal-parameter derivative.

## Source boundary

- GLOBAL_KNOWLEDGE_V1 current phase snapshot: `688f64b4be0b0594f5a3774bbf88171080ea322e`.
- Enterprise Math current phase main: `88e814717bd60144e6a5add07fc4ab596d483b62`.
- Canonical D25 local-progress blob remains `51dd15a8142f3dda0506a306f9c0693a036f5891`.
- Portable branch head immediately before this write: `2f0f7757f66ab15c2a8d094e3eca4a7e59204c92`.
- Durable predecessors this turn:
  - Q-shell three-channel residual;
  - middle-channel symmetric-Beta polynomialization;
  - Q-contiguous two-observable terminal reduction.

## 1. Starting point

Let
[
p=6m+1,qquad N=2m-2,qquad n=N+1=2m-1,
]
and
[
U_a=sum_{j=0}^{N}rac{Q_j}{j+a},
qquad
Q_j=-rac{(5/6)_j}{(2/3)_j}2^{-j}.
]

The preceding exact contiguous reduction proves
[
oxed{
B_p
equiv
3+rac16U_1+rac18left(U_{4/3}-U_{2/3}ight)
pmod p.
}
	ag{1}
]

Thus the still-open target
[
B_pstackrel?{equiv}q_p(3/4)+rac{10}{3}pmod p
]
is equivalent to
[
oxed{
rac16U_1+rac18left(U_{4/3}-U_{2/3}ight)
stackrel?{equiv}
q_p(3/4)+rac13
pmod p.
}
	ag{2}
]

The purpose of this unit is to show that the entire left side of (2), not just the middle channel, factors through one symmetric Beta carrier and one polynomial observer.

## 2. Common symmetric Beta carrier

Define
[
A_{m,j}:=rac{(m+1)_j}{(2m+2)_j}2^{-j}.
	ag{3}
]
Equivalently, for the algebraic Beta moment carrier
[
Xsimoperatorname{Beta}(m+1,m+1),
]
[
A_{m,j}=2^{-j}mathbb E[X^j].
	ag{4}
]

### 2.1 The fractional-channel difference

Directly,
[
egin{aligned}
U_{4/3}-U_{2/3}
&=
sum_{j=0}^{N}
Q_j
left(
rac1{j+4/3}-rac1{j+2/3}
ight)\
&=
sum_{j=0}^{N}
rac{(5/6)_j}{(5/3)_j}2^{-j}
rac1{j+4/3}.
end{aligned}
	ag{5}
]
For (p=6m+1),
[
rac56equiv m+1,qquad
rac53equiv2m+2
pmod p,
]
with all denominators in range (p)-units. Therefore
[
oxed{
U_{4/3}-U_{2/3}
equiv
sum_{j=0}^{n-1}
rac{A_{m,j}}{j+4/3}
pmod p.
}
	ag{6}
]

### 2.2 The (U_1) channel

Similarly,
[
U_1
equiv
-sum_{j=0}^{n-1}
rac{(m+1)_j}{(2m+1)_j}2^{-j}rac1{j+1}
pmod p.
	ag{7}
]
Use
[
rac{(m+1)_j}{(2m+1)_j}
=
rac{(m+1)_j}{(2m+2)_j}
rac{2m+1+j}{2m+1}.
]
Since
[
rac{2m+1+j}{j+1}
=
1+rac{2m}{j+1},
]
we get
[
oxed{
U_1
equiv
-rac1{2m+1}V_m
-rac{2m}{2m+1}W_m
pmod p,
}
	ag{8}
]
where
[
V_m:=sum_{j=0}^{n-1}A_{m,j},
qquad
W_m:=sum_{j=0}^{n-1}rac{A_{m,j}}{j+1}.
	ag{9}
]

Define also
[
D_m:=sum_{j=0}^{n-1}rac{A_{m,j}}{j+4/3}.
	ag{10}
]
Then the complete left side of (2) is
[
oxed{
L_m:=
rac16U_1+rac18(U_{4/3}-U_{2/3})
equiv
-rac{V_m}{6(2m+1)}
-rac{mW_m}{3(2m+1)}
+rac18D_m
pmod p.
}
	ag{11}
]

All three sums in (11) are now observables of the **same** symmetric Beta carrier (4).

## 3. One polynomial observer in (Y=X(1-X))

Put
[
Y:=X(1-X).
]
For (kge0), let
[
C_0(Y)=2,qquad C_1(Y)=1,qquad
C_k(Y)=C_{k-1}(Y)-Y C_{k-2}(Y).
	ag{12}
]
Then
[
C_k(X(1-X))=X^k+(1-X)^k.
]

Because the Beta carrier is symmetric under (Xleftrightarrow1-X), every polynomial (f(X)) may be replaced inside expectation by its symmetric average.

Define
[
P_m^{(V)}(Y)
:=
rac12
sum_{j=0}^{n-1}2^{-j}C_j(Y),
	ag{13}
]
[
P_m^{(W)}(Y)
:=
rac12
sum_{j=0}^{n-1}rac{2^{-j}}{j+1}C_j(Y),
	ag{14}
]
[
P_m^{(D)}(Y)
:=
rac12
sum_{j=0}^{n-1}rac{2^{-j}}{j+4/3}C_j(Y).
	ag{15}
]
Each has degree at most (m-1), and
[
V_m=mathbb E[P_m^{(V)}(Y)],
quad
W_m=mathbb E[P_m^{(W)}(Y)],
quad
D_m=mathbb E[P_m^{(D)}(Y)].
	ag{16}
]

The preceding middle-channel note proves the sharper form
[
P_m^{(V)}(Y)
=
-2^{-n}H_m(Y),
	ag{17}
]
where
[
H_m(Y)=
rac{C_n(Y)+C_{n+1}(Y)-3cdot2^n}{Y+2}
]
is a degree-((m-1)) polynomial.

Now define the single terminal-observer polynomial
[
oxed{
Phi_m(Y)
:=
-rac{1}{6(2m+1)}P_m^{(V)}(Y)
-rac{m}{3(2m+1)}P_m^{(W)}(Y)
+rac18P_m^{(D)}(Y).
}
	ag{18}
]
Then
[
oxed{
L_m
equiv
mathbb E[Phi_m(Y)]
pmod p.
}
	ag{19}
]

Therefore the full open upper-chart target is equivalent to the **single symmetric-Beta polynomial moment**
[
oxed{
mathbb E_{operatorname{Beta}(m+1,m+1)}
[Phi_m(X(1-X))]
stackrel?{equiv}
q_p(3/4)+rac13
pmod p.
}
	ag{20}
]

No cubic/sextic auxiliary extension and no multiple unrelated carriers are needed for this terminal observer.

## 4. Explicit moment expansion

For every (rge0),
[
oxed{
mathbb E[Y^r]
=
rac{(m+1)_r^2}{(2m+2)_{2r}}.
}
	ag{21}
]
If
[
Phi_m(Y)=sum_{r=0}^{m-1}phi_{m,r}Y^r,
]
then the target (20) is equivalently
[
oxed{
sum_{r=0}^{m-1}
phi_{m,r}
rac{(m+1)_r^2}{(2m+2)_{2r}}
stackrel?{equiv}
q_p(3/4)+rac13
pmod p.
}
	ag{22}
]

The reduction is finite, exact at the stated modular observer, and preserves the full cutoff (m).

## 5. BRC interpretation and lease

Population:
- the regular Q-chart rows (0le jle2m-2);
- the common symmetric Beta moment carrier (X);
- invariant coordinate (Y=X(1-X)).

Fine provenance before quotient:
- (U_1);
- (U_{4/3});
- (U_{2/3});
- their distinct pole-orbit labels.

Observer:
[
L_m=rac16U_1+rac18(U_{4/3}-U_{2/3})
]
only.

Allowed future operation for this compression:
- terminal scalar evaluation modulo (p);
- symmetric Beta moment evaluation through degree (m-1).

Safe quotient proved:
- for this observer, all three required sums factor through the one (Y)-polynomial (Phi_m).

Lease boundary:
- if a future step differentiates a parameter, inspects pole-orbit provenance separately, or returns to local Q-shell transport, restore the finer channels. Equation (20) is not a global equivalence of the underlying states.

Tool reuse:
[
oxed{	exttt{COMPOSE_APPLIED}}
]
with `T0_BRC`, `T1_SCALE_ENUMERATION_VALUATION`, and `T6_OPERATION_SAFE_QUOTIENT`.

## 6. Independent regression

A fresh modular computation for every prime
[
p<10000,qquad pequiv1pmod6
]
(611 primes) constructed (V_m,W_m,D_m) directly from the symmetric Beta recurrence (3), independently of the original (b_j) recurrence.

It verified
[
oxed{
B_p-3equiv
-rac{V_m}{6(2m+1)}
-rac{mW_m}{3(2m+1)}
+rac18D_m
pmod p
}
]
for
[
oxed{611/611,qquad0	ext{ failures}.}
]

The identity itself is proved by (5)-(19). The finite scan is regression/falsification evidence only. The final congruence (20)/(22) remains open and is not promoted.

## 7. Next exact unit

The scientific bottleneck is now one explicit polynomial moment (22), not a search for a larger state.

Next:
1. derive the exact (m)-recurrence of the polynomial family (Phi_m) together with the Beta-measure transport
[
mathbb E_{m+1}[f(Y)]
=
rac{2(2m+3)}{m+1},
mathbb E_m[Yf(Y)];
]
2. test whether the resulting finite-dimensional transported observer closes against the durable endpoint digit (delta_p);
3. if closure fails, retain the first cross-measure moment that survives as the explicit repair coordinate. Do not reopen scalar Gosper or erase the local pole-orbit provenance outside the terminal lease.

