# BRC N=4 / S23: exact phase transition when expanding the upper a_A endpoint

Date: 2026-11-02. Author-side analytic proof, independently unreviewed. Frozen scientific model: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. This extends the exact b_U-lower result at enterprise-math@83c033e51fb28d7776ad27b35f6729ff39fde39e.

## Frozen model and statement

The four-stop positive BRC source law is F(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c)). Retain six distinct sources AU0,AU1,AV,BU0,BU1,BV and source mixing

20M = ((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),(0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20)).

Freeze a_B=1/4, b_AV=0, b_BV=1/3, c_AU0=c_AU1=c_BU0=c_BU1=c_BV=1/2. The remaining controls (a,b,c)=(a_A,b_U,c_AV) obey one shared b_U on A and B branches. Let P(a,b,c) be the complete six-row, four-stop observation and D(P,Q)=max_i TV(P_i,Q_i). The lawful center must come from P(Q_h), whereas the relaxed center may be one joint convex combination of complete six-row P-vectors.

Q_h=[1/2,7/8+h] × [1/8,1/2] × [1/2,7/8], for every real 0<=h<=1/8.

For the declared TV observer, AU=(a,(1-a)b,(1-a)(1-b)), AV=(a,(1-a)c,(1-a)(1-c)), BU=(1/4,3b/4,3(1-b)/4), with the original duplicated AU/BU rows and fixed BV. This three-atom rewriting exactly preserves the original four-stop TV because the AU and BU tail atoms have fixed equal splits and AV has a fixed zero stop. TV between two three-atom probability vectors equals their largest absolute singleton-coordinate discrepancy.

Define
R_L(h)=inf_{z in Q_h} sup_{theta in Q_h} D(P(theta),P(z)),
R_H(h)=inf_{C in conv P(Q_h)} sup_{theta in Q_h} D(P(theta),C).

**Theorem (full continuous parameter domain).** Write
F_h=3/16+h/2,
T_h=(sqrt(43-16h+16h^2)-5+4h)/8,
h_*=(4-sqrt(13))/8.
Then

R_H(h)=F_h;
R_L(h)=max{F_h,T_h};
R_L(h)-R_H(h)=max{0,(sqrt(43-16h+16h^2)-13/2)/8}.

The gap is positive exactly for 0<=h<h_* and is zero for h_*<=h<=1/8. The phase point is approximately 0.04930609056700136; at h=1/8 both radii equal 1/4.

## Universal lower bounds

Put q=1/8-h and u=1-q, so 0<=q<=1/8. The first-stop AU event ranges over [1/2,u] and forces any center to have radius at least (u-1/2)/2 = 1/4-q/2 = F_h.

For a lawful center z=(x,y,t) with risk r, three actual BRC events give
(1) u-x<=r (AU first atom at a=u),
(2) 7/16-(1-x)(1-y)<=r (AU combined tail at a=1/2,b=1/8),
(3) (3/4)(1/2-y)<=r (BU second atom at b=1/2).

Hence 1-x<=q+r and 1-y<=1/2+4r/3, with nonnegative factors, so
(q+r)(1/2+4r/3)>=7/16-r.
After substituting q=1/8-h this is
32r^2+(40-32h)r-9-12h>=0.
The polynomial is strictly increasing for r>=0 and its positive root is T_h. Thus R_L>=max(F_h,T_h).

## A single joint-hull center attains F_h

Let C_h= (1/2)P(1/2,1/8,7/8)+(1/2)P(u,1/2,1/2). The same mixture weights apply to all six rows. Its effective three-atom rows are

AU=(3/4-q/2, 1/32+q/4, 7/32+q/4),
AV=(3/4-q/2, 7/32+q/4, 1/32+q/4),
BU=(1/4,15/64,33/64), with BV fixed.

