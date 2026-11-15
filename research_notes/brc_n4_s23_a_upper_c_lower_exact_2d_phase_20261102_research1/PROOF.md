# Exact two-control endpoint phase diagram: BRC N4/S23

Date: 2026-11-02. Scientific input freeze: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Immediate predecessor: enterprise-math@cb8a37eb0ca3f478a5e4da21b197c0501f5db660. Status: AUTHOR_ANALYTIC_PROOF / EXACT_QUADRATIC_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Precise statistical model and question

Retain the SIX distinct positive source labels AU0, AU1, AV, BU0, BU1, BV and four-stop law

F(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c)).

The exact rows of the original integer 20M mixing matrix are

    (10,10, 0, 0, 0, 0)
    ( 9,11, 0, 0, 0, 0)
    ( 0, 0,20, 0, 0, 0)
    ( 0, 0, 0,10,10, 0)
    ( 0, 0, 0, 2,18, 0)
    ( 0, 0, 0, 0, 0,20).

Freeze a_B=1/4, b_AV=0, b_BV=1/3, and c_AU0=c_AU1=c_BU0=c_BU1=c_BV=1/2. The same b_U must control the A and B U-sources. Only (a,b,c)=(a_A,b_U,c_AV) vary over

Q(h,t)=[1/2,7/8+h] × [1/8,1/2] × [1/2-t,7/8],  0≤h,t≤1/8.

For each legal strategy let P(a,b,c) be the full six-row four-stop preparation observation. Define D(P,Q)=max_i TV(P_i,Q_i) and TV(p,q)=Σ_j|p_j-q_j|/2. The lawful Chebyshev radius R_L restricts the common center to P(Q); the hull radius R_H permits one center from the JOINT convex hull of complete six-row P(Q), never six separately selected centers.

Under exactly the above freezes AU0=AU1, BU0=BU1 and each U-row has equal third/fourth atoms. Grouping that pair is TV-exact for this observer, yielding three-atom effective rows

AU=(a,(1-a)b,(1-a)(1-b)); AV=(a,(1-a)c,(1-a)(1-c));
BU=(1/4,3b/4,3(1-b)/4); BV=constant.

For probability triples TV is exactly the largest absolute singleton-coordinate discrepancy. The checker separately retains all six source labels and four stopping atoms.

## Theorem (ALL REAL h,t, entire closed parameter square)

Set p=1/8-h, d=1/2-p=3/8+h and

L(h)=d/2=3/16+h/2,
H(h,t)=3/16+h/3+t/6,
q(h)=[sqrt(43-16h+16h²)-5+4h]/8.

Then the exact radii are

R_H(h,t)=max{L(h),H(h,t)},
R_L(h,t)=max{L(h),H(h,t),q(h)}.

Thus the gap is max{q(h)-max(L,H),0}. It is STRICTLY POSITIVE if and only if

0≤h<h_*=(4-sqrt(13))/8  AND
0≤t<t_c(h)=[6sqrt(43-16h+16h²)+8h-39]/8.

At t=t_c(h), or for all h≥h_*, the gap is zero. The curve satisfies t_c(0)=(6sqrt(43)-39)/8 and t_c(h_*)=h_*; it remains inside [0,1/8] on this domain. The corner h=t=1/8 has R_H=R_L=1/4. Both previously proved one-coordinate rays are recovered as restrictions, whereas this is the full simultaneous two-coordinate phase diagram.

## Lower bounds (valid for every real strategy)

Let U=1-p. The AV first atom takes values [1/2,U]. Any Chebyshev center of radius r requires r≥(U-1/2)/2=d/2=L.

On the SAME AV row, the three separate attainable coordinate maxima are U, 7/16, 1/4+t/2. If its center triple is (v1,v2,v3), then each vi≥max_i-r, and their sum equals 1. Consequently

3r≥U+7/16+(1/4+t/2)-1=9/16+h+t/2,

or r≥H. This holds for arbitrary joint hull centers, not just lawful ones.

For lawful center controls (x,y,z), three genuine witness events yield

r≥U-x,
r≥7/16-(1-x)(1-y),
r≥(3/4)(1/2-y).

The first and third give 1-x≤p+r and 1-y≤1/2+4r/3, so

(p+r)(1/2+4r/3)≥7/16-r,

equivalently 32r²+(40-32h)r-9-12h≥0.
The polynomial increases strictly for r≥0, has negative value at zero and unique positive root q(h). Therefore R_L≥max(L,H,q), R_H≥max(L,H).

## Common AV center construction (valid for each radius below)

For r in [3/16,1/4], define s=p+r, x=U-r and

z=z(r)=(7/16-r)/s.

Both proposed radii belong to [3/16,1/4]: L,H≤1/4 on the full square and q<1/4 because its defining quadratic at r=1/4 equals 3-20h>0. The AV control z is legal: z≥1/2 is implied by r≤7/24-p/3 (whose right side ≥1/4), while z≤7/8 follows from r≥L≥7/30-7p/15, using L-(7/30-7p/15)=1/60-p/30>0. Thus z∈[1/2,7/8]⊂[1/2-t,7/8].

