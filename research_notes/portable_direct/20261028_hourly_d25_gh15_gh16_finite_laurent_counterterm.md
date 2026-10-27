# D25 GH-15 / GH-16 — exact Laurent polar counterterm and reflected obstruction polynomial

2026-10-28 Asia/Hong_Kong; TASK_RESEARCH author-side portable result of logical lane chatgpt-research-hourly-enterprise-math-20260923 (not control maintenance or on-hour research). Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Scope: auxiliary scalar hypergeometric source, not native X6 dynamics or original W/S/Hasse acceptance. Status AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

## Exact inputs and model

Consume GH-3 finite hypergeometric observer, GH-7 characteristic-zero obstruction, GH-13 unique cyclic rational resolvent and GH-14 p=19 true rank poles, without repeating their proofs or counting them as new research. The on-hour D25 CM0 Gauss quadrature result (project commit 619e4d0040f1c90b87eaa1469870248aea5c70c8) concerns a *different* Cauchy moment and is not claimed as this lane's work.

Fix a prime p=4d+3>=7 and k=F_p. Fix z in k* other than 1. Define

\[
a_z(x)=z(4x+1)^3/[(4x+2)(4x+3)(4x+4)],\quad f(x)=8x+1,
\quad C_0=1,\quad C_{r+1}=a_z(r)C_r\quad(0\le r<d),
\]
\[
T_{p,z}=\sum_{r=0}^{d} f(r)C_r,\qquad
t_0(x)=1,\quad t_j(x)=\prod_{i=0}^{j-1}a_z(x+i),\quad
R_z(x)=\frac{\sum_{j=0}^{p-1}f(x+j)t_j(x)}{z-1}.
\]

Every C_r is a unit for 0<=r<=d. GH-13 proves the rational identity a_z(x)R_z(x+1)-R_z(x)=f(x) in k(x), but *not* rankwise pole-free evaluation.

## GH-15: exact finite-window Laurent correction (proved for all stated p,z)

For each integer 0<=r<=d, R_z(r+e) has pole order at most two, while R_z(d+1+e) has pole order at most one. Write

\[
R_z(r+e)=A_r e^{-2}+B_r e^{-1}+H_r+O(e),\qquad
A=A_0,\quad B=B_0
\]

where B is a *Laurent coefficient*, not the Hasse B0 input. Set, for 0<=r<d,

\[
\ell_r=\frac{12}{4r+1}-4\sum_{b=2}^4\frac1{4r+b},\qquad
\ell'_r=-\frac{48}{(4r+1)^2}+16\sum_{b=2}^4\frac1{(4r+b)^2},
\quad L=\sum_{r<d}\ell_r,\quad J=\sum_{r<d}\ell'_r.
\]

**Theorem:**

\[
\boxed{T_{p,z}=C_d(H_d+f(d))-H_0+B L+
\frac A2(J-L^2)\quad\text{in }\mathbb F_p.}\tag{GH15}
\]

The B L and A(J-L²)/2 terms cannot be dropped merely because the cyclic rational function solves a global Gosper equation.

**Full proof.** At x=r+e for 0<=r<=d, the four zero-factor positions of t_j occur in increasing order at i=d-r (denominator b=3, valuation -1), i=2d+1-r (denominator b=2, -1), i=3d+2-r (cubed numerator b=1, +3), and i=4d+2-r (denominator b=4, -1). Thus every t_j has e-valuation >=-2. At r=d+1, the cyclically ordered positions are i=d (-1), 2d+1 (+3), 3d+1 (-1), 4d+2 (-1), so the valuation is >=-1. Summing cannot decrease the minimum valuation.

For r<d, the finite nonzero transfer expands as

