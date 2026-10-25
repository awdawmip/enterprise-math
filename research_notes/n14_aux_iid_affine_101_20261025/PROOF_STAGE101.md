# Stage101: exact real affine minimax interval (external finite iid, N=14)

**Status:** author exact-rational computation-assisted proof; not independently reviewed or native Result/CLAIM-admitted; not P000/X6/BRC/Heartbeat-native mathematics. This is an external iid auxiliary problem.

**Source pins read:** GLOBAL_KNOWLEDGE_V1 main@426dad34b4dd0bc8632b5b518af2d2e0c77d3957, Enterprise Math source main@85d742b2ea4a3611ffb1fb6748a730e8b3ef646a, P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, ACTIVE worldview and docs/PORTABLE_RESEARCH_PROTOCOL.md. Previous author Stage100 endpoint and code: research_notes/n14_aux_iid_affine_100_20261025/PROOF.en.md, CHECKER.py, certificate100.json.

## Scope and theorem

Observations in {0,1,2} are iid under P=(1/8,1/24,5/6) or Q=(1/12,1/12,5/6). Tests may depend on *complete ordered observation histories*, may randomize all decisions/stopping, and must stop by time 14. Set eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau); V14(alpha) is the minimum of max(tP,tQ) with eP,eQ<=alpha.

Start at the author-proved Stage100 point:

    alpha100=2586556142352106327/7450150876955541504
    V100=751869170025529135/58204303726215168
    s100=17567190885961211/20889600000000000.

**Theorem. For every REAL delta in**

    0 <= delta <= eta101=72291875/6467144858468352,

the exact minimax value is

    V14(alpha100+delta)=V100-(119052/47)*delta.

The sharp right endpoint of this supporting line is

    alpha101=152150366213667431/438244169232678912
    V101=44227501292577155/3423782572130304.

Sharpness here means that the **same** affine support line is not attained at any alpha>alpha101. Other later segments are not ruled out.

## 1. Global Bellman dual valid for all ordered-history policies

For a count state v=(n,a,b), where a=#symbol0 and b=#symbol1, the ordered-prefix likelihood ratio Q/P=2^(a+b)/3^a. Define K101=61236/47, lambdaP=57816/47=72+(8/9)K101, lambdaQ=K101, Gamma101=lambdaP+lambdaQ=119052/47. The exact backward Bellman value D(v) is the minimum of

    decide P: lambdaQ*2^(a+b)/3^a;
    decide Q: lambdaP;
    continue: 1+(1/8)*D(v+0)+(1/24)*D(v+1)+(5/6)*D(v+2), n<14.

The continue option is omitted at depth n=14. Because the iid conditional future and likelihood ratio depend only on v, induction yields for **every** arbitrary full-ordered-history randomized policy

    D(root) <= tP+lambdaP*eP+lambdaQ*eQ.

Hence for eP,eQ<=alpha,

    V14(alpha)>=D(root)-Gamma101*alpha.

Exact Fraction backward enumeration covers 680 count states and 1240 nonselected action comparisons: 1238 strictly positive gaps, 0 negative, 2 equal-action ties. Minimum positive gap is 42839/1949184. The ties are **only**

    A101=(12,6,2): continue vs immediately decide P;
    B   =(12,0,1): continue vs immediately decide Q.

The exact root is

    D(root)=4594969511561419789973/5149368988483977216
           =V100+Gamma101*alpha100.

Therefore the support line through Stage100 is a universal lower bound.

## 2. Genuine ordered first-hit masses and suffixes

Fix the Stage100 endpoint policy: at A101 continue, at B immediately decide Q with probability s100 (otherwise continue), elsewhere take the Bellman minimizer. Exact forward rational propagation confirms eP=eQ=alpha100, tP=V100 and preserves distinct ordered histories rather than replacing them with unordered words.

First arrivals:

    A101: 7383 ordered words,
          pA=1538125/65229815808, qA=1538125/185752092672.
    B:      12 ordered words,
          pB=48828125/725594112, qB=48828125/362797056.

Conditional suffix tuples (P error,Q error,P extra time,Q extra time,terminal ordered suffix count), when choosing CONTINUE at the named tied state and following all later strict Bellman minimizers:

    RA=(1/576,143/144,25/24,13/12,5);
    RB=(63/64,1/144,9/8,13/12,5).

The two first-hit cones are disjoint: A101 and B have the **same depth 12**, but different symbol-0 counts (six vs zero). One path cannot visit both, and there is no cross influence of their independent randomizations.

