# Enterprise Math R1 — N4 partial-compression common TV minimax and strict subadditivity

2026-10-28 Asia/Shanghai. Status: AUTHOR_EXACT_PROOF / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED. Research is portable author-side; no native CLAIM or independent mathematical admission is asserted.

Source pins: GLOBAL_KNOWLEDGE_V1 main@6b3e7a6520898c41e063db04e82b1d3c2c9c3a4b (verified); Enterprise Math main@d42136a33bab42ab25e6d4318774708be2544d62 (verified). Parent source is research_notes/brc_n4_exact_common_tv_minimax_7over380_20261028_r1t11/PROOF.md. Exact self-contained verifier and stdout are this directory's VERIFY.py and RESULT.json.

## The frozen finite tree, scopes, and question

This is an EXTERNAL dual-law, four-time sequential finite probability model, not a proved dynamic law of native X6 Cells. Q masses q(h)>0, likelihood ratios r(h)=P(h)/Q(h)>0, ordered history h, and separately typed decision times t=1,2,3,4. Local actions are STOP P, STOP Q, CONTINUE; at t4 stopping is mandatory. Randomized policies employ fresh independent random decisions at each (t,r); no persistent shared random seed. Readout is both laws' complete joint distributions of (T,D), eight events ordered (1,P),(1,Q),...,(4,P),(4,Q).

At t1: A=(q=1/2,r=1/2), B=(1/2,3/2). At t2: AU=(1/6,1), AV=(1/3,1/4), BU=(1/4,1), BV=(1/4,2), with obvious parents. Each t2 parent h has two equal-Q-mass t3 children h0,h1 with likelihood ratios r(h)(1-e_h), r(h)(1+e_h): e_AU=1/10, e_AV=0, e_BU=4/5, e_BV=0. Each t3 parent also has equal-Q-mass children at t4 and ratios r(h)(1±e_h), with e_AV0=0, e_AV1=3/50, all other e_h=1/20. Both P and Q masses conserve at every parent. All 2,4,8,16 prefixes are strictly positive.

The fixed full-history policy F continues all at t1; at t2 AU and BV STOP P, AV and BU CONTINUE; at t3 AV0 and BU0 STOP Q, BU1 STOP P, AV1 CONTINUE, other reachable nodes STOP P; at t4 choose Q when 100r<2501/100 and P otherwise. Its exact ordered observations are:
Q=(0,0,5/12,0,1/8,7/24,1/12,1/12)
P=(0,0,2/3,0,9/40,1/15,53/2400,47/2400).

Let S2 constrain equal (t,r) histories to the same local action at t2 only, S3 constrain t3 only, S23 constrain both. At t1 and t4 all classes retain (t,r) actions. The other of t2/t3 may use ordered history when unconstrained. For I=2,3,23 define d_I=inf over sigma in S_I of max(TV_Q(Law^F(T,D),Law^sigma(T,D)),TV_P(...)).

**THEOREM (this fixed F and tree):**
d2=7/380, d3=1/2000, d23=7/380, hence d2+d3-d23=1/2000>0.

This is strict subadditivity for the actual COMMON TOTAL VARIATION minimax of valid behavioral strategies, not merely for a signed linear objective. In this example compressing t2 entirely masks the extra optimal cost of compressing t3, while compressing t3 alone costs strictly more than zero.

## Matching feasible primal witnesses

Witness sigma2 belongs to BOTH S2 and S23. At t1 always CONTINUE. At t2 both AU,BU with r=1 use (P,Q,C)=(2/5,0,3/5); AV continues and BV stops P. At t3 the shared action by r is: 9/10 -> (7/19,0,12/19); 11/10 -> P; 1/4 -> (0,13/20,7/20); 1/5 -> Q; 9/5 or 2 -> P. At t4 r=189/200 or 1/4 -> Q, all other ratios -> P. Direct exact tree transport gives
sigma2-Q=(0,0,5/12,0,109/760,7/24,169/2280,169/2280)
sigma2-P=(0,0,2/3,0,157/760,83/1200,337/12000,6727/228000).
Subtract F componentwise; TV_Q=TV_P=7/380. So d2,d23 <=7/380.

NEW witness sigma3 belongs to S3: at t1 and t2 use F. At t3 both AV0 and AV1, same r=1/4, select (STOP P,STOP Q,CONTINUE)=(0,1/2,1/2); BU0 STOP Q, BU1 STOP P, other reachable histories STOP P. At t4 all nodes with r=1/4 use (253/500,247/500,0), r=47/200 uses Q, all other r use P. All decisions are legal immediate behavioral randomizations. t<=3 observation laws remain identical to F; t4 Q=(503/6000,497/6000), P=(259/12000,241/12000), versus F t4 Q=(500/6000,500/6000), P=(265/12000,235/12000). Both TV values equal 1/2000. Thus d3<=1/2000.

## Exact dual/Bellman lower bounds

