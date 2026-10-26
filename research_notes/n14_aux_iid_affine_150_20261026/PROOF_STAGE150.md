# Stage150 — exact full-real N=14 ternary iid optimal affine segment

Evidence: author-level exact finite computation-assisted proof, NOT independently reviewed, NOT a native CLAIM or Result, and NOT a theorem of P000, Heartbeat World or X6 dynamics.

## Exact statement

Given P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), horizon N=14, and arbitrary randomized decisions on COMPLETE ORDERED symbol histories, let eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau), and V14(alpha)=min max(tP,tQ) subject to eP,eQ<=alpha.

For EVERY REAL 0<=delta<=13860171875/12892681248178176,

    V14(alpha149+delta)=V149-(88912/121)*delta,

where alpha149=6124245464096172775/17602807464179269632 and V149=106280162016260661671/8801403732089634816. The exact right endpoint is

    alpha150=18372793163552518325/52808422392537808896
    V150=318819628004877985013/26404211196268904448.

The corresponding affine Bellman support is STRICTLY below V14(alpha) for all alpha>alpha150 (right-sharp support).

## Exact dual and earliest closure

At a state s=(n,a,b), counting the first two symbols, Q(prefix)/P(prefix)=2^(a+b)/3^a for EVERY ordered history with those counts. For positive K,L let

    H(s)=min{ K*Q(prefix)/P(prefix) [decide P], L [decide Q],
             1+sum_i P_i*H(next_i(s)) [continue] },

where continuation is absent at depth 14. Backward induction covers all 680 count states. It bounds ALL complete-history policies (not merely count-based policies), since suffix laws and likelihood ratios depend only on the counts. Consequently

    H(root)<=tP+L*eP+K*eQ<=max(tP,tQ)+(K+L)*alpha.

Start with K149=100164600/266527, L149=98815768/266527. Fix B=(11,0,1) on its Q/continue tie and saturated G=(11,7,3) at P-stop. B continuation has (constant,K,L) coefficients (239/192,7/288,1493/1536), so the tie-preserving dual ray is (dK,dL)=(-1,-112/129). The G continue-minus-P gap grows at strictly positive slope 266527/81251424. A complete exact rational scan of every nonchosen action gap on all 680 states yields the FIRST positive closure

    t*=202961376/32249767, at R=(13,5,2), P/continue.

The dual at this first closure is K150=44712/121, L150=44200/121, and its fresh exact Bellman evaluation gives

    H150(root)=1183067867036626543351/4418962039762845696.

Exactly two states tie: B=(11,0,1), Q versus continue, and R=(13,5,2), P versus continue. Across the finite Bellman state-action table there are 1238 strictly positive nonminimal gaps, minimum 607/29403, and ZERO negative gaps. All other actions are uniquely determined.

## Ordered provenance and observer decomposition

At B stop for Q with probability b, and at R stop for P with probability r; elsewhere take the unique strict Bellman minimizer. B is at depth 11 with 0 first-symbol occurrences, while R is at depth 13 with 5 first-symbol occurrences. B cannot lead to R in two steps, and R cannot lead backwards to B; their GENUINE ORDERED history cones are disjoint.

Literal ordered-prefix DFS with P integer symbol weights (3,1,20)/24 and Q integer weights (1,1,10)/12 gives first-hit data:

    B: 11 histories, P mass 107421875/1451188224,
       Q mass 107421875/725594112;
    R: 14662 histories, P mass 114546875/440301256704,
       Q mass 114546875/835884417024.

Both a rational backward four-observer recursion and independently structured integer-weight literal-prefix DFS agree on EVERY coordinate at all four deterministic (b,r) corners, including exactly zero four-vector mixed corner difference. Their DFS visits are 563974, 563842, 519988, 519856, in the corner order (0,0),(1,0),(0,1),(1,1).

