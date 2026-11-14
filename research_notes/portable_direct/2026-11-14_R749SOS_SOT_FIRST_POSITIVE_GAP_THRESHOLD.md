# R749SOS–SOT | First positive calibration-gap threshold in the frozen Walsh model

Date: 2026-11-14. Status: AUTHOR_EXACT_NOT_REVIEWED.
Frozen scientific source: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Earlier frontier: R749SOQ–SOR, Draft PR #2394 @20191ce4c73f5335fa935be6c5a1518b1483784d.
This is the 16-atom auxiliary Walsh source observer, with no native X6/V29/V39 bridge claimed.

## Statement and definitions

Let K=F_2^4 and chi_m(k)=(-1)^popcount(m AND k). Set A=chi_3, B=chi_12, C=chi_15=AB. At s=1/2, the legal probability source is

mu_(t,h,u,v,w,z)(k) =
[1+t A(k)+(1/2)B(k)+h C(k)+u chi_1(k)+v chi_2(k)+w chi_4(k)+z chi_8(k)]/16,

subject to sixteen nonnegative atoms. Let F_t be its compatible fiber; TV is total variation. Let rho be the free minimax TV Chebyshev radius over all probability centers, and rho_cal the minimax radius over calibrated centers in F_t.

R749SOS: For EVERY REAL 1/6 <= t <= 5/22,

rho(t,1/2) = rho_cal(t,1/2) = (7-2t)/16.

R749SOT: For EVERY REAL 5/22 <= t <= 1/4,

rho(t,1/2) = (7-2t)/16,
rho_cal(t,1/2) = (1+t)/3,
g(t,1/2) := rho_cal-rho = (22t-5)/48.

Together with R749SOR's exact theorem rho=rho_cal=(1-t)/2 for all real 0<=t<=1/6, the first strictly positive g as t increases at fixed s=1/2 begins immediately above the exact threshold t*=5/22. Thus g=0 for all t in [0,5/22], and g>0 for t in (5/22,1/4]. The boundary t=5/22 is included in both new statements.

## Matching free-radius lower bound

For 1/6<=t<=1/4 consider

p_plus(t)  = mu_(t,0,+t,+t,+1/2,+(1-t)),
p_minus(t) = mu_(t,0,-t,-t,-1/2,-(1-t)).

All sixteen atoms of each source are affine in t; checking endpoints 1/6, 5/22 and 1/4 establishes nonnegative unit-mass laws across the combined interval. The signs of their atomwise differences agree weakly at neighboring endpoints. Exact sixteen-atom sign summation gives

TV(p_plus(t),p_minus(t))=(7-2t)/8.

Consequently, for every decoder (including calibrated ones), the TV triangle inequality gives radius at least (7-2t)/16.

## Zero-gap extension SOS: explicit upper center

Choose the legal calibrated center

q_zero(t,k) = [1+t A(k)+(1/2) B(k)+(1/4-3t/2) C(k)]/16.

For the bounded six-dimensional joint probability polytope with y=(t,h,u,v,w,z) and t in [1/6,5/22], there are 16 source-atom facets plus two parameter endpoint facets. Its full dimensionality follows at an interior t and zero other coefficients. The map

D_zero(y) = TV(mu_y,q_zero(t)) - (7-2t)/16

is convex (TV of affine maps minus an affine function). Every maximum is attained at a vertex. The exact integer Bareiss enumeration over all C(18,6)=18,564 active bases produces 9,536 nonsingular bases, 392 feasible bases and 100 distinct rational vertices (50 at each endpoint, none inside). Maximum D_zero over vertices is exactly 0; there are zero violations, 44 tight vertices. By convexity, the upper bound holds for every real parameter and every source. With the source-pair lower bound this proves R749SOS.

## Positive-gap onset SOT: exact calibrated lower bound

Translations k -> k XOR a for a in {0,3,12,15} preserve A,B,C and permute the legal source family F_t. Group-averaging any calibrated center preserves its A,B moments and cannot increase worst-case TV by convexity and invariance. The averaged center has only Fourier coefficients 1,A,B,C and therefore is

q_h(t,k)=[1+t A(k)+(1/2) B(k)+h C(k)]/16.

It suffices to establish the lower bound for every real h. Introduce two explicit compatible source families

a_t = mu_(t, t-1/2, 0,0, -1/2-t, -1/2-t),
b_t = mu_(t, t+1/2, 0,0, t-1/2, t-1/2).

Their sixteen atom values are affine in t and nonnegative at the two endpoints 5/22,1/4, hence throughout. The fixed exact sign-event supports (full 16-component vectors included in the companion JSON) give the algebraic inequalities for every real h:

TV(a_t,q_h) >= 3/8 + t/4 + h/4,
TV(b_t,q_h) >= 1/4 + t/2 - h/2.

These are TV dual inequalities arising from one fixed signed sum of atom differences each. Their maximum is always at least (1+t)/3; the affine forms intersect precisely at h=t/3-1/6. Thus rho_cal >= (1+t)/3 for the whole real interval.

## SOT: explicit upper centers and full exact certificate

Choose q_cal(t,k) = [1+t A(k)+(1/2) B(k)+(t/3-1/6)C(k)]/16.

For free prediction, let lambda(t)=44t-10 in [0,1] and

q_free(t) = (1-lambda(t))*q_cal(5/22) + lambda(t)*q_1,
q_1(k)=[1+(7/16) A(k)+(1/2) B(k)+(1/16) C(k)]/16.

Both are probability centers affine in t; q_free need not preserve source t and s. In the joint six-dimensional source polytope with t in [5/22,1/4], complete C(18,6)=18,564 active-basis enumeration yields 9,536 nonsingular bases, 476 feasible bases, and 92 unique rational vertices (50 at 5/22, 42 at 1/4). At every vertex the exact checks establish

TV(mu,q_free(t)) <= (7-2t)/16,
TV(mu,q_cal(t)) <= (1+t)/3.

Both maximum excesses are exactly zero (32 free-tight and 28 calibrated-tight vertices), with zero violations. Convexity extends these affine-center bounds to all real t and all compatible source laws. Combining the upper bounds and matching lower witnesses completes R749SOT.

## Reproduction, provenance and next question

Run Python 3 standard library:
python research_notes/portable_direct/R749SOS_SOT_EXACT_CERTIFICATE.py

Compare printed JSON to research_notes/portable_direct/R749SOS_SOT_EXACT_RESULTS.json. The program performs complete integer Bareiss / Fraction vertex enumeration, 37,128 joint active bases in total, exact lower source-TV checks and fixed-event-support algebra checks. All numerical comparisons are exact; the all-real-parameter proof relies on vertex completeness, linearity and convexity rather than finite parameter sampling.

This is an author-side exact proof, not yet independently reviewed. It extends the verified frozen Walsh research frontier R749SOQ/SOR and preserves its scientific source pin. The native X6/V29/V39 source/branch/signed-port correspondence remains a separate open problem.

Next mathematical unit: perturb s from 1/2 near (t,s)=(5/22,1/2); derive two-dimensional piecewise free/calibrated centers and source-event dual certificates to identify the tangent or corner of the actual zero/positive-gap boundary. Use the same frozen auxiliary input and preserve eventual typed native observer provenance.
