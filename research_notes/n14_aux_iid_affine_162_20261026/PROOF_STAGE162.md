# Stage162 — exact full-real interval and right-sharp support (AUTHOR)

## Scope and source
Finite ternary iid sequential decisions, horizon 14, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). Full ordered-history randomized policies are allowed. Define eP=P(decide Q), eQ=Q(decide P), tP=E_P stopping time, tQ=E_Q stopping time, V14(alpha)=minimum max(tP,tQ) under eP,eQ<=alpha. This is an external auxiliary model, not native P000/X6/BRC or a three-dimensional Cell-slice result.

Reused exact Stage161 proof and Stage162 DUAL-ONLY candidate from immutable source awdawmip/enterprise-math@a1a433279a998b0ba35c6add1de4eabed6985f59, research_notes/n14_aux_iid_affine_161_20261026. GLOBAL_KNOWLEDGE_V1 main snapshot 36faab26371c1213e055cb55227feada61205483.

## New theorem

Set K=1776538556208/5886215131, L=5152927839848/17658645393,
A=440625016346358918245/1265046575011281764352,
B=2138967403739208846181/180720939287325966336, and
eta=29431075655/2510013045657305088.

For **every real** 0<=delta<=eta,

V14(A+delta) = B - (10482543508472/17658645393)*delta.

The new exact right endpoint is
alpha162=440625031179621048365/1265046575011281764352,
V162=2138966145833987829541/180720939287325966336.

For every alpha>alpha162 the same dual support line is strictly unattainable:
V14(alpha)>Hroot-(K+L)alpha,
Hroot=211461038972875305263848856447/967349797503719726804631552.

This is sharpness of the **specific support**, not a claim that the value function stops existing past alpha162.

## Universal dual inequality and exhaustive Bellman certificate

Represent a count state by s=(n,a,b), where a is the count of symbol 0, b of symbol 1. The likelihood ratio Q(history)/P(history) is ell(s)=2^(a+b)/3^a. Under the P reference measure, Bellman's exact value is

H_s=min{ K*ell(s) [decide P], L [decide Q], 1+sum_i P_i H_child(s,i) [continue if n<14] }.

At n=14 continuation is not permitted. Hence any full-ordered-history policy satisfies
max(tP,tQ)>=tP>=Hroot-K*eQ-L*eP>=Hroot-(K+L)alpha.

Exactly 680=binom(17,3) count states were exhaustively checked in rational arithmetic. Only R=(10,0,1) and X=(7,3,3) tie (Q versus continue). All 1238 nonminimal gaps are **strictly positive**, with minimum 1055356088281/183084835434624. Every dual-optimal policy therefore follows forced actions outside these two ties on all positively reached prefixes. This finite census plus the recursion is a universal dual certificate for the stated model.

## True ordered paths, affine observers, and independent algorithm agreement

Use r,x in [0,1] as the probabilities of deciding Q immediately at R and X; zero means continue. The two tie cones are disjoint: X is at depth 7 with three symbol-0 observations, whereas R is at depth 10 with zero symbol-0 observations. Neither can be an ancestor of the other. Their first-hit prefix data under forced strict actions are:

R: 10 prefixes, P mass 9765625/120932352, Q mass 9765625/60466176.
X: 56 prefixes, P mass 35/5308416, Q mass 35/2239488.

A conditional-suffix exact Fraction recursion and a second, literal, unmerged integer-weight ordered-history DFS computed the four deterministic corners separately. Their four-vector outputs matched exactly. The DFS visited 483664, 473080, 483424, 472840 nodes at corners (r,x)=(0,0),(0,1),(1,0),(1,1), respectively (1,913,008 total). P and Q terminal masses equal 1 at each corner.

For M=(eP,eQ,tP,tQ),

M(r,x)=M00+r*dR+x*dX,

M00=(608980370270800655/1752976676930715648,
7002931380335/20061226008576,
2600664590463380201/219122084616339456,
153523688266399/13374150672384),

dR=(4521484375/1486016741376,
-3232421875/1253826625536,
-61181640625/557256278016,
-20751953125/104485552128),

dX=(34732355/300578991243264,
-6118315/80244904034304,
-1206850085/112717121716224,
-143514245/6687075336192).

The exact mixed vector M11-M10-M01+M00=(0,0,0,0). Because the first-hit cones do not intersect, independent randomized tie decisions obey the same affine formula; for arbitrary history-dependent tie randomizations, averaging the coin over each state's incoming P mass gives the same four observers (likelihood ratio is constant within each state).

## Entire feasible primal interval, attained duality, and strict sharpness

Error subtraction yields

eP-eQ=D0+Dr*r+Dx*x,

D0=-8835332954136275/5258930030792146944,
Dr=225517578125/40122452017152,
Dx=126080896865/657366253849018368.

Thus the exact equality-of-errors curve is

r(x)=353413318165451/1182361600000000
     -(3602311339/105568000000000)*x.

For every real x in [0,1], r(x) is strictly between 0 and 1. In particular r(0) is the inherited Stage161 right-endpoint coin and r(1)=1766864861392271/5911808000000000. The common error strictly increases from A to alpha162 as x runs from 0 to 1. Endpoint values are exactly tP=B at x=0 and tP=V162 at x=1. The two P-minus-Q stopping-time gaps are
526231060559760430495/1265046575011281764352 and
526240831439401052735/1265046575011281764352,
both positive. Thus tP>tQ throughout the real segment. At both endpoints tP+K*eQ+L*eP=Hroot; linearity implies equality throughout. This feasible primal family attains the universal dual lower bound for every real alpha in [A,alpha162].

The randomized finite-horizon policy space is a finite product of compact simplices and the four observer functions are continuous; a feasible optimum exists. If equality with this same dual support held for alpha>alpha162, then K,L>0 force eP=eQ=alpha and all positively reached actions to be Bellman minimizers. Such a policy can randomize only at R/X. Since Q/P is constant across histories arriving at a given count state, and their cones are disjoint, weighted-average coins give the above M(r,x) exactly. Error equality forces r=r(x); for x in [0,1] the greatest possible common error is alpha162 at x=1. Contradiction. Consequently the support is strictly unattainable immediately and everywhere to its right.

## Actual validation scope and next independent task

Actual local author execution used Python integers and Fraction, not floating-point thresholds. Two mathematically distinct evaluation algorithms agreed at every corner and counted all ordered first hits. A portable code/certificate bundle was generated. This constitutes AUTHOR computation-assisted proof, not independent Driver review, a native Source Result, an ACTIVE owner CLAIM, or P000 theorem admission.

Follow-on exact dual-ray scan (Stage163 DUAL-ONLY): retaining R's Q/continue tie with dK=-1 and dL=-10592/12501, X becomes strictly Q; first new closure Y=(8,4,1) at step 19719048267802073097/3261849711321095041 gives K163=163900037061/554150611, L163=476600779976/1662451833, 1238 strictly positive gaps (minimum 1577397669610597/79424873185738752). Stage163 primal full-real interval remains **OPEN**. Do not promote these scalar/positive-mass calculations to native BRC cancellation or six-dimensional Cell dynamics without a typed correspondence proof.
