# BRC N4/S23: exact simultaneous a-upper / shared-b-lower phase diagram

Date: 2026-11-02. Author-side proof, independently unreviewed and not admitted. Frozen scientific input: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. This composes and extends the preceding single-endpoint results at 83c033e51fb28d7776ad27b35f6729ff39fde39e and 449e666f276a88153cc68f33acedc8df635aa25b.

## Source-preserving observer and theorem

Use the four-stop positive BRC law F(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c)). Keep labeled sources AU0, AU1, AV, BU0, BU1, BV and original positive mixing
20M=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),(0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20)).
Freeze a_B=1/4, b_AV=0, b_BV=1/3, and c_AU0=c_AU1=c_BU0=c_BU1=c_BV=1/2. The free controls (a,b,c)=(a_A,b_U,c_AV) share b_U across both A and B sources. P(a,b,c) is the entire six-row four-stop observation; D(P,Q)=max_i TV(P_i,Q_i).

For this specific TV observer the identical AU/BU rows and split tails yield exactly the reduced three-atom rows:
AU=(a,(1-a)b,(1-a)(1-b)), AV=(a,(1-a)c,(1-a)(1-c)), BU=(1/4,3b/4,3(1-b)/4); BV is constant. The six labeled sources and common joint mixing remain preserved. TV of any three-atom laws equals their maximum absolute singleton-coordinate discrepancy.

Let Q(h,k)=[1/2,7/8+h] x [1/8-k,1/2] x [1/2,7/8] for all real h,k in [0,1/8]. R_L is the optimal worst-case D-radius with a legal center P(z), z in Q; R_H allows a single joint convex combination of full six-row P observations as its center. Define:
F_h=3/16+h/2,
H_hk=3/16+(h+k)/4,
T_hk=(sqrt(43-16h+16h^2+24k)-5+4h)/8,
K(h)=(2/3)h-(2/3)h^2-1/32.

THEOREM (continuous, exact): R_H(h,k)=max(F_h,H_hk) and R_L(h,k)=max(F_h,T_hk). Further, T_hk>H_hk throughout the entire square. Thus R_L=R_H exactly when k<=K(h); the zero-gap sector begins at h_*=(4-sqrt(13))/8, k=0. At h=1/8 its boundary is k=1/24. At (h,k)=(1/8,1/8) the strict gap reopens:
R_H=1/4, R_L=(sqrt(177)-9)/16, gap=(sqrt(177)-13)/16>0.

## Exact hull lower and upper certificates

Set q=1/8-h, l=1/8-k, u=1-q. The AU first-coordinate range [1/2,u] requires radius F_h. Its tail coordinate (1-a)(1-b) ranges in [q/2,(1-l)/2] and requires radius H_hk=(1-l-q)/4, for every center.

Use the one common mixture C=(P(1/2,l,7/8)+P(u,1/2,1/2))/2. Its reduced AU row has first atom (1/2+u)/2, second (l+q)/4 and tail (1-l+q)/4. The first atom incurs exactly F and the tail exactly H. AU second atom ranges in [ql,1/4]; its upper error is H, and its lower error is <=H because 2(l+q)-4ql<=1 for 0<=l,q<=1/8. AV second atom is centered at w=7/32+q/4 on [q/2,7/16], radius 7/32-q/4<=F. AV third atom is centered at 1/32+q/4 on [q/8,1/4], with errors <=7/32-q/4. BU second atom has radius 3/16-3l/8<=H; BV is constant. Consequently C has worst risk max(F,H), which achieves the universal lower bound.

## Lawful lower certificate

For every lawful center P(x,y,t) with risk r, use three actual source-sensitive event constraints: AU first atom at a=u, AU tail at (a,b)=(1/2,l), and BU second atom at b=1/2:
u-x<=r,
(1-l)/2-(1-x)(1-y)<=r,
3(1/2-y)/4<=r.
Therefore 1-x<=q+r and 1-y<=1/2+4r/3; multiplying nonnegative factors and inserting the tail witness gives
(q+r)(1/2+4r/3)>=7/16+k/2-r.
Equivalently 32r^2+(40-32h)r-9-12h-12k>=0.
For r>=0 this polynomial is strictly increasing; its unique positive root is T_hk. Also the AU first-atom span requires r>=F. Hence R_L>=max(F,T).

