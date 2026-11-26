# PREFIX-1105 -- Effective integer-edge band via a complex analytic majorant and exact Beta moments

2026-11-26. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / FINITE_EXACT_RATIONAL_AUXILIARY_CERTIFICATE / NOT_REVIEWED. Continuation of R6 own activity RA-0ABD84561C86E53067DB0322, EM-DIRECT-780BBE / TASK_RESEARCH. Original registration r6-20261123-2358-session-start-own-v1 independently read SUCCEEDED. LEASED query r6-20261126-1553-owner-read-v1 SUCCEEDED/error=null; tasks=[] as_of 2026-11-26T07:54:20.405349Z, Source 4b3d656422062c2fc8e29910da57e8ffdff13195. Independent research only; no new claim, run, Result or review.

Frozen input: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json and joint/time companions. Stage46 X6 chart O, incoming -e1, reversal signed -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Retain full six-axis Cell equality, ordered path multiplicity, signed phase and ports in the original BRC carrier. The following bounds concern ONLY the inherited exact radial test identity D_m(k)=L[x^m(1-x)^k], not a new native state update, physical reference computation or residual attribution.

Immutable parents:
- 08f0330096daa21d866aef04ea1db0c6d4f24384:research_notes/portable_direct/2026-11-26_r6_prefix1095_certified_lower_edge.md
- dc4fcdd14e85a886f07b6484ee67acd260e5081a:research_notes/portable_direct/2026-11-26_r6_prefix1095_frobenius_certificate.py
- 0919218e87c1f6a094123bb19ff315c17846b778:research_notes/portable_direct/2026-11-26_r6_prefix1096_second_order_last_negative_edge.md
- 53d572769fe8745d7c60d93b92b28b182dabfa00:research_notes/portable_direct/2026-11-26_r6_prefix1097_effective_monotone_last_negative.md
- 60f5d76fb61beaefbd9c479a0e96c9429c379513:research_notes/portable_direct/2026-11-26_r6_prefix1100_centered_beta_dual.md
- f0476c7795f31809302dae513504a06d1e9a9e4c:research_notes/portable_direct/2026-11-26_r6_prefix1101_adaptive_precision.md
- 4b000fd990a72817573fa4bb2c0a09c2dc8ded70:research_notes/portable_direct/2026-11-26_r6_prefix1102_sparse_integer_edge.md
- acd24d8499f11d2b8faa6cd0fd8567735f295333:research_notes/portable_direct/2026-11-26_r6_prefix1104_compressed_exception_sieve.md

## 1. Effective result

