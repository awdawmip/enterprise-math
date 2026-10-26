# Stage146 — exact full-real affine optimum for finite ternary iid N14

**Evidence class:** AUTHOR COMPUTATION-ASSISTED PROOF; independently structured local calculations, **not** independent Research Driver review or native Result. This is an **external finite iid auxiliary model**, not a native P000/X6/Heartbeat theorem.

## Frozen inputs, model and observer
Global knowledge source: \`awdawmip/chatgpt-global-knowledge main@8a584051572960ae4823296de3397ffaafbb4b11\`. Enterprise Math research input: \`awdawmip/enterprise-math main@f52af9bc69937880cca0d3fa5f97cbe9a79e7194\`. The latest verified predecessor is Stage145, commit \`fa50a1db0997a8cd9e6767a05a1ed19522bcbb1d\`.

Let P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), with all randomized stopping/decision rules on arbitrary *complete ordered ternary prefixes*, stopping by n=14. Set eP=P(decide Q), eQ=Q(decide P), tP=E_P tau, tQ=E_Q tau, and V14(alpha)=min max(tP,tQ) subject to eP,eQ<=alpha. This is exactly a finite-horizon experiment: it neither asserts an infinite-time theorem nor embeds these histories into P000.

The BRC-appropriate carrier is each **labeled ordered prefix** with its separate positive integer P/Q mass weights and branch provenance; the specified observer is M=(eP,eQ,tP,tQ). Count-state compression is justified only for iid suffix Bellman optimization and for effective randomization at a tie with a constant likelihood ratio. It is not an assertion that ordered paths or future provenance coincide.

## Exact theorem

Define
\`\`\`
alpha145=61650988568176660266901/177207634216336528244736
V145=34260854261470059183743591/2835322147461384451915776
eta146=487599068297/2916998094096074539008
alpha146=246603954391193214663775/708830536865346112978944
V146=274086831038532347195394643/22682577179691075615326208
slope146=3426743127131935/4255410050592
\`\`\`
Then **for every real** 0<=delta<=eta146:
\`\`\`
V14(alpha145+delta) = V145 - slope146*delta.
\`\`\`
The supporting affine line is strictly below V14(alpha) for **every alpha>alpha146** (right-end sharpness of this support).

## Universal dual lower bound

For s=(n,a,b), r(s)=Q(prefix)/P(prefix)=2^(a+b)/3^a. Use K=580442338958517/1418470016864, L=52669253445512/132981564081. Define backward H(s) as the min of P-decision K*r(s), Q-decision L, and (for n<14) continuation 1+sum_i P_i H(child_i). A complete exact Fraction evaluation of all 680 states gives:
\`\`\`
Hroot=1064448260606076968085635550307/3642399692121256208464084992
ties: T=(7,1,2), Q/C; U=(8,6,2), P/C
strictly positive alternative gaps: 1238
minimum positive gap: 6129035788073/1378752856391808
negative gaps: 0
\`\`\`
The alternative actions at every other state have a strictly positive gap. Backward induction conditional on each *literal history* (using iid suffix and prefix likelihood ratio) yields for all randomized ordered-history policies:
\`\`\`
Hroot <= tP + L*eP + K*eQ <= max(tP,tQ) + (K+L)*alpha.
\`\`\`
Hence V14(alpha)>=Hroot-(K+L)*alpha universally, with K+L=slope146.

## Original feasible optimizer and complete observation certificate

At T, v is the probability to stop and decide Q, versus continuing. At U, u is the probability to stop and decide P, versus continuing. Else follow the strict Bellman minimizer; notably the old R=(11,2,0) is now **forced P-stop**.

The true ordered cones for T and U are disjoint: depth(T)=7 and depth(U)=8, but the first-symbol count increases from 1 to 6, requiring five such outcomes in one step; the reverse chronological ordering is impossible. Thus mixed randomization contributions vanish exactly.

Independent **integer-weight literal-prefix DFS**, with P branch integer weights (3,1,20)/24 and Q branch weights (1,1,10)/12, gives first-hit inventories under the fixed strict policy:
\`\`\`
T: 70 prefixes; mass P=21875/2985984; Q=21875/1119744
U: 11 prefixes; mass P=11/150994944; Q=11/429981696
\`\`\`
With M=(eP,eQ,tP,tQ), the four deterministic corner values were computed both by backward exact Fraction recursion and the structurally separate literal-prefix integer DFS. They match term by term, and have **exact** affine representation M(v,u)=M00+v*dT+u*dU:
\`\`\`
M00:
304885407585151333/876488338465357824
1163358021173/3343537668096
1324443418302820519/109561042308169728
38903505975665/3343537668096
dT:
1191246875/9393093476352
-1878471875/20061226008576
-377661353125/31701690482688
-44855715625/1671768834048
dU:
-5073079/14427791579676672
117733/213986410758144
-17208257/200385994162176
-627143/17832200896512
mixed M11-M10-M01+M00=(0,0,0,0).
DFS visited nodes for (v,u)=(0,0),(1,0),(0,1),(1,1):
607816, 592066, 606232, 590482.
\`\`\`

Balance eP=eQ to obtain exactly
\`\`\`
v(u)=245752551670737/579687950800000
    +(9485087007/2318751803200000)*u.
\`\`\`
For every real u in [0,1] both coins are admissible: 0<v(u)<1. At u=0 the balanced policy matches the Stage145 endpoint *exactly*. At u=1,
\`\`\`
v_end=28086276907713/66250051520000  (strictly inside (0,1))
eP=eQ=alpha146
tP=V146
tP-tQ=386046490754488341010345/840095451099669467234304 >0
\`\`\`
and at u=0:
\`\`\`
tP-tQ=434302292346744026388749/945107382487128150638592 >0.
\`\`\`
Because the four observables are affine, both errors stay equal and grow strictly from alpha145 to alpha146; tP remains the larger expectation throughout. The endpoint dual equalities tP+L*eP+K*eQ=Hroot hold exactly; by affinity they hold for every real u. This attains the lower bound and proves the theorem.

## Strict right-end sharpness

Suppose alpha>alpha146 and an optimal policy attained the same affine support. The policy space is a finite product of probability simplices (or its compact occupancy-measure image); an optimum exists. K,L>0 and equality in the two-step dual chain require **both errors to equal alpha** and only Bellman-minimizing actions at every positive-mass prefix. Exactly two nontrivial tie states remain, T and U. Every literal prefix reaching a given count tie has the same likelihood ratio Q/P, so arbitrary history-dependent tie coins have the same four-observer effect as a single effective coin for each state. Their cones are disjoint, giving the exact affine M above. The error balance forces v=v(u), 0<=u<=1. The common error is strictly increasing in u, hence cannot exceed alpha146. This contradicts eP=eQ=alpha>alpha146. Thus the support is strictly below V14 for every alpha>alpha146.

## Verification scope and continuation

Local author computations executed:
- Full exact Fraction Bellman 680 states, all 1238 non-selected strictly positive action gaps.
- Exact Fraction backward four-observer recursion for all 4 deterministic corners.
- Independent positive integer-weight forward ordered-prefix DFS (4 corners), including first-hit counts/masses and mixed-term zero.
- Endpoint equalities, monotonic common error, positive tP-tQ and dual equality.

The checked portable source is \`VERIFY_STAGE146.py\`; raw local extended checker output and evidence were also retained for the author's work. GitHub storage/readback **is not remote execution**, and no clean-independent Research Driver or native Owner/CLAIM/Result was obtained; the gateway's direct native control read returned CONTROL_QUOTA and session_start returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false). The external iid result is not promoted to P000-native space.

A separate exact author dual-ray scan identifies Stage147 candidate K=488636304489/1197470344, L=59157759848/149683793, with tie T=(7,1,2) Q/C and new tie W=(10,4,1) P/C. Stage147 primal interval remains **OPEN**. See DUAL_CANDIDATE_147.json and NEXT_TASK_PACKET_147.md.