## Construct a legal center achieving the lower bound

Put r=max(F,T), s=q+r, x=u-r, y=1/2-4r/3, w=7/32+q/4, t=w/s. We prove z=(x,y,t) is lawful and its worst error <=r over ALL real Q.

First, T increases with h and k: its defining positive-root polynomial is increasing in r and q, decreases in k, and q=1/8-h. Thus 3/16<=r<9/32 because its maximum T at h=k=1/8 is (sqrt177-9)/16<9/32. Put r0=3/8-q. The defining inequality at r0 has residual
(q+r0)(1/2+4r0/3)-(7/16+k/2-r0)=5/16-3q/2-k/2>=1/16,
so r<=r0 (also F<=r0) and s<=3/8. Therefore x in [1/2,u], y in [l,1/2] and s>0. The inequalities 2w-s=7/16-q/2-r>0 and 7s-8w>=7(q+F)-8w=3q/2>=0 imply 1/2<=t<=7/8.

For fixed z, every relevant observed coordinate is multi-affine in (a,b,c), hence each extreme over Q is at a parameter-box vertex. In fact the following exact coordinate intervals prove the required bounds for every real parameter:

* AU/AV first atom: x has error at most r on [1/2,u] since r>=F.
* AU second: interval [ql,1/4], center sy. From s<=3/8, sy-q/2=r(1/2-4s/3)>=0, so sy>=ql. The lower discrepancy sy-ql<=sy<=s/2<=r (q<=r). For its upper discrepancy define g(q,r)=(q+r)(1/2-4r/3)+r-1/4. It increases in r, as derivative 3/2-4q/3-8r/3>=7/12, and at r=F equals (1-2q)(1-4q)/24>=0. Thus 1/4-sy<=r.
* AU tail: interval [q/2,7/16+k/2], center s(1-y). Upper error <=r is precisely the quadratic root condition r>=T; lower error <=r follows from sy>=q/2.
* AV second: interval [q/2,7/16], center w, radius 7/32-q/4<=F<=r.
* AV third: interval [q/8,1/4], center s-w. Upper discrepancy <=r because 2r>=2F=1/2-q>=15/32-3q/4=1/4+w-q. Lower discrepancy <=r because w>=7q/8.
* BU second: interval [3l/4,3/8], center 3y/4=3/8-r. Its half-width 3/16-3l/8<=H<T<=r, so each endpoint error is <=r. BV is constant.

For three-atom laws the row TV equals the largest singleton discrepancy. All six mixed rows therefore have risk <=r. Combined with the lower bound, R_L=max(F,T).

## Strict gap and phase boundary

Let Delta=43-16h+16h^2+24k. The expression S=13/2-2h+2k is positive, and
Delta-S^2=3/4+10h+12h^2-2k+8hk-4k^2>=7/16>0.
Hence T>H at every h,k in the square. The hull and lawful radii coincide exactly if T<=F, equivalent to sqrt(Delta)<=13/2, i.e.
Delta<=169/4, equivalent to k<=K(h).
K(h)>=0 first at the unique h_*=(4-sqrt(13))/8 in [0,1/8]; K(1/8)=1/24. For h=k=1/8, Delta=177/4, so T=(sqrt177-9)/16>1/4=F=H. All assertions follow.

## Exact computation, source scope and status

VERIFY.js reconstructs original four-stop positive sources and 20M with V8 BigInt rational arithmetic. It checks 83 rational endpoint boxes including h=1/16,k=1/128 and h=1/8,k=1/24, 664 parameter vertices and 7968 full four-stop mixed-row-to-center comparisons. An exact integer sqrt bracket at scale 2^38 supplies a rational legal upper surrogate for irrational T. These finite tests validate the implementation; the analytic inequalities establish the full real continuum theorem.

This is a BRC source-preserving statistical observer theorem. P000 native X6 Cell, three-dimensional slice and independent-time transfer are distinct obligations; no theorem admission or independent Driver review is asserted. The full eleven-control ten-label minimax interval remains [1/2,2/3] for k=4,6.