The resulting AV three-atom center is

AV_c=(U-r,7/16-r,p+2r-7/16).

All AV observation coordinates attain precisely these endpoint intervals:
first [1/2,U], second [p(1/2-t),7/16], third [p/8,1/4+t/2].
The first-coordinate errors are at most r since r≥L. The second upper discrepancy is exactly r, and the opposite discrepancy is ≤r because

2H-(7/16-p(1/2-t))=h/6+5t/24+ht≥0.

The third upper discrepancy is 3H-2r≤r, and the opposite discrepancy is ≤r because r≤1/4≤7/16-7p/8. Hence the single AV row is controlled uniformly across every real parameter of Q(h,t).

## Explicit JOINT convex hull center attaining max(L,H)

Let r=max(L,H), s=p+r, alpha=r/d and beta=1/3, and choose

w2=(1-4p-2r)/(6d),
w1=alpha-w2,
w4=beta-w2,
w3=1-alpha-beta+w2.

The weights sum to one. Since r≥d/2 and r≤1/4≤2d/3, we have 1/2≤alpha≤2/3. Since 0≤p≤1/8 and 3/16≤r≤1/4, we have 0≤w2≤1/3. Consequently all four weights are nonnegative: w1≥alpha-1/3≥0, w4≥0, w3≥1-alpha-1/3≥0.

Apply these SAME weights to four WHOLE lawful strategies, using the common legal z=z(r):

C_H=w1 P(1/2,1/8,z)+w2 P(1/2,1/2,z)
   +w3 P(U,1/8,z)+w4 P(U,1/2,z).

Exact multiplication gives the joint reduced row centers

AU=(U-r, 1/16, p+r-1/16),
AV=(U-r, 7/16-r, p+2r-7/16),
BU=(1/4,3/16,9/16),
BV=fixed.

For AU, the complete real parameter coordinate intervals are
a∈[1/2,U], (1-a)b∈[p/8,1/4], (1-a)(1-b)∈[p/2,7/16].
The first discrepancy is ≤r because r≥L; second-coordinate errors are 3/16 and 1/16-p/8, both ≤r. Tail errors are d-r≤r (since r≥d/2) and p/2+r-1/16≤r (since p≤1/8). AV was handled above. BU worst error is 3/16≤r because its center has average b=1/4; BV is constant. Therefore this one genuine joint convex combination attains radius ≤r across ALL real Q, giving R_H=max(L,H).

## Explicit LAWFUL causal center attaining max(L,H,q)

Take r=max(L,H,q) and choose the SINGLE tuple

x=U-r,
y=1/2-4r/3,
z=(7/16-r)/(p+r).

The bounds above give legal x and z; because r∈[3/16,1/4], y∈[1/6,1/4]⊂[1/8,1/2]. BU has second center 3/8-r, so its endpoint errors are r and 9/32-r≤r. AV is already controlled.

The AU second coordinate is sy=s(1/2-4r/3). The quantity
g(r)=sy+r-1/4 has derivative
g'(r)=3/2-4p/3-8r/3≥2/3>0.
At r=L its value is (8h+1)(8h+3)/192>0. Thus the error relative to maximal observed value 1/4 is ≤r. The opposite second error sy-p/8≤r because sy≤s/2≤r, using p≤1/8<r.

The AU tail coordinate is s(1-y)=s(1/2+4r/3). Its full observed range is [p/2,7/16]. The upper error is ≤r precisely because r≥q satisfies the quadratic lower-witness constraint; the lower error is
r/2+4r(p+r)/3≤r
since p+r≤1/8+1/4=3/8. AU first coordinate is controlled since r≥L. All six original prepared rows therefore have worst-case TV≤r on ALL real Q, so R_L=max(L,H,q).

## Exact phase proof, numerical meaning and limits

Substituting r=L into the quadratic gives -(64h²-64h+3)/8. Its relevant root is h_*=(4-sqrt(13))/8. Thus q>L precisely for h<h_*; in that range q>H precisely when t<6(q-3/16-h/3)=t_c(h). This proves the phase classification including boundary equalities. A discriminating rational pair is h=1/25 with t=47/1000 (strict gap) versus t=49/1000 (zero gap); both are covered by the exact checker.

VERIFY.py was actually run with Python standard-library Fraction arithmetic in Q(sqrt(43-16h+16h²)), exact surd comparisons through rational squares, and the ORIGINAL six mixed four-atom source laws. It checked 294 rational parameter boxes, 8 legal vertices, 6 source rows and 2 common centers per box (28,224 exact TV comparisons), polynomial identities, convex weights, source normalization and sharpness witnesses. RUN_EVIDENCE.json is its actual stdout. **The full real-continuum result follows from the analytic proof above**, not from finite grid extrapolation.

This is a finite-statistical observer result under the pinned positive-source BRC S23 construction. It does not change P000 native six-axis Cell, native geometry/time or future-operation fidelity; a separate faithful native bridge remains open. No independent mathematical review, canonical theorem admission, native CLAIM or Result was performed. The full eleven-control ten-label minimax interval remains [1/2,2/3] for k=4,6.
