# BRC N=4/S23 — exact one-endpoint Chebyshev phase transition

2026-11-01. Author-side analytic proof / exact quadratic-field arithmetic executed / UNREVIEWED / NOT_ADMITTED.

## Frozen model

Continue the exact asymmetric lawful-versus-hull gap at immutable EM source 43ec6098b1330ae86d0a7863be336c5d97f6ef34 and its immediate exact pointwise-modulus next question at c9733c685867703b98cb04f83948d53329fca100. Keep the six distinct positive BRC source identities AU0,AU1,AV,BU0,BU1,BV, four-stop law

\[
F(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c)),
\]

and the original positive preparation mixing matrix

\[
20M=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
(0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20)).
\]

Freeze a_B=1/4, b_AV=0, b_BV=1/3, and c_AU0=c_AU1=c_BU0=c_BU1=c_BV=1/2. The controls (a,b,c)=(a_A,b_U,c_AV) have b_U **shared across A and B**. Move only the lower a endpoint:

\[
Q_h=[1/2-h,7/8]\times[1/8,1/2]\times[1/2,7/8],\quad 0\le h\le1/8.
\]

Under the specified freeze, the AU0/AU1 and BU0/BU1 probability rows coincide (their labeled sources remain distinct). Effective three-atom representations for *this fixed four-stop total-variation observer* are:

\[
AU=(a,(1-a)b,(1-a)(1-b)),\quad AV=(a,(1-a)c,(1-a)(1-c)),
\]
\[
BU=(1/4,3b/4,3(1-b)/4),\quad BV=(1/4,1/4,1/2).
\]

