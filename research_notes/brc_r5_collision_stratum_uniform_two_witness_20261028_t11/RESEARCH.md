# R5 — Two fixed witnesses exclude an entire likelihood-ratio collision stratum

**2026-10-28, portable mathematical author proof / finite exact computation.**
Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED.
Fixed GLOBAL_KNOWLEDGE input snapshot: awdawmip/chatgpt-global-knowledge main@e19534794cc19afce8f2c4651350e3c3bb30cb48.
Enterprise Math source input: awdawmip/enterprise-math main@c9a28fe95d621a2d1b9f22bb93f766a3eb739098, including research_notes/brc_r5_collision_strata_20261028_t11/RESEARCH.md and its verifier.

## Precise statistical observer (external model)

A sequential policy observing history h may stop and declare P or Q, or continue where allowed. The 4D observables are O=(e_P,e_Q,T_P,T_Q)=(P(declare Q),Q(declare P),E_P tau,E_Q tau). At time 1 a history is A or B; at time 2 it is AC, AL, BC, or BH, with AL and BH forced to declare at time 2; AC and BC may continue to time 3. Full policies may condition on all observed history. Seedless likelihood-ratio (LR) policies may condition only on the pair (time, P(h)/Q(h)); independent local behavioral randomizations are allowed, but a hidden persistent common random seed is not.

Six strictly positive branches, with P mass first, Q mass second:

| history | P | Q(epsilon) |
|---|---:|---:|
| AC low | 1/24 | 1/12 + epsilon |
| AC high | 1/8 | 1/12 - epsilon |
| AL side | 1/12 | 1/3 |
| BC low | 1/32 | 1/8 |
| BC high | 7/32 | 1/8 |
| BH side | 1/2 | 1/4 |

For ALL REAL epsilon in (-1/12,1/12) every leaf is strictly positive and both P,Q sum to 1. The two time-2 hidden histories AC and BC have different positive masses (1/6,1/6) and (1/4,1/4), but the identical LR signature 1. This **collision persists throughout the entire family**. Time-1 ratios A=1/2, B=3/2 and time-2 side ratios AL=1/4, BH=2 remain distinct. There are no other time-2 collisions.

Define signed support V_C(lambda;eps)=max_{O in O_C(eps)} lambda·O and loss Delta_lambda=V_full-V_LR.

## Uniform convex-hull exclusion theorem

Two integer signed support directions suffice:
lambda0=(912,456,128,-194), lambda1=(400,600,-88,34).

Exact support envelopes for EVERY REAL |epsilon|<1/12 are:

    V_full(lambda0) = max(868, 857+456 epsilon)
    V_LR(lambda0)   = max(857, 857+456 epsilon)

    V_full(lambda1) = max(1499/3-600 epsilon, 547, 533+600 epsilon)
    V_LR(lambda1)   = max(1496/3-600 epsilon, 547, 532+600 epsilon)

Consequently:

    max(Delta_lambda0(epsilon),Delta_lambda1(epsilon)) >= 9/44 > 0

and the constant is SHARP: at epsilon*=25/1056, both gaps equal 9/44. It follows that for each epsilon in the interval,

    conv(O_LR(epsilon)) != conv(O_full(epsilon)).

Thus no member of this entire strictly-positive collision-preserving one-parameter stratum solves the parent problem of hull-equal yet real-image-unequal strategy classes. Lambda0 alone stops separating at epsilon>=11/456, but lambda1 resumes separation already at epsilon>7/300.

## Exact proof of the support envelopes

Each deterministic policy assigns stop P, stop Q or continue at time 1 (A,B); actions P/Q/continue at AC,BC; mandatory P/Q at the two side leaves AL,BH; and mandatory P/Q to each of four time-3 C leaves. Therefore the full class has exactly 3^2*3^2*2^2*2^4=5184 deterministic decision descriptions (unreachable-action redundancies included). The relaxed LR class identifies the common action at both time-2 ratio-1 states AC and BC, leaving 3^2*3*2^2*2^4=1728 descriptions. A deterministic policy's score is exactly one affine function a+b epsilon because Q changes only in the AC low/high leaf pair. For a fixed lambda, compute each affine line using exact Fraction arithmetic at epsilon=0 and epsilon=1/48 (the latter only for coefficient extraction, not approximation).

