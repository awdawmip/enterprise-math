# S23 AV: sharp Bayes-risk loss throughout the lawful c-variation family

Date: 2026-11-06. Classification: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific source: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessor: awdawmip/enterprise-math@132ecfa92a844056c9c78d135e4faaef582b77d5, PR #1774.

## Model, preserved provenance and quantifiers

Use the lawful six-source S23 statistical model on Q=[1/2,7/8] x [1/8,1/2] x [1/2,7/8]. Keep all source labels AU0, AU1, AV, BU0, BU1, BV; their common second-stage control b is fixed *to the same value* under both hypotheses. Also fix a under both hypotheses and allow only c to vary: theta_-=(a,b,x), theta_+=(a,b,y), where 1/2<=a<=7/8, 1/8<=b<=1/2 and 1/2<=x<y<=7/8. Put q=1-a.

The source-tagged full AV four-stop experiment under H_- and H_+ is
A_-=(a,0,qx,q(1-x)), A_+=(a,0,qy,q(1-y)).
The forward deterministic observer W=1 iff the AV stop is 3 gives the two Bernoulli laws
B_-=(qx,1-qx), B_+=(qy,1-qy).

For every real prior t=Pr(H_+) in [0,1], define R_A(t) and R_B(t) as minimum binary 0-1 Bayes classification error for these respective experiments (one AV sample). Their difference L(t)=R_B(t)-R_A(t) is an exact observer-loss function.

## Theorem 1: exact real-prior loss curve

Define two rational breakpoints

k=(1-qx)/(2-q(x+y)),
h=(1-x)/(2-x-y).

They satisfy 1/2<k<h<1. For every real t in [0,1],

L(t) =
  0,                                    0<=t<=1/2;
  a(2t-1),                              1/2<=t<=k;
  q[(1-x)-(2-x-y)t],                    k<=t<=h;
  0,                                    h<=t<=1.

Consequently L is positive exactly on (1/2,h) and has its unique maximum at t=k:

max_t L(t) = a q (y-x) / [2-q(x+y)].

The full and compressed experiments have the same total variation q(y-x), and their equal-prior Bayes error is (1-q(y-x))/2.

**Proof.** For finite conditional laws U_-,U_+, the Bayes 0-1 risk is sum_j min((1-t)U_{-,j},t U_{+,j}). Substituting the displayed laws and cancelling the shared stop3 contribution gives

L(t)=min((1-t)(1-qx),t(1-qy))
     -a min(1-t,t)
     -q min((1-t)(1-x),t(1-y)).

The three minima switch at k, 1/2 and h respectively. Because q<1 and y>x,
k-1/2 = q(y-x)/[2(2-q(x+y))] > 0,
h-1/2 = (y-x)/[2(2-x-y)] > 0.
Moreover k<h follows on cross-multiplying positive denominators:
(1-x)(2-q(x+y))-(1-qx)(2-x-y) = (1-q)(y-x) = a(y-x)>0.
Substituting the correct affine branches yields all four expressions. Their slopes are 0, 2a>0, -q(2-x-y)<0 and 0. Continuity holds at every breakpoint, proving positivity and the unique maximum. The two distribution differences have masses +q(y-x),-q(y-x) in exactly two atoms before/after deterministic grouping, so both total variations equal q(y-x). The equal-prior risk identity follows directly. QED.

## Theorem 2: sharp uniform 1/14 bound and uniqueness

Over all a,b,x,y in the stated lawful box (with x<y), and all real priors t,

0 <= L(t) <= 1/14.

Equality to 1/14 occurs precisely at
a=1/2, x=1/2, y=7/8, t=4/7,
with any b in [1/8,1/2]. In particular, the predecessor's 1/14 example is extremal for this entire common-(a,b), variable-c lawful family.

**Proof.** By Theorem 1 it is enough to maximize
F(a,x,y)=a(1-a)(y-x) / [2-(1-a)(x+y)].
For any fixed q=1-a in [1/8,1/2], differentiating the rational function in x and y gives numerator factors -2+2qy<0 and 2-2qx>0 respectively (the denominator is strictly positive). Thus its unique maximum with respect to x,y is at x=1/2,y=7/8. Writing q=1-a then gives
F(q)=3q(1-q)/(16-11q).
Its derivative is 3(16-32q+11q^2)/(16-11q)^2. The numerator decreases on [1/8,1/2] and remains positive even at q=1/2, where it equals 11/4. Hence F increases strictly with q and is uniquely maximized at q=1/2, i.e. a=1/2. The attained value is
3(1/2)(1/2)/(16-11/2)=1/14.
At these parameters, k=(1-1/4)/(2-1/4-7/16)=4/7. Theorem 1 gives uniqueness of the maximizing prior. The common b does not enter AV and can take any lawful value. QED.

## Theorem 3: strict reverse-kernel obstruction for every nonidentical pair

For every allowed a,b and x<y above, there is no hypothesis-independent row-stochastic kernel from the Bernoulli W output back to the full AV four-stop output that reconstructs both A_- and A_+.

**Proof.** Let r=qx<s=qy. If a reverse K existed, the target stop3 equations r K(yes,3)+(1-r)K(no,3)=r and s K(yes,3)+(1-s)K(no,3)=s imply K(yes,3)=1 and K(no,3)=0 by subtraction and stochastic bounds. Likewise the target stop1 equations have constant target probability a in both hypotheses and force K(yes,1)=K(no,1)=a. Since a>0, the yes row has mass at least 1+a>1. Contradiction. QED.

## BRC applicability, verification and next mother-objective link

This theorem preserves source tagging, stop ordering, positive four-stop mass and the common b coupling. The one-bit W projection is a declared information-reducing observer; the exact L(t) quantifies one-step binary 0-1 decision loss and its complete lawful-parameter worst case. The reverse-kernel obstruction is a scope-specific fiber/experiment witness. No hypothesis-independent restoration of full AV is assumed.

VERIFY.js uses only exact rational BigInt arithmetic and checks 24 lawful parameter pairs, 216 rational priors (all analytically derived knots and midpoint witnesses), total variation, risk formulas, slope-derived bounds, and the sharp extremizer. Finite checks supplement; the all-real theorems follow from the displayed algebra.

For the original ten-label behavioral mother objective, next verify whether a *single legitimate* ten-label encoding/decoding policy implements AV and its stop3 projection with the same source and hypothesis coupling. A licensed experiment map would transfer appropriate inequality directions. This author result has not been independently reviewed/admitted; no formal task CLAIM/Result is attached.