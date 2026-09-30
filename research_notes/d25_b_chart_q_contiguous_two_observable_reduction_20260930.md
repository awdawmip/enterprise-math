# D25 portable research: Q-contiguous transport and two-observable terminal reduction

Status: `AUTHOR_PORTABLE_PROOF / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT`

This unit continues the durable Q-shell residual lane. It does not claim native session/CLAIM/run authority and does not alter the canonical D25 source pin.

## Source boundary

- GLOBAL_KNOWLEDGE_V1 current phase snapshot: `688f64b4be0b0594f5a3774bbf88171080ea322e`.
- Enterprise Math current phase main: `88e814717bd60144e6a5add07fc4ab596d483b62`.
- Canonical D25 local-progress blob remains `51dd15a8142f3dda0506a306f9c0693a036f5891`.
- Portable branch head immediately before this write: `3b6f4a9b5dc1eedd0552b3e67e3edccec7f548a7`.
- Immediate durable inputs:
  - Q-shell residual note, blob `06cc7006202ecfdeff338c571e85f86e26b6568e`;
  - middle-channel symmetric-Beta note, blob `c3216b6e54482c23c5272af6af0b13c687770608`.

## 1. General contiguous transport law

Let
[
Q_j=-rac{(5/6)_j}{(2/3)_j}2^{-j},
qquad
q(j)=rac{Q_{j+1}}{Q_j}
=rac{6j+5}{4(3j+2)}.
]
For a parameter (c
eq-1/3), set
[
R_c(j)=rac1{j+c}.
]
A direct partial-fraction calculation gives the exact identity
[
oxed{
Delta_QR_c(j)
:=
q(j)R_c(j+1)-R_c(j)
=
-rac1{j+c}
+
rac{6c+1}{4(3c+1)}rac1{j+c+1}
+
rac1{4(3c+1)}rac1{j+2/3}.
}
	ag{1}
]

For a finite cutoff (N), define
[
U_c(N):=sum_{j=0}^{N}rac{Q_j}{j+c},
qquad
J=N+1.
]
Multiplying (1) by (Q_j) and summing gives
[
oxed{
-U_c(N)
+
rac{6c+1}{4(3c+1)}U_{c+1}(N)
+
rac1{4(3c+1)}U_{2/3}(N)
=
rac{Q_J}{J+c}+rac1c.
}
	ag{2}
]
This is an exact finite contiguous/two-ended transport law; no prime reduction is used.

It shows explicitly how an integer parameter shift transports within one denominator orbit while injecting only the distinguished (c=2/3) channel forced by the pole of the Q-transfer.

## 2. Eliminate the (U_2) channel

The preceding Q-shell note gives, for
[
p=6m+1,qquad N=2m-2,qquad J=2m-1,
]
[
B_p=
rac{Q_J}{6(J+1)}+rac16+mathcal R_p,
]
where
[
mathcal R_p=
rac7{96}U_2
-rac{11}{96}U_{2/3}
+rac18U_{4/3}.
	ag{3}
]

Set (c=1) in (2):
[
-U_1+rac7{16}U_2+rac1{16}U_{2/3}
=
rac{Q_J}{J+1}+1.
	ag{4}
]
Thus
[
rac7{96}U_2
=
rac16U_1
-rac1{96}U_{2/3}
+
rac16left(rac{Q_J}{J+1}+1ight).
	ag{5}
]
Substituting into (3),
[
oxed{
mathcal R_p
=
rac16U_1
+
rac18left(U_{4/3}-U_{2/3}ight)
+
rac16left(rac{Q_J}{J+1}+1ight).
}
	ag{6}
]

Combining with the earlier exact boundary term yields a particularly clean exact prefix formula:
[
oxed{
B_p
=
rac16U_1
+
rac18left(U_{4/3}-U_{2/3}ight)
+
rac{Q_J}{3(J+1)}
+rac13.
}
	ag{7}
]

Equation (7) is exact over the rational finite sum, not merely modulo (p).

## 3. Terminal reduction modulo (p)

The durable Q-endpoint theorem gives
[
Q_Jequiv-rac83pmod p.
]
Also
[
J+1=2m=rac{p-1}{3}equiv-rac13pmod p.
]
Hence
[
rac{Q_J}{3(J+1)}+rac13
equiv
rac83+rac13
=3
pmod p.
]
Therefore
[
oxed{
B_p
equiv
3+
rac16U_1
+
rac18left(U_{4/3}-U_{2/3}ight)
pmod p.
}
	ag{8}
]

The durable open upper-chart target is
[
B_pstackrel?{equiv}q_p(3/4)+rac{10}{3}pmod p.
]
By (8) this is exactly equivalent to
[
oxed{
rac16U_1
+
rac18left(U_{4/3}-U_{2/3}ight)
stackrel?{equiv}
q_p(3/4)+rac13
pmod p.
}
	ag{9}
]

Thus the three separately written Q-shell sums in (3) can be reduced, for the terminal scalar observer, to two summed observables:
[
oxed{
U_1,
qquad
D_{1/3,2/3}:=U_{4/3}-U_{2/3}.
}
	ag{10}
]

This is not a local-support reduction: (D_{1/3,2/3}) still contains two distinct pole-orbit provenances. It is a terminal observer quotient enabled by the exact contiguous boundary (4).

## 4. Shift-orbit interpretation

The local Q-shell note proved that, if one forbids new finite pole locations and retains simple poles, three pole locations are minimal after a Q-twisted shell subtraction.

Equation (2) explains why this does not contradict the two-observable terminal reduction:

- local differencing distinguishes denominator shift orbits;
- finite summation adds the endpoint term (Q_J/(J+c)+1/c);
- after that boundary is retained, an integer-orbit representative such as (U_2) may be transported to (U_1) plus the distinguished (U_{2/3}) channel;
- the final scalar observer only accesses the particular signed combination (U_{4/3}-U_{2/3}).

So the local shell lease and terminal quotient lease are different. The local three-pole carrier must be restored if future operations inspect the two fractional channels separately.

## 5. BRC / toolbox disposition

Existing tools are composed, not extended:

- `T0_BRC`: pole-orbit/provenance and observer lease;
- `T1_SCALE_ENUMERATION_VALUATION`: finite-difference / exact boundary extraction;
- `T6_OPERATION_SAFE_QUOTIENT`: local-vs-terminal quotient distinction.

Reuse resolution:
[
oxed{	exttt{COMPOSE_APPLIED}.}
]

The two-observable compression (10) is safe only for the present terminal scalar target (9). It is not a license to erase the separate (U_{4/3}) and (U_{2/3}) provenance in a later local or parameter-sensitive operation.

## 6. Independent checks

For all
[
p<10000,qquad pequiv1pmod6
]
(611 primes), a fresh modular computation from the original (b_j) recurrence and the independent (Q_j) recurrence checked:

1. equation (8): 611/611 passes;
2. equivalence between the original open target and (9): 0 mismatches;
3. both formulations agree with the finite sample in all 611 cases.

The first two items are consequences of the exact algebra above. The third is regression/falsification evidence only and does not prove the open congruence.

## 7. Next unit

Do not return to scalar Gosper and do not erase the fractional-orbit provenance locally.

The next smallest scientific unit is now the two-observable target (9). The middle component (U_{2/3}) already has a durable symmetric-Beta polynomialization. Attack the signed difference
[
D_{1/3,2/3}=U_{4/3}-U_{2/3}
]
with an exact finite contiguous or symmetry transformation, while retaining its two pole-orbit labels. If that produces a terminal boundary term, compare it directly with the already-owned Q-endpoint digit rather than introducing a generic new state.

