# R5: Exact facet/Bellman gate for a ternary single-collision BRC observer

2026-10-27 | Author-side proof + exact rational verification. Independent Driver review, native Task CLAIM/Result and mathematical admission: NOT OBTAINED.

## Frozen sources and scope

Global input GLOBAL_KNOWLEDGE_V1: awdawmip/chatgpt-global-knowledge main@bef297775ae755ce23dad58f2a1bd392f08278cc (00_BOOTSTRAP, OPERATING_MANUAL, Enterprise Math project router, original P000 V4, ACTIVE worldview, TASK route, math/code policies). Project input: awdawmip/enterprise-math main@8e9c6ec65632404dd596c69f9d8329d7841f0218 (AGENTS, PORTABLE_RESEARCH_PROTOCOL, ACTIVE native X6/residual/joint contracts). Reuses the R5 finite-horizon occupation coupling result at 39f1cd95b3f322ef2c555fea578a22405b105f19, especially its next task's convex-hull gate.

Type: EXTERNAL finite two-measure rational observation tree. T0_BRC REUSE_APPLIED to ordered positive P/Q branch masses, conservation, physical history labels and provenance-aware LR readout. This is not a native Heartbeat-world evolution computation: native spatial X6 has six discrete axes, separately typed time and a three-dimensional research slice; no native plane. We have not derived a Cell/X6-to-statistical-tree dynamics/readout-preservation bridge. Python Fraction is exact for the external probability tree but not an executed native BRC-Shor arithmetic engine.

Four observables at stopping: O=(P(decide Q), Q(decide P), E_P[tau], E_Q[tau]). A full-history behavioral policy chooses stop P, stop Q or continue at each distinct physical nonterminal history; a seedless time/LR behavioral policy must use the same distribution at every (t,r), with independent fresh local randomization and without a persistent root seed.

## Theorem A: exact convex-hull facet/Bellman gate

Let U be the finite set of four-vectors from all deterministic full-history policies and W the finite set from deterministic seedless time/LR policy tables on any finite strictly positive rational P/Q observation tree. Then:

(1) O_full = conv(U), and conv(O_seedless) = conv(W) subset O_full. The seedless behavioral image itself need not be convex.

(2) For EVERY signed lambda in R^4, the respective minimum lambda dot O over either behavioral class equals the minimum over its deterministic action tables.

(3) Consequently equality of all signed supports for the two behavioral classes is equivalent to conv(U)=conv(W). If conv(W) has dimension four, exact full-history Bellman minima against each rational facet normal lambda_k of conv(W), oriented as lambda_k dot x >= b_k, decide hull equality: the two hulls are equal iff min_full(lambda_k dot O)>=b_k for every facet. If conv(W) has lower affine dimension, include both orientations of a rational basis of its affine-hull equations. Any failed facet supplies a finite exact rational separation certificate; after clearing denominators lambda can be integral.

Proof: every seedless trajectory visits a (t,r) class at most once, because time strictly increases. Independently presampling an action at each such class therefore induces exactly the same terminal distribution as fresh behavioral randomization for that class; thus each seedless behavioral O is a convex combination of deterministic class-action tables. Conversely all deterministic seedless tables are behavioral strategies. For full histories, joint occupation masses satisfy finite linear flow constraints; the convex mixture of two full strategies can be reconstructed behaviorally by Q-mass-weighting their action probabilities at each REACHED history, with arbitrary actions at unreachable histories. Because P(h)=r(h)Q(h), this reconstructs the four observables under both P and Q. Hence O_full is convex; it contains all deterministic full vectors and itself lies in their convex hull by independent presampling, giving equality. Linear optimization over conv(U) and conv(W) attains a deterministic minimum. Finite rational polytopes are intersections of finitely many rational facets and affine-hull equations; a full-history Bellman recursion takes the min of stop P, stop Q and child continuation costs at every actual history. Checking all compressed-hull inequalities and the automatically valid reverse inclusion completes the equivalence. QED.

This gate intentionally does NOT infer the image equality O_seedless=O_full from convex-hull equality; that is the remaining real-algebraic question.

## Theorem B: eight positive rational leaves; exact genuine facet gap

Root has Q=1, r=P/Q=1. Internal history table:

| history | t | Q(h) | r(h) |
|:--|--:|--:|--:|
| a |1|1/2|3/2|
| b |1|1/2|1/2|
| ax |2|1/4|1|
| ay |2|1/4|2|
| bu |2|1/8|1|
| bv |2|3/8|1/3|

At ax, terminal LR values y=(1/2,1,3/2) have conditional Q=(1/3,1/3,1/3). At bu, the same three terminal y have conditional Q=(1/6,2/3,1/6). At ay and bv a sole terminal child preserves the parent's LR. At every node define P=Q*r. All eight leaves are strictly positive; P and Q are individually conserved at each parent and normalized to 1. The sole nonterminal coalescence of distinct histories into the same time/LR is ax~bu at time 2 with r=1.

Use the signed functional