The first-atom radius is exactly F_h. Other varying coordinates have endpoint ranges [q/8,1/4] and [q/2,7/16]. The latter interval has midpoint 7/32+q/4 and halfwidth H=7/32-q/4<=F_h. For [q/8,1/4], center 1/32+q/4 also has both endpoint errors <=H for 0<=q<=1/8. BU's second-atom radius is 9/64<=F_h. Therefore sup_{theta in Q_h}D(P(theta),C_h)=F_h, proving R_H=F_h.

## Explicit lawful center attains max(F_h,T_h)

Set r=max(F_h,T_h), s=q+r, x=u-r, y=1/2-4r/3, w=7/32+q/4 and t=w/s. We first show z=(x,y,t) is legal.

For 0<=h<=1/8, 3/16<=r<=1/4: the upper bound for T_h follows from sqrt(43-16h+16h^2)<=7-4h, whose squared difference is 6-40h>=1. Hence x in [1/2,u] and y in [1/6,1/4]. Also s>0,
2w-s >= 3/16-q/2 >0, and
7s-8w >= 7(q+F_h)-8w =3q/2>=0.
Therefore 1/2<=t<=7/8, and z is a lawful causal strategy.

Its varying rows are
AU=(x,sy,s(1-y)),
AV=(x,w,s-w),
BU=(1/4,3/8-r,3/8+r).

We check all continuous-coordinate extrema.

* First atoms: distances to [1/2,u] are r and (u-1/2)-r<=r by r>=F_h.
* AU second atom: its interval is [q/8,1/4]. Since y<=1/4, sy<=s/4<=q/8+r using q<=6r. For the other endpoint, put g(q,r)=(q+r)(1/2-4r/3)+r-1/4. Its derivative in r is 3/2-4q/3-8r/3>=2/3 on our domain. Since r>=F_h=1/4-q/2 and g(q,F_h)=(2q-1)(4q-1)/24>=0 for 0<=q<=1/8, we obtain sy>=1/4-r.
* AU third atom: interval [q/2,7/16]. The inequality 7/16-s(1-y)<=r is exactly the quadratic lower-certificate inequality, valid for r>=T_h. The other endpoint satisfies s(1-y)-q/2<=r because sy-q/2=r(1/2-4s/3)>=0 as s<=3/8.
* AV second atom: w is the midpoint of [q/2,7/16], with error H<=r.
* AV third atom: interval [q/8,1/4], center s-w. The upper endpoint difference is 15/32-3q/4-r<=r since F_h-(15/64-3q/8)=1/64-q/8>=0. The lower endpoint difference is r+5q/8-7/32<=r because q<=1/8.
* BU second atom: interval [3/32,3/8], center 3/8-r, endpoint differences r and 9/32-r<=r. BV is fixed.

For three-atom laws, all these coordinate differences <=r imply row TV<=r. The supremum across all real strategies is <=r. The first-stop endpoint gives equality when r=F_h; the AU tail witness gives equality when r=T_h>F_h. Thus R_L=max(F_h,T_h).

## The exact transition

T_h-F_h=(sqrt(43-16h+16h^2)-13/2)/8. Equality occurs at 16h^2-16h+3/4=0, whose roots are (4±sqrt(13))/8. Only h_*=(4-sqrt(13))/8 lies in [0,1/8]. The quadratic changes from positive to negative there, proving a single exact phase change.

## Verification and limits

VERIFY.py reconstructs all six positive four-stop source rows and the original 20M mixing, then checks both centers against all eight parameter vertices in each of 14 rational boxes and at the irrational transition h* in Q(sqrt(13)). The 15 exact cases entail 1,440 vertex-to-center row-distance comparisons (15×8×6×2). The analytic extrema arguments, not the finite sample, prove the result for every real h and every real control in Q_h. This is a model-local BRC TV theorem; P000 native X6 Cell, independent time, three-dimensional slice and the full eleven-control ten-label problem retain their separate scientific obligations. The existing global ten-label minimax bound remains [1/2,2/3] for k=4,6.
