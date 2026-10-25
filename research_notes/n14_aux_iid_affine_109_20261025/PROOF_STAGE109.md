# Stage109 — exact Bellman support interval, external ternary iid N=14

**Status:** author-level exact finite-model proof and two exact author-side checks. Not a native CLAIM/Result, independent Research Driver acceptance, P000/X6/Heartbeat theorem, or verified bridge.

Sources: GLOBAL_KNOWLEDGE_V1 canonical main@babff194f059aaaa452e7827f815845aefcb647a (P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc); Enterprise Math initial main@f651ea40d12cee192ecab1bc741f98f1a9e01892, Stage108 author proof and certificate. These pins are distinct.

## The theorem

For ordered ternary iid histories with P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), horizon tau<=14, allow all randomized history-dependent stopping and terminal decisions. Define eP=P(decide Q), eQ=Q(decide P), tP=E_P tau, tQ=E_Q tau and V14(alpha)=min max(tP,tQ) with eP,eQ<=alpha.

The Stage108 author-proved endpoint is

    alpha108 = 13084095824621807507/37682150988866125824
    V108 = 1934483126570299962385/150728603955464503296.

For **every real** 0<=delta<=23181244375/130840802044674048,

    V14(alpha108+delta) = V108 - (957523557/506348)*delta.

In particular,

    alpha109 = 13084102500820187507/37682150988866125824
    V109 = 1934432626777903782385/150728603955464503296.

This supporting line is **unattainable for alpha>alpha109**, so the right endpoint is sharp.

## Bellman proof

For count-state z=(n,a,b), the ordered-prefix likelihood ratio is R(z)=2^(a+b)/3^a. For dual multipliers K,L>0, backward induction on all 680 count states uses

    H(z)=min{K*R(z), L, 1+sum_j P_j H(child_j)}

with continuation removed at n=14. Although H depends only on counts, the resulting lower bound applies to **every** ordered-history randomized policy:

    H(root) <= tP + L*eP + K*eQ <= max(tP,tQ)+(K+L)*alpha.

At the Stage108 endpoint C=(11,5,4) has saturated immediate-Q stopping. Preserve the A=(10,3,0) P/continue tie on the exact two-multiplier face

    L=-185064/635+(21376/17145)*K.

The next gap root along decreasing K is

    K109=491857029/506348
    L109=116416632/126587
    Gamma109=957523557/506348
    D=(10,3,3): immediate Q / continue.

At K109 precisely A (P/continue) and D (Q/continue) tie. Exact bottom-up enumeration: 680 states, 1240 nonchosen-action comparisons, 1238 strictly positive, 0 negative, 2 equalities, min strict positive gap 20261/759522. The root Bellman dual equals

    H109(root)=1160567907474457192913899/1733625457833035169792
              = V108 + Gamma109*alpha108.

The fixed policy that continues at A and D and uses every other selected action has nonnegative action gaps at both K108 and K109. Every such fixed-policy gap is affine in K on the face, so it remains nonnegative for the connecting segment.

## Ordered first hits and forced suffixes

Force continuation at A and D and otherwise follow the strict Bellman actions. Exact first-hit count, P-mass and Q-mass:

    A: 120 ; 390625/5971968 ; 390625/20155392
    D: 2051 ; 1281875/9172942848 ; 1281875/3869835264.

The conditional forced-continue tuple (P-error,Q-error,additional P-time,additional Q-time,ordered terminal suffix count) is

    A: (635/165888, 10201/10368, 7711/6912, 1069/864, 21)
    D: (4075/4096, 31/20736, 1955/1536, 75/64, 15).

Thus 2520 and 30765 complete ordered histories, respectively, are replaced by immediate stops. A and D are at depth 10 with distinct count vectors, hence their path cones are disjoint. At depth 11, previously saturated C=(11,5,4) is not a one-step descendant of either A or D. No cross-mixing term is hidden.

## Exact primal family and optimality for all real alpha

At A stop and decide P with probability u, otherwise continue; at D stop and decide Q with probability w, otherwise continue. The Stage108 endpoint has w=0 and

    u108=159404052982303/211315200000000.

Relative to that endpoint, the exact error changes are

    eP-alpha108 = x*(u-u108)+zP*w
    eQ-alpha108 = y*(u-u108)+zQ*w
    x=-248046875/990677827584
    y=65234375/208971104256
    zP=8973125/12524124635136
    zQ=-39738125/80244904034304.

Balancing eP=eQ gives

    u(w)=u108+(22757603/10565760000)*w
    alpha(w)=alpha108+(23181244375/130840802044674048)*w
    0<=w<=1.

The right endpoint has u(1)=159859205042303/211315200000000<1, so D saturates at w=1 before A does. Exact root moment recurrences at w=0,1/2,1 give eP=eQ=alpha(w), tP=V108-Gamma109*(alpha(w)-alpha108), and tP>tQ; at the right endpoint

    tQ=115034081136642114605/9420537747216531456.

Since the two cones are disjoint, all four root moments are affine in w; verifying their exact endpoint identities proves these properties for **every real** w in [0,1], not merely three grid points. The constructed policy uses only dual-minimizing actions and therefore attains the global Bellman lower bound throughout the entire real interval.

## Sharpness against arbitrary history-dependent randomization

If the same supporting line attained V14(alpha) at alpha>alpha109, positivity of both K and L would force eP=eQ=alpha and every positive-mass history to use only Bellman-minimizing actions. All strict actions are therefore forced; randomness can occur only at A and D. Their within-state prefix likelihood ratios and conditional suffix moments are constant. Averaging any history-dependent stop probabilities with the first-hit P mass therefore reduces every such policy to effective u,w in [0,1], even without count-based randomization. Their cones are disjoint, so the displayed affine error identities are necessary; eP=eQ implies alpha=alpha108+eta109*w<=alpha109. Contradiction. The policy polytope has finitely many history nodes and is compact, so the infimum is attained and the supporting line is genuinely sharp.

## Evidence, scope, next step

Exact Python Fraction checks executed: full 680-state Bellman, all 1240 comparisons, first-hit path probabilities, conditional suffixes, endpoint/midpoint moments. Separate top-down memoized Bellman and literal ordered-history DFS visited 995728 nodes at w=0 and 1/2, 952657 at w=1, and reproduced every moment. Both are **author-side**, not independent Driver review. BRC-compatible positive rational branch mass and ordered-provenance retention were applied; no typed native Heartbeat/BRC-Shor numerical operation or native correspondence was asserted.

**Next dual-only candidate:** After D is fixed immediate Q, the first additional gap root is K110=6497577/6734, L110=3069240/3367, Gamma110=1805151/962 at E=(13,6,4), competing immediate Q. Stage110 primal feasibility/overlap/affine segment is **not proved**.

Connected GitHub login awdawmip was verified. Native control task query returned CONTROL_QUOTA; native session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. No active native owner/CLAIM/Result or independent Driver acceptance was verified.