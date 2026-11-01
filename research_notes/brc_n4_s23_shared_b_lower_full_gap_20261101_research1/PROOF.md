# Exact persistent lawful-vs-joint-hull gap under the full legal shared-b lower-endpoint expansion

Date 2026-11-01. Author-side analytic proof; unreviewed and not admitted to native Enterprise Math theorem authority.

## Scientific model and frozen sources

Continue the six-source BRC N4/S23 model from immutable 43ec6098b1330ae86d0a7863be336c5d97f6ef34 and the a-lower endpoint theorem eefe29110ece7bae426457655a4db6028626ddbd. The four-stop law is
\[
F(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c)).
\]
Six source labels, in order, are AU0, AU1, AV, BU0, BU1, BV. Keep the original positive mixing matrix
\[
20M=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
(0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20)).
\]
Freeze a_B=1/4, b_AV=0, b_BV=1/3, and c_AU0=c_AU1=c_BU0=c_BU1=c_BV=1/2. The free controls (a,b,c)=(a_A,b_U,c_AV) share b_U across both A and B sources. The observation P(a,b,c) comprises all six mixed four-stop laws. Its metric is D(P,P')=max_i TV(P_i,P'_i), with TV(p,q)=sum_t |p_t-q_t|/2.

For this frozen *four-stop-TV observer*, the A-U, A-V, B-U rows reduce exactly to the three-atom presentations
\[
AU=(a,(1-a)b,(1-a)(1-b)),\quad
AV=(a,(1-a)c,(1-a)(1-c)),\quad
BU=(1/4,3b/4,3(1-b)/4),
\]
and BV is constant. AU and BU have equally split last two atoms, and AV has an identically zero second stop; these explain the equality of the displayed and original TV. The source labels, mixing relation, and legal shared b remain unchanged. This compression is scoped to this observer, not future operations or P000 native space.

Let
\[
Q_h=[1/2,7/8]\times[1/8-h,1/2]\times[1/2,7/8],\quad 0\le h\le1/8.
\]
Define R_L(h)=inf_{z in Q_h}sup_{theta in Q_h}D(P(theta),P(z)); define R_H(h) by allowing the center in the *joint* convex hull conv{P(theta):theta in Q_h} (one shared mixture for all six rows).

## Theorem, all real h and continuous controls

For every real h in [0,1/8],
\[
\boxed{R_H(h)=3/16+h/4,\qquad R_L(h)=(\sqrt{43+24h}-5)/8.}
\]
Their gap is strictly positive and decreasing on this whole interval. In particular the full legal expansion to b_U=0 satisfies
\[
\boxed{R_L(h)-R_H(h)\ge(4\sqrt{46}-27)/32>0.}
\]

## Lower bounds

For any center, the AU tail event ranges over [1/16,7/16+h/2], forcing risk at least its half-width H(h)=3/16+h/4.

For a lawful center z=(x,y,t) of risk r, three legal witnesses yield
\[
7/8-x\le r,\quad 7/16+h/2-(1-x)(1-y)\le r,\quad 3(1/2-y)/4\le r.
\]
The first and third imply 1-x<=1/8+r and 1-y<=1/2+4r/3, with nonnegative factors. The second therefore gives
\[
(1/8+r)(1/2+4r/3)\ge7/16+h/2-r
\Longleftrightarrow 32r^2+40r-9-12h\ge0.
\]
This polynomial increases for r>=0, so r>=T(h)=(sqrt(43+24h)-5)/8. On h∈[0,1/8], T(h)>H(h), since squaring positive sides reduces the inequality to 3/4-2h-4h^2>0 (at h=1/8 it is 7/16).

## Explicit joint-hull upper witness

Use a single mixture of complete joint observations:
\[
C_h=\tfrac12 P(1/2,1/8-h,7/8)+\tfrac12 P(7/8,1/2,1/2).
\]
Its effective rows are
\[
AU=(11/16,1/16-h/4,1/4+h/4),\quad
AV=(11/16,1/4,1/16),\quad
BU=(1/4,15/64-3h/8,33/64+3h/8).
\]
For three-atom probability laws TV is the largest absolute singleton difference. AU first atom differs by <=3/16. Its second atom ranges in [1/64-h/8,1/4], with maximum center deviation H. Its third atom ranges in [1/16,7/16+h/2], with exact center deviation H. AV's second and third atoms range in [1/16,7/16] and [1/64,1/4], respectively; their maximum deviations are 3/16, and the first atom is as in AU. BU's second-atom interval is [3/32-3h/4,3/8], centered at 15/64-3h/8, with radius 9/64+3h/8. This is <=H because H-(9/64+3h/8)=3/64-h/8>0. BV is fixed. Therefore sup_{theta∈Q_h}D(P(theta),C_h)=H, proving R_H=H.

## Explicit lawful upper witness

Put r=T(h), s=1/8+r, and choose
\[
x=7/8-r,\quad y=1/2-4r/3,\quad t=(1/4)/s.
\]
We have 3/16<r<1/4; hence x∈[1/2,7/8], y>1/6>1/8-h, and 2/3<t<4/5, so this is a lawful z∈Q_h. The centered rows become
\[
AU=(x,sy,s(1-y)),\quad AV=(x,1/4,r-1/8),
\quad BU=(1/4,3/8-r,3/8+r).
\]
The defining quadratic yields s(1-y)=7/16+h/2-r.

For AU, first-atom errors are r and 3/8-r<=r. Its second-atom lower error is <=sy<=s/2<=r. The upper error is <=r because
\[
sy-(1/4-r)=-3/16+(4/3)r(1-r)\ge1/64
\]
for r∈[3/16,1/4]. Its third atom has upper error exactly r and lower error 3/8+h/2-r<=r by r>H.

For AV, the second atom is the midpoint of [1/16,7/16], hence radius 3/16<=r. The third center r-1/8 against [1/64,1/4] gives errors bounded by 3/8-r<=r and r-9/64<r. Its first atom obeys the AU bound. For BU, the second atom at 3/8-r against [3/32-3h/4,3/8] gives upper error r and lower error 9/32+3h/4-r<=r since r>H>=9/64+3h/8. BV is fixed. Thus sup_{theta∈Q_h}D(P(theta),P(z))=r and R_L=T.

The exact gap derivative is 3/(2sqrt(43+24h))-1/4<0. At h=1/8 the gap is (4sqrt46-27)/32>0, because 16*46=736>27²=729.

## Actual verification, provenance and next unit

VERIFY.py reconstructs all six positive four-stop source rows, their original 20M mixing, the lawful center and the shared joint mixture, and checks exact rational/quadratic identities and vertex extrema for fourteen rational h values. RUN_EVIDENCE.txt is the executed local Fraction arithmetic result for the same mathematical tests. Finite vertex tests cross-check the implementation; the proof above covers every real h and every real parameter in Q_h by coordinate interval extrema. This result is a finite BRC statistics theorem and is not a six-axis P000 native-space, independent-time, or unrestricted eleven-control ten-label minimax theorem.

Next independently executable question: move only the *upper* a_A endpoint from 7/8 toward 1, keeping b/c intervals, and determine joint-hull and lawful exact radii and any transition using three-event witnesses and a joint mixture certificate. Compare with the a-lower phase transition and this b-lower nonclosure result. The current full eleven-control ten-label bound remains [1/2,2/3] for k=4,6.
