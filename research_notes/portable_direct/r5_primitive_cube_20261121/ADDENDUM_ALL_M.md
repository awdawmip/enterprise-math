# R5 | Universal cubic-root residual for all positive thresholds

2026-11-21. Scientific status AUTHOR_SYMBOLIC_PROOF / EXACT_FINITE_CHECKED / NOT_REVIEWED. Extension of the same branch RESEARCH.md. Frozen 256-hypothesis, 101-price scalar model; source input SHA256 = 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b. Native X6/P000 are unchanged.

## Theorem: primitive cubic-root poles never vanish

Let omega=(-1+sqrt(-3))/2, omega^3=1, omega!=1. Set A3 = [3^32 product_{j=0}^{31}(219+3j)]^-1. As before, F_m^(3)(N) means ONLY the two primitive cube-root partial-fraction contributions of the frozen R5 failure-count generating function.

For EVERY fixed positive m, write m in one of the classes below.

1. m=3k+1, k>=0:
\[
F_m^{(3)}(N)=\frac{(k+1)A_3}{31!}N^{31}(2,-1,-1)_{N\bmod3}+O_m(N^{30}).
\]
The primitive cubic pole order is exactly 32.

2. m=3k+2, k>=0: put b_k=floor((k+2)^2/4) and b_-1=0,
\[
Q_{3k+2}=(216+i\sqrt3)b_k+(873+i\sqrt3)b_{k-1}.
\]
Then
\[
F_m^{(3)}(N)=\frac{2A_3}{30!}N^{30}\operatorname{Re}(Q_m\omega^{-N})+O_m(N^{29}).
\]
The primitive cubic pole order is exactly 31.

3. m=3k+3, k>=0:
\[
Q_{3k+3}=(216-i\sqrt3)\binom{k+2}{2},
\quad F_m^{(3)}(N)=\frac{2A_3}{30!}N^{30}\operatorname{Re}(Q_m\omega^{-N})+O_m(N^{29}).
\]
Again the pole order is exactly 31.

In both latter families Re(Q_m)>0, so no cancellation occurs. The earlier m=2 and m=3 coefficients Q2=217+2omega and Q3=215-2omega are recovered exactly. Combined with the previously established nonzero q=-1 residue, the scalar model needs a joint cost label N mod6 when maintaining both frequency contributions down to the displayed degree.

## Complete all-m rational identities

Let H_{j,m}(q) denote the finite multiplicity polynomial for short event j=0,1,2 (price sets specified in RESEARCH.md). On U={214,...,221}, h(n)=max(a0(n)+a1(n)+a2(n)-1,0) is the three-event overlap weight, and H_{h,m}(q) its finite weighted polynomial. Let H01(m) be the coefficient of s in H_{0,m}(omega(1-s)). Define
\[
Q_m=H01(m)+219(1-\omega)H_{1,m}(\omega)
 +219(2+\omega)H_{2,m}(\omega)-657H_{h,m}(\omega).
\]
Then in Q(sqrt(-3))(z):
\[
\boxed{\sum_{m\ge1}H_{h,m}(\omega)z^m=
 \frac{z(2+z+2z^3)}{(1-z^3)^3(1+z^3)}}.
\]
\[
\boxed{\sum_{m\ge1}Q_mz^m=
\frac{z[-657+(216+I)z+(216-I)z^2-1737z^3+(873+I)z^4+(216-I)z^5-1080z^6]}
{(1-z^3)^3(1+z^3)},\quad I=\sqrt{-3}.}
\]

**Proof by exact generating-function elimination.** Define
\[
M(a,b;z)=(1-abz^2)/[(1-az)(1-bz)(1-abz)],
\]
\[
V(a,b,c;z)=(1-abcz^3)/[(1-abcz^2)(1-az)(1-bz)(1-cz)],
\]
\[
S(a,b,c;z)=M(b,c;z)/(1-az)+M(a,c;z)/(1-bz)+M(a,b;z)/(1-cz)-V(a,b,c;z).
\]
At omega, the three interpolation weights c_r(omega) for r=219,220,221 are each 1/3 (the r residues cover 0,1,2). Hence the exact overlap generating function is
\[
H_h(z)=\frac{z}{3(1-z)(1-z^3)}\sum_{c\in\{1,\omega,\omega^2\}}S(\omega,\omega^2,c;z).
\]
Reducing with omega^2+omega+1=0 gives the first boxed expression. In the same notation,
\[
H_0(z)=z/(1-z^3)^2,
\]
\[
H_1(z)=z/[(1-z^3)^2(1-z)(1-\omega z)],
\quad H_2(z)=z/[(1-z^3)^2(1-z)(1-\omega^2 z)],
\]
\[
H_{01}(z)=-H_0(z)\sum_{p=214}^{218}p z\omega^p/(1-z\omega^p).
\]
Substitute into Q(z)=H01(z)+219(1-omega)H1(z)+219(2+omega)H2(z)-657Hh(z) and simplify over Q(sqrt(-3)), obtaining exactly the second boxed identity.

Writing t=z^3, its two previously unresolved residue classes have generating functions:
\[
\sum_{k\ge0}Q_{3k+2}t^k=\frac{(216+I)+(873+I)t}{(1-t)^3(1+t)},
\quad \sum_{k\ge0}Q_{3k+3}t^k=\frac{216-I}{(1-t)^3}.
\]
The first denominator has a **genuine** t=-1 pole since the numerator there equals -657, not zero; hence its threshold k quasipolynomial requires mod2 and the associated m class needs m mod6. Coefficients of 1/[(1-t)^3(1+t)] are b_k=floor((k+2)^2/4), proving the closed form.

## Evidence and frontier

Exact symbolic elimination of BOTH rational identities in Q(sqrt(-3))(z) returned zero; 12 coefficients in each subsequence were also checked, as well as the independent earlier m=2/3 exhaustive local evidence. VERIFY_ALL_M_SYMBOLIC.py and RESULT_ALL_M.json preserve reproducibility. Local check PASS. These are author-supplied exact proofs with no independent mathematical Review.

This is not a complete N-asymptotic for all roots or a physical BRC claim. Next: fifth-root entry order and joint cost/threshold observer at lower precision.