Let b be the certified first simple root, rho=1/b-1, c,d the exact PREFIX-1096 shifts. Use the parent bounds .044<b<.045, 99<c<100, 9<d<10, r2<166, r3<16425 (both positive), g'(b)<0. Put f(m)=rho*m+c+d/m and B=Beta(m+1,k+1). For all integer m>=10^12 and real k=f(m)+e, |e|<=2, the new bound is
  | D_m(k)/(g'(b)*B) + b^2*e/m | <= 1000*|e|/m^2 + 10^26/m^3.       (1)
In particular for m>=10^16 and C=10^30, any such k with |e|>=C/m^2 has strict sign sign(D_m(k))=sign(e); its normalized magnitude |D_m(k)/(g'(b)*B)|>2/m^3. This gives an explicit, deliberately coarse integer boundary, not just a big-O assertion. No finite real-root uniqueness threshold is needed for the integer consequence.

Given a rational enclosure [l,u] of f(m) of width <=1/8, let L=floor(l-C/m^2) and U=ceil(u+C/m^2)-1. The endpoints L and U+1 have strict negative and positive signs by (1) (|e|<2), and are in the parent 1097 monotonic cone. Thus K_last(m) is in [L,U], with U-L<=1. When there are two candidates, one sign evaluation at U suffices, including the exact-zero case. For the inherited fast oracle H=D/(K*B), K=36/(4*36^8*16^3*4^3), any undecided interval of radius <=S^-3, S=m+k+2, implies |D/(g'B)|<=2/m^3 (K/|g'|<1). By (1) the queried integer j then obeys |j-f(m)|<C/m^2. Consequently PREFIX-1104 can use A=C+1 and M>=10^31, provided the required rational coefficient precision is supplied. The mathematical band and integer localization have explicit activation scales; actual end-to-end adaptive anchor construction and its finite precision-supply runtime still need implementation. These coarse constants are not optimal and do not yet give a useful low-scale filter.

## 2. Reconstruct and bound the inherited analytic density

From 1095, put R=36x and K0=36/(4*36^8). The exact local density is
 g(x)=K0 R^3 N(R) dot Z9(R) / [(R-16)^3(R-4)^3].
Here N is the nine-entry polynomial row obtained by exact elimination of the same 66 signed Laurent terms; Z9 consists of the four extended Frobenius modes plus two homogeneous mixed modes, with the inherited six anchor intervals. On the complex disk |x-b|<=1/200, R has modulus <=9/5 and stays in a simply connected neighborhood avoiding 0. The inherited R^lambda series are analytic there with the branch positive on the real axis. No new propagation is introduced.

I actually reran the parent's elimination and rational recurrence through n=200 (local reconstruction of the prefix of the pinned Python source, not the full anchor/root program). All 66 terms, rank 28 and the matrix SHA256 333adb48c52ac3c5530e8d0509a7b45b77db62a99e65557cafbd70ce38bba312 matched. The newly computed weighted row norm sum over entries and powers is
  sum |N_jk| (9/5)^k = 9233110834194237010896/9765625 < 10^15.
The plain sum of absolute coefficients is 638713023553008.
For each Frobenius mode use the parent geometric coefficient bound 64*T_lambda*2^-n for n>=201, and |R^lambda|<=4. The exact ceiling of the nine-vector infinity-norm majorant at |R|<=9/5 is respectively 5,5,5,6 for lambda=0,1/2,1,2. The actual anchors have absolute values <1; the two homogeneous modes have norm <=2. Hence ||Z9||_infty<=32, uniformly in this disk. As |R|<=2, |R-16|>=14 and |R-4|>=2,
 |g| <= K0*32*10^15/2744.
At the simple root the derivative of the prefactor drops out; 1095 gives F'(t)<-8*10^9, t=sqrt(36x), dt/dx>=180/13, R>1. Thus
 |g'(b)|>= K0*8*10^9*(180/13)/(16^3*4^3)
            =9765625/7244331614208 > 10^-6.
Their ratio is <=85196800000/3087 < 10^8. It follows that G(x)=g(x)/g'(b) is analytic on the disk and bounded by 10^8 there. Its coefficients a_j in powers of Y=x-b satisfy a0=0,a1=1,a_j=g^(j)(b)/(j!*g'(b)), |a_j|<=10^8*200^j by Cauchy. For |Y|<=1/1000, the degree-five polynomial P5 has remainder
 |G-P5| <= (5/4)*10^8*200^6*|Y|^6.
This is an analytic proof using the already paired BRC observer, not a new classical reference or a Taylor replacement of native evolution.

## 3. Explicit complement payment

Take a C^3 cutoff chi equal to 1 on |x-b|<=1/2000 and 0 on |x-b|>=1/1000, using the polynomial transition of 1097 on each side. Derivative bounds R_i*2000^i with R=(1,7,42,420). L(chi*x^m*(1-x)^k) is the integral with ordinary density g by the inherited observer identity. The complement is controlled by the original weighted C^3 norm with coefficients C_j=(114025897/629856,118208/2187,1637/324,4/27).
 J=sum_j C_j sum_i<=j binom(j,i) R_i 2000^i
  =314110550142289441/629856 <2*10^15.
Write W=x^m*(1-x)^k, W3=x^(m-3)*(1-x)^(k-3). For m>=10^12, |e|<=2, the modes p=m/(m+k), p3=(m-3)/(m+k-6) both satisfy |p-b|,|p3-b|<=8/m (use k=f(m)+e, the stated b,c,d bounds). Both are in [.04,.05]. On the complement |x-b|>=1/2000, distance to either mode is >=1/4000. The second derivative of log W or log W3 is <=-m/2 throughout (0,1). Taylor's theorem gives sup complement W3 <= max W3 * exp(-m/64000000), and similarly for W. At p3, W3/W<=25^3*2^3=125000. Hence max W3 <=125000 max W. To lower bound B, integrate over [p,p+1/m], in [.04,.05]; there |(log W)''|<=700m since k<=22m. Thus B>=max W/(2m). This also follows from exp(-350/m)>=1/2. In the complement derivatives up to three of W are bounded termwise by falling coefficients times W3; all weighted factors x^(3+j)<=1. The product rule and the preceding J give
 |L((1-chi)W)/(g'(b)B)| <= J*(24m)^3*125000*2m*10^6*exp(-m/64000000).
The omitted polynomial integral |E[(1-chi)P5]| <= 6*10^8*200^5 *2m*exp(-m/64000000). Both together are bounded by 10^32*m^4*exp(-m/64000000) <= m^-3 for m>=10^12: use exp(t)>=t^40/40!, and the exact inequality 10^32*(64000000)^40*40! < (10^12)^33. This is a whole-complement bound, including endpoints, not a finite sample.

## 4. Exact moment coefficient remainder and signs

For X with positive Beta weight W/B, z=1/m, c_e=c+e, the inherited raw moment identity is
 E[X^j]=prod_(i=0)^(j-1) b*(1+(1+i)z)/(1+b*(c_e+2+i)z+b*d*z^2).
For j<=6 on complex |z|<=1/16, the denominator modulus is >=1-(45/1000)*109/16-(45/1000)*10/256. Twice this lower bound exceeds 11/8, the numerator factor before b. Thus every ratio has modulus <=2b. The binomial expansion then bounds the analytic centered moment M_n(z)=E[(X-b)^n] by (3b)^n<=1 on this disk for n<=6. By Cauchy, truncating its z-series at degree 2 costs <=8192/m^3 for m>=32. This estimate applies to the exact rational moment identity, keeping signed odd moments.

Use PREFIX-1096's exact first two moment coefficients with c replaced by c_e. For n=5,6 both coefficients vanish (also constant zero), so |E[Y^5]|, E[Y^6]<=8192/m^3. Substitution in E[P5] yields
 E[P5] = -b^2*e/m + B2(e)/m^2 + remainder.
Let A_e=1-b*(c_e+2), v=b(1-b), L0=1-2b. The second coefficient B2(e) is b^2 times
 -[d+(c_e+2)A_e] + r2/2*[A_e L0-(c_e+3)v+A_e^2]
 +r3*v/6*(2L0+3A_e)+r4*v^2/8.
Parent c,d imply B2(0)=0. Differentiating this polynomial in e (A_e'=-b) and using |A_e|<=6, |c_e+2|<=104, |v|,|L0|<=1, r2<166, r3<16425 gives |B2'(e)|<1000 on [-2,2]. Consequently |B2(e)|<=1000|e|. All moment truncation errors paid together are <=8192*6*10^8*200^5/m^3. The local Taylor error, using the nonnegative sixth moment, is <=8192*(5/4)*10^8*200^6/m^3. Adding the complement bound, the exact sum of constants is <10^26. This proves (1). Since 1000/m<=b^2/2 at m>=10^12, for |e|>=10^30/m^2 the leading signed term dominates by more than 2/m^3. Multiplication by the negative g'(b) gives the claimed sign. The integer conclusions in section 1 follow from 1097; no need to differentiate another approximate observer.

## 5. Actual computation and reproducibility

The local exact SymPy/Fraction reconstruction reused the source of 1095 through the end of the 'basis' loop (stopped BEFORE the new anchor/moment code). It recomputed the same rank-28 elimination, 66 Laurent terms and four 201-term rational basis arrays, not any classical propagation or full CT table. To reproduce the NEW norms insert the following after that loop in the pinned 1095 script, and stop before '# Exact moments via grouped Euler occupancy recurrence'. Names below are the actual parent variables.

    print(sum(abs(c)*sy.Rational(9,5)**k for v in nums for k,c in enumerate(v)))
    print(sum(abs(c) for v in nums for c in v))
    for a,z,h,err,T in basis:
        bound=4*(sum(max(abs(x) for x in z[n]+[h[0][n],h[1][n]])*F(9,5)**n for n in range(201))+640*T*F(9,10)**201)
        print(a,-(-bound.numerator//bound.denominator))

Executed local output: 9233110834194237010896/9765625; 638713023553008; (0,5),(1/2,5),(1,5),(2,6). This prefix was executed in an equivalent local transcription of the frozen source, with the original matrix hash and signed readout assertions, not by running the remote full script.

The following independent exact numerical bounds script was actually executed successfully (nine assertions):
    from fractions import Fraction as F
    from math import comb,factorial
    b0,b1=F(44,1000),F(45,1000)
    p=F(36,4*36**8)
    l=p*8*10**9*F(180,13)/(16**3*4**3)
    u=p*32*10**15/2744
    assert l>F(1,10**6) and u/l<10**8
    assert F(11,8)<2*(1-b1*109/16-b1*10/256)
    C=[F(114025897,629856),F(118208,2187),F(1637,324),F(4,27)]
    R=[1,7,42,420]
    J=sum(C[j]*sum(comb(j,i)*R[i]*2000**i for i in range(j+1)) for j in range(4))
    assert J<2*10**15
    assert 2*10**15*24**3*125000*2*10**6+2*6*10**8*200**5 <10**32
    assert 10**32*64000000**40*factorial(40) < (10**12)**33
    assert 8192*(6*10**8*200**5+F(5,4)*10**8*200**6)+1 <10**26
    assert F(1000,10**12)<b0*b0/2
    assert b0*b0*10**30/2-10**26>2
    assert F(10**30,10**32)<F(1,8)

Output: all nine checks pass; J=314110550142289441/629856; derivative lower=9765625/7244331614208; ratio=85196800000/3087. No floating point decision, no new physical reference. No end-to-end true-window sieve or adaptive oracle execution; coefficient centers and 18 certified rows were not repeated. Proof remains conditional on inherited BRC correspondence and parent certificates, and unreviewed.

## 6. Next

Improve the very loose constant by bounding the actual local signed derivative jets rather than the full row-norm disk majorant, and obtain moment remainder bounds retaining their small b-powers; establish a much smaller effective C and M, then run the actual compressed sieve with appropriately refined anchors. The finite precision supply of 1101 has its own effective-constant work. Other spectral zeros, exact c2=0, arbitrary integer zero/separation, and B_fix,odd(32) remain open. No shared task status change or formal acceptance.
