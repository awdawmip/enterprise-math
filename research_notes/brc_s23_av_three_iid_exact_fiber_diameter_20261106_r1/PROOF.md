# S23 conditional AV: three shared-parameter IID trials, exact fiber diameter and certified deficiency bounds

Date: 2026-11-06. Author-side analytic proof, exact rational checks executed; independent review pending. Frozen scientific input enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Source formulas and n=1,n=2 results reused from Draft PR #1777@a8b13eb9b5f4fad53663f7d93b808ae181bdf547.

## Statement and scope

Let a,c range over the full real box [1/2,7/8]^2. Write z=(1-a)c, u=1-a-z. The complete conditional AV law is A=(a,z,u) on stops (1,3,4), and the compressed third-stop-indicator law is B=(z,1-z) on (Y,N). Three observations are conditionally independent GIVEN ONE shared unknown (a,c), and a uniform reconstruction L is independent of those parameters:

    delta_3 = inf_{row-stochastic L: {Y,N}^3 -> {1,3,4}^3}
              sup_{a,c} TV(A(a,c)^tensor3, B(a,c)^tensor3 L).

NEW THEOREM: The maximum total-variation diameter among full three-trial laws with indistinguishable compressed observations is exactly 5211/10976, attained at (a,c)=(1/2,1/2) and (5/7,7/8), both with z=1/4. Consequently

    5211/21952 <= delta_3 <= 99/343.

The upper bound is attained as a VALID uniform error guarantee by the explicitly specified kernel L_3=L_2 tensor L_1; it is not claimed optimal. These are auxiliary conditional-AV statistical observer quantities, not yet the original ten-label S23 R_beh(k,10).

## Proof: all-real fiber diameter

The legal range of z is [1/16,7/16]. At fixed z, the EXACT feasible a interval, derived from c=z/(1-a) in [1/2,7/8] and a in [1/2,7/8], is

    l(z)=max(1/2,1-2z),    h(z)=min(7/8,1-8z/7).

For any a in this interval, one has a>=2(1-z)/3 (for z<=1/4 use a>=1-2z; for z>=1/4 use a>=1/2). Equivalently u=1-z-a<=a/2.

For an ordered three-trial outcome containing i first stops, j third stops and k fourth stops, i+j+k=3, its probability is a^i z^j u^k. Fix z and vary a. If k=0 and i>=1 the probability increases in a. If k>=1 it is nonincreasing: when i=0 this is immediate, otherwise its derivative has the sign of i*u-k*a<=2u-a<=0, since i<=2,k>=1. All-third probability z^3 remains unchanged. Thus all ordered outcome probabilities have consistent signs of their differences between ANY two a0<=a1 along the fiber. The positive differences consist precisely of zero-fourth outcomes with at least one first stop. Summing them gives EXACTLY

    TV(A(a0,z)^tensor3,A(a1,z)^tensor3)
       = (a1+z)^3 - (a0+z)^3.

This is maximized at the legal fiber endpoints a0=l(z), a1=h(z). Hence the all-fiber maximum reduces to max_z D(z), where D(z)=(h(z)+z)^3-(l(z)+z)^3. The three exact pieces are:

    [1/16,7/64]:  D=(7/8+z)^3-(1-z)^3.
    [7/64,1/4]:   D=(1-z/7)^3-(1-z)^3.
    [1/4,7/16]:   D=(1-z/7)^3-(1/2+z)^3.

On the first interval D'=3(7/8+z)^2+3(1-z)^2>0. On the middle interval D'=3(1-z)^2-(3/7)(1-z/7)^2>0 because 1-z>=3/4 and 1-z/7<=1 imply (1-z)^2>=9/16>1/7>=(1-z/7)^2/7. On the last interval D'=-(3/7)(1-z/7)^2-3(1/2+z)^2<0. Therefore the GLOBAL maximum lies at z=1/4, where l=1/2, h=5/7:

    max D(z)=(27/28)^3-(3/4)^3=5211/10976.

Both extremal pairs obey c in [1/2,7/8]. They yield identical B and hence identical B^tensor3. Any single parameter-independent reconstruction produces the same Q under both; the TV triangle inequality gives

    5211/10976 <= TV(A0^tensor3,Q)+TV(Q,A1^tensor3)
               <= 2 sup_{a,c} TV(A^tensor3,B^tensor3 L).

Taking the infimum over L gives the universal exact lower certificate 5211/21952. QED.

## Proof: a constructive universal upper bound

Previously verified author-side theorems supply two FIXED rational row-stochastic kernels with uniform inequalities on the SAME box:

    TV(A,B L1)<=9/70,
    TV(A^tensor2,B^tensor2 L2)<=9/49.

For completeness L1(Y)=(0,1,0), L1(N)=(88/105,0,17/105). L2 acts on binary pair YY, YN, NY, NN, assigning six exchange-orbit masses in order 11,(13/31),(14/41),33,(34/43),44:

    YY    (0,0,0,1,0,0)
    YN/NY (0,11/21,1/4,0,5/28,1/21)
    NN    (340/441,2/21,59/441,0,0,0).

Each doubleton output orbit is split evenly over its two ordered outputs. This is the explicit 4x9 kernel at the n=2 exact theorem in PR #1777. Let L3=L2 tensor L1: use L2 for binary trials 1-2 and L1 for trial 3. Under one shared (a,c), the reconstructed law is (B^tensor2 L2) tensor (B L1). Independent maximal coupling of two pairs of probability laws gives the standard finite-space inequality

    TV(P tensor Q,P' tensor Q') <= 1-(1-TV(P,P'))(1-TV(Q,Q')).

Applying the prior certified bounds pointwise and then uniformly,

    TV(A^tensor3,B^tensor3 L3)
      <= 1-(1-9/49)(1-9/70)=1-(40/49)(61/70)=99/343.

Thus delta_3<=99/343. QED.

## Executed exact verification and research continuation

The locally executed Python standard-library Fraction checker verified the rational extremal fiber outcome enumeration, 102 rational legal fibers and 1,020 within-fiber pairs, 81 legal parameter values of the 6x27 tensor-kernel reconstruction, and the exact theorem constants. The saved VERIFY.py is an equivalent compact reproducible checker of this theorem, with actual saved output in RUN_EVIDENCE.txt; the ALL-REAL proof is the sign/derivative argument above and prior n=1/n=2 exact upper certificates, not finite-grid inference.

This identifies a precisely typed BRC branch-observer residual: observing only third-stop indicators hides a family of stop1/stop4 allocations, and three trials expose a sharp full-output fiber separation 5211/10976. Scientific input is frozen; P000, six-dimensional X6 ontology, the separate parameter b and source provenance remain unchanged. The legal six-source/ten-label decoder/encoder bridge remains an open independent mother-model task.

NEXT: improve the upper bound with a genuinely joint 8x27 kernel and matching all-real certificate; or prove a larger multi-hypothesis lower bound to establish delta_3 exactly. Independently test legal transfer to ten-label S23 R_beh(k,10), k=4,6. Author source publication is not formal task CLAIM, review or admission.
