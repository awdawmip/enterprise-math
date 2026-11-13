# Exact AU+BU-provenance minimax in the 16-leaf BRC N=4 external model

**Date:** 2026-10-30. **Status:** AUTHOR_ANALYTIC_PROOF / EXACT_SYMBOLIC_AND_16_LEAF_CHECKED / UNREVIEWED / NOT_ADMITTED. This is a theorem conditional on the previously supplied finite dual-probability source and original instantaneous behavioral S2/S23 policy semantics, not a statement about the P000 native X6 world, an independent heartbeat/time dynamics, or a physically calibrated measurement.

## Input, observer, and result

Use the exact source and behavioral definitions in PR #1735, commit `6d9bc93c9d110418d22daf344ed83d883a4a1a23`, especially `OBSERVER_AU_REFINEMENT_NO_GO.md` and its 16-leaf source verifier. The four time-two Q masses are AU=1/6, AV=1/3, BU=1/4, BV=1/4; time-three P/Q child likelihood ratios respectively (9/10,11/10), (1/4,1/4), (1/5,9/5), (2,2), with each child split equally again into time-four leaves. All 16 P/Q leaves are strictly positive, both laws normalize to 1. The target F continues at time one with rates `a=961/1000`, `b=151/1000`, continues AU only at time two, stops at time three on AU with decision P, and stops elsewhere earlier with decision Q.

The *full declared observer* is `O'=(T,Decision,Z_BU,Z_AU)`; each source bit is 1 only when that source reaches T>=3. The class S2 requires equality of AU/BU conditional time-two action kernels; S23 adds equality of contemporaneous equal-likelihood-ratio node actions. These are instantaneous behavioral policies, not arbitrary latent-history couplings. Define `d'_i=inf_{G in S_i} max(TV_P(O'_F,O'_G),TV_Q(O'_F,O'_G))`.

**Theorem (exact, attained):**

    d'_2 = d'_23 = 71691/2414000 = 0.0296980115990057995...

This closes the earlier PR #1735 strict interval `[(7789-sqrt(50220529))/36000,151/4000]` without changing the observer, the tree, or the strategy class.

## Causal reduction inherited and checked at its exact scope

The earlier author's K' map sends any early stop to `(T,Q,0,0)` at the same T, and any T>=3 observation to `(3,Q,1,0)` if its BU bit is set and `(3,P,0,Z_AU)` otherwise. K' fixes the target in *both* source laws. Given any S2 behavioral G, preserving its first- and second-stage conditional continuation kernels and stopping at time three with decision Q on BU/P elsewhere realizes K' as a genuine S23 policy. The BU time-three likelihood-ratio set `{1/5,9/5}` is disjoint from the non-BU set `{9/10,11/10,1/4,2}`, so this decision is current-ratio-measurable. On the original full 16-leaf source, `Law_L(O'_(G^K))=K'_# Law_L(O'_G)` for each L=P,Q. Total-variation data processing gives a simultaneous improvement under both laws. Thus the optimizer can be sought in this collapsed S23 class, for which the following five-atom formulas are exact. This theorem *uses* that source reduction, and independent review of its behavior/observer semantics remains an admission obligation.

Put `A,B,c in [0,1]`: first-stage A/B continuation, and common **conditional** AU/BU continuation rate `c`. Let `U in [0,A]` and `V in [0,B]` be unconditional first-stage-weighted AV/BV continuation. Every such tuple is realized by a legal S23 policy, including zero-rate endpoints. With target-minus-candidate signs and the observable atom order `(1,Q,0,0),(2,Q,0,0),(3,P,0,1),(3,P,0,0),(3,Q,1,0)`, write

    s=(A-a+B-b)/2;        t=(A-a+3(B-b))/4;
    r=(a-Ac)/6;           H=Bc/4;
    N_P=U/12+V/2;         N_Q=U/3+V/4.

The *full* signed P/Q probability vectors are

    Delta_P=(t, H+N_P-t-r, r, -N_P, -H),
    Delta_Q=(s, H+N_Q-s-r, r, -N_Q, -H).

Direct summation of the 16 strictly positive leaves yields these identities (verified symbolically in `VERIFY.py`). The TV error for a law is half of its full five-atom absolute-mass sum, and equivalently the maximum absolute signed mass of any **observable event**.

## Four event bounds and two new simultaneous exact duals

Let `e=max(TV_P,TV_Q)`. All events used below are legitimate unions of actual observer atoms; no AU/BU source is projected away.

* The P-observable event `{(1,Q,0,0),(3,Q,1,0)}` has signed mass `t-H`, so `t>=H-e`.
* The Q-observable event `{(1,Q,0,0),(3,P,0,1)}` has signed mass `s+r`, so `s+r<=e`.
* The AU time-three atom has signed mass `r`, so `e>=r=(a-Ac)/6 >= (a-c)/6`, using `A<=1` and `c>=0`.
* The BU time-three atom has signed mass `-H`, so `e>=H=Bc/4`.