J=298 e_P +375 e_Q +37 E_P[tau] -17 E_Q[tau].

Exact result: min_full J=280, min_seedless J=281; gap=1.

Local mechanism: at time 2 and r=1 the better immediate decision is Q, costing 298 per unit Q mass in classification loss. Terminal optimal loss in a three-point kernel K_s=(s,1-2s,s) is

H(s)=149s+298(1-2s)+375s=298-72s.

One extra observation contributes (37*r-17)=20; thus the continue-minus-stop difference at this collision equals 20-72s. At ax (s=1/3) it equals -4; at bu (s=1/6) it equals +8. Full history can continue at ax and stop/decide Q at bu. A compressed common action at r=1 cannot separate them. When both are reached the net difference is (1/4)*(-4)+(1/8)*(+8)=0, although the full-history policy exploits the opposite signs. This is a difference in observer action values, NOT cancellation of positive BRC physical branch mass.

One full optimal deterministic strategy: continue at root, a, b and ax; stop/decide P at ay; stop/decide Q at bu; continue at bv. Terminal action: decide Q at LR 1/2, 1 or 1/3, and decide P at LR 3/2. Its exact observation vector is

O_F=(3/8,1/3,19/8,21/8), and J(O_F)=280.

Full-history Bellman recursion confirms global minimality 280 for any real behavioral strategy. Independently, the exact verifier exhausts 3^6*2^5 = 23,328 deterministic seedless time/LR action tables and finds 326 distinct four-vectors. The smallest J is exactly 281. It is attained by exactly four distinct four-vectors:

O_1=(3/8,1/3,2,7/4)
O_2=(1/4,1/2,11/8,15/8)
O_3=(1/2,1/4,17/8,19/8)
O_4=(11/32,17/48,5/2,11/4).

Their differences against O_1 have exact rational matrix rank 3. Five other compressed four-vectors have affine rank 4. Thus J>=281 supports a three-dimensional face of a four-dimensional compressed convex polytope: this is a genuine facet, not an accidental one-sided test. Since J(O_F)=280, O_F lies strictly outside conv(O_seedless). The exact enumeration is exhaustive in a declared finite deterministic domain; Theorem A upgrades the minimum statement to all REAL seedless local randomizations. QED.

## Theorem C: open rational model family uniformly excluded

Keep the internal table and singleton terminals, replacing only the ax and bu kernels by K_{s_a} and K_{s_b} for arbitrary real parameters 0<s_a,s_b<1/2, where K_s=(s,1-2s,s) on y=(1/2,1,3/2). Q and P conservation holds because E_{K_s}(Y)=1. Let V_c and V_f be the seedless and full minima of J.

For every admissible pair,

V_c(s_a,s_b)-V_f(s_a,s_b)
>= 1 -36|s_a-1/3| -18|s_b-1/6|.

Hence if |s_a-1/3|<=1/100 and |s_b-1/6|<=1/100, the gap is >=23/50 >0 for ALL REAL parameter values, and in particular for all rational such values.

Proof: in minimizing J, both classes may take the same fixed Bayes-optimal terminal action at each terminal LR because error coefficients 298 and 375 are positive and terminal decisions do not change time. Hence for any fixed nonterminal behavioral policy the ONLY parameter dependence is -72(s_a c_a+s_b c_b), where c_a,c_b are actual Q masses continued from ax and bu. They satisfy 0<=c_a<=1/4 and 0<=c_b<=1/8. Every fixed-policy J is therefore Lipschitz in the two parameters with bound 18|delta_a|+9|delta_b|. Minimizing over an unchanged strategy space preserves this uniform bound for V_c and V_f. Their difference can shrink from its base gap 1 by no more than twice this amount, proving the displayed inequality. At radius 1/100 the lower bound is 1-36/100-18/100=23/50; positivity of every leaf is preserved. QED.

## Reproducibility, provenance and limits

VERIFY.py is an actual locally executed Python 3 standard-library Fraction verifier, with its EXACT stdout stored in EXACT_OUTPUT.txt. It verifies all 15 node masses, eight positive leaves, every exact P and Q flow identity, both collision kernels, 23,328 seedless action tables, all 326 unique vectors, the facet rank and 4D affine rank, and the independent full-history Bellman minimum and witness. All-real behavioral statements follow from Theorem A and Bellman theory, not random samples; the parameter-neighborhood statement follows from the displayed analytic proof.

Background literature: Kuhn's perfect-recall mixed/behavioral equivalence, e.g. https://arxiv.org/abs/1408.1022; Main and Randour's finite-memory randomization distinctions (2022), https://arxiv.org/abs/2201.10825. These are context, not asserted independent validation or evidence of worldwide novelty.

The stronger mother problem -- identical all-signed support functions but unequal real behavioral four-images -- remains OPEN. The present strictly positive ternary one-collision family FAILS the necessary hull gate. No independent Driver mathematical review, official Result/CLAIM, P000 physical derivation or native X6/Heartbeat experimental verification is claimed.

