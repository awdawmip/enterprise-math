# EC49FTM addendum — conditional discount law and stochastic-order theorem

**2026-11-19 · AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED.** Follows EC49FTM_JOINT_LAW_PROOF.md and the original BRC16943 frozen science at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Parent original-index Bellman optimality is inherited from PR #2774; no native rerun.

## Statement

Let M=max_z(D-S) and Z=z_* under the independently uniform external a,b design described in the main EC49FTM proof. Put

    m0=11457/512; m1=1461/64; m2=1469/64; m3=187/8.
    A(m)=(4m+2647)/3696
    B0(m)=(8m+173)/480
    B1(m)=(64m+1411)/3840
    c=131072/945.

For Lebesgue-almost every m in the interior of the support [m0,m3], Z conditional on M=m is **uniform plus, in the upper segment, one atom**:

    segment          lower L(m)     upper U(m)     atom at Z=3/4
    m0<m<m1          A(m)           B1(m)          0
    m1<m<m2          B0(m)          B1(m)          0
    m2<m<m3          B0(m)          3/4            p(m)

    p(m)=5(64m-1055)/(102437-4288m) for m2<m<m3.

Precisely, the absolutely continuous conditional density is c/f_M(m) on the interval [L(m),U(m)], and zero elsewhere; for m2<m<m3 add p(m) times the Dirac mass at 3/4. Here f_M is the positive marginal density from EC49FTL:

    f_M(m) = 512(512m-11457)/121275                   on (m0,m1)
             512/525                                  on (m1,m2)
             (6555968-274432m)/127575                 on (m2,m3).

For the lower two intervals, c(U-L)=f_M, so the conditional law is ordinary uniform. In the upper interval its continuous mass is 1-p(m).

**Stochastic-order theorem:** choose the conditional versions above at interior points. If m<m' lie in (m0,m3), the conditional law of Z given M=m' first-order stochastically dominates the law given M=m. Equivalently, every conditional quantile of Z can be chosen nondecreasing in m, and the conditional expectation is nondecreasing. In fact the conditional mean is strictly increasing within each of the three open segments, and has an *upward jump* of exactly

    207/114176

at m=m2 (one-sided limits). The clipping probability increases strictly in the upper interval, from its right-hand limit 115/223 at m2 to its left-hand limit 1 at m3.

## Proof

From the affine inverse in the EC49FTM joint-law proof,

    a=(47-m)/945+(44/45)z; b=1/27-m/54+(10/9)z,

both a and b increase with z at fixed m. The source constraints a>=3/4, b>=7/16, b<=57/128, and z<3/4 yield

    z >= max(A(m),B0(m));
    z <= min(B1(m),3/4).

The upper source constraint a<=a_c(b) is equivalent to z<=3/4, and a<=49/64 is automatic in the interior portion because a_c(b)<49/64 throughout B. The four intersections occur exactly at

    A(m0)=B1(m0); A(m1)=B0(m1);
    B1(m2)=3/4;   B0(m3)=3/4.

This proves the three conditional support intervals. By Theorem 1 of the main note, the interior joint density c is constant. Dividing by f_M gives the uniform continuous component; dividing the line density by f_M supplies p(m). Exact simplification verifies f_M=c(U-L)+g, where g is zero below m2 and is 64(64m-1055)/25515 above it.

On each of the first two intervals, both L(m) and U(m) are strictly increasing affine functions, so the conditional uniform laws increase in first-order stochastic order (couple them by one shared Uniform[0,1] variable). At m1 the intervals join continuously. On the third interval L increases, U is fixed at 3/4, and

    p'(m)=10160640/(102437-4288m)^2 >0.

Couple with one common uniform random variable: the quantile of the conditional law equals L+(U-L)t/(1-p) for 0<=t<=1-p and is 3/4 above that threshold. The continuous uniform component on an interval with increasing L and fixed U moves right, and its mixture weight 1-p decreases, shifting additional mass to U; hence quantiles are nondecreasing. At m2 the left and right continuous intervals coincide but right after m2, p=115/223>0, so the law jumps upward in stochastic order. One-sided conditional means at m2 are respectively 1911/2560 and 106797/142720, yielding the displayed jump 207/114176.

This is a fully exact theorem on the parent affine pushforward, for all real conditional m in the stated open ranges. As usual for conditioning on continuously distributed M, values assigned at isolated breakpoints do not alter the regular conditional law.

## Reproducibility and next question

`EC49FTM_CONDITIONAL_LAW_VERIFY.py` checks all segment identities with standard-library Fraction arithmetic, 297 distinct rational m samples and 41x297 rational quantile order checks. The analytic coupling is the universal proof, rather than the finite regression. The machine summary is `EC49FTM_CONDITIONAL_LAW_CERT.json`.

Next: investigate whether analogous first-order stochastic monotonicity survives a typed nonuniform price prior and which exact Bellman phase changes occur below z=11/16. No formal task control, author identity, activity or review state is changed.