## 3. Feasible optimal primal continuum for all real parameters

Take an arbitrary REAL u in [0,1]. At A101 immediately decide P with probability u (otherwise continue). At B immediately decide Q with probability

    s(u)=s100+h*u,  h=4314133/87040000000

(otherwise continue). All other actions remain the unique Bellman minimizers. Let

    X=pA*RA.Perror        =1538125/37572373905408;
    Y=qA*(1-RA.Qerror)    =1538125/26748301344768;
    E=pB*(1-RB.Perror)    =48828125/46438023168;
    H=qB*RB.Qerror        =48828125/52242776064.

Disjoint first-hit cones give **exact** error identities

    eP-alpha100=-X*u+E*(s-s100);
    eQ-alpha100=+Y*u-H*(s-s100).

Their equality is equivalent to s=s100+h*u with

    h=(X+Y)/(E+H)=4314133/87040000000.

The common error becomes

    eP=eQ=alpha100+eta101*u,
    eta101=E*h-X=Y-H*h=72291875/6467144858468352>0.

Endpoint

    s101=s100+h=1033425075169483/1228800000000000

lies in (0,1), as does s100, so **all real u in [0,1]** define valid randomized policies. Every chosen action is a Bellman minimizer, hence

    tP+lambdaP*eP+lambdaQ*eQ=D(root);
    tP=V100-Gamma101*eta101*u.

The time difference tP-tQ is affine in u by disjointness, and its exact endpoints are strictly positive:

    u=0: 1137198023932879775/1862537719238885376;
    u=1: 66892673788070575/109561042308169728.

Thus tP>tQ throughout the **entire real interval**, so max(tP,tQ)=tP saturates the global Bellman lower bound. Substitution u=delta/eta101 proves the exact theorem for every real delta, not an extrapolation from finite tests.

## 4. Right sharpness of this exact supporting line

The randomized bounded stopping-policy space is a finite compact polytope, so a minimizing policy exists at each alpha. Suppose alpha>alpha101 attained this supporting line. Since lambdaP,lambdaQ>0, equality in the dual chain forces eP=eQ=alpha and only Bellman-minimizing actions on all reached histories. The full gap scan leaves exactly the A101 and B ties. Inside each count fiber, Q/P is constant and the iid conditional suffix laws agree, so any full-ordered-history dependent mixing has an equivalent *P-first-arrival weighted average* action probability u or s at that count state, preserving both errors and durations. The tied cones are disjoint, yielding the same two affine error equations. Equality of errors forces s=s100+h*u with u in [0,1], hence alpha=alpha100+eta101*u<=alpha101. Contradiction. The line cannot remain attained to the right.

## 5. Exact scope, independent author checking and next research front

Two locally EXECUTED independent author implementations of the declared model:
* CHECKER_STAGE101.py: Python standard-library Fraction backward Bellman, all 680 states/1240 comparisons, genuine ordered first-hit masses, suffixes, exact interval identities, tP-tQ endpoint tests, next-kink affine-gap certificate. Output certificate101.json: PASS.
* INDEPENDENT_ORDERED101.py: differently written bottom-up Bellman with **full unaggregated ordered-history DFS**, at u=0,1/2,1. EACH parameter: 1,083,634 ordered prefix node visits; 722,423 terminal histories; A=7383 first hits, B=12. All exact rational constraints PASS (independent101_certificate.json). Two author implementations are NOT independent Research Driver mathematical review.

**Stage102 dual-only candidate (no primal theorem):** Along lambdaP=72+(8/9)K for decreasing K, the first next kink is K102=96424629120/78169393, lambdaP102=91338977736/78169393, new critical A102=(5,0,2) continue/decide Q; B remains continue/decide Q. The checker fixes the optimal policy at the rational midpoint, verifies all 1240 action gaps are nonnegative at both rational endpoints, and therefore certifies no intervening switch along this fixed dual pencil (affine dependence). Ordered first hits, causal cone overlap, error balancing and Stage102 primal interval remain OPEN; see NEXT_TASK_PACKET_102.md.

Native gateway control query returned CONTROL_QUOTA and native em_session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Current owner, native CLAIM, formal Result and independent review are UNVERIFIED. GitHub publication of this author note is a durable evidence checkpoint, not native authority. No native P000 readout/embedding/provenance preservation map, and no BRC-native numerical execution, has been established.
