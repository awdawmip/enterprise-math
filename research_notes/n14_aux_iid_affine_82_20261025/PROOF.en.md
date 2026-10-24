# N=14 auxiliary iid — exact 82nd affine optimal segment

2026-10-25. **Author-level finite auxiliary model proof**; neither a native X6/Heartbeat theorem nor an independent Research Driver review. Predecessor: `awdawmip/enterprise-math@a08886fc5fd0f02a508c5d9a8ff9a9733bc08d9f`, stage81 proof and inherited stopping table.

## Exact statement

For any randomized ordered-history test with i.i.d. P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), horizon 14, denote eP=P(decide Q), eQ=Q(decide P), tP=E_P T, tQ=E_Q T and V14(alpha)=inf{max(tP,tQ):eP,eQ<=alpha}. The inherited endpoint is alpha81=304236249079487029/876488338465357824, V81=180235246120378679/13695130288521216, balancing stop-Q coin B=(12,0,1) with s81=1329243902945633/2457600000000000. The earlier stage81 A81=(11,3,3) is now deterministic Q.

**Theorem:** For every REAL 0<=delta<=eta82=6009805/1241691812825923584,

    V14(alpha81+delta)=V81-(6137299512/1201961)*delta.

Right endpoint alpha82=5172016234423397153/14900301753911083008 and value V82=6127998356585438501/465634429809721344. This supporting line is sharp on the right.

## Bellman global lower bound

At count-state (n,a,b), a zeros/b ones, Q/P likelihood ratio is 2^(a+b)/3^a. Choose lambdaQ=K82=3203342640/1201961, lambdaP=72+8*K82/9=2933956872/1201961, Gamma82=6137299512/1201961. P-normalized stopping costs are stop P: lambdaQ*2^(a+b)/3^a, stop Q: lambdaP; continuing (n<14) costs 1+D(child0)/8+D(child1)/24+5*D(child2)/6. Exact backward minimization has 680 states, 1240 nonselected comparisons, 1238 strictly positive gaps, no negative gaps, and exactly TWO ties: A82=(9,7,2), C/P; B=(12,0,1), C/Q. Minimum positive margin 139049/4807844. Root

    Droot=235131708769327545855619883/131688099973769994436608
         =V81+Gamma82*alpha81.

Because conditional laws and likelihood ratio are constant on each ordered-prefix count fiber, this Bellman recursion lower-bounds all history-dependent randomized strategies:

    Droot<=tP+lambdaP*eP+lambdaQ*eQ<=max(tP,tQ)+Gamma82*alpha.

## Exact BRC ordered path evidence and primal equality

A82 has 36 nominal ordered prefixes but only 20 live first hits; pA=5/301989888, qA=5/1289945088. At B all 12 nominal prefixes are live; pB=48828125/725594112, qB=48828125/362797056. Under continuation from each state, the exact quadruple (conditional P-error, conditional Q-error, extra P-time, extra Q-time) is

    RA=(35213/7962624,244067/248832,382601/331776,27271/20736),
    RB=(63/64,1/144,9/8,13/12).

Independent ordered DFS enumerates 53 terminal suffix words/17 terminal decision-state classes at A, so immediate stopping there truncates 20*53=1060 full words; B has 5 terminal suffix words (12*5=60). Ordered word counts are not substituted for their exact P/Q masses.

At A immediately decide P with probability u and otherwise continue. At B decide Q with probability s and otherwise continue. The action cones do not intersect: B is later (n=12>9), while every descendant of A has a>=7 and cannot be B with a=0. Hence risks and sample times are AFFINE in u and s without any mixed term. Define

    X=pA*RA.Perror=176065/2404631929946112,
    Y=qA*(1-RA.Qerror)=23825/320979616137216,
    E=pB*(1-RB.Perror)=48828125/46438023168,
    H=qB*RB.Qerror=48828125/52242776064.

Exact errors change by Delta eP=-X*u+E*(s-s81), Delta eQ=Y*u-H*(s-s81). Error equality forces

    s=s81+h82*u, h82=(X+Y)/(E+H)=155080591/2088960000000000.

The common increase is eta82=-X+E*h82=Y-H*h82=6009805/1241691812825923584. At u=1, s82=7532383150562527/13926400000000000, with 0<s81<s82<1. Exact endpoint forward recursion gives the theorem's alpha82/V82 and tP-tQ positive at both endpoints:

    start 139656202124227933/219122084616339456,
    end   791385134454226187/1241691812825923584.

All observables are jointly affine, so for EVERY real u∈[0,1] we obtain eP=eQ=alpha81+eta82*u, tP>tQ and tP=V81-Gamma82*eta82*u. Bellman-minimizing actions thus achieve the global lower bound throughout the entire interval.

## Right sharpness, limits and successor

If alpha>alpha82 attained this dual line, strict positive lambdaP,lambdaQ force eP=eQ=alpha and all used actions Bellman-optimal. Only ties A/B may randomize. At any count state, prefix words have common likelihood ratio and same P/Q weight per ordered word, allowing history-varying tie decisions to average into effective u,s. Their disjoint cones force s=s81+h82*u and alpha<=alpha82, contradiction. Finite-horizon randomized policy space is compact; nonattainment excludes equality to the right.

The two author exact checkers share inherited stopping rules. Source publication/readback is not remote checker execution or independent review; formal native CLAIM/Result, Lean certificate and transfer to genuine BRC/X6/Heartbeat dynamics remain unverified. After fixing A82 to P, the **UNPROVED** next candidate is K83=246614868/98923, A83=(8,4,4), continue versus Q.
