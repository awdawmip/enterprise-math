# Stage100 — Exact affine minimax interval in a 14-step iid sequential test

**Status:** exact-rational author computation-assisted proof; independent Research Driver review, native Result admission and P000/X6 transfer **not established**. External auxiliary iid model only.

**Immutable sources read:** GLOBAL_KNOWLEDGE_V1 main 426dad34b4dd0bc8632b5b518af2d2e0c77d3957; Enterprise Math main 85d742b2ea4a3611ffb1fb6748a730e8b3ef646a; Stage99 source research_notes/n14_aux_iid_affine_99_20261025/PROOF_STAGE99.md (blob cbc1369d890e06121d328f301ca183e30dc9540f). P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Current portable protocol docs/PORTABLE_RESEARCH_PROTOCOL.md was read. P000 refers to six native spatial Cell dimensions plus separate time; no preservation map from this auxiliary model has been demonstrated.

## Theorem

Take independent observations in {0,1,2} with P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6). Tests may use the entire **ordered** history, randomize stopping/decisions, and must stop by time 14. Let eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau), and V14(alpha)=min max(tP,tQ) subject to eP,eQ<=alpha.

The verified author Stage99 baseline is

alpha99 = 2586555057332842327/7450150876955541504,
V99 = 751890958002985135/58204303726215168,
s99 = 17542569190345211/20889600000000000.

For **every real** delta satisfying

0 <= delta <= eta100 = 117732125/808393107308544,

the exact minimax value is

V14(alpha99+delta) = V99 - Gamma100*delta,
Gamma100 = 345840912/134551.

The new endpoint is

alpha100 = 2586556142352106327/7450150876955541504,
V100 = 751869170025529135/58204303726215168.

**Sharpness:** this specific supporting affine line cannot be attained for any alpha>alpha100; this is not a claim that no later affine segment exists.

## Bellman dual proof

Let v=(n,a,b), where a and b are the counts of symbols 0 and 1. For every ordered word with count state v, the likelihood ratio Q/P equals r(v)=2^(a+b)/3^a. Set

lambdaQ=K=177963480/134551,
lambdaP=167877432/134551=72+(8/9)K,
Gamma100=lambdaP+lambdaQ.

Define the exact backward value D(v) as the minimum of:
- decide P: lambdaQ*r(v);
- decide Q: lambdaP;
- continue: 1+sum_i P_i D(v+i), available only for n<14.

The exact-rational recursion checks all 680 count states and all 1240 comparisons with nonselected actions: 1238 strictly positive gaps, 0 negative gaps, and precisely 2 ties. The smallest strictly positive gap is 12889/807306. The only ties are A=(9,5,1), continue/decide P, and B=(12,0,1), continue/decide Q. The root value is

D(0,0,0) = 3336345672953513652547807/3685386950901636268032
         = V99 + Gamma100*alpha99.

At B=(12,0,1), the children after continuing use C at (13,1,1), Q at (13,0,2), and Q at (13,0,1). Following C at (13,1,1), exactly the terminal child (14,2,1) chooses P. Consequently the **analytic** B gap is

D_C(B)-D_Q(B) = 9/8 + K/72 - lambdaP/64 = 0

for lambdaP=72+(8/9)K. All remaining Bellman inequalities are verified in the exact checker, not inferred from this local formula.

Backward induction, including any full-ordered-history randomized strategy, yields

D(0,0,0) <= tP + lambdaP*eP + lambdaQ*eQ.

Therefore max(tP,tQ)>=tP>=D(root)-(lambdaP+lambdaQ)*alpha.

## Exact first-arrival cones and feasible primal mixtures

At baseline Stage99 policy, C is chosen at A; at B immediate Q is selected with probability s99, otherwise C; all other states follow the unique Bellman actions. Full rational forward propagation yields eP=eQ=alpha99, tP=V99, tP>tQ. It preserves the numbers of distinct ordered histories, not just aggregated state probabilities:

A=(9,5,1): 336 first-arrival ordered words, P-mass=875/3538944, Q-mass=875/13436928.
B=(12,0,1): 12 first-arrival ordered words, P-mass=48828125/725594112, Q-mass=48828125/362797056.

