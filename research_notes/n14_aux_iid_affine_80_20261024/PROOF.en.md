# N=14 auxiliary iid discrimination: exact 80th optimal affine segment

Date: 2026-10-24. Status: **author-level exact finite-model proof, unreviewed**. This does not assert native BRC/X6/Heartbeat equivalence, native CLAIM, independent Driver review, Lean formalization or P000 promotion.

## Pinned model and inherited frontier

Ordered-history randomized sequential tests on iid symbols 0,1,2; P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), N=14. Errors eP=P(decide Q), eQ=Q(decide P); times tP=E_P(T), tQ=E_Q(T). Define V14(alpha)=inf max(tP,tQ) for eP,eQ<=alpha.

Source predecessor: enterprise-math main at 238626c2bb75a51b843c3cb3e1af56c60a30e530, exact stopping table in research_notes/n14_aux_iid_affine_79_20261024/verify_n14_79.py. Freeze its A79=(8,4,0) to P; retain B=(12,0,1) as the balancing coin. Endpoint data from stage79:

    alpha79=5171970272373679493/14900301753911083008
    V79=3068302372712437543/232817214904860672
    s79=24255210254075761/41779200000000000.

**Theorem.** For EVERY real 0<=delta<=eta80, where

    eta80=60528125/19960323637248,
    Gamma80=49844768/8301,

we have V14(alpha79+delta)=V79-Gamma80*delta. Thus

    alpha80=304236203316287029/876488338465357824,
    V80=180239004423178679/13695130288521216.

The indicated Bellman supporting line is sharp on the right: it is unattainable at alpha>alpha80.

## Exact global dual

At z=(n,a,b), the likelihood ratio Q(word)/P(word)=2^(a+b)/3^a. Let L=tP+lambdaP*eP+lambdaQ*eQ, where

    K80=lambdaQ=8690664/2767,
    lambdaP=72+(8/9)*K80=23772776/8301,
    Gamma80=lambdaP+lambdaQ=49844768/8301.

P-normalized action costs are: stop P: lambdaQ*2^(a+b)/3^a; stop Q: lambdaP; continue: 1+(1/8)D(child0)+(1/24)D(child1)+(5/6)D(child2) when n<14. Fraction-exact backwards comparison checks all 680 count states, 1240 nonchosen actions: 1238 strictly positive gaps, 0 negative gaps, exactly TWO zero gaps at B=(12,0,1), continue/Q and A80=(7,0,2), continue/Q. Smallest positive gap=3364539239/148719919104. At the root,

    Droot=476885545810844786863579/227366553050029228032
         =V79+Gamma80*alpha79.

The same P/Q likelihood ratio and suffix distribution hold for any ordered words with a given count state. Thus the Bellman bound covers ALL ordered-history randomized tests. For any feasible test Droot<=L<=max(tP,tQ)+Gamma80*alpha and hence V14(alpha)>=Droot-Gamma80*alpha.

## Positive first-hit BRC branches and suffixes

All C(7,2)=21 nominal ordered words first reach A=(7,0,2), with exact positive weights pA=21875/1492992, qA=21875/373248. B=(12,0,1) has 12 first-hit histories, pB=48828125/725594112, qB=48828125/362797056. The inherited continuation suffix quadruples (P-error,Q-error,additional P-time,additional Q-time) are

    RA=(56451961/56623104,2285/3981312,3410317/2359296,1257859/995328)
    RB=(63/64,1/144,9/8,13/12).

Independent organized ordered-word DFS enumerates 119 suffix terminal words at A across 26 terminal states, so immediate stopping at A truncates exactly 21*119=2499 prior complete histories. At B there are 5 suffix terminal words across 5 states, yielding 12*5=60 former complete histories. Word counts and positive probability weights are separately retained.

The two randomization cones are disjoint: A has (n,b)=(7,2), B=(12,1); b never decreases. B cannot precede A, and A cannot precede B. Hence their coin effects have no mixed term and all risks/times are affine in both coins.

## Attainment by two coins

At A stop Q with probability u, otherwise continue. At B stop Q with probability s, otherwise continue. Put

    X=pA*(1-RA.Perror)=3743753125/84537841287168
    Y=qA*RA.Qerror=49984375/1486016741376
    E=pB*(1-RB.Perror)=48828125/46438023168
    H=qB*RB.Qerror=48828125/52242776064.

Relative to u=0,s=s79, the changes are

    Delta eP=X*u+E*(s-s79)
    Delta eQ=-Y*u-H*(s-s79).

Equality of errors is uniquely restored by

    s=s79+h80*u,
    h80=-(X+Y)/(E+H)=-170743041/4352000000,
    eta80=X+E*h80=-Y-H*h80=60528125/19960323637248,
    s80=s79+h80=1330357474145633/2457600000000000.

Both s79 and s80 are strictly inside (0,1). Exact forward evaluation yields eP=eQ=alpha79, tP=V79 at u=0 and eP=eQ=alpha80,tP=V80 at u=1; tP-tQ respectively equals

    2186055790582274861/3725075438477770752 > 0
    139577535183427933/219122084616339456 > 0.

By cone disjointness, the four observables are affine for EVERY REAL u in [0,1]; the positive time gap survives, errors equal alpha79+eta80*u, and all selected actions Bellman-minimize. Hence L=Droot and tP=V79-Gamma80*eta80*u attains the global bound on the whole real interval.

## Sharp right endpoint

Any policy attaining that same supporting line above alpha80 must have equality at every dual step. Since the only action ties are A and B, all positive-probability histories choose fixed Bellman-minimizing actions elsewhere. At a tie state any arbitrary history-specific randomization reduces to an effective P/Q-compatible coin because likelihood ratios and conditional suffix risks coincide at fixed counts. Thus u,s are in [0,1], and equality of the two errors forces s=s79+h80*u, so alpha=alpha79+eta80*u<=alpha80, contradiction. This is sharpness of this LINE, not a claim that V14 fails to exist beyond the endpoint.

## Scope, reproducibility, next frontier

The exact rational backward/forward checker and separate ordered-word DFS crosscheck use the same inherited stopping table and are both author-side, not independent Driver reviews. The computation is finite and exhaustive for this declared auxiliary model only. No native X6 embedding, observer-preservation theorem, Heartbeat dynamics or BRC arithmetic-transfer conclusion is asserted. Native activity Owner/CLAIM remains unverified after CONTROL_QUOTA and STATIC_READONLY_SCOPE_DENIED.

At endpoint A80 is fixed to Q. The next *candidate only* is K81=46656/17 at A81=(11,3,3), continue/Q. Full stage81 interval remains open; see NEXT_TASK_PACKET_81.md.