On these descriptions the EXACT DISTINCT affine-line counts are:

| signed lambda | full lines | relaxed LR lines |
|---|---:|---:|
| lambda0 | 137 | 85 |
| lambda1 | 140 | 88 |

Every displayed candidate envelope line occurs in its respective finite set of policy-score lines. For each candidate envelope, find all intersections of its displayed lines inside [-1/12,1/12] by exact rational arithmetic and include both endpoints. At every breakpoint check every affine policy line is <= maximum candidate line there. Between successive breakpoints the maximum candidate envelope equals one fixed affine line; a competing affine line cannot rise above it without a positive endpoint. Hence finitely many rational endpoint checks establish the FOUR stated envelopes on the ENTIRE real parameter interval. The checked breakpoint tuples and exact code appear in VERIFY.py / EXACT_OUTPUT.txt. No floating-point extrapolation is used.

**Accidental time-3 LR collisions.** The relaxed LR enumeration permits different declarations at terminal C leaves even if their ratios accidentally match, which happens inside the interval at epsilon=-5/84,-1/24,1/84. But both chosen lambda vectors have positive first two coefficients lambda_P and lambda_Q. At a terminal leaf with masses (p,q), declaring Q contributes lambda_P p to the error objective and declaring P contributes lambda_Q q; time cost is unaffected by the declaration. A maximizing terminal action can therefore be chosen solely from p/q by comparing lambda_P(p/q) with lambda_Q, breaking ties uniformly. Equal LR terminal leaves thus have a common maximizing action and the relaxed LR optimum equals the **genuine** seedless LR optimum at every epsilon. Three collision values have been independently checked by exact fully-constrained enumeration.

**All real behavioral strategies.** Each time-LR information state is visited at most once on a sample path. Expected linear objective is multi-affine in each of the independent local behavioral probability vectors. Successively replacing each randomized local action by a best deterministic action never reduces the objective. Thus deterministic support maxima are valid for **all real seedless LR behavioral strategies** and all full behavioral strategies; there is no assumption of a finite randomization grid.

**Sharp 9/44 bound.** For epsilon<=0, Delta_lambda0=11. For epsilon>=0, algebra on the exact envelopes gives

    Delta_lambda0 = 11-456 epsilon on [0,11/456]; zero thereafter;
    Delta_lambda1 = 0 on [0,7/300];
                    600 epsilon-14 on [7/300,1/40];
                    1 thereafter.

The two nonzero moving margins cross at 11-456 epsilon = 600 epsilon-14, i.e. epsilon*=25/1056. At this point both equal 9/44. Their respective monotonicity and the neighboring constant branches prove the global uniform bound and its attainment. QED.

## BRC / Enterprise X6 typed interpretation and limitations

This is an **external statistical decision model** with an explicit observer/history map, not a proof about native Heartbeat World cell dynamics. Under current locked P000 the native carrier remains a six-axis integer Cell relational space and separately typed time, and a present-day three-dimensional research slice is only a layer inside X6 (not a native plane). History labels here may be injected as provenance labels for distinct X6 Cells with separately typed observer decision time, but no native evolution or physical calibration is inferred.

The applicable BRC interface is the six labeled positive-rational branch-weight histogram under each of P and Q. The observer quotient (t,full history)->(t,likelihood ratio) erases hidden A/B provenance at t=2; the two signed support probes detect downstream effects. Signed lambda components are **linear observer weights**, NOT BRC signed branch masses or a BRC-Shor numerical operation. The precise observer scope is only (e_P,e_Q,T_P,T_Q), not the entire trajectory law.

This is an author-proved analytic finite model theorem backed by exact standard-library Python verification; it has not received independent Driver mathematical review, Source CLAIM/Result admission or comprehensive external novelty review. Current connected native Enterprise Math status was CODE_REVIEW_REQUIRED, research_authority_granted=false, active-job quota 5/5; source owner and a live authorized claim were not established. This file is a neutral portable research artifact, not a self-awarded native role or formal checkpoint. P000 and ACTIVE worldview files were not changed.

Next discriminating research unit: see NEXT_TASK.md.
