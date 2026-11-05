# D25: exact positive CM-branch hypergeometric transport (2026-11-05)

TASK_RESEARCH, research lane `chatgpt-research-onhour-enterprise-math-20260923`; task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen science `c47e13e4aba0e006366f989d6334d443f6333ae3`. Author-side exact proof, UNREVIEWED / NOT_ADMITTED. Distinct from native H0/B0 p373 (NOT_EXECUTED).

## Positive branch (complements prior negative-branch obstruction)

For 0<z<=1/2 define u=(1+sqrt(1-z))/2 and t=t(z) in (0,1/9] as the unique solution of

J3(u)=J4(v), v=(1+sqrt(1-t))/2,
J3(u)=27(1+8u)^3/[u(1-u)^3],
J4(v)=64(1+3v)^3/[v(1-v)^2].

Existence/uniqueness: J3 and J4 are increasing on the indicated u,v ranges, and u(z),v(t) decrease. Both composite functions decrease continuously from infinity to the same high-conjugate endpoint J0=2417472+1707264 sqrt(2). Indeed
J3'(u)=27(8u+1)^2(8u^2+20u-1)/[u^2(u-1)^4]>0,
J4'(v)=-64(3v+1)^2(9v-1)/[v^2(v-1)^3]>0
on these ranges. Thus t'(z)>0.

Write F_A(z)=2F1(1/6,1/3;1;z), F_B(t)=2F1(1/8,3/8;1;t) and define the positive gauge

M(z)^2 = 3 t(z) sqrt(1-t(z)) / [2 z sqrt(1-z) t'(z)].

**Theorem:** F_A(z)=M(z) F_B(t(z)) exactly throughout 0<z<=1/2.

**Proof:** Both Gauss equations have y''+P(x)y'+Q_q(x)y=0, where P(x)=(1-3x/2)/[x(1-x)], Q_q(x)=-q/[x(1-x)] and q_A=1/18, q_B=3/64. Let I_q=Q_q-P'/2-P^2/4 and Schwarzian S(f;x)=f'''/f'-(3/2)(f''/f')^2. Define

I_J(J)=[J^2-1968 J+2654208]/[4 J^2 (J-1728)^2].

Exact rational-function identities (verified by denominator clearing) are

(4u(1-u))'^2 I_(1/18)(4u(1-u)) + S(4u(1-u);u)/2
 = J3'(u)^2 I_J(J3(u))+S(J3(u);u)/2
 = (8u^2-8u+9)/[36u^2(u-1)^2],

and

(4v(1-v))'^2 I_(3/64)(4v(1-v)) + S(4v(1-v);v)/2
 = J4'(v)^2 I_J(J4(v))+S(J4(v);v)/2
 = (3v^2-3v+4)/[16v^2(v-1)^2].

Schwarzian composition on J3(u(z))=J4(v(t(z))) implies
I_A(z)=t'(z)^2 I_B(t(z))+S(t(z);z)/2.
Thus the two differential operators are gauge-conjugate by any nonzero M satisfying
M'/M=[P(t)t'-t''/t'-P(z)]/2.
Integrating P(x)=1/x-1/[2(1-x)] gives M^2=C t sqrt(1-t)/[z sqrt(1-z)t']. The positive constant C=3/2 is determined at the origin:
J3(u(z))=2^6 3^9 z^(-3)(1+O(z)),
J4(v(t))=2^16 t^(-2)(1+O(t)),
so t(z)~(32 sqrt(3)/243)z^(3/2) and t'(z)/t(z)~3/(2z); hence M(z)->1.
Therefore Y(z)=M(z)F_B(t(z)) solves the A Gauss equation and Y(z)->1 as z->0+. The unique bounded solution of that equation with limit 1 is F_A(z): by reduction of order the other independent solution behaves like F_A(z) log z, since exp(-integral P)=1/[z sqrt(1-z)]. QED.

Endpoint exact derivatives obtained by implicit differentiation (the Galois conjugate of the earlier low-branch jet):
t(1/2)=1/9, t'(1/2)=8 sqrt(2)/27, t''(1/2)=(104-16 sqrt(2))/81,
M(1/2)^2=3 sqrt(2)/4, (M'/M)(1/2)=(sqrt(2)-1)/6.

## New exact weighted period identities

By Clausen, A(z)=F_A(z)^2=3F2(1/2,1/3,2/3;1,1;z),
B(t)=F_B(t)^2=3F2(1/2,1/4,3/4;1,1;t).
The original *infinite* 216 and 2304 integer-coefficient models equal A_inf=A(1/2) and B_inf=B(1/9). Theorem gives
A_inf=(3 sqrt(2)/4)B_inf, hence **8 A_inf^2=9 B_inf^2** exactly.

Let P_inf=A(1/2)+6(1/2) A'(1/2) and Q_inf=B(1/9)+8(1/9) B'(1/9), retaining original weights (6k+1),(8k+1). Differentiating A=M^2 B(t) gives
P_inf=(3 sqrt(2)/4)[(1+6(M'/M)(1/2))B_inf+3t'(1/2)B'(1/9)]
=(3 sqrt(2)/4) sqrt(2)[B_inf+(8/9)B'(1/9)]
=(3/2)Q_inf.
Therefore **2 P_inf=3 Q_inf** exactly.

This DISCHARGES the two previously published high-precision infinite-series candidate identities. The previous *low* J-conjugate branch t'=-8sqrt(2)/27 has a valid canonical-positive-period obstruction; the *high* branch has the proved positive gauge. BRC observer must keep LOW_MINUS and HIGH_PLUS CM branch labels separate, alongside original 216/2304 family, sign, root conjugation, coefficient/weight, and finite vs infinite truncation.

## Checks, status, next unit

The accompanying local checker `d25_plus_j_branch_hypergeom_transport_20261105.py` asserts both universal rational projective identities and endpoint constants exactly in SymPy. The 90-digit checks at z=0.40,0.50,0.60 have relative residual <1e-80; weighted checks <1e-75. These are implementation diagnostics; the proof is the rational-identity + bounded-origin argument above.

The frozen mother target remains Delta_p-R_p=0 (mod p), p=13 or 19 (mod 24). Its finite 216/2304 congruence mod p^3 requires a *finite p-parameter terminator* and signed p^2 half-endpoint carry/upper-shell correction: infinite analytic equality alone supplies neither. Native p373 fixed H0/B0 divided-power [X]U mod139129, rank, Frobenius, eta, kappa, odd observer, and independent replication remain in support Issue #1559, pending actual executor. No Source CLAIM/run or admitted Result is asserted.

Next exact action: expand t(z) at z=0 in Puiseux powers and the algebraic gauge, isolate its two exponent cosets, and test whether a p-parameter finite transform can preserve endpoint/carry data at p=13 and p=19. Preserve distinct native experiment obligations.