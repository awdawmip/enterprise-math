# BRC N=4 S23: exact sharp nonlinear TV modulus for overwrite-only two-view banks

Date: 2026-11-03. Status: AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Input, observer and question

Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. In the exact 11-coordinate S23 model, source i=0,...,5 has four ordered first-success probabilities

b(p,q,r) = (p,(1-p)q,(1-p)(1-q)r,(1-p)(1-q)(1-r)),

with A=(0,0,0,1,1,1), B=(2,2,3,2,2,4), C=(5,6,7,8,9,10) as the indices of p,q,r in z∈[0,1]^11. The six distinctly labeled observed rows are P_j(z)=sum_i (M_ji/20)b(z_Ai,z_Bi,z_Ci), where

~~~
M = ((10,10, 0, 0, 0, 0),
     ( 9,11, 0, 0, 0, 0),
     ( 0, 0,20, 0, 0, 0),
     ( 0, 0, 0,10,10, 0),
     ( 0, 0, 0, 2,18, 0),
     ( 0, 0, 0, 0, 0,20)).
~~~

U_(m,beta) replaces every coordinate z_k with bit k set in mask m (k=0,...,4) by the same fixed beta∈[0,1]. For each of (3,31),(7,27),(11,23),(15,19), N denotes the mask NOT covering z2 and E the mask covering z2. Let their respective constants be beta_N,beta_E; a=1-beta_N and b=1-beta_E.

Remove the original baseline view and retain only N and E. For z,w∈[0,1]^11 set d_F(z,w)=max_(v∈{N,E}, j=0,...,5) TV(P_j(U_v z),P_j(U_v w)), with TV the half-L1 distance of four-outcome probability distributions. Define Omega_F(eps)=max_{||z-w||_infinity≤eps} d_F(z,w), for every real eps∈[0,1].

## Theorem: all-real exact moduli and sharp forward Lipschitz constants

For every real eps,beta_N,beta_E∈[0,1]:

* For F=(3,31), with N=3 and E=31, Omega_F(eps)=max{a(2eps-eps²), b²eps}; sharp global Lipschitz constant max{2a,b²}.
* For F=(7,27),(11,23),(15,19), with (N,E)=(27,7),(11,23),(19,15), respectively, Omega_F(eps)=max{a,b}(2eps-eps²); sharp global Lipschitz constant 2max{a,b}.

The value of each modulus is attained by legal states for every eps (eps=0 included). At beta_N=1,beta_E=0,eps=1/2, the first pair has modulus 1/2 but the other three have modulus 3/4.

## Proof of the universal upper bounds

Both N and E always overwrite z0,z1. For any source, its first gate is therefore the same fixed beta in both compared states. Factoring out its first outcome gives

TV(b(beta,q,r),b(beta,q',r'))=(1-beta)TV(q2(q,r),q2(q',r')),

where q2(q,r)=(q,(1-q)r,(1-q)(1-r)). Couple the two Bernoulli gate pairs maximally, independently. Their first-success outputs agree if both coupled bits agree, hence

TV(q2(q,r),q2(q',r'))≤1-(1-|q-q'|)(1-|r-r'|)≤2eps-eps².

If the second gate is also fixed to beta, directly subtracting the last two outcomes gives the exact identity

TV(b(beta,beta,r),b(beta,beta,r'))=(1-beta)²|r-r'|≤(1-beta)²eps.

The mixer M/20 has nonnegative rows summing to one. TV convexity under common-weight mixing carries each raw-source bound to every labeled observed row. N always has upper bound a(2eps-eps²). E=31 covers all second-gate coordinates (z2,z3,z4) and thus has bound b²eps. Other E masks 7,23,15 have bound b(2eps-eps²). Taking the maximum of the two view bounds yields the theorem's asserted upper bounds.

## Exact extremizers (lower bounds)

For N in all four pairs let z be identically zero and let w have exactly coordinates z2,z5,z6 equal eps. N leaves these gates free. At each state raw sources i=0 and i=1 have identical (p,q,r), namely (beta_N,0,0) at z and (beta_N,eps,eps) at w. Their observed mixture row j=0 remains exactly this common distribution. Its TV distance is a[1-(1-eps)²]=a(2eps-eps²).

For E=31 set z=0 and w7=eps (all other w coordinates zero). Observed row j=2 isolates source i=2, whose first and second gates are both beta_E and whose third gate is z7. Its TV equals b²eps.

For E=7 or E=23 set z=0 and w3=w7=eps. The same isolated row j=2 has gates (beta_E,z3,z7) and reaches b(2eps-eps²).

For E=15 set z=0 and w4=w10=eps. Observed row j=5 isolates source i=5 with gates (beta_E,z4,z10) and reaches b(2eps-eps²).

The maximum over states and the maximum over a finite collection of views commute. The four exact extremizers therefore close the corresponding joint-view upper bounds. For eps>0, divide by eps and take eps→0 to obtain the sharp global Lipschitz constants. QED.

## Exact observation loss after dropping baseline

All four pairs overwrite original z0,z1 in both views. Two legal states differing only in z0 and/or z1 have the same two-view readout. For example, z=0 and w0=1 with all other w coordinates zero have ||z-w||_infinity=1 but d_F(z,w)=0. Therefore the full-state optimal inverse coefficient inf_{z≠w}d_F(z,w)/||z-w||_infinity is zero for every beta_N,beta_E and all four masks. This is a precise fiber of the specified reduced observer, not permission to erase these state coordinates: the unmodified observer and future operations can distinguish them. In contrast, the predecessor's positive inverse modulus applies to the three-view bank containing baseline.

## Evidence, reuse and next unit

VERIFY.py executes exact Python Fraction arithmetic for the original six-source observer, 1,200 extremizer checks on 4 pairs × 5² beta choices × 6 radii × 2 views, 1,400 rational state-pair upper-bound checks and 1,400 exact hidden-coordinate checks. RUN_EVIDENCE.json is actual process output. The symbolic argument above establishes the continuum theorem; rational tests verify witnesses and implementation.

BRC reuse: REUSE_APPLIED (frozen branch/mixer/provenance and predecessor's two-gate TV coupling); COMPOSE_APPLIED (two-view family and isolated-source witnesses). No physical X6/time evolution inference or P000 change. Next: classify all remaining nine-coordinate observation fibers for interior beta; compare with three-view full reconstruction under a precisely declared noise/cost model.