Write wQ,wP as bounded scores on the eight (T,D) events and L_w(policy)=E_Q[wQ]+E_P[wP]. For any sigma,
|L_w(sigma)-L_w(F)|<=osc(wQ)*TV_Q+osc(wP)*TV_P.
At a Q-mass unit of node with ratio r, the cost of decision a in {P,Q} is c(t,r,a)=wQ(t,a)+r*wP(t,a). At t4 choose the minimal of c_P,c_Q as a function of r. At t3, for each allowed signature group, take the minimum across immediate P, immediate Q, or Q-weighted continuation to optimally terminated t4 children. At t1,t2 enumerate all deterministic prefix actions; later minimizations by grouped Bellman are exact.

For S2, reuse but INDEPENDENTLY REMINIMIZE on the larger S2 class the integer pair
w2Q=(0,0,3,45,45,-45,-45,-45),
w2P=(0,0,-29,50,-50,50,50,50).
Their oscillations are 90 and 100. F scores -467/12. Enumerating t1 A/B actions 3^2, t2 common U={AU,BU}, AV,BV actions 3^3, 243 prefixes, then t3 node-specific minima (BV0/BV1 share r and continuation kernel so may choose the same minimizing action), yields the following row-A/column-B best score grid:
A=P: (B=P:0, B=Q:0, B=C:-95/4).
A=Q: (B=P:0, B=Q:0, B=C:-95/4).
A=C: (B=P:-91/6, B=Q:-91/6, B=C:-425/12).
Therefore min_{sigma in S2} L_w2(sigma)=-425/12 and the gap is 7/2. Consequently 90 TV_Q+100 TV_P >=7/2, implying d2>=7/380. In particular this is not an illegitimate inference from an earlier S23 lower bound.

For S3, a NEW rational dual certificate is
w3Q=(1/10,1/10,169/1750,1/10,374/3875,-11/125,1/10,-1/10),
w3P=(2/5,2/5,-697/1750,2/5,-617/1550,17/50,-2/5,2/5).
Their exact oscillations are 1/5 and 4/5. L_w3(F)=-859/2800. At t2 AU,AV,BU,BV can be controlled individually; at t3 the shared AV0/AV1 signature (r=1/4) must have its Q masses accumulated BEFORE minimizing over P/Q/C, similarly BV0/BV1 share their ratio. t1 has 3^2 and t2 has 3^4 choices: 729 exact prefix combinations. The best row-A/column-B t1 score grid is:
A=P: (B=P:1/2, B=Q:1/2, B=C:-21/200).
A=Q: (B=P:1/2, B=Q:1/2, B=C:-21/200).
A=C: (B=P:2091/7000, B=Q:2091/7000, B=C:-268/875).
Thus min_{sigma in S3} L_w3(sigma)=-268/875 and the gap -268/875+859/2800=1/2000. The oscillations sum to 1, so d3>=1/2000.

**Completeness over ALL allowed real randomized strategies:** Fixing every signature's other action simplex, L_w is affine in one remaining signature's P/Q/C mixture; every trajectory visits a signature at most once since t belongs to it. Even when multiple histories share a signature at the same time, their path contributions combine linearly rather than with powers of the same local probability. Successively replacing every mixture by a non-increasing-cost deterministic vertex proves a deterministic strategy attains the global LINEAR SCORE minimum. Enumerated 243/729 prefixes and exact groupwise continuation costs exhaust these vertices. Terminal nodes at equal ratio have equal immediate costs, so a common argmin is legal. Hence both dual inequalities hold for every valid real behavioral strategy, not just for a relaxation or a finite sampled subset.

Now S23 subset S2 gives d23>=d2=7/380, while sigma2 belongs S23 gives d23<=7/380. Combining all bounds proves the theorem.

## Computational evidence, BRC reuse, and native semantics

VERIFY.py uses only Python Fraction exact rational arithmetic to reconstruct tree weights, check 2/4/8/16 positive nodes, P and Q parent conservation, equality of compressed signatures, both primal distributions, both total variation norms, both oscillation-weighted dual objective gaps, 243 and 729 Bellman prefix cases and every exact root table entry. RESULT.json records actual executable output, with status PASS_EXACT_FRACTION_N4_PARTIAL_TV_STRICT_SUBADD. Finite testing pertains to the declared finite tree; quantification over real behavioral probabilities relies on the algebraic multi-affinity argument. Not Lean formally checked, not independently reviewed, not admitted.

Applied typed BRC primitives: positive rational masses, ordered provenance, likelihood ratios, tagged future kernels, and full TWO-LAW joint terminal readout. Equal likelihood ratios do not imply equal future transition kernels. This example exhibits exact partial masking of nonzero residual observation costs. Source P000 assumes the native Heartbeat World with six discrete spatial Cell axes and separately typed time, and permits neither native planes nor unsourced information-erasing quotient. The present outside probability tree has NO established embedding into native X6 Cell states, rotation/transition dynamics, or an observer/future-operation fidelity theorem. Neither an X6 physical result nor a challenge to P000 is claimed.

Next research unit: same fixed N4 tree, vary full-history F' to classify whether d23(F')=d2(F') persists and whether some F' yields d2(F')<d23(F')<d2(F')+d3(F'). Maintain fully exact behavioral primal/dual certificates and leave native X6 lift separate.