The two equal AU tail atoms are grouped only in computing the declared TV; for three-atom probability laws TV equals the maximum of the three singleton absolute differences. The joint metric is D(P,P')=max over all six preparation rows of TV. Let R_L(h) be the least maximum D-radius with center P(z), z in Q_h, and R_H(h) the analogous least radius when the center is any **joint** convex combination of whole six-row lawful observations.

## Theorem (all real parameters)

Write
\[
H(h)=3/16+h/2,\quad T(h)=(\sqrt{43+42h}-5)/8,\quad
h_*=(\sqrt{37}-5)/16.
\]
For every real 0<=h<=1/8,
\[
\boxed{R_H(h)=H(h),\qquad R_L(h)=\max\{T(h),H(h)\}.}
\]
Consequently the strict lawful-versus-hull minimax gap is exactly
\[
G(h)=\begin{cases}
(2\sqrt{43+42h}-13-8h)/16>0,&0\le h<h_*,\\
0,&h_*\le h\le1/8.
\end{cases}
\]
The gap closes precisely at h_*, approximately 0.0676726581, within this solved interval. The one-sided base-box derivatives are R_L'(0+)=21/(8\sqrt{43}), R_H'(0+)=1/2 and G'(0+)=21/(8\sqrt{43})-1/2. No formula is claimed for h>1/8.

## Universal lower bounds

The first AV stop mass traverses [l,u]=[1/2-h,7/8]. Any center has radius r>=H(h), by the two extremes. For any *lawful* center (x,y,t), three legal event witnesses additionally force
\[
7/8-x\le r,\qquad
7/16+7h/8-(1-x)(1-y)\le r,\qquad
3(1/2-y)/4\le r.
\]
Hence (1-x)<=(1/8+r), (1-y)<=(1/2+4r/3), both factors nonnegative, and
\[
(1/8+r)(1/2+4r/3)\ge7/16+7h/8-r
\Longleftrightarrow32r^2+40r-9-21h\ge0.
\]
The polynomial increases on r>=0; its positive root is T(h). Therefore R_L>=max(H,T). The identity T(h)>=H(h) is equivalent (for nonnegative h) to 64h^2+40h-3<=0, whose unique positive root is h_*.

## One joint convex-hull upper witness

With l=1/2-h and u=7/8, use the *single joint* mixture
\[
V_h=(4/9)P(l,1/8,7/8)+(1/18)P(l,1/2,1/2)
 +(2/9)P(u,1/8,7/8)+(5/18)P(u,1/2,1/2).
\]
Its effective rows are:
\[
AU=(11/16-h/2,\ 1/16+h/12,\ 1/4+5h/12),
\]
\[
AV=(11/16-h/2,\ 1/4+5h/12,\ 1/16+h/12),
\]
\[
BU=(1/4,3/16,9/16),\qquad BV=(1/4,1/4,1/2).
\]
Over the *entire real box*, the AU three coordinate ranges are [l,u], [1/64,1/4+h/2], [1/16,7/16+7h/8]. AV has the same first range and the other two reversed. BU's second coordinate spans [3/32,3/8]. The maximum error is H from the first atom; each other coordinate differs by at most 3/16+11h/24, 3/16+5h/12 or less, all <=H. These are exact interval extrema of the multiaffine products, not sampled grid bounds. Thus R_H<=H and the lower bound proves R_H=H.

## Exact lawful center for 0<=h<=h_*

Let r=T(h). Then H<=r<1/4. Define
\[
x=7/8-r,\quad y=1/2-4r/3,\quad
t=(1/4+7h/16)/(1/8+r),\quad s=1-x=1/8+r.
\]
These are lawful: x is between l and u, y between 1/8 and 1/2; the inequalities r<=1/4 and r>=H>=9/56+h/2 give 1/2<=t<=7/8. Equality in the quadratic lower-bound polynomial yields
\[
sy=2r-5/16-7h/8,\quad s(1-y)=7/16+7h/8-r,
\]
\[
st=1/4+7h/16,\quad s(1-t)=r-1/8-7h/16.
\]
Compare each against the exact coordinate ranges above. The a errors are r and 3/8+h-r<=r. AU second-atom upper error is 9/16+11h/8-2r<=r because r>=H>=3/16+11h/24; its lower-end error is <=r since r<1/4<21/64+7h/8. The AU tail has upper error exactly r and lower error 3/8+7h/8-r<=r. AV's c-atom midpoint error is 3/16+7h/16<=r; its last-atom upper error is 3/8+15h/16-r<=r, and its lower-end error <=r. The BU risk is max(r,9/32-r)=r and BV remains fixed. Hence all real policies in Q_h have joint TV <=r against this *single legal* center. Together with the lower witness, R_L=T for h<=h_*.

## Exact lawful hull-tight center for h_*<=h<=1/8

Set r=H(h) and
\[
x=11/16-h/2,\quad y=1/4-2h/3,\quad
t=(1/4+7h/16)/(5/16+h/2),\quad s=1-x.
\]
All controls are legal on this interval. AU's effective center coordinates become
\[
(x,sy,s(1-y))=
(11/16-h/2,\ 5/64-h/12-h^2/3,\ 15/64+7h/12+h^2/3).
\]
Its a-coordinate error is r. For the other two coordinates the maximal relevant errors are bounded by
\[
11/64+7h/12+h^2/3\le r,\qquad
13/64+7h/24-h^2/3\le r.
\]
The first is equivalent to 64h^2+16h-3<=0, true through h=1/8; the second is equivalent to 64h^2+40h-3>=0, true from h_*. All smaller endpoint errors are dominated. For AV, st=1/4+7h/16 is its c-atom interval midpoint and s(1-t)=1/16+h/16, so each error is <=3/16+7h/16<=r. BU reaches r at b=1/2 and never exceeds it. BV stays constant. Thus R_L<=H on this interval. The universal a-extreme lower bound establishes equality, proving the transition.

## Exact verification and scope

The companion VERIFY.py was executed with standard-library Python Fraction and exact ordered quadratic-field arithmetic. It materializes the original six BRC source distributions and the 20M mixing matrix; for each of ten rational displacements it checks the exact TV maximum against all eight box vertices for the explicit lawful and joint-hull centers, plus the radical polynomial identity. It separately checks 64h_*^2+40h_*-3=0 in Q(sqrt(37)) and equality of the radical and hull branches at h_*. The actual stdout is RUN_EVIDENCE.txt; terminal marker PASS_BRC_N4_S23_ONE_ENDPOINT_EXACT_HULL_GAP_PHASE_20261101. The universal real result is the interval/analytic argument above, not a finite sampling inference.

The previous generic bound G(h)>=G(0)-4h only certifies positivity for h<G(0)/4≈0.001795. The exact directional theorem determines the whole phase change and is materially sharper in this one direction. It neither improves the full eleven-control, ten-label minimax interval [1/2,2/3] (k=4,6) nor proves native P000 six-axis Cell geometry, independent time, full three-dimensional slice, arbitrary future-observer quotienting, or S2 causal transfer. The proof is author-side, unreviewed, and not mathematically admitted by native Enterprise Math governance.