With M=(eP,eQ,tP,tQ), the exact affine map M(b,r)=M00+b*dB+r*dR is

    M00=(1212667745012379235/3505953353861431296,
         224474522556365/641959232274432,
         5331415431779770717/438244169232678912,
         630124894153661/53496602689536);
    dB=(4619140625/2229025112064,
        -751953125/417942208512,
        -25673828125/278628139008,
        -17939453125/104485552128);
    dR=(-114546875/10567230160896,
        114546875/10030613004288,
        -114546875/440301256704,
        -114546875/835884417024).

These signed observer INCREMENTS are differences of positive P and Q branch masses, not negative BRC primitive mass.

## Attainment on the full real interval

The two errors are exactly equal if and only if

    b(r)=7957468505269291/8143872000000000
        +(3658169/636240000)*r.

For all real 0<=r<=1 this is a valid STRICTLY INTERIOR probability 0<b(r)<1. At r=0,

    eP=eQ=alpha149, tP=V149,
    tP-tQ=36781979277243213665/79212633588806713344>0.

At r=1, the R P-stop coin saturates first, B stays interior with b(1)=727663006224481/740352000000000, and

    eP=eQ=alpha150, tP=V150,
    tP-tQ=36808457207099213665/79212633588806713344>0.

The common error increases STRICTLY and affinely by eta150=13860171875/12892681248178176. At BOTH endpoints,

    tP+L150*eP+K150*eQ=H150(root).

All four observations are affine in r; errors stay balanced, tP>tQ, and the lower-bound equality holds at every intermediate real r. The optimal value decrement is exactly (K150+L150)*delta=(88912/121)*delta. This proves every real point in the stated segment, not merely rational sample points.

## Right-sharpness of support

On the finite ordered-history tree, the compact behavioral policy space has compact observer image, so minima exist. Suppose some alpha>alpha150 attained the SAME dual affine lower support. Because K150,L150>0, BOTH errors would equal alpha, and each reached history could use only Bellman-minimizing actions. Every strict state then has its unique action. At a tied count state, different ordered first-hit prefixes have the same likelihood ratio and identical conditional suffix law. History-dependent coins can therefore be replaced by one P-mass-weighted effective coin without changing the FOUR observers. Since the two cones are disjoint, every support-attaining policy has an M(b,r) in the square [0,1]^2. Error balance imposes the exact displayed b(r), whose common error cannot exceed alpha150. Contradiction. The support line is strictly suboptimal to the right; this makes NO prediction about the next value-function segment.

## Evidence and authority

The actual local author execution passed rational Bellman recursion and full directional-gap scan, 680 states, 1238 strict gaps, the ordered first-hit counts and masses, four deterministic corners evaluated by TWO distinct exact algorithms, mixed-term cancellation, balance, time-dominance and dual-attainment endpoints. VERIFY_STAGE150.py is the portable independent rerun artifact; certificate150.json records exact numeric evidence. The complete local author code, original logs and SHA256 inventory are preserved separately in a downloadable research package.

GLOBAL_KNOWLEDGE_V1 input snapshot fixed at canonical main@252fe47ffec83b449cfbbff70c59c19c0c2999a7; EM input main@1ee9151e3124246048e94ad7981e1e52752fef0e. Prior Stage149 author work is preserved at EM immutable commit 8916bf64a694927ce557a35ce71e34643a57b414, which DIVERGES from the observed canonical main (no false claim of Stage149 main integration). This Stage150 theorem rechecks the exact Stage149 endpoint with its new dual rather than assuming acceptance. P000 projection and canonical blob matched; the ACTIVE worldview and portable research protocol were read. GitHub principal awdawmip has write access; native control tasks returned CONTROL_QUOTA and native session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Therefore active owner, native CLAIM, Result and independent Driver acceptance remain UNVERIFIED; this is SOURCE-ONLY author research, not a Task takeover or native theorem.

Stage151 DUAL-ONLY candidate: K151=45154992/127757, L151=6412152/18251, tied B=(11,0,1) Q/C and U=(9,4,1) P/C, 1238 positive Bellman gaps. No Stage151 primal optimality result is claimed. See NEXT_TASK_PACKET_151.md.
