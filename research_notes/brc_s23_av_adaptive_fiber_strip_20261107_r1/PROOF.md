# S23/AV: observer-adaptive lawful-fiber strip reaches constructive coefficient sqrt(80/27)

Date 2026-11-07. Frozen science awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Author-side mathematical proof, independent review pending. Predecessor: padded nonadaptive strip at commit 5dd610b667f39e732059b9e4194cca7037753f2c.

## Exact model and theorem

For all legal real a,c in [1/2,7/8], set z=(1-a)c, b=(1-a)(1-c), s=1-z=a+b, p=a/s. The full source P=(a,z,b) on ordered labels (1,3,4), and the compressed observer B=(z,1-z) on (Y,N), are repeated independently n times with ONE SHARED unknown pair (a,c). The decoder L is a single parameter-independent kernel from {Y,N}^n to the *full ordered* {1,3,4}^n. Define delta_n=inf_L sup_(a,c) TV(P^tensor n,B^tensor n L).

**Theorem:** An explicit observer-only adaptive kernel L_n below satisfies

lim_(n->infinity) sqrt(n/log n)*inf_(a,c) [1-TV(P^tensor n,B^tensor n L_n)]
= sqrt(80/27)=4sqrt(15)/9=1.721325931647739... .

Therefore the optimal auxiliary problem obeys the new constructive bound

liminf_(n->infinity) sqrt(n/log n)*(1-delta_n) >= sqrt(80/27).

The previous author-side padded nonadaptive kernel had coefficient (19/3)sqrt(3584/185193)=0.881057116059..., so this is a factor of about 1.9537 in achievable asymptotic overlap. This theorem specifies a decoder, not the exact minimax leading constant.

## 1. Lawful hidden-p fibers

Write u=1-a in [1/8,1/2]. Fixed z requires c=z/u in [1/2,7/8], equivalent to
u_min(z)=max(1/8,8z/7) <= u <= u_max(z)=min(1/2,2z).
Hence z ranges over [1/16,7/16], and the exact lawful interval of p=(1-u)/(1-z) is

p_-(z)=(1-u_max(z))/(1-z), p_+(z)=(1-u_min(z))/(1-z),
h(z)=p_+(z)-p_-(z)=[u_max(z)-u_min(z)]/(1-z).

Its breakpoints are z=7/64 and 1/4. The endpoint functions are continuous and globally 2-Lipschitz on [1/16,7/16]. Indeed on z<=1/4, p_-=(1-2z)/(1-z) has derivative -1/(1-z)^2 of magnitude <=16/9; on z>=1/4, p_-=(1/2)/(1-z) has derivative <=128/81. On z<=7/64, p_+=(7/8)/(1-z) has derivative <2, while for z>=7/64, p_+=(1-8z/7)/(1-z) has derivative -1/[7(1-z)^2] of magnitude <2. Thus p in [2/3,56/57] and s in [9/16,15/16]. Fiber width h is positive in the open z interval and zero at its endpoints.

## 2. A decoder determined by the actual compressed input

For the binary input word count R observed Ys, put m=n-R and zhat=R/n. Clamp zhat to [1/16,7/16], obtaining ztilde. Let

W_n=ceil(4 sqrt(n log(n+2)))+1,
A_(n,R)=max(0,floor(m*p_-(ztilde))-W_n),
D_(n,R)=min(m,ceil(m*p_+(ztilde))+W_n),
L_(n,R)=D_(n,R)-A_(n,R)+1.

Preserve each observed Y position as full output label 3. Draw K uniformly from the integer interval [A_(n,R),D_(n,R)], then choose uniformly K of the m other positions as label 1 and label the remaining as 4. This is a normalized parameter-independent stochastic decoder, using only observed R, retaining full output positions.

Condition on the Y positions. Their joint position law is identical in source and decoder. Given R=r, target K~Bin(m,p), decoder K~Unif([A_(n,r),D_(n,r)]), and both conditional arrangements given K are uniform. Consequently the exact full ordered total-variation overlap is

O_n(a,c)=1-TV(P^tensor n,B^tensor n L_n)
=sum_(r=0)^n BinPMF(n,r,z)*F_(n,r)(p),

F_(n,r)(p)=sum_(k=A_(n,r))^(D_(n,r))
min{BinPMF(n-r,k,p),1/L_(n,r)}.                                  (1)

No independence assumption about reconstructed output sites is made.

## 3. Typical observer and uniform strip geometry

Set t_n=sqrt[(3/2)log(n+2)/n]. Hoeffding gives
Pr(|R/n-z|>t_n)<=2(n+2)^(-3).
On the typical event E_n, m>=n/2 for all sufficiently large n and
|ztilde-z|<=t_n. The two endpoint functions are 2-Lipschitz, so the distance of true p from the estimated lawful interval is <=2t_n. The width of padding beyond mp is at least
W_n-2m*t_n >= [4-sqrt(6)+o(1)]sqrt(n log n).
Since 4-sqrt(6)>1, it contains every integer with
|k-mp| <= (1+epsilon)sqrt(m*p(1-p)*log m)
for all fixed 0<epsilon<1, uniformly in parameters on E_n. For sufficiently large n, clipping at 0,m does not affect strip endpoints because p_± in [2/3,56/57], m>=n/2 and W_n=o(n). Thus uniformly on E_n,

