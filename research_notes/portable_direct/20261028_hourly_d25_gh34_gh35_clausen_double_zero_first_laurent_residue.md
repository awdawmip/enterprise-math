# D25/LIFT GH-34 and GH-35: Clausen double-zero and finite first-Laurent-residue certificate

2026-10-28, TASK_RESEARCH author-portable derivation. Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Logical research lane: chatgpt-research-hourly-enterprise-math-20260923, distinct from CONTROL_PLANE_MAINTENANCE chatgpt-hourly-enterprise-math-20260921.

Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. These are exact scalar auxiliary GH-3 observations, not native X6 dynamics or original W/S/Hasse acceptance.

Dependencies, not newly claimed: GH-13 cyclic rational resolvent, GH-15 endpoint-retaining Laurent telescope, GH-16 obstruction, GH-17 Clausen weighted factorization, GH-18 simple roots, GH-32/33 CM(-24) F zero and double-pole elimination. Mathematical admission and independent review of these dependencies remain separate.

## GH-34: exact unweighted Clausen square and double zero at 9

For a prime p=8m+3>=11 set d=2m, k=F_p and
\[
F_m(z)=\sum_{r=0}^m\frac{(-m)_r^2}{(2m+2)_r r!}z^r,\quad
h_0=1,\quad h_{s+1}=h_s\frac{(4s+3)^3}{(4s+4)(4s+5)(4s+6)}.
\]
Let K_d(z)=sum_{s=0}^d h_s z^s and H_d(z)=sum_{s=0}^d(8s+5)h_s z^s=(8z d/dz+5)K_d(z), where H_d denotes the GH-16 obstruction (not the Laurent finite part, denoted elsewhere by the same letter).

GH-17 supplies H_d=F_m G_m with G_m=16z F_m'+5F_m. Since F_m G_m=(8z d/dz+5)(F_m^2), the difference K_d-F_m^2 is killed by the operator 8z d/dz+5. Every coefficient multiplier 8s+5, 0<=s<=d, is nonzero modulo p: 5<=8s+5<=2p-1, and equality to p would imply 8s=8m-2. Therefore the operator is injective on degree<=d and
\[
\boxed{K_d(z)=F_m(z)^2 \ \text{in }F_p[z].} \tag{GH34}
\]
This uses the previously established GH-17 identity rather than re-proving it.

For every prime p≡19 (mod 24), GH-32 and GH-18 give F_m(9)=0, F_m'(9)≠0. Consequently
\[
K_d(9)=K_d'(9)=0,\quad K_d''(9)=2F_m'(9)^2\ne0,
\quad H_d'(9)=144F_m'(9)^2\ne0.
\]
Thus the unweighted carrier K_d has a root of **exact order 2**, while the weighted GH-16 obstruction H_d has a root of exact order 1. This is compatible with GH-33.

## GH-35: exact two-provenance first-residue formula

Now let p=4d+3>=7 be any prime and z∈F_p^* with z≠1. Define
\[
a_z(x)=z(4x+1)^3/[(4x+2)(4x+3)(4x+4)],\quad
C_0=1,\ C_{r+1}=a_z(r)C_r\ (r<d),
\]
\[
t_j(x)=\prod_{i=0}^{j-1}a_z(x+i),\quad
R_z(x)=\frac1{z-1}\sum_{j=0}^{p-1}(8(x+j)+1)t_j(x).
\]
Let A_0(z), B_0(z) be the coefficients of x^-2 and x^-1 respectively in R_z at x=0. This B_0 is a Laurent residue and is **not** the original Hasse B0. Put j_0=2d+2=(p+1)/2, and let alpha_p be the nonzero coefficient [x^-2](t_{j_0}(x)/z^{j_0}) from GH-16.

Define the finite source sequences, 0<=s<d:
\[
k_0=h_0=1,\quad
k_{s+1}=k_s\frac{(4s+2)^3}{(4s+3)(4s+4)(4s+5)},\quad
h_{s+1}=h_s\frac{(4s+3)^3}{(4s+4)(4s+5)(4s+6)},
\]
\[
\lambda_s=\sum_{t=0}^{s-1}
\left(\frac{12}{4t+3}-\frac4{4t+4}-\frac4{4t+5}-\frac4{4t+6}\right).
\]
All displayed denominators are units on the stated finite ranges. Let
\[
Q_d(z)=\sum_{s=0}^d(8s+3)k_sz^s,\quad
K_d(z)=\sum_{s=0}^d h_sz^s,\quad
H_d(z)=\sum_{s=0}^d(8s+5)h_sz^s,
\]
\[
D_d(z)=\sum_{s=0}^d(8s+5)h_s\lambda_s z^s,
\quad
\lambda_*=
12\sum_{i=0}^{j_0-1}\frac1{4i+1}
-4\sum_{i=0}^{j_0-1}\sum_{\substack{b=2,3,4\\4i+b\ne0\ (p)}}\frac1{4i+b}.
\]
The ordinary products in alpha_p are regularized by dividing out the two actual factors 4x in the denominators at i=d,b=3 and i=2d+1,b=2.

