# D25/LIFT GH-38 and GH-39: resonant Picard–Fuchs defect and full Gauss–Clausen tail

2026-10-28, TASK_RESEARCH author-side portable proof, NOT_ADMITTED / UNREVIEWED / REGISTER_PENDING. Mother ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION OPEN; task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Logical Research lane chatgpt-research-hourly-enterprise-math-20260923 is distinct from maintenance chatgpt-hourly-enterprise-math-20260921. No service-signed session, CLAIM, run or Source checkpoint is claimed. Preserve frozen science Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 and P000.

## Exact definitions

Let p=4d+3 >=7 be prime, k=F_p, theta=z d/dz. For 0<=r<d set c_0=a_0=1,

\[
c_{r+1}/c_r=\frac{(4r+1)^3}{(4r+2)(4r+3)(4r+4)},\quad
a_{r+1}/a_r=\frac{(8r+1)^2}{16(4r+3)(r+1)}.
\]

All displayed denominators are units. Define

\[
S_d(z)=\sum_{r=0}^dc_rz^r,\quad
T_d(z)=(8\theta+1)S_d(z)=\sum_{r=0}^d(8r+1)c_rz^r,\quad
B_d(z)=\sum_{r=0}^da_rz^r.
\]

This T_d(9) equals the original GH-3 finite truncated sum; B_d here is a Gauss polynomial, NOT the source Hasse B0 nor the GH-15 Laurent B_0.

## GH-38: exact nonzero resonant forcing (PROVED)

Define operators

\[
\mathscr D_3=\theta(\theta-\tfrac12)(\theta-\tfrac14)-z(\theta+\tfrac14)^3,\qquad
\mathscr D_2=\theta(\theta-\tfrac14)-z(\theta+\tfrac18)^2.
\]

For every stated p,

\[
\boxed{\mathscr D_3S_d(z)=\tfrac18c_dz^{d+1},\qquad
\mathscr D_2B_d(z)=-\tfrac{25}{64}a_dz^{d+1}.}
\]

PROOF. The coefficient of z^n in D_3 S_d, setting c_n=0 for n>d, is
n(n-1/2)(n-1/4)c_n-(n-3/4)^3c_{n-1}. It is zero for n=0,...,d by the c recurrence. The sole remaining coefficient at n=d+1 is -(d+1/4)^3 c_d=c_d/8, because d+1/4=-1/2 in F_p. Likewise the coefficient of z^n in D_2 B_d is n(n-1/4)a_n-(n-7/8)^2a_{n-1}. Only n=d+1 remains; it equals -(d+1/8)^2 a_d=-25a_d/64, because d+1/8=-5/8 in F_p. None of the defining factors vanishes on 0<=r<d: in particular 4d+3=p is encountered only at the NEXT Gauss step, and 8r+1=0 would require p=1 mod8, while p=3 or 7 mod8. Hence a_d,c_d are nonzero. QED.

IMPLICATION: the finite polynomial cannot be substituted as a homogeneous characteristic-p Picard–Fuchs/Gauss solution. The exact boundary resonance term must be retained before any special-value or Hasse/CM argument. This is an independent differential-observer obstruction, distinct from GH-37's cyclic Laurent return-band diagnosis.

## GH-39: full signed Gauss-square source tail (PROVED)

The formal Clausen identity

\[
{}_2F_1(\tfrac18,\tfrac18;\tfrac34;z)^2
={}_3F_2(\tfrac14,\tfrac14,\tfrac14;\tfrac12,\tfrac34;z)
\]

holds in Q[[z]] (or by the symmetric-square relation of the normalized second-order Gauss equation with the third-order equation above). Through degree d, every denominator is invertible modulo p, so it reduces to the exact statement

\[
\boxed{S_d(z)\equiv B_d(z)^2 \pmod{z^{d+1}}}.
\]

Let b_n=\sum_{0<=i,j<=d,\ i+j=n}a_ia_j (0<=n<=2d), retain ordered pair source labels (i,j), and define

\[
Q_d(z)=B_d(z)+16\theta B_d(z)=\sum_{r=0}^d(16r+1)a_rz^r,\quad
E_d(z)=\sum_{n=d+1}^{2d}(8n+1)b_nz^n.
\]

Then the following is a pointwise-valid polynomial identity over F_p, NOT merely a truncated-series identity:

\[
\boxed{T_d(z)=B_d(z)Q_d(z)-E_d(z).}
\]

PROOF. The Clausen coefficient equality gives b_n=c_n for n<=d. Applying the operator (8theta+1) to the FULL polynomial B_d^2 yields B_d(B_d+16theta B_d) by the product rule. Separating its coefficients into n<=d and n>d yields T_d+E_d, establishing the formula. QED.

At p=19, d=4, z=9, exact residues are T_d(9)=0, B_d(9)=2, Q_d(9)=6 and E_d(9)=12. Both product and omitted tail are nonzero; omitting the high tail would falsely calculate T_d(9)=12. The full coefficient and exact finite-field check scripts are separate reproducible author evidence.

This does NOT independently prove T_d(9)=0: the identity is source-complete but only reduces the open arithmetic target to an independent evaluation of E_d(9) relative to B_d(9)Q_d(9). Recombining the convolution to get T=T, or evaluating the low-degree congruence modulo z^{d+1} at nonzero z, is invalid as a vanishing proof.

## Verification and next exact unit

Locally executed Python standard-library finite-field checker passed 154 prime cases 7<=p<2000, p=3 mod4 for all polynomial coefficients, both resonant defects, pairwise convolution and exact high-tail identity. Additional direct checks of T_d(9)=0 and T'_d(9) !=0 passed all 338 primes 7<=p<5000, p=3 mod4. The latter are FINITE OBSERVATIONS, not universal theorems or Source admission. Exact selected samples (p: T,Tprime,B,Q,E):
7:(0,3,6,2,5); 11:(0,2,7,9,8); 19:(0,14,2,6,12); 43:(0,7,15,42,28); 67:(0,25,38,37,66).
No native X6/primitive experiment or independent Driver mathematical review was performed.

BRC COMPOSE_APPLIED: carrier retains ordered pairs (i,j), their sum n, exact signed F_p weights, low/high degree split, theta differentiation and evaluation provenance. The b_n quotient is sufficient for THESE polynomial observers only; it does not collapse original W/S, F/G, GH-15 first Laurent residue, the six Hasse ports or native X6 state. P000 remains unchanged.

NEXT (OPEN): obtain an arithmetic certificate for E_d(9)=B_d(9)Q_d(9) independent of the defining convolution (especially for p=19 mod24). Test genuine Frobenius/CM special-value or nonlocal WZ relations without assuming the result. Preserve GH-20/21 next-digit, GH-5 S, R23/R36 Green, original Hasse six ports, [X]U mod p^2, eta/kappa, native p=373, and independent Driver review. Do not repeat GH-36/GH-37 Laurent reassembly. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.