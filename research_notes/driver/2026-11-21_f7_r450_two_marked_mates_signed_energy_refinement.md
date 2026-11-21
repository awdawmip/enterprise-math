# CBRC F7 Driver r450 — Two marked mates and signed primitive-energy refinement

Date: 2026-11-21 (+08:00). This is a new scoped mathematical corollary by the continuing Driver line EM-DVR-DEBB5E, building on r448/r449. The original F7 problem and frozen Result remain attributable to researcher EM-CBRCF7-83A1D4 and RR-AA38973D56330E59D315. This note does not constitute native independent Review, Result admission, Task completion, or parent closure.

## Exact scalar setting

Use the original rank-one involution A=I+uv^T with u=(1,1,-1,-1), v=(1,-2,-1,2). For z=(a,b,c,d), let t=a-2b-c+2d, so Az=(a+t,b+t,c-t,d-t).

The original admissible q:Z^2->[0,infinity) obeys q(0,0)=0, q(-x,y)=q(x,y), q(s,0)=1 for nonzero s, q(x,y)>=1/2 on nonzero arguments, and the *fixed-scale* marks q(2,1)=q(-1,-1)=1/2. No homogeneity, regularity, upper cap, or new axiom is assumed. Let E(q)=sup_z |q((Az)_1,(Az)_2)+q((Az)_3,(Az)_4)-q(a,b)-q(c,d)|.

## Theorem A — exact opposite-sign marked mates

If E(q)<=epsilon, then

    3/2-epsilon <= q(4,1) <= 3/2+epsilon,
    3/2-epsilon <= q(5,-1) <= 3/2+epsilon.       (R450.1)

In particular, whenever epsilon<1, *both* marked mates lie strictly above the nonaxis floor 1/2, one in each signed-y half-plane. Consequently a scalar that equals 1/2 on all nonaxis points in either one of the two open y-half-planes must have E(q)>=1. A hypothetical half-defect scalar must satisfy q(4,1)>=1 and q(5,-1)>=1, regardless of any scale dependence.

**Proof.** For the two exact old-axis inputs, direct integer multiplication gives

    A(2,0,3,0)=(1,-1,4,1),
    A(-3,0,-4,0)=(-2,1,-5,-1).

Each input has two nonzero old-axis slots, contributing total scalar value 2. Each transformed output contains one fixed marked scalar value 1/2, by the original J-evenness in the second identity. Thus the two exact defects are

    D_q(2,0,3,0)=q(4,1)-3/2,
    D_q(-3,0,-4,0)=q(5,-1)-3/2.

Bounding their absolute values proves (R450.1). If either signed half-plane is identically at the floor, one of these equations has defect -1. QED.

The q(4,1) half of (R450.1) is already implicit in r449's (c,t)=(2,1) marked pair. The q(5,-1) counterpart and the combined signed-sector exclusion are the additional observations.

## Theorem B — sharpened finite primitive convex energy

Retain exactly r449's finite primitive set

    Omega_L={(x,y) in Z^2: x>0, y!=0, gcd(x,|y|)=1,
              x<=3L-2, |y|<=L-1},

and N(L)=sum_{c=2}^L phi(c). Let 0<=epsilon<1 and assume E(q)<=epsilon. Put a=1-epsilon and delta(x,y)=q(x,y)-1/2>=0 for nonzero (x,y). For every convex nondecreasing Psi:[0,infinity)->[0,infinity) with Psi(0)=0,

    sum_{Omega_L} Psi(delta) >=
       Psi(a)                                      (L=2);
       2 Psi(a)+2(N(L)-1) Psi(a/2)                 (3<=L<=5);
       2 Psi(a)+2(N(L)-2) Psi(a/2)                 (L>=6).       (R450.2)

For Psi(t)=t^2 this reads

    sum_{Omega_L} delta^2 >= a^2 *
       1                                           (L=2);
       (N(L)+3)/2                                  (3<=L<=5);
       (N(L)+2)/2                                  (L>=6).       (R450.3)

At epsilon=1/2 and L>=6, the new square-energy lower bound is (N(L)+2)/8 versus r449's (N(L)+1)/8. The asymptotic L^2 coefficient is unchanged, and no new estimate for the unrestricted infinite-domain minimax is asserted.

**Proof.** Reuse r448's disjoint family of N(L) primitive pairs P(c,t)=(c+2t,t), R(c,t)=(c-t,-t), 2<=c<=L, 1<=t<c, gcd(c,t)=1. Their deviations obey delta(P)+delta(R)>=a, hence each ordinary pair contributes at least 2 Psi(a/2) by Jensen and monotonicity.

The pair (2,1) contains P=(4,1), whose deviation is >=a by Theorem A. It therefore contributes at least Psi(a). The second high point (5,-1) belongs to Omega_L exactly when L>=3. It cannot belong to any P-pair (negative second coordinate). In the R-family, R(c,t)=(5,-1) forces (c,t)=(6,1). Therefore for 3<=L<=5 the point (5,-1) is outside all enumerated pairs and supplies one additional Psi(a). For L>=6 it occupies the (6,1) pair, whose energy is at least Psi(a), replacing its former Jensen contribution 2 Psi(a/2). The two distinguished pairs are disjoint. All leftover points have nonnegative energy. Summation proves (R450.2); squaring gives (R450.3). QED.

## Exact validation and scope

Direct integer matrix multiplication was independently checked for the two marked witnesses and A(7,0,6,0)=(8,1,5,-1). Finite primitive pair membership was separately enumerated for 2<=L<=7 and agreed with the symbolic disjoint-pair proof. Those checks supplement, but do not substitute for, the exact argument above.

This strengthens the earlier r449 coercivity bound by isolating a second opposite-sign fixed high direction. It excludes one-sided floor ansatz from any globally subunit-defect search, while preserving original mathematical authorship, frozen scientific assumptions and the open bound 1/2<=E_infinity<=4/7.

Source theorem: r448, fixed commit b4b3141368975f7598a8c98acbf49b435161c4cf; r449, fixed commit e43bf08f8e28db64d1ab0efaac33c01f48d2cd5c. Original Native Review and exact SHA256 manifest mismatches remain separate unresolved control questions (issue #2874).