**Dual 1.** The first inequality expands to `A+(3-c)B>=a+3b-4e`. Since `A<=1` and `3-c>0`, this implies `(3-c)B>=d-4e`, where `d=a+3b-1=207/500>0`. Multiply by `c>=0`, use `Bc<=4e`, and rearrange exactly:

    4e(3-c) >= c(d-4e),
    hence e >= d*c/12.                                           (I)

**Dual 2.** The first inequality together with the Q event gives

    A+(3-c)B>=a+3b-4e,
    (3-c)A+3B<=2a+3b+6e.

Eliminate A. The factor `g(c)=(3-c)^2-3` is positive on `[0,1]`, and

    g(c) B >= a+6b-(a+3b)c-(18-4c)e.

Use `Bc<=4e`, multiply the inequality by `c>=0`, and combine:

    4e*g(c) >= c[a+6b-(a+3b)c-(18-4c)e],
    e >= f(c) := c[a+6b-(a+3b)c]/[6(4-c)].               (II)

There is no division by c, A, B, or a potentially zero mass. Both dual inequalities hold at all boundary points, for **every** legal real strategy.

## Exact covering of all real continuation rates

Define rational constants

    E*=71691/2414000,
    c*=1039/1207,
    c0=a-6E*=472427/603500.

Direct rational arithmetic gives `3/4<c0<c*<1`, and `d*c*/12=E*`. At the stipulated values of a,b,

    f(c)=c(1867-1414c)/[6000(4-c)],
    f'(c)=(707c^2-5656c+3734)/[3000(4-c)^2].

The derivative numerator has derivative `1414c-5656<0` on `[0,1]`, and its value at c=3/4 is `-1765/16<0`. Therefore `f` is strictly decreasing on `[3/4,1]`. Exact substitution gives `f(c*)=E*`. Now partition **every real c in [0,1]**:

1. `0<=c<=c0`: AU atom bound `e>=(a-c)/6 >= (a-c0)/6=E*`.
2. `c0<=c<=c*`: dual (II) and decreasing f give `e>=f(c)>=f(c*)=E*`.
3. `c*<=c<=1`: dual (I) gives `e>=d*c/12>=d*c*/12=E*`.

Hence all collapsed legal policies, and by K' data processing all original S2/S23 behavioral policies, satisfy `e>=E*`.

## Exact legal attainment

Choose the genuine S23 behavioral policy

    A=1, B=69/500, c=1039/1207, U=V=0,

with early decision Q and stop at time three, deciding P on AU/AV/BV and Q on BU. The common AU/BU time-two **conditional** continuation equals c. It is legal since `0<=A,B,c<=1`, `0<=U<=A`, `0<=V<=B`, and time-three decision is measurable from the disjoint current likelihood-ratio groups.

Direct summation of all 16 P/Q leaves gives *target minus candidate* observed signed vectors

    Delta_P=(0,13/1000,40309/2414000,0,-71691/2414000),
    Delta_Q=(13/1000,0,40309/2414000,0,-71691/2414000).

Both have zero sum and TV exactly `71691/2414000`; the universal lower bound is attained. QED.

## Source provenance, verification and remaining scope

The source's five-atom K' reduction, source-law definitions, original S2/S23 information sets and prior interval came from PR #1735 at immutable commit `6d9bc93c9d110418d22daf344ed83d883a4a1a23`; the present event-mask duals, real-c interval covering and rational matching strategy are **new to this deliverable**. Independently executed `VERIFY.py` rebuilds all 16 positive leaves for P and Q, symbolically derives both full five-atom signed vectors, validates the actual observable event masks and dual identities, checks derivative/root arithmetic, and exactly verifies both P/Q TV values of the attaining strategy. `VERIFY_EVIDENCE.txt` holds its console output. The proof—not sampled testing—covers continuous real policies. Observer time-four collapse is justified only within the declared current terminal observable and stop/decision semantics; a later T4-sensitive operation requires a fresh preservation theorem.

Frozen read authority for this authored calculation: GLOBAL_KNOWLEDGE_V1 canonical main `13c260412ff71512277f01b1de8beb92403c5924`; Enterprise Math main `dcfa196433e9b0dfe501e41345817aa4a91e5a77`; native P000 was read in that project snapshot. GitHub actor `awdawmip`; active native Owner returned `CONTROL_QUOTA` on attempted current control query; Site gateway reported `research_authority_granted=false`. These facts limit only task/state authority: this is a portable author-side proof, with no native CLAIM/Result, independent Driver review, or P000 bridge claimed. Do not silently promote this result to Working Truth/Foundation.