L_(n,R)=m*h(z)+O(sqrt(n log n)).                                   (2)

## 4. Uniform conditional overlap, including vanishing-width fibers

Write v=p(1-p), so v_min=56/3249<=v<=1/4. The uniform local Stirling formula for |k-mp|=O(sqrt(m log m)) is

log BinPMF(m,k,p)=-0.5 log(2*pi*m*v)-(k-mp)^2/(2*m*v)+o(1),     (3)

with uniform remainder (the entropy Taylor remainder is O((log m)^(3/2)/sqrt m)). The binomial Bernstein tail bound at radius r=(1+epsilon)sqrt(m*v*log m) is
Pr(|Bin(m,p)-mp|>=r) <=2exp[-r^2/(2*(m*v+r/3))]
=m^[-(1+epsilon)^2/2+o(1)]=o(sqrt(log m/m)).
These two facts imply the following uniform cases.

Case I, h(z)>=h0=1/100: (2) makes L/(m h(z))->1 uniformly. In the inner window radius (1-epsilon)sqrt(m v log m), (3) makes each atom larger than 1/L, so the overlap equals count/L there. Outside the outer window the Bernstein tail is negligible. Letting epsilon tend to zero gives, uniformly on E_n,
F_(n,R)(p)=[2sqrt(v)/h(z)+o(1)]sqrt(log m/m).
With m/n=s+o(1), the coefficient relative to sqrt(log n/n) is
C_f(a,c)=2sqrt(v/s)/h(z).

Case II, n^(-1/4)<=h(z)<h0: equation (2) still gives L=(1+o(1))m h(z) uniformly. On an inner window of radius (1/2)sqrt(m v log m), (3) bounds every atom below by c*m^(-5/8) for a fixed c>0, whereas 1/L=O(n^(-3/4)); all central terms therefore contribute exactly 1/L. Counting them shows
F_(n,R)(p) >= [sqrt(v/s)/h(z)+o(1)]sqrt(log n/n).
The coefficient is at least sqrt((56/3249)/(15/16))/h0 >10, strictly exceeding sqrt(80/27).

Case III, h(z)<n^(-1/4): (2) gives L=O(n^(3/4)). Within |k-mp|<=sqrt m there are Omega(sqrt m) integers, each with binomial mass at least c/sqrt m by (3). The strip includes this window. Thus
F_(n,R)(p) >= c sqrt(m)*min{c'/sqrt m,1/L} >= c'' n^(-1/4),
which divided by sqrt(log n/n) tends to infinity uniformly.

The exceptional event has probability O(n^(-3)) and the overlap is nonnegative. Thus these three cases prove a global uniform liminf for O_n/sqrt(log n/n) at least the smallest C_f(a,c) over positive-width fibers.

## 5. Exact optimization over lawful fibers

For fixed z, p>=2/3, so v=p(1-p) decreases with p and C_f is minimal at p=p_+(z). Substituting exact fiber endpoints gives the following squared coefficient:

C_f,min(z)^2 =
  28(1-8z)/[(1-z)(16z-1)^2],                 1/16<z<=7/64;
  (7-8z)/[9z(1-z)],                          7/64<=z<=1/4;
  16z(7-8z)/[(1-z)(7-16z)^2],                1/4<=z<7/16.

The first branch decreases: logarithmic derivative
-8/(1-8z)+1/(1-z)-32/(16z-1)<0.
The second decreases: derivative -8/(7-8z)-1/z+1/(1-z)<0.
The third increases: derivative
(7-16z)/[z(7-8z)]+1/(1-z)+32/(7-16z)>0.
The unique global minimum is at z=1/4, p=p_+(1/4)=20/21, the actual lawful corner (a,c)=(5/7,7/8). Its square is 80/27. This pair has h(1/4)=2/7>h0, so Case I also provides a matching upper limit for this *particular decoder*. Combined with the global liminf, it proves the theorem with equality. The minimax constructive inequality follows from delta_n<=sup TV for any fixed decoder.

## Scope, independent evidence and future problem

VERIFY.py independently enumerates all full ordered 3^n target and decoder words at n=2..5 for six lawful rational pairs, checks exact probability normalization and identity (1) using Fraction, verifies exact fiber endpoints and a rational coefficient grid, and reports several observable finite-n strip lengths. RUN_EVIDENCE.txt contains actual executed output. The all-real n->infinity result is proved analytically above, not inferred from finite samples.

BRC/provenance discipline: only the lawfully observed Y count is used for adapting the decoder, all observed Y positions remain fixed and output ordering is retained; the fiber interval is an observer-specific future-operation certificate, not a claim about native X6 spatial redundancy. P000 and the six-source/ten-label S23 mother experiment remain separate. Exact optimal minimax coefficient and lawful mother-model transfer are open. Native Owner/CLAIM/RA and independent review were unconfirmed after BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false.

Next: optimize padding for finite n, seek matching minimax fixed-fiber dual asymptotics, and construct a source/time-typed repeated mother experiment.