**General theorem:**
\[
\boxed{
 B_0(z)=
 \frac{2zC_d(z)Q_d(z)+
 \alpha_pz^{j_0}[\lambda_*H_d(z)+8K_d(z)+D_d(z)]}{z-1}.
 }\tag{GH35}
\]
Also A_0(z)=alpha_p z^{j_0}H_d(z)/(z-1), consistently with GH-16.

**Proof.** The indices of the first and second denominator zeros in the cyclic sum are i=d and i=2d+1. On j=d+1+s (0<=s<=d) the Laurent residue of t_j is exactly 2z C_d k_s z^s, and its weight 8j+1 reduces to 8s+3. This produces the first summand 2zC_dQ_d.

For j=j_0+s (0<=s<=d), t_j has exactly two simple denominator zeros and no numerator zero. Its coefficient of x^-2 is alpha_p z^{j_0+s}h_s, and the logarithmic first derivative of the regularized unit equals lambda_*+lambda_s. Differentiating the weight gives an additional 8. Therefore the x^-1 coefficient from this band is
\[
\alpha_p z^{j_0+s}h_s[8+(8s+5)(\lambda_*+\lambda_s)].
\]
Summing over s yields the second summand. At j>=3d+3 the numerator zero at i=3d+2 is cubic: after only two denominator zeros, all such t_j have valuation at least +1; the third denominator zero is at i=4d+2 and is outside j<=p-1. There is no further residue. Division by z-1 proves the theorem.

For all target primes p≡19 (mod 24), GH-34 and GH-32 imply H_d(9)=K_d(9)=0. Hence the **two-source target certificate** is
\[
\boxed{ B_0(9)=\frac{18C_d(9)Q_d(9)+
             \alpha_p9^{(p+1)/2}D_d(9)}8\pmod p. }\tag{GH35-target}
\]
The two terms are distinct signed provenance bands: a single-pole band and a two-pole harmonic first jet. Neither may be dropped as redundant merely from the total F-port zero.

Exact sample witnesses: p=19 has (Q,D,C_d,alpha_p)=(7,8,6,2), numerator bands (15,11), B_0=8. For p=43: (Q,D)=(37,12), bands (35,25), B_0=29. For p=67: (Q,D)=(25,48), bands (57,36), B_0=20. These agree with earlier GH-15 Laurent residues.

## Verification and next scientific obligation

A standalone Python standard-library checker independently compared the finite-band formula with direct Laurent-jet traversal of the complete cyclic sum on all 76 primes 11<=p<2001 with p≡3 mod 8, for z=2 and z=9 (152 parameter cases), plus full polynomial Clausen squares and the 37 target-prime double-zero conditions. All passed; finite checks are not universal proofs.

BRC COMPOSE_APPLIED: carrier retains (p,z,r,j), signed band identity, epsilon-jet, h/k coefficients and lambda; observer is the pair (A_0,B_0); future operation is GH-15's finite telescope. The GH34/GH35 scalar readout is not a certified substitute for native six-dimensional X6, time if relevant, original W/S, or the six Hasse source ports.

The **remaining** GH-3 obligation is to prove/refute for every p≡19 mod24
\[
T_{p,9}=C_d(H_d^{finite}+8d+1)-H_0^{finite}+B_0L=0\pmod p.
\]
GH35 resolves B_0 into two exact finite bands but does **not** prove that total cancellation. Next derive an independent arithmetic formula for C_dH_d^{finite}-H_0^{finite}, then test/prove its cancellation with the signed bands and boundary terms. Preserve GH-20/GH-21 p-adic moments, R23/R36 original Green sources, original Hasse H0/B0, [X]U mod p^2, Frobenius eta/kappa, native p=373 and independent Driver review. No Source-native CLAIM/OPEN/checkpoint, Result admission, identity registration or separate review is inferred from GitHub evidence. Existing control issue #1558 remains the support path; no protected prior session/staging or frozen scientific pin was changed.