When continuing at a critical state and thereafter following Bellman actions, the conditional suffix vector (P-error,Q-error,P-extra-time,Q-extra-time,number of terminal ordered suffixes) is

RA=(17611/3981312, 122033/124416, 191287/165888, 4543/3456, 49),
RB=(63/64,1/144,9/8,13/12,5).

The A and B future cones are disjoint: a path reaching A at time 9 already contains five 0-symbols, while any path reaching B at time 12 has zero 0-symbols; symbol counts cannot decrease, and B cannot reach the earlier-time A.

For any real u in [0,1], at A decide P with probability u and otherwise C; at B decide Q with probability

s(u)=s99+h*u, h=64118999/54400000000,

and otherwise C. All other actions are the unique Bellman minimizers. Put pA,qA,pB,qB equal to the first-arrival masses above and define:

X=pA*RA.Perror=15409625/14089640214528,
Y=qA*(1-RA.Qerror)=2085125/1671768834048,
E=pB*(1-RB.Perror)=48828125/46438023168,
H=qB*RB.Qerror=48828125/52242776064.

Disjointness makes the error responses **exactly affine**:

eP-alpha99 = -X*u + E*(s-s99),
eQ-alpha99 = +Y*u - H*(s-s99).

Because h=(X+Y)/(E+H), both errors are exactly

eP=eQ=alpha99+eta100*u,
eta100=E*h-X=Y-H*h=117732125/808393107308544>0.

All real parameters are feasible since 0<s99<s100=s99+h<1 and

s100=17567190885961211/20889600000000000.

Every used action is a Bellman minimizer, so tP+lambdaP*eP+lambdaQ*eQ=D(root) and tP=V99-Gamma100*eta100*u. The difference tP-tQ is affine and strictly positive at **both endpoints**:

u=0: 1137415722727759775/1862537719238885376,
u=1: 1137198023932879775/1862537719238885376.

Thus tP>tQ for **all real** u in [0,1], and max(tP,tQ)=tP reaches the universal lower bound. This proves the complete real interval, not merely finitely tested values.

## Right sharpness of the support line

Suppose alpha>alpha100 permitted a strategy attaining the same support line. Equality in the positive-multiplier dual bound forces eP=eQ=alpha, tP=max(tP,tQ), and Bellman-minimizing actions at every reached node. There are exactly the two ties A and B. Any history-dependent mixture at each tied count state can be replaced by its P-first-arrival weighted mean, preserving both P and Q quantities because the likelihood ratio is constant within a count fiber and the conditional suffix distributions are identical. The two path cones do not intersect. The equal-error equations then uniquely give s=s99+h*u for some u in [0,1], hence alpha=alpha99+eta100*u<=alpha100, a contradiction. Finite-history randomized strategy spaces are compact, so this is genuine nonattainment of the line.

## Next dual kink, scope and verification

An additional exact affine-gap calculation on the dual pencil lambdaP=72+(8/9)K, decreasing K, proves the next possible policy kink is

K101_dual=61236/47, lambdaP101=57816/47, Gamma101=119052/47,
new tied state A101=(12,6,2), continue/decide P; B continues as C/Q tie.

The calculation constructs the fixed policy at the rational midpoint between K101 and K100 and checks the same 1240 affine action gaps are nonnegative at **both** endpoints. The only endpoint ties are {A100,B} at K100 and {A101,B} at K101; affine dependence rules out an intervening switch. This is **only a dual-pencil candidate**, not proof of Stage101 primal/minimax optimality.

Portable evidence: CHECKER_STAGE100.py, INDEPENDENT_ORDERED100.py, certificate100.json, independent100_certificate.json, and NEXT_TASK_PACKET_101.md in the same directory. The first program exhausts all 680 states and proves exact identities; the second uses a separate bottom-up Bellman and **unaggregated ordered-word DFS** for u=0,1/2,1, with 1,107,826 visited ordered-prefix nodes and 738,551 terminal ordered paths per parameter. Both pass using exact rational arithmetic. They are two author implementations, not independent mathematical review.

The native controller returned CONTROL_QUOTA; its session-start returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false). Current native owner, CLAIM, formal Result and independent review were not established. Ordinary GitHub author-source persistence never substitutes for native admission, and the auxiliary iid proof makes no P000 native-space/BRC claim.
