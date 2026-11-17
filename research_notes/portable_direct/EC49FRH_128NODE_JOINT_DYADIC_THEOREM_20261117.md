# EC49FRH: 12 exact native BRC seams, 128-node enclosure and joint dyadic budget theorem

Date: 2026-11-17. Author state: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. This is an independent portable research result, not a formal TASK CLAIM, Result, Review or P000 change. Parent: [EC49FRG PR #2614](https://github.com/awdawmip/enterprise-math/pull/2614), scientific pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` (unchanged).

## Precise frozen BRC model
Class 16943: 310 raw configurations, 141 complete *named* profile states, 144 terminal observations and 84 named root observations = 228 physical actions. Prior is p_i(lambda)=(1-lambda)/141+lambda*m_i/310, sum_i m_i=310, 0<=lambda<=1. Root observation cost is xt, terminal observation cost is t>0, x>=1. V(x,lambda) is the minimum expected cost over all adaptive separating decision trees. Frozen master SHA256: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; profile CSV SHA256: `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`.

The inherited three feasible fixed-tree costs (divided by t) are
A=(1-lambda)(6x+290)/141+lambda(6x+751)/310;
B=(1-lambda)(5x+293)/141+lambda(5x+704)/310;
C=(1-lambda)(5x+295)/141+lambda(5x+685)/310.
Let K(x)=7557-169x, G(x)=310(3-x)/K(x), beta=620/3299.

## New exact Bellman computations
All 12 new critical points lambda=G(x) were computed by original integer Bellman DP and a separately implemented integer weighted-subset DP. Both examined the full 141-state/228-action physical problem; the 4 tied first-action trees were fully replayed. At every critical point the complete interpolated optimum first-action set is exactly {32,34,140,142}. Weighted Bellman totals below are normalized-cost times (denominator x)*310*141*(denominator lambda), as integers.

| Price x | lambda=G(x) | Bellman integer optimum | raw JSON SHA256 |
|---|---|---:|---|
|91/32|310/45289|138083037120|`3a215c48b520c12261c36e09132011a7d6863f1e2280d74a39dbe587ab99e40a`|
|271/96|5270/679673|6215087833920|`52d3883189777d6d7e22946d6eea9b57609e6b906d5d0d85044142d7fdeec553`|
|269/96|5890/680011|6216438997440|`51fac82cdbb7ec464fb4c57e872b6b760bc58c2d824d9757f9c1afc20144b1ca`|
|89/32|2170/226783|690865573440|`285eb4521282b76223819c63c1380b6399b82ea5d235cdb740fa055b52a3e5b9`|
|265/96|7130/680687|6219141324480|`6d815153def76f86f09121b093e07aac22141617f35db3027c3567b15c94d945`|
|263/96|310/27241|248819699520|`817260b2e156aa446cb017d3fce7a9b89fd38cdf2f5d20ae19bab6a7a7598029`|
|87/32|930/75707|230438653760|`f255a7797c413d82aea1b30bfce301159a7453c49a806992852a94ca31aacd78`|
|259/96|8990/681701|6223194815040|`747d1878fde37a185bf205fb69f12ea865367cd89846db21a23db6030becdbe7`|
|257/96|9610/682039|6224545978560|`78debda7f742c00cac0598d51bea1aa84aa164a0120b66f3bc7ca16ded20c20a`|
|85/32|3410/227459|691766349120|`8d82a552920b332ec0f9e285a5717c928ef561474c75eb4dab4100e871943ebe`|
|253/96|2170/136543|1245449661120|`cb54d05fb1d8e5824115a6152780865554a55cdf6ca75682932c192008fe237c`|
|251/96|11470/683053|6228599469120|`42917c5c9827aa832322e685946df433f1b30f272b3ed8855b91ca18861165be`|

At each newly sampled x, the claim that V/t=min(A,B,C) for **all** real lambda in [0,1], with first-action changes {32,34}->{140,142}->{16,23}, uses the inherited exact endpoint certificates and named-first-action exclusion lemma, plus affine prior cost and Bellman concavity. New critical-anchor Bellman computations alone do not establish that full statement without the inherited hypotheses.

## New theorem: dyadic budget simultaneously minimizes area enclosure and maximal regret enclosure
Fix any finite initial price grid P in [1,3] with certified endpoint observations. Allow exactly m>=0 further nodes, where each node must be an *arithmetic midpoint* of a current interval [a,b]. For a<b define
U(a,b)=(b-a)(G(a)-G(b))=2185500*(b-a)^2/(K(a)K(b)),
R(a,b)=50*(b-a)/(sqrt(K(a))+sqrt(K(b)))^2.
U is the bound on the uncertified parameter-strip area, R is the inherited intervalwise candidate-strategy regret bound (units t), not observed error. In this dyadic-only model, choosing at each step the current interval with maximal K(a)/K(b) *simultaneously* minimizes sum U over all final intervals and minimizes max R over final intervals, among **every valid refinement of m new nodes**. Ties may yield multiple minimizers.

Proof: set u=K(a), v=K(b), r=u/v>1. As b-a=(u-v)/169,
U=(2185500/169^2)*(r+r^{-1}-2),
R=(50/169)*(sqrt(r)-1)/(sqrt(r)+1).
Both strictly increase with r. The ratio-priority algorithm is therefore simultaneously maximum-U and maximum-R. For h=(a+b)/2, K(h)=(u+v)/2, and direct rational algebra gives U(a,h)+U(h,b)=U(a,b)/2. The total area improvement from splitting a node I is U(I)/2. Every descendant's reward is strictly below the ancestor's reward: the children have positive U and sum to U(parent)/2. The m largest rewards in the infinite dyadic forest are automatically ancestor-closed; they are exactly the m nodes selected by greedy max-U, up to ties. Any legal m-node refinement is another ancestor-closed selection of m rewards, proving minimum sum U.

For regret, every proper dyadic child J of I satisfies 1<K(left_J)/K(right_J)<K(left_I)/K(right_I); hence R(J)<R(I), and the weights tend to zero down any dyadic infinite path. For any threshold z>0, all dyadic nodes with R>z must have been split by *every* final partition with maximum leaf R<=z; this finite set is ancestor-closed. Greedy max-R splits all such forced nodes before any node with R<=z. Therefore if any m-split refinement reaches threshold z, greedy also reaches it within m splits. Use the optimal attainable threshold to conclude minimax optimality. QED.

This extends the previous dyadic-area theorem to a separate minimax regret objective and proves simultaneous optimality for any finite dyadic budget. It does not claim unrestricted continuous/rational-grid optimality.

## Exact new continuous-parameter certificate
The 12 midpoint insertions in greedy order are
91/32,271/96,269/96,89/32,265/96,263/96,87/32,259/96,257/96,85/32,253/96,251/96.
The inherited 116 certified price nodes become 128, leaving 127 uncertified strips. Exact sums of the analytic enclosure:
S116=353039202146480393615/236644210143071463572064;
S128=328238036058866176955/238057456560501514334688;
S116-S128=13113000/116005288213.

Consequently the certified proportion of the [1,3]x[0,1] parameter rectangle is >= 1-S128/2 = 99.931059072712673974... percent. Under the inherited endpoint-to-continuum and outside-[1,3] comparison bounds, for all x>=1, lambda in [0,1]:
0<=t*min(A,B,C)-V(x,lambda)<0.000036582279225540488*t.
The unique largest interval *bound* among the 127 is [31/12,125/48], versus the former [17/6,137/48]. The bound falls from 0.000036800695366496801t to 0.000036582279225540488t (about 0.59351%). Every interval radical was enclosed outward using exact integer isqrt at scale 10^38; the winner's certified lower bound exceeds all others' certified upper bounds. The general bound is conditional on the previously established continuum enclosure lemma and the inherited exact 116-node endpoint proof.

## Reproduction and next question
Native program: EC49FQL_ALL_FIRST_BELLMAN.py with frozen master and profile. Independent program: EC49FRH_INDEPENDENT_VERIFY.py reconstructs all 228 physical observations, independently solves the integer weighted-subset Bellman and replays four tied first-action trees. Exact geometry: EC49FRH_GEOMETRY.py, its 128-node plan and numerical result. The independent checker was corrected to permit a subset without an admissible two-step separating tree (no invalid universal two-step existence assertion); all 12 independent checks passed. Full raw certificate JSON, independent code/logs, frozen inputs and the inherited complete parent archive are in accompanying local self-contained evidence, each item SHA256-indexed. Raw archive is **not claimed** to be a GitHub blob.

Open goal: establish a uniform parameterized Bellman lower bound on the remaining 127 strips, or exhibit an exact named-action decision tree Q satisfying F_Q(x,lambda)<min(A,B,C) at an explicit rational point. For the policy seam lambda=G(x), a fixed-tree competitor gap multiplied by K(x) is quadratic in x; turning this into a simultaneous all-tree certificate remains unresolved.

No formal research admission, CLAIM, Result, or Activity checkpoint is asserted by this publication.