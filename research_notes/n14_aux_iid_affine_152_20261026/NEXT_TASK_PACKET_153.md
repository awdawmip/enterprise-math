# Stage153 — exact real primal interval OPEN; Stage153 dual candidate obtained

## Frozen model and authority

The *external auxiliary* ternary iid ordered-history sequential testing problem has horizon N=14, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). For M=(eP,eQ,tP,tQ) let V14(alpha)=min max(tP,tQ) subject to eP,eQ<=alpha. Read Stage152 author proof, executable verifier and certificate in this directory. No native P000/X6/Heartbeat representation, current Owner confirmation, session CLAIM, Result, or independent Driver acceptance is implied.

At the Stage152 proved right endpoint:

    alpha152 = 18373003413933759925/52808422392537808896
    V152     = 318745538371909741813/26404211196268904448
    K152     = 12844717560/36346217
    L152     = 12768141608/36346217

The dual-minimizing face has B=(11,0,1) Q/continue, Q-stop probability b=2686983670724537/2714624000000000 (interior), and W=(8,3,3) Q/continue, Q-stop probability w=1 (saturated).

## New exact author-scanned dual frontier (NOT a primal theorem)

Keep B's Q/continue equality. Treat W strictly Q-stop immediately beyond Stage152. Along the rational direction dK=-1 and dL=-112/129, the derivative at B of Q and continue is exactly -112/129; the former W continue-vs-Q gap opens with positive directional derivative 36346217/13866909696. Exhaustive rational action-gap directional scan over all N14 count states identifies the first new positive gap closure at

    t_star = 500973822/617885689
    R=(12,2,2), Q/continue tie.

Thus the candidate is

    K153=5994/17
    L153=5960/17
    H153(root)=79691642847444362851/310422953206480896.

A *fresh*, not merely linearly extrapolated, 680-state Bellman computation at (K153,L153) obtains exactly two ties, B=(11,0,1) Q/C and R=(12,2,2) Q/C, with 1238 positive nonminimal gaps, minimum 71917/33841152 and zero negative gaps.

The exact directional scanning method is: at K152,L152 select Q at B and W, propagate rational Bellman derivatives under selected actions, verify B's two derivatives equal and W's Q-side derivative favored; for every positive gap g with strictly negative derivative dg find -g/dg, and take the exact minimum. Confirm the computed candidate with a fresh backward Bellman recurrence. This is only a dual candidate; it does NOT establish primal feasibility or right sharpness.

## First unanswered scientific unit

1. Compute the actual ordered *first-hit* prefix count and positive rational P/Q masses of B and R under all strict Stage153 Bellman decisions. R has a=2 at depth12 whereas B has a=0 at depth11; B might reach R, so DO NOT assume disjoint cones from monotonicity alone. Check ancestor relations using actual reached prefixes.
2. Compute four exact rational observer corners M(b,r) for Q-stop coins at B and R via backward Fraction recursion and independent literal ordered-prefix integer DFS. Determine whether an interaction term exists. If B->R occurs, preserve the conditional suffix interaction instead of forcing an affine square.
3. Solve eP=eQ with the actual (possibly bilinear) observer surface, identify every legal parameter interval, check whether tP remains the maximizing time, and verify Bellman dual equality and right sharpness for ALL real alpha in any asserted segment. If impossible, report an exact obstruction, not a guessed segment.
4. Preserve fixed P000/ACTIVE and BRC ordered-branch semantics. A native Source CLAIM and independent review require separate actual authorization; GitHub author notes do not substitute them.

## Inputs and execution provenance

GLOBAL_KNOWLEDGE_V1 canonical read snapshot for Stage152: main@43639a1bd021e9c6e90e699fbb7b5021855fbef7.
Enterprise Math base source main at Stage152 start: b3d16cec31ce33651cf8702e2e00847b9e3da3ca.
Exact preceding proof/checker/certificate in current Stage152 directory. The additional directional scan was actually executed in a local Python 3 Fraction program using the Stage152 recursion. It has not been independently Driver-reviewed or native-published. The project Source native control read returned CONTROL_QUOTA; session_start denied static_machine_readonly (operation_sent=false). Do not invent or adopt another owner.