\[
a_z(r+e)=a_z(r)\left(1+\ell_r e+
\frac{\ell_r^2+\ell'_r}{2}e^2+O(e^3)\right).
\]

Comparing e^-2 and e^-1 in the rational recurrence gives the exact transport invariants

\[
C_r A_r=A,\qquad C_r B_r=B-A\sum_{i<r}\ell_i.
\]

The constant coefficient comparison, multiplied by C_r, is

\[
C_r f(r)=C_{r+1}H_{r+1}-C_rH_r+
\ell_r C_{r+1}B_{r+1}+
\frac{\ell_r^2+\ell'_r}{2}A.
\]

Sum for r=0,...,d-1; use
\(\sum_r \ell_r\sum_{i\le r}\ell_i=
(L^2+\sum_r\ell_r^2)/2\).
Adding the authentic endpoint f(d)C_d proves (GH15), with no evaluation of a singular rational function. QED.

The exact successor-endpoint Laurent expansion is

\[
a_z(d+e)=2z/e-12z+56ze+O(e^2).
\]

If R_z(d+1+e)=V_{-1}/e+V_0+V_1e+..., coefficient comparison yields

\[
A=2zC_dV_{-1},\quad
B_d=2zV_0-12zV_{-1},\quad
H_d=2zV_1-12zV_0+56zV_{-1}-f(d).
\]

Since 2z C_d is a unit, A=0 iff the successor endpoint is regular. This preserves both finite endpoints and all Laurent transport data.

## GH-16: exact one-polynomial double-pole obstruction

Set j0=2d+2 and define the nonzero field element

\[
\alpha_p=\frac1{16}
\frac{\prod_{i=0}^{j_0-1}(4i+1)^3}
{\prod_{\substack{0\le i<j_0,\ b\in\{2,3,4\}\\4i+b\not\equiv0\pmod p}}(4i+b)}
\in k^*.
\]

Define h_0=1 and
\(h_{s+1}=h_s(4s+3)^3/[(4s+4)(4s+5)(4s+6)]\)
for 0<=s<d, and the finite polynomial

\[
\mathcal H_d(z)=\sum_{s=0}^{d}(8s+5)h_s z^s
=\sum_{s=0}^d(8s+5)z^s
\frac{(3/4)_s^3}{(1)_s(5/4)_s(3/2)_s}.
\]

All denominators are units in the stated range.

**Theorem:**

\[
\boxed{A=\frac{\alpha_p z^{2d+2}}{z-1}\mathcal H_d(z).}\tag{GH16}
\]

Thus the unique rational resolvent has poles of order at most one on the entire authentic rank window 0,...,d *if and only if* H_d(z)=0, equivalently the successor rank d+1 has no simple pole. If H_d(z) is nonzero, every rank in the authentic window has an actual double pole by C_r A_r=A with C_r units.

**Proof.** In the cyclic formula for R_z(e), the coefficient of e^-2 is supported *exactly* on j=j0,...,3d+2, after the two denominator zeros at i=d and 2d+1 but before the cubed numerator zero at i=3d+2. The leading coefficient at j0 is alpha_p z^j0; moving from j0+s to j0+s+1 multiplies it by z(4s+3)^3/[(4s+4)(4s+5)(4s+6)]. The weight f(j0+s)=8s+5 modulo p. Therefore the numerator's e^-2 coefficient is alpha_p z^j0 H_d(z); divide by z-1. The transport relation and endpoint equivalence from GH15 prove the remaining assertions. QED.

## Exact finite certificates, limits and continuation

For p=19, d=4, alpha=2 and

\[
\mathcal H_4(z)=5+11z+5z^2+13z^3+14z^4 \pmod{19}.
\]

At z=9, H_4(9)=0, rank-zero A=0 and simple residue B=8; at z=2, H_4(2)=14 and the actual double-pole coefficient A=1. This refutes blanket pole-removability for arbitrary z, without refuting the z=9 conjecture.

| p | d | A at z=9 | B | C_d | H_0 | H_d | L | J | polar counterterm | T_{p,9} |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|19|4|0|8|6|17|5|14|17|17|0|
|43|10|0|29|16|32|21|16|18|34|0|
|67|16|0|20|64|66|62|42|65|36|0|

The executed Python standard-library checker, separately linked in this project, covered 86 primes 7<=p<1000 with p=3 mod 4 at both z=2 and z=9 (172 exact parameter cases). For selected primes 7,11,19,23,43,67,139 it tested every rank's two transport invariants; all cases passed. At all 86 sampled primes H_d(9)=0 and T_{p,9}=0. This is **finite evidence only**, not a universal proof of either vanishing statement. Theorems GH15 and GH16 are general algebraic statements; neither proves GH-3's T_{p,9}=0 universally.

**BRC source-faithfulness:** retain (p,d,j,r,z), the original finite sequence, both finite endpoints, Laurent A/B/H, first- and second-log moments L/J, rank-pole and sign/provenance distinctions. The rank r is an auxiliary scalar observation, not an X6 Cell coordinate. All native research keeps the six-dimensional Heartbeat World spatial basis and separately typed time when required. No collapse into original S MM/LH, original W/S, Hasse six-channel or native Green boundaries is licensed by these auxiliary identities.

**Next exact mathematical action:** prove or refute H_{(p-3)/4}(9)=0 for all p=19 mod 24 by a characteristic-p CM/WZ certificate; if proved, use GH15 with A=0 to isolate the remaining B L counterterm and test the original GH-3 T_p obstruction independently. Preserve GH-10's two next-digit moments, S MM/LH labels and finite/positive-infinity boundaries, then investigate R23/R36 source-faithful Green coupling. Original H0/B0, [X]U mod p², Frobenius eta/kappa and native p=373 still require real native execution. No formal Source CLAIM/open/checkpoint, Research-Activity registration, independent Driver admission or mathematical promotion is asserted. Control fault follows issue #1558, native experiment support issue #1